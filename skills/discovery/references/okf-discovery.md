# Discovery bundle (OKF v0.2)

Bundle layout, conformance, indexes. Markdown is the source of truth; `catalog.json` is an
optional rebuildable cache.

## Layout

```text
docs/discovery/
  index.md                    # lists team bundles only; no okf_version
  <team>/                     # one OKF bundle root per team
    index.md                  # okf_version: "0.2" only
    catalog.json              # optional cache
    <slug>.md                 # UseCase (stable; updated in place)
    YYYY-MM-DD-<slug>.md      # Capture (one per meeting)
    YYYY-MM-DD-ranking.md     # Ranking (one per rank run)
```

No type subfolders. Project is optional frontmatter (`project:`), not a nested bundle.

## Conformance

- Every concept file has YAML frontmatter with `type` (`Capture` · `UseCase` · `Ranking`).
- Only the team root `index.md` carries `okf_version`.
- Links are bundle-relative: `/slug.md`.
- `index.md` and `log.md` are reserved, not concepts.
- Preserve unknown frontmatter keys on rewrite.
- `generated.by: discovery/skill` on every write.

## Team index

```markdown
---
okf_version: "0.2"
---

# <Team> discovery

## Use cases

* [Title](/slug.md) - P1 · 73.3 | none · needs-discovery

## Captures

* [Meeting title](/YYYY-MM-DD-slug.md) - one line

## Rankings

* [YYYY-MM-DD](/YYYY-MM-DD-ranking.md) - n scored, m needs-discovery
```

## catalog.json

Rebuild from frontmatter after every write:

```json
{
  "okf_version": "0.2",
  "team": "<team>",
  "concepts": [
    {"id": "slug", "path": "slug.md", "type": "UseCase", "title": "…",
     "status": "scored", "priority": "P1", "overall": 73.3}
  ]
}
```

## First write

1. Ensure `docs/discovery/index.md` lists the team.
2. Create `<team>/index.md` (`okf_version` only in frontmatter).
3. Write concepts; refresh the team index and `catalog.json`.
