"""Implement skill content contract: review exit boundary + hard Git ban."""

from __future__ import annotations

import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
IMPLEMENT_SKILL = REPO_ROOT / "skills" / "implement" / "SKILL.md"


class ImplementSocContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = IMPLEMENT_SKILL.read_text(encoding="utf-8")
        cls.lower = cls.text.lower()

    def test_skill_file_exists(self) -> None:
        self.assertTrue(IMPLEMENT_SKILL.is_file())

    def test_hard_git_ban(self) -> None:
        # Must forbid publish actions inside implement (bug 001 / FR-3).
        for needle in (
            "never stage",
            "never commit",
            "never push",
            "open/update a pr",
            "force-align",
        ):
            self.assertIn(needle, self.lower)
        self.assertNotRegex(
            self.text,
            re.compile(r"Commit only if the user asked", re.I),
        )

    def test_review_exit_is_context_boundary(self) -> None:
        # Prefer subagent code-review; else handoff kind cd-rvw (FR-2).
        self.assertRegex(self.lower, r"subagent")
        self.assertRegex(self.lower, r"cd-rvw")
        self.assertRegex(self.lower, r"handoff")
        self.assertIn("never same-agent inline", self.lower)
        # Must not prescribe same-agent inline review as the only path.
        self.assertNotRegex(
            self.text,
            re.compile(
                r"### 5\.\s*Review\s*\n\s*\nRun \*\*`code-review`\*\* on the change",
                re.I,
            ),
        )

    def test_housekeeping_before_review(self) -> None:
        self.assertRegex(self.lower, r"upkeep")
        self.assertRegex(self.lower, r"context")
        # Housekeeping section should appear before review exit in the body.
        upkeep_pos = self.lower.find("upkeep")
        review_pos = self.lower.find("review exit")
        if review_pos < 0:
            review_pos = self.lower.find("### 5")
        self.assertGreater(upkeep_pos, 0)
        self.assertGreater(review_pos, upkeep_pos)

    def test_points_at_commit_skill(self) -> None:
        self.assertRegex(self.lower, r"`commit`|/\*\*`commit`\*\*")

    def test_soft_grill_reopen(self) -> None:
        # FR-6: soft-suggest new-session grill; do not auto-run inline.
        self.assertIn("soft-suggest", self.lower)
        self.assertIn("new-session", self.lower)
        self.assertIn("grill-me", self.lower)
        self.assertRegex(self.lower, r"do \*\*not\*\* auto-run|do not auto-run")


if __name__ == "__main__":
    unittest.main()
