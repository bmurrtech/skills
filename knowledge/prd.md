---
title: PRD
description: OKF product requirement documents under docs/prd (ignore or track via setup).
type: concept
tags: [prd]
---

# PRD

A **PRD** is an OKF concept file at `docs/prd/NNNN-PRD-<slug>.md` describing an
MVP: journey, behavioral FRs, DoD, bug appendix.

## Track vs ignore

**Default (setup A):** `docs/prd/` is gitignored — day-to-day specs churn and
stay local while **`to-prd`** / **`implement`** still have a stable home.

**Opt-in (setup B):** track `docs/prd/` so teammates and remote agents share
PRD context from the repo. Setup re-asks on every run and retargets
`.gitignore` + `AGENTS.md` (+ `CONTEXT.md` when applicable).

Decision: [ADR 0013](../docs/adr/0013-ADR-prd-tracking-choice.md) (setup still
omits `about-prd.md` from the consumer).

Human how-to: [docs/how-to-bmurrtech-skills.md](../docs/how-to-bmurrtech-skills.md#prds-docsprd).
Library pointer: [docs/about-prd.md](../docs/about-prd.md).

## Rules

- Home is always `docs/prd/` — policy is ignore **or** track, not a different path
- No project-key prefix
- Cite ADRs under `docs/adr/`; do not put architecture rationale in the PRD
- Diagrams via `ascii`; new ADRs via `to-adr` when warranted

## Related

- Skill: [`skills/to-prd`](../skills/to-prd/SKILL.md)
- Setup choice: [`skills/setup-bmurrtech-skills/references/prd-tracking.md`](../skills/setup-bmurrtech-skills/references/prd-tracking.md)
- Scaffold why: [skill-scaffold.md](skill-scaffold.md)
- Glossary: [CONTEXT.md](../CONTEXT.md)
