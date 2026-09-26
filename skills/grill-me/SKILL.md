---
name: grill-me
description: >
  Relentless design-tree interview until shared understanding; when glossary/OKF
  skills and files exist, update them on the fly and offer to-adr when warranted.
  Use when stress-testing a plan, grilling a design, or before implementing ambiguous work.
disable-model-invocation: true
---

# grill-me

Interview until the design tree is empty. Map decisions as a tree; work **frontier rounds** only. On settled terms and warranted decisions, update docs via **`context`** / **`to-adr`** **when those skills are available and the target files exist**. Do not implement until the user confirms shared understanding.

## Design tree

Every decision branches into the decisions that hang off it. The **frontier** is every decision whose prerequisites are already settled — ask those now, nothing else.

## Rounds

1. Ask the **whole current frontier** in one round.
2. Wait for answers.
3. Settled decisions push the frontier outward; recompute; ask the next round.
4. A question that depends on another question still open in this round belongs to a **later** round.

Finding **facts** is your job (filesystem, tools, sub-agents) — never the user's. A running exploration is an unsettled prerequisite: ask the rest of the frontier now; only downstream questions wait. **Decisions** are the user's — put each to them and wait.

**Done when:** frontier empty; nothing silently assumed. Then stop and await explicit confirmation before acting.

## Question format

```
❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>

---

❓ **Q2** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>
```

Number questions per round. Always give your recommended answer.

## Docs (if applicable)

If **`context`** is installed and `CONTEXT.md` / `knowledge/` exist (or the user follows that convention): as terms resolve, run **`context`** immediately — do not batch. Otherwise skip with a one-line note.

When a settled choice passes the ADR warrant (costly to reverse · real alternatives · future “why?”) and **`to-adr`** is available: ask once to create via **`to-adr`**. Yes → follow `to-adr` then cite. No → continue; optional todo. If authoring would muddy the grill thread, suggest **`handoff`** first.

Do **not** auto-author PRDs; that is **`to-prd`** after the grill when the user asks.

## Completion bar

Shared understanding confirmed by the user; glossary/OKF updated when applicable; warranted ADRs created or explicitly deferred.
