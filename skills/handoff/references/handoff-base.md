# Handoff base template

Read when drafting a handoff body. Fill what you know; **omit** empty sections
rather than inventing. Kind overlays add or specialize sections — they do not
replace this file.

## Template

```markdown
# <Title from aim>

## Goal / position
<Where the work stands in 2–4 sentences. No “see this chat.”>

## Next action
- **Skill / command:** `<e.g. implement | code-review | to-adr | wait>`
- **Spec / focus path:** `<path or N/A>`
- **Commit allowed:** `<yes | no | ask>`
- **Deploy allowed:** `<yes | no | ask>`

## Acceptance / constraints
- <Short bullet the next agent must satisfy or not regress>
- <…>

## Repo state
- **Branch:** `<name>`
- **Staged:** `<yes | no | partial — detail>`
- **Note:** Re-verify with `git status` (and deploy/logs if relevant) before
  editing — this section can be stale.

## Evidence / artifacts
- `<path or URL>` — <why it matters>
- `<…>`

## Settled decisions
- <path to ADR / PRD / CONTEXT term> — <one-line pointer>
- <…>

## Open frontier
- <Open question or follow-up, if any>

## Suggested skills
- <next workflow skill first>
- <housekeeping last, if needed>

## Kind block
<!-- Only when a legend kind matched. Heading MUST use Display (slug), e.g.
     ## Kind: code-review (cd-rvw) — see kind-legend.md. Never slug-only. -->
```

## Fill rules

| Section | Rule |
|---------|------|
| Next action | Required. One primary next skill/command. |
| Acceptance / constraints | Hybrid inline bullets. Prefer these over “read the whole plan.” |
| Repo state | Always include the re-verify cue when claiming status. |
| Evidence | Paths the user already produced (logs, exports, plans). |
| Suggested skills | Names only. Next workflow ≠ only `upkeep`/`context`. |
| Kind block | Omit entirely when kind is none. When present, heading = **Display (slug)** from the legend — never slug alone. |
