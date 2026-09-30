# Post-grill next steps

Read when the design-tree frontier is empty. This beat **replaces** a separate
“confirm shared understanding” ask — choosing A, B, or C affirms shared
understanding and routes.

## Prompt shape

Present exactly this choice (adapt slash style to the host if needed):

```text
**Next step?** (route A/B/C — not setup Commit PRDs? A/B)

**A)** `/to-prd` — write a PRD under docs/prd/ from this grill
**B)** `/handoff` → implement (`impl`) — pack plan for a fresh agent
**C)** `Go` — kick off implementation in this session without a skill

➡️ **A** (default cycle: grill → PRD → implement)
```

Always recommend **A**. One-line why is enough.

## On reply

| Choice | Action |
|--------|--------|
| **A** (or affirmatives that accept the ➡️) | Auto-run **`to-prd`** in this session from the grilled decisions. Do not wait for a second invoke. |
| **B** | Auto-run **`handoff`** with aim **implement** / kind **`impl`**. Spec = grilled plan (link paths if any). No aim-ask beat. |
| **C** / `Go` / `GO` | Wait only if they have not already said Go in this message. Then implement the settled plan **in this session without loading `/implement`**. Still honor hard bans (no stage/commit/push/PR unless the user separately runs **`commit`**). |

Silent on some options after a partial answer → do **not** invent a route; ask once which of A/B/C.

## Boundaries

- Do **not** auto-author a PRD unless the user picked **A** (or accepted ➡️ A).
- Do **not** load **`implement`** on **C** — bare build only.
- **B** owns the handoff file; the next agent owns **`implement`**.
- README default cycle stays grill → to-prd → implement; A matches that path.
