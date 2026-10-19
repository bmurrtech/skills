# Doop diagram compose (shared)

Read before every draw or structural edit. Type-specific layout lives in
`*-template.md`. Edit this file when testing shows the grammar is wrong.

## Purpose

One sentence before drawing: what should a stakeholder understand after looking?

Prefer several focused frames/pages over one crowded mural.

## Backbone first

1. Draw the happy path (primary spine) before branches, failures, or parallel paths.
2. Label edges that carry meaning (event, trigger, payload, guard, protocol).
3. Add only differences that change understanding.
4. Do not invent nodes or guarantees — mark `[TBD]`, `[Assumption]`, `[Existing]`, `[Proposed]`, `[Optional]`, `[Deprecated]`.
5. If dense, split by layer or by question (separate frames/pages).

## Visual grammar (Doop HTML frames)

Frames are complete HTML documents in sandboxed iframes. Design to the frame size; reset margin/box-sizing.

| Element | Default treatment |
|---------|-------------------|
| Noun / system / step | Rounded rectangle; short title + optional one-line detail |
| Decision | Diamond or clearly marked decision pill |
| Actor / role | Capsule or lane header |
| Boundary (trust, VPC, SaaS plane) | Hard outlined region with title |
| Soft group | Light background band — not a dependency |
| Primary path | Solid arrow, stronger stroke |
| Optional / weaker path | Dashed arrow; legend explains dashes |
| Bidirectional | Two-headed or paired arrows with labels |

**Shapes/arrows:** stay consistent inside a canvas (fixed legend).  
**Color:** soft accents OK for lanes/domains; one ground, one strong accent; avoid purple-gradient AI clichés and neon-on-charcoal.  
**Type:** readable labels; no lorem; no emoji-as-icons.

## Icons (hybrid)

1. Prefer Doop MCP `search_icons` for UI symbols (DB, mail, message, cloud, server, webhook, …).
2. Choose icons from the stakeholder vocabulary in the prompt — relevance over a rigid allowlist.
3. If search misses, use simple inline SVG or labeled shape; never gray “icon here” tiles.
4. Real vendor logos only via `search_logos` when the brand is truly in the stack; do not invent marks.

## MCP ops (steal, then override)

- Call `get_guide` once for etiquette/streaming/review checkpoints.
- Narrate with `set_status` (short, present tense).
- After create or significant edit: `get_frame_screenshot` and fix fit/spacing/alignment issues.
- Prefer `edit_frame_html` for surgical meeting changes.
- Persist standing taste with `set_guidelines` / `save_decision` (diagram grammar, not marketing moodboards).

**Override:** ignore landing-page heroes, stock photography mandates, and logo-wall habits unless the operator asked for a UI mock.

## Frame sizing (starting points)

| Content | Size |
|---------|------|
| Process strip | 1400×720 |
| Wide topology | 1600×900 |
| Swimlane | 1400×900 |
| Sequence | 1200×800 |

Resize with `update_frame` after content settles — frames do not scroll for viewers.

## Exit check

Clear entry and direction? Important edges labeled? Material uncertainty marked? Better than the same idea in sentences?
