#!/usr/bin/env python3
"""Ensure docs/ROADMAP.md exists with the standard header."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

HEADER_MARKER = "## Conventions"
ENTRY_STOP = "<!-- Entries append below this rule."


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def template_header() -> str:
    template = (
        Path(__file__).resolve().parents[1] / "references" / "roadmap-template.md"
    )
    text = template.read_text(encoding="utf-8")
    # Ledger header only: stop after the entries-append comment (entry shape
    # below that comment is author SoT, not copied into docs/ROADMAP.md).
    if ENTRY_STOP in text:
        idx = text.index(ENTRY_STOP)
        end = text.find("\n", idx)
        chunk = text if end == -1 else text[: end + 1]
        return chunk.rstrip() + "\n"
    if HEADER_MARKER not in text:
        raise SystemExit("roadmap-template.md missing Conventions section")
    return text.rstrip() + "\n"


def ensure(path: Path, *, force_header: bool = False) -> str:
    header = template_header()
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(header, encoding="utf-8")
        return "created"
    body = path.read_text(encoding="utf-8")
    if HEADER_MARKER in body and not force_header:
        return "exists"
    if force_header:
        # Preserve entries after first ## that is not "# Roadmap" / Conventions intro
        entries = _extract_entries(body)
        path.write_text(header + ("\n" + entries if entries else ""), encoding="utf-8")
        return "reset-header"
    path.write_text(header + "\n" + body.lstrip(), encoding="utf-8")
    return "prepended-header"


def _extract_entries(body: str) -> str:
    lines = body.splitlines()
    out: list[str] = []
    collecting = False
    for line in lines:
        if line.startswith("## ") and not line.startswith("## Conventions"):
            collecting = True
        if collecting:
            out.append(line)
    return "\n".join(out).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--path",
        type=Path,
        default=None,
        help="ROADMAP path (default: <repo>/docs/ROADMAP.md)",
    )
    parser.add_argument(
        "--force-header",
        action="store_true",
        help="rewrite header from template; keep existing ## entries",
    )
    args = parser.parse_args()
    path = args.path or (repo_root() / "docs" / "ROADMAP.md")
    status = ensure(path, force_header=args.force_header)
    print(f"{status}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
