---
name: grill-me
description: >
  Relentless design-tree interview until shared understanding; when glossary/OKF
  skills and files exist, update them on the fly and offer to-adr when warranted;
  after the frontier empties, route A/B/C (to-prd / handoff→implement / bare Go).
  Use when stress-testing a plan, grilling a design, or before implementing ambiguous work.
disable-model-invocation: true
---

# grill-me

Interview until the design tree is empty. Map decisions as a tree; work **frontier rounds** only. On settled terms and warranted decisions, update docs via **`context`** / **`to-adr`** **when those skills are available and the target files exist**. Do not implement until the user picks a post-grill route (A/B/C).

## Design tree

Every decision branches into the decisions that hang off it. The **frontier** is every decision whose prerequisites are already settled — ask those now, nothing else.

## Rounds

1. Ask the **whole current frontier** in one round.
2. Wait for answers.
3. Apply **rec-default**: if the reply is only affirmatives (“yes”, “agreed”, “LGTM”, “ship it”, …), treat **every** ➡️ recommendation in that round as accepted. If the reply answers some questions and is silent on others, accept the unanswered recommendations unless the user contradicts them. Do not re-ask unanswered questions.
4. Settled decisions push the frontier outward; recompute; ask the next round.
5. A question that depends on another question still open in this round belongs to a **later** round.

Finding **facts** is your job (filesystem, tools, sub-agents) — never the user's. A running exploration is an unsettled prerequisite: ask the rest of the frontier now; only downstream questions wait. **Decisions** are the user's — put each to them and wait.

**Done when:** frontier empty; nothing silently assumed. Then present the **next-steps** A/B/C prompt (not a separate confirm beat).

## Question format

```
❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>

---

❓ **Q2** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>
```

Number questions per round. Always give your recommended answer.

## Boundaries

- Do not re-ask a round’s unanswered questions after **rec-default** applies.
- Do not invent answers the user contradicted; contradictions override **rec-default**.

## Docs (if applicable)

If **`context`** is installed and `CONTEXT.md` / `knowledge/` exist (or the user follows that convention): as terms resolve, run **`context`** immediately — do not batch. Otherwise skip with a one-line note.

When a settled choice passes the ADR warrant (costly to reverse · real alternatives · future “why?”) and **`to-adr`** is available: ask once to create via **`to-adr`**. Yes → follow `to-adr` then cite. No → continue; optional todo. If authoring would muddy the grill thread, suggest **`handoff`** first.

Do **not** auto-author PRDs during rounds — that is post-grill **A** (`to-prd`).

## Completion bar

Frontier empty → prompt A/B/C per [references/next-steps.md](references/next-steps.md). Choosing a route affirms shared understanding. Recommend **A**. Glossary/OKF updated when applicable; warranted ADRs created or explicitly deferred.
