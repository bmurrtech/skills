"""Seams for discovery priority_score.py formula + rank."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "skills" / "discovery" / "scripts" / "priority_score.py"


def _load():
    spec = importlib.util.spec_from_file_location("priority_score", SCRIPT)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules["priority_score"] = mod
    spec.loader.exec_module(mod)
    return mod


ps = _load()


class DiscoveryPriorityScoreTests(unittest.TestCase):
    def test_p1_and_n_formula(self):
        row = ps.score_one(
            {"id": "a", "K": 4, "P": 5, "F": 4, "S": 5, "confidence": "H"}
        )
        self.assertEqual(row["V"], 9)
        self.assertEqual(row["p_level"], "P1")
        self.assertEqual(row["N"], 5 * 4 + 5 * 5 + 6 * 4 + 4 * 5)
        self.assertEqual(row["status"], "scored")

    def test_quadrants(self):
        self.assertEqual(
            ps.score_one({"id": "p2", "K": 4, "P": 4, "F": 2, "S": 3})["p_level"],
            "P2",
        )
        self.assertEqual(
            ps.score_one({"id": "p3", "K": 2, "P": 2, "F": 5, "S": 3})["p_level"],
            "P3",
        )
        self.assertEqual(
            ps.score_one({"id": "p4", "K": 2, "P": 2, "F": 2, "S": 1})["p_level"],
            "P4",
        )

    def test_gate_skips_p_level(self):
        row = ps.score_one({"id": "x", "gate": "deferred", "K": 5, "P": 5, "F": 5, "S": 5})
        self.assertEqual(row["status"], "deferred")
        self.assertIsNone(row["p_level"])
        self.assertIsNone(row["N"])

    def test_rank_orders_p_then_n(self):
        result = ps.rank(
            [
                {"id": "low-p1", "K": 4, "P": 3, "F": 4, "S": 2, "confidence": "M"},
                {"id": "high-p1", "K": 5, "P": 5, "F": 5, "S": 5, "confidence": "H"},
                {"id": "p2", "K": 5, "P": 4, "F": 2, "S": 5, "confidence": "H"},
                {"id": "blocked", "gate": "blocked"},
            ]
        )
        ids = [r["id"] for r in result["ranked"]]
        self.assertEqual(ids, ["high-p1", "low-p1", "p2"])
        self.assertEqual(result["ranked"][0]["rank"], 1)
        self.assertEqual(result["gated"][0]["id"], "blocked")

    def test_near_tie_flag(self):
        result = ps.rank(
            [
                {"id": "a", "K": 4, "P": 4, "F": 4, "S": 4, "confidence": "H"},
                {"id": "b", "K": 4, "P": 4, "F": 4, "S": 3, "confidence": "H"},
            ]
        )
        self.assertIn("b", result["ranked"][0]["near_tie_with"])
        self.assertIn("a", result["ranked"][1]["near_tie_with"])

    def test_cli_stdin(self):
        payload = {
            "candidates": [
                {"id": "a", "K": 3, "P": 4, "F": 4, "S": 3, "confidence": "M"}
            ]
        }
        proc = subprocess.run(
            [sys.executable, str(SCRIPT), "--stdin"],
            input=json.dumps(payload),
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        out = json.loads(proc.stdout)
        self.assertEqual(out["ranked"][0]["p_level"], "P1")

    def test_cli_file(self):
        payload = {"candidates": [{"id": "g", "gate": "needs-discovery"}]}
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
            json.dump(payload, fh)
            path = fh.name
        proc = subprocess.run(
            [sys.executable, str(SCRIPT), path],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        out = json.loads(proc.stdout)
        self.assertEqual(out["gated"][0]["status"], "needs-discovery")
        self.assertEqual(out["ranked"], [])

    def test_rejects_bad_band(self):
        with self.assertRaises(ValueError):
            ps.score_one({"id": "x", "K": 6, "P": 3, "F": 3, "S": 3})

    def test_rejects_bad_confidence_when_gated(self):
        with self.assertRaises(ValueError):
            ps.score_one({"id": "x", "gate": "blocked", "confidence": "Z"})


if __name__ == "__main__":
    unittest.main()
