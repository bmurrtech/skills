---
description: Generate a slide deck as a self-contained HTML page
---

Generate a slide deck for: $@

Before writing HTML, read `./slide-deck.html`, `./slide-patterns.md`, and only the shared CSS/library sections needed for the source.

Plan the deck first: inventory the source, map every item to slides, choose a narrative arc, and assign a composition to each slide. Use the 10 slide types and nav chrome from `slide-patterns.md` / `slide-deck.html`, including carousel dots, prev/next, slide count, and keyboard controls. Treat `100dvh` as a hard content budget: split dense content across slides rather than scrolling or dropping content. Before delivery, enable `prefers-reduced-motion: reduce` at the target viewport and a short landscape height; fix every overflow or `autoFit()` warning before shipping.

Use visual-first slides: diagrams, charts, tables, SVG accents. Vary compositions; three centered slides in a row is a smell.

This remake does **not** ship a PPTX exporter — deliver the HTML deck as the source of truth.

Write to `.scratch/diagrams/` and open in the browser. Optional AI-readable companion `.md` only when requested (ask before replace).
