# Skills live under skills/ only

<!-- File: docs/adr/0001-ADR-skills-home.md -->

## Status
Accepted
- **Date (optional):** 2026-09-25
- **Supersedes:** —
- **Superseded by:** —
- **Related PRDs:** —

## Context and Problem Statement

Agent hosts discover skills from several local directories. This repository needs one tracked source of truth so installs and edits stay coherent.

## Decision Drivers

* Single SoT for published skills
* Local agent dirs remain disposable / machine-specific
* Compatible with `npx skills add bmurrtech/skills`

## Considered Options

* Track skills only under `skills/`
* Track under `.agents/skills/` as SoT
* Dual-track both trees in git

## Decision Outcome

Chosen option: "Track skills only under `skills/`", because it matches the public skills CLI layout and keeps local agent tooling gitignored.

### Consequences

* Good, because clones and installs have one obvious home
* Good, because `.agents/`, `.claude/`, and `.cursor/` can stay local-only
* Bad, because contributors must sync or install into host-specific dirs themselves

### Confirmation

`skills/*/SKILL.md` exists for each published skill; `.gitignore` ignores local agent dirs and `/pm/`.

## Pros and Cons of the Options

### Track skills only under `skills/`

* Good, because one SoT
* Good, because matches common `skills/` install layout
* Bad, because hosts that only read `.agents/skills/` need an install step

### Track under `.agents/skills/` as SoT

* Good, because some hosts read that path natively
* Bad, because conflicts with ignoring local agent dirs
* Bad, because couples the library to one host layout

### Dual-track both trees in git

* Good, because both layouts present
* Bad, because duplication and drift

## Assumptions

- Consumers install via `npx skills add bmurrtech/skills` or equivalent.

## Constraints

- New skills must be created under `skills/` only.

## Implementation Notes (Normative)

- `skill-create` scaffolds exclusively into `skills/<name>/`.
- `CONTEXT.md` states the hard rule; `AGENTS.md` enforces it for agents.
