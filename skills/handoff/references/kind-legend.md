# Handoff kind legend

Closed set only. Add new rows here when introducing a kind; ship a matching
delta file under `kinds/`. Do **not** invent slugs at write time.

In the **handoff file** and glance, label kinds as **`Display (slug)`** — full
name first, slug in parentheses — so readers learn by association without a
legend. Filenames still use the slug prefix only.

| Slug | Display (use in handoff body) | Next-work signal | Overlay |
|------|-------------------------------|------------------|---------|
| `impl` | implement (`impl`) | Next session runs **`implement`** against a plan/spec | [kinds/impl.md](kinds/impl.md) |
| `cd-rvw` | code-review (`cd-rvw`) | Next session runs **`code-review`** (or applies review fixes) | [kinds/cd-rvw.md](kinds/cd-rvw.md) |
| `prd` | to-prd (`prd`) | Next session runs **`to-prd`** (create/edit) | [kinds/prd.md](kinds/prd.md) |
| `adr` | to-adr (`adr`) | Mid-session fork — ADR candidacy for later **`to-adr`** | [kinds/adr.md](kinds/adr.md) |
| `idea` | idea (`idea`) | Capture/continue under **`idea`** / `.scratch/ideas/` | [kinds/idea.md](kinds/idea.md) |
| `rd-mp` | roadmap (`rd-mp`) | Next session runs **`roadmap`** (promote/status/publish) | [kinds/rd-mp.md](kinds/rd-mp.md) |
| `vs-expl` | visual-explainer (`vs-expl`) | Next session runs **`visual-explainer`** | [kinds/vs-expl.md](kinds/vs-expl.md) |

## Match rules

1. Prefer the user’s invoke arg when it names a kind or clear next skill.
2. Else infer from aim (single clear next skill → that kind).
3. No row fits → **no kind** (base template only; filename without kind prefix).
4. Never invent a slug. Never use `generic`.

## Filename

- Kind matched: `{slug-from-legend}-{short-kebab}-{yyyyMMdd-HHmmss}.md`
- No kind: `{short-kebab}-{yyyyMMdd-HHmmss}.md`
