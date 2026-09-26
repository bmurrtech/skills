---
title: PRD
description: Local OKF product requirement documents under docs/prd (gitignored).
type: concept
tags: [prd]
---

# PRD

A **PRD** is an OKF concept file at `docs/prd/NNNN-PRD-<slug>.md` describing an MVP: journey, behavioral FRs, DoD, bug appendix.

## Rules

- Local-only — directory is gitignored; see [docs/about-prd.md](../docs/about-prd.md)
- No project-key prefix
- Cite ADRs under `docs/adr/`; do not put architecture rationale in the PRD
- Diagrams via `ascii`; new ADRs via `to-adr` when warranted

## Related

- Skill: [`skills/to-prd`](../skills/to-prd/SKILL.md)
- Glossary: [CONTEXT.md](../CONTEXT.md)
