# Lint measure → LLM judge

Read when running quality check after a Generate/Edit draft (skip for Detect
unless the user wants metrics only).

The script **measures**. The LLM **decides**. Do not treat numeric thresholds
as rewrite orders.

## Run

Prefer the library-rooted path (works from repo root). From an installed skill
directory, the relative `scripts/` form is fine.

```bash
python3 skills/writing-for-humans/scripts/writing_for_humans_linter.py /path/to/draft.md
# or from the skill directory:
python3 scripts/writing_for_humans_linter.py /path/to/draft.md
# or:
python3 skills/writing-for-humans/scripts/writing_for_humans_linter.py --text '...'
# or stdin:
python3 skills/writing-for-humans/scripts/writing_for_humans_linter.py - < draft.md
```

Stdout is deterministic JSON. Prefer `agent_summary` for LLM consumption; open
`findings` only when you need sentence context. Do not recount words yourself.

## agent_summary

| Field | Meaning |
|-------|---------|
| `recommendation` | **STOP** (budget 0) or **REVISE_ONCE** (budget 1) |
| `revision_budget` | 0 or 1 — max lint-driven revisions allowed |
| `material_review_needed` | True when any review/critical finding exists |
| `material_kinds` | Kinds that drove materiality |
| `advisory_count` | Count of advisory findings (no forced rewrite) |
| `top_material` | Compact material signals (no full sentence dumps) |

Exit code is **0** on successful analysis even when findings exist. Nonzero only
for execution errors (missing file, bad args).

## Severity

| Level | Meaning | Typical LLM action |
|-------|---------|-------------------|
| **info** | Aggregate stats | None |
| **advisory** | Soft signal (e.g. 21-word sentence, filler, noun-cluster candidate) | Usually accept |
| **review** | Higher odds of a real problem (e.g. >30 words) | Inspect; rewrite only if material |
| **critical** | Reserved for future structural defects | Fix if present |

Word count is a **diagnostic signal**, not a definition of good writing. Soft
threshold = script `SOFT_LIMIT` (20); hard review = `HARD_LIMIT` (30). A clear
21-word sentence can stand. A short sentence with buried conditions can need
work for structure, not length.

Noun-cluster candidates are **advisory** (signal only) so false positives do
not force a revision budget.

## Revision budget

Honor `agent_summary.recommendation` / `summary.revision_budget`.

For routine writing:

- **STOP** when findings are informational or advisory-only → accept the draft.
- **REVISE_ONCE** when `material_review_needed` is true → one **targeted**
  revision addressing material issues only, then re-lint **once**, then **STOP**.
- Never run more than one lint-driven revision automatically.
- A second revision needs a **substantive new defect**, not failure to hit a
  numeric threshold.

Do not trade meaning, technical accuracy, or natural prose for marginal
metric improvement. Do not rewrite a sentence solely to reduce its word count.

## Mode notes

- **Instructions / controlled:** length, filler, indirect, passive heuristic,
  and noun-cluster signals are in-scope for judgment.
- **Prose:** prefer advisory restraint; preserve voice. Length alone rarely
  justifies a rewrite.
- **Mixed:** lint the whole draft; apply judgment per section function.

## What the script must not do

The linter must not decide “too many ideas,” rewrite text, or claim grammar
certainty. Matching and counting only. Semantic judgment stays with the LLM.
