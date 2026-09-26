# Local OKF PRDs under docs/prd (gitignored)

<!-- File: docs/adr/0004-ADR-local-okf-prds.md -->

## Status
Superseded
- **Date (optional):** 2026-09-25
- **Supersedes:** —
- **Superseded by:** [0007-ADR-scaffold-omit-about-prd.md](0007-ADR-scaffold-omit-about-prd.md)
- **Related PRDs:** —

## Context and Problem Statement

PRDs are useful for day-to-day MVP planning but may contain local product detail that should not ship with the public skills library.

## Decision Drivers

* Keep ADRs tracked and citeable
* Allow local PRD authoring with OKF shape
* Align ignore policy with `/pm` local-only posture

## Considered Options

* Track PRDs under `docs/prd/`
* Gitignore `docs/prd/` and document via `docs/about-prd.md`
* Keep PRDs under `/pm` only

## Decision Outcome

Chosen option: "Gitignore `docs/prd/` and document via `docs/about-prd.md`", because PRDs stay local while ADRs and glossary remain shared.

### Consequences

* Good, because consumers can author PRDs without polluting the library remote
* Bad, because PRDs are not shared across clones unless copied deliberately

### Confirmation

`.gitignore` contains `/docs/prd/`; `docs/about-prd.md` exists and is tracked.

## Pros and Cons of the Options

### Track docs/prd

* Good, because shareable
* Bad, because couples library remote to product drafts

### Gitignore docs/prd + about-prd.md

* Good, because local OKF PRDs + clear explainer
* Bad, because no remote PRD history

### /pm only

* Good, because already ignored
* Bad, because splits product docs away from `docs/`

## Assumptions

- `to-prd` always targets `docs/prd/`.

## Constraints

- No project-key prefix on PRD filenames.

## Implementation Notes (Normative)

- `setup-bmurrtech-skills` must ensure the ignore rule and `docs/about-prd.md`.
- `to-prd` creates OKF frontmatter on each PRD.
