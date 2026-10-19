"""Seams for skills/release/scripts/changelog_release_notes.py."""

from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    REPO_ROOT / "skills" / "release" / "scripts" / "changelog_release_notes.py"
)


def _load():
    spec = importlib.util.spec_from_file_location(
        "changelog_release_notes", SCRIPT
    )
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules["changelog_release_notes"] = mod
    spec.loader.exec_module(mod)
    return mod


crn = _load()

SAMPLE_CHANGELOG = """# Changelog

## [Unreleased]

### Added
- pending

## [1.2.3] - 2026-10-01

### Added
- feature A

### Fixed
- bug B

## [1.2.2] - 2026-09-01

### Changed
- older
"""


class ChangelogReleaseNotesTests(unittest.TestCase):
    def test_script_lives_under_release_skill(self) -> None:
        self.assertTrue(SCRIPT.is_file())
        self.assertFalse(
            (REPO_ROOT / "scripts" / "changelog_release_notes.py").exists(),
            msg="ops duplicate must not exist — SoT is skills/release/scripts/",
        )

    def test_extract_section_stops_at_next_heading(self) -> None:
        section = crn.extract_section(SAMPLE_CHANGELOG, "1.2.3")
        assert section is not None
        self.assertIn("## [1.2.3] - 2026-10-01", section)
        self.assertIn("feature A", section)
        self.assertIn("bug B", section)
        self.assertNotIn("Unreleased", section)
        self.assertNotIn("1.2.2", section)

    def test_extract_missing_version(self) -> None:
        self.assertIsNone(crn.extract_section(SAMPLE_CHANGELOG, "9.9.9"))

    def test_parse_funding_yml_ko_fi_and_bmc(self) -> None:
        text = """
ko_fi: bmurrtech
buy_me_a_coffee: bmurrtech
patreon: # empty
"""
        ctas = crn.parse_funding_yml(text)
        urls = {u for _, _, u in ctas}
        self.assertIn("https://ko-fi.com/bmurrtech", urls)
        self.assertIn("https://www.buymeacoffee.com/bmurrtech", urls)

    def test_build_notes_with_cta_and_extra(self) -> None:
        notes = crn.build_notes(
            changelog_text=SAMPLE_CHANGELOG,
            version="1.2.3",
            extra_note="Artifact blurb.",
            ctas=[
                ("ko_fi", "Ko-fi", "https://ko-fi.com/bmurrtech"),
            ],
        )
        self.assertIn("feature A", notes)
        self.assertIn("Artifact blurb.", notes)
        self.assertIn("## Support", notes)
        self.assertIn("https://ko-fi.com/bmurrtech", notes)

    def test_build_notes_omits_cta_when_empty(self) -> None:
        notes = crn.build_notes(
            changelog_text=SAMPLE_CHANGELOG,
            version="1.2.3",
            extra_note=None,
            ctas=[],
        )
        self.assertNotIn("## Support", notes)

    def test_main_reads_repo_funding(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / ".github").mkdir()
            (root / "CHANGELOG.md").write_text(SAMPLE_CHANGELOG, encoding="utf-8")
            (root / ".github" / "FUNDING.yml").write_text(
                "ko_fi: acme\nbuy_me_a_coffee: acme\n",
                encoding="utf-8",
            )
            ctas = crn.resolve_ctas(root)
            urls = {u for _, _, u in ctas}
            self.assertEqual(
                urls,
                {
                    "https://ko-fi.com/acme",
                    "https://www.buymeacoffee.com/acme",
                },
            )

    def test_context_fallback_when_no_funding(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "CONTEXT.md").write_text(
                "See https://ko-fi.com/fallback and "
                "https://www.buymeacoffee.com/fallback\n",
                encoding="utf-8",
            )
            ctas = crn.resolve_ctas(root)
            urls = {u for _, _, u in ctas}
            self.assertEqual(
                urls,
                {
                    "https://ko-fi.com/fallback",
                    "https://www.buymeacoffee.com/fallback",
                },
            )


if __name__ == "__main__":
    unittest.main()
