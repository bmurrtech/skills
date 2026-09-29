# Commit maintenance orchestration

Read after Intent / Inspect, before Branch / Stage.

## Order

1. Invoke **`upkeep`** when the skill is available and target artifacts exist
   (`AGENTS.md` and/or `CHANGELOG.md` conventions, or user follows them).
2. Invoke **`roadmap` status** when ledger impact is detected **or** release
   context is present (`release_intent: true`).
3. Re-read the full intended diff (maintenance may have edited files).
4. Then Branch → Stage → Commit → Publish.

Canonical push / review publish / local-only are **publish routes only** — never
skip maintenance because the route is “just a push.”

## Ledger impact (when to call roadmap status)

Treat as impact when any of:

- Diff touches `docs/ROADMAP.md`
- Session absorbed or closed a ROADMAP idea (shipped skill, Done marking needed)
- Release context is present (cut may warrant Status / shipped-in-version)
- User explicitly asked to update roadmap status

Otherwise skip roadmap with no noise.

## Soft-skip vs release_intent

| Condition | Behavior |
|-----------|----------|
| Missing `upkeep` / `roadmap` / artifacts; ordinary commit | Soft-skip; one-line note |
| `release_intent: true` and missing `upkeep` or `CHANGELOG.md` | **Hard-stop** unless user explicitly waives |
| Waive ambiguous under release_intent | Ask once; do not invent CHANGELOG |

## Release context (consume only)

When `release` passed context, forward it to **`upkeep`** (release-cut). Do
**not** invent or alter `version` — schema lives in
[`../../release/references/version-gate.md`](../../release/references/version-gate.md).
