# Writing levers

Read when authoring or editing any agent-consumed document. Preserve these named
concepts; do not flatten them into unnamed checklist vibes.

## Context pointers

A **context pointer** is a reference held in the agent's context that names
out-of-context material and encodes when to reach it. A skill `description` is
one; so is any always-loaded instruction line that names a doc to open on a
condition. The pointer's *wording*, not its target, decides reach reliability.
A must-have target behind a weak pointer is a **variance bug**: sharpen wording
first; inline only if sharpening fails.

A pointer does two jobs: state what the material is, and list the **branches**
that should trigger reaching it (distinct cases → different paths). Always-loaded
pointers earn harder pruning than the body:

- **Front-load the leading word** — where triggering work happens.
- **One trigger per branch.** Synonyms renaming one branch are duplication;
  keep only genuinely distinct branches.
- **Cut identity the body already carries.**

## The two loads

Every document and pointer spends one of two budgets:

- **Context load** — always-loaded material on the agent's window (skill
  description, always-on instructions, anything present every turn) spending
  tokens and attention whether or not it fires.
- **Cognitive load** — cost on the human: which documents exist and when to
  reach for each. The human is the index. Not a cost to minimise: price of
  human agency; spend where judgement matters, remove where it does not.

Material reached only through a pointer escapes context load at the price of
the pointer's own line; material with no pointer rides entirely on cognitive load.

## Information hierarchy

Two content types: **steps** (ordered actions) and **reference** (definitions,
rules, facts on demand). Mix freely: all steps, all reference (this skill), or
both. Place each piece on the **information hierarchy**:

1. **In-file step** — primary: what the agent does, in order.
2. **In-file reference** — on demand. A flat peer-set (every review rule on one
   rung) is fine, not a smell.
3. **Disclosed reference** — separate file behind a pointer; loaded when the
   pointer fires. Spans sibling files through fully external docs any document
   can point at.

Push too little → top bloats; push too much → hide needed material. That tension
*is* the decision.

**Progressive disclosure** moves down the ladder so the top stays legible. Not
primarily a token optimisation — it protects hierarchy. Branching is the cleanest
test: inline what every branch needs; disclose what only some branches reach.
When a document has steps, in-file reference that should be disclosed buries
them and turns attending into a coin-flip: a **variance** lever, not just
legibility.

**Co-location** is the within-file companion: ladder decides *how far down*;
co-location decides *what sits beside it*. Keep a concept's definition, rules,
and caveats under one heading. Grouped material reads like docs for the agent;
scattered does not. (Distinct from **duplication**: one meaning in two places vs
one meaning fragmented across many.)

**Sprawl** is length failure even when every line is live. Cure via the ladder:
disclose reference; split by branch or sequence so each path carries only what
it needs.

## Steps and completion criteria

Every step ends on a **completion criterion** (done vs not-done). Two properties:

- **Clarity** — can the agent tell done from not-done? Vague bounds
  ("understanding reached") invite **premature completion**. Visible
  **post-completion steps** supply the pull; criterion clarity is the
  resistance. Defend: **sharpen the bound first**; only if irreducibly fuzzy
  *and* you observe the rush, hide later steps by splitting. Hiding works only
  across a real context boundary (handoff or subagent); an inline call leaves
  later steps in context.
- **Demand** — how much it requires. "Every modified model accounted for" forces
  more than "produce a change list." Demand drives **legwork** (digging latent
  in wording, not a separate step). Not step-bound: "every rule applied" binds
  flat reference just as "every step done" binds a sequence — how an
  all-reference document still carries an exhaustiveness bar.

Strongest criteria are both checkable and exhaustive.

## When to split

Splitting spends one of the two loads — cut only when it earns:

- **By sequence** — when post-completion steps tempt rushing the current one.
  Keeping later steps out of view drives legwork. Reverse: merging exposes later
  steps and invites premature completion.
- **By invocation** (skills) — see [mechanics.md](mechanics.md).

## Leading words

A **leading word** is a compact pretrained concept the agent thinks with while
running the document (*lesson*, *fog of war*, *tracer bullets*). Repeat as a
token, never as a sentence — accumulates a distributed definition and recruits
priors. Coin your own only with a clear definition; made-up words recruit no
priors (you pay definition tokens). Prefer an existing word first.

Anchors twice: in the body, *execution* (same behaviour each appearance; in flat
reference, a class to look for); in a pointer, *invocation* (shared language
across prompts/docs/code → more reliable reach).

Hunt restatements that collapse to one token:

- "fast, deterministic, low-overhead" → *tight*
- "a loop you believe in" → *red* (binary observable: goes *red* or it doesn't)

## Negative imperatives (guardrails)

**Negative imperatives** name behaviour to avoid — the antithesis of user intent.
They are a design lever, not a style smell. Soft preference steering still prefers
the **positive** (*write one-line comments*); soft bans (*don't be verbose*) drag
the forbidden act into context and half-read as invitations (*don't think of an
elephant*). Hard **guardrails** are different: irreversible, security-sensitive,
or scope-breaking acts the agent must not invent around. State them as blunt
*Do not* / *Never* lines, co-located under a **Boundaries** (or equivalent)
heading so the avoid-set is one place to scan.

Earn each line: it must block a real failure mode the positive steps do not
already make impossible. Prefer pairing — positive workflow says what to do;
Boundaries say what must not happen even if the happy path is tempting.

Shape:

```markdown
## Boundaries

- Do not modify unrelated files or widen scope beyond the request.
- Do not add dependencies without asking.
- Never commit secrets, API keys, or .env files.
- If a command fails, report the failure. Do not guess or
  present assumptions as confirmed results.
```

Omit Boundaries when the skill has no hard avoid-set. Do not bury guardrails
inside long prose or dilute them into soft “prefer not to” hedges.

## Pruning

- **Single source of truth** — one authoritative place per meaning. **Duplication**
  costs maintenance and tokens and inflates ladder rank. (Inverse of a leading
  word: that repeats a *token* on purpose, never the meaning.)
- **Environment as SoT** — `package.json` scripts, config, layout, `--help`. A
  document that restates them is a **cache**: earn the load only when lookup is
  expensive. Cache unwritten convention, rationale, gotchas. Leave one-file /
  one-command lookups to the environment.
- **Relevance** — does the line still bear on what the document does? Fail by
  never bearing (exposition / undisclosed branch) or by going stale. Without
  pruning, fate is **sediment**: stale layers because adding feels safe and
  removing feels risky.
- **No-ops** — instructions the model already obeys by default. Test is
  model-relative (does it change behaviour vs default?), settled by running the
  document. Fail → delete the whole sentence. Weak leading words (*be thorough*
  when already thorough-ish) are no-ops; fix with a stronger word (*relentless*),
  not a different technique.
