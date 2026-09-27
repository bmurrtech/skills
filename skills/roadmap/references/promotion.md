# Promotion (scratch → roadmap)

Read when normalizing a `.scratch/ideas/` dump into a `docs/ROADMAP.md` entry.

**Shapes (keep synchronized):**

| Layer | SoT |
|-------|-----|
| Public ledger entry | [roadmap-template.md](roadmap-template.md) (entry below the HTML comment) |
| Internal scratch | [scratch-template.md](../../idea/references/scratch-template.md) |

Scratch is detailed (dev notes OK). Roadmap is the same field spine, leaner, public.

**Public vs process:** `roadmap-template.md` / `docs/ROADMAP.md` hold only reader-facing
conventions (non-commitment, unordered, undated) and entry shape. Author/agent
process stays here and in `SKILL.md` — never copy process bullets into the ledger.

## Authoring bar (agent-facing)

When promoting or drafting an entry:

- Capture enough context that the idea remains understandable in a future session.
- Record boundaries and constraints when they materially affect implementation.
- Assume research, validation, and testing before implementation where required;
  state only durable constraints in the published entry, not process reminders.

## Commitment levels

```text
brain dump
   ↓  idea skill (default / ambiguous)
/.scratch/ideas/
   ↓  explicit promote
/docs/ROADMAP.md
   ↓  explicit publish
GitHub / Fizzy
```

Never infer publication from capture or promotion.

## Field mapping

| Roadmap field | Derived from scratch |
|---------------|----------------------|
| Title | Short durable name (`#` working title → `##` public title) |
| Domain | System or concern primarily affected |
| Intent | Why the idea exists and what outcome it seeks (1–2 sentences) |
| Scope | Capabilities explicitly or strongly implied (fewer bullets) |
| Boundaries | Non-goals, ownership distinctions, and "don't do X" |
| Constraints | Hard architectural / context / security / compat / ops only |
| Open Questions | Meaningful unresolved decisions |
| Interfaces | Scratch / GitHub / Fizzy / PRD·handoff / Knowledge rows with signal |
| Notes | Public-worthy context only |

**Usually drop on promote:** `Context`, `References`, `Dev notes`, and procedural
“we should test X” lines unless they are durable constraints.

## Required vs optional (published entry)

**Always emit:** title (`## …`), Domain, Intent, Scope, Boundaries.

**Emit when signal exists:** Constraints, Open Questions, Interfaces, Notes.

Do **not** invent detail to fill fields. Do **not** publish filler such as
`None.` / `None known.` for optional sections — omit the section instead.
(The blank entry in `roadmap-template.md` shows placeholders for authors; live
entries stay sparse.)

## Noise reduction

Drop implementation procedure that is not a durable constraint. Keep the
underlying constraint (“must not bloat context”).

## Provenance

After append, mark the scratch file (do not delete):

```markdown
> Promoted to `/docs/ROADMAP.md#<anchor>`
```

When promoting from scratch, set **Interfaces → Scratch** to that file path.
