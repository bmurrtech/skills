---
name: code-review
description: >
  Two-axis review (Standards vs Spec) of a diff against a fixed point, with
  severity and ship recommendation. Use when reviewing a branch, PR, or local
  changes.
disable-model-invocation: true
---

# code-review

Review `git diff <fixed-point>...HEAD` on two axes in **parallel** (separate sub-agents). Do not merge or rerank findings across axes. Keep using tools until findings are evidence-backed (diff hunks, file reads, targeted checks).

## 1. Pin the fixed point

User supplies commit/branch/tag/`main`/etc. If missing → ask.

Confirm: `git rev-parse <fixed-point>` works and the three-dot diff is non-empty. Fail here if not.

Also note: `git log <fixed-point>..HEAD --oneline`.

Working-tree-only / no history: review `git diff` (or the file set) against the Spec the user named; note “no fixed point.”

## 2. Spec source

In order:

1. Issue refs in commit messages (fetch via project issue-tracker workflow if present)
2. Path the user passed
3. Spec under `docs/`, `specs/`, `.scratch/`, or `docs/prd/` matching branch/feature — **if present**
4. Ask. None → Spec axis reports “no spec available” (skip Spec sub-agent)

## 3. Standards sources

Whatever the **target** repo documents: `AGENTS.md`, `CODING_STANDARDS.md`, `CONTRIBUTING.md`, `CONTEXT.md`, `docs/adr/` — **if present**.

Always include the **smell baseline** (judgement; repo docs override):

Mysterious Name · Duplicated Code · Feature Envy · Data Clumps · Primitive Obsession · Repeated Switches · Shotgun Surgery · Divergent Change · Speculative Generality · Message Chains · Middle Man · Refused Bequest

For code/config diffs, also apply [references/checklist.md](references/checklist.md) and [references/deslop-lens.md](references/deslop-lens.md). Skip anything tooling already enforces.

## 4. Parallel sub-agents

**Standards** — diff + commit list + standards paths + smell baseline + checklist/deslop refs. Each finding: severity (`CRITICAL`/`HIGH`/`MEDIUM`/`LOW`), `file:line` or hunk, one-line fix. Under 400 words.

**Spec** — diff + commit list + spec path/contents. Report missing/partial requirements, scope creep, wrong implementations; quote spec lines; severity + location. Under 400 words.

## 5. Aggregate

Present `## Standards` and `## Spec` separately. Then:

- Counts per axis by severity
- Worst issue on each axis (one line)
- **Recommendation:** `APPROVE` (no CRITICAL/HIGH) · `REQUEST CHANGES` (any CRITICAL/HIGH) · `COMMENT` (MEDIUM/LOW only)

Offer a fix/deslop pass only if the user asks — do not auto-rewrite.

## 6. Housekeeping (if applicable)

If **`upkeep`** / **`context`** are installed **and** target artifacts exist: run **`upkeep`** then **`context`**. Otherwise skip with a one-line note.

**Done when:** both axes reported (or Spec skipped), recommendation stated, housekeeping applied or skipped.
