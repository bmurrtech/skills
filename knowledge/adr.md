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
- Index: [`docs/adr/index.md`](../docs/adr/index.md)
- Decision catalog (slim, tracked): [`docs/adr/catalog.json`](../docs/adr/catalog.json)

## Shape

Authoring SoT ships with the skill (release artifact includes `skills/` only —
see [skills-release-artifact](skills-release-artifact.md)):

- Process + warrant + classify: [`skills/create-adr/SKILL.md`](../skills/create-adr/SKILL.md)
- Headings, placement, anti-bloat: [`skills/create-adr/references/mechanics.md`](../skills/create-adr/references/mechanics.md)
- Optional at-a-glance HTML: `skills/create-adr/scripts/build_catalog.py` → slim
  `docs/adr/catalog.json` + `.scratch/adr-optics/` glance (seam → [adr-catalog.md](adr-catalog.md))

Do **not** treat this OKF page as the only copy of the template — consumers
without `knowledge/` still author via the skill.

## Lifecycle

- **Published** Accepted files are immutable; change course with a **new** ADR that **supersedes** the old path (bidirectional Status links + index).
- **In-flight** ADRs (not yet on the remote default branch) may be edited in place — do not supersede for the same unfinished decision. Status=Accepted alone does not mean published; detect with `git status` / `git log origin/<default> -- <path>` (gate SoT: **`create-adr`**).
- **Relate** when a new ADR preserves or extends a published Accepted one — index Related (and optional Status **Related ADRs**); leave `Superseded by` empty.
- Citing an older ADR as a reason a **rejected option** fails is relate, not supersede.
- Create only when costly to reverse, alternatives were real, or future readers will ask why.

## Related

- Skill: [`skills/create-adr`](../skills/create-adr/SKILL.md)
- How-to: [docs/how-to-adr.md](../docs/how-to-adr.md)
- ADR: [0010](../docs/adr/0010-ADR-to-adr-mechanics-shipped.md) (supersedes 0003)
- Glossary: [CONTEXT.md](../CONTEXT.md)
