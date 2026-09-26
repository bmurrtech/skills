# bmurrtech/skills

Opinionated skills library for agentic coding — reusable prompts and procedures that make coding agents predictable.

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/bmurrtech/skills?style=social)](https://github.com/bmurrtech/skills)
[![Skills](https://img.shields.io/badge/skills-agent-ready-0A7.svg)](skills/)

## About

`bmurrtech/skills` is a tracked library of Agent Skills under [`skills/`](skills/). Each skill is a folder with `SKILL.md`, `agents/openai.yaml`, and optional `scripts/`, `references/`, `assets/`. Domain language lives in [`CONTEXT.md`](CONTEXT.md) and [`knowledge/`](knowledge/). ADRs live in [`docs/adr/`](docs/adr/). Local PRDs live under gitignored [`docs/prd/`](docs/about-prd.md).

## Features

| Skill | What it does |
|-------|----------------|
| [`setup-bmurrtech-skills`](skills/setup-bmurrtech-skills/) | Provision gitignore, AGENTS/CLAUDE/CONTEXT, OKF, docs scaffold |
| [`skill-create`](skills/skill-create/) | Scaffold and validate new skills under `skills/` |
| [`grill-me`](skills/grill-me/) | Design-tree interview; glossary/OKF when present |
| [`context`](skills/context/) | Maintain `CONTEXT.md` and `knowledge/` |
| [`upkeep`](skills/upkeep/) | Maintain `AGENTS.md`; ensure `CLAUDE.md` pointer |
| [`to-adr`](skills/to-adr/) | Author MADR ADRs under `docs/adr/` |
| [`to-prd`](skills/to-prd/) | Author local OKF PRDs under `docs/prd/` |
| [`tdd`](skills/tdd/) | Red-green tests at agreed seams |
| [`implement`](skills/implement/) | Universal ship-from-spec: TDD, target-repo checks, code-review |
| [`code-review`](skills/code-review/) | Two-axis Standards vs Spec review (any repo) |
| [`ascii`](skills/ascii/) | Plain-text diagrams when structure beats prose |
| [`wait-what`](skills/wait-what/) | Re-pitch in STE using glossary language |
| [`handoff`](skills/handoff/) | Temp `bmurrtech-skills-handoff-*.md` for the next agent |

## Quick start

```bash
npx skills add bmurrtech/skills
```

```bash
npx skills add bmurrtech/skills --list
```

```bash
npx skills add bmurrtech/skills --skill grill-me
```

**Alternative (curl):**

```bash
curl -fsSL "https://get.mycmd.site/bmurrtech-skills" | sh
```

Prefer reading install scripts before piping to a shell.

New repo without scaffold? After install, run **`setup-bmurrtech-skills`**.

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

- [Matt Pocock](https://github.com/mattpocock) — early inspiration for grill/TDD/review discipline (this library is first-party and does not depend on those skills).
- [MADR](https://adr.github.io/madr/) — ADR heading shape under `docs/adr/`.

## License

Apache License 2.0. See [`docs/about-license.md`](docs/about-license.md) and [`LICENSE`](LICENSE).
