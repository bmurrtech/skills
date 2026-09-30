# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

### Changed

### Fixed

## [0.2.2-rc2] - 2026-09-30

Operator-facing ship: setup **Commit PRDs?** A/B (ADR 0013), grill post-frontier A/B/C routes, and tighter release CHANGELOG verify — plus version-gate **recommend-as-default**.

### Added

- **[ADR 0013](docs/adr/0013-ADR-prd-tracking-choice.md)** — setup **Commit PRDs?** A ignore (default) / B track; supersedes [0007](docs/adr/0007-ADR-scaffold-omit-about-prd.md)’s always-ignore constraint (still omits `about-prd.md` from scaffold).

### Changed

- **`setup-bmurrtech-skills`**: re-asks PRD A/B every run; writes `.gitignore` + `AGENTS.md` (+ `CONTEXT.md` when stub/edit ok) per [references/prd-tracking.md](skills/setup-bmurrtech-skills/references/prd-tracking.md).
- **`to-prd`**, OKF (`knowledge/prd.md`), skill-scaffold, how-to, README, CONTEXT/AGENTS: dual policy (ignore or track).
- **`grill-me`**: after frontier empty, prompt A/B/C next steps (recommend **A** `/to-prd`; **B** auto-`handoff` implement/`impl`; **C**/`Go` bare implement without `/implement`) — replaces separate “confirm shared understanding” beat; details in `references/next-steps.md`. Light cross-links in `to-prd`, `implement`, `handoff` `impl` kind, how-to, CONTEXT.
- **`release` version gate**: channel-preserving primary **recommend** is ➡️ default when no override (LGTM / affirmatives / “go with recommended” authorize that pair); still never invent outside the table. Wired through `release` / `commit` maintenance, how-to, CONTEXT, README.

### Fixed

- **Review nits (PRD tracking / grill exit):** B-flip strips any contiguous `docs/prd` policy comment (not only “local PRDs”); **`upkeep`** + `knowledge/upkeep.md` bound “don’t heal B” (no re-add `/docs/prd/` ignore); drop leftover “local PRD” blurbs; disambiguate setup policy A/B vs grill next-step A/B/C in prompts; AGENTS Overview/Structure templates in `prd-tracking.md`.
- **`release` / `commit` / `upkeep`**: under `release_intent`, require **`upkeep`** release-cut then **CHANGELOG verify** (dated `## [<version>]` present; Unreleased must not still hold ship bullets) before stage/commit/push/tag — hard-stop if cut skipped.
- **README**: “Update installed skills” documents `npx skills list` / `ls` for installed status (no invented pack SemVer); points updates at `add --all` / `update`.

## [0.2.2-rc1] - 2026-09-30

Operator-facing ship: clearer **handoff** cold-starts and an **implement** path that pauses for fresh review instead of owning Git.

### Added

- **`handoff` hybrid briefs** — base template + closed kind overlays (implement, code-review, ADR, PRD, idea, roadmap, visual-explainer). After write: short in-chat **at-a-glance** (path, temp|keep, next action, check bullets). Kind labels read as **Display (slug)** e.g. code-review (`cd-rvw`). Decision: [ADR 0012](docs/adr/0012-ADR-handoff-hybrid-kinds.md).
- **Ship path clarity** — how-to + README cycle diagrams use `/skill` names; full git tail after review lives in the how-to (commit → merge → release).
- **Implement SoC content contract** — `tests.test_implement_soc` (+ OKF test map) gates review-exit + hard Git-ban wording; wired into AGENTS bulk + CI/release unittests.

### Changed

- **`implement`**: after checks + soft housekeeping, exits via **fresh-context review** (subagent **`code-review`**, or **`handoff`** → fresh **`code-review`**). Never stages/commits/pushes — publish with **`commit`** when you intend to. Soft-suggests a **new** grill session if design cracks mid-build.
- **`handoff`**: portable file is the brief (not “see this chat”); aim ask only when ambiguous; filenames `{kind}-{slug}-{ts}`; temp by default, **keep** → `.scratch/handoffs/`.
- Catalog / glossary: `skills.sh.json` Ship description + Universal sprint skill wording match the new review/Git SoC.

### Fixed

- **`impl` kind** After green / Suggested skills aligned with full Git ban + subagent review exit (no same-session CR implication).

## [0.2.1-rc1] - 2026-09-29

### Added

- **`release`**: **version gate** + **publication gate**; structured **release context** into **`commit`** / **`upkeep`** (refs under `skills/release/references/`).
- **`commit`**: maintenance orchestration — always **`upkeep`** when applicable; conditional **`roadmap` status** on ledger impact / release context ([`references/maintenance.md`](skills/commit/references/maintenance.md)).
- **`upkeep`**: **release-cut** mode — Unreleased → dated section when `release_intent` + confirmed version.
- **`roadmap`**: **status** action (Done / Advanced / Superseded + optional shipped-in-version); [`references/status.md`](skills/roadmap/references/status.md).
- **`merge`**: hard-stop when required maintenance is missing on the reviewed head; route back through **`commit`** (no merge-time mutation).

### Changed

