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

## Shape

Authoring SoT ships with the skill (release artifact includes `skills/` only —
see [skills-release-artifact](skills-release-artifact.md)):

- Process + warrant + classify: [`skills/to-adr/SKILL.md`](../skills/to-adr/SKILL.md)
- Headings, placement, anti-bloat: [`skills/to-adr/references/mechanics.md`](../skills/to-adr/references/mechanics.md)
- Optional at-a-glance HTML: `skills/to-adr/scripts/build_catalog.py` → `.scratch/adr-optics/`
  (catalog row shape → [adr-catalog.md](adr-catalog.md))

Do **not** treat this OKF page as the only copy of the template — consumers
without `knowledge/` still author via the skill.

## Lifecycle

- **Accepted** files are immutable.
- Change course with a **new** ADR that **supersedes** the old path (bidirectional Status links + index).
- **Relate** when a new ADR preserves or extends an Accepted one — index Related (and optional Status **Related ADRs**); leave `Superseded by` empty.
- Citing an older ADR as a reason a **rejected option** fails is relate, not supersede.
- Create only when costly to reverse, alternatives were real, or future readers will ask why.

## Related

- Skill: [`skills/to-adr`](../skills/to-adr/SKILL.md)
- How-to: [docs/how-to-adr.md](../docs/how-to-adr.md)
- ADR: [0010](../docs/adr/0010-ADR-to-adr-mechanics-shipped.md) (supersedes 0003)
- Glossary: [CONTEXT.md](../CONTEXT.md)
