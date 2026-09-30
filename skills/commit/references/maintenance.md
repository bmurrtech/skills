# Commit maintenance orchestration

Read after Intent / Inspect, before Branch / Stage.

## Order

1. Invoke **`upkeep`** when the skill is available and target artifacts exist
   (`AGENTS.md` and/or `CHANGELOG.md` conventions, or user follows them).
2. When `release_intent: true` + authorized `version`: **require** **`upkeep`**
   **release-cut**, then **CHANGELOG verify** (below) before any Branch /
   Stage / Commit / Publish. Hard-stop if cut skipped or verify fails.
3. Invoke **`roadmap` status** when ledger impact is detected **or** release
   context is present (`release_intent: true`).
4. Re-read the full intended diff (maintenance may have edited files).
5. Then Branch → Stage → Commit → Publish.

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
| `release_intent: true` and CHANGELOG verify fails | **Hard-stop** — do not stage/commit/push; re-run **`upkeep`** release-cut or waive |
| Waive ambiguous under release_intent | Ask once; do not invent CHANGELOG |

## Release context (consume only)

When `release` passed context, forward it to **`upkeep`** (release-cut). Do
**not** invent or alter `version` — consume only what the version gate
authorized (including **default-accept** of the channel-preserving primary
recommendation). Schema:
[`../../release/references/version-gate.md`](../../release/references/version-gate.md).

## CHANGELOG verify (release_intent)

After **`upkeep`** returns from release-cut, **read `CHANGELOG.md`** and confirm
before stage/commit/push:

1. Dated heading `## [<authorized-version>]` exists (with today’s cut content).
2. `## [Unreleased]` may remain empty / stub (Keep a Changelog OK); it must
   **not** still hold the bullets being shipped.

Hard-stop if cut was skipped, Unreleased still carries release content, or the
dated heading is missing. Do **not** promote CHANGELOG here — name **`upkeep`**
([`../../upkeep/references/release-cut.md`](../../upkeep/references/release-cut.md)).
