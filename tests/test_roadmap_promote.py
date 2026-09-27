"""Seams for roadmap promote scripts (ensure / append / mark)."""

from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / "skills" / "roadmap" / "scripts"

VALID_ENTRY = """## Sample Capability

**Domain:** `testing`

**Intent**  
Prove append + validate.

**Scope**
- One entry

**Boundaries**
- Not a sprint plan
"""


def _load(name: str):
    path = SCRIPTS / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


ensure_header = _load("ensure_header")
append_entry = _load("append_entry")
mark_promoted = _load("mark_promoted")


class RoadmapScriptTests(unittest.TestCase):
    def test_github_anchor(self):
        self.assertEqual(
            append_entry.github_anchor("Durable Debug and Regression Knowledge"),
            "durable-debug-and-regression-knowledge",
        )

    def test_ensure_creates_header(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "ROADMAP.md"
            status = ensure_header.ensure(path)
            self.assertEqual(status, "created")
            text = path.read_text(encoding="utf-8")
            self.assertIn("# Roadmap", text)
            self.assertIn("## Conventions", text)
            self.assertIn("<!-- Entries append below this rule.", text)
            # Blank entry shape lives in template after the comment — not in ledger
            self.assertNotIn("## <Idea title>", text)
            self.assertEqual(ensure_header.ensure(path), "exists")

    def test_append_requires_fields_and_rejects_filler(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "ROADMAP.md"
            ensure_header.ensure(path)
            anchor = append_entry.append_entry(path, VALID_ENTRY)
            self.assertEqual(anchor, "sample-capability")
            self.assertIn("## Sample Capability", path.read_text(encoding="utf-8"))
            with self.assertRaises(ValueError):
                append_entry.append_entry(path, VALID_ENTRY)
            bad = VALID_ENTRY + "\n**Open Questions**\n- None.\n"
            with self.assertRaises(ValueError):
                append_entry.append_entry(
                    path,
                    bad.replace("## Sample Capability", "## Other"),
                )

    def test_mark_promoted_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            scratch = Path(tmp) / "idea.md"
            scratch.write_text("# Title\n\n## Idea\n\nhi\n", encoding="utf-8")
            self.assertEqual(
                mark_promoted.mark(scratch, "sample-capability", "/docs/ROADMAP.md"),
                "added",
            )
            text = scratch.read_text(encoding="utf-8")
            self.assertIn(
                "> Promoted to `/docs/ROADMAP.md#sample-capability`", text
            )
            self.assertEqual(
                mark_promoted.mark(scratch, "sample-capability", "/docs/ROADMAP.md"),
                "updated",
            )
            self.assertEqual(
                text.count("Promoted to"),
                scratch.read_text(encoding="utf-8").count("Promoted to"),
            )


if __name__ == "__main__":
    unittest.main()
