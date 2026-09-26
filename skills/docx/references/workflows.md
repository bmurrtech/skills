# Workflows

`docx <command> --help` is authoritative.

## create

```bash
docx create OUT.docx --from draft.md
docx create OUT.docx --text-file body.txt
```

Confirm `OUT.docx` first. No bundled starter template.

## read

```bash
docx read FILE
docx read FILE --ast
docx outline FILE
docx find FILE "phrase"
docx wc FILE
```

Use `find` for span locators — do not hand-count offsets.

## edit

```bash
docx replace FILE "old" "new"
docx replace FILE --batch fills.jsonl
docx edit FILE --at LOC --text "…"
docx insert FILE --after LOC --text "…"
docx delete FILE --at LOC
docx comments add FILE --anchor "…" --text "…"
docx comments list FILE
docx comments resolve FILE --at cN
```

Overwrite unless `-o` / `--dry-run`.

## redline

```bash
docx track-changes FILE on
docx replace FILE "old" "new"
docx track-changes list FILE
docx read FILE --current
docx track-changes accept FILE --at tcN   # or --all / reject
```

## render

```bash
docx render FILE --out pages/
```

Only when layout must be verified. See [host-apps.md](host-apps.md).
