# Slide visual patterns

Read in slides mode **after** the action-title outline and **before** writing any
slide body. Pick one pattern per slide by matching what the source *describes*.
Classes live in [deck-shell.html](deck-shell.html) (`vx-*`); restyle via tokens,
not by rewriting structure.

Snippets below use **placeholder** labels (Item A, Entity 1, Measure One…).
Replace them with the user's content — do not copy placeholder nouns into a
deck when the source uses different terms.

## Pick by concept

| Source describes… | Use | Not this |
|-------------------|-----|----------|
| Many items enter a process and come out ordered / filtered / ranked | **Funnel** (inputs → process → ranked list) | Title slide with a subtitle |
| 2–4 peer concepts, pillars, roles, equal lenses | **Quadrant** (`vx-quad` of `vx-card`s with short badge) | Metric / dashboard cards |
| A + B combine into C (roll-up, "X and Y form Z") | **Merge** (`vx-merge`; `vx-pair` when two roll-ups sit side by side) | Bullets or two cards with no connector |
| Two aggregates feed one outcome with weights | **Merge** of two weighted inputs → result | Progress bars inside cards |
| Percent split / weights / budget summing to 100 | **Proportion** (`vx-prop`, segment width = value, grouped under a brace label) | Mono list of numbers |
| Formula, calculation, derived score | **Calculator chain** (`vx-calc` cards → arrow → result + one worked example) | Single code block |
| Thresholds, tiers, bands, maturity levels | **Scale** (`vx-scale` bands in order; unscored / N/A as dashed) | Two-column label list |
| Small ordinal rating (1–3, Low/Med/High) | **Pills** (`vx-pills`) next to the thing being rated | Sentence describing the scale |
| Ordered steps / phases | CSS pipeline (process steps) | Numbered bullets |
| Before vs after, option A vs B | `slide--split` comparison | Stacked paragraphs |
| One real measured number with change | `slide--dashboard` metric card + context line | — |
| Complex graph (8+ nodes, branches, cycles) | Mermaid | Hand-drawn CSS |

When the source includes a **"Visual direction"** (or similar) per slide, it is
the spec for that slide: honor its pattern, build order, and slide count. Do not
merge or drop source slides to hit a smaller count unless the user asks.

## Cross-slide rules

- **Entity identity color.** Assign `--e1..--e4` (classes `vx-e1..vx-e4`) to
  recurring concepts once; reuse that color for the same concept on every slide
  (badge, card edge, segment, connector). Parent-group accents may use `--accent`.
- **Kicker + title + takeaway.** Each content slide: `vx-eyebrow` → action title
  → `vx-stage` (centers the visual) → `vx-keyline` (the "so what").
- **Build order = reading order.** Put `.reveal` on parts in assembly order
  (inputs → connector → outcome).
- **Classes over inline styles.** Prefer `vx-*` / slide classes. Deck-specific
  components go in one `<style id="deck-custom">` block.
- **Proportional means proportional.** If a number is a share, encode size
  (`style="--w:30"` on a segment). Never show weights as text only.
- **One worked example** beside any formula.

## Snippets

### Funnel

```html
<div class="vx-funnel">
  <div class="vx-funnel__col"><p>Inputs</p>
    <p class="vx-funnel__item reveal">Item A</p>
    <p class="vx-funnel__item reveal">Item B</p></div>
  <div class="vx-arrow reveal"></div>
  <div class="vx-card reveal"><p class="vx-card__name">Shared process</p>
    <p><span class="vx-badge vx-e1">1</span> <span class="vx-badge vx-e2">2</span>
       <span class="vx-badge vx-e3">3</span> <span class="vx-badge vx-e4">4</span></p></div>
  <div class="vx-arrow reveal"></div>
  <div class="vx-funnel__col"><p>Output</p>
    <p class="vx-rank vx-funnel__item reveal"><b>1</b>Item B</p>
    <p class="vx-rank vx-funnel__item reveal"><b>2</b>Item A</p></div>
</div>
```

### Quadrant

