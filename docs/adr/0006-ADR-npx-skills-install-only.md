# Install via npx skills only (defer curl gateway)

<!-- File: docs/adr/0006-ADR-npx-skills-install-only.md -->

## Status
Accepted
- **Date (optional):** 2026-09-26
- **Supersedes:** —
- **Superseded by:** —
- **Related ADRs:** [0005-ADR-skills-release-artifact.md](0005-ADR-skills-release-artifact.md), [0011](0011-ADR-skill-scanner-posture-prereqs.md)
- **Related PRDs:** —

## Context and Problem Statement

Consumers need a supported way to install this skills library. README advertised both `npx skills add bmurrtech/skills` and `curl | sh` via `get.mycmd.site`. The curl path needs a Cloudflare Worker, registry/catalog, bootstrap installer, and ongoing channel updates — while the audience already has Node and a native skills CLI. Should we implement the curl alternative now?

## Decision Drivers

* Match the primary audience (agent hosts with Node / `npx`)
* Avoid permanent maintenance for a second install surface (Worker, CF tokens, registry, `curl | sh` trust)
* Keep GitHub Release artifacts available for future adapters without promising a broken public curl URL
* Prefer one supported install UX until a concrete no-Node or gateway requirement appears

## Considered Options

* Ship **npx skills only** now; defer curl/Cloudflare gateway for this library
* Implement curl + Worker + registry now (single-repo or distribution gateway)
* Document both, with curl marked experimental / best-effort

## Decision Outcome

Chosen option: "Ship **npx skills only** now; defer curl/Cloudflare gateway for this library", because curl is unnecessary overhead for this product’s audience and the package-repo Release pipeline already covers the shared artifact need without a second installer.

### Consequences

* Good, because one supported install path; no false `get.mycmd.site` promise
* Good, because Cloudflare/Worker/catalog work stays optional until a real gateway or no-Node need
* Good, because ADR 0005 release tarballs remain for later curl/plugin adapters
* Bad, because environments without Node have no first-party installer until curl (or equivalent) returns

### Confirmation

README Quick start documents `npx skills add` only (no curl alternative). CI/release workflows package GitHub Release assets without requiring Worker deploy.

## Pros and Cons of the Options

### Ship npx skills only (defer curl)

* Good, because aligns with `skills` CLI ecosystem
* Good, because no Worker/registry/channel ops tax
* Bad, because no curl for air-gapped / no-Node machines

### Implement curl + Worker now

* Good, because stable `get.` URL and channel pins (`@stable`, `@1.4.2`)
* Good, because reuses a multi-product distribution gateway pattern if one already exists
* Bad, because large maintenance and trust surface for overlapping UX
* Bad, because current workflows only cover package-repo half — curl still needs full CF control plane

### Document both (curl experimental)

* Good, because keeps the door open in docs
* Bad, because users hit a non-functional or unmaintained path
* Bad, because “experimental” still implies support

## Assumptions

- Primary consumers can run `npx skills add bmurrtech/skills`.
- GitHub Releases from `release.yml` stay the artifact SoT for future non-npx adapters.
- A later ADR may reintroduce curl if `get.mycmd.site` gateway adoption or no-Node demand is concrete.

## Constraints

- Do not advertise a public curl install URL until Worker + registry + bootstrap + checksum path are live.
- Do not treat deferring curl as permission to drop filtered Release packaging (ADR 0005).

## Implementation Notes (Normative)

- Supported install: `npx skills add bmurrtech/skills` (and skill-scoped variants).
- Keep `.github/workflows/release.yml` publishing `bmurrtech-skills-<ver>.tar.gz` + `.sha256`.
- Curl / Cloudflare gateway for this library is **out of scope** until superseded or extended by a new ADR.
