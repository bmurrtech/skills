---
title: ADR catalog
description: Seam map for to-adr build_catalog parse + at-a-glance visualizer.
type: test-map
tags: [tests, adr, to-adr]
---

# ADR catalog (test map)

## Seam

`skills/to-adr/scripts/build_catalog.py` public contract: parse ADR Status/synopsis,
build catalog without requiring index rewrite, write visualizer HTML + JSON under
`.scratch/adr-optics/` by default (escapes `<` in embedded JSON; `--open` launches browser).

Catalog rows intentionally include full ADR `markdown` and recent git `history`
so the offline at-a-glance HTML can show bodies without re-reading `docs/adr/`.
Do not slim the JSON for “list view” unless the visualizer is split into a
list-only payload plus on-demand body fetch.

## Run

```bash
python3 -m unittest tests.test_adr_catalog -v
```

## Tests

- `tests/test_adr_catalog.py`

## Related

- Concept: [adr.md](adr.md)
- Skill: [`skills/to-adr`](../skills/to-adr/SKILL.md)
- How-to: [docs/how-to-adr.md](../docs/how-to-adr.md)
