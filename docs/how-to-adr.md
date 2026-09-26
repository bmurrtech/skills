# How to use `to-adr`

Record one significant decision under **`docs/adr/`**. Markdown is authoritative.
Optional **at-a-glance** HTML catalogs the decision log for browsing.

Install and scaffold are covered in [how-to-bmurrtech-skills.md](how-to-bmurrtech-skills.md)
(run **`setup-bmurrtech-skills`** so `docs/adr/` and `.scratch/adr-optics/` exist).
This page is prompts + scope — not a second install guide.

## What ADRs cover (and do not)

Create only when costly to reverse, alternatives were real, or someone will ask
“why this way?” later. One decision per file. Accepted files are immutable —
change course by **superseding**.

Placement (ADR vs PRD / AGENTS / glossary), anti-bloat, and the heading template
live in the skill — not duplicated here:
[`skills/to-adr/references/mechanics.md`](../skills/to-adr/references/mechanics.md).

OKF split: glossary owns terms (`CONTEXT.md` / `knowledge/`); ADRs own *which
option won and why*; PRDs (`docs/prd/`, local) cite ADRs; ops stay in `AGENTS.md`.

## Authoring prompts

```text
Record an ADR: we keep the release artifact as skills/ + LICENSE only
Supersede ADR 0003 — template SoT moves into the shipped to-adr skill
Relate this choice to ADR 0005 without superseding it
```

Ambiguous create vs edit → say which. Point at an existing ADR when the warrant
fails instead of minting a twin.

## At-a-glance visualization

After create/supersede (or anytime you want the decision log), ask the agent to
refresh the catalog. Output lands under **`.scratch/adr-optics/`** (gitignored);
Markdown under `docs/adr/` stays SoT. The skill **opens the HTML in your default
browser** after a visualize prompt. If `.scratch/adr-optics/` is missing, the
skill runs **`setup-bmurrtech-skills`** first.

```text
docs/adr/*.md ──► build_catalog ──► .scratch/adr-optics/adr-at-a-glance.html
                      │                      │
                      │                      +── adr-catalog.json (same dir)
                      v
                 browser opens (file://)
```

### Prompts to refresh the view

```text
Refresh the ADR at-a-glance catalog
Rebuild the decision-log visualizer for docs/adr/
Open the ADR catalog HTML after superseding 0010
```

Prefer natural-language refresh; the skill owns rebuild + open.

### Open manually in a browser

If the agent could not auto-open: open the path it reports
(`.scratch/adr-optics/adr-at-a-glance.html`, or a `file://` URI to that file).

Companion JSON (search/debug): `.scratch/adr-optics/adr-catalog.json` — row shape
(full `markdown` + git `history` for offline pane) → [knowledge/adr-catalog.md](../knowledge/adr-catalog.md).

## Related

- Skill: [`skills/to-adr/`](../skills/to-adr/)
- Library how-to: [how-to-bmurrtech-skills.md](how-to-bmurrtech-skills.md)
- Scaffold tree: [skill-scaffold.md](skill-scaffold.md)
- Concept: [knowledge/adr.md](../knowledge/adr.md)
- Index: [adr/index.md](adr/index.md)
