# Discovery records tracking choice

Read during **Present and confirm** and **Write** when applying or flipping
`docs/discovery/` track-vs-ignore policy. Pattern mirrors
[prd-tracking.md](prd-tracking.md) / [ADR 0013](../../../docs/adr/0013-ADR-prd-tracking-choice.md)
(no separate ADR yet).

Bundles under `docs/discovery/` may hold personal and client-confidential data:
names, emails, titles/roles, client business details, pain points, stakeholder
sentiment, tech stack/systems, and similar evidence-derived fields.

## Prompt shape

Always re-ask on every setup run (idempotent flip path). Show **detected**
policy first, then:

```text
**Detected:** docs/discovery/ is <ignored | tracked | unset | conflict>

**Commit discovery records?** (setup policy A/B — not grill-me next-step A/B/C)
Team OKF under docs/discovery/<team>/ can include names, emails, titles/roles,
client business details, pain points, stakeholder sentiment, tech stack/systems,
and other client-confidential data.

**A)** Keep `docs/discovery/` **ignored** (gitignored) — default; keeps PII/client
    data out of VCS unless you opt in
**B)** **Track** `docs/discovery/` — shareable for teammates + remote agents.
    Prefer a **private** repo (never public). Unsure? See
    https://github.com/bmurrtech/skills/blob/main/docs/how-to-discovery.md
    (Personal data) and
    https://github.com/bmurrtech/skills/blob/main/docs/how-to-bmurrtech-skills.md
    (Discovery records).

➡️ **A** (default; no reply / LGTM / affirmatives → A)
```

If Explore found **conflict**: state both facts; recommend resolve (remove ignore
**or** untrack) before applying; still accept A or B as the target policy.

## Detect (Explore)

Let `ignore` = `.gitignore` has a `docs/discovery` ignore line (`/docs/discovery/`,
`docs/discovery/`, `docs/discovery/**`, or equivalent). Treat `/docs/discovery/`
and `docs/discovery/` as the same surface.

Let `tracked_files` = `git ls-files docs/discovery` is non-empty.

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
| `.gitignore` | Presence/absence of `docs/discovery` ignore lines |
| `AGENTS.md` | Overview / structure / Git & PR bullets that state discovery policy |
| `CONTEXT.md` | Short discovery policy pointer — **only** when creating the stub **or** user confirmed editing an existing file |
| `CLAUDE.md` | If AGENTS body changed and CLAUDE is the pointer → refresh |

Do **not** invent a policy marker file. Do **not** create library how-tos in the consumer.

## Write matrix

### A — ignore

1. **`.gitignore`:** ensure a distinct `/docs/discovery/` entry (append if missing). Prefer append over rewrite. Contiguous comment optional, e.g. “Discovery OKF — default ignored (setup A); track via setup B.”
2. **`AGENTS.md`:** set policy lines to local/ignored:
   - Overview: discovery records under gitignored `docs/discovery/`
   - Structure: `docs/discovery/` — discovery OKF (ignored)
   - Git & PR: include `docs/discovery/` among ignored trees in the never-commit-secrets bullet; **remove** any “tracked by setup choice” discovery bullet
3. **`CONTEXT.md`:** if stub create or edit allowed — one hard-rule / gloss line: discovery records ignored (ADRs tracked); cite setup / how-tos, do not duplicate AGENTS bullets.
4. Report: policy **A**. If flipping from tracked files still in the index, warn: ignore applies going forward; offer `git rm -r --cached docs/discovery` **only after explicit confirm** (do not run unprompted).

### B — track (commit)

1. **`.gitignore`:** remove only `docs/discovery` ignore lines this skill owns (`/docs/discovery/`, `docs/discovery/`, `/docs/discovery/*`, `docs/discovery/**`, and a contiguous comment line that documents `docs/discovery` ignore/track policy). Leave all other ignores untouched.
2. **`AGENTS.md`:** set policy lines to tracked:
   - Overview: discovery records under `docs/discovery/` (tracked)
   - Structure: `docs/discovery/` — discovery OKF (tracked)
   - Git & PR: **omit** `docs/discovery/` from ignored trees; add:
     - `` `docs/discovery/` **is tracked by setup choice** (not in `.gitignore`) — keep the repo **private**; see how-to-discovery Personal data. ``
3. **`CONTEXT.md`:** if stub create or edit allowed — one hard-rule / gloss line: discovery tracked by setup choice; private-repo recommend; cite setup/how-tos.
4. Report: policy **B**; remind private-repo; next **`commit`** can add `docs/discovery/` files.

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
… discovery records under gitignored `docs/discovery/` (setup **A**) …

<!-- Structure -->
- `docs/discovery/` — discovery OKF (ignored)
```

### A — Git & PR (secrets line)

```markdown
- Never commit secrets or ignored trees (`pm/`, `docs/prd/`, `docs/discovery/`, `.scratch/`, agent dirs, `.env`).
```

(Include `docs/prd/` only when PRD policy is also **A**; omit it when PRD is **B**.)

### B — Overview / Structure

```markdown
<!-- Overview (adapt to surrounding sentence) -->
… discovery records under `docs/discovery/` (tracked; setup **B**; keep repo private) …

<!-- Structure -->
- `docs/discovery/` — discovery OKF (tracked)
```

### B — Git & PR

```markdown
- Never commit secrets or ignored trees (`pm/`, …, `.scratch/`, agent dirs, `.env`).
- `docs/discovery/` **is tracked by setup choice** (not in `.gitignore`) — keep the repo **private**; Personal data: how-to-discovery.
```

(Omit `docs/discovery/` from the ignored-trees list; keep `docs/prd/` in that list only when PRD policy is **A**.)

## Boundaries

- Do **not** default to B on silence — silence / LGTM / bare affirmatives → **A**.
- Do **not** `git rm --cached` without explicit confirm.
- Do **not** invent a discovery policy marker file.
- Do **not** let **`upkeep`** “heal” B by re-adding `/docs/discovery/` — upkeep has no gitignore discovery mandate.
- On **B**, always surface the private-repo recommendation and the two how-to links from the prompt.
