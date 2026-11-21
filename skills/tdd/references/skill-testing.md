# Testing Agent Skills

Read when the seam under test is a **skill** (`skills/<name>/`), not application
code. Pair with layout/frontmatter bars in **`writing-for-agents`**
`references/mechanics.md` and with `scripts/quick_validate.py` when present.

## Rigor levels

Match rigor to visibility and blast radius (internal team skill ≠ widely
deployed skill):

| Level | What | When |
|-------|------|------|
| **Manual** | Run real user queries in the chat/agent UI; watch trigger + behavior | Fast iteration; no harness |
| **Scripted** | Repeatable prompt suites in an agent CLI / automation loop | Regressions across edits |
| **Programmatic** | Eval harness / API against fixed cases + scored checks | Systematic coverage; ship gates |

Start at the cheapest level that fails when the skill is wrong; escalate when
the skill is user-visible or high-blast-radius.

## Pro tip: one hard task first

Iterate on a **single challenging task** until the agent succeeds, then extract
the winning approach into the skill. That uses in-context learning and gives
faster signal than broad suites. After the foundation works, expand to multiple
cases for coverage.

This mirrors vertical slices for code: one failing scenario → minimal skill
change → repeat — not “write every trigger case then hope.”

## Three test areas

### 1. Triggering

**Goal:** skill loads at the right times (description as context pointer).

| Expect | Cases |
|--------|--------|
| pass | Obvious tasks for the skill |
| pass | Paraphrased requests (same intent, different words) |
| fail | Unrelated topics |

Example suite shape:

```text
Should trigger:
- "Help me set up a new ProjectHub workspace"
- "I need to create a project in ProjectHub"
- "Initialize a ProjectHub project for Q4 planning"

Should NOT trigger:
- "What's the weather in San Francisco?"
- "Help me write Python code"
- "Create a spreadsheet"   # unless this skill owns sheets
```

Record pass/fail per phrase. Under/over-trigger → fix **description** first
(see Iteration signals below).

### 2. Functional

**Goal:** correct outputs once the skill is loaded.

Cover:

- Valid outputs for the happy path
- Tool/MCP/API calls succeed with expected side effects
- Error handling (bad input, missing auth, empty sets)
- Edge cases agreed at the seam

Example:

```text
Test: Create project with 5 tasks
Given: Project name "Q4 Planning", 5 task descriptions
When: Skill executes workflow
Then:
  - Project created
  - 5 tasks with correct properties
  - Tasks linked to project
  - No API errors
```

Prefer observable outcomes (files, API state, returned paths) over “model
sounded confident.”

### 3. Performance comparison

**Goal:** skill beats baseline on success criteria you named up front.

Example comparison shape:

| Metric | Without skill | With skill |
|--------|---------------|------------|
| Clarifying / back-and-forth | many turns of re-stated instructions | few clarifying questions |
| Failed tool calls needing retry | several | zero (or far fewer) |
| Tokens / wall time | high | lower for same outcome |
| User corrections | frequent | rare |

Define the metrics before comparing. A skill that “works” but costs more
attention or retries than bare prompting is not done.

## Iteration signals

Skills are living documents. Plan to re-test after description or body edits.

| Signal | Meaning | Fix |
|--------|---------|-----|
| **Undertriggering** — never loads; users force-enable; “when do I use this?” | Description too vague / missing keywords | Add nuance, user phrases, technical terms people say |
| **Overtriggering** — loads on irrelevant queries; users disable; purpose confused | Description too broad | Narrow scope; add **negative** triggers (“Do NOT use for …”) |
| **Execution issues** — inconsistent results; tool failures; user corrections | Body / refs weak | Sharpen steps, add error handling, disclose deep refs, consider a validation script |

After each fix: re-run the **triggering** suite (cheap) then the **functional**
cases that failed.

## Session indexing (this library)

When testing skills in **bmurrtech/skills** (or a consumer with the same
conventions):

1. Agree the skill seam (which skill folder + which scenarios).
2. Keep prompt suites and expected outcomes under `.scratch/` while exploring;
   promote durable cases into an OKF **test-map** + AGENTS Test-index line when
   they become regressions you will re-run.
3. Always run `python3 scripts/quick_validate.py skills/<name>` as a structural
   red/green before behavioral suites (layout + frontmatter).

Structural validate ≠ triggering/functional proof — both earn their keep.
