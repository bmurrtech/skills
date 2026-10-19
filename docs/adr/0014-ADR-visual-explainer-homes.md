# Visual-explainer dual homes: scratch vs tracked docs/visuals

<!-- File: docs/adr/0014-ADR-visual-explainer-homes.md -->

## Status
Accepted
- **Date:** 2026-10-10
- **Supersedes:** —
- **Superseded by:** —
- **Related ADRs:** [0002](0002-ADR-glossary-okf.md), [0013](0013-ADR-prd-tracking-choice.md)
- **Related PRDs:** —

## Context and Problem Statement

**visual-explainer** produces self-contained HTML. Some visuals are throwaway
session aids; others should live in git for the team. How should the skill choose
a write root, and what should setup provision?

## Decision Drivers
* Keep draft HTML out of git by default
* Make durable/team visuals a first-class tracked path
* One placement policy agents can resolve without asking every time
* Align scratch naming with “visuals” (not a diagrams-only label)

## Considered Options
* Scratch-only under `.scratch/visuals/` (promote manually outside the skill)
* Dual home: default `.scratch/visuals/`; tracked `docs/visuals/` on durable cues
* Tracked-only under `docs/visuals/`

## Decision Outcome
Chosen option: "Dual home: default `.scratch/visuals/`; tracked `docs/visuals/` on durable cues", because most asks are exploratory while team/commit/docs intent needs a stable tracked path without changing the default.

### Consequences
* Good, because draft HTML stays gitignored under `.scratch/`
* Good, because team/history visuals have a known tracked home
* Bad, because agents must resolve home before write (mitigated by cue list + silent default)

### Confirmation
- **visual-explainer** resolves mode then home; mode refs write under the resolved home
- **setup-bmurrtech-skills** creates `.scratch/visuals/` and `docs/visuals/`; renames legacy `.scratch/diagrams/` → `visuals/` when safe
- Fact-check “latest HTML” considers both homes by mtime

## Pros and Cons of the Options

### Scratch-only under `.scratch/visuals/`
* Good, because simplest default
* Bad, because durable team visuals have no skill-owned tracked home
* Why not chosen: team/commit asks would still pollute ad-hoc paths or stay invisible to git

### Dual home: default `.scratch/visuals/`; tracked `docs/visuals/` on durable cues
* Good, because default stays private; durable cues flip to tracked
* Bad, because two roots to teach in how-tos

### Tracked-only under `docs/visuals/`
* Good, because one path
* Bad, because every explore visual hits git history
* Why not chosen: contradicts scratch-first agent hygiene

## Implementation Notes
- Durable cues include team/group, commit/track/git history, docs/README/publish (see skill `references/homes.md`)
- Soft uncertainty defaults to scratch without asking
- Optional Markdown companion shares the HTML’s home
- Mode ask only when mode is unclear or the user requests help; clear signals run

## References
- [skills/visual-explainer/SKILL.md](../../skills/visual-explainer/SKILL.md)
- [skills/visual-explainer/references/homes.md](../../skills/visual-explainer/references/homes.md)
- [skills/setup-bmurrtech-skills/SKILL.md](../../skills/setup-bmurrtech-skills/SKILL.md)
- [docs/how-to-visual-explainer.md](../how-to-visual-explainer.md)
