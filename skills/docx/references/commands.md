# docx command reference

Authoritative, versioned help: `docx <command> --help` (and `docx --help` for
the index). This file is a quick map aligned to the library pin (**0.26.0**).
None of the `info` commands need a FILE:

```bash
docx --help            # every command, one capability hint each
docx info locators     # the addressing grammar (the backbone)
docx info schema       # the JSON-AST shape that `docx read --ast` emits
docx info skill        # skill text regenerated from the binary
```

## Read & query (never mutate)

| Command | What it does |
| ------- | ------------ |
| `read FILE` | Markdown with `pN` locators. `--from/--to` slice; `--accepted` (default) / `--current` / `--baseline`; `--comments`; `--ast` for JSON AST. |
| `find FILE [QUERY]` | Find spans by text or formatting; returns locators for `--at`. `--batch queries.jsonl` + `--json` for many queries in one read. |
| `wc FILE [LOCATOR]` | Word count (whole doc or slice). |
| `outline FILE` | Headings as a locator tree. |
| `diff FILE --against OLD` | What changed vs another version (snapshot OLD first). |
| `render FILE` | Page PNG/JPG via Word or LibreOffice — layout only. |
| `styles FILE` | List/describe styles (`--used`, `--at ID`). |
| `validate FILE` | Schema-check WML parts (exit 0 = clean). |
| `info <topic>` | `schema` / `locators` / `skill` — no FILE. |

## Mutate (overwrite in place; `-o PATH` copies; `--dry-run` previews)

| Command | What it does |
| ------- | ------------ |
| `create FILE` | New `.docx` (`--from PATH.md` / `-`; `--text-file` for literal text). |
| `edit FILE` | Replace/strip text or formatting at a locator (`--clear`, `--track`, `--batch`). |
| `insert FILE` | Insert with `--at` / `--before` / `--after` (`--track`, `--batch`). |
| `delete FILE` | Remove paragraph, range, table, or section break. |
| `replace FILE PATTERN REPL` | Substitute spans (first match; `--all`); preserves formatting; `--bold` / `--color` / `--clear` / `--batch`. |
| `sections FILE` | Multi-column layout, breaks, page setup — only way to do columns. |
| `styles set/create/…` | Restyle headings, mint a style, set default font. |
| `comments` | `add` / `reply` / `resolve` / `delete` / `list` (`--anchor` / `--batch`). |
| `footnotes` / `endnotes` | `add` / `edit` / `delete` / `list`. |
| `headers` / `footers` | `set` / `list` / `clear` (page numbers, fields, …). |
| `images` | `add` / `extract` / `replace` / `delete` / `list`. |
| `hyperlinks` | `add` / `list` / `replace` / `delete`. |
| `tables` | Rows/columns, merge, widths, borders, formatting. |
| `lists` | Renumber / format / restart numbered lists. |
| `track-changes` | `on`/`off`, `list`, `accept`/`reject` (`--at tcN` / `--all`). |
| `raw` | Last resort OOXML patch — hard-gated; prefer other verbs. |

## Two gotchas

1. **Ids shift** after structural edits. Re-read, or `--batch FILE.jsonl` from one read.
2. **`docx read` proves content**; only `docx render` proves layout — once at the end when needed.
