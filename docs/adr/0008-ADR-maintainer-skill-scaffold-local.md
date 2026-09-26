# Maintainer skill scaffolding is local-only

<!-- File: docs/adr/0008-ADR-maintainer-skill-scaffold-local.md -->

## Status
Superseded
- **Date (optional):** 2026-09-26
- **Supersedes:** —
- **Superseded by:** [0009](0009-ADR-local-maintainer-skills-host-path.md)
- **Related ADRs:** [0001](0001-ADR-skills-home.md), [0005](0005-ADR-skills-release-artifact.md), [0006](0006-ADR-npx-skills-install-only.md)
- **Related PRDs:** —

## Context and Problem Statement

ADR 0001 tracks published skills under `skills/` only. A scaffolder skill lived there too, so it shipped in the release artifact and appeared in consumer catalogs — even though it is library-maintainer tooling, not a portable product skill. Hosts already provide create-skill tooling; shipping a redundant creator confuses the universal vs library-specific boundary.

## Decision Drivers

* Packaged `skills/` must be consumer-useful product skills
* Maintainer scaffolding may still exist for this repo’s contributors
* CI must validate skills on a clean checkout (no ignored `.agents/` tree)
* Preserve ADR 0001 SoT: published skills live only under `skills/`

## Considered Options

* Keep scaffolder as a shipped skill under `skills/`
* Move scaffolder to ignored `.agents/maintainer/` (outside host discovery); track validate/init CLIs under `scripts/`
* Delete scaffolder entirely; document only

## Decision Outcome

Chosen option: "Move scaffolder to ignored `.agents/maintainer/`; track validate/init CLIs under `scripts/`", because the product catalog stays universal/library product skills, contributors keep local create tooling outside host discovery paths (`.agents/skills/` would still appear in `npx skills --list`), and CI keeps a tracked validator without shipping a creator skill.

### Consequences

* Good, because `npx skills` / release tarballs no longer advertise a maintainer-only creator
* Good, because `scripts/quick_validate.py` works on clean CI checkouts
* Good, because ADR 0001’s SoT for **published** skills is unchanged
* Bad, because new contributors must obtain the local scaffolder themselves (or use `scripts/init_skill.py` + **`writing-for-agents`**)

### Confirmation

- No `skills/skill-create/` in git or in `scripts/package_skills.py` members
- Local scaffolder (if present) is **not** under `.agents/skills/` / other discovery roots
- CI calls `scripts/quick_validate.py`
- README / how-to / glossary do not list a creator product skill

## Pros and Cons of the Options

### Keep scaffolder as a shipped skill under `skills/`

* Good, because one place for create+validate docs
* Bad, because consumers get a redundant creator
* Bad, because blurs universal vs maintainer tooling

### Move scaffolder to ignored `.agents/maintainer/`; track validate/init CLIs under `scripts/`

* Good, because product boundary is clear
* Good, because CI remains deterministic
* Good, because path is outside `.agents/skills/` discovery
* Bad, because local skill is untracked (must be re-provisioned per machine)

### Delete scaffolder entirely; document only

* Good, because zero maintainer skill surface
* Bad, because loses a ready workflow for library maintainers who want the skill UX

## Assumptions

- `.agents/` stays gitignored (ADR 0001).
- Release artifact remains `skills/` + `LICENSE` only (ADR 0005).

## Constraints

- Do not reintroduce a tracked creator skill under `skills/` without a new ADR.
- Do not document maintainer scaffolding as a consumer install target.

## Implementation Notes (Normative)

- Published skills: `skills/` only — **preserves** [ADR 0001](0001-ADR-skills-home.md) Decision Outcome.
- ADR 0001 Implementation Notes that name a shipped `skill-create` scaffolder are **displaced** by this ADR (Decision Outcome of 0001 unchanged; scaffolding tooling rules live here).
- Maintainer create skill (if present): ignored `.agents/maintainer/` — not under host discovery paths, not product, not OKF.
- Library validate/scaffold CLIs: `scripts/quick_validate.py`, `scripts/init_skill.py`.
- Authoring guidance for consumers and maintainers: shipped **`writing-for-agents`** (standalone; soft-skip validator when absent).