- CHANGELOG SoC: `release` no longer promotes Unreleased → dated; **`upkeep`** owns all CHANGELOG mutation.
- How-to / README / `skills.sh.json` **Git lifecycle** callouts for gates + maintenance.
- Glossary: **Git lifecycle**, **Version gate** / **publication gate**, **Release context** (CONTEXT.md).

## [0.2.0] - 2026-09-28

### Added

- **Git lifecycle** skills: **`commit`**, **`merge`**, **`release`** — local-first commits / gate-aware PR merge / build-before-tag releases; catalog group in `skills.sh.json`, README, and [docs/how-to-bmurrtech-skills.md](docs/how-to-bmurrtech-skills.md#git-lifecycle).
- **`grill-me`**: **rec-default** — affirmative or silent answers accept unanswered ➡️ recommendations.

### Changed

- ROADMAP “Release skill” → **Done** (absorbed into **`release`** / suite).
- **`commit`**: branch-before-commit for review publish; how-to Intent matrix points at skill SoT.
- README: update-via `npx skills@latest add bmurrtech/skills --all`; leaner Features; docx section above Roadmap.

## [0.1.1-rc1] - 2026-09-27

Scanner-posture harden + docx operator-install path.

### Added

- ADR 0011: prerequisite-driven scanner posture for published skills (no agent CLI download; local Spec; no font CDNs); [docs/accepted-risk.md](docs/accepted-risk.md) points here.
- [docs/how-to-docx-cli.md](docs/how-to-docx-cli.md): operator install for pinned docx-cli (**0.26.0**); DIGESTS for manual verify only.

### Changed

- **`code-review`**: Spec sources are local only (user path → `docs/` / `specs/` / `.scratch/` / `docs/prd/` → ask); no tracker/`gh` fetch; trust wording is evidence-only without attack-demo phrases ([ADR 0011](docs/adr/0011-ADR-skill-scanner-posture-prereqs.md)). Optional `gh` Spec deferred to `.scratch/ideas/code-review-optional-gh-issue-context.md`.
- **`to-adr`**: document repo-local `build_catalog.py` I/O + side effects; at-a-glance HTML uses system fonts only (no Google Fonts CDN).
- **`docx`**: probe-only ensure (no `--install` / download); upstream capability fold-in (`references/commands.md` + richer workflows); README Prerequisites + Acknowledgements for [kklimuk/docx-cli](https://github.com/kklimuk/docx-cli); **`setup-bmurrtech-skills`** points at how-to.

## [0.1.0-rc1] - 2026-09-27

First public beta (release candidate). Install via the skills CLI (GitHub source — not an npm package for this repo):

```bash
npx skills@latest add bmurrtech/skills
```

GitHub Release assets (`bmurrtech-skills-0.1.0-rc1.tar.gz` + `.sha256`) are the filtered artifact for future adapters (ADR 0005); `npx skills` clones the git tree and installs skill folders only (ADR 0006).

### Added

- **`idea`**: capture exploratory thoughts under `.scratch/ideas/` (preserve first; never promote/publish).
- **`roadmap`**: durable `docs/ROADMAP.md` ledger; promote from scratch; explicit GitHub/Fizzy publish branch; scripts `ensure_header` / `append_entry` / `mark_promoted`.
- [docs/ROADMAP.md](docs/ROADMAP.md): unordered idea ledger + seed entries (debug/OKF, issue tracking, context-bloat spikes, OMX ultrawork/ralph — research/future mint only; no stub skills yet).
- [knowledge/roadmap.md](knowledge/roadmap.md) + [knowledge/roadmap-promote.md](knowledge/roadmap-promote.md) + `tests/test_roadmap_promote.py` (CI-gated).
- [docs/how-to-adr.md](docs/how-to-adr.md): ADR scope, OKF integration, at-a-glance refresh prompts.
- [knowledge/skill-scaffold.md](knowledge/skill-scaffold.md): why consumer scaffold paths exist.
- [knowledge/adr-catalog.md](knowledge/adr-catalog.md) + `tests/test_adr_catalog.py`: to-adr catalog/visualizer seam.
- ADR 0010: ADR template SoT lives in shipped **`to-adr`** mechanics (supersedes ADR 0003).
- **`to-adr`**: at-a-glance catalog under `.scratch/adr-optics/` (`build_catalog.py --visualize --open`).
- **`visual-explainer`**: lean intent-routed HTML diagrams / reviews / slides under `.scratch/diagrams/`; [docs/how-to-visual-explainer.md](docs/how-to-visual-explainer.md).
- [docs/how-to-bmurrtech-skills.md](docs/how-to-bmurrtech-skills.md): install → shape → ship (flows, branches, clusters, local PRDs).
- [docs/skill-scaffold.md](docs/skill-scaffold.md): folders/files **`setup-bmurrtech-skills`** creates (inventory; whys → knowledge).
- ADR 0007: setup omits library PRD explainer from consumers (supersedes ADR 0004 setup note).
- ADR 0008: maintainer skill scaffolding is local-only (superseded by 0009).
- ADR 0009: local maintainer skills under ignored `.agents/skills/` (host-readable; not tracked/shipped).
- **`docx`**: Word `.docx` via pinned docx-cli; `ensure_office.py` probes Word/LibreOffice and can install LibreOffice (brew/winget/apt/dnf/pacman). Optional from **`setup-bmurrtech-skills`** (“Want AI to edit your `.docx` files?”).
- **`docx`**: `toolchain_ready.py` (`ToolchainReady` evidence) + `ensure_toolchain.py` façade (delegates to `ensure_docx` / `ensure_office`; does not fuse cores). Injectable download/run adapters for unit tests.
- Initial skills library under `skills/` (`setup-bmurrtech-skills`, `writing-for-agents`, `grill-me`, `context`, `upkeep`, `to-adr`, `to-prd`, `tdd`, `implement`, `code-review`, `ascii`, `wait-what`, `handoff`, `docx`, `idea`, `roadmap`, `visual-explainer`).
- **`writing-for-agents`**: levers for any agent-consumed doc (context pointers, two loads, hierarchy, completion criteria, leading words, pruning); skill mechanics + checklist under `references/`.
- `CONTEXT.md` + `knowledge/` OKF bundle; `docs/adr/` (MADR); `docs/about-prd.md`; `AGENTS.md` / `CLAUDE.md` pointer.
- Apache-2.0 `LICENSE`; consumer bootstrap via `npx skills add bmurrtech/skills`.
- `.scratch/` convention: gitignored agent scratch pad for exploratory / pre-PRD dumps (`setup-bmurrtech-skills`, `.gitignore`); ideas → `.scratch/ideas/`; keep handoffs → `.scratch/handoffs/`.
- OKF **test maps** + `AGENTS.md` Test index for session-scoped TDD (`tdd`, `knowledge/test-map.md`).
- Glossary terms for universal vs library-specific sprint skills; `.scratch/`; test maps.
- `CHANGELOG.md` (this file).
- `scripts/package_skills.py` + `tests/test_package_skills.py`: filtered **skills release artifact** (`skills/` + `LICENSE` only; excludes `__pycache__` / bytecode).
- ADR 0005: release packaging excludes library OKF (do not gitignore `knowledge/` for clean installs).
- ADR 0006: supported install is **`npx skills` only**; defer curl / Cloudflare gateway for this library.
- `.github/workflows/ci.yml`: unittest + all-skills `quick_validate` + package smoke on `main` / PRs.
- `.github/workflows/release.yml`: on `v*` tags, build filtered tarball + sha256 and attach to GitHub Release.

### Changed

- **`handoff`**: default remains throwaway OS temp; **keep** / non-transitory → `.scratch/handoffs/{yyyyMMdd-HHmmss}-handoff.md` (writing-for-agents reshape).
- Docs: `how-to-adr.md` trims placement/OKF diagrams and multi-OS open recipes to prompts+scope; catalog JSON row shape SoT in [knowledge/adr-catalog.md](knowledge/adr-catalog.md).
- Docs: ADR at-a-glance output path `.scratch/adr-optics/` (was under diagrams); setup provisions both scratch subdirs; visualize auto-opens browser (`--open`).
- Docs: `how-to-use-bmurrtech-skills.md` → `how-to-bmurrtech-skills.md`; PRD how-to content lives there; `about-prd.md` kept as thin ADR 0007 pointer; `skill-scaffold.md` inventory-only; visual-explainer how-to drops install/setup duplication.
- **`to-adr`**: self-contained skill; `references/madr.md` → `references/mechanics.md`; writing-for-agents-shaped workflow + Boundaries.
- **`setup-bmurrtech-skills`**: ensure `.scratch/diagrams/` + `.scratch/adr-optics/`; do not copy library how-tos into consumers.
- README: compact ASCII spine; links to how-to-adr / visual-explainer / skill-scaffold + knowledge why.
- **`writing-for-agents`**: full lever set; mechanics under `references/`. Soft-skips validators when absent.
- Unship **`skill-create`** from the product catalog (ADR 0009); local maintainer path under ignored `.agents/skills/`.
- **`implement`**, **`code-review`**, **`tdd`**: portable for any consumer repo (target-repo checks; soft-gate `upkeep`/`context`).
- **`code-review`**: severity (`CRITICAL`–`LOW`) + `APPROVE` / `REQUEST CHANGES` / `COMMENT`; Standards axis loads checklist + deslop lens via `references/` (no body bloat).
- **`grill-me`**, **`wait-what`**: soft-gate CONTEXT/OKF when artifacts are absent.
- **`upkeep`**: preserve Test index one-liners; document `.scratch/` in template; **own `CHANGELOG.md`** (create if missing; keep Unreleased current after implement/code-review).
- **`to-adr`**: classify cited prior ADRs as **supersede** vs **relate** vs **reject-option-cost** (citing “breaks ADR N” under a rejected option is relate, not supersede); MADR Status includes Related ADRs.
- README: deslopped copy; Features table updated for portable sprint skills and `.scratch/` / test-maps.

### Removed

- `docs/how-to-use-bmurrtech-skills.md` (renamed to `how-to-bmurrtech-skills.md`).
- **`skill-create`** as a shipped / documented universal skill.
