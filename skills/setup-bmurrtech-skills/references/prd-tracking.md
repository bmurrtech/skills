# PRD tracking choice

Read during **Present and confirm** and **Write** when applying or flipping
`docs/prd/` track-vs-ignore policy. Decision: [ADR 0013](../../../docs/adr/0013-ADR-prd-tracking-choice.md).

## Prompt shape

Always re-ask on every setup run (idempotent flip path). Show **detected**
policy first, then:

```text
**Detected:** docs/prd/ is <ignored | tracked | unset | conflict>

**Commit PRDs?** (setup policy A/B — not grill-me next-step A/B/C)
Useful for teams and/or remote AI coding so agents get PRD context from the repo.

**A)** Keep `docs/prd/` **ignored** (gitignored) — less PR noise; solo / draft-heavy
**B)** **Track** `docs/prd/` — shareable for teammates + remote agents

➡️ **A** (default; no reply / LGTM / affirmatives → A)
```

If Explore found **conflict**: state both facts; recommend resolve (remove ignore
**or** untrack) before applying; still accept A or B as the target policy.

## Detect (Explore)

Let `ignore` = `.gitignore` has a `docs/prd` ignore line (`/docs/prd/`,
`docs/prd/`, `docs/prd/**`, or equivalent). Treat `/docs/prd/` and `docs/prd/`
as the same surface.

Let `tracked_files` = `git ls-files docs/prd` is non-empty.

Classify **exactly one** (evaluate in this order):

| Order | Class | Evidence |
|-------|-------|----------|
| 1 | `conflict` | `ignore` **and** `tracked_files` |
| 2 | `ignored` | `ignore` **and not** `tracked_files` |
| 3 | `tracked` | **not** `ignore` **and** `tracked_files` |
| 4 | `unset` | **not** `ignore` **and not** `tracked_files` (greenfield / empty path) |

## Target files (only these for this choice)

| File | Role |
|------|------|
| `.gitignore` | Presence/absence of `docs/prd` ignore lines |
| `AGENTS.md` | Overview / structure / Git & PR bullets that state PRD policy |
| `CONTEXT.md` | Short PRD policy pointer — **only** when creating the stub **or** user confirmed editing an existing file |
| `CLAUDE.md` | If AGENTS body changed and CLAUDE is the pointer → refresh |

Do **not** create `docs/about-prd.md`. Do **not** invent a policy marker file.

## Write matrix

### A — ignore

1. **`.gitignore`:** ensure a distinct `/docs/prd/` entry (append if missing). Prefer append over rewrite.
2. **`AGENTS.md`:** set policy lines to local/ignored:
   - Overview: PRDs under gitignored `docs/prd/`
   - Structure: `docs/prd/` — PRDs (ignored)
   - Git & PR: include `docs/prd/` among ignored trees in the never-commit-secrets bullet; **remove** any “tracked by setup choice” bullet
3. **`CONTEXT.md`:** if stub create or edit allowed — one hard-rule / gloss line: PRDs ignored (ADRs tracked); cite setup/ADR, do not duplicate AGENTS bullets.
4. Report: policy **A**. If flipping from tracked files still in the index, warn: ignore applies going forward; offer `git rm -r --cached docs/prd` **only after explicit confirm** (do not run unprompted).

### B — track (commit)

1. **`.gitignore`:** remove only `docs/prd` ignore lines this skill owns (`/docs/prd/`, `docs/prd/`, `/docs/prd/*`, `docs/prd/**`, and a contiguous comment line that documents `docs/prd` ignore/track policy — e.g. “local PRDs”, “setup A”, “Default ignored”, dual-policy notes). Leave all other ignores untouched.
2. **`AGENTS.md`:** set policy lines to tracked:
   - Overview: PRDs under `docs/prd/` (tracked)
   - Structure: `docs/prd/` — PRDs (tracked)
   - Git & PR: **omit** `docs/prd/` from ignored trees; add:
     - `` `docs/prd/` **is tracked by setup choice** (not in `.gitignore`) so agents/teammates share PRD context. ``
3. **`CONTEXT.md`:** if stub create or edit allowed — one hard-rule / gloss line: PRDs tracked by setup choice; cite setup/ADR.
4. Report: policy **B**; next **`commit`** can add `docs/prd/` files.

### Idempotent no-op

| Chosen | Already matches when |
|--------|----------------------|
| **A** | class is `ignored` **and** AGENTS (and CONTEXT when in scope) already state ignore |
| **B** | class is `tracked` **and** AGENTS (and CONTEXT when in scope) already state track |

`unset` and `conflict` are **never** no-ops — always apply the write matrix (after conflict warning).

Skip matching surfaces; report “already A/B”.

### Patch discipline

- Prefer surgical line replace for known setup-owned bullets over rewriting whole AGENTS/CONTEXT.
- Ambiguous existing prose → show proposed diff bullets; ask once before replace.
- Never silent-overwrite unrelated sections.
- Ops detail lives in **AGENTS**; CONTEXT keeps a short pointer only (no glossary↔ops duplication).

## AGENTS bullet templates

### A — Overview / Structure

```markdown
<!-- Overview (adapt to surrounding sentence) -->
… PRDs under gitignored `docs/prd/` (setup **A**) …

<!-- Structure -->
- `docs/prd/` — PRDs (ignored)
```

### A — Git & PR (secrets line)

```markdown
- Never commit secrets or ignored trees (`pm/`, `docs/prd/`, `.scratch/`, agent dirs, `.env`).
```

### B — Overview / Structure

```markdown
<!-- Overview (adapt to surrounding sentence) -->
… PRDs under `docs/prd/` (tracked; setup **B**) …

<!-- Structure -->
- `docs/prd/` — PRDs (tracked)
```

### B — Git & PR

```markdown
- Never commit secrets or ignored trees (`pm/`, `.scratch/`, agent dirs, `.env`).
- `docs/prd/` **is tracked by setup choice** (not in `.gitignore`) so agents/teammates share PRD context.
```

## Boundaries

- Do **not** default to B on silence — silence / LGTM / bare affirmatives → **A**.
- Do **not** `git rm --cached` without explicit confirm.
- Do **not** reintroduce `docs/about-prd.md` as a setup create.
- Do **not** let **`upkeep`** “heal” B by re-adding `/docs/prd/` — upkeep has no gitignore PRD mandate.
