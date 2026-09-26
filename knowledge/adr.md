---
title: ADR
description: Markdown Architectural Decision Records under docs/adr with an index catalog.
type: concept
tags: [adr, decisions]
---

# ADR

An **ADR** records one significant decision: context, options, and outcome.

## Location

- Directory: [`docs/adr/`](../docs/adr/)
- Filename: `NNNN-ADR-<slug>.md` (four-digit sequence, no project-key prefix)
- Catalog: [`docs/adr/index.md`](../docs/adr/index.md)

## Shape (MADR-compatible)

Required headings: Status; Context and Problem Statement; Decision Drivers; Considered Options; Decision Outcome (with Consequences); Pros and Cons of the Options. Include Assumptions, Constraints, and Implementation Notes when they bind later work.

## Lifecycle

- **Accepted** files are immutable.
- Change course with a **new** ADR that supersedes the old path.
- Create only when costly to reverse, alternatives were real, or future readers will ask why.

## Related

- Skill: [`skills/to-adr`](../skills/to-adr/SKILL.md)
- Glossary: [CONTEXT.md](../CONTEXT.md)
