# Donation CTAs via setup; CHANGELOG-extract release notes

<!-- File: docs/adr/0015-ADR-donation-cta-changelog-release-notes.md -->

## Status
Accepted
- **Date (optional):** 2026-10-18
- **Supersedes:** —
- **Superseded by:** —
- **Related ADRs:** [0005-ADR-skills-release-artifact.md](0005-ADR-skills-release-artifact.md), [0013-ADR-prd-tracking-choice.md](0013-ADR-prd-tracking-choice.md)
- **Related PRDs:** —

## Context and Problem Statement

GitHub Release bodies for this library were a hardcoded stub that ignored
`CHANGELOG.md`. Operators also want optional Ko-fi / Buy Me a Coffee (and
similar) surfaces for the library and for consumer scaffolds — without forcing
funding on every repo. How should funding files, README CTAs, glossary terms,
and release-note generation relate — and where does the notes extractor live?

## Decision Drivers

* Release notes must reflect the dated CHANGELOG section for the tagged version
* Prefer GitHub-native `.github/FUNDING.yml` over inventing `CTA.yaml`
* Consumer scaffolds must not assume OSS (“Support open source”) wording
* Donation links are opt-in; never invent usernames/URLs
* Extractor must be exact and reusable in CI and **`release`** bootstrap
* One editable SoT for the extractor — no byte-identical dual copy
* Script must ship with **`release`** (ADR 0005); library CI may call the skill path directly

## Considered Options

* Keep stub release notes; document FUNDING.yml manually
* CI extracts CHANGELOG; setup optional Donation CTA triad; dual byte-identical copies (`scripts/` + skill)
* CI extracts CHANGELOG; setup optional Donation CTA triad; single SoT under `skills/release/scripts/`; bootstrap copies outward
* Skill (not CI) alone composes notes via `gh release create` (workflow only attaches assets)

## Decision Outcome

Chosen option: "CI extracts CHANGELOG; setup optional Donation CTA triad; single SoT under `skills/release/scripts/`; bootstrap copies outward", because the tag workflow already owns publication (ADR 0005 dogfood), CHANGELOG is the notes SoT, funding is opt-in like docx, and one skill-tree file kills dual-copy drift while still shipping in the release artifact.

### Consequences

* Good, because tagged Releases show the real changelog + optional CTA footer
* Good, because GitHub Sponsors sidebar works from FUNDING.yml
* Good, because consumers get **Support this Repo** wording; this OSS library keeps **Support open source**
* Good, because bootstrap source and dogfood runtime are the same path in this clone
* Bad, because library CI path is longer (`skills/release/scripts/…`) than `scripts/…`
* Bad, because setup gains another optional prompt (re-ask on re-run)

### Confirmation

- `.github/FUNDING.yml` present for this library (`ko_fi` / `buy_me_a_coffee`: `bmurrtech`)
- No `scripts/changelog_release_notes.py` twin in this library
- `.github/workflows/release.yml` calls `skills/release/scripts/changelog_release_notes.py`
- `setup-bmurrtech-skills` offers Donation CTA; write matrix in `references/donation-cta.md`
- `release` bootstrap copies skill script → consumer `scripts/`
- `tests.test_changelog_release_notes` loads the skill path and asserts the ops twin is absent

## Pros and Cons of the Options

### Keep stub notes + manual FUNDING

* Good, because smallest diff
* Bad, because notes drift from CHANGELOG; funding undocumented for consumers
* Why not chosen: fails the release-notes driver

### Dual byte-identical copies

* Good, because short `scripts/` path for ops
* Bad, because parity test / human dual-edit risk
* Why not chosen: fragility

### CI extract + setup CTA + skill-only SoT (chosen)

* Good, because one publication owner; deterministic extract; opt-in funding; one editable file
* Bad, because dogfood CI references a skill-tree path

### Skill-only `gh release create` notes

* Good, because agent can shape prose
* Bad, because competes with workflow-owned publication (discovery contract)
* Why not chosen: breaks dogfood “workflow owns create”

## Assumptions

- Keep a Changelog dated headings use `## [<version>]` (optional ` - YYYY-MM-DD`).
- CTA footer prefers FUNDING.yml; CONTEXT URL fallback; omit if neither.
- No backfill required for prior tags.
- Bootstrap still writes a consumer-local `scripts/changelog_release_notes.py` from the skill SoT.

## Constraints

- Do **not** invent nonstandard funding filenames GitHub ignores.
- Do **not** invent donation URLs during setup or release bootstrap.
- Do **not** use “Support open source” as the consumer README heading.
- Do **not** reintroduce a second tracked copy under library `scripts/`.
- Hard-stop release notes generation when the CHANGELOG version heading is missing.

## Implementation Notes (Normative)

- SoT: `skills/release/scripts/changelog_release_notes.py`
- Dogfood: `.github/workflows/release.yml` calls that path
- Bootstrap: copy SoT → consumer `scripts/`; see `skills/release/references/bootstrap.md`
- Setup Donation CTA: `skills/setup-bmurrtech-skills/references/donation-cta.md`
- Tests: `tests/test_changelog_release_notes.py`

## References

- [0005-ADR-skills-release-artifact.md](0005-ADR-skills-release-artifact.md)
- [0013-ADR-prd-tracking-choice.md](0013-ADR-prd-tracking-choice.md)
- Glossary: Donation CTA, FUNDING.yml, Release notes (CHANGELOG extract)
