# Upkeep release-cut

Read when **release context** is present (`release_intent: true` + confirmed
`version`), or when classifying soft-skip vs hard-stop for CHANGELOG work.

## Ordinary vs release-cut

| Mode | Trigger | CHANGELOG action |
|------|---------|------------------|
| Ordinary | implement / code-review / commit maintenance | Ensure Unreleased; add session bullets; **no** version bump |
| Release-cut | `release_intent` + confirmed version | Promote Unreleased → dated `## [X.Y.Z…]` (today’s date); leave empty Unreleased |

Consume authorized `version` only — do not invent or alter it. Schema:
[`../../release/references/version-gate.md`](../../release/references/version-gate.md).

## Missing CHANGELOG

| Condition | Behavior |
|-----------|----------|
| Missing file, ordinary | Create Keep a Changelog stub with Unreleased |
| Missing file, `release_intent` | **Hard-stop** unless user explicitly waives |
| Waive ambiguous | Ask once; do not invent cut content |

Soft-skip / hard-stop orchestration for callers:
[`../../commit/references/maintenance.md`](../../commit/references/maintenance.md).
