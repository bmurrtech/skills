# bmurrtech/skills

Opinionated skills library for agentic coding: reusable prompts and procedures that make coding agents predictable.

Built around [Open Knowledge Format (OKF)](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing): a vendor-neutral, agent- and human-friendly way to keep project metadata, context, and curated knowledge portable across tools and sessions.

- Progressive disclosure = token efficiency: agents load only the concepts they need, not the entire wiki, delivering the benefits of RAG without window bloat or text embedding pipelines
- Shared language and knowledge live in the repo (`CONTEXT.md` + `knowledge/`), never trapped in transient chat history
- Unified OKF shape for glossary, local PRDs, and test maps means skills compose cleanly without custom glue

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/bmurrtech/skills?style=social)](https://github.com/bmurrtech/skills)
[![skills.sh](https://skills.sh/b/bmurrtech/skills)](https://skills.sh/bmurrtech/skills)

## Quick start

```bash
npx skills@latest add bmurrtech/skills --list
npx skills@latest add bmurrtech/skills
```

`--list` shows what the CLI finds before you install. To take everything without the picker, use `--all`. To take one skill:

```bash
npx skills@latest add bmurrtech/skills --skill grill-me
```

A full GitHub URL or a path into a skill folder works too.

New repo with no scaffold? After install, run **`setup-bmurrtech-skills`**.

### Update installed skills

After a new release of this pack, refresh from **`bmurrtech/skills`**:

```bash
npx skills@latest add bmurrtech/skills --all
```

That reinstalls every skill in this repo (not every skill on your machine). Scope with `-g` (global) or omit for project. Named skills only: `npx skills@latest update grill-me to-prd` (`-p` / `-g` / `-y` still apply to `update`).

## How to use

Default cycle after install:

```text
setup-bmurrtech-skills [if needed]
        |
        v
     grill-me
        |
        +-- [decision?] --> to-adr
        |
        v
      to-prd
        |
        v
     implement  (+ tdd)
        |
        v
      handoff  -->  code-review   [fresh agent; recommended]
```

Flows, branches, and every skill: **[docs/how-to-bmurrtech-skills.md](docs/how-to-bmurrtech-skills.md)**.

## What `setup-bmurrtech-skills` adds to *your* repo

```text
.
├── .gitignore              # patched: ignore local-only paths below
├── .scratch/               # created on disk; gitignored
│   ├── diagrams/           # visual-explainer HTML (+ optional .md companions)
│   ├── adr-optics/         # to-adr at-a-glance catalog HTML
│   └── ideas/              # idea brain dumps (on demand; promote via roadmap)
├── AGENTS.md               # agent ops manual
├── CLAUDE.md               # body is exactly: AGENTS.md
├── CONTEXT.md              # glossary SoT (OKF root)
├── knowledge/
│   └── index.md            # OKF catalog stub → CONTEXT + concepts
└── docs/
    ├── adr/
    │   └── index.md        # empty ADR catalog (tracked decisions home)
    └── prd/                # usually not created as files yet; path ignored
```

Tree and whys: **[docs/skill-scaffold.md](docs/skill-scaffold.md)** · [knowledge/skill-scaffold.md](knowledge/skill-scaffold.md). Also: [docs/how-to-visual-explainer.md](docs/how-to-visual-explainer.md) · [docs/how-to-adr.md](docs/how-to-adr.md) · [docs/ROADMAP.md](docs/ROADMAP.md).

## Features

### Bootstrap

| Skill | What it does | Example prompt |
|-------|----------------|----------------|
| [`setup-bmurrtech-skills`](skills/setup-bmurrtech-skills/) | Drops AGENTS, CONTEXT, `.scratch/`, and an ADR home into your repo | `Run setup-bmurrtech-skills on this repo` |
| [`docx`](skills/docx/) | Edit Word `.docx` via pinned docx-cli (operator-installed) | `Fill this contract template with the docx skill` |

### Shape and record

| Skill | What it does | Example prompt |
|-------|----------------|----------------|
| [`grill-me`](skills/grill-me/) | Interviews you until the design tree is resolved | `Grill me on this auth redesign before we code` |
| [`to-prd`](skills/to-prd/) | Writes a local sprint PRD under `docs/prd/` | `Turn that grill into a PRD for the MVP` |
| [`to-adr`](skills/to-adr/) | Records a tracked ADR under `docs/adr/` | `Write an ADR for picking Postgres over SQLite` |
| [`ascii`](skills/ascii/) | Draws structure as plain text in the terminal | `ASCII the request path through the API gateway` |
| [`visual-explainer`](skills/visual-explainer/) | Builds HTML diagrams under `.scratch/diagrams/` | `Visual explainer for this architecture diff` |
| [`writing-for-agents`](skills/writing-for-agents/) | Tightens skills and other agent-facing docs | `Rewrite this SKILL.md with writing-for-agents` |

### Ship

| Skill | What it does | Example prompt |
|-------|----------------|----------------|
| [`tdd`](skills/tdd/) | Red-green loops at seams you agree on first | `TDD the invoice total calculator at this seam` |
| [`implement`](skills/implement/) | Turns a spec into working code, with TDD and a review pass | `Implement the PRD; prefer tdd at the seams we listed` |
| [`code-review`](skills/code-review/) | Standards and Spec review with a ship call | `Code-review the diff since main` |

### Git lifecycle

| Skill | What it does | Example prompt |
|-------|----------------|----------------|
| [`commit`](skills/commit/) | Local-first commit; push/PR only on intent | `Commit this` · `Commit and push this` · `Push this directly to main` |
| [`merge`](skills/merge/) | Integrate a chosen PR under GitHub gates | `Merge PR #42` |
| [`release`](skills/release/) | Build-before-tag; push one `v*` tag | `Release 0.2.0` |

Defaults and overrides: **[how-to](docs/how-to-bmurrtech-skills.md#git-lifecycle)**.

### Session hygiene / ideas

| Skill | What it does | Example prompt |
|-------|----------------|----------------|
| [`handoff`](skills/handoff/) | Packs the session for a fresh agent (temp file, or keep under `.scratch/handoffs/`) | `Handoff this session; keep it under .scratch` |
| [`idea`](skills/idea/) | Parks a brain dump under `.scratch/ideas/` without promoting it | `Capture this idea; don't work on it now` |
| [`roadmap`](skills/roadmap/) | Moves durable ideas into [docs/ROADMAP.md](docs/ROADMAP.md) | `Promote that scratch idea onto the roadmap` |
| [`wait-what`](skills/wait-what/) | Re-explains when the last message did not land | `Wait-what; re-pitch that last explanation` |
| [`upkeep`](skills/upkeep/) | Keeps AGENTS, the CLAUDE pointer, and CHANGELOG Unreleased honest | `Run upkeep after that layout change` |
| [`context`](skills/context/) | Maintains `CONTEXT.md` and the `knowledge/` OKF | `Update CONTEXT for the new billing terms` |

## Want AI to edit your `.docx` files?

### Prerequisites

- **`docx`:** install [docx-cli](https://github.com/kklimuk/docx-cli) yourself at the skill pin (**0.26.0**), plus Word or LibreOffice for render/import. Agents only probe PATH — see **[docs/how-to-docx-cli.md](docs/how-to-docx-cli.md)**.

Optional skill **`docx`**. Install the CLI yourself (pin **0.26.0**), then probe with `ensure_toolchain.py`. Word/LibreOffice stay a manual prerequisite for render/import. How-to: **[docs/how-to-docx-cli.md](docs/how-to-docx-cli.md)**. Residual risk: [docs/accepted-risk.md](docs/accepted-risk.md).

```bash
npx skills@latest add bmurrtech/skills --skill docx
```

## Roadmap

Future exploration lives in **[docs/ROADMAP.md](docs/ROADMAP.md)**: unordered ideas, not a sprint plan or commitment queue.

**Have an idea or improvement?** [Open a GitHub issue](https://github.com/bmurrtech/skills/issues/new). Bugs, feature requests, and skill suggestions welcome.

## Support open source

- ⭐ **Star the repo** ([![Star on GitHub](https://img.shields.io/badge/Star-on_GitHub-blue?logo=github)](https://github.com/bmurrtech/skills))
- ☕ **[Buy Me a Coffee](https://www.buymeacoffee.com/bmurrtech)** or **[Ko-fi](https://ko-fi.com/bmurrtech)**

<p align="center">
  <a href="https://www.buymeacoffee.com/bmurrtech" target="_blank" rel="noopener"><img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Support%20the%20project-FFDD00?style=for-the-badge&logo=buymeacoffee&logoColor=black" alt="Buy Me a Coffee"></a><!--
  --><a href="https://ko-fi.com/bmurrtech" target="_blank" rel="noopener"><img src="https://img.shields.io/badge/Ko--fi-Support%20the%20project-FF5E5B?style=for-the-badge&logo=ko-fi&logoColor=white" alt="Ko-fi"></a>
</p>

## Acknowledgements

- [Matt Pocock](https://github.com/mattpocock): grill/TDD/review discipline. This library is first-party and does not depend on those skills.
- [MADR](https://adr.github.io/madr/): interoperable ADR spine; full authoring contract in **`to-adr`** `references/mechanics.md`.
- [Knowledge Catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main): open-source AI-powered data and metadata catalog.
- [visual-explainer](https://github.com/nicobailon/visual-explainer): agent skill that turns complex terminal output into styled HTML pages you actually want to read. (MIT) Ask your agent to explain architecture, review a diff, or compare requirements against a plan. You get self-contained HTML in the browser instead of ASCII art.
- [kklimuk/docx-cli](https://github.com/kklimuk/docx-cli): CLI for AI agents (Claude, Codex) to read, edit, and comment on `.docx` files with full format fidelity. (MIT)

## License

Apache License 2.0. See [`docs/about-license.md`](docs/about-license.md) and [`LICENSE`](LICENSE).
