# Local PRDs (`docs/prd/`)

Product requirement documents for day-to-day work live under **`docs/prd/`** and are **gitignored** (local developer only).

## Layout

- Path: `docs/prd/NNNN-PRD-<slug>.md` (four-digit sequence, no project-key prefix)
- Each file is an OKF concept (YAML frontmatter + Markdown body)
- Local catalog: `docs/prd/index.md` (also gitignored)
- Author with the **`to-prd`** skill; cite ADRs under tracked `docs/adr/` via **`to-adr`**

## Tracked vs local

| Tracked | Local (ignored) |
|---------|-----------------|
| `docs/adr/` | `docs/prd/` |
| `CONTEXT.md`, `knowledge/` | PRD bodies and local PRD index |
| This file (`docs/about-prd.md`) | |

Consumers: run **`setup-bmurrtech-skills`** so `.gitignore` includes `/docs/prd/`.
