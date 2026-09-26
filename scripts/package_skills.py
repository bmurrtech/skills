#!/usr/bin/env python3
"""Build the filtered skills release artifact (skills/ + LICENSE only)."""

from __future__ import annotations

import argparse
import hashlib
import sys
import tarfile
from pathlib import Path

RELEASE_INCLUDE_DIRS: frozenset[str] = frozenset({"skills"})
RELEASE_INCLUDE_FILES: frozenset[str] = frozenset({"LICENSE"})

# Root names / files that must never appear in the skills release artifact.
# Library OKF, ops manuals, docs, and tooling stay tracked in git but out of installs.
RELEASE_EXCLUDE_ROOTS: frozenset[str] = frozenset(
    {
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
        "pm",
        ".scratch",
        ".agents",
        ".claude",
        ".cursor",
        ".changeset",
        ".github",
        "node_modules",
        "package.json",
        "package-lock.json",
        "dist",
        ".gitignore",
        ".env",
    }
)


def build_release_members(repo_root: Path) -> list[str]:
    """Return sorted relative POSIX paths included in the release artifact."""
    root = repo_root.resolve()
    members: list[str] = []

    for name in sorted(RELEASE_INCLUDE_FILES):
        path = root / name
        if not path.is_file():
            raise FileNotFoundError(f"required release file missing: {name}")
        members.append(name)

    for dirname in sorted(RELEASE_INCLUDE_DIRS):
        base = root / dirname
        if not base.is_dir():
            raise FileNotFoundError(f"required release directory missing: {dirname}")
        for path in sorted(base.rglob("*")):
            if not path.is_file():
                continue
            rel_parts = path.relative_to(root).parts
            # Skip dotfiles/dirs, bytecode caches, and compiled Python.
            if any(part.startswith(".") for part in rel_parts):
                continue
            if any(part == "__pycache__" for part in rel_parts):
                continue
            if path.suffix in {".pyc", ".pyo"}:
                continue
            rel = path.relative_to(root).as_posix()
            members.append(rel)

    for member in members:
        top = member.split("/", 1)[0]
        if top in RELEASE_EXCLUDE_ROOTS and top not in RELEASE_INCLUDE_DIRS:
            raise RuntimeError(f"excluded path leaked into members: {member}")

    return members


def package_skills(
    repo_root: Path,
    *,
    version: str,
    out_dir: Path,
) -> tuple[Path, Path]:
    """Write tar.gz + sha256 under out_dir. Returns (tarball, checksum) paths."""
    if not version or "/" in version or "\\" in version:
        raise ValueError(f"invalid version: {version!r}")

    members = build_release_members(repo_root)
    out_dir.mkdir(parents=True, exist_ok=True)

    archive_root = f"bmurrtech-skills-{version}"
    tarball = out_dir / f"{archive_root}.tar.gz"
    checksum_path = out_dir / f"{archive_root}.tar.gz.sha256"

    with tarfile.open(tarball, "w:gz") as tar:
        for rel in members:
            abs_path = repo_root / rel
            tar.add(abs_path, arcname=f"{archive_root}/{rel}")

    digest = hashlib.sha256(tarball.read_bytes()).hexdigest()
    checksum_path.write_text(f"{digest}  {tarball.name}\n", encoding="utf-8")
    return tarball, checksum_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Package skills/ + LICENSE into a release tarball (excludes library OKF)."
    )
    parser.add_argument(
        "--version",
        required=True,
        help="Semver used in artifact names (e.g. 1.4.2)",
    )
    parser.add_argument(
        "--out",
        default="dist",
        help="Output directory (default: dist/)",
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root (default: cwd)",
    )
    args = parser.parse_args(argv)

    repo_root = Path(args.repo_root).resolve()
    out_dir = Path(args.out)
    if not out_dir.is_absolute():
        out_dir = (Path.cwd() / out_dir).resolve()

    tarball, checksum = package_skills(
        repo_root, version=args.version, out_dir=out_dir
    )
    print(tarball)
    print(checksum)
    return 0


if __name__ == "__main__":
    sys.exit(main())
