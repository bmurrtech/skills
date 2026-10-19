---
name: visual-explainer
description: >
  Visual explainer: self-contained HTML for architectures, diffs, plans, slides,
  tables, and recaps. Default home .scratch/visuals/; tracked docs/visuals/ when
  the ask is for team/group/commit/docs. Use when the user asks for a diagram,
  architecture overview, visual plan, slide deck, diff review, plan review,
  project recap, fact-check, comparison table, help choosing a visual, or any
  visual explanation; or when about to dump a complex ASCII table (4+ rows or
  3+ columns).
---

# visual-explainer

Turn visual or tabular intent into a **self-contained HTML page**, then open it
in the browser. Prefer HTML over ASCII art or box-drawing tables when this skill
is loaded.

**Homes:** default **`.scratch/visuals/`** (gitignored). **`docs/visuals/`**
when the ask is durable/public — see step 2 and [references/homes.md](references/homes.md).

## Workflow

### 1. Resolve mode

Pick **one** mode from the user ask (or explicit manual name).

| Mode | Manual name | Clear signals (run — do not ask) |
|------|-------------|----------------------------------|
| Diagram | `generate-web-diagram` | diagram, architecture, arch diag, flowchart, explain visually |
| Visual plan | `generate-visual-plan` | implementation plan as visuals, “I need a plan…”, feature plan HTML |
| Slides | `generate-slides` | slide deck, presentation, magazine-quality slides |
| Diff review | `diff-review` | review this diff, “see the diff”, visual diff, architecture before/after |
| Plan review | `plan-review` | compare plan to codebase, plan risk |
| Project recap | `project-recap` | mental model, catch me up, context switch back |
| Fact-check | `fact-check` | verify doc against code, fact-check this HTML/MD |
| Complex table | *(diagram/table)* | about to print 4+ row or 3+ col ASCII table → HTML instead |

**Visual plan** ≠ **plan review**: a new/feature plan → visual plan; comparing a
plan to the codebase or assessing plan risk → plan review.

If several modes could apply, prefer the **narrower** review/plan/slides mode
over a generic diagram. `--slides` on a scrollable mode means generate a slide
deck for that topic instead of a long page.

**Unclear mode, or user asks for help / confirmation before creating:** suggest
**once** from the content — recommended mode + 1–2 alternates — then wait. Do
**not** ask when a clear signal or manual name is already present.

**Done when:** mode is named (or one suggest-and-wait is in flight).

### 2. Resolve home

| Home | When |
|------|------|
| `.scratch/visuals/` | Default — private, draft, or no durable cue |
| `docs/visuals/` | Durable/public cues (team, group, commit/track, docs/README/publish) — [references/homes.md](references/homes.md) |

Soft uncertainty (“maybe later”) → **`.scratch/visuals/`** without asking.
Ask placement **only** when the user explicitly wants help choosing a home.

Companion `.md` (if requested) lands in the **same** home as the HTML.

**Done when:** write root is named.

### 3. Load mode + templates

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

### 4. Design, then write HTML

Commit audience, diagram type, and aesthetic before coding HTML (vary; no default
slate/indigo/Inter cliché). Follow mode-specific required sections. Page must be
one complete self-contained HTML document (inline CSS; CDN ok for Mermaid /
Chart.js / fonts).

**Done when:** HTML content is ready to write.

### 5. Deliver under the resolved home

1. Ensure the resolved home exists (create if missing).
2. Write `*.html` with a descriptive kebab-case name.
3. **Markdown companion:** write `<same-basename>.md` in that home **only** when
   the user asks for an AI-readable / source-brief equivalent. HTML remains the
   visual SoT; the `.md` is never the HTML source. Ask before replacing an
   existing companion.
4. Open the HTML in the browser when the harness allows; otherwise report the
   `file://` path.
5. In chat: short summary + path(s). Do not paste the full HTML.

**Done when:** HTML is on disk under the resolved home, browser opened or path
reported, companion rules honored.
