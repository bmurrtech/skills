# Setup omits about-prd; library docs explain local PRDs

<!-- File: docs/adr/0007-ADR-scaffold-omit-about-prd.md -->

## Status
Superseded
- **Date (optional):** 2026-09-26
- **Supersedes:** [0004-ADR-local-okf-prds.md](0004-ADR-local-okf-prds.md)
- **Superseded by:** [0013-ADR-prd-tracking-choice.md](0013-ADR-prd-tracking-choice.md)
- **Related ADRs:** [0002-ADR-glossary-okf.md](0002-ADR-glossary-okf.md)
- **Related PRDs:** —

## Context and Problem Statement

ADR 0004 required `setup-bmurrtech-skills` to create a tracked `docs/about-prd.md` in every consumer so local PRDs were explained. That explainer is library-product documentation, not process surface the agent needs every run. Should consumers still receive `about-prd.md` at scaffold time?

## Decision Drivers

* Keep consumer scaffold lean (OKF + ADR index + ignore rules)
* Keep `docs/prd/` gitignored and usable by **`to-prd`**
* Preserve a short “why PRDs are local” explainer for humans who seek it — in the library repo, not forced into every consumer

## Considered Options

* Keep ADR 0004 as-is (setup always writes `docs/about-prd.md`)
* Drop `about-prd.md` from setup; explain in library docs (`docs/about-prd.md`, `docs/skill-scaffold.md`)
* Delete the library explainer entirely and rely only on AGENTS one-liners

## Decision Outcome

Chosen option: "Drop `about-prd.md` from setup; explain in library docs (`docs/about-prd.md`, `docs/skill-scaffold.md`)", because ignore + OKF/ADR indexes are the necessary consumer surface, and “why ignored” is optional human reading that belongs with the skills library.

### Consequences

* Good, because scaffold stays knowledge/indexes-first without doc bloat
* Good, because library still answers “why aren’t PRDs tracked?”
* Bad, because a consumer clone without visiting the library may lack an in-repo PRD explainer (mitigated by `to-prd` skill + ignore rule + AGENTS structure line)

### Confirmation

`setup-bmurrtech-skills` does not create `docs/about-prd.md`; `.gitignore` still includes `/docs/prd/`; library `docs/about-prd.md` remains tracked.

## Pros and Cons of the Options

### Keep ADR 0004 setup write

* Good, because every consumer has the explainer on disk
* Bad, because duplicates library docs and fattens greenfield trees

### Library-only explainer (chosen)

* Good, because lean scaffold
* Bad, because explainer is one hop away (GitHub / clone of this library)

### Delete explainer entirely

* Good, because fewer files
* Bad, because the ignore decision loses a dedicated human doc

## Assumptions

- `to-prd` remains the authoring path for `docs/prd/`.
- Consumers who need the rationale can open this library’s docs.

## Constraints

- Do not reintroduce `docs/about-prd.md` as a setup create target without a new ADR.
- Keep `/docs/prd/` ignored.

## Implementation Notes (Normative)

- `setup-bmurrtech-skills`: ensure ignore for `/docs/prd/`; create `AGENTS.md`, `CLAUDE.md`, `CONTEXT.md`, `knowledge/index.md`, `docs/adr/index.md`, `.scratch/` — **not** `docs/about-prd.md`.
- Library keeps tracked `docs/about-prd.md` (and `docs/skill-scaffold.md`) as the human explainer.
