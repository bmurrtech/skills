# Requirements gathering

Use only for use cases already ranked high enough to take toward a POC or MVP,
or when the user explicitly asks to gather requirements. Recall the use case,
its rank, and any Decision that binds it. Do not re-rank unless they reopen
priority.

Ask the short list. Add a follow-up sentence only when an answer is too vague
to start a POC (for example "pretty accurate" on money, safety, or legal notice).

Short list:

1. How good is good enough? If helpful: are you okay with [the error level they implied], or is that unacceptable?
2. What constraints should we know about? (policy, procedure, security, privacy, integrations, data silos, buy-in, records)
3. Where do people have to meet the solution? Can this live outside that system? Willing to try a different interface if needed?
4. What starts it? (event, person, process step, webhook/integration, file change/upload, other)
5. What sources must a first version see?
6. What is the minimum integration without which a POC is fake?
7. What is the high-level workflow, start to finish, for the first slice?

Stop when those seven are answered or explicitly unknown. Unknown is allowed.
A guess is not.

```markdown
# Requirements — [use case title]

## Bound by

- [Decision or prior rank this conversation must respect. Drop if none.]

## Good enough

- **Bar:** [what "good" means in their words]
- **Miss:** [the error, delay, or wrong answer they will not accept]
- **Acceptable miss:** [what they will tolerate, or "none stated"]

## Constraints

- [policy / procedure / security / privacy / integration / data silo / buy-in / records / other] — [what they said]
- [drop unused rows]

## Where it has to show up

- **Place:** [site, system, screen, process, document, or inbox they already use]
- **Outside that place:** [acceptable / unacceptable / not discussed]
- **Different interface:** [willing / unwilling / not discussed]
- **Not the same as:** [a contrast they drew, or drop]

## What starts it

- **Trigger:** [event / human / process step / webhook or integration / file change or upload / other]
- **Detail:** [the actual event or action]

## Sources

- [source] — [what it is for]

## Minimum integrations for a POC

- [system or feed] — [why the POC is fake without it]

## Workflow (first slice)

1. [start]
2. [step]
3. [end state a person can recognize]

## Still blank on purpose

- **Stakeholder:**

## Too thin to build

- [Any of the seven that stayed unknown, and the one question that would close it. Drop if the seven are enough.]
```
