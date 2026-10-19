# Kind: `adr`

Delta only — apply on top of [handoff-base.md](../handoff-base.md).

## When

Mid-session **fork**: decisions in a coding/debug/grill chat warrant an ADR, but
ADR authoring would muddy this session. Capture **candidacy** here; run
**`create-adr`** in a **separate** session.

## Extra / specialize

### Kind block — ADR candidacy

```markdown
## Kind: create-adr (adr)
- **Decision statement:** `<what must be decided / was leaned>`
- **Options considered:**
  - `<option A>`
  - `<option B>`
- **Lean recommendation:** `<option>` — `<why, short>`
- **Related paths:** `<code / PRD / CONTEXT / prior ADR>`
- **Warrant cues:** costly to reverse? real alternatives? future “why?”
- **Do not:** write `docs/adr/…` from **`handoff`** — next skill is **`create-adr`**
```

## Base fill rules

| Base section | Rule |
|--------------|------|
| Next action | Skill = `create-adr`; commit/deploy usually **no** / N/A |
| Goal / position | State that coding session continues separately if still in flight |
| Suggested skills | `create-adr` first |
| Acceptance / constraints | Candidacy bullets are the payload — keep them portable |
