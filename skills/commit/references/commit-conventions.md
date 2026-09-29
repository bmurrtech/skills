# Commit conventions

Read when drafting the commit message (step 3).

## Shape

```text
<type>[optional scope][optional !]: <short description>
```

Common types: `feat` `fix` `docs` `refactor` `test` `ci` `build` `perf`
`style` `chore` `revert`.

Prefer `fix(scope):` / `chore(release): prepare X.Y.Z` over inventing exotic
top-level types (`hotfix`, `release` as type).

`chore` is a fallback, not the default for feature/fix work.

## Examples

```text
docs: document release workflow
fix(release): reject invalid tags
feat(cli): add release status
chore(release): prepare 0.2.0
feat!: change manifest format
```
