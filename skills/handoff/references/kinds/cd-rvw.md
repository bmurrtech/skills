# Kind: `cd-rvw`

Delta only — apply on top of [handoff-base.md](../handoff-base.md).

## When

Next session should **`code-review`**, or continue from a review verdict (fix
pass). Must stand alone without the source transcript.

## Extra / specialize

### Kind block — code-review

```markdown
## Kind: code-review (cd-rvw)
- **Fixed point:** `<commit SHA | none — review working tree / staged>`
- **Spec path(s):** `<plan / PRD / constraint note>`
- **Diff scope:** `<staged | unstaged | branch…>`
- **Staged set notes:** `<what is staged; what left out on purpose>`
- **Verdict to carry:** `<APPROVE | REQUEST CHANGES | COMMENT | none yet>`
- **Worst issue (if any):** `<one line>`
- **Commit allowed after:** `<no until asked | yes>`
```

## Base fill rules

| Base section | Rule |
|--------------|------|
| Next action | `code-review` or “apply review fixes”; commit default **no** unless user said yes |
| Acceptance / constraints | Include hard constraints that must not regress |
| Suggested skills | `code-review` (or `implement` for fix pass) first |
| Open frontier | Omit chat-only “read the review from this thread” — put verdict inline |
