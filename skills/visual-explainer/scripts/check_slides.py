#!/usr/bin/env python3
"""Structural floors for visual-explainer HTML slide decks (stdlib only).

Fails closed on missing shell marker, missing data-screen-label, empty action
titles, missing type-floor CSS tokens, and unresolved overflow markers.
Does not render the page — browser overflow remains the SlideEngine check.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SHELL_MARKER_RE = re.compile(
    r"""data-ve-deck-shell\s*=\s*["']1["']""",
    re.IGNORECASE,
)
ATTR_RE = re.compile(
    r"""([a-zA-Z_:][-a-zA-Z0-9_:.]*)\s*=\s*(["'])(.*?)\2""",
    re.DOTALL,
)
SCREEN_LABEL_RE = re.compile(r"""^\d{2}\s+\S""")
BODY_FLOOR_RE = re.compile(r"""--slide-body-min\s*:\s*\d+px""")
LABEL_FLOOR_RE = re.compile(r"""--slide-label-min\s*:\s*\d+px""")


def _attrs(open_tag_inner: str) -> dict[str, str]:
    return {m.group(1).lower(): m.group(3) for m in ATTR_RE.finditer(open_tag_inner)}


def _strip_comments(html: str) -> str:
    return re.sub(r"<!--.*?-->", "", html, flags=re.DOTALL)


def _slide_chunks(html: str) -> list[tuple[str, str]]:
    """Return list of (opening_attrs_blob, inner_html) per section.slide."""
    chunks: list[tuple[str, str]] = []
    body = _strip_comments(html)
    pos = 0
    while True:
        start = body.find("<section", pos)
        if start < 0:
            break
        tag_end = body.find(">", start)
        if tag_end < 0:
            break
        open_tag = body[start : tag_end + 1]
        if not re.search(r"""class=["'][^"']*\bslide\b""", open_tag, re.I):
            pos = tag_end + 1
            continue
        # Find matching close — naive depth for nested sections rare in slides
        depth = 1
        cursor = tag_end + 1
        inner_start = cursor
        closed = False
        while depth and cursor < len(body):
            next_open = body.find("<section", cursor)
            next_close = body.find("</section>", cursor)
            if next_close < 0:
                break
            if next_open >= 0 and next_open < next_close:
                depth += 1
                cursor = next_open + 8
            else:
                depth -= 1
                if depth == 0:
                    inner = body[inner_start:next_close]
                    attr_blob = open_tag[len("<section") : -1]
                    chunks.append((attr_blob, inner))
                    pos = next_close + len("</section>")
                    closed = True
                    break
                cursor = next_close + len("</section>")
        if not closed:
            pos = tag_end + 1
    return chunks


def _action_title(attrs: dict[str, str]) -> str:
    # Required attribute — heading text is not a substitute (shell contract).
    return attrs.get("data-action-title", "").strip()


def analyze(path: Path) -> dict:
    html = path.read_text(encoding="utf-8")
    failures: list[dict] = []

    if not SHELL_MARKER_RE.search(html):
        failures.append(
            {
                "kind": "missing_shell_marker",
                "detail": 'Root must keep data-ve-deck-shell="1" from deck-shell.html',
            }
        )

    if not BODY_FLOOR_RE.search(html) or not LABEL_FLOOR_RE.search(html):
        failures.append(
            {
                "kind": "missing_type_floor",
                "detail": "CSS must define --slide-body-min and --slide-label-min (px)",
            }
        )

    slides = _slide_chunks(html)
    if not slides:
        failures.append(
            {
                "kind": "no_slides",
                "detail": "No <section class=\"slide\"> found",
            }
        )

    for i, (attr_blob, inner) in enumerate(slides, start=1):
        attrs = _attrs(attr_blob)
        label = attrs.get("data-screen-label", "").strip()
        if not label or not SCREEN_LABEL_RE.match(label):
            failures.append(
                {
                    "kind": "missing_screen_label",
                    "slide": i,
                    "detail": 'Need data-screen-label like "01 Action title"',
                }
            )
        title = _action_title(attrs)
        if not title:
            failures.append(
                {
                    "kind": "empty_action_title",
                    "slide": i,
                    "detail": "Set data-action-title or non-empty display/heading",
                }
            )
        if re.search(
            r"""data-slide-check\s*=\s*["']overflow["']""",
            attr_blob,
            re.I,
        ):
            failures.append(
                {
                    "kind": "unresolved_overflow",
                    "slide": i,
                    "detail": "Remove data-slide-check=overflow before shipping",
                }
            )

    if not any(f["kind"] == "unresolved_overflow" for f in failures):
        if re.search(
            r"""data-slide-check\s*=\s*["']overflow["']""",
            html,
            re.I,
        ):
            failures.append(
                {
                    "kind": "unresolved_overflow",
                    "detail": "Unresolved data-slide-check=overflow in deck",
                }
            )

    return {
        "ok": not failures,
        "path": str(path),
        "slide_count": len(slides),
        "failures": failures,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Check visual-explainer slide deck structural floors"
    )
    parser.add_argument("html", type=Path, help="Path to deck HTML")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print full JSON report",
    )
    args = parser.parse_args(argv)
    if not args.html.is_file():
        print(f"error: not a file: {args.html}", file=sys.stderr)
        return 2
    report = analyze(args.html)
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        if report["ok"]:
            print(f"OK: {report['path']} ({report['slide_count']} slides)")
        else:
            print(f"FAIL: {report['path']}", file=sys.stderr)
            for f in report["failures"]:
                slide = f.get("slide")
                prefix = f"slide {slide}: " if slide else ""
                print(f"  - {f['kind']}: {prefix}{f['detail']}", file=sys.stderr)
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
