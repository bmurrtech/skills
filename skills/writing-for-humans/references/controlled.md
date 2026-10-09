# Controlled technical English

Read when the user asks for **strict** STE, controlled English, ASD-STE100-style
writing, or maximum procedural clarity. This file is **this skill’s** variant —
inspired by simplified technical English practice, not the official ASD-STE100
issue. Do not claim ASD-STE100 compliance.

Default Instructions mode uses [instructions.md](instructions.md) alone. This
overlay tightens that mode; it does not replace Prose for explanation or voice.

## Sentence shape

- One main idea per sentence when the idea fits.
- Treat sentence length as a **diagnostic signal**, not a hard limit. Soft /
  hard thresholds are SoT in `writing_for_humans_linter.py` (`SOFT_LIMIT` /
  `HARD_LIMIT`). Look at soft overruns when sentences pack multiple ideas;
  hard overruns are a stronger review signal. Do **not** rewrite solely to
  reduce word count.
- Prefer simple present / imperative. Avoid “should be performed,” “is to be.”
- Prefer short, concrete words. Cut filler connectors (`in order to` → `to`)
  when they add no meaning.
- Flag stacked noun clusters (`system configuration parameter value`) as an
  advisory signal — rename only when the cluster is not itself the technical
  term (LLM judgment; do not chase the metric).

Length metrics come from `scripts/writing_for_humans_linter.py` (see
[lint.md](lint.md)); do not hand-count to chase thresholds.

## Verbs and voice

- Use a small, repeated verb set: open, select, enter, set, create, run, save,
  remove, check, verify, restart, configure, compare, connect, disconnect.
- Prefer active voice with a clear actor (the reader, or a named component).
- Do not invent elegant synonyms for the same action.

## Terminology

- One approved name per thing for the whole procedure. Repeat it; do not cycle.
- Keep official product/UI/API/command strings exact even when “plain.”
- Define a term once if the reader may not know it; then reuse that form.

## Logic and structure

- Put conditions before the action they gate.
- Number steps in dependency order. One primary operation per step unless
  tightly coupled.
- State the expected result after critical steps. Describe state when exact
  output varies — do not invent output.
- Warnings before irreversible or high-impact actions.

## Limits of this variant

- Use for actionable instruction surfaces only.
- Do not force controlled shape onto essays, creative prose, or nuanced
  trade-off reasoning — keep those in Prose mode.
- If a rule here fights technical accuracy, accuracy wins; note the conflict.
