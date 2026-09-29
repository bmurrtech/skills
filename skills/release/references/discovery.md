# Release discovery

Read in step 1.

## Ladder (cheap → deep)

1. `CONTEXT.md`, `AGENTS.md`, release docs / ADRs
2. `.github/workflows/*`, scripts, Makefile/task runners
3. Root manifests only (`Cargo.toml`, `package.json`, `pyproject.toml`, `go.mod`, …)
4. Targeted search for unanswered release questions
5. Broader inspection only if still ambiguous

Do not recursively ingest the repository up front.

## Decision

```text
tag-triggered release workflow exists?
  yes → use it (thin orchestration over repo-native command)
  no  → can confidently infer reproducible contract?
         yes → build locally first
               succeeds → BOOTSTRAP (scaffold) — no tag same run
               fails    → stop; fix build
         no  → gap report; stop before inventing CI
```

## Prefer

```text
repository-native release command
        ↓
scripts/package_* | make release | cargo … | npm run … | python …
        ↓
works locally
        ↓
release.yml calls the same thing
```

## Dogfood fixture (this library)

When **both** are present:

- `scripts/package_skills.py --version <semver> --out dist/`
- `.github/workflows/release.yml` on `push.tags: ["v*"]`

→ that pair is the contract (ADR 0005). Do not invent an alternate packaging or
publication path (including competing `gh release create` when the workflow
owns publication).
