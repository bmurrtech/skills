"""Seams for to-adr ADR catalog / at-a-glance visualizer."""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / "skills" / "to-adr" / "scripts"

SAMPLE_ADR = """# Keep release artifact filtered

<!-- File: docs/adr/0001-ADR-sample.md -->

## Status
Accepted
- **Date (optional):** 2026-09-26
- **Supersedes:** —
- **Superseded by:** —
- **Related ADRs:** [0002](0002-ADR-peer.md)
- **Related PRDs:** —

## Context and Problem Statement

Installers need a clean package without library OKF collisions.

## Decision Drivers
* Consumer cleanliness

## Considered Options
* Ship full tree
* Filter at package time

## Decision Outcome
Chosen option: "Filter at package time", because maintainers keep OKF in git.

### Consequences
* Good, because installs stay clean

### Confirmation
Tarball excludes knowledge/.

## Pros and Cons of the Options

### Filter at package time
* Good, because tracked meta + clean installs

### Ship full tree
* Bad, because collisions
* Why not chosen: overlays library OKF

## Assumptions
- Installers consume the filtered artifact.

## Constraints
- Do not gitignore knowledge/ for clean installs.

## Implementation Notes (Normative)
- Include skills/ + LICENSE only.
"""


def _load():
    path = SCRIPTS / "build_catalog.py"
    spec = importlib.util.spec_from_file_location("build_catalog", path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules["build_catalog"] = mod
    spec.loader.exec_module(mod)
    return mod


catalog = _load()


class BuildCatalogTests(unittest.TestCase):
    def test_parse_adr_extracts_status_and_synopsis(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            path = home / "0001-ADR-sample.md"
            path.write_text(SAMPLE_ADR, encoding="utf-8")
            row = catalog.parse_adr(path, home)
            self.assertEqual(row["number"], "0001")
            self.assertEqual(row["status_raw"], "accepted")
            self.assertEqual(row["status"], "stable")
            self.assertEqual(row["date"], "2026-09-26")
            self.assertIn("clean package", row["synopsis"])
            self.assertEqual(row["related_adrs"], ["/0002-ADR-peer.md"])

    def test_build_catalog_skips_index_and_counts_adrs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            (home / "index.md").write_text("# ADR index\n", encoding="utf-8")
            (home / "0001-ADR-sample.md").write_text(SAMPLE_ADR, encoding="utf-8")
            (home / "notes.md").write_text("# not an adr\n", encoding="utf-8")
            built = catalog.build_catalog(home, write_index_md=False)
            self.assertEqual(len(built["decisions"]), 1)
            self.assertEqual(built["generated"]["by"], "bmurrtech/skills/to-adr")

    def test_write_visualizer_embeds_catalog_and_escapes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp) / "adr"
            out = Path(tmp) / "diagrams"
            home.mkdir()
            (home / "0001-ADR-sample.md").write_text(
                SAMPLE_ADR.replace(
                    "Installers need a clean package",
                    "Installers need a clean <package>",
                ),
                encoding="utf-8",
            )
            built = catalog.build_catalog(home, write_index_md=False)
            html_path = catalog.write_visualizer(out, built)
            self.assertTrue(html_path.is_file())
            html = html_path.read_text(encoding="utf-8")
            self.assertNotIn("__CATALOG_JSON__", html)
            self.assertNotIn("fonts.googleapis.com", html)
            self.assertNotIn("fonts.gstatic.com", html)
            self.assertIn("\\u003c", html)
            catalog_json = (out / catalog.CATALOG_NAME).read_text(encoding="utf-8")
            payload = json.loads(catalog_json)
            self.assertEqual(len(payload["decisions"]), 1)

    def test_write_index_opt_in_emits_related_column(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            (home / "0001-ADR-sample.md").write_text(SAMPLE_ADR, encoding="utf-8")
            catalog.build_catalog(home, write_index_md=True)
            index = (home / "index.md").read_text(encoding="utf-8")
            self.assertIn("| Related |", index)
            self.assertIn("0001-ADR-sample.md", index)
            self.assertIn("relates", index)


if __name__ == "__main__":
    unittest.main()
