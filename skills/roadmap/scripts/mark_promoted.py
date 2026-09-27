#!/usr/bin/env python3
"""Mark a scratch idea file as promoted (provenance; do not delete)."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def marker_line(anchor: str, roadmap_rel: str = "/docs/ROADMAP.md") -> str:
    anchor = anchor.lstrip("#")
    return f"> Promoted to `{roadmap_rel}#{anchor}`"


def mark(scratch: Path, anchor: str, roadmap_rel: str) -> str:
    if not scratch.exists():
        raise FileNotFoundError(scratch)
    text = scratch.read_text(encoding="utf-8")
    line = marker_line(anchor, roadmap_rel)
    # Idempotent: replace existing promotion marker or insert after title
    if re.search(r"^> Promoted to `[^`]+`\s*$", text, re.MULTILINE):
        text = re.sub(
            r"^> Promoted to `[^`]+`\s*$",
            line,
            text,
            count=1,
            flags=re.MULTILINE,
        )
        scratch.write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")
        return "updated"
    lines = text.splitlines()
    insert_at = 1 if lines and lines[0].startswith("# ") else 0
    lines.insert(insert_at, "")
    lines.insert(insert_at + 1, line)
    lines.insert(insert_at + 2, "")
    out = "\n".join(lines).rstrip() + "\n"
    scratch.write_text(out, encoding="utf-8")
    return "added"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scratch", type=Path, required=True)
    parser.add_argument("--anchor", required=True, help="heading anchor without #")
    parser.add_argument(
        "--roadmap-rel",
        default="/docs/ROADMAP.md",
        help="path shown in the marker (default: /docs/ROADMAP.md)",
    )
    args = parser.parse_args()
    try:
        status = mark(args.scratch, args.anchor, args.roadmap_rel)
    except FileNotFoundError as exc:
        print(exc, file=sys.stderr)
        return 1
    print(f"{status}: {args.scratch}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
