# Slide authoring

Read when running **slides** mode (from [generate-slides.md](generate-slides.md)).
Mechanics SoT: [deck-shell.html](deck-shell.html). Mermaid zoom / overflow / CDN
only if a slide needs them: [css-patterns.md](css-patterns.md),
[libraries.md](libraries.md).

## Action-title outline

Before HTML: ordered takeaway sentences covering every major point from
**user-provided** source. Do not invent facts. Titles alone = coherent story;
then fill bodies (auto-continue unless interrupted).

## Shell fill contract

Start from [deck-shell.html](deck-shell.html). Keep `data-ve-deck-shell="1"`,
SlideEngine, nav, overview, print CSS, `vx-*` pattern CSS, and
`--slide-body-min` / `--slide-label-min`. Edit only slide sections inside
`.deck`, document title, fonts link, `:root` theme tokens (incl. `--e1..--e4`),
and one `<style id="deck-custom">` block for deck-specific components.

Per slide:

```html
<section
  class="slide slide--content"
  data-screen-label="04 Cut p99 below 50ms"
  data-action-title="Cut p99 below 50ms"
  data-notes="Optional speaker detail."
>
```

`data-screen-label` = 1-indexed `NN` + action title (for “change slide 4”).
`data-notes` optional (shell: N toggles notes).

## Copy rules

- Action titles: takeaway not topic; strong verb; tied to on-slide data; concise.
  “Customer Sentiment” → a sentence that makes the point.
- Sentence case; aim for one line.
- Tone in the title (good news vs bad).
- Punchy sentences — not paragraphs; speech or `data-notes` carry detail.
- One idea per slide; hierarchy heading → subhead → support.
- One context line per KPI (e.g. “12% above Q1 target”).
- End data slides with a short conclusion or next step under the visual.

## Layout rules

Grid; align; generous whitespace; power at grid power-points. Slide frames for
rhythm (free-form OK — one-line HTML comment when breaking it):

| Class / intent | Use |
|----------------|-----|
| `slide--title` | Open with large headline stating the main idea |
| `slide--divider` | Section break |
| `slide--statement` / big quote | Big statement |
| `slide--dashboard` | Real metrics only + takeaway |
| `slide--split` | Comparison |
| closing `slide--bleed` or final content | Close |
| rare full-bleed statement | Break the template once for a poignant message |

What goes **inside** the frame is chosen by concept, not by frame — see
[slide-visual-patterns.md](slide-visual-patterns.md) (funnel, quadrant, merge,
proportion, calculator chain, scale, pills). Most important view top /
upper-left; multi-view ≤ 3–4; consistent order, positions, and entity colors
across slides.

## Typography and color

Default: one clear sans + optional mono (shell: DM Sans + IBM Plex Mono).
Expressive display only when user/brand asks. Strong contrast; no busy patterns
behind text. **One accent** for data that supports the action title; rest
neutral. Match fonts, sizes, legends, and color scales across visuals.

## Assets

Surf/raster only if the user asks or supplies brand imagery (inline base64/SVG);
soft-fail to CSS/SVG. Mermaid for complex graphs; CSS pipeline / inline SVG for
simple flows.

## Anti-slop

No Inter / Roboto / Arial / system-ui as primary; no purple-on-white cliché; no em dashes; no three identical centered slides in a row.

## Delivery check

```bash
python3 skills/visual-explainer/scripts/check_slides.py <deck.html>
```

Exit 0 required. Clear any in-browser `data-slide-check="overflow"` under
reduced motion before shipping.

## Boundaries

- Do not rewrite SlideEngine, nav, overview, print CSS, or drop `data-ve-deck-shell="1"`.
- Do not call surf unless the user asks for images or supplies brand assets.
- Do not ship with a failing checker or unresolved overflow markers.
- Do not write HTML before the action-title outline exists in chat.
- Do not hand-build components with long inline `style=""` runs; use `vx-*`
  classes or the `deck-custom` style block.
