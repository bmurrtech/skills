"""Seams for visual-explainer slides structural checker."""

from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    REPO_ROOT
    / "skills"
    / "visual-explainer"
    / "scripts"
    / "check_slides.py"
)


def _load():
    spec = importlib.util.spec_from_file_location("check_slides", SCRIPT)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules["check_slides"] = mod
    spec.loader.exec_module(mod)
    return mod


check = _load()


MINIMAL_OK = """<!DOCTYPE html>
<html lang="en" data-ve-deck-shell="1">
<head>
<meta charset="UTF-8">
<title>Ok Deck</title>
<style>
:root {
  --font-body: 'DM Sans', sans-serif;
  --font-mono: 'IBM Plex Mono', monospace;
  --slide-body-min: 16px;
  --slide-label-min: 10px;
}
.slide__body { font-size: max(16px, var(--slide-body-min)); }
.slide__label { font-size: max(10px, var(--slide-label-min)); }
</style>
</head>
<body>
<div class="deck">
  <section class="slide" data-screen-label="01 Open with the risk" data-action-title="Open with the risk">
    <h1 class="slide__display">Open with the risk</h1>
  </section>
  <section class="slide" data-screen-label="02 Cut the queue" data-action-title="Cut the queue">
    <h2 class="slide__heading">Cut the queue</h2>
    <p class="slide__body">Context line.</p>
  </section>
</div>
<script>function SlideEngine(){}</script>
</body>
</html>
"""


class CheckSlidesTests(unittest.TestCase):
    def _write(self, text: str) -> Path:
        tmp = tempfile.NamedTemporaryFile(
            mode="w", suffix=".html", delete=False, encoding="utf-8"
        )
        tmp.write(text)
        tmp.close()
        return Path(tmp.name)

    def test_ok_deck_passes(self):
        path = self._write(MINIMAL_OK)
        report = check.analyze(path)
        self.assertEqual(report["ok"], True)
        self.assertEqual(report["failures"], [])

    def test_missing_shell_marker_fails(self):
        html = MINIMAL_OK.replace(' data-ve-deck-shell="1"', "")
        path = self._write(html)
        report = check.analyze(path)
        self.assertFalse(report["ok"])
        kinds = {f["kind"] for f in report["failures"]}
        self.assertIn("missing_shell_marker", kinds)

    def test_missing_screen_label_fails(self):
        html = MINIMAL_OK.replace(
            ' data-screen-label="02 Cut the queue"',
            "",
            1,
        )
        path = self._write(html)
        report = check.analyze(path)
        self.assertFalse(report["ok"])
        kinds = {f["kind"] for f in report["failures"]}
        self.assertIn("missing_screen_label", kinds)

    def test_empty_action_title_fails(self):
        html = MINIMAL_OK.replace(
            'data-action-title="Cut the queue"',
            'data-action-title=""',
            1,
        )
        path = self._write(html)
        report = check.analyze(path)
        self.assertFalse(report["ok"])
        kinds = {f["kind"] for f in report["failures"]}
        self.assertIn("empty_action_title", kinds)

    def test_unresolved_overflow_marker_fails(self):
        html = MINIMAL_OK.replace(
            'data-screen-label="01 Open with the risk"',
            'data-screen-label="01 Open with the risk" data-slide-check="overflow"',
            1,
        )
        path = self._write(html)
        report = check.analyze(path)
        self.assertFalse(report["ok"])
        kinds = {f["kind"] for f in report["failures"]}
        self.assertIn("unresolved_overflow", kinds)

    def test_body_floor_token_missing_fails(self):
        html = MINIMAL_OK.replace("--slide-body-min: 16px;", "")
        path = self._write(html)
        report = check.analyze(path)
        self.assertFalse(report["ok"])
        kinds = {f["kind"] for f in report["failures"]}
        self.assertIn("missing_type_floor", kinds)

    def test_shell_file_in_repo_passes_when_present(self):
        shell = (
            REPO_ROOT
            / "skills"
            / "visual-explainer"
            / "references"
            / "deck-shell.html"
        )
        self.assertTrue(shell.is_file(), "deck-shell.html must ship with the skill")
        report = check.analyze(shell)
        self.assertEqual(report["failures"], [])
        self.assertTrue(report["ok"])
        self.assertGreaterEqual(report["slide_count"], 1)

    def test_heading_without_action_title_attr_fails(self):
        html = MINIMAL_OK.replace(
            ' data-action-title="Cut the queue"',
            "",
            1,
        )
        path = self._write(html)
        report = check.analyze(path)
        self.assertFalse(report["ok"])
        kinds = {f["kind"] for f in report["failures"]}
        self.assertIn("empty_action_title", kinds)


if __name__ == "__main__":
    unittest.main()
