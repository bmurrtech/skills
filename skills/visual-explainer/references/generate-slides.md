---
description: Generate a slide deck as a self-contained HTML page
---

Generate a slide deck for: $@

## Steps

1. Read [slide-authoring.md](slide-authoring.md) (copy, layouts, attributes, Boundaries).
2. Read [deck-shell.html](deck-shell.html) once — frozen base. Copy it; replace only
   `.deck` slide sections, `<title>`, fonts link, and `:root` theme tokens.
3. Write the full **action-title outline** in chat. Titles alone must read as a
   coherent story. Auto-continue into HTML unless the user interrupts.
4. Read [slide-visual-patterns.md](slide-visual-patterns.md). For each outline
   title, name the pattern that matches what the source describes (funnel,
   quadrant, merge, proportion, calculator, scale…) and its entity colors — in
   chat, one line per slide. Honor any per-slide "visual direction" in the source.
5. Fill slide bodies with those patterns (`vx-*` classes; free-form OK with a
   one-line why comment).
6. Write under the **resolved home**, open in the browser.
7. Run until exit 0:

```bash
python3 skills/visual-explainer/scripts/check_slides.py <resolved-home>/<name>.html
```

Optional AI-readable companion `.md` only when requested (ask before replace).
HTML is the SoT — no PPTX.

**Done when:** outline + per-slide pattern map in chat, shell marker intact,
checker exit 0, HTML path reported.
