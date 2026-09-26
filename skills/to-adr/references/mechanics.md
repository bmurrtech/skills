# ADR mechanics

Read when authoring or superseding an ADR body. Process (warrant, classify,
number, index, visualize) stays in `SKILL.md`. Heading names in the template
below are SoT for new files.

Spine is **MADR-compatible** (Status → problem → drivers → options → outcome →
pros/cons). Extras below are placement and anti-bloat rules — not a standing
architecture handbook.

## Placement (ADR vs supportive docs)

| Put here | Not here — put / cite instead |
|----------|-------------------------------|
| Why this option won; rejected options | Feature scope, journeys, MVP phases → **PRD** |
| Assumptions / constraints **entailed by this decision** | Standing “how we work” → consumer **AGENTS.md** (or equivalent ops manual) |
| Implementation Notes = norms that exist **because** of the Decision Outcome | Glossary terms → consumer **CONTEXT.md** / `knowledge/` when those exist |
| Paths under **References** (cite, don’t paste) | Restating ops/glossary text already linked |

One costly decision per file. If a draft wants stack **and** security **and**
deploy as separate costly choices, split warrants or pick the primary one.

**Baselines** (security, quality gates, deploy posture) get their **own** ADR
only when that baseline *is* the decision. Otherwise link an existing ADR or
ops doc — do not paste a checklist into every ADR.

## Contain / do not contain

**ADRs contain:** the why; alternatives and why not; assumptions/constraints that
bind later work; short normative Implementation Notes; consequences (and optional
risks→mitigations / follow-ups that are acceptance aftermath).

**ADRs do not contain:** feature requirements or user journeys; MVP/sprint plans;
PRD bug logs; step-by-step implementation guides; copy of AGENTS/CONTEXT/knowledge.

## Template (headings SoT)

```markdown
# {short title}

<!-- File: docs/adr/NNNN-ADR-<slug>.md -->

## Status
[Proposed | Accepted | Deprecated | Superseded]
- **Date (optional):** [YYYY-MM-DD]
- **Supersedes:** [older](NNNN-ADR-older.md)   <!-- only when this outcome replaces that decision -->
- **Superseded by:** [newer](NNNN-ADR-newer.md)
- **Related ADRs:** [peer](NNNN-ADR-peer.md)   <!-- preserves/extends; never a substitute for Supersedes -->
- **Related PRDs:** —   <!-- optional; link when a PRD home exists -->

## Context and Problem Statement
{Problem in two or three sentences, optionally as a question.}

## Decision Drivers
* {driver}

## Considered Options
* {option 1}
* {option 2}

## Decision Outcome
Chosen option: "{option}", because {justification}.

### Consequences
* Good, because {…}
* Bad, because {…}

### Confirmation
{How we will know the decision holds.}

## Pros and Cons of the Options

### {option 1}
* Good, because {…}
* Bad, because {…}
* Why not chosen: {…}   <!-- optional but preferred on rejected options -->

### {option 2}
* Good, because {…}
* Bad, because {…}

## Assumptions
- {assumption}

## Constraints
- {constraint}

## Implementation Notes (Normative)
{Only repo/system rules *entailed by this Decision Outcome*. Later work cites
these — does not duplicate them. Omit the section if nothing normative remains.}

## References
- {path or ADR/ops/glossary link — prefer cite over paste}
```

## Optional cues (not required headings)

- **Risks → mitigations** under Consequences when material to the choice.
- **Follow-ups** only for acceptance aftermath (cleanup, sunset) — never sprint
  tracking.
- **Why not chosen** on rejected options when Pros/Cons alone leave the reject
  reason unclear.

## Implementation Notes anti-bloat

Include a bullet only if a future agent should **obey or cite** it because of
*this* outcome. Forbidden as default subsections: standing Security / Quality /
Ops / Versioning checklists unless that topic *is* the decision.
