# Agent-artifacts lens (gated)

**When to read:** Standards axis only when the diff touches agent-consumed
artifacts. Path match (any hit → load this file; no hit → do not load):

- `skills/**` · `**/SKILL.md` · `**/agents/**`
- `**/skills/**/scripts/**` · `.agents/skills/**`
- Close cousins only if clearly skill/agent-instruction trees (e.g. host skill
  homes under `~/.agents/skills/` mirrored in-repo)

**When not to read:** Ordinary app/lib/docs diffs. Do not load this file “just
in case.”

This is a **scoring** lens — findings only. Do not rewrite skills unless the
user asks. Soft-skip any pointer below when the target skill/OKF is absent;
use the bullets here instead.

## Writing for agents (score)

If **`writing-for-agents`** is installed, use its levers as the bar; otherwise
score with this short set:

- **Context pointers** — descriptions/when-to-read name distinct branches; no
  dead hops
- **Hierarchy** — always-needed rules inline; branch-only detail under
  `references/` with when-to-read
- **Completion criteria** — steps have clear done/not-done bounds
- **Leading words / guardrails** — triggers front-loaded; negative imperatives
  where needed; no sprawl of always-irrelevant branches
- **Skills only** — frontmatter + invocation posture sane; run
  `quick_validate.py` on touched skill folders when that script exists

## Skill scripts vs LLM (score)

If [knowledge/skill-scripts.md](../../../knowledge/skill-scripts.md) (or
equivalent) exists, use it. Else score with:

- **LLM** for judgment (meaning, tradeoffs, ambiguous calls)
- **Script** only when exactness, repetition, or compression beats tool/token
  cost — not for pseudo-semantic “smart” regex
- **Hybrid OK** — LLM bands/labels → script formula/sort → LLM interprets small
  evidence
- Flag new scripts that are trivial one-step work, or that dump huge
  intermediates into context without a compression win

## Findings shape

Same as Standards: severity, `file:line` or hunk, one-line fix. Prefer
`MEDIUM`/`LOW` for prose/hierarchy debt; `HIGH` when a pointer or script
failure would mis-route agents or silently skip real checks.
