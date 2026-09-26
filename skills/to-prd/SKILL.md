---
name: to-prd
description: >
  Author local OKF-shaped PRDs under docs/prd/ (gitignored): MVP journey, FRs,
  DoD, bug appendix; cite docs/adr via to-adr; diagrams via ascii. Use when turning
  a grilled idea into a product requirement doc or editing an existing PRD.
disable-model-invocation: true
---

# to-prd

Author **PRDs** — MVP scope, one critical journey, behavioral FRs, DoD, living bug appendix. Durable “why” lives in **ADRs** via **`to-adr`**, not here.

## Homes

- PRD home: `docs/prd/` (local-only; gitignored — see `docs/about-prd.md`)
- Filename: `NNNN-PRD-<slug>.md` (no project-key prefix)
- Catalog: `docs/prd/index.md` (local)
- ADR home: `docs/adr/` (tracked)

Missing ignore/scaffold → run **`setup-bmurrtech-skills`**.

## Action

- **New:** next `NNNN` = max in `docs/prd/` + 1 (first is `0001`). Write OKF frontmatter + body from [references/prd-template.md](references/prd-template.md). Update local `index.md`.
- **Edit:** only the user-specified file. Ambiguous create vs edit → ask.
- Proceed from conversation and existing docs; do not block on unanswered questionnaires.

### ADR — exist then cite / warrant then ask

| Branch | Action |
|--------|--------|
| User cites an ADR | Resolve path under `docs/adr/`; cite in Summary. Missing → say so; omit bullet. |
| Decision looks ADR-worthy (user asks, or warrant: costly to reverse · real alternatives · future “why?”) | If the grill thread is muddy, suggest **`handoff`** first. Ask once: create via **`to-adr`** now? Yes → run `to-adr`, then cite. No → todo and continue PRD. |

Skip the offer when warrant fails and the user did not ask.

### Diagrams

At least one ASCII diagram tied to UJ-1 or an FR — follow **`ascii`**.

## PRDs contain / do not

**Contain:** MVP definition, UJ-1, scope in/out/non-goals, behavioral FRs, phases (order only), DoD, bug appendix, ADR path cites, diagrams.

**Do not contain:** stack rationale / architecture “why” (→ `to-adr`); assumptions/constraints that belong in ADRs (cite instead).
