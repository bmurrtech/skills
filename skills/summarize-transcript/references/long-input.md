# Long input

Read when `assess_size.py` hints `map-reduce`, the transcript file is huge, or
a single pass will not fit cleanly. Host LLM only — no lab/API calls.

## Assess

From the skill folder:

```text
python scripts/assess_size.py <path-or-->
```

stdin: pass `-` and pipe text. The script prints words, rough tokens, and a
strategy hint (`direct` | `map-reduce`). The hint is advisory — choose
map-reduce when one pass will not fit cleanly.

**Done when:** strategy is named (`direct` or `map-reduce`).

## Chunk (map-reduce only)

```text
python scripts/chunk_transcript.py <input> --out .scratch/summarize-transcript/<run-id>
```

Defaults: `CHUNK_WORDS=3000`, `OVERLAP_WORDS=300` (overridable via flags).
Prefers speaker-turn boundaries when speaker labels are present; otherwise
paragraph boundaries. Units longer than `chunk_words` (e.g. a single pasted
blob) are hard-split on word windows with the same overlap. Creates
`chunk_NNN.txt` under the out dir. Use a fresh run-id (date-slug or short uuid).

**Done when:** chunk files exist and the out dir path is noted.

## Map

For each `chunk_NNN.txt`, write `chunk_NNN_map.md` in the same dir.

**Extract-then-abstract:** produce atomic notes with verbatim quotes — not a
prose mini-summary. Each note should carry (when present): claim type, text,
speaker, timestamp, and a short verbatim quote.

Preserve (never drop for brevity):

- meaning, *nuance*, and detail that change decisions or understanding
- key facts, names, numbers, quotes, timestamps
- narrative / topic arc and transitions
- ideas that support future thinking, even if not immediately actionable
- anything the *focus* directive calls out
- *stance* pairs: proposal/question/outcome + surface reply + substance/reframe
  (e.g. "Would X solve Y?" → "nice, but real issue is Z") — keep as one unit
- decisions, action items, open questions (owner/due only when explicit)

Drop only: pure repetition, filler, off-topic chatter, hype.

Inject `FOCUS:` when present. Prefer missing compression over missing key
takeaways, *signal*, or reframe pairs. Do not collapse stance pairs into
"mixed sentiment."

**Done when:** every chunk has a map file of atomic notes with quotes; maps are
usable alone as section notes; any stance pairs in the chunk appear in the map.

## Reduce

Concatenate maps in order. If the combined maps still will not fit, chunk the
combined maps and map again (recurse). Otherwise synthesize into the skill's
final emit shape (Title → *core summary* → themes → implications → takeaways
→ optional sections).

Synthesize from the notes — do not concatenate and do not summarize
summaries-of-summaries. Remove overlap redundancy. Keep *nuance* and stance
reframe pairs intact (no averaging into valence mood).

**Reversals:** when the room changes position, prefer later/final wording.
Flag unresolved conflict rather than averaging or dropping the reversal.

Apply *focus* again. Final output must still pass the skill Exit check and
Boundaries.

**Done when:** one final Markdown summary exists; intermediates stay under
`.scratch/summarize-transcript/<run-id>/` unless the user asks to delete them.
