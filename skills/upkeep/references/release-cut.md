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

## Release-cut Done-when (evidence)

After promoting, **`CHANGELOG.md` must show**:

1. A dated heading `## [<authorized-version>]` (Keep a Changelog date OK) whose
   body holds the bullets just shipped — not still under Unreleased.
2. `## [Unreleased]` still present above dated releases; may be empty or a stub
   (section headers only). It must **not** retain the bullets for this cut.

If either fails → cut is incomplete; do not report success. Callers
(**`commit`** / **`release`**) hard-stop before stage/commit/push/tag — see
[`../../commit/references/maintenance.md`](../../commit/references/maintenance.md)
**CHANGELOG verify**.

## Missing CHANGELOG

| Condition | Behavior |
|-----------|----------|
| Missing file, ordinary | Create Keep a Changelog stub with Unreleased |
| Missing file, `release_intent` | **Hard-stop** unless user explicitly waives |
| Waive ambiguous | Ask once; do not invent cut content |

Soft-skip / hard-stop orchestration for callers:
[`../../commit/references/maintenance.md`](../../commit/references/maintenance.md).
