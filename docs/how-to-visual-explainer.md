# How to use `visual-explainer`

Complex visual or tabular intent → self-contained HTML under **`.scratch/diagrams/`**,
opened in the browser. Intent routing picks the mode.

Install and scaffold (including `.scratch/diagrams/`) are covered in
[how-to-bmurrtech-skills.md](how-to-bmurrtech-skills.md). This page is modes +
prompts — not a second install guide.

## Flow

```text
your ask ──► visual-explainer ──► .scratch/diagrams/<name>.html
                    │                      │
                    │ intent route         + - - [if asked] → <name>.md
                    v                            (AI companion; not HTML SoT)
              one mode runs
```

Prefer HTML over ASCII murals when this skill is loaded. For text-first docs
(ADRs, PRDs, README) where a pasteable diagram is enough, use **`ascii`** instead.

## Capabilities

- Architecture / flowchart / sequence / ER / state (Mermaid or CSS Grid)
- Visual implementation plans
- Magazine-style HTML slide decks
- Diff review and plan-vs-code review pages
- Project recap (mental-model snapshot)
- Fact-check of an HTML/MD doc against the codebase
- Proactive HTML for complex ASCII tables (4+ rows or 3+ columns)
- Optional **AI-readable Markdown companion** beside the HTML

## Intent → mode

| You mean… | Mode |
|-----------|------|
| Diagram / architecture / “explain visually” | Diagram |
| Visual implementation plan | Visual plan |
| Slide deck / presentation | Slides |
| Review this diff / before-after | Diff review |
| Compare plan to codebase | Plan review |
| Catch me up / mental model | Project recap |
| Verify doc against code | Fact-check |
| About to dump a big terminal table | Complex table → HTML |

If several could apply, prefer the narrower review/plan/slides mode over a
generic diagram.

## Example prompts

```text
Explain our auth flow as a diagram
Visual plan for adding SSO
Make a slide deck from docs/how-to-bmurrtech-skills.md
Review the diff on this branch as HTML
Plan-review docs/prd/0001-PRD-foo.md against the code
Project recap — I have not touched this repo in two weeks
Fact-check .scratch/diagrams/auth-flow.html
Compare these 12 requirements in a table
Also write an AI-readable Markdown companion beside the HTML
Give me a source brief .md next to the diagram for agents to re-ingest later
```

## Output

| Artifact | When |
|----------|------|
| `.scratch/diagrams/<name>.html` | Always (visual SoT); open in browser when allowed |
| `.scratch/diagrams/<name>.md` | **Only** when you ask for an AI-readable / source-brief equivalent |

The Markdown companion is **not** the source of the HTML. The agent asks before
replacing an existing companion.

## Related

- Skill: [`skills/visual-explainer/`](../skills/visual-explainer/)
- Library how-to: [how-to-bmurrtech-skills.md](how-to-bmurrtech-skills.md)
- Scaffold tree: [skill-scaffold.md](skill-scaffold.md)
