"""Seams for writing-for-humans measure-only linter."""

from __future__ import annotations

import importlib.util
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    REPO_ROOT
    / "skills"
    / "writing-for-humans"
    / "scripts"
    / "writing_for_humans_linter.py"
)


def _load():
    spec = importlib.util.spec_from_file_location("writing_for_humans_linter", SCRIPT)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules["writing_for_humans_linter"] = mod
    spec.loader.exec_module(mod)
    return mod


lint = _load()


class WritingForHumansLinterTests(unittest.TestCase):
    def test_soft_threshold_is_advisory_budget_zero(self):
        # Exactly 21 words; function words break noun-cluster runs.
        text = (
            "It is time to run the job and then to save the log and then to "
            "exit the app now here."
        )
        self.assertEqual(lint.word_count(text), 21)
        report = lint.analyze(text)
        self.assertEqual(report["summary"]["revision_budget"], 0)
        self.assertFalse(report["summary"]["material_review_needed"])
        self.assertEqual(report["agent_summary"]["recommendation"], "STOP")
        kinds = {(f["kind"], f["severity"]) for f in report["findings"]}
        self.assertIn(("sentence_length", "advisory"), kinds)
        self.assertFalse(any(f["kind"] == "noun_cluster" for f in report["findings"]))

    def test_hard_threshold_sets_revision_budget_one(self):
        words = [f"w{i}" for i in range(31)]
        text = " ".join(words) + "."
        self.assertEqual(lint.word_count(text), 31)
        report = lint.analyze(text)
        self.assertGreater(report["summary"]["max_sentence_words"], 30)
        self.assertTrue(report["summary"]["material_review_needed"])
        self.assertEqual(report["summary"]["revision_budget"], 1)
        self.assertEqual(report["agent_summary"]["recommendation"], "REVISE_ONCE")
        self.assertIn("sentence_length", report["agent_summary"]["material_kinds"])

    def test_filler_and_indirect_are_advisory(self):
        text = (
            "In order to start the service, configuration should be performed "
            "on the host."
        )
        report = lint.analyze(text)
        kinds = {f["kind"] for f in report["findings"] if f["severity"] != "info"}
        self.assertIn("filler_connector", kinds)
        self.assertIn("indirect_instruction", kinds)
        self.assertNotIn("passive_heuristic", kinds)
        self.assertEqual(report["summary"]["revision_budget"], 0)
        self.assertEqual(report["agent_summary"]["recommendation"], "STOP")

    def test_noun_cluster_is_advisory_not_budget(self):
        text = "Set the system configuration parameter value now."
        report = lint.analyze(text)
        self.assertTrue(
            any(
                f["kind"] == "noun_cluster" and f["severity"] == "advisory"
                for f in report["findings"]
            )
        )
        self.assertEqual(report["summary"]["revision_budget"], 0)
        self.assertEqual(report["agent_summary"]["recommendation"], "STOP")

    def test_phrase_match_uses_word_boundaries(self):
        text = "This is to beaumaris harbor for the ferry."
        report = lint.analyze(text)
        self.assertFalse(
            any(f["kind"] == "indirect_instruction" for f in report["findings"])
        )

    def test_urls_excluded_from_noun_cluster(self):
        text = "See https://example.com/path/to/resource for details now."
        report = lint.analyze(text)
        self.assertFalse(any(f["kind"] == "noun_cluster" for f in report["findings"]))

    def test_paths_and_identifiers_excluded(self):
        text = "Open skills/writing-for-humans/scripts/tool.py and call parse_json_value."
        report = lint.analyze(text)
        self.assertFalse(any(f["kind"] == "noun_cluster" for f in report["findings"]))

    def test_code_fences_excluded_from_word_metrics(self):
        text = (
            "Run the health check.\n\n"
            "```bash\n"
            "curl -fsS http://localhost:8080/health due to the fact that unused\n"
            "```\n"
        )
        report = lint.analyze(text)
        joined = " ".join(s["text"] for s in report["sentences"])
        self.assertNotIn("due to the fact that", joined.lower())
        self.assertFalse(
            any(f["kind"] == "filler_connector" for f in report["findings"])
        )

    def test_agent_summary_omits_full_sentence_dumps(self):
        text = " ".join(f"w{i}" for i in range(31)) + "."
        report = lint.analyze(text)
        summary = report["agent_summary"]
        blob = json.dumps(summary)
        self.assertNotIn(text.rstrip("."), blob)
        self.assertIn("recommendation", summary)
        self.assertIn("top_material", summary)

    def test_cli_json_stdout(self):
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as fh:
            fh.write("Verify the service is active.\n")
            path = fh.name
        try:
            buf = io.StringIO()
            with redirect_stdout(buf):
                code = lint.main([path])
            self.assertEqual(code, 0)
            report = json.loads(buf.getvalue())
            self.assertIn("revision_budget", report["summary"])
            self.assertIn("agent_summary", report)
            self.assertEqual(report["tool"], "writing_for_humans_linter")
            self.assertEqual(report["agent_summary"]["recommendation"], "STOP")
        finally:
            Path(path).unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
