# Merge maintenance check

Read during readiness when deciding whether the reviewed head is missing
required maintenance.

## Hard-stop signals

Any of:

- Diff ships skill/docs/operator-facing behavior but `CHANGELOG.md` Unreleased
  (or dated cut) does not reflect it
- Release-prep PR expected `upkeep` / CHANGELOG / release-cut and those edits
  are absent on the head
- User or CI notes call out stale AGENTS/CHANGELOG for this change set

## Action

**Stop.** Do not edit the PR head. Instruct return through **`commit`**
(orchestrates **`upkeep`** / **`roadmap`**). Re-enter merge after the new head
lands.

Do not invent gates from advisory bots; GitHub mergeability remains separate.
