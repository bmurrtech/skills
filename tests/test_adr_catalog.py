"""Seams for create-adr ADR catalog / at-a-glance visualizer."""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / "skills" / "create-adr" / "scripts"

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

OLDER = """# Old decision

## Status
Superseded
- **Date (optional):** 2026-01-01
- **Supersedes:** —
- **Superseded by:** [0002](0002-ADR-new.md)

## Context and Problem Statement

Old path.

## Decision Outcome
Chosen option: "old".
"""

NEWER = """# New decision

## Status
Accepted
- **Date (optional):** 2026-02-01
- **Supersedes:** [0001](0001-ADR-old.md)
- **Superseded by:** —

## Context and Problem Statement

New path.

## Decision Outcome
Chosen option: "new".
"""

SELF = """# Self

## Status
Accepted
- **Date (optional):** 2026-03-01
- **Supersedes:** [0001](0001-ADR-self.md)
- **Superseded by:** —

## Context and Problem Statement

Loop.

## Decision Outcome
Chosen option: "self".
"""

# Mirror-only: older declares Superseded by; newer omits Supersedes.
MIRROR_OLDER = """# Old decision

## Status
Superseded
- **Date (optional):** 2026-01-01
- **Supersedes:** —
- **Superseded by:** [0002](0002-ADR-new.md)

## Context and Problem Statement

Old path.

## Decision Outcome
Chosen option: "old".
"""

MIRROR_NEWER = """# New decision

## Status
Accepted
- **Date (optional):** 2026-02-01
- **Supersedes:** —
- **Superseded by:** —

## Context and Problem Statement

New path.

## Decision Outcome
Chosen option: "new".
"""

CYCLE_A = """# Cycle A

## Status
Accepted
- **Date (optional):** 2026-05-01
- **Supersedes:** [0002](0002-ADR-cycle-b.md)
- **Superseded by:** —

## Context and Problem Statement

A.

## Decision Outcome
Chosen option: "a".
"""

CYCLE_B = """# Cycle B

## Status
Accepted
- **Date (optional):** 2026-05-02
- **Supersedes:** [0001](0001-ADR-cycle-a.md)
- **Superseded by:** —

## Context and Problem Statement

B.

## Decision Outcome
Chosen option: "b".
"""

