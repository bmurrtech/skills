# ADR template SoT lives in shipped to-adr mechanics

<!-- File: docs/adr/0010-ADR-to-adr-mechanics-shipped.md -->

## Status
Accepted
- **Date (optional):** 2026-09-26
- **Supersedes:** [0003](0003-ADR-docs-adr-madr.md)
- **Superseded by:** —
- **Related ADRs:** [0005](0005-ADR-skills-release-artifact.md), [0011](0011-ADR-skill-scanner-posture-prereqs.md)
- **Related PRDs:** —

## Context and Problem Statement

ADR 0003 fixed ADRs under `docs/adr/` with MADR headings, but left heading/process
detail easy to drift into library-only `knowledge/` — which does not ship in the
skills release artifact. Consumer installs of **`to-adr`** need a self-contained
authoring contract (placement vs ops/glossary, anti-bloat Implementation Notes,
optional at-a-glance catalog) without depending on this repo’s OKF.

## Decision Drivers

* Skills release artifact ships `skills/` only (ADR 0005) — authoring rules must travel with the skill
* Keep MADR-compatible spine for interoperability
* Prevent kitchen-sink ADRs that duplicate AGENTS / CONTEXT / knowledge
* Optional HTML decision log without tracking generated views in git

## Considered Options

* Keep “MADR headings” as the only SoT; leave detail in library `knowledge/adr.md`
* Ship expanded mechanics + process inside `skills/to-adr` (template, placement, catalog script); library OKF only summarizes
* Abandon MADR-shaped headings for a custom mini-template only

## Decision Outcome

Chosen option: "Ship expanded mechanics + process inside `skills/to-adr`", because
consumers get a complete authoring skill from the release artifact, while
`docs/adr/` + immutability + index from ADR 0003 remain; library `knowledge/adr.md`
points at the skill instead of duplicating the template.

### Consequences

* Good, because **`to-adr`** works without this library’s `knowledge/`
* Good, because placement / anti-bloat rules sit next to the template agents load
* Good, because at-a-glance HTML can regenerate under `.scratch/diagrams/`
* Bad, because “strict MADR-only” wording in ADR 0003 is superseded — readers must follow skill mechanics

### Confirmation

- `skills/to-adr/references/mechanics.md` exists and is the heading SoT
- `skills/to-adr/SKILL.md` does not require `knowledge/` to complete the workflow
- `python3 skills/to-adr/scripts/build_catalog.py --home docs/adr --visualize` writes `.scratch/diagrams/adr-at-a-glance.html`

## Pros and Cons of the Options

### knowledge/ as template SoT

* Good, because progressive disclosure in the library repo
* Bad, because excluded from the release artifact (ADR 0005)
* Why not chosen: consumers would lack the contract that prevents ADR bloat

### Ship mechanics in skills/to-adr

* Good, because self-contained with the shipped skill
* Good, because MADR-compatible spine preserved
* Bad, because skill bundle grows slightly (scripts + template HTML)

### Custom mini-template only

* Good, because shortest files
* Bad, because weaker options/consequences discipline and less interoperable
* Why not chosen: loses MADR interoperability without enough gain

## Assumptions

- Consumer repos may lack CONTEXT/knowledge/AGENTS; ADRs still cite paths when those files exist.
- Generated catalog HTML is a view, not tracked SoT.

## Constraints

- Accepted ADRs remain immutable; change via supersede.
- Do not require library `knowledge/` to author an ADR with this skill.

## Implementation Notes (Normative)

- Heading + placement SoT: `skills/to-adr/references/mechanics.md`
- Process: `skills/to-adr/SKILL.md` (warrant, classify, index, visualize)
- Catalog rebuild: `skills/to-adr/scripts/build_catalog.py` → `.scratch/diagrams/adr-at-a-glance.html`
- Path/layout from ADR 0003 preserved: `docs/adr/NNNN-ADR-<slug>.md` + `index.md`
- Library `knowledge/adr.md` may summarize and link the skill; must not be the only copy of the template

## References

- [0003-ADR-docs-adr-madr.md](0003-ADR-docs-adr-madr.md)
- [0005-ADR-skills-release-artifact.md](0005-ADR-skills-release-artifact.md)
- [skills/to-adr/SKILL.md](../../skills/to-adr/SKILL.md)
