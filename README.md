# bmurrtech/skills

Opinionated skills library for agentic coding — reusable prompts and procedures that make coding agents predictable.

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/bmurrtech/skills?style=social)](https://github.com/bmurrtech/skills)
[![Skills](https://img.shields.io/badge/skills-agent-ready-0A7.svg)](skills/)

## Quick start

```bash
npx skills@latest add bmurrtech/skills
```

```bash
npx skills@latest add bmurrtech/skills --list
```

```bash
npx skills@latest add bmurrtech/skills --skill grill-me
```

New repo with no scaffold? After install, run **`setup-bmurrtech-skills`**.

## How to use

Install → optional scaffold → pick a **shape** entry → record (PRD/ADR) when needed → **ship** (`implement` → `code-review`). Dashed paths are optional.

```text
+========================+
| npx skills@latest add  |
| bmurrtech/skills       |
+-----------+------------+
            |
            | [Optional] setup-bmurrtech-skills
            |            (+ docx?)
            v
+===========+=================================+
| shape: one entry                            |
|   unclear  --------> grill-me               |
|     | - - - - - - > wait-what / handoff     |
|   have target -----> (skip to ship)         |
|   scaffold only ---> (conventions ready)    |
+===========+=================================+
            |
            + - - [decision?] - - > to-adr
            + - - [product spec?] > to-prd
            |                       (ascii as needed)
            v
+========================+
| implement              |
|   prefer tdd           |
|   target-repo checks   |
|   v                    |
| code-review            |
|   v                    |
| upkeep → context [opt] |
+========================+
```

Branches, side loops, skill clusters, and maintainer notes: **[docs/how-to-bmurrtech-skills.md](docs/how-to-bmurrtech-skills.md)** — not duplicated here.

## What `setup-bmurrtech-skills` adds to *your* repo

After `npx skills add`, run **`setup-bmurrtech-skills`** in the consumer project when conventions are missing. It scaffolds agent process files (not skill folders). Idempotent; confirms before overwrite.

```text
.
├── .gitignore          # ignore .scratch/, docs/prd/, pm/, local agent dirs
├── .scratch/           # local exploratory dumps (not handoffs)
│   ├── diagrams/       # visual-explainer HTML (+ optional .md)
│   └── adr-optics/     # to-adr at-a-glance catalog HTML
├── AGENTS.md           # ops manual for agents
├── CLAUDE.md           # pointer → AGENTS.md
├── CONTEXT.md          # glossary SoT
├── knowledge/index.md  # OKF catalog stub
└── docs/
    ├── adr/index.md    # tracked ADR catalog
    └── prd/            # ignored local PRDs (authored later)
```

Optional: docx toolchain if you opt in. **What setup creates:** **[docs/skill-scaffold.md](docs/skill-scaffold.md)**. **Why:** [knowledge/skill-scaffold.md](knowledge/skill-scaffold.md). Visuals: **[docs/how-to-visual-explainer.md](docs/how-to-visual-explainer.md)**. ADRs: **[docs/how-to-adr.md](docs/how-to-adr.md)**.

## Features

| Skill | What it does |
|-------|----------------|
| [`setup-bmurrtech-skills`](skills/setup-bmurrtech-skills/) | Provision gitignore (`.scratch/` + `diagrams/` + `adr-optics/`), AGENTS/CLAUDE/CONTEXT, OKF + ADR indexes; optional docx |
| [`docx`](skills/docx/) | Create/edit Word `.docx` via pinned docx-cli; LibreOffice probe/install |
| [`visual-explainer`](skills/visual-explainer/) | Intent-routed HTML diagrams, reviews, slides under `.scratch/diagrams/` |
| [`writing-for-agents`](skills/writing-for-agents/) | Writing levers for skills and repeatable agent instructions |
| [`grill-me`](skills/grill-me/) | Design-tree interview; glossary/OKF when present |
| [`context`](skills/context/) | Maintain `CONTEXT.md` and `knowledge/` |
| [`upkeep`](skills/upkeep/) | Maintain `AGENTS.md`; ensure `CLAUDE.md` pointer |
| [`to-adr`](skills/to-adr/) | Author/supersede ADRs under `docs/adr/`; optional at-a-glance HTML |
| [`to-prd`](skills/to-prd/) | Author local OKF PRDs under `docs/prd/` |
| [`tdd`](skills/tdd/) | Red-green at seams; OKF test-maps + AGENTS index for session scope |
| [`implement`](skills/implement/) | Ship from a spec: TDD, target-repo checks, code-review |
| [`code-review`](skills/code-review/) | Two-axis Standards vs Spec review; severity + ship recommendation |
| [`ascii`](skills/ascii/) | Plain-text diagrams when structure beats prose |
| [`wait-what`](skills/wait-what/) | Re-pitch in STE using glossary language |
| [`handoff`](skills/handoff/) | Temp `bmurrtech-skills-handoff-*.md` for the next agent |

## Want AI to edit your `.docx` files?

Optional skill **`docx`**. After install, run its ensure steps (pinned docx-cli + Word/LibreOffice probe). See the skill and glossary term in [`CONTEXT.md`](CONTEXT.md).

```bash
npx skills@latest add bmurrtech/skills --skill docx
```

## Support open source

- ⭐ **Star the repo** — [![Star on GitHub](https://img.shields.io/badge/Star-on_GitHub-blue?logo=github)](https://github.com/bmurrtech/skills)
- ☕ **[Buy Me a Coffee](https://www.buymeacoffee.com/bmurrtech)** or **[Ko-fi](https://ko-fi.com/bmurrtech)**

<p align="center">
  <a href="https://www.buymeacoffee.com/bmurrtech" target="_blank" rel="noopener">
    <img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Support%20the%20project-FFDD00?style=for-the-badge&logo=buymeacoffee&logoColor=black" alt="Buy Me a Coffee">
  </a>
  <a href="https://ko-fi.com/bmurrtech" target="_blank" rel="noopener">
    <img src="https://img.shields.io/badge/Ko--fi-Support%20the%20project-FF5E5B?style=for-the-badge&logo=ko-fi&logoColor=white" alt="Ko-fi">
  </a>
</p>

## Acknowledgements

- [Matt Pocock](https://github.com/mattpocock) — grill/TDD/review discipline. This library is first-party and does not depend on those skills.
- [MADR](https://adr.github.io/madr/) — interoperable ADR spine; full authoring contract in **`to-adr`** `references/mechanics.md`.
- [Knowledge Catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main) — open-source AI-powered data and metadata catalog.
- [visual-explainer](https://github.com/nicobailon/visual-explainer) — agent skill that turns complex terminal output into styled HTML pages you actually want to read. (MIT) Ask your agent to explain architecture, review a diff, or compare requirements against a plan — self-contained HTML in the browser instead of ASCII art.

## License

Apache License 2.0. See [`docs/about-license.md`](docs/about-license.md) and [`LICENSE`](LICENSE).
