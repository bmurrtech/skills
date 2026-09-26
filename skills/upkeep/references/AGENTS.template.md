# AGENTS.md

## Project overview

<One short paragraph describing the project and the areas a coding agent is most
likely to touch. Link deeper documentation rather than repeating it.>

## Project structure

- `<path>/` — <purpose>
- `<path>/` — <purpose>
- `<path>/` — <purpose>

## Setup & build

```bash
<install command>
<build command>
```

## Testing & validation

```bash
<full test command>
<single-test command>
<lint command>
<typecheck command>
```

- Run the smallest relevant check while iterating (prefer Test index → OKF test-maps).
- Run the required broader checks before considering the change complete.
- Never delete or weaken a valid test merely to make a change pass.
- Do not claim a failed, interrupted, skipped, or timed-out check passed.

### Test index (OKF)

One-liners only — each points at a `knowledge/` test-map. Maintained by **`tdd`** / **`upkeep`**. Load maps for the current seams; do not dump the whole `tests/` tree into context.

```markdown
- [<capability>](knowledge/<slug>.md) — `<smallest run command>`
```

## Code style

- Formatter: <tool/command>.
- Linter: <tool/command>.
- Follow patterns in neighboring files before introducing a new abstraction.
- Do not reformat unrelated code.
- Do not add comments that merely restate obvious code behavior.

## Git & PR workflow

- Base branch: `<branch>`.
- PR target: `<branch>`.
- Commit convention: <convention>.
- Required checks: <checks>.
- Do not commit, push, tag, release, or open a PR unless requested.

## Boundaries

- Do not modify unrelated files or widen the requested scope.
- Do not add dependencies without approval unless repository policy explicitly
  permits it.
- Do not edit generated files directly; use <generator command/workflow>.
- Never commit secrets, API keys, credentials, `.env` files, or production data.
- <project-specific prohibition>

## References

- `<path-or-url>` — <what it covers>
- `CHANGELOG.md` — Keep a Changelog; upkeep keeps Unreleased current after implement/review
