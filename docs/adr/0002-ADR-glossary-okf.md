# Glossary and OKF split from AGENTS.md

<!-- File: docs/adr/0002-ADR-glossary-okf.md -->

## Status
Accepted
- **Date (optional):** 2026-09-25
- **Supersedes:** —
- **Superseded by:** —
- **Related PRDs:** —

## Context and Problem Statement

Agents need both a domain glossary and an operating manual. Mixing them causes duplication and stale instructions.

## Decision Drivers

* Single source of truth per concern
* Progressive disclosure for deeper concepts
* Post-change maintenance without one overloaded skill

## Considered Options

* One mega `AGENTS.md` with glossary + ops
* Root OKF-shaped `CONTEXT.md` + `knowledge/` concepts; separate `AGENTS.md`
* Glossary only inside `knowledge/` with no root `CONTEXT.md`

## Decision Outcome

Chosen option: "Root OKF-shaped `CONTEXT.md` + `knowledge/` concepts; separate `AGENTS.md`", because the root glossary stays discoverable while concepts load on demand, and ops stay in `AGENTS.md`.

### Consequences

* Good, because `context` and `upkeep` skills have clear ownership
* Good, because OKF indexing can grow without bloating always-loaded ops
* Bad, because agents must know which file to update

### Confirmation

`CONTEXT.md` has no command blocks that belong in `AGENTS.md`; `AGENTS.md` links to the glossary instead of restating definitions.

## Pros and Cons of the Options

### One mega AGENTS.md

* Good, because one file
* Bad, because context and ops churn together
* Bad, because poor progressive disclosure

### CONTEXT.md + knowledge/ + AGENTS.md

* Good, because SoT split
* Good, because OKF-compatible
* Bad, because two maintenance skills

### knowledge/ only

* Good, because pure OKF
* Bad, because no single root glossary agents already expect

## Assumptions

- `CLAUDE.md` remains a one-line pointer to `AGENTS.md`.

## Constraints

- `upkeep` must not rewrite glossary definitions; `context` must not rewrite ops commands.

## Implementation Notes (Normative)

- After `implement` / `code-review`, run `upkeep` then `context`.
- `CLAUDE.md` body must be exactly `AGENTS.md`.
