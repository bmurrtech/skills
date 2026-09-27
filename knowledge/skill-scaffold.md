---
title: Skill scaffold
description: Why setup-bmurrtech-skills provisions AGENTS, glossary, ADR home, and local-only pads.
type: concept
tags: [scaffold, setup, okf]
---

# Skill scaffold

**`setup-bmurrtech-skills`** provisions a stable process surface in a **consumer**
repo so agents stop re-litigating layout each session. The folder/file inventory
is [docs/skill-scaffold.md](../docs/skill-scaffold.md). This concept holds the
**why**.

## Why the scaffold exists

Coding agents need known homes for:

- Durable decisions vs day-to-day product specs
- Glossary language so skills do not invent synonyms
- What is safe to commit vs local-only dumps
- One ops manual both humans and hosts can load

Without that, sessions pollute tracked trees with scratch, or drift
AGENTS / CLAUDE / glossary independently.

## Why each artifact

| Artifact | Why |
|----------|-----|
| `.gitignore` patches | Separates collaboration SoT (tracked) from local working surfaces (ignored). |
| `.scratch/` (+ `diagrams/`, `adr-optics/`; `handoffs/` on **keep**; `ideas/` on **idea** capture) | Known dump pad so drafts do not land in `docs/`, `pm/`, or repo root. `diagrams/` → visual-explainer; `adr-optics/` → to-adr catalog. Default handoffs are throwaway (OS temp via **`handoff`**); **keep** → `.scratch/handoffs/`. Brain dumps → `.scratch/ideas/` via **`idea`**; promote only via **`roadmap`**. |
| `AGENTS.md` | Short executable ops surface; domain vocab stays in CONTEXT/knowledge. Owned by **`upkeep`**. |
| `CLAUDE.md` → `AGENTS.md` | Claude hosts look for `CLAUDE.md`; pointer avoids two manuals. |
| `CONTEXT.md` + `knowledge/` | Shared ubiquitous language + progressive disclosure. Consumer glossary is yours — library OKF is not shipped into consumers ([skills-release-artifact](skills-release-artifact.md)). |
| `docs/adr/` | Costly-to-reverse decisions need a **tracked** trail. |
| `docs/prd/` ignore | Day-to-day specs churn; keep local to avoid PR noise while giving **`to-prd`** a stable home ([prd](prd.md)). |
| Optional docx | Needs host apps + pinned CLI; opt-in keeps scaffold light. |

## Related

- Tree: [docs/skill-scaffold.md](../docs/skill-scaffold.md)
- Flows: [docs/how-to-bmurrtech-skills.md](../docs/how-to-bmurrtech-skills.md)
- Skill: [`setup-bmurrtech-skills`](../skills/setup-bmurrtech-skills/SKILL.md)
- ADRs: [0002](../docs/adr/0002-ADR-glossary-okf.md), [0007](../docs/adr/0007-ADR-scaffold-omit-about-prd.md)
