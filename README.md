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

After install, run **`setup-bmurrtech-skills`** when conventions are missing. It scaffolds agent process files (not skill folders) — tree and whys:
**[docs/skill-scaffold.md](docs/skill-scaffold.md)** · [knowledge/skill-scaffold.md](knowledge/skill-scaffold.md).

Also: [docs/how-to-visual-explainer.md](docs/how-to-visual-explainer.md) · [docs/how-to-adr.md](docs/how-to-adr.md) · [docs/ROADMAP.md](docs/ROADMAP.md).

## Features

Short index only — when/how for each skill:
**[docs/how-to-bmurrtech-skills.md](docs/how-to-bmurrtech-skills.md#skill-registry)**.

| Skill | What it does |
|-------|----------------|
| [`setup-bmurrtech-skills`](skills/setup-bmurrtech-skills/) | Scaffold AGENTS/CONTEXT/`.scratch`/ADR home |
| [`grill-me`](skills/grill-me/) | Design-tree interview to shared understanding |
| [`to-prd`](skills/to-prd/) | Local OKF PRD under `docs/prd/` |
| [`to-adr`](skills/to-adr/) | Tracked ADR under `docs/adr/` |
| [`implement`](skills/implement/) | Spec → TDD → checks → code-review |
| [`tdd`](skills/tdd/) | Red-green at agreed seams |
| [`code-review`](skills/code-review/) | Standards ‖ Spec review + ship call |
| [`handoff`](skills/handoff/) | Compact for a fresh agent (temp or keep) |
| [`idea`](skills/idea/) | Scratch brain dump under `.scratch/ideas/` |
| [`roadmap`](skills/roadmap/) | Promote ideas → [docs/ROADMAP.md](docs/ROADMAP.md) |
| [`wait-what`](skills/wait-what/) | STE re-pitch when explanation failed |
| [`ascii`](skills/ascii/) | Plain-text structure diagrams |
| [`visual-explainer`](skills/visual-explainer/) | HTML diagrams/reviews under `.scratch/diagrams/` |
| [`upkeep`](skills/upkeep/) | AGENTS / CLAUDE / CHANGELOG Unreleased |
| [`context`](skills/context/) | CONTEXT.md + knowledge OKF |
| [`writing-for-agents`](skills/writing-for-agents/) | Levers for agent-facing instructions |
| [`docx`](skills/docx/) | Word `.docx` via pinned docx-cli |

## Roadmap

Future exploration lives in **[docs/ROADMAP.md](docs/ROADMAP.md)** — unordered ideas, not a sprint plan or commitment queue.

**Have an idea or improvement?** [Open a GitHub issue](https://github.com/bmurrtech/skills/issues/new) — bugs, feature requests, and skill suggestions welcome.

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
