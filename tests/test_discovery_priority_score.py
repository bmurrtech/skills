"""Seams for discovery priority_score.py (KPFS → BV / DR / Overall → P0–P3)."""

from __future__ import annotations

import importlib.util
import itertools
import json
import subprocess
import sys
import tempfile
import unittest
from fractions import Fraction
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


def _expected(k: int, p: int, f: int, s: int) -> tuple[float, float, float, str]:
    bv = Fraction(k + p, 6) * 100
    dr = Fraction(f + s, 6) * 100
    overall = bv * Fraction(2, 5) + dr * Fraction(3, 5)
    if overall >= 80:
        label = "P0"
    elif overall >= 65:
        label = "P1"
    elif overall >= 50:
        label = "P2"
    else:
        label = "P3"
    return (
        float(round(bv, 1)),
        float(round(dr, 1)),
        float(round(overall, 1)),
        label,
    )


def _uc(uid: str, k, p, f, s) -> dict:
    return {"id": uid, "K": k, "P": p, "F": f, "S": s}


class ScoreOneTests(unittest.TestCase):
    def test_reference_value(self):
        row = ps.score_one(_uc("ref", 3, 3, 2, 3))
        self.assertEqual(row["bv"], 100.0)
        self.assertEqual(row["dr"], 83.3)
        self.assertEqual(row["overall"], 90.0)
        self.assertEqual(row["priority"], "P0")
        self.assertEqual(row["status"], "scored")

    def test_all_81_combos_match_exact_model(self):
        for k, p, f, s in itertools.product((1, 2, 3), repeat=4):
            with self.subTest(K=k, P=p, F=f, S=s):
                row = ps.score_one(_uc("x", k, p, f, s))
                bv, dr, overall, label = _expected(k, p, f, s)
                self.assertEqual(row["bv"], bv)
                self.assertEqual(row["dr"], dr)
                self.assertEqual(row["overall"], overall)
                self.assertEqual(row["priority"], label)

    def test_threshold_boundaries(self):
        cases = {
            (1, 2, 3, 3): ("P0", 80.0),
            (2, 2, 2, 2): ("P1", 66.7),
            (1, 2, 1, 2): ("P2", 50.0),
            (3, 2, 1, 2): ("P2", 63.3),
            (1, 1, 1, 1): ("P3", 33.3),
        }
        for (k, p, f, s), (label, overall) in cases.items():
            with self.subTest(K=k, P=p, F=f, S=s):
                row = ps.score_one(_uc("b", k, p, f, s))
                self.assertEqual(row["priority"], label)
                self.assertEqual(row["overall"], overall)

    def test_null_dimension_is_unscored(self):
        row = ps.score_one(_uc("gap", 3, None, 2, None))
        self.assertEqual(row["status"], "needs-discovery")
        self.assertEqual(row["priority"], "none")
        self.assertEqual(row["missing"], ["P", "S"])
        self.assertIsNone(row["bv"])
        self.assertIsNone(row["dr"])
        self.assertIsNone(row["overall"])

    def test_absent_dimension_is_unscored(self):
        row = ps.score_one({"id": "thin", "K": 2, "P": 2})
        self.assertEqual(row["status"], "needs-discovery")
        self.assertEqual(row["missing"], ["F", "S"])

    def test_extra_keys_pass_through(self):
        row = ps.score_one({**_uc("x", 2, 2, 2, 2), "title": "Intake triage"})
        self.assertEqual(row["title"], "Intake triage")

    def test_rejects_invalid_bands(self):
        for bad in (0, 4, 2.0, True, "3", -1):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                ps.score_one(_uc("x", bad, 2, 2, 2))

    def test_rejects_missing_or_blank_id(self):
        with self.assertRaises(ValueError):
            ps.score_one({"K": 1, "P": 1, "F": 1, "S": 1})
        with self.assertRaises(ValueError):
            ps.score_one(_uc("  ", 1, 1, 1, 1))

    def test_rejects_non_object(self):
        with self.assertRaises(ValueError):
            ps.score_one(["not", "a", "dict"])


class RankTests(unittest.TestCase):
    def test_sorts_label_then_overall_then_s_then_id(self):
        result = ps.rank(
            [
                _uc("p2-low", 1, 2, 1, 2),
                _uc("p0-top", 3, 3, 3, 3),
                _uc("p1-hi-s", 2, 2, 1, 3),
                _uc("p1-lo-s", 2, 2, 3, 1),
                _uc("p1-b", 2, 2, 2, 2),
                _uc("p1-a", 2, 2, 2, 2),
                _uc("gap", 3, 3, None, 3),
            ]
        )
        ids = [r["id"] for r in result["scored"]]
        self.assertEqual(
            ids, ["p0-top", "p1-hi-s", "p1-a", "p1-b", "p1-lo-s", "p2-low"]
        )
        self.assertEqual([r["rank"] for r in result["scored"]], [1, 2, 3, 4, 5, 6])
        self.assertEqual([r["id"] for r in result["unscored"]], ["gap"])
        self.assertNotIn("rank", result["unscored"][0])

    def test_overall_never_lifts_lower_label(self):
        result = ps.rank([_uc("p1", 2, 2, 2, 2), _uc("p0", 1, 2, 3, 3)])
        self.assertEqual([r["priority"] for r in result["scored"]], ["P0", "P1"])

    def test_rejects_duplicate_ids(self):
        with self.assertRaises(ValueError):
            ps.rank([_uc("dup", 1, 1, 1, 1), _uc("dup", 2, 2, 2, 2)])

    def test_empty_input(self):
        self.assertEqual(ps.rank([]), {"scored": [], "unscored": []})


class CliTests(unittest.TestCase):
    def _run(self, *args: str, stdin: str | None = None):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            input=stdin,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_stdin(self):
        payload = {"use_cases": [_uc("a", 3, 3, 2, 3)]}
        proc = self._run("--stdin", stdin=json.dumps(payload))
        self.assertEqual(proc.returncode, 0, proc.stderr)
        out = json.loads(proc.stdout)
        self.assertEqual(out["scored"][0]["priority"], "P0")
        self.assertEqual(out["scored"][0]["overall"], 90.0)

    def test_file(self):
        payload = {"use_cases": [_uc("g", None, 2, 2, 2)]}
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
            json.dump(payload, fh)
            path = fh.name
        proc = self._run(path)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        out = json.loads(proc.stdout)
        self.assertEqual(out["scored"], [])
        self.assertEqual(out["unscored"][0]["missing"], ["K"])

    def test_bad_envelope_exits_1(self):
        proc = self._run("--stdin", stdin=json.dumps({"candidates": []}))
        self.assertEqual(proc.returncode, 1)
        self.assertIn("use_cases", proc.stderr)

    def test_bad_band_exits_1(self):
        payload = {"use_cases": [_uc("x", 5, 1, 1, 1)]}
        proc = self._run("--stdin", stdin=json.dumps(payload))
        self.assertEqual(proc.returncode, 1)
        self.assertIn("K", proc.stderr)
        self.assertEqual(proc.stdout, "")


if __name__ == "__main__":
    unittest.main()
