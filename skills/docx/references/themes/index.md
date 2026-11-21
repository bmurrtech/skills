# Themes

Named style kits for **create** (and restyle of a fresh create). Not domain
templates — colors, fonts, margins, heading defs, table-header recipe only.

## Pick

| Theme | When (keywords / cues) |
|-------|------------------------|
| **professional** | professional, corporate, business, executive, board, client-facing, formal, consulting — **default** if create with no cue |
| **technical** | technical, engineering, design doc, architecture, RFC, API, runbook, spec, ADR |
| **editorial** | editorial, narrative, storytelling, proposal, brief, warm, creative, memo, essay |
| *(none)* | plain, unstyled, no theme, raw markdown — skip apply |

Ambiguous multi-cue → prefer **professional**; state the choice in one line.
User names a theme id → that id wins. Do not invent a fourth ad-hoc palette
unless the operator supplies brand tokens.

## Load

After pick, read **only** that folder:

- [professional/theme.md](professional/theme.md)
- [technical/theme.md](technical/theme.md)
- [editorial/theme.md](editorial/theme.md)

Each folder also has `tokens.json`, `styles.json`, `styles-set.jsonl`.

## Apply contract

1. `docx create OUT.docx --from draft.md` (or `--text-file`)
2. Follow the theme’s `theme.md` (default font → style create/set → margins →
   table headers after tables exist)
3. State `theme: <id>` in the session reply
4. `docx validate OUT.docx` before handoff

`docx create --from` maps Markdown `#`/`##`/`###` → `Heading1`/`Heading2`/
`Heading3` (not `Title`/`Subtitle`). Still set Title/Subtitle defs so explicit
`--style Title` inserts match the kit. Lists use `ListParagraph` (basedOn
`Normal`) — restyle `Normal` + `set-default-font`.

Style-id mutations (`Heading1`, …) are stable. Do **not** ship content-locator
JSONL in theme kits — re-locate table rows with `docx read` / `docx find` after
create.

## Done when

Theme id chosen (or plain skip); `theme.md` steps exit 0; operator has path +
theme name.
