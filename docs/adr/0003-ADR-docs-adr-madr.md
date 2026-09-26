# ADRs under docs/adr with MADR headings

<!-- File: docs/adr/0003-ADR-docs-adr-madr.md -->

## Status
Superseded
- **Date (optional):** 2026-09-25
- **Supersedes:** —
- **Superseded by:** [0010](0010-ADR-to-adr-mechanics-shipped.md)
- **Related PRDs:** —

## Context and Problem Statement

Significant decisions need a tracked, reviewable home that agents and humans can cite from the glossary and `AGENTS.md`.

## Decision Drivers

* Interoperability with MADR-shaped records
* Repo-local numbering without a multi-project key
* Immutability of accepted decisions

## Considered Options

* `docs/adr/NNNN-ADR-<slug>.md` + `index.md` (MADR headings)
* Local-only decision notes under `/pm`
* Minimal status/context/decision-only templates

## Decision Outcome

Chosen option: "`docs/adr/NNNN-ADR-<slug>.md` + `index.md` (MADR headings)", because decisions stay tracked and citeable, and MADR headings stay interoperable.

### Consequences

* Good, because ADRs are versioned with the library
* Good, because `to-adr` has a stable target layout
* Bad, because richer templates cost a little authoring time

### Confirmation

Every ADR appears in `docs/adr/index.md`; accepted files are not edited in place.

## Pros and Cons of the Options

### docs/adr + MADR

* Good, because tracked and standard headings
* Bad, because more structure than a short note

### Local /pm notes

* Good, because private scratch
* Bad, because not shared with consumers of the library

### Minimal templates

* Good, because fast
* Bad, because weak options/consequences discipline

## Assumptions

- This repository is a single project; no project-key filename prefix is required.

## Constraints

- Accepted ADRs are immutable; supersede instead of rewrite.

## Implementation Notes (Normative)

- Author via `skills/to-adr`.
- Update `docs/adr/index.md` on create and supersede.
