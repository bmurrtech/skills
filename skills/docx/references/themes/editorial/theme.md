# Theme: editorial

Narrative / proposal / memo voice. Georgia body, Arial display headings, ink +
burgundy accent, 1.1" margins, soft gray table headers (not loud navy).

**Apply SoT:** bash below (`docx styles set` has no `--batch` on pin 0.26.0).
[tokens.json](tokens.json) = machine summary · [styles.json](styles.json) /
[styles-set.jsonl](styles-set.jsonl) = snapshots (regen if bash changes; do not
invent a JSONL styles batch).

## Apply (after `docx create OUT.docx …`)

Replace `OUT.docx` with the confirmed path.

```bash
docx styles set-default-font OUT.docx "Georgia" --size 11
docx styles set OUT.docx --at Normal --font "Georgia" --size 11 --color 1C1917
docx styles set OUT.docx --at Title --font "Arial" --color 1C1917 --size 28 --bold --space-after 8
docx styles set OUT.docx --at Subtitle --color 78716C --size 13 --italic --space-after 10
docx styles set OUT.docx --at Heading1 --font "Arial" --color 1C1917 --size 16 --bold --space-before 22 --space-after 8
docx styles set OUT.docx --at Heading2 --font "Arial" --color 7F1D1D --size 13 --bold --space-before 16 --space-after 6
docx styles set OUT.docx --at Heading3 --font "Arial" --color 7F1D1D --size 12 --bold --space-before 12 --space-after 4
docx sections OUT.docx --margins 1.1
```

## Tables

```bash
docx tables format OUT.docx --at tN:r0 --shade E7E5E4 --valign center --repeat-header
docx edit OUT.docx --at tN:r0cC --color 1C1917 --size 10 --bold
```

## Verify

```bash
docx validate OUT.docx
docx outline OUT.docx
```

**Done when:** styles + margins applied; table headers shaded when tables exist;
`theme: editorial` stated.
