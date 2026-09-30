# Kind: `prd`

Delta only — apply on top of [handoff-base.md](../handoff-base.md).

## When

Next session should author or edit a PRD via **`to-prd`**. Handoff does **not**
write the PRD body.

## Extra / specialize

### Kind block — PRD

```markdown
## Kind: to-prd (prd)
- **Action:** `<create | edit>`
- **Topic / working title:** `<…>`
- **Existing PRD path:** `<docs/prd/… or none>`
- **Cite ADRs:** `<paths or none>`
- **Do not:** draft FR/DoD/journey inside this handoff — that is **`to-prd`**
```

## Base fill rules

| Base section | Rule |
|--------------|------|
| Next action | Skill = `to-prd` |
| Acceptance / constraints | Scope intent / non-goals as short bullets if known |
| Suggested skills | `to-prd` first; `to-adr` / `ascii` only if warranted |
| Settled decisions | Link grilled decisions / CONTEXT terms |
