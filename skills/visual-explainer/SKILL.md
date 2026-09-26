---
name: visual-explainer
description: >
  Visual explainer: self-contained HTML for architectures, diffs, plans, slides,
  tables, and recaps under .scratch/diagrams/. Use when the user asks for a
  diagram, architecture overview, visual plan, slide deck, diff review, plan
  review, project recap, fact-check, comparison table, or any visual explanation;
  or when about to dump a complex ASCII table (4+ rows or 3+ columns).
---

# visual-explainer

Turn visual or tabular intent into a **self-contained HTML page** under
`.scratch/diagrams/`, then open it in the browser. Prefer HTML over ASCII art or
box-drawing tables when this skill is loaded.

## Workflow

### 1. Route intent

Pick **one** mode from the user ask (or explicit manual name). Do not ask which
command to run when intent is clear.

| Mode | Manual name | Trigger signals |
|------|-------------|-----------------|
| Diagram | `generate-web-diagram` | diagram, architecture, flowchart, explain visually |
| Visual plan | `generate-visual-plan` | implementation plan as visuals, feature plan HTML |
| Slides | `generate-slides` | slide deck, presentation, magazine-quality slides |
| Diff review | `diff-review` | review this diff, visual diff, architecture before/after |
| Plan review | `plan-review` | compare plan to codebase, plan risk |
| Project recap | `project-recap` | mental model, catch me up, context switch back |
| Fact-check | `fact-check` | verify doc against code, fact-check this HTML/MD |
| Complex table | *(diagram/table)* | about to print 4+ row or 3+ col ASCII table → HTML instead |

If several modes could apply, prefer the **narrower** review/plan/slides mode over
a generic diagram. `--slides` on a scrollable mode means generate a slide deck
for that topic instead of a long page.

**Done when:** mode is named.

### 2. Load mode + templates

Read only what the mode needs:

| Mode | Read |
|------|------|
| Diagram / complex table | [references/generate-web-diagram.md](references/generate-web-diagram.md) + template below |
| Visual plan | [references/generate-visual-plan.md](references/generate-visual-plan.md) |
| Slides | [references/generate-slides.md](references/generate-slides.md), [references/slide-patterns.md](references/slide-patterns.md), [references/slide-deck.html](references/slide-deck.html) |
| Diff review | [references/diff-review.md](references/diff-review.md) |
| Plan review | [references/plan-review.md](references/plan-review.md) |
| Project recap | [references/project-recap.md](references/project-recap.md) |
| Fact-check | [references/fact-check.md](references/fact-check.md) |

**Templates / patterns** (pick by content):

- Text-heavy architecture → [references/architecture.html](references/architecture.html)
- Mermaid flows / sequence / ER / state → [references/mermaid-flowchart.html](references/mermaid-flowchart.html) + Mermaid bits in [references/libraries.md](references/libraries.md)
- Tables / matrices → [references/data-table.html](references/data-table.html)
- CSS / overflow / connectors → [references/css-patterns.md](references/css-patterns.md)
- 4+ major sections → [references/responsive-nav.md](references/responsive-nav.md)
- Named palette or theme picker → [references/themes.md](references/themes.md)

**Representation defaults:** Mermaid for topology/flows; CSS Grid cards for
text-heavy architecture; HTML `<table>` for data; Chart.js for dashboards;
`100dvh` slides for decks.

**Done when:** required refs for this mode are loaded.

### 3. Design, then write HTML

Commit audience, diagram type, and aesthetic before coding HTML (vary; no default
slate/indigo/Inter cliché). Follow mode-specific required sections. Page must be
one complete self-contained HTML document (inline CSS; CDN ok for Mermaid /
Chart.js / fonts).

**Done when:** HTML content is ready to write.

### 4. Deliver under `.scratch/diagrams/`

1. Ensure `.scratch/diagrams/` exists (create if missing).
2. Write `*.html` with a descriptive kebab-case name.
3. **Markdown companion (feature):** write `.scratch/diagrams/<same-basename>.md`
   **only** when the user asks for an AI-readable / source-brief equivalent.
   HTML remains the visual SoT; the `.md` is never the HTML source. Ask before
   replacing an existing companion.
4. Open the HTML in the browser when the harness allows; otherwise report the
   `file://` path.
5. In chat: short summary + path(s). Do not paste the full HTML.

**Done when:** HTML is on disk, browser opened or path reported, companion rules
honored.
