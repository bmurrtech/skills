# AGENTS.md

## Project overview

`bmurrtech/skills` is a library of Agent Skills for agentic coding. Create skills only under `skills/`. Glossary/OKF: `CONTEXT.md` + `knowledge/`. ADRs: `docs/adr/`. Local PRDs: gitignored `docs/prd/` (see [how-to-bmurrtech-skills](docs/how-to-bmurrtech-skills.md#local-prds-docsprd); why → [knowledge/prd.md](knowledge/prd.md)).

## Project structure

- `skills/` — tracked skills (`SKILL.md` + `agents/openai.yaml` + optional bundles); **shipped** in release artifact
- `CONTEXT.md` / `knowledge/` — glossary + OKF (**tracked, not shipped**)
- `scripts/package_skills.py` — builds filtered release tarball + sha256
- `scripts/quick_validate.py` / `scripts/init_skill.py` — skill frontmatter validate + scaffold CLIs (library CI/ops; not product skills)
- `.github/workflows/ci.yml` — unittest + package smoke
- `.github/workflows/release.yml` — on `v*` tags: package + GitHub Release assets
- `docs/adr/` — tracked ADRs
- `docs/how-to-bmurrtech-skills.md` — consumer how-to (flows + branches + local PRDs); README links here
- `docs/how-to-adr.md` — ADR authoring + at-a-glance prompts
- `docs/how-to-visual-explainer.md` — visual-explainer modes + prompts
- `docs/skill-scaffold.md` — folders/files setup creates (whys → `knowledge/skill-scaffold.md`)
- `CHANGELOG.md` — Keep a Changelog (Unreleased maintained by **upkeep**)
- `docs/prd/` — local PRDs (ignored)
- `.scratch/` — untracked agent scratch pad (subdir roles → [CONTEXT.md](CONTEXT.md) **.scratch/**)
- `docs/about-license.md` — license explainer
- `AGENTS.md` / `CLAUDE.md` — ops manual + pointer
- `pm/`, `.agents/`, `.claude/`, `.cursor/` — local-only; ignored
- `dist/` — packaging output (ignored)

## Setup & build

```bash
python3 scripts/quick_validate.py skills/<name>
python3 scripts/init_skill.py <name>
python3 scripts/package_skills.py --version <semver> --out dist/
```

Consumer bootstrap: run skill **`setup-bmurrtech-skills`**.

Release packaging: `scripts/package_skills.py` (see [ADR 0005](docs/adr/0005-ADR-skills-release-artifact.md); glossary: [Skills release artifact](knowledge/skills-release-artifact.md)).

## Testing & validation

```bash
python3 scripts/quick_validate.py skills/<name>
python3 -m unittest tests.test_package_skills tests.test_docx_ensure tests.test_adr_catalog -v
```

- Validate every new or edited skill locally with `scripts/quick_validate.py` (CI also validates all `skills/*/SKILL.md` on PR/`main`).
- Do not claim a failed/interrupted/skipped/timed-out check passed.

### Test index (OKF)

One-liners → `knowledge/` test-maps for session-scoped runs (see **`tdd`**).

- [Package skills](knowledge/package-skills.md) — `python3 -m unittest tests.test_package_skills -v`
- [Docx ensure](knowledge/docx-ensure.md) — `python3 -m unittest tests.test_docx_ensure -v`
- [ADR catalog](knowledge/adr-catalog.md) — `python3 -m unittest tests.test_adr_catalog -v`

## Code style

- Lean `SKILL.md`; disclose branch-only detail under `references/`.
- Do not duplicate glossary ↔ AGENTS content.
- Align `policy.allow_implicit_invocation` with whether the skill may model-trigger.

## Git & PR workflow

- Base branch: `main`.
- Do not commit, push, tag, release, or open a PR unless requested.
- Never commit secrets or ignored trees (`pm/`, `docs/prd/`, `.scratch/`, agent dirs, `.env`).

## Boundaries

- Tracked/published skills only under `skills/` (never dual-track SoT into agent dirs). Library-local / maintainer skills may live under ignored `.agents/skills/` so hosts (Cursor) can load them — not tracked, not shipped, not catalog SoT ([ADR 0009](docs/adr/0009-ADR-local-maintainer-skills-host-path.md)).
- After `implement` or `code-review` **in this library**, run **upkeep** then **context** (universal skills soft-skip when those artifacts are absent in consumer repos).
- Accepted ADRs are immutable — supersede via **to-adr**.
- Handoffs go to OS temp as `bmurrtech-skills-handoff-*.md`, not the repo.
- Prefer **grill-me** before implementing ambiguous designs.

## Security

- Never commit API keys, tokens, or `.env` files.
- Prefer reading curl-installed scripts before piping to a shell.

## References

- [CONTEXT.md](CONTEXT.md)
- [knowledge/index.md](knowledge/index.md)
- [docs/adr/index.md](docs/adr/index.md)
- [docs/about-prd.md](docs/about-prd.md) — thin pointer (ADR 0007); PRD how-to in how-to-bmurrtech-skills
- [README.md](README.md)
- [docs/how-to-bmurrtech-skills.md](docs/how-to-bmurrtech-skills.md)
- [docs/how-to-adr.md](docs/how-to-adr.md)
- [docs/how-to-visual-explainer.md](docs/how-to-visual-explainer.md)
- [docs/skill-scaffold.md](docs/skill-scaffold.md)
- [CHANGELOG.md](CHANGELOG.md)
