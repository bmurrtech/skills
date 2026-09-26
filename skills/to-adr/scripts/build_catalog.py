"""Build a local ADR catalog and self-contained at-a-glance visualizer.

Reads Markdown ADRs from --home, optionally refreshes index.md, and with
--visualize writes catalog JSON + HTML under --out (default: .scratch/adr-optics/).
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import webbrowser
from datetime import datetime
from pathlib import Path

CATALOG_NAME = "adr-catalog.json"
VISUALIZER_NAME = "adr-at-a-glance.html"
TEMPLATE = Path(__file__).with_name("visualizer_template.html")
INDEX_NAME = "index.md"

_LINK = re.compile(r"\[[^\]]+\]\(([^)\s]+\.md(?:#[^)\s]+)?)\)", re.IGNORECASE)
_ADR_FILE = re.compile(r"(?:^|-)(\d{4})-ADR-", re.IGNORECASE)
_STATUS_MAP = {
    "proposed": "draft",
    "draft": "draft",
    "accepted": "stable",
    "stable": "stable",
    "deprecated": "deprecated",
    "superceded": "deprecated",
    "superseded": "deprecated",
}


def _section(text: str, heading: str) -> str:
    match = re.search(
        rf"^##\s+{re.escape(heading)}\s*$\n(?P<body>.*?)(?=^##\s|\Z)",
        text,
        re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    return match.group("body").strip() if match else ""


def _first_paragraphs(text: str) -> str:
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip()]
    raw = " ".join(paragraphs) if paragraphs else ""
    return re.sub(r"\s+", " ", raw).strip()


def _synopsis_fallback(text: str) -> str:
    remainder = re.sub(r"^#\s+.+$", "", text, count=1, flags=re.MULTILINE)
    remainder = re.sub(r"<!--.*?-->", "", remainder, flags=re.DOTALL)
    kept = []
    for paragraph in [part.strip() for part in re.split(r"\n\s*\n", remainder) if part.strip()]:
        first = paragraph.splitlines()[0].strip()
        if re.match(r"^##\s+", first):
            continue
        if re.match(
            r"^(Proposed|Draft|Accepted|Stable|Deprecated|Superceded|Superseded)\b",
            first,
            re.IGNORECASE,
        ):
            continue
        if re.match(r"^[-*]\s+", first):
            continue
        kept.append(paragraph)
    return _first_paragraphs("\n\n".join(kept))


def _synopsis(text: str) -> str:
    problem = _section(text, "Context and Problem Statement")
    body = _first_paragraphs(problem) if problem else _synopsis_fallback(text)
    if not body:
        title_match = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
        body = title_match.group(1).strip() if title_match else ""
    return body[:400] + ("…" if len(body) > 400 else "")


def _related_kind(link: str) -> str:
    name = Path(link.split("#", 1)[0]).name
    if re.search(r"-ADR-", name, re.IGNORECASE) or re.match(r"\d{4}-ADR-", name, re.IGNORECASE):
        return "adr"
    if re.search(r"-PRD-", name, re.IGNORECASE):
        return "prd"
    return "other"


def _git_history(path: Path, limit: int = 8) -> list[dict]:
    try:
        proc = subprocess.run(
            [
                "git",
                "log",
                "--follow",
                f"-{limit}",
                "--format=%H\t%aI\t%an\t%s",
                "--",
                str(path),
            ],
            cwd=path.parent,
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError:
        return []
    if proc.returncode != 0 or not proc.stdout.strip():
        return []
    rows = []
    for line in proc.stdout.splitlines():
        parts = line.split("\t", 3)
        if len(parts) < 4:
            continue
        rows.append(
            {
                "hash": parts[0][:7],
                "date": parts[1],
                "author": parts[2],
                "subject": parts[3],
            }
        )
    return rows


def _normalized_link(link: str) -> str:
    path = link.split("#", 1)[0].replace("\\", "/")
    return path if path.startswith("/") else f"/{path}"


def _status_field_links(status_body: str, field: str) -> list[str]:
    """Links on a Status bullet for Supersedes / Superseded by / Related ADRs / Related PRDs."""
    pattern = re.compile(
        rf"^\s*[-*]?\s*(?:\*\*)?{re.escape(field)}(?:\*\*)?\s*:\s*(.+)$",
        re.MULTILINE | re.IGNORECASE,
    )
    match = pattern.search(status_body)
    if not match:
        return []
    value = match.group(1).strip()
    if value in {"—", "-", "–", ""}:
        return []
    return list(dict.fromkeys(_normalized_link(link) for link in _LINK.findall(value)))


def parse_adr(path: Path, home: Path) -> dict:
    text = path.read_text(encoding="utf-8-sig")
    title_match = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
    status_body = _section(text, "Status")
    status_match = re.search(
        r"^\s*(?:[-*]\s*)?(Proposed|Draft|Accepted|Stable|Deprecated|Superceded|Superseded)\b",
        status_body,
        re.MULTILINE | re.IGNORECASE,
    )
    raw_status = status_match.group(1).casefold() if status_match else "draft"
    date_match = re.search(
        r"^\s*[-*]?\s*(?:\*\*)?Date[^0-9\n]*(\d{4}-\d{2}-\d{2})",
        status_body,
        re.MULTILINE | re.IGNORECASE,
    )
    links = list(dict.fromkeys(_normalized_link(link) for link in _LINK.findall(text)))
    body = re.sub(r"\s+", " ", text).strip()
    relative = "/" + path.relative_to(home).as_posix()
    number_match = _ADR_FILE.search(path.name)
    synopsis = _synopsis(text)
    supersedes = _status_field_links(status_body, "Supersedes")
    superseded_by = _status_field_links(status_body, "Superseded by")
    related_adrs = _status_field_links(status_body, "Related ADRs")
    related_prds = _status_field_links(status_body, "Related PRDs")
    return {
        "path": relative,
        "slug": path.stem,
        "type": "ADR",
        "number": number_match.group(1) if number_match else "",
        "title": title_match.group(1).strip() if title_match else path.stem,
        "status": _STATUS_MAP.get(raw_status, "draft"),
        "status_raw": raw_status,
        "date": date_match.group(1) if date_match else None,
        "month": date_match.group(1)[:7] if date_match else "",
        "related": links,
        "related_kinds": list(dict.fromkeys(_related_kind(link) for link in links)),
        "supersedes": supersedes,
        "superseded_by": superseded_by,
        "related_adrs": related_adrs,
        "related_prds": related_prds,
        "synopsis": synopsis,
        "markdown": text,
        "history": _git_history(path),
        "search_text": f"{path.name} {body}".casefold(),
    }


def _related_cell(decision: dict) -> str:
    bits: list[str] = []
    for target in decision.get("superseded_by") or []:
        name = Path(target).name
        bits.append(f"superseded by [{name}]({target.lstrip('/')})")
    for target in decision.get("supersedes") or []:
        name = Path(target).name
        bits.append(f"supersedes [{name}]({target.lstrip('/')})")
    for target in decision.get("related_adrs") or []:
        name = Path(target).name
        bits.append(f"relates [{name}]({target.lstrip('/')})")
    for target in decision.get("related_prds") or []:
        name = Path(target).name
        bits.append(f"[{name}]({target.lstrip('/')})")
    return "; ".join(bits) if bits else "—"


def write_index(home: Path, decisions: list[dict]) -> Path:
    """Write the git-tracked Markdown catalog, including a valid empty home."""
    lines = [
        "# ADR index",
        "",
        "| NNNN | Title | Status | Path | Related |",
        "|------|-------|--------|------|---------|",
    ]
    if not decisions:
        lines.append("| — | _No decisions recorded._ | — | — | — |")
    else:
        for decision in decisions:
            path = decision["path"].lstrip("/")
            title = decision["title"].replace("|", r"\|")
            lines.append(
                f"| {decision['number'] or '—'} | {title} | "
                f"{decision['status_raw'].title()} | "
                f"[{path}]({path}) | {_related_cell(decision)} |"
            )
    output = home / INDEX_NAME
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return output


def _is_adr_file(path: Path) -> bool:
    name = path.name.casefold()
    if name in {INDEX_NAME.casefold(), "log.md"}:
        return False
    return bool(re.search(r"(?:^|-)\d{4}-adr-", name))


def build_catalog(home: Path, *, write_index_md: bool = False) -> dict:
    home.mkdir(parents=True, exist_ok=True)
    decisions = [
        parse_adr(path, home)
        for path in sorted(home.glob("*.md"))
        if _is_adr_file(path)
    ]
    decisions.sort(key=lambda item: (item["date"] is None, item["date"] or "", item["path"]))
    if write_index_md:
        write_index(home, decisions)
    return {
        "generated": {
            "by": "bmurrtech/skills/to-adr",
            "at": datetime.now().astimezone().isoformat(),
        },
        "decisions": decisions,
    }


def write_visualizer(out_dir: Path, catalog: dict) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    safe = json.dumps(catalog, ensure_ascii=False).replace("<", "\\u003c")
    html = TEMPLATE.read_text(encoding="utf-8").replace("__CATALOG_JSON__", safe)
    output = out_dir / VISUALIZER_NAME
    output.write_text(html, encoding="utf-8")
    (out_dir / CATALOG_NAME).write_text(
        json.dumps(catalog, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--home",
        type=Path,
        default=Path("docs/adr"),
        help="ADR home (default: docs/adr)",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path(".scratch/adr-optics"),
        help="Directory for catalog JSON + visualizer HTML (default: .scratch/adr-optics)",
    )
    parser.add_argument(
        "--visualize",
        action="store_true",
        help=f"Write {VISUALIZER_NAME} and {CATALOG_NAME} under --out",
    )
    parser.add_argument(
        "--open",
        action="store_true",
        help="Open the visualizer in the default browser after --visualize",
    )
    parser.add_argument(
        "--write-index",
        action="store_true",
        help="Rewrite docs/adr/index.md from Status links (opt-in; agent-edited Related may be richer)",
    )
    args = parser.parse_args()
    home = args.home.resolve()
    catalog = build_catalog(home, write_index_md=args.write_index)
    result = {
        "ok": True,
        "home": str(home),
        "count": len(catalog["decisions"]),
        "index": str(home / INDEX_NAME) if args.write_index else None,
    }
    if args.visualize:
        out_dir = args.out.resolve()
        visualizer = write_visualizer(out_dir, catalog)
        result["visualizer"] = str(visualizer)
        result["catalog"] = str(out_dir / CATALOG_NAME)
        if args.open:
            uri = visualizer.as_uri()
            result["opened"] = bool(webbrowser.open(uri))
            result["file_uri"] = uri
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
