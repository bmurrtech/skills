# Kind: `prd`

Delta only — apply on top of [handoff-base.md](../handoff-base.md).

## When

Next session should author or edit a PRD via **`create-prd`**. Handoff does **not**
write the PRD body.

Common entry: **`grill-me`** post-grill **A** usually auto-runs **`create-prd`**
in-session (no handoff). Use this kind when the operator still wants a packed
brief before PRD authoring.

## Extra / specialize

### Kind block — PRD

```markdown
## Kind: create-prd (prd)
- **Action:** `<create | edit>`
- **Topic / working title:** `<…>`
- **Existing PRD path:** `<docs/prd/… or none>`
- **Cite ADRs:** `<paths or none>`
- **Do not:** draft FR/DoD/journey inside this handoff — that is **`create-prd`**
```

## Base fill rules

| Base section | Rule |
|--------------|------|
| Next action | Skill = `create-prd` |
| Acceptance / constraints | Scope intent / non-goals as short bullets if known |
| Suggested skills | `create-prd` first; `create-adr` / `ascii` only if warranted |
| Settled decisions | Link grilled decisions / CONTEXT terms |
