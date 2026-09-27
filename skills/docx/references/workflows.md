# Workflows

`docx <command> --help` is authoritative. Command map:
[commands.md](commands.md).

## create

```bash
docx create OUT.docx --from draft.md
docx create OUT.docx --text-file body.txt
```

Confirm `OUT.docx` first. No bundled starter template. `--text-file` lands
literal text (each newline a paragraph) when GFM would mangle content.

## read

```bash
docx read FILE
docx read FILE --ast
docx read FILE --from t1 --to t1
docx outline FILE
docx find FILE "phrase"
docx find FILE --batch queries.jsonl --json
docx wc FILE
docx diff FILE --against OLD.docx
```

Use `find` for span locators — do not hand-count offsets. `--current` shows
tracked changes as CriticMarkup; default read is accepted-clean.

## edit

```bash
docx replace FILE "old" "new"
docx replace FILE "old" "new" --all
docx replace FILE "[Status]" "Approved" --bold --clear highlight
docx replace FILE --batch fills.jsonl
docx edit FILE --at LOC --text "…"
docx edit FILE --at t2:r2c1 --text "Charlie Darwin"
docx insert FILE --after LOC --text "…"
docx delete FILE --at LOC
docx comments add FILE --anchor "…" --text "…"
docx comments reply FILE --at cN --text "…"
docx comments list FILE
docx comments resolve FILE --at cN
```

`replace` preserves run formatting/tabs unless you overlay `--bold` / `--color`
/ `--clear`. Overwrite unless `-o` / `--dry-run`. Batch locators address the
document **as read** — one read, one write.

## redline

```bash
docx track-changes FILE on
docx replace FILE "old" "new"
docx edit FILE --at p12:0-40 --text "…" --track
docx track-changes list FILE
docx read FILE --current
docx track-changes accept FILE --at tcN   # or --all / reject
```

## render

```bash
docx render FILE --out pages/
```

Only when layout must be verified (columns, breaks, image/table geometry).
See [host-apps.md](host-apps.md).
