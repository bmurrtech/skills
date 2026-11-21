# Focus

Read when the user gave emphasis, audience, depth, or intended use — or any
phrase that should steer the summary.

## Build the directive

Map optional inputs into one line. Do not request missing fields.

| User gave | Include as |
|-----------|------------|
| area of interest / topic | what to emphasize |
| preferred depth | how deep to go |
| intended use | what the summary is for |
| probes / proposals / outcomes to watch | *stance* targets in the directive |
| free-form steer | as stated |

Format:

```text
FOCUS: {one or two sentences}
```

Omit the directive entirely when the user gave no steer. Do not invent a focus.
Do not write "no specific focus."

Inject the same `FOCUS:` line into Extract, Emit, and every map/reduce pass
when long-input is active.

## Examples

```text
FOCUS: Emphasize AI and technology architecture decisions.
FOCUS: Extract actionable advice for the sponsoring team.
FOCUS: Highlight business implications and priority tradeoffs.
FOCUS: Write for a non-technical executive audience; keep jargon light.
FOCUS: Prefer depth on risks, constraints, and open questions.
FOCUS: Emphasize what matters for a discovery brief handoff later.
FOCUS: Stance on whether X solves Y; capture soft-yes and reframes to the real issue.
FOCUS: Prefer evidence-linked decisions and action items for the sponsoring team.
```

Tiny shape check — user says "focus on the data access blockers":

```text
FOCUS: Emphasize data access blockers and what they prevent.
```

Then every synthesis pass must visibly weight those blockers in the *core
summary*, themes, and takeaways without inventing blockers absent from the
transcript.

When *focus* names probes, also emit `### Stance on probes` per
[optional-sections.md](optional-sections.md) — still omit the heading if no
probe was voiced and none were user-named.

When *focus* asks for evidence-linked or meeting-shaped output, prefer the
Decisions / Action items / Open questions / Evidence sections in
[optional-sections.md](optional-sections.md).
