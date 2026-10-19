#!/usr/bin/env python3
"""Build GitHub Release notes from CHANGELOG + optional Donation CTA footer.

Extracts the dated ``## [<version>]`` section from Keep a Changelog markdown,
optionally appends an artifact/install blurb, then a CTA footer derived from
``.github/FUNDING.yml`` (preferred) or ``CONTEXT.md`` URL fallbacks.

Stdout = release body. Exit 1 if the version heading is missing.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

HEADING_RE = re.compile(
    r"^## \[([^\]]+)\](?:\s+-\s+\d{4}-\d{2}-\d{2})?\s*$",
    re.MULTILINE,
)

# FUNDING.yml key → (label, url builder). Username values only.
PLATFORM_URLS: dict[str, tuple[str, str]] = {
    "ko_fi": ("Ko-fi", "https://ko-fi.com/{user}"),
    "buy_me_a_coffee": ("Buy Me a Coffee", "https://www.buymeacoffee.com/{user}"),
    "patreon": ("Patreon", "https://www.patreon.com/{user}"),
    "open_collective": ("Open Collective", "https://opencollective.com/{user}"),
    "liberapay": ("Liberapay", "https://liberapay.com/{user}"),
    "issuehunt": ("IssueHunt", "https://issuehunt.io/r/{user}"),
    "polar": ("Polar", "https://polar.sh/{user}"),
    "thanks_dev": ("thanks.dev", "https://thanks.dev/u/{user}"),
}

BADGE: dict[str, str] = {
    "ko_fi": (
        "https://img.shields.io/badge/Ko--fi-Support%20the%20project"
        "-FF5E5B?style=for-the-badge&logo=ko-fi&logoColor=white"
    ),
    "buy_me_a_coffee": (
        "https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Support%20the%20project"
        "-FFDD00?style=for-the-badge&logo=buymeacoffee&logoColor=black"
    ),
}

CONTEXT_URL_RE = re.compile(
    r"https?://(?:www\.)?(ko-fi\.com|buymeacoffee\.com)/([A-Za-z0-9_-]+)",
    re.IGNORECASE,
)


def extract_section(changelog: str, version: str) -> str | None:
    """Return body under ``## [<version>]`` through the next ``## `` heading."""
    matches = list(HEADING_RE.finditer(changelog))
    for i, m in enumerate(matches):
        if m.group(1) != version:
            continue
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(changelog)
        body = changelog[start:end].strip("\n")
        heading = m.group(0).rstrip()
        return f"{heading}\n\n{body}".rstrip() + "\n"
    return None


def _strip_yaml_comment(value: str) -> str:
    if "#" in value:
        value = value.split("#", 1)[0]
    return value.strip().strip("'\"")


def parse_funding_yml(text: str) -> list[tuple[str, str, str]]:
    """Return list of (key, label, url) from FUNDING.yml usernames / custom URLs."""
    found: list[tuple[str, str, str]] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, rest = line.partition(":")
        key = key.strip()
        rest = _strip_yaml_comment(rest)
        if not rest:
            continue
        if key == "custom":
            # e.g. ['https://…', 'https://…'] or a single URL
            urls = re.findall(r"https?://[^\s'\"\],]+", rest)
            for u in urls:
                found.append(("custom", "Sponsor", u.rstrip("/")))
            continue
        if key == "github":
            users = re.findall(r"[A-Za-z0-9_-]+", rest)
            for u in users:
                found.append(
                    (
                        "github",
                        "GitHub Sponsors",
                        f"https://github.com/sponsors/{u}",
                    )
                )
            continue
        if key in PLATFORM_URLS and re.fullmatch(r"[A-Za-z0-9_-]+", rest):
            label, tmpl = PLATFORM_URLS[key]
            found.append((key, label, tmpl.format(user=rest)))
    return found


def parse_context_cta_urls(text: str) -> list[tuple[str, str, str]]:
    """Fallback: Ko-fi / Buy Me a Coffee URLs mentioned in CONTEXT.md."""
    found: list[tuple[str, str, str]] = []
    seen: set[str] = set()
    for m in CONTEXT_URL_RE.finditer(text):
        host, user = m.group(1).lower(), m.group(2)
        if host.startswith("ko-fi"):
            key, label, url = (
                "ko_fi",
                "Ko-fi",
                f"https://ko-fi.com/{user}",
            )
        else:
            key, label, url = (
                "buy_me_a_coffee",
                "Buy Me a Coffee",
                f"https://www.buymeacoffee.com/{user}",
            )
        if url in seen:
            continue
        seen.add(url)
        found.append((key, label, url))
    return found


def resolve_ctas(repo_root: Path) -> list[tuple[str, str, str]]:
    funding = repo_root / ".github" / "FUNDING.yml"
    if funding.is_file():
        ctas = parse_funding_yml(funding.read_text(encoding="utf-8"))
        if ctas:
            return ctas
    context = repo_root / "CONTEXT.md"
    if context.is_file():
        return parse_context_cta_urls(context.read_text(encoding="utf-8"))
    return []


def render_cta_footer(ctas: list[tuple[str, str, str]]) -> str:
    if not ctas:
        return ""
    lines = ["## Support", ""]
    bullets: list[str] = []
    badges: list[str] = []
    for key, label, url in ctas:
        bullets.append(f"- **[{label}]({url})**")
        badge_img = BADGE.get(key)
        if badge_img:
            badges.append(
                f'<a href="{url}" target="_blank" rel="noopener">'
                f'<img src="{badge_img}" alt="{label}"></a>'
            )
    lines.extend(bullets)
    if badges:
        lines.append("")
        lines.append('<p align="center">')
        lines.append("  " + "<!--\n  -->".join(badges))
        lines.append("</p>")
    lines.append("")
    return "\n".join(lines)


def build_notes(
    *,
    changelog_text: str,
    version: str,
    extra_note: str | None,
    ctas: list[tuple[str, str, str]],
) -> str:
    section = extract_section(changelog_text, version)
    if section is None:
        raise ValueError(f"No CHANGELOG heading ## [{version}] found")
    parts = [section.rstrip(), ""]
    if extra_note and extra_note.strip():
        parts.append(extra_note.strip())
        parts.append("")
    footer = render_cta_footer(ctas)
    if footer:
        parts.append(footer.rstrip())
        parts.append("")
    return "\n".join(parts).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", required=True, help="Semver without leading v")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path("."),
        help="Repo root (CHANGELOG, .github/FUNDING.yml, CONTEXT.md)",
    )
    parser.add_argument(
        "--changelog",
        type=Path,
        default=None,
        help="CHANGELOG path (default: <repo-root>/CHANGELOG.md)",
    )
    parser.add_argument(
        "--extra-note",
        default="",
        help="Optional install/artifact blurb appended after the CHANGELOG section",
    )
    parser.add_argument(
        "--no-cta",
        action="store_true",
        help="Omit Donation CTA footer even when FUNDING.yml / CONTEXT has URLs",
    )
    args = parser.parse_args(argv)

    root = args.repo_root.resolve()
    changelog_path = (args.changelog or root / "CHANGELOG.md").resolve()
    if not changelog_path.is_file():
        print(f"CHANGELOG not found: {changelog_path}", file=sys.stderr)
        return 1

    ctas: list[tuple[str, str, str]] = []
    if not args.no_cta:
        ctas = resolve_ctas(root)

    try:
        notes = build_notes(
            changelog_text=changelog_path.read_text(encoding="utf-8"),
            version=args.version,
            extra_note=args.extra_note or None,
            ctas=ctas,
        )
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    sys.stdout.write(notes)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
