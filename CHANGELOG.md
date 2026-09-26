# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

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

### Changed

- Docs: `how-to-adr.md` trims placement/OKF diagrams and multi-OS open recipes to prompts+scope; catalog JSON row shape SoT in [knowledge/adr-catalog.md](knowledge/adr-catalog.md).
- Docs: ADR at-a-glance output path `.scratch/adr-optics/` (was under diagrams); setup provisions both scratch subdirs; visualize auto-opens browser (`--open`).
- Docs: `how-to-use-bmurrtech-skills.md` → `how-to-bmurrtech-skills.md`; PRD how-to content lives there; `about-prd.md` kept as thin ADR 0007 pointer; `skill-scaffold.md` inventory-only; visual-explainer how-to drops install/setup duplication.
- **`to-adr`**: self-contained skill; `references/madr.md` → `references/mechanics.md`; writing-for-agents-shaped workflow + Boundaries.
- **`setup-bmurrtech-skills`**: ensure `.scratch/diagrams/` + `.scratch/adr-optics/`; do not copy library how-tos into consumers.
- README: compact ASCII spine; links to how-to-adr / visual-explainer / skill-scaffold + knowledge why.
- **`writing-for-agents`**: full lever set; mechanics under `references/`. Soft-skips validators when absent.
- Unship **`skill-create`** from the product catalog (ADR 0009).

### Removed

- `docs/how-to-use-bmurrtech-skills.md` (renamed to `how-to-bmurrtech-skills.md`).
- **`skill-create`** as a shipped / documented universal skill.

## [0.1.0-rc1] - 2026-09-26

First public beta (release candidate). Install via the skills CLI (GitHub source — not an npm package for this repo):

```bash
npx skills@latest add bmurrtech/skills
```

GitHub Release assets (`bmurrtech-skills-0.1.0-rc1.tar.gz` + `.sha256`) are the filtered artifact for future adapters (ADR 0005); `npx skills` clones the git tree and installs skill folders only (ADR 0006).

### Added

- **`docx`**: Word `.docx` via pinned docx-cli; `ensure_office.py` probes Word/LibreOffice and can install LibreOffice (brew/winget/apt/dnf/pacman). Optional from **`setup-bmurrtech-skills`** (“Want AI to edit your `.docx` files?”).
- **`docx`**: `toolchain_ready.py` (`ToolchainReady` evidence) + `ensure_toolchain.py` façade (delegates to `ensure_docx` / `ensure_office`; does not fuse cores). Injectable download/run adapters for unit tests.
- Initial skills library under `skills/` (`setup-bmurrtech-skills`, `skill-create`, `writing-for-agents`, `grill-me`, `context`, `upkeep`, `to-adr`, `to-prd`, `tdd`, `implement`, `code-review`, `ascii`, `wait-what`, `handoff`).
- **`writing-for-agents`**: levers for any agent-consumed doc (context pointers, two loads, hierarchy, completion criteria, leading words, pruning); skill mechanics + checklist under `references/`.
- `CONTEXT.md` + `knowledge/` OKF bundle; `docs/adr/` (MADR); `docs/about-prd.md`; `AGENTS.md` / `CLAUDE.md` pointer.
- Apache-2.0 `LICENSE`; consumer bootstrap via `npx skills add bmurrtech/skills`.
- `.scratch/` convention: gitignored agent scratch pad for exploratory / pre-PRD dumps (`setup-bmurrtech-skills`, `.gitignore`).
- OKF **test maps** + `AGENTS.md` Test index for session-scoped TDD (`tdd`, `knowledge/test-map.md`).
- Glossary terms for universal vs library-specific sprint skills; `.scratch/`; test maps.
- `CHANGELOG.md` (this file).
- `scripts/package_skills.py` + `tests/test_package_skills.py`: filtered **skills release artifact** (`skills/` + `LICENSE` only; excludes `__pycache__` / bytecode).
- ADR 0005: release packaging excludes library OKF (do not gitignore `knowledge/` for clean installs).
- ADR 0006: supported install is **`npx skills` only**; defer curl / Cloudflare gateway for this library.
- `.github/workflows/ci.yml`: unittest + all-skills `quick_validate` + package smoke on `main` / PRs.
- `.github/workflows/release.yml`: on `v*` tags, build filtered tarball + sha256 and attach to GitHub Release.

### Changed

- **`implement`**, **`code-review`**, **`tdd`**: portable for any consumer repo (target-repo checks; soft-gate `upkeep`/`context`).
- **`code-review`**: severity (`CRITICAL`–`LOW`) + `APPROVE` / `REQUEST CHANGES` / `COMMENT`; Standards axis loads checklist + deslop lens via `references/` (no body bloat).
- **`grill-me`**, **`wait-what`**: soft-gate CONTEXT/OKF when artifacts are absent.
- **`upkeep`**: preserve Test index one-liners; document `.scratch/` in template; **own `CHANGELOG.md`** (create if missing; keep Unreleased current after implement/code-review).
- **`to-adr`**: classify cited prior ADRs as **supersede** vs **relate** vs **reject-option-cost** (citing “breaks ADR N” under a rejected option is relate, not supersede); MADR Status includes Related ADRs.
- README: deslopped copy; Features table updated for portable sprint skills and `.scratch/` / test-maps.
