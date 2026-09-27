#!/usr/bin/env python3
"""Append a roadmap entry fragment to docs/ROADMAP.md and print its anchor."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_MARKERS = (
    "**Domain:**",
    "**Intent**",
    "**Scope**",
    "**Boundaries**",
)


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def github_anchor(title: str) -> str:
    """Approximate GitHub/Slugger heading anchors."""
    s = title.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    s = re.sub(r"\s+", "-", s.strip())
    s = re.sub(r"-+", "-", s)
    return s


def extract_title(entry: str) -> str:
    for line in entry.splitlines():
        if line.startswith("## "):
            return line[3:].strip()
    raise ValueError("entry must start with a ## title heading")


def validate_entry(entry: str) -> None:
    text = entry.strip()
    if not text.startswith("## "):
        raise ValueError("entry must start with ## title")
    for marker in REQUIRED_MARKERS:
        if marker not in text:
            raise ValueError(f"entry missing required field marker: {marker}")
    # Reject obvious filler-only optional sections
    for m in re.finditer(
        r"\*\*(Open Questions|Notes)\*\*\s*\n(?:\s*-\s*None\.?\s*\n?)+",
        text,
        re.IGNORECASE,
    ):
        raise ValueError(
            f"omit empty optional section rather than filler: {m.group(1)}"
        )


def append_entry(roadmap: Path, entry: str) -> str:
    validate_entry(entry)
    title = extract_title(entry)
    anchor = github_anchor(title)
    body = roadmap.read_text(encoding="utf-8") if roadmap.exists() else ""
    # Detect duplicate title
    if re.search(rf"^## {re.escape(title)}\s*$", body, re.MULTILINE):
        raise ValueError(f"entry title already present: {title}")
    fragment = entry.strip() + "\n"
    if body and not body.endswith("\n"):
        body += "\n"
    if body and not body.endswith("\n\n"):
        body += "\n"
    roadmap.parent.mkdir(parents=True, exist_ok=True)
    roadmap.write_text(body + fragment + "\n", encoding="utf-8")
    return anchor


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--entry",
        type=Path,
        required=True,
        help="Markdown fragment containing one ## entry",
    )
    parser.add_argument(
        "--roadmap",
        type=Path,
        default=None,
        help="ROADMAP path (default: <repo>/docs/ROADMAP.md)",
    )
    args = parser.parse_args()
    roadmap = args.roadmap or (repo_root() / "docs" / "ROADMAP.md")
    entry = args.entry.read_text(encoding="utf-8")
    try:
        anchor = append_entry(roadmap, entry)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1
    print(anchor)
    print(f"appended: {roadmap}#{anchor}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
