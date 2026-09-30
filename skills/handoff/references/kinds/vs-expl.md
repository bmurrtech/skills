# Kind: `vs-expl`

Delta only — apply on top of [handoff-base.md](../handoff-base.md).

## When

Next session should run **`visual-explainer`** (diagram, slides, plan review,
etc.).

## Extra / specialize

### Kind block — visual-explainer

```markdown
## Kind: visual-explainer (vs-expl)
- **Mode:** `<diagram | visual-plan | slides | diff-review | plan-review | project-recap | fact-check | …>`
- **Output dir:** `.scratch/diagrams/`
- **Companion .md:** `<yes | no | ask>`
- **Subject / paths:** `<what to visualize>`
```

## Base fill rules

| Base section | Rule |
|--------------|------|
| Next action | Skill = `visual-explainer` (+ mode) |
| Suggested skills | `visual-explainer` first |
| Evidence / artifacts | Link plans/diffs/ADRs to visualize |
