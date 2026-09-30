# Kind: `impl`

Delta only — apply on top of [handoff-base.md](../handoff-base.md).

## When

Next session should **`implement`** a known plan/spec. Do not re-grill.

## Extra / specialize

### Kind block — implement

```markdown
## Kind: implement (impl)
- **Spec path(s):** `<plan / PRD / issue path>`
- **Do not:** re-open grill; re-litigate settled decisions
- **Validation cue:** `<targeted test command or N/A>`
- **After green:** run **`upkeep`** → **`context`** when those artifacts exist;
  then review via **subagent `code-review`** or **`handoff`** for code-review
  (no same-session inline review); never stage/commit/push/PR — name
  **`commit`** for later user intent
```

## Base fill rules

| Base section | Rule |
|--------------|------|
| Next action | Skill = `implement`; Spec path required when known |
| Acceptance / constraints | Pull short DoD bullets from plan/conversation; inline |
| Suggested skills | `implement` first; then `tdd` if seams; housekeeping inside implement; review via **subagent `code-review`** or **`handoff`** for code-review (no same-session inline); name `commit` (do not run from implement) |
