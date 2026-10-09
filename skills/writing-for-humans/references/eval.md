# Eval

Read before returning substantial Generate/Edit output, or after Detect.
Answer pass/fail; fix fails; re-check. Waive only with a stated reason.

## Global

1. Solves the actual ask?
2. Facts and technical identifiers preserved / not invented?
3. Assumptions labeled; material caveats kept?
4. Unsupported claims removed or sourced?
5. Audience-appropriate?

## Instructions (and Mixed actionable sections)

1. Each action explicit with a clear target?
2. Prerequisites and dependency order correct?
3. Conditions/branches explicit where needed?
4. Exact commands/labels preserved; placeholders explained?
5. Destructive effects warned before the step?
6. Verification proportionate; recovery when useful?
7. Decision tree used when symptoms diverge?
8. If controlled overlay loaded: short sentences, fixed verbs, one name per
   thing — without claiming official ASD-STE100 compliance?

## Prose (and Mixed explanatory sections)

1. Point clear; filler gone without stripping voice/nuance?
2. Claims concrete and supported by the draft?
3. Banned words / slop patterns cleared (or kept as real voice)?
4. Writer would recognize their voice (Edit)?
5. Detect-only: pattern + quote + short fix; no rewrite/score?

## Proportionality

Did the change fix a real problem, or only make the text more uniform?
Uniformity alone is not a pass. Did any rewrite exist only to hit a word-count
threshold? That fails.

## Lint budget (Generate/Edit)

1. Was the linter run and its JSON read (not re-counted by hand)?
2. Was `revision_budget` honored (0 accept / at most 1 material revision)?
3. If re-linted once, did work stop afterward unless a new substantive defect
   appeared?

## Smoke cases (self-check)

| Case | Pass signal |
|------|-------------|
| Simple UI procedure | Exact labels; direct actions; order; light verify |
| Destructive command | Warn; separate inspect vs delete; no invented state |
| Complex troubleshooting | Hypotheses labeled; branches; no fake root cause |
| Verbose technical prose | Cut filler; keep distinctions/caveats/reasoning |
| Creative / voice draft | No instruction-flattening; personality kept |
| Strict / STE-style ask | [controlled.md](controlled.md) applied; no false ASD-STE100 claim |
