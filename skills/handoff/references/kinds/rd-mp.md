# Kind: `rd-mp`

Delta only — apply on top of [handoff-base.md](../handoff-base.md).

## When

Next session should run **`roadmap`** (promote / status / publish). Do not invent
tracker fields.

## Extra / specialize

### Kind block — roadmap

```markdown
## Kind: roadmap (rd-mp)
- **Action:** `<promote | status | publish>`
- **Source idea path:** `<.scratch/ideas/… or none>`
- **Ledger:** `docs/ROADMAP.md`
- **Publish target:** `<none | GitHub | Fizzy | …>` — only if user asked
- **Do not:** invent Domain/Scope fields the user did not imply
```

## Base fill rules

| Base section | Rule |
|--------------|------|
| Next action | Skill = `roadmap` + action |
| Suggested skills | `roadmap` first |
| Settled decisions | Link prior idea scratch / CONTEXT if relevant |