MALFORMED = """# Bad link

## Status
Proposed
- **Date (optional):** 2026-04-01
- **Supersedes:** older-without-link
- **Superseded by:** —

## Context and Problem Statement

Missing markdown link.

## Decision Outcome
Chosen option: "bad".
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
            fat, slim, invalid = catalog.build_catalog(home, write_index_md=False)
            self.assertEqual(len(fat["decisions"]), 1)
            self.assertEqual(fat["schema_version"], 2)
            self.assertEqual(fat["generated"]["by"], "bmurrtech/skills/create-adr")
            self.assertIn("lineage_edges", fat)
            self.assertIn("issues", fat)
            self.assertFalse(invalid)
            self.assertNotIn("markdown", slim["decisions"][0])
            self.assertNotIn("history", slim["decisions"][0])
            self.assertIn("markdown", fat["decisions"][0])

    def test_lineage_edge_from_supersedes_pair(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            (home / "0001-ADR-old.md").write_text(OLDER, encoding="utf-8")
            (home / "0002-ADR-new.md").write_text(NEWER, encoding="utf-8")
            fat, _, invalid = catalog.build_catalog(home)
            self.assertFalse(invalid)
            self.assertEqual(len(fat["lineage_edges"]), 1)
            edge = fat["lineage_edges"][0]
            self.assertEqual(edge["from"], "0001-ADR-old")
            self.assertEqual(edge["to"], "0002-ADR-new")
            self.assertEqual(edge["type"], "supersedes")
            self.assertNotIn("effect", edge)
            old = next(d for d in fat["decisions"] if d["slug"] == "0001-ADR-old")
            new = next(d for d in fat["decisions"] if d["slug"] == "0002-ADR-new")
            self.assertEqual(old["lineage"]["successors"], ["0002-ADR-new"])
            self.assertEqual(old["superseded_by"], ["0002-ADR-new"])
            self.assertEqual(old["supersedes"], [])
            self.assertEqual(new["supersedes"], ["0001-ADR-old"])
            self.assertEqual(new["lineage"]["predecessors"], ["0001-ADR-old"])

    def test_mirror_only_superseded_by_fills_graph_fields(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            (home / "0001-ADR-old.md").write_text(MIRROR_OLDER, encoding="utf-8")
            (home / "0002-ADR-new.md").write_text(MIRROR_NEWER, encoding="utf-8")
            fat, _, invalid = catalog.build_catalog(home)
            self.assertFalse(invalid)
            self.assertEqual(len(fat["lineage_edges"]), 1)
            old = next(d for d in fat["decisions"] if d["slug"] == "0001-ADR-old")
            new = next(d for d in fat["decisions"] if d["slug"] == "0002-ADR-new")
            self.assertEqual(old["superseded_by"], ["0002-ADR-new"])
            self.assertEqual(old["lineage"]["successors"], ["0002-ADR-new"])
            self.assertEqual(new["supersedes"], ["0001-ADR-old"])
            self.assertEqual(new["lineage"]["predecessors"], ["0001-ADR-old"])

    def test_self_target_is_invalid_lineage(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            (home / "0001-ADR-self.md").write_text(SELF, encoding="utf-8")
            fat, _, invalid = catalog.build_catalog(home)
            self.assertTrue(invalid)
            codes = {i["code"] for i in fat["issues"]}
            self.assertIn("invalid_lineage", codes)
            self.assertEqual(fat["lineage_edges"], [])

    def test_cycle_pair_is_invalid_lineage(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            (home / "0001-ADR-cycle-a.md").write_text(CYCLE_A, encoding="utf-8")
            (home / "0002-ADR-cycle-b.md").write_text(CYCLE_B, encoding="utf-8")
            fat, _, invalid = catalog.build_catalog(home)
            self.assertTrue(invalid)
            codes = {i["code"] for i in fat["issues"]}
            self.assertIn("invalid_lineage", codes)
            self.assertEqual(fat["lineage_edges"], [])

    def test_main_invalid_lineage_writes_catalog_then_exits_nonzero(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            (home / "0001-ADR-self.md").write_text(SELF, encoding="utf-8")
            with mock.patch.object(
                sys, "argv", ["build_catalog.py", "--home", str(home)]
            ):
                code = catalog.main()
            self.assertEqual(code, 1)
            catalog_path = home / "catalog.json"
            self.assertTrue(catalog_path.is_file())
            payload = json.loads(catalog_path.read_text(encoding="utf-8"))
            self.assertTrue(
                any(i["code"] == "invalid_lineage" for i in payload["issues"])
            )

    def test_slim_catalog_omits_generated_at(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            (home / "0001-ADR-sample.md").write_text(SAMPLE_ADR, encoding="utf-8")
            fat, slim, _ = catalog.build_catalog(home)
            self.assertIn("at", fat["generated"])
            self.assertNotIn("at", slim["generated"])
            self.assertEqual(slim["generated"]["by"], "bmurrtech/skills/create-adr")

    def test_malformed_supersession_issue(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            (home / "0001-ADR-bad.md").write_text(MALFORMED, encoding="utf-8")
            fat, _, invalid = catalog.build_catalog(home)
            self.assertFalse(invalid)
            codes = {i["code"] for i in fat["issues"]}
            self.assertIn("malformed_supersession", codes)

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
            fat, _, _ = catalog.build_catalog(home, write_index_md=False)
            html_path = catalog.write_visualizer(out, fat)
            self.assertTrue(html_path.is_file())
            html = html_path.read_text(encoding="utf-8")
            self.assertNotIn("__CATALOG_JSON__", html)
            self.assertNotIn("fonts.googleapis.com", html)
            self.assertNotIn("fonts.gstatic.com", html)
            self.assertIn("\\u003c", html)
            self.assertIn("returnStack", html)
            catalog_json = (out / catalog.SCRATCH_CATALOG_NAME).read_text(encoding="utf-8")
            payload = json.loads(catalog_json)
            self.assertEqual(len(payload["decisions"]), 1)
            self.assertEqual(payload["schema_version"], 2)

    def test_write_home_catalog_slim(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            (home / "0001-ADR-sample.md").write_text(SAMPLE_ADR, encoding="utf-8")
            _, slim, _ = catalog.build_catalog(home)
            path = catalog.write_home_catalog(home, slim)
            self.assertEqual(path.name, "catalog.json")
            payload = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(payload["schema_version"], 2)
            self.assertNotIn("markdown", payload["decisions"][0])

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
