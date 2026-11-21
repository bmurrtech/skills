# Optional sections

Read when the transcript has timestamps, the user asks for a TOC/chapters,
quotable lines earn a place, proposals / questions / desired outcomes draw a
*stance*, material decisions/actions/open questions appear, or *focus* asks for
evidence-linked / meeting-shaped output. Omit headings when empty — never pad.

## Stance on probes

Add `### Stance on probes` when the user named propositions to watch, or the
room clearly voiced a proposal, question, or desirable outcome and someone
took a position on it. Not valence mood (pos/neg/neutral). Not discovery
quadrant *Sentiment* (commitment score) — hand that to `/discovery` only if
the user asks after this summary.

**Substance labels** (pick one per probe):

| Label | Means |
|-------|--------|
| **Endorse** | Clear support for the proposition as framed |
| **Conditional** | Yes if named conditions hold |
| **Polite-interest** | Soft yes / "would be nice" without real buy-in |
| **Reframe** | Rejects or sidesteps the premise; names a different real issue |
| **Reject** | Clear no |
| **Defer** | Not now; time or dependency named |
| **Unclear** | Position too thin to call |

Surface vs substance: record both when they diverge (e.g. surface
Polite-interest, substance Reframe). Never score polite-interest as Endorse.

Table (or equivalent bullets):

```text
| Probe | Surface | Substance | Reframe / condition | Evidence | Conf |
| Would X solve Y? | Polite-interest | Reframe | Real issue is Z | "…nice, but… Z" — Speaker | H |
```

Rules:

- Probe = question, proposal, solution, or desired outcome as stated
- Evidence = short quote + speaker (+ timestamp if present); no invention
- Conf = H / M / L from how explicit the room was
- Prefer missing a row over inventing a probe the room did not voice
- User-named probes with no hit → one row: Substance **Unclear**, evidence "not addressed"
- Soft-yes + "real issue is Z" stays one paired row — do not collapse to "mixed"

**Done when:** every user-named or clearly voiced probe has a row; divergences
and reframes are explicit.

## Decisions

Add `### Decisions` when the transcript records commitments or conclusions the
room reached (not mere discussion). Prefer final wording when a decision
changed mid-transcript; note conditions and dissent when they matter.

For each decision:

- Decision statement (plain language)
- Who decided / affirmed, if identifiable
- Conditions or limits, if stated
- Evidence: short quote + speaker (+ timestamp when present)
- Confidence H / M / L from how explicit the room was

Do not upgrade "we talked about X" into a decision. Prefer missing a row over
invention.

**Done when:** every clear decision has a row; superseded early wording is not
presented as final without note.

## Action items

Add `### Action items` when tasks or commitments to act appear.

For each item:

- Task
- Owner — name only when explicit; otherwise `missing`
- Due / trigger — only when explicit; otherwise `missing`
- Evidence: short quote + speaker (+ timestamp when present)

Never invent owners or deadlines.

**Done when:** every explicit action is listed; missing owner/due are marked,
not guessed.

## Open questions

Add `### Open questions` when questions were raised but not resolved, or
blockers remain unanswered.

For each:

- Question / unresolved issue
- Context (one line)
- Evidence: short quote + speaker (+ timestamp when present) when available

**Done when:** unresolved items that affect follow-up are listed; answered
questions are not duplicated here.

## Evidence (focus-steered)

Add `### Evidence` when *focus* asks for evidence-linked output, or when
material claims in Overview / takeaways need a compact citation trail beyond
per-section evidence columns.

Format (or equivalent bullets):

```text
| ID | Claim type | Claim | Speaker | Time | Quote |
| E1 | Decision | … | Dana | 00:18:42 | "…" |
```

Claim types: Decision · Action · Risk · Commitment · Approval · Fact · Other.
Every row needs a quote present in the transcript. Omit the section when empty.

**Done when:** every listed claim has a transcript-grounded quote; no unsupported
rows.

## Timestamped TOC

When the source has timestamps (`[HH:MM:SS]`, `HH:MM:SS`, or similar) or the
user asks for chapters / a table of contents, add a section such as
`### Timestamped sections` (place after Overview or before Key takeaways —
whichever reads cleaner).

Format each entry:

```text
[HH:MM:SS] Section Title — one-sentence description
```

Rules:

- Place markers at natural topic transitions, not arbitrary intervals
- Titles specific and descriptive (not "Introduction" or "Discussion")
- Note speaker changes when multiple speakers matter
- One-sentence description: what the reader gets in that span
- Apply *focus* when choosing which transitions to surface
- Do not invent timestamps; only use times present in the source

## Pull quotes

When the transcript has powerful standalone lines, add `### Pull quotes`.
Do not fold these into `### Reference insights`.

For each quote:

- Exact quote, or very close paraphrase if wording is unclear (say when
  paraphrased)
- Who said it, if identifiable
- One sentence of context (why it matters)
- Approximate timestamp when available

Prioritize surprising insights, memorable phrases, emotional or contrarian
moments. Keep each quote short (about 1–3 sentences). Apply *focus* when
ranking. Skip the section when nothing earns it.

## Reference insights (reminder)

Secondary ideas, metaphors, or observations that are not pull-quote material
and not immediately actionable stay under `### Reference insights`. Omit when
empty.
