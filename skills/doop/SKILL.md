---
name: doop
description: >
  Localhost Doop canvases for business-process and present-state architecture
  diagrams (Lucid/Eraser-style), edited live over MCP from the coding harness.
  Use when drawing or updating a lead funnel, lifecycle, swimlane, topology, or
  stack map on Doop; ensuring local Doop is up; connecting MCP; or capturing
  meeting notes against a canvas id.
disable-model-invocation: true
---

# doop

Stakeholder **process** and **architecture** diagrams on localhost Doop.
Inference stays in the harness; Doop is the live canvas via MCP. Prefer skill
templates over Doop’s stock UI/marketing taste.

## Boundaries

- Do **not** treat Doop DB files under its `data/` as consumer-repo artifacts.
- Certainty tags and invent rules: [compose.md](references/compose.md) (backbone first).

## Workflow

### 1. Route mode + form

| Signal | Mode | Default form(s) |
|--------|------|-----------------|
| funnel, process, lifecycle, stages, swimlane | `process` | [pipeline-template.md](references/pipeline-template.md) + [lifecycle-template.md](references/lifecycle-template.md) |
| architecture, stack, systems, SaaS, topology | `architecture` | [topology-template.md](references/topology-template.md) |
| both / full picture | `both` | process defaults + topology (one canvas, two pages/frames) |

Honor explicit form flags (`sequence`, `swimlane`, `decision-tree`, `boxes-edges`, `lineage`, …). Ambiguous → ask once.

Always load [compose.md](references/compose.md), then the matching `*-template.md`. Other refs when needed: [mcp-connect.md](references/mcp-connect.md), [sidecar-template.md](references/sidecar-template.md), [boxes-edges-template.md](references/boxes-edges-template.md), [sequence-template.md](references/sequence-template.md), [swimlane-template.md](references/swimlane-template.md), [decision-tree-template.md](references/decision-tree-template.md), [lineage-template.md](references/lineage-template.md).

**Done when:** mode + form list chosen; compose + templates loaded.

### 2. Ensure localhost Doop

Resolve Doop home (`DOOP_HOME`, else `~/.doop`, else ask once). Probe / start:

```bash
python3 skills/doop/scripts/ensure_doop.py status
python3 skills/doop/scripts/ensure_doop.py ensure
```

Harness install: resolve this skill’s `scripts/ensure_doop.py` the same way. Script refuses start unless checkout identity matches upstream Doop; refuses “already up” unless `/healthz` or Doop HTML markers match. Ports/runtime details: `python3 …/ensure_doop.py --help` (incl. `stop`).

**Done when:** Doop identified live (or clear prereq / identity failure reported).

### 3. Connect MCP (harness)

If MCP to Doop is not already available, print the matching one-liner from
[mcp-connect.md](references/mcp-connect.md). Do not claim edits succeeded without tools.

**Done when:** MCP tools callable, or operator blocked on connect with instructions.

### 4. Canvas + sidecar

- Reuse canvas id if the operator named one or `.scratch/doop/<slug>.md` exists for this session.
- Else `create_canvas`; for `both`, use two pages/frames (Process | Architecture).
- Call `get_guide({ topic: "doop-instructions" })` once for MCP ops etiquette, then **override aesthetics** with skill compose + templates.
- Seed durable grammar via `set_guidelines` (named doc, e.g. `bmurrtech-diagram-grammar`) from compose + active templates.
- Write or append `.scratch/doop/<slug>.md` — see [sidecar-template.md](references/sidecar-template.md).

**Done when:** canvas URL/id known; sidecar on disk; guidelines seeded or confirmed present.

### 5. Draw or edit

**New draw:** happy-path backbone first per compose; stream HTML with `append_frame_html` (sensible chunks); `set_status` while working; `get_frame_screenshot` after major sections and at end.

**Live edit (meeting):** `get_canvas` → prefer `edit_frame_html` → screenshot → confirm with room. Structural redraw only when surgical edit cannot express the change.

**Icons:** prefer Doop `search_icons`; hybrid creativity OK when the stakeholder prompt needs a clearer symbol — see compose.

**Feedback:** address harness chat requests immediately; also poll/claim Doop UI feedback and `get_comments` when humans type on the canvas.

**Done when:** frames match the asked change; screenshot reviewed; unknowns tagged.

### 6. Close the beat

Remind: export PNG/JPG from Doop UI if they need files outside Doop. Append meeting notes to the sidecar. Wait for the next NL change.

**Done when:** sidecar updated; operator knows export is manual.
