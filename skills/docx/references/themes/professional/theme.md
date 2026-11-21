# Theme: professional

Corporate / exec / client-facing default. Navy headings, Calibri, 1" margins.

**Apply SoT:** bash below (`docx styles set` has no `--batch` on pin 0.26.0).
[tokens.json](tokens.json) = machine summary · [styles.json](styles.json) /
[styles-set.jsonl](styles-set.jsonl) = snapshots (regen if bash changes; do not
invent a JSONL styles batch).

## Apply (after `docx create OUT.docx …`)

Replace `OUT.docx` with the confirmed path.

```bash
docx styles set-default-font OUT.docx "Calibri" --size 11
docx styles set OUT.docx --at Normal --font "Calibri" --size 11 --color 1F2937
docx styles set OUT.docx --at Title --color 1E3A5F --size 26 --bold --space-after 6
docx styles set OUT.docx --at Subtitle --color 6B7280 --size 14 --space-after 6
docx styles set OUT.docx --at Heading1 --color 1E3A5F --size 16 --bold --space-before 18 --space-after 8
docx styles set OUT.docx --at Heading2 --color 1E3A5F --size 13 --bold --space-before 14 --space-after 6
docx styles set OUT.docx --at Heading3 --color 1E3A5F --size 12 --bold --space-before 12 --space-after 4
docx sections OUT.docx --margins 1
```

## Tables

After tables exist, `docx read OUT.docx` → for each header row:

```bash
docx tables format OUT.docx --at tN:r0 --shade 1E3A5F --valign center --repeat-header
```

Then white bold header text (locate cells; do not reuse stale JSONL):

```bash
docx edit OUT.docx --at tN:r0cC --color FFFFFF --size 10 --bold
```

## Verify

```bash
docx validate OUT.docx
docx outline OUT.docx
```

**Done when:** styles + margins applied; table headers shaded when tables exist;
`theme: professional` stated.
