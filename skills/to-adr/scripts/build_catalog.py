"""Build a local ADR decision catalog and optional at-a-glance visualizer.

Reads Markdown ADRs from --home. Always writes slim docs/adr/catalog.json
(schema_version 2) beside index.md. With --visualize, writes fat JSON + HTML
under --out (default: .scratch/adr-optics/). Exits non-zero on invalid_lineage
after writing catalog/index artifacts.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import webbrowser
from collections import defaultdict, deque
from datetime import datetime
from pathlib import Path

CATALOG_NAME = "catalog.json"
SCRATCH_CATALOG_NAME = "adr-catalog.json"
VISUALIZER_NAME = "adr-at-a-glance.html"
TEMPLATE = Path(__file__).with_name("visualizer_template.html")
INDEX_NAME = "index.md"
SCHEMA_VERSION = 2

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
_SLIM_DROP = frozenset({"markdown", "history", "search_text"})


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


def _stem_from_link(link: str) -> str:
    return Path(link.split("#", 1)[0]).stem


def _status_field_raw(status_body: str, field: str) -> str | None:
    # Accept **Field:** value (colon inside bold) and **Field**: value.
    pattern = re.compile(
        rf"^\s*[-*]?\s*(?:\*\*)?{re.escape(field)}(?:\*\*)?\s*:\s*(?:\*\*)?\s*(.+)$",
        re.MULTILINE | re.IGNORECASE,
    )
    match = pattern.search(status_body)
    if not match:
        return None
    return match.group(1).strip()


def _status_field_links(status_body: str, field: str) -> list[str]:
    """Links on a Status bullet for Supersedes / Superseded by / Related ADRs / Related PRDs."""
    value = _status_field_raw(status_body, field)
    if value is None or value in {"—", "-", "–", ""}:
        return []
    return list(dict.fromkeys(_normalized_link(link) for link in _LINK.findall(value)))


def _field_is_malformed(status_body: str, field: str) -> bool:
    value = _status_field_raw(status_body, field)
    if value is None or value in {"—", "-", "–", ""}:
        return False
    return not _LINK.search(value)


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
        "supersedes": [_stem_from_link(link) for link in supersedes],
        "supersedes_paths": supersedes,
        "superseded_by": [_stem_from_link(link) for link in superseded_by],
        "superseded_by_paths": superseded_by,
        "related_adrs": related_adrs,
        "related_prds": related_prds,
        "malformed_supersedes": _field_is_malformed(status_body, "Supersedes"),
        "malformed_superseded_by": _field_is_malformed(status_body, "Superseded by"),
        "synopsis": synopsis,
        "markdown": text,
        "history": _git_history(path),
        "search_text": f"{path.name} {body}".casefold(),
    }


def _issue(code: str, message: str, decisions: list[str]) -> dict:
    return {"code": code, "message": message, "decisions": decisions}


def _find_cycles(adj: dict[str, set[str]]) -> list[list[str]]:
    """Return strongly connected components that contain a cycle (Tarjan)."""
    cycles: list[list[str]] = []
    seen_cycle_keys: set[frozenset[str]] = set()
    nodes = sorted(adj)
    index: dict[str, int] = {}
    lowlink: dict[str, int] = {}
    stack: list[str] = []
    on_stack: set[str] = set()
    counter = 0

    def strongconnect(node: str) -> None:
        nonlocal counter
        index[node] = counter
        lowlink[node] = counter
        counter += 1
        stack.append(node)
        on_stack.add(node)
        for nxt in sorted(adj.get(node, ())):
            if nxt not in index:
                strongconnect(nxt)
                lowlink[node] = min(lowlink[node], lowlink[nxt])
            elif nxt in on_stack:
                lowlink[node] = min(lowlink[node], index[nxt])
        if lowlink[node] == index[node]:
            component: list[str] = []
            while True:
                member = stack.pop()
                on_stack.discard(member)
                component.append(member)
                if member == node:
                    break
            if len(component) > 1 or (len(component) == 1 and component[0] in adj.get(component[0], ())):
                key = frozenset(component)
                if key not in seen_cycle_keys:
                    seen_cycle_keys.add(key)
                    cycles.append(sorted(component))

    for node in nodes:
        if node not in index:
            strongconnect(node)
    return cycles


def _resolve_decision(
    link: str,
    by_slug: dict[str, dict],
    by_path: dict[str, dict],
    by_name: dict[str, dict],
) -> dict | None:
    if link in by_path:
        return by_path[link]
    name = Path(link).name
    if name in by_name:
        return by_name[name]
    return by_slug.get(Path(link).stem)


def _collect_lineage_edges(
    decisions: list[dict],
) -> tuple[list[dict], list[dict], bool, dict[str, set[str]], dict[str, set[str]]]:
    """Pure graph build from Status links. Does not mutate decision rows."""
    by_slug = {d["slug"]: d for d in decisions}
    by_path = {d["path"]: d for d in decisions}
    by_name = {Path(d["path"]).name: d for d in decisions}

    edge_keys: dict[tuple[str, str], dict] = {}
    issues: list[dict] = []
    invalid = False

    for decision in decisions:
        if decision.get("malformed_supersedes") or decision.get("malformed_superseded_by"):
            issues.append(
                _issue(
                    "malformed_supersession",
                    f"{decision['slug']}: Supersedes/Superseded by label has no Markdown link",
                    [decision["slug"]],
                )
            )

        # Canonical: replacement declares Supersedes → older; edge older → replacement
        for link in decision.get("supersedes_paths") or []:
            older = _resolve_decision(link, by_slug, by_path, by_name)
            if older is None:
                issues.append(
                    _issue(
                        "unresolved_supersession",
                        f"{decision['slug']} supersedes unresolved target {link}",
                        [decision["slug"]],
                    )
                )
                continue
            if older["slug"] == decision["slug"]:
                invalid = True
                issues.append(
                    _issue(
                        "invalid_lineage",
                        f"{decision['slug']}: self-target supersession",
                        [decision["slug"]],
                    )
                )
                continue
            key = (older["slug"], decision["slug"])
            edge_keys[key] = {
                "from": older["slug"],
                "to": decision["slug"],
                "type": "supersedes",
            }

        # Mirror: older declares Superseded by → newer; edge older → newer
        for link in decision.get("superseded_by_paths") or []:
            newer = _resolve_decision(link, by_slug, by_path, by_name)
            if newer is None:
                issues.append(
                    _issue(
                        "unresolved_supersession",
                        f"{decision['slug']} superseded by unresolved target {link}",
                        [decision["slug"]],
                    )
                )
                continue
            if newer["slug"] == decision["slug"]:
                invalid = True
                issues.append(
                    _issue(
                        "invalid_lineage",
                        f"{decision['slug']}: self-target superseded-by",
                        [decision["slug"]],
                    )
                )
                continue
            key = (decision["slug"], newer["slug"])
            edge_keys.setdefault(
                key,
                {
                    "from": decision["slug"],
                    "to": newer["slug"],
                    "type": "supersedes",
                },
            )

    adj: dict[str, set[str]] = defaultdict(set)
    for frm, to in edge_keys:
        adj[frm].add(to)

    for cycle in _find_cycles(adj):
        invalid = True
        issues.append(
            _issue(
                "invalid_lineage",
                "cycle among " + ", ".join(cycle),
                cycle,
            )
        )
        cycle_set = set(cycle)
        for key in list(edge_keys):
            if key[0] in cycle_set and key[1] in cycle_set:
                del edge_keys[key]

    adj = defaultdict(set)
    rev: dict[str, set[str]] = defaultdict(set)
    for frm, to in edge_keys:
        adj[frm].add(to)
        rev[to].add(frm)

    for decision in decisions:
        successors = sorted(adj.get(decision["slug"], ()))
        if len(successors) > 1:
            issues.append(
                _issue(
                    "multiple_successors",
                    f"{decision['slug']} has several successors: {', '.join(successors)}",
                    [decision["slug"], *successors],
                )
            )

    edges = [edge_keys[key] for key in sorted(edge_keys)]
    return edges, issues, invalid, adj, rev


def _lineage_for_slug(
    slug: str,
    adj: dict[str, set[str]],
    rev: dict[str, set[str]],
) -> dict:
    predecessors = sorted(rev.get(slug, ()))
    successors = sorted(adj.get(slug, ()))

    ancestors: set[str] = set()
    queue = deque(predecessors)
    while queue:
        node = queue.popleft()
        if node in ancestors:
            continue
        ancestors.add(node)
        queue.extend(rev.get(node, ()))

    descendants: set[str] = set()
    queue = deque(successors)
    while queue:
        node = queue.popleft()
        if node in descendants:
            continue
        descendants.add(node)
        queue.extend(adj.get(node, ()))

    if not predecessors:
        roots = [slug]
    else:
        seen: set[str] = set()
        walk = deque(predecessors)
        roots_acc: list[str] = []
        while walk:
            node = walk.popleft()
            if node in seen:
                continue
            seen.add(node)
            preds = rev.get(node, ())
            if not preds:
                roots_acc.append(node)
            else:
                walk.extend(preds)
        roots = sorted(set(roots_acc))

    depth = 0
    if predecessors:
        memo: dict[str, int] = {}

        def longest(node: str) -> int:
            if node in memo:
                return memo[node]
            preds = rev.get(node, ())
            if not preds:
                memo[node] = 0
                return 0
            memo[node] = 1 + max(longest(p) for p in preds)
            return memo[node]

        depth = longest(slug)

    return {
        "predecessors": predecessors,
        "successors": successors,
        "roots": roots,
        "ancestors": sorted(ancestors),
        "descendants": sorted(descendants),
        "depth": depth,
    }


_PARSE_ONLY = (
    "supersedes_paths",
    "superseded_by_paths",
    "malformed_supersedes",
    "malformed_superseded_by",
)


def _attach_lineage(
    decisions: list[dict],
    adj: dict[str, set[str]],
    rev: dict[str, set[str]],
) -> list[dict]:
    """Return public decision rows with graph-derived supersedes fields + lineage."""
    attached: list[dict] = []
    for decision in decisions:
        row = {key: value for key, value in decision.items() if key not in _PARSE_ONLY}
        lineage = _lineage_for_slug(row["slug"], adj, rev)
        # Both public fields come from the same supersession graph
        row["supersedes"] = list(lineage["predecessors"])
        row["superseded_by"] = list(lineage["successors"])
        row["lineage"] = lineage
        attached.append(row)
    return attached


def link_lineage(decisions: list[dict]) -> tuple[list[dict], list[dict], bool]:
    """Build supersession edges + issues; rewrite decisions in-place with public rows.

    Returns (edges, issues, has_invalid_lineage). Graph build is pure; attach copies
    rows then replaces the caller's list contents so callers keep the same list object.
    """
    edges, issues, invalid, adj, rev = _collect_lineage_edges(decisions)
    attached = _attach_lineage(decisions, adj, rev)
    decisions[:] = attached
    return edges, issues, invalid


def _related_cell(decision: dict, issues: list[dict]) -> str:
    bits: list[str] = []
    for target in decision.get("superseded_by") or []:
        bits.append(f"superseded by [{target}]({target}.md)")
    for target in decision.get("supersedes") or []:
        bits.append(f"supersedes [{target}]({target}.md)")
    for target in decision.get("related_adrs") or []:
        name = Path(target).name
        bits.append(f"relates [{name}]({target.lstrip('/')})")
    for target in decision.get("related_prds") or []:
        name = Path(target).name
        bits.append(f"[{name}]({target.lstrip('/')})")
    slug = decision["slug"]
    reviews = [
        f"`{issue['code']}`" for issue in issues if slug in (issue.get("decisions") or [])
    ]
    if reviews:
        bits.append("lineage review: " + ", ".join(dict.fromkeys(reviews)))
    return "; ".join(bits) if bits else "—"


def write_index(home: Path, decisions: list[dict], issues: list[dict]) -> Path:
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
                f"[{path}]({path}) | {_related_cell(decision, issues)} |"
            )
    output = home / INDEX_NAME
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return output


def _is_adr_file(path: Path) -> bool:
    name = path.name.casefold()
    if name in {INDEX_NAME.casefold(), CATALOG_NAME.casefold(), "log.md"}:
        return False
    return bool(re.search(r"(?:^|-)\d{4}-adr-", name))


def _slim_decision(decision: dict) -> dict:
    return {key: value for key, value in decision.items() if key not in _SLIM_DROP}


def _catalog_payload(
    decisions: list[dict],
    edges: list[dict],
    issues: list[dict],
    *,
    slim: bool,
) -> dict:
    rows = [_slim_decision(d) for d in decisions] if slim else decisions
    generated: dict[str, str] = {"by": "bmurrtech/skills/to-adr"}
    if not slim:
        # Fat/scratch only — keep slim tracked catalog free of wall-clock churn
        generated["at"] = datetime.now().astimezone().isoformat()
    return {
        "schema_version": SCHEMA_VERSION,
        "generated": generated,
        "decisions": rows,
        "lineage_edges": edges,
        "issues": issues,
    }


def write_home_catalog(home: Path, catalog: dict) -> Path:
    output = home / CATALOG_NAME
    output.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return output


def build_catalog(home: Path, *, write_index_md: bool = False) -> tuple[dict, dict, bool]:
    """Return (fat_catalog, slim_catalog, has_invalid_lineage)."""
    home.mkdir(parents=True, exist_ok=True)
    decisions = [
        parse_adr(path, home)
        for path in sorted(home.glob("*.md"))
        if _is_adr_file(path)
    ]
    decisions.sort(key=lambda item: (item["date"] is None, item["date"] or "", item["path"]))
    edges, issues, invalid = link_lineage(decisions)
    if write_index_md:
        write_index(home, decisions, issues)
    fat = _catalog_payload(decisions, edges, issues, slim=False)
    slim = _catalog_payload(decisions, edges, issues, slim=True)
    return fat, slim, invalid


def write_visualizer(out_dir: Path, catalog: dict) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    safe = json.dumps(catalog, ensure_ascii=False).replace("<", "\\u003c")
    html = TEMPLATE.read_text(encoding="utf-8").replace("__CATALOG_JSON__", safe)
    output = out_dir / VISUALIZER_NAME
    output.write_text(html, encoding="utf-8")
    (out_dir / SCRATCH_CATALOG_NAME).write_text(
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
        help="Directory for fat catalog JSON + visualizer HTML (default: .scratch/adr-optics)",
    )
    parser.add_argument(
        "--visualize",
        action="store_true",
        help=f"Write {VISUALIZER_NAME} and {SCRATCH_CATALOG_NAME} under --out",
    )
    parser.add_argument(
        "--open",
        action="store_true",
        help="Open the visualizer in the default browser after --visualize",
    )
    parser.add_argument(
        "--write-index",
        action="store_true",
        help="Rewrite docs/adr/index.md from Status links + lineage issues (opt-in)",
    )
    args = parser.parse_args()
    home = args.home.resolve()
    fat, slim, invalid = build_catalog(home, write_index_md=args.write_index)
    home_catalog = write_home_catalog(home, slim)
    result = {
        "ok": not invalid,
        "home": str(home),
        "count": len(fat["decisions"]),
        "schema_version": SCHEMA_VERSION,
        "catalog": str(home_catalog),
        "issues": fat["issues"],
        "lineage_edges": len(fat["lineage_edges"]),
        "index": str(home / INDEX_NAME) if args.write_index else None,
        "invalid_lineage": invalid,
    }
    if args.visualize:
        out_dir = args.out.resolve()
        visualizer = write_visualizer(out_dir, fat)
        result["visualizer"] = str(visualizer)
        result["scratch_catalog"] = str(out_dir / SCRATCH_CATALOG_NAME)
        if args.open:
            uri = visualizer.as_uri()
            result["opened"] = bool(webbrowser.open(uri))
            result["file_uri"] = uri
    print(json.dumps(result, indent=2))
    return 1 if invalid else 0


if __name__ == "__main__":
    raise SystemExit(main())