```html
<div class="vx-quad">
  <div class="vx-card vx-e1 reveal"><span class="vx-badge">1</span>
    <p class="vx-card__name">Entity one</p>
    <p class="vx-card__text">Primary question for this lens.</p></div>
  <div class="vx-card vx-e2 reveal"><span class="vx-badge">2</span>
    <p class="vx-card__name">Entity two</p>
    <p class="vx-card__text">Primary question for this lens.</p></div>
  <div class="vx-card vx-e3 reveal"><span class="vx-badge">3</span>
    <p class="vx-card__name">Entity three</p>
    <p class="vx-card__text">Primary question for this lens.</p></div>
  <div class="vx-card vx-e4 reveal"><span class="vx-badge">4</span>
    <p class="vx-card__name">Entity four</p>
    <p class="vx-card__text">Primary question for this lens.</p></div>
</div>
```

### Merge (two roll-ups side by side)

```html
<div class="vx-pair">
  <div class="vx-merge vx-e1">
    <div class="vx-merge__parts">
      <div class="vx-card vx-e1 reveal"><span class="vx-badge">1</span><p class="vx-card__name">Part A</p></div>
      <div class="vx-card vx-e2 reveal"><span class="vx-badge">2</span><p class="vx-card__name">Part B</p></div>
    </div>
    <div class="vx-merge__bracket reveal"></div>
    <div class="vx-merge__out reveal">Measure one<small>Why this grouping matters</small></div>
  </div>
  <div class="vx-merge vx-e3">
    <div class="vx-merge__parts">
      <div class="vx-card vx-e3 reveal"><span class="vx-badge">3</span><p class="vx-card__name">Part C</p></div>
      <div class="vx-card vx-e4 reveal"><span class="vx-badge">4</span><p class="vx-card__name">Part D</p></div>
    </div>
    <div class="vx-merge__bracket reveal"></div>
    <div class="vx-merge__out reveal">Measure two<small>How this grouping is judged</small></div>
  </div>
</div>
```

### Proportion

```html
<div class="vx-prop">
  <div class="vx-prop__group" style="flex:40">
    <p class="vx-prop__label">Measure one · 40%</p>
    <div class="vx-prop__segs">
      <div class="vx-prop__seg vx-e1 reveal" style="--w:20"><span class="vx-prop__pct">20%</span><span>Entity 1</span></div>
      <div class="vx-prop__seg vx-e2 reveal" style="--w:20"><span class="vx-prop__pct">20%</span><span>Entity 2</span></div>
    </div>
  </div>
  <div class="vx-prop__group" style="flex:60">
    <p class="vx-prop__label">Measure two · 60%</p>
    <div class="vx-prop__segs">
      <div class="vx-prop__seg vx-e3 reveal" style="--w:30"><span class="vx-prop__pct">30%</span><span>Entity 3</span></div>
      <div class="vx-prop__seg vx-e4 reveal" style="--w:30"><span class="vx-prop__pct">30%</span><span>Entity 4</span></div>
    </div>
  </div>
</div>
```

### Calculator chain + scale

```html
<div class="vx-calc-row">
  <div>
    <div class="vx-calc reveal"><p class="vx-calc__tag">Measure one</p>
      <p class="vx-calc__eq">M1 = f(inputs…)</p></div>
    <div class="vx-calc reveal"><p class="vx-calc__tag">Measure two</p>
      <p class="vx-calc__eq">M2 = g(inputs…)</p></div>
  </div>
  <div class="vx-arrow reveal"></div>
  <div class="vx-calc reveal"><p class="vx-calc__tag">Overall</p>
    <p class="vx-calc__eq">Overall = M1×w1 + M2×w2</p>
    <p class="vx-card__text">Example: … → 90.0</p></div>
</div>
<div class="vx-scale" style="margin-top:20px">
  <div class="vx-scale__band reveal" style="--band:var(--green)"><b>Tier A</b><span>≥ 80</span></div>
  <div class="vx-scale__band reveal" style="--band:var(--e2)"><b>Tier B</b><span>65–79</span></div>
  <div class="vx-scale__band reveal" style="--band:var(--accent)"><b>Tier C</b><span>50–64</span></div>
  <div class="vx-scale__band reveal" style="--band:var(--red)"><b>Tier D</b><span>&lt; 50</span></div>
  <div class="vx-scale__band vx-scale__band--off reveal"><b>Unscored</b><span>missing evidence</span></div>
</div>
```

## Boundaries

- Do not use `slide--dashboard` / metric cards for anything that is not a real measured number.
- Do not show a share, weight, or threshold as text only — encode it in size or order.
- Do not recolor the same entity between slides.
- Do not compress a source that specifies N slides into fewer without the user asking.
- Do not leave placeholder snippet labels in a shipped deck when the source names real terms.
