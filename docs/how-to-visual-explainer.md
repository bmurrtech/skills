# How to use `visual-explainer`

Complex visual or tabular intent → self-contained HTML, opened in the browser.
Default home **`.scratch/visuals/`**; tracked **`docs/visuals/`** when the ask is
for team/group/commit/docs. Intent routing picks the mode.

Install and scaffold (including `.scratch/visuals/` and `docs/visuals/`) are
covered in [how-to-bmurrtech-skills.md](how-to-bmurrtech-skills.md). This page is
modes + prompts — not a second install guide. Decision: [ADR 0014](adr/0014-ADR-visual-explainer-homes.md).

## Flow

```text
your ask ──► visual-explainer ──► resolve mode ──► resolve home
                    │                                    │
                    │                         .scratch/visuals/  (default)
                    │                      or docs/visuals/      (durable cues)
                    v                                    v
              one mode runs                    <name>.html
                                                     │
                                                     + - - [if asked] → <name>.md
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
- Help choosing a mode when the ask is unclear

## Intent → mode

| You mean… | Mode |
|-----------|------|
| Diagram / architecture / “explain visually” | Diagram |
| Visual implementation plan / “I need a plan…” | Visual plan |
| Slide deck / presentation | Slides |
| Review this diff / before-after | Diff review |
| Compare plan to codebase / plan risk | Plan review |
| Catch me up / mental model | Project recap |
| Verify doc against code | Fact-check |
| About to dump a big terminal table | Complex table → HTML |

If several could apply, prefer the narrower review/plan/slides mode over a
generic diagram. Unclear or “what kind of visual?” → the skill suggests once
from your content, then waits.

## Homes

| Cue in your ask | Write root |
|-----------------|------------|
| (none / draft / private) | `.scratch/visuals/` |
| team, group, commit, track, docs, README, publish… | `docs/visuals/` |

## Example prompts

```text
Explain our auth flow as a diagram
Visual plan for adding SSO
Make a slide deck from docs/how-to-bmurrtech-skills.md
Review the diff on this branch as HTML
Plan-review docs/prd/0001-PRD-foo.md against the code
Project recap — I have not touched this repo in two weeks
Fact-check .scratch/visuals/auth-flow.html
Compare these 12 requirements in a table
Also write an AI-readable Markdown companion beside the HTML
Put this architecture diagram in docs for the team
What kind of visual should I use for this notes dump?
```

## Output

| Artifact | When |
|----------|------|
| `<home>/<name>.html` | Always (visual SoT); open in browser when allowed |
| `<home>/<name>.md` | **Only** when you ask for an AI-readable / source-brief equivalent |

`<home>` is `.scratch/visuals/` or `docs/visuals/`. The Markdown companion is
**not** the source of the HTML. The agent asks before replacing an existing
companion.

## Related

- Skill: [`skills/visual-explainer/`](../skills/visual-explainer/)
- Library how-to: [how-to-bmurrtech-skills.md](how-to-bmurrtech-skills.md)
- Scaffold tree: [skill-scaffold.md](skill-scaffold.md)
- ADR: [0014](adr/0014-ADR-visual-explainer-homes.md)
