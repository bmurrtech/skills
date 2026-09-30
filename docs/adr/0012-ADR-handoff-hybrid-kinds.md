# Handoff is a hybrid portable brief with base + kind overlays

<!-- File: docs/adr/0012-ADR-handoff-hybrid-kinds.md -->

## Status
Accepted
- **Date (optional):** 2026-09-30
- **Supersedes:** —
- **Superseded by:** —
- **Related ADRs:** [0002](0002-ADR-glossary-okf.md)
- **Related PRDs:** —

## Context and Problem Statement

Live use showed thin path-index handoffs (Matt-style compact + temp file) failed
cold starts: wrong suggested skills, “see this chat” pointers, missing
acceptance/verdict, and temp paths never entered the next prompt. How should
**`handoff`** balance portability (no forked specs) with enough inline substance
for a fresh agent — and how should naming, kinds, and chat UX work?

## Decision Drivers

* Cold agent must act from the file without the source transcript
* Long specs/plans/ADRs stay single-sourced by path (Matt constraint)
* Mid-session forks (especially ADR candidacy) must separate concerns
* Filename should describe action/content, not a library prefix
* Chat must not dump the full brief; human still needs a glance to catch mis-aim
* Kind set stays closed and maintainer-extended — no invented/`generic` slugs

## Considered Options

* Keep Matt-thin path-index only (status quo)
* Embed everything needed inline (no path refs)
* **Hybrid brief:** next action + acceptance/constraints/verdict (+ ADR
  candidacy) inline; long artifacts path-ref; `handoff-base.md` + modular kind
  overlays; closed kind legend; temp default / keep on intent; post-write glance;
  ask before write only when aim is ambiguous

## Decision Outcome

Chosen option: "Hybrid brief", because it fixes cold-start gaps without forking
plans/ADRs and without overloading chat.

### Consequences

* Good, because implement/review/ADR-fork handoffs carry actionable checks
* Good, because kind overlays change independently of the base template
* Good, because glance + optional pre-ask reduce mis-aim without paste dumps
* Bad, because writers must judge what stays inline vs path-ref
* Bad, because closed kinds need manual legend updates to grow

### Confirmation

- `skills/handoff` ships `references/handoff-base.md`, `kind-legend.md`, and
  `references/kinds/*` deltas
- Filenames use `{kind}-{slug}-{ts}` or `{slug}-{ts}` — no `bmurrtech-*-handoff-*`
- Default destination remains OS temp; keep → `.scratch/handoffs/`
- Reply after write is at-a-glance only; full detail in the file
- `adr` kind captures candidacy for a later **`to-adr`** session; handoff does
  not author ADR/PRD bodies

## Pros and Cons of the Options

### Keep Matt-thin path-index only

* Good, because smallest skill and closest to upstream handoff
* Bad, because live failures showed path indexes are insufficient when the next
  prompt omits the handoff or chat-only facts
* Why not chosen: does not meet the cold-start bar

### Embed everything inline

* Good, because maximum portability of a single file
* Bad, because duplicates plans/ADRs and drifts
* Why not chosen: breaks single-source discipline

### Hybrid brief

* Good, because actionable substance travels; long SoT stays linked
* Good, because kinds encode conditional use without rewriting the base
* Bad, because more references to maintain than a one-page skill

## Assumptions

- User (or next prompt) will point the fresh agent at the handoff path
- Closed kind list covers the library’s primary session seams for v1
- Correction/reprompt creates a new timestamped file (no overwrite)

## Constraints

- `disable-model-invocation: true` — naming a skill in the file does not run it
- Do not write default handoffs into tracked trees
- Secrets/PII never appear in handoff files

## Implementation Notes (Normative)

- Template SoT: `skills/handoff/references/handoff-base.md`
- Kind SoT: `skills/handoff/references/kind-legend.md` + `skills/handoff/references/kinds/`
- Glossary terms **handoff** / **Handoff kind** live in `CONTEXT.md`
- Consumer how-to may summarize destination and kinds; skill references remain SoT

## References

- [CONTEXT.md](../../CONTEXT.md) — **handoff**, **Handoff kind**, **.scratch/**
- [skills/handoff/SKILL.md](../../skills/handoff/SKILL.md)
- Live failure notes (local): `pm/notes/handoff-skill-problems.md`
- Upstream inspiration (local mirror): `pm/repos/matt-pocock-skills/skills/productivity/handoff`
