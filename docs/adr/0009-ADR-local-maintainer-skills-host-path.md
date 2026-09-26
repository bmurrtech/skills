# Local maintainer skills under ignored .agents/skills/

<!-- File: docs/adr/0009-ADR-local-maintainer-skills-host-path.md -->

## Status
Accepted
- **Date (optional):** 2026-09-26
- **Supersedes:** [0008](0008-ADR-maintainer-skill-scaffold-local.md)
- **Superseded by:** —
- **Related ADRs:** [0001](0001-ADR-skills-home.md), [0005](0005-ADR-skills-release-artifact.md), [0006](0006-ADR-npx-skills-install-only.md)
- **Related PRDs:** —

## Context and Problem Statement

ADR 0008 kept maintainer-only skills untracked and out of the product catalog by placing them under `.agents/maintainer/`, outside host discovery. Cursor (and similar hosts) only load skills from discovery roots such as `.agents/skills/`, so those tools became unusable in the IDE while still needed by library maintainers.

## Decision Drivers

* Maintainer-local skills must load in Cursor / agent hosts that read `.agents/skills/`
* Must remain **untracked** (not product, not OKF, not release artifact)
* Preserve ADR 0001: published SoT stays `skills/`
* Tracked validate/init CLIs under `scripts/` for CI (from ADR 0008)

## Considered Options

* Keep `.agents/maintainer/` (outside discovery) — ADR 0008
* Place local-only skills under ignored `.agents/skills/`
* Dual-track copies under `.cursor/skills/` only

## Decision Outcome

Chosen option: "Place local-only skills under ignored `.agents/skills/`", because hosts can load them, `.agents/` stays gitignored, and GitHub / release installs never include that tree. Local `npx skills add <clone-path> --list` may show them; that is clone-local noise, not the shipped catalog.

### Consequences

* Good, because Cursor can read maintainer skills
* Good, because git + release artifact still exclude them
* Bad, because path-based local listing mixes product + local skills (document; do not treat as catalog SoT)

### Confirmation

- No `skills/skill-create/` (or other maintainer-only names) tracked under `skills/`
- Local copies (if present) live under `.agents/skills/` and are gitignored
- CI / packaging still use tracked `scripts/` and `skills/` only

## Pros and Cons of the Options

### Keep `.agents/maintainer/` (outside discovery)

* Good, because `npx --list` on a local path stays clean
* Bad, because Cursor cannot load the skills (**reject-option-cost** vs host UX)

### Place local-only skills under ignored `.agents/skills/`

* Good, because host discovery works
* Good, because still untracked / unshipped
* Bad, because local path listing can include them

### Dual-track copies under `.cursor/skills/` only

* Good, because Cursor-specific
* Bad, because couples to one host; ignores other agents that also read `.agents/skills/`

## Assumptions

- `.agents/` remains gitignored.
- Consumer install from GitHub source or release tarball has no `.agents/` tree.

## Constraints

- Do not track maintainer-only skills under `skills/`.
- Do not document them in README Features / consumer how-to catalog.

## Implementation Notes (Normative)

- Published skills: tracked `skills/` only (ADR 0001).
- Library-local / maintainer skills (e.g. scaffolder, experimental): ignored `.agents/skills/` — host-readable, not product, not OKF.
- Validate/scaffold CLIs for this repo: `scripts/quick_validate.py`, `scripts/init_skill.py`.
- Product catalog evidence: tracked `skills/*/SKILL.md`, release members, remote `npx skills add bmurrtech/skills --list` — not a dirty local clone’s `.agents/skills/`.
- ADR 0001 Implementation Notes naming a shipped `skill-create` remain displaced (see superseded [0008](0008-ADR-maintainer-skill-scaffold-local.md) intent, restated here).
