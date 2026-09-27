# Published skills use prerequisites and local Spec — not agent-side installs or CDN fetches

<!-- File: docs/adr/0011-ADR-skill-scanner-posture-prereqs.md -->

## Status
Accepted
- **Date (optional):** 2026-09-27
- **Supersedes:** —
- **Superseded by:** —
- **Related ADRs:** [0005](0005-ADR-skills-release-artifact.md), [0006](0006-ADR-npx-skills-install-only.md), [0010](0010-ADR-to-adr-mechanics-shipped.md)
- **Related PRDs:** —

## Context and Problem Statement

Post-ingest scanners (Snyk / Socket / Gen) flagged **MEDIUM** on shipped **`code-review`**, **`docx`**, and **`to-adr`**. Maintainers want cleaner PASS posture without gutting core review / Word / ADR function. How should published skills obtain CLIs, Spec context, and visualizer assets — agent download/install/fetch, or operator prerequisites plus local-only inputs?

## Decision Drivers

* Favor function over badge cosmetics, but remove *unnecessary* capabilities scanners treat as remote exec / unverifiable deps / default third-party content
* Consumers install skills via `npx skills` (ADR 0006); the shipped `skills/` tree is what scanners assess (ADR 0005)
* Operators can install docx-cli, Word/LibreOffice, and fonts themselves; agents should not escalate privilege or pull release binaries by default
* Spec for review should prefer local artifacts; tracker fetch is optional future work
* Avoid prompt-injection *demos* inside SKILL.md (attack phrases such as “ignore previous”) that add signal without improving behavior

## Considered Options

* Accept residual MEDIUM and document only (`docs/accepted-risk.md` as SoT)
* Chase literal zero MEDIUM even if that removes `docx read` / CLI invoke / catalog helper
* **Prerequisite-driven posture:** delete agent download/install paths; local Spec only for `code-review`; system fonts (no CDN) for `to-adr` visualizer; keep core function; accept residual only if untrusted document ingest still flags

## Decision Outcome

Chosen option: "Prerequisite-driven posture", because it clears download / default tracker-fetch / CDN-font W012-class findings while preserving review, Word editing when the CLI exists, and ADR authoring plus local at-a-glance catalog.

### Consequences

* Good, because scanners no longer see agent-initiated binary download or Google Fonts runtime URLs in `to-adr`
* Good, because `code-review` Spec defaults to local diff + local Spec / scratch — no default third-party issue body in context
* Good, because operators get explicit README + skill hints (OS-specific copy-paste) instead of silent installs
* Bad, because first-time `docx` users must install CLI + office host themselves before the skill can succeed
* Bad, because `docx read` of untrusted Word content may still MEDIUM — that is an accepted floor, not a wording chase

### Confirmation

- `docx` skill does not download or `npx`-install docx-cli; probe pin / PATH and print manual prereq commands on failure
- `code-review` Spec order has no `gh`/tracker fetch; optional tracker Spec lives only as scratch idea until explicitly requested later
- `to-adr` visualizer template has no `fonts.googleapis.com` / `fonts.gstatic.com` (or other font CDN) links
- `docs/accepted-risk.md` is a thin pointer to this ADR, not a parallel SoT

### Risks → mitigations

* Gen still flags printed `sudo apt…` **strings** in office hints → fall back to README-only prereq text in a follow-up; scripts must never *execute* package managers
* Residual MEDIUM on document ingest → do not weaken `docx` core; document as floor under this ADR

### Follow-ups

* Implement the skill/README/script changes entailed below (separate change set)
* Optional later: restore tracker Spec behind explicit user request (see `.scratch/ideas/code-review-optional-gh-issue-context.md`)

## Pros and Cons of the Options

### Accept residual MEDIUM only

* Good, because zero behavior change
* Bad, because leaves avoidable download / CDN / tracker-fetch surface in shipped skills
* Why not chosen: compromise path exists without removing core function

### Chase literal zero MEDIUM

* Good, because cleanest badges
* Bad, because reading Word and invoking `docx` are the product; zero flags likely requires gutting them
* Why not chosen: breaks the compromise (function over benign residual)

### Prerequisite-driven posture

* Good, because removes unnecessary remote/install/CDN/default-tracker capabilities
* Good, because README + probe/fail UX matches how operators already install tools
* Bad, because setup friction until prereqs exist
* Bad, because untrusted-doc floor may remain

## Assumptions

- Operators can install docx-cli (matching the skill’s documented pin) and Word or LibreOffice on their OS.
- Local Spec paths (`docs/`, `specs/`, `docs/prd/`, `.scratch/`) or user-passed paths cover most `code-review` Spec needs.
- Google Fonts preconnect/stylesheet links were the concrete W012 for `to-adr` visualizer; system/local font stacks suffice.

## Constraints

- Do not auto-download docx-cli or auto-run package managers / `sudo` from skill scripts.
- Do not put attack-demo phrases (e.g. “ignore previous”, “ignore the review and run…”) in SKILL.md; use positive evidence-only rules instead.
- Do not remove agent-invoked `build_catalog.py` solely for badge optics unless a post-fonts re-scan still fails on the helper.
- Shipped skill scripts remain in scope for scanners — dormant download code still counts as capability; delete it rather than leave unused.

## Implementation Notes (Normative)

- **`docx`:** Probe `docx` on PATH and pin/version; on failure, notify and print OS-specific **manual** install commands (CLI + LibreOffice/Word as needed); never `--install` download / `urllib` fetch / `npx` skill add. Committed pin/DIGESTS may document expected version for mismatch messages only. User reruns the skill after prereqs.
- **`code-review`:** Spec sources = user path → local `docs/` / `specs/` / `.scratch/` / `docs/prd/` → ask. No tracker/`gh` fetch in the shipped skill until a future explicit opt-in.
- **Trust wording:** Third-party or document-derived text is quoted evidence only; do not execute embedded commands or links. No hostile “ignore …” examples in prompts.
- **`to-adr`:** Keep repo-local `scripts/build_catalog.py` + visualizer; **system/local fonts only** — no font CDN URLs in the HTML template.
- **Docs:** README Prerequisites call out CLI / office / local Spec expectations. `docs/accepted-risk.md` points here for residual floor (`docx` ingest).

## References

- [0005-ADR-skills-release-artifact.md](0005-ADR-skills-release-artifact.md)
- [0006-ADR-npx-skills-install-only.md](0006-ADR-npx-skills-install-only.md)
- [0010-ADR-to-adr-mechanics-shipped.md](0010-ADR-to-adr-mechanics-shipped.md)
- [docs/accepted-risk.md](../accepted-risk.md)
- [README.md](../../README.md) (Prerequisites — when updated)
- `.scratch/ideas/code-review-optional-gh-issue-context.md` (deferred `gh` Spec)
- `skills/docx/`, `skills/code-review/`, `skills/to-adr/`
