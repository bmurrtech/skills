# Setup offers PRD track vs ignore; default ignore

<!-- File: docs/adr/0013-ADR-prd-tracking-choice.md -->

## Status
Accepted
- **Date (optional):** 2026-09-30
- **Supersedes:** [0007-ADR-scaffold-omit-about-prd.md](0007-ADR-scaffold-omit-about-prd.md)
- **Superseded by:** —
- **Related ADRs:** [0002-ADR-glossary-okf.md](0002-ADR-glossary-okf.md)
- **Related PRDs:** —

## Context and Problem Statement

ADR 0007 kept `docs/prd/` always gitignored and omitted `docs/about-prd.md` from scaffold. Teams and remote AI agents often need PRDs in git history for shared context. Should every consumer be forced local-only, or may setup offer a durable track-vs-ignore choice?

## Decision Drivers

* Preserve lean scaffold (no `about-prd.md` invent)
* Default stays quiet (solo / draft-heavy) without PR noise
* Allow teams / remote agents to **track** PRDs when they choose
* Idempotent re-runs: re-ask and retarget the same policy surfaces
* Agents must read policy from `AGENTS.md` / gitignore — not a side marker file

## Considered Options

* Keep ADR 0007 always-ignore for `docs/prd/`
* Setup A/B choice: **A** ignore (default) · **B** track; retarget gitignore + AGENTS (+ CONTEXT when stub/edit ok)
* Always track `docs/prd/` in every consumer

## Decision Outcome

Chosen option: "Setup A/B choice: **A** ignore (default) · **B** track; retarget gitignore + AGENTS (+ CONTEXT when stub/edit ok)", because the costly choice is *whether* PRDs are collaboration SoT, not a single forced ignore, while silent/no-reply and greenfield default remain **A**.

### Consequences

* Good, because consumers can share PRDs with teammates and remote agents
* Good, because default A preserves ADR 0007’s quiet local pad
* Good, because re-running setup can flip policy surgically
* Bad, because `to-prd` / OKF / how-to must speak in dual policy (ignore *or* track)
* Bad, because B→A flips need care around already-tracked files (`git rm --cached` only with confirm)

### Confirmation

`setup-bmurrtech-skills` prompts Commit PRDs? A/B (➡️ A); apply matrix in `skills/setup-bmurrtech-skills/references/prd-tracking.md`; never creates `docs/about-prd.md`; library explainer remains in library docs.

## Pros and Cons of the Options

### Keep always-ignore (0007)

* Good, because simplest mental model
* Bad, because blocks team/remote-agent PRD sharing
* Why not chosen: real alternative (track) exists and is costly to bolt on later per clone

### Setup A/B choice (chosen)

* Good, because default quiet + opt-in share
* Bad, because dual wording across skills/docs

### Always track

* Good, because agents always see PRDs in clones
* Bad, because forces PR noise on solo/draft workflows
* Why not chosen: violates default-local driver

## Assumptions

- `to-prd` always authors under `docs/prd/` regardless of track vs ignore.
- Library how-tos / `docs/about-prd.md` remain library-only (not setup creates).
- Policy SoT = `.gitignore` presence of `docs/prd` ignore lines + matching `AGENTS.md` bullets (optional CONTEXT gloss).

## Constraints

- Do **not** create `docs/about-prd.md` in consumers via setup.
- Do **not** invent a separate policy marker file.
- Default / no user reply / affirmatives on ➡️ → **A** (ignore).
- Never `git rm --cached` on B→A without explicit user confirm.
- Do **not** silently overwrite unrelated AGENTS/CONTEXT prose — patch owned policy lines or ask.

## Implementation Notes (Normative)

- `setup-bmurrtech-skills`: Explore classifies ignore vs tracked; Present always re-asks A/B; Write applies [prd-tracking.md](../../skills/setup-bmurrtech-skills/references/prd-tracking.md) to `.gitignore`, `AGENTS.md`, and `CONTEXT.md` when applicable; refresh `CLAUDE.md` if AGENTS body changed and CLAUDE is the pointer.
- `upkeep` must **not** “heal” B repos by re-adding `/docs/prd/` ignore.
- Library docs (`knowledge/prd.md`, skill-scaffold, how-to) describe dual policy; this library may stay on **A**.

## References

- [skills/setup-bmurrtech-skills/SKILL.md](../../skills/setup-bmurrtech-skills/SKILL.md)
- [skills/setup-bmurrtech-skills/references/prd-tracking.md](../../skills/setup-bmurrtech-skills/references/prd-tracking.md)
- [knowledge/prd.md](../../knowledge/prd.md)
- [docs/about-prd.md](../about-prd.md)
- [0007-ADR-scaffold-omit-about-prd.md](0007-ADR-scaffold-omit-about-prd.md)
