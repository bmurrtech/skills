---
title: ADR catalog
description: Seam map for create-adr build_catalog parse, lineage, dual-write catalog, at-a-glance visualizer.
type: test-map
tags: [tests, adr, create-adr]
---

# ADR catalog (test map)

## Seam

`skills/create-adr/scripts/build_catalog.py` public contract:

- Parse ADR Status (title, author status → OKF status, date, supersedes /
  superseded-by links, related links) without requiring the rest of the template.
- Build supersession **decision lineage** (`lineage_edges`, per-record `lineage`,
  `issues`). Public `supersedes` / `superseded_by` come from the same graph
  (predecessors / successors). Edges have no strength field. Exit non-zero only
  for `invalid_lineage` after writing artifacts.
- Always write slim tracked `docs/adr/catalog.json` (`schema_version` 2; no
  wall-clock `generated.at` — fat/scratch only).
- Opt-in `--write-index` rewrites `docs/adr/index.md` (Related + lineage review).
- `--visualize` writes fat JSON + HTML under `.scratch/adr-optics/` by default
  (escapes `<` in embedded JSON; `--open` launches browser). Fat rows keep full
  `markdown` + git `history` for the offline pane.

Do not slim the scratch JSON for “list view” unless the visualizer is split into
a list-only payload plus on-demand body fetch. Home `catalog.json` stays slim
(no `markdown` / `history` / `search_text`).

## Run

```bash
python3 -m unittest tests.test_adr_catalog -v
```

## Tests

- `tests/test_adr_catalog.py`

## Related

- Concept: [adr.md](adr.md)
- Skill: [`skills/create-adr`](../skills/create-adr/SKILL.md)
- How-to: [docs/how-to-adr.md](../docs/how-to-adr.md)
