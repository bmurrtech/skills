# Skills release artifact excludes library OKF

<!-- File: docs/adr/0005-ADR-skills-release-artifact.md -->

## Status
Accepted
- **Date (optional):** 2026-09-25
- **Supersedes:** —
- **Superseded by:** —
- **Related PRDs:** —

## Context and Problem Statement

Installers need a lightweight skills package. Shipping the library’s `knowledge/` / `CONTEXT.md` / ops docs into consumer repos risks colliding with consumer OKF (or other `knowledge/` conventions) and bloats drop-in installs. Should library meta be gitignored, or filtered only at package time?

## Decision Drivers

* Keep consumer installs clean and conflict-free
* Preserve library glossary/OKF as tracked SoT for maintainers (ADR 0002)
* One reproducible include/exclude contract for all install adapters

## Considered Options

* Gitignore `knowledge/` (and related library meta) so it never appears in clones/tags
* Keep library meta tracked; filter release artifacts to `skills/` + `LICENSE` only
* Ship the full tagged tree as the install artifact

## Decision Outcome

Chosen option: "Keep library meta tracked; filter release artifacts to `skills/` + `LICENSE` only", because maintainers still need the OKF in git, while installers must never overlay library knowledge onto consumers.

### Consequences

* Good, because source repo remains the glossary/ADR SoT
* Good, because packaging SoT (`scripts/package_skills.py`) is testable and shared by curl/CLI/plugin adapters
* Bad, because naive “clone whole repo into consumer root” installers must be forbidden / corrected

### Confirmation

`python3 -m unittest tests.test_package_skills` passes; tarballs from `scripts/package_skills.py` contain no `knowledge/`, `CONTEXT.md`, `AGENTS.md`, or `docs/`.

## Pros and Cons of the Options

### Gitignore knowledge/

* Good, because absent from git checkout
* Bad, because breaks ADR 0002 collaborator SoT
* Bad, because gitignore ≠ packaging; full-repo tarballs still risk mistakes

### Filter release artifacts

* Good, because tracks library meta and ships clean skills packs
* Good, because explicit include/exclude contract
* Bad, because every installer must consume the filtered artifact

### Ship full tree

* Good, because simplest packaging
* Bad, because consumer OKF collisions and weight

## Assumptions

- Generic installers install skill folders into agent skill paths, not repo-root OKF.
- Consumer scaffold remains opt-in via `setup-bmurrtech-skills`.

## Constraints

- Do not gitignore `knowledge/` or `CONTEXT.md` to achieve clean installs.
- Ecosystem-specific packs may add thin wrappers; they still must not inject library OKF into consumer roots.

## Implementation Notes (Normative)

- Include: `LICENSE`, `skills/**` (non-dotfiles).
- Exclude: `knowledge/`, `CONTEXT.md`, `AGENTS.md`, `CLAUDE.md`, `docs/`, `scripts/`, `tests/`, README/CHANGELOG, integrations, local agent dirs, tooling manifests.
- Command: `python3 scripts/package_skills.py --version <semver> --out dist/`.
