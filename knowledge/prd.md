---
title: PRD
description: Local OKF product requirement documents under docs/prd (gitignored).
type: concept
tags: [prd]
---

# PRD

A **PRD** is an OKF concept file at `docs/prd/NNNN-PRD-<slug>.md` describing an
MVP: journey, behavioral FRs, DoD, bug appendix.

## Why local (gitignored)

Day-to-day product specs churn and are often personal or premature for the
remote. Keeping `docs/prd/` ignored avoids PR noise while still giving
**`to-prd`** / **`implement`** a stable home. Cite tracked ADRs when decisions
harden. Setup ensures the ignore rule but does **not** copy a library explainer
into the consumer ([ADR 0007](../docs/adr/0007-ADR-scaffold-omit-about-prd.md)).

Human how-to (layout + flows): [docs/how-to-bmurrtech-skills.md](../docs/how-to-bmurrtech-skills.md#local-prds-docsprd).
Library pointer file (ADR 0007): [docs/about-prd.md](../docs/about-prd.md).

## Rules

- Local-only — directory is gitignored
- No project-key prefix
- Cite ADRs under `docs/adr/`; do not put architecture rationale in the PRD
- Diagrams via `ascii`; new ADRs via `to-adr` when warranted

## Related

- Skill: [`skills/to-prd`](../skills/to-prd/SKILL.md)
- Scaffold why: [skill-scaffold.md](skill-scaffold.md)
- Glossary: [CONTEXT.md](../CONTEXT.md)
