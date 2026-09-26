# MADR headings (SoT)

Use these headings when authoring a new ADR. Filename remains `NNNN-ADR-<slug>.md`.

```markdown
# {short title}

<!-- File: docs/adr/NNNN-ADR-<slug>.md -->

## Status
[Proposed | Accepted | Deprecated | Superseded]
- **Date (optional):** [YYYY-MM-DD]
- **Supersedes:** [older](NNNN-ADR-older.md)
- **Superseded by:** [newer](NNNN-ADR-newer.md)
- **Related PRDs:** —

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

### {option 2}
* Good, because {…}
* Bad, because {…}

## Assumptions
- {assumption}

## Constraints
- {constraint}

## Implementation Notes (Normative)
{Repo-wide rules later work should cite, not duplicate.}
```
