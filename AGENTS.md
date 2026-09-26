# AGENTS.md

## Project overview

`bmurrtech/skills` is a library of Agent Skills for agentic coding. Create skills only under `skills/`. Glossary/OKF: `CONTEXT.md` + `knowledge/`. ADRs: `docs/adr/`. Local PRDs: gitignored `docs/prd/` (see `docs/about-prd.md`).

## Project structure

- `skills/` — tracked skills (`SKILL.md` + `agents/openai.yaml` + optional bundles)
- `CONTEXT.md` / `knowledge/` — glossary + OKF
- `docs/adr/` — tracked ADRs
- `docs/prd/` — local PRDs (ignored)
- `docs/about-prd.md` / `docs/about-license.md` — tracked explainers
- `AGENTS.md` / `CLAUDE.md` — ops manual + pointer
- `pm/`, `.agents/`, `.claude/`, `.cursor/` — local-only; ignored

## Setup & build

```bash
python3 skills/skill-create/scripts/quick_validate.py skills/<name>
python3 skills/skill-create/scripts/init_skill.py <name>
```

Consumer bootstrap: run skill **`setup-bmurrtech-skills`**.

## Testing & validation

```bash
python3 skills/skill-create/scripts/quick_validate.py skills/<name>
```

- Validate every new or edited skill (including presence of `agents/openai.yaml` via workflow).
- Do not claim a failed/interrupted/skipped/timed-out check passed.

## Code style

- Lean `SKILL.md`; disclose branch-only detail under `references/`.
- Do not duplicate glossary ↔ AGENTS content.
- Align `policy.allow_implicit_invocation` with whether the skill may model-trigger.

## Git & PR workflow

- Base branch: `main`.
- Do not commit, push, tag, release, or open a PR unless requested.
- Never commit secrets or ignored trees (`pm/`, `docs/prd/`, agent dirs, `.env`).

## Boundaries

- Never create skills outside `skills/`.
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
- [docs/about-prd.md](docs/about-prd.md)
- [README.md](README.md)
