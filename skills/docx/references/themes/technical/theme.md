# Theme: technical

Engineering / specs / runbooks. Dense Arial, near-black H1, teal H2/H3, 0.75"
margins, slate table headers.

**Apply SoT:** bash below (`docx styles set` has no `--batch` on pin 0.26.0).
[tokens.json](tokens.json) = machine summary · [styles.json](styles.json) /
[styles-set.jsonl](styles-set.jsonl) = snapshots (regen if bash changes; do not
invent a JSONL styles batch).

## Apply (after `docx create OUT.docx …`)

Replace `OUT.docx` with the confirmed path.

```bash
docx styles set-default-font OUT.docx "Arial" --size 10
docx styles set OUT.docx --at Normal --font "Arial" --size 10 --color 111827
docx styles set OUT.docx --at Title --color 111827 --size 22 --bold --space-after 4
docx styles set OUT.docx --at Subtitle --color 64748B --size 12 --space-after 4
docx styles set OUT.docx --at Heading1 --color 111827 --size 14 --bold --space-before 14 --space-after 4
docx styles set OUT.docx --at Heading2 --color 0F766E --size 12 --bold --space-before 10 --space-after 3
docx styles set OUT.docx --at Heading3 --color 0F766E --size 11 --bold --space-before 8 --space-after 2
docx sections OUT.docx --margins 0.75
```

## Tables

```bash
docx tables format OUT.docx --at tN:r0 --shade 334155 --valign center --repeat-header
docx edit OUT.docx --at tN:r0cC --color F8FAFC --size 9 --bold
```

## Verify

```bash
docx validate OUT.docx
docx outline OUT.docx
```

**Done when:** styles + margins applied; table headers shaded when tables exist;
`theme: technical` stated.
