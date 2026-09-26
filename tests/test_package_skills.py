"""Release artifact must ship skills + LICENSE only — not library OKF/ops/docs."""

from __future__ import annotations

import sys
import tarfile
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.package_skills import (  # noqa: E402
    RELEASE_EXCLUDE_ROOTS,
    RELEASE_INCLUDE_FILES,
    RELEASE_INCLUDE_DIRS,
    build_release_members,
    package_skills,
)


class PackageSkillsContractTests(unittest.TestCase):
    def test_include_set_is_skills_and_license(self) -> None:
        self.assertEqual(RELEASE_INCLUDE_DIRS, frozenset({"skills"}))
        self.assertEqual(RELEASE_INCLUDE_FILES, frozenset({"LICENSE"}))

    def test_exclude_set_covers_library_meta(self) -> None:
        required = {
            "knowledge",
            "docs",
            "CONTEXT.md",
            "AGENTS.md",
            "CLAUDE.md",
            "README.md",
            "CHANGELOG.md",
            "scripts",
            "tests",
            "integrations",
        }
        self.assertTrue(required.issubset(RELEASE_EXCLUDE_ROOTS))

    def test_repo_members_include_skills_and_license_only(self) -> None:
        members = build_release_members(REPO_ROOT)
        self.assertIn("LICENSE", members)
        self.assertTrue(any(m.startswith("skills/") for m in members))
        # Maintainer scaffolding is local-only — never a shipped skill
        self.assertFalse(
            any(
                m == "skills/skill-create"
                or m.startswith("skills/skill-create/")
                for m in members
            ),
            msg="skill-create must not appear in the release artifact",
        )
        forbidden_prefixes = (
            "knowledge/",
            "docs/",
            "scripts/",
            "tests/",
            "integrations/",
        )
        forbidden_files = {
            "CONTEXT.md",
            "AGENTS.md",
            "CLAUDE.md",
            "README.md",
            "CHANGELOG.md",
        }
        for path in members:
            self.assertFalse(
                any(path == p or path.startswith(p) for p in forbidden_prefixes),
                msg=f"excluded path leaked: {path}",
            )
            self.assertNotIn(path, forbidden_files)

    def test_tarball_layout_and_exclusions(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out_dir = Path(tmp)
            tarball, checksum = package_skills(
                REPO_ROOT, version="0.0.0-test", out_dir=out_dir
            )
            self.assertTrue(tarball.is_file())
            self.assertTrue(checksum.is_file())
            self.assertEqual(tarball.name, "bmurrtech-skills-0.0.0-test.tar.gz")

            prefix = "bmurrtech-skills-0.0.0-test/"
            with tarfile.open(tarball, "r:gz") as tar:
                names = [m.name for m in tar.getmembers() if m.isfile()]

            self.assertIn(f"{prefix}LICENSE", names)
            self.assertTrue(any(n.startswith(f"{prefix}skills/") for n in names))

            forbidden_prefixes = (
                "knowledge/",
                "docs/",
                "scripts/",
                "tests/",
                "integrations/",
            )
            forbidden_files = {
                "CONTEXT.md",
                "AGENTS.md",
                "CLAUDE.md",
                "README.md",
                "CHANGELOG.md",
            }
            for name in names:
                rel = name[len(prefix) :] if name.startswith(prefix) else name
                self.assertFalse(
                    any(rel == p or rel.startswith(p) for p in forbidden_prefixes),
                    msg=f"excluded path leaked: {rel}",
                )
                self.assertNotIn(rel, forbidden_files)
                self.assertNotIn("__pycache__", rel.split("/"))
                self.assertFalse(rel.endswith(".pyc") or rel.endswith(".pyo"))
                self.assertTrue(
                    rel == "LICENSE" or rel.startswith("skills/"),
                    msg=f"unexpected release member: {rel}",
                )

if __name__ == "__main__":
    unittest.main()
