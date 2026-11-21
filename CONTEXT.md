---
title: bmurrtech/skills
description: Domain language and entry point for the skills library knowledge bundle.
type: glossary
okf_version: "0.2"
tags: [skills, agents, glossary]
---

# bmurrtech/skills

Opinionated library of Agent Skills for agentic coding. This file is the glossary SoT. Progressive disclosure lives under [`knowledge/`](knowledge/index.md). Ops instructions for agents live in [`AGENTS.md`](AGENTS.md) — do not duplicate them here.

## Language

**Skill**:
A tracked folder under `skills/<name>/` with required `SKILL.md` and `agents/openai.yaml`, plus optional `scripts/`, `references/`, and `assets/` (omit unused dirs). The only place new skills are created or modified in this repository. Mint/modify/improve practices SoT: [knowledge/agent-skill.md](knowledge/agent-skill.md). Ops commands stay in [`AGENTS.md`](AGENTS.md).
_Avoid_: prompt pack; `.agents/skills` as SoT; skill-named dirs/symlinks at repo root (install noise); skill-folder `README.md`; empty optional dirs by default

**SKILL.md**:
The skill entry document: YAML frontmatter (`name`, `description`) plus Markdown body loaded after the skill triggers. Filename must be exactly `SKILL.md` (case-sensitive). Body: lean Workflow steps with **Done when**; disclose branch-only detail under `references/`.
_Avoid_: `skill.md` / `SKILL.MD`; stuffing always-irrelevant branches into the body

**Skill description**:
Frontmatter `description` — first progressive-disclosure level. Shape: **what + when + key capabilities** (concrete user trigger phrases; file types when relevant; ≤1024 chars; no `<` / `>`). Host uses it to decide whether to load the body.
_Avoid_: vague “helps with X”; missing triggers; internals-only jargon with no user phrases

**Skill testing**:
Behavioral red/green for a skill seam under **`tdd`**: triggering (should / should-not), functional outputs, baseline comparison vs bare prompting. Prefer one hard task first, then expand. Structural layout/frontmatter checks use `scripts/quick_validate.py`. Depth: [skills/tdd/references/skill-testing.md](skills/tdd/references/skill-testing.md).
_Avoid_: treating validate-only as proof the skill routes or executes well

**agents/openai.yaml**:
Host UI metadata (`interface`) and `policy.allow_implicit_invocation` for a skill. Required in this library; align policy with whether the skill may model-trigger.

**OKF bundle**:
A directory of Markdown concept files with YAML frontmatter, linked for progressive disclosure. Root glossary is this file; concepts live under `knowledge/`. PRDs are OKF concepts under `docs/prd/` (ignore or track via setup; this library ignores).

**CONTEXT.md**:
This glossary. Owned by the `context` skill. Not an ops manual.

**AGENTS.md**:
Agent operating manual. Owned by `upkeep`. May link here; must not restate glossary definitions.

**CLAUDE.md**:
Repo file whose entire body is exactly `AGENTS.md`.

**ADR**:
Tracked decision under `docs/adr/NNNN-ADR-<slug>.md`, indexed by `docs/adr/index.md`. **Published** Accepted = immutable (change via supersede); **in-flight** (not yet on remote default) may be edited in place. Authoring SoT ships in **`create-adr`** (`references/mechanics.md`); library OKF only summarizes. Rebuildable slim **decision catalog** at `docs/adr/catalog.json`; local glance under `.scratch/adr-optics/`.

**create-adr** (skill):
Author, in-place-edit (in-flight), or supersede (published Accepted) under `docs/adr/`; classify cited priors; update `docs/adr/index.md`; rebuild slim `catalog.json` and optional `.scratch/adr-optics/` glance. How-to: [docs/how-to-adr.md](docs/how-to-adr.md). Gate SoT: [`skills/create-adr/SKILL.md`](skills/create-adr/SKILL.md).
_Avoid_: editing published Accepted ADRs in place; treating Status=Accepted alone as published; PRD/feature scope inside an ADR

**create-prd** (skill):
Author OKF-shaped PRDs under `docs/prd/` (ignore or track per setup). Cite tracked ADRs; use **`ascii`** for structure diagrams. Durable “why” stays in **`create-adr`**.
_Avoid_: stack/architecture rationale in the PRD body

**Decision catalog**:
Rebuildable JSON for one ADR home (`docs/adr/catalog.json`, `schema_version` 2). Source Markdown stays authoritative. Slim tracked cache (no full bodies); fat copy under `.scratch/adr-optics/` only for the at-a-glance HTML.
_Avoid_: treating catalog.json as SoT; standup/discovery `catalog` senses; mixing project keys into one file

**Decision lineage**:
DAG of supersession only among ADRs in one home. Ordinary links and git history are not edges. Glance **Previous** walks a predecessor; **Next** pops a return stack (not “the successor”).
_Avoid_: edge-strength field; encoding relate/PRD links as lineage

**How-to doc**:
Library consumer guide under `docs/how-to-<topic>.md` (e.g. `how-to-bmurrtech-skills`, `how-to-adr`, `how-to-visual-explainer`). Install/scaffold lives in the main skills how-to; topic how-tos are prompts + scope only.
_Avoid_: `how-to-use-…` naming; duplicating setup into every topic how-to; scaffolding library how-tos into consumers


**.scratch/**:
Gitignored local scratch pad for exploratory, pre-PRD, and other agent artifact dumps related to these skills. Includes `.scratch/visuals/` for default **visual-explainer** HTML (optional Markdown companions; durable team/commit visuals → tracked `docs/visuals/`), `.scratch/adr-optics/` for **`create-adr`** at-a-glance HTML + fat `adr-catalog.json` (tracked slim catalog stays `docs/adr/catalog.json`), `.scratch/doop/` for **`doop`** session sidecars (canvas URL/id + meeting notes; Doop DB stays in the Doop install `data/`), `.scratch/handoffs/` for **kept** (non-transitory) **`handoff`** docs, and `.scratch/ideas/` for **`idea`** brain dumps (promote only via **`roadmap`**). Default handoffs are throwaway under the OS temp dir; only an explicit keep signal lands under `.scratch/handoffs/`.
_Avoid_: committing scratch; using tracked `docs/` for throwaways; `/pm/diagrams` or harness skill dirs as visual SoT; writing default handoffs into the repo; treating scratch ideas as roadmap or tracker commitments; treating Doop `data/` as a consumer-repo path

**handoff** (skill):
Writes one markdown file so a fresh agent can continue without this chat. The file is the brief you point at later — full detail lives there. **Aim:** optional invoke arg when present; else infer. If ≥2 plausible next aims and no arg, one short ask before write. After write, a brief in-chat at-a-glance (path + temp|keep, intent + kind as Display (slug) or none, next action, 2–4 check bullets, reprompt-if-wrong cue) — not a dump of the file. **What travels in the file:** next action, acceptance/constraints/verdict, and session facts the next skill needs. Long specs/plans/ADRs stay path refs (hybrid). **What does not:** “see this chat” as the only carrier of a fact. Irrelevant history stays out. Temp by default; **keep** / clear persist intent → `.scratch/handoffs/`. Shape: `references/handoff-base.md` + optional kind overlays; legend in `references/kind-legend.md`. Name: `{kind}-{slug}-{yyyyMMdd-HHmmss}.md` when a closed kind matches; else `{slug}-{yyyyMMdd-HHmmss}.md`. Decision: [ADR 0012](docs/adr/0012-ADR-handoff-hybrid-kinds.md).
_Avoid_: `bmurrtech-*-handoff-*` prefixes; inventing kind slugs; `generic` kind; pasting full specs; transcript-only pointers; pasting the full handoff into chat; default writes into the repo; hard facts about repo state with no re-verify cue; skipping the post-write glance; asking before write when aim is already clear

**Handoff kind**:
Closed slug from `kind-legend.md` (filename prefix + machine id). In the handoff **body** and glance, write **Display (slug)** — e.g. code-review (`cd-rvw`) — so readers need no legend. No match → base only, title/slug filename, no invented kind. **`adr`**: fork — put ADR candidacy in the handoff; run **`create-adr`** in a separate session. Handoff never authors the ADR/PRD.
_Avoid_: open-ended kind invention; catch-all `generic`; full-template copies per kind; drafting ADR/PRD bodies inside `handoff`; slug-only kind labels in the handoff body or glance; kind abbreviations alone in how-to diagrams

**ROADMAP.md**:
Tracked durable idea ledger under `docs/ROADMAP.md`. Unordered and undated; inclusion ≠ priority or sprint commitment. Owned by **`roadmap`** (promote / publish). Raw thoughts stay in `.scratch/ideas/` via **`idea`** until explicitly promoted.
_Avoid_: dates/estimates/sprint assignments in the ledger; implicit promote or publish; using ROADMAP as the issue tracker

**idea** / **roadmap** (skills):
Capture-local vs durable-intent vs tracked-work commitment levels — **`idea`** preserves first under `.scratch/ideas/`; **`roadmap`** promotes into `docs/ROADMAP.md` and publishes to GitHub/Fizzy only on separate explicit intent.
_Avoid_: collapsing capture/promote/publish into one step; inventing roadmap fields to fill the template

**Test map**:
OKF concept (`type: test-map`) under `knowledge/` naming a seam, the smallest run command, and tracked test paths. Indexed by a one-liner in `AGENTS.md` so agents load only session-relevant tests.
_Avoid_: dumping the whole `tests/` tree into context each session

**grill-me**:
Design-tree interview in frontier rounds; after frontier empty, A/B/C route (**A** `create-prd` recommended, **B** `handoff`→implement, **C** bare `Go`); updates glossary via `context`; warrants ADRs via `create-adr`.

**upkeep** / **context** (skills):
Ops manual vs glossary/OKF ownership — never cross-edit.

**Skill scripts vs LLM**:
Library rule for optional `skills/<name>/scripts/`: LLM for judgment; scripts for cheap deterministic work (formula, sort, validate, compress) when total tool cost or exactness beats letting the model do it. Depth: [knowledge/skill-scripts.md](knowledge/skill-scripts.md).
_Avoid_: smart/semantic scripts; scripting trivial arithmetic; dumping full computational traces into context

**discovery** (skill):
User-invoked business-analysis skill for solution creators: turn meetings, transcripts, or notes into evidence-scored use cases ranked P0–P3. Modes: prep → capture → brief → rank. Not sector-specific; not PRD/ADR/tickets/intake (point at those skills). Depth: [knowledge/discovery.md](knowledge/discovery.md); how-to: [docs/how-to-discovery.md](docs/how-to-discovery.md).
_Avoid_: inventing people, emails, or bands; solution design during discovery; stuffing raw transcripts into the committed bundle; department jargon as schema

**summarize-transcript** (skill):
User-invoked skill that turns an already-provided transcript into retained-signal Markdown (*core summary*, themes, takeaways; optional stance / decisions / actions / evidence). Long input uses host-LLM map-reduce via assess/chunk scripts. Not transcription from audio/video; not a discovery brief.
_Avoid_: inventing owners/dates; valence mood scores; marketing publish packs; calling external LLM APIs

**Discovery OKF bundle**:
One OKF v0.2 bundle per team at `docs/discovery/<team>/` (root `index.md` with `okf_version` only; concepts `Capture` / `UseCase` / `Ranking` carry `type`; optional rebuildable `catalog.json` cache). Project is optional frontmatter, not a nested bundle. Parent `docs/discovery/index.md` lists teams only. May hold personal/client-confidential fields (names, emails, titles, pain points, sentiment, stack) — setup **Commit discovery records?** A ignore (default) / B track; B → keep repo private. This library **A**. Pattern mirrors PRD A/B ([ADR 0013](docs/adr/0013-ADR-prd-tracking-choice.md)); no separate ADR yet.
_Avoid_: per-project OKF roots; type subtrees as required layout; treating `catalog.json` as SoT; defaulting to track; public repos on B

**Discovery priority formula**:
KPFS bands 1–3 (or unscored). BV = (K+P)/6×100; DR = (F+S)/6×100; Overall = 0.4·BV + 0.6·DR → P0 ≥ 80 · P1 ≥ 65 · P2 ≥ 50 · P3 < 50. Any unscored dimension → priority none + needs-discovery. F = weakest area; S needs sponsorship for a 3. Generic blockers lower a band; they never suppress priority. LLM assigns bands; script applies the math. Timing/reuse are unscored notes.
_Avoid_: defaulting unknowns to a band; hand-computing Overall; client-specific gates; hiding BV behind Overall

**writing-for-agents**:
Standalone guidance for writing skills and other agent instructions so behaviour is repeatable across LLMs. Owns levers: context pointers, two loads, information hierarchy, completion criteria, leading words, negative-imperative guardrails, pruning. Skill mechanics (layout, description examples, body template), workflow **patterns**, and packaging **troubleshooting** live under its `references/`. Soft-skips skill validators when absent. Does not own ops-manual create/maintain. Library mint/modify SoT still summarized in [knowledge/agent-skill.md](knowledge/agent-skill.md).
_Avoid_: flattening levers into unnamed checklist vibes; treating this as upkeep for ops manuals; soft bans where a hard Boundaries line is required

**writing-for-humans**:
Mode-route human-facing writing by function: STE-inspired **Instructions**, slop-aware **Prose**, or **Mixed**. Jobs: Generate / Edit / Detect. Optional **controlled** overlay is this skill’s owned strict procedural English — not official ASD-STE100. Quality check uses measure-only `writing_for_humans_linter.py` (compact `agent_summary` STOP/REVISE_ONCE + `revision_budget`); LLM judges material vs cosmetic — script never rewrites.
_Avoid_: claiming official ASD-STE100 compliance; treating word-count thresholds as hard rewrite orders; more than one lint-driven revision without a new substantive defect; STE/controlled flattening of essays/creative prose

**Context pointer**:
Always-loaded reference that names out-of-context material and encodes when to reach it (skill `description`, always-on instruction line). Wording decides reach reliability; weak wording on a must-have target is a variance bug.
_Avoid_: treating the target path as the trigger; stuffing identity the body already carries

**Leading word**:
Compact pretrained token the agent thinks with while running a document (*tight*, *red*). Recruits priors; repeats as a token, not a sentence. Anchors execution in the body and invocation in pointers.
_Avoid_: coining words with no prior; restating the same idea as a phrase in three places

**setup-bmurrtech-skills**:
Idempotent provision of gitignore (incl. `.scratch/`), `.scratch/` + `.scratch/visuals/` + `.scratch/adr-optics/`, tracked `docs/visuals/`, AGENTS/CLAUDE/CONTEXT, knowledge stub, docs/adr index; **Commit PRDs?** A ignore (default) / B track ([ADR 0013](docs/adr/0013-ADR-prd-tracking-choice.md)); **Commit discovery records?** A ignore (default) / B track (private-repo recommend; ref `discovery-tracking.md`); optional **`docx`**; optional **Donation CTA** (default no; re-ask on re-run). Does not install skill folders into harnesses (that is `npx skills`) and does not copy library how-tos / explainers into the consumer. Does not pre-create `.scratch/handoffs/` — **`handoff`** creates it on **keep**. Tree: [docs/skill-scaffold.md](docs/skill-scaffold.md); why: [knowledge/skill-scaffold.md](knowledge/skill-scaffold.md).

**Donation CTA**:
Optional setup choice to scaffold repo funding surfaces: `.github/FUNDING.yml`, a README **Support this Repo** section (badges + links), and matching `CONTEXT.md` glossary entries for the chosen platforms/URLs. Default **no**; re-ask on every setup run. This OSS library keeps its own README heading **Support open source**. Decision: [ADR 0015](docs/adr/0015-ADR-donation-cta-changelog-release-notes.md).
_Avoid_: inventing non-GitHub funding filenames; forcing CTAs on private/internal repos without asking; using “Support open source” wording in non-OSS consumer scaffolds

**FUNDING.yml**:
GitHub-recognized funding file at `.github/FUNDING.yml` (Sponsors sidebar). Preferred platforms here: Ko-fi + Buy Me a Coffee usernames; other keys left empty unless the operator supplies them. This library: `ko_fi` / `buy_me_a_coffee` → `bmurrtech`.
_Avoid_: `CTA.yaml` or other nonstandard names GitHub ignores

**Release notes (CHANGELOG extract)**:
GitHub Release body built by extracting the matching dated `## [<version>]` section from `CHANGELOG.md`, plus a short install/artifact blurb and an optional Donation CTA footer when funding context exists. Owned by the tag-triggered release workflow (and the same pattern in **`release`** bootstrap scaffolds). SoT script: `skills/release/scripts/changelog_release_notes.py` (this library’s CI calls it in-place; bootstrap copies it into consumer `scripts/`). Decision: [ADR 0015](docs/adr/0015-ADR-donation-cta-changelog-release-notes.md).
_Avoid_: hardcoded stub release bodies that ignore CHANGELOG; competing `gh release create` notes when the workflow owns publication; a second ops copy under repo `scripts/`

**visual-explainer**:
Lean Agent Skill that turns architectures, diffs, plans, tables, and related intent into self-contained HTML. Default **`.scratch/visuals/`**; tracked **`docs/visuals/`** on durable cues (team/group/commit/docs). Resolves mode then home; unclear mode or help → suggest once from content. Modes: diagram, visual-plan, slides, diff-review, plan-review, project-recap, fact-check. Optional AI-readable Markdown companion (same basename, same home) only when requested; ask before replace. [ADR 0014](docs/adr/0014-ADR-visual-explainer-homes.md). Inspired by [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) (MIT); no Pi/MCP/PPTX bundle in this remake.
_Avoid_: ASCII/box-drawing as the primary artifact when this skill is loaded; writing visuals under `/pm/` or agent install dirs; treating the `.md` companion as HTML source; asking mode when the ask already names slides/diff/plan-review/etc.

**Deck shell** (visual-explainer slides):
Frozen HTML/CSS/JS that owns deck mechanics. Keeps `100dvh` scroll-snap; shell patches include print-to-PDF CSS, 1-indexed `data-screen-label`, Esc overview, optional speaker-notes hook, plus existing nav/counter/localStorage. The model fills slide `<section>`s and theme tokens — it does not rewrite the shell.
_Avoid_: regenerating SlideEngine / nav / scaling per deck; treating the reference deck as copy-paste of the whole file including engine; fixed-canvas letterbox rewrite this cycle

**Action-title outline** (visual-explainer slides):
Before slide bodies: the full deck as an ordered list of action titles (takeaway sentences, not topic labels). Titles alone must read as a coherent story (chat-only unless the user asks a file); then a per-slide **visual pattern** map (concept → `vx-*` pattern from the skill catalog) and bodies fill in (auto-continue unless interrupted). Frame classes (title / divider / statement / …) hold the slide; patterns (funnel, quadrant, merge, proportion, calculator, scale, pills, …) hold the visual. Free-form OK with a one-line why. Sans-default type; expressive display only when asked. Surf/raster only on ask or supplied brand assets. Deliver only after `check_slides` is green.
_Avoid_: topic-label titles (“Customer Sentiment”); writing HTML before the title story and pattern map exist; hard-gating every outline for user OK by default; proactive surf; shipping a deck with a failing checker; domain-specific nouns in frozen skill refs (placeholders only)

**doop** (skill, local-only):
Experimental localhost Doop canvases for business-process and present-state architecture diagrams via MCP. **Not shipped** in the product catalog while `skills/doop/` is gitignored (kept on disk for library dogfood). Session sidecars → **`.scratch/doop/`**; canvas data stays in the Doop install. Not UI mockups (prefer **visual-explainer** / raw Doop) and not ascii-only Markdown diagrams (**`ascii`**).
_Avoid_: treating doop as a published skill; Doop Agent Settings as primary path; skill-owned export/graduate; treating Doop `data/` as a repo path

**docx**:
Word `.docx` via pinned **docx-cli** on PATH (operator-installed; pin **0.26.0**). Skill probes version/pin and prints OS-specific **manual** prereq commands on failure — does not download or auto-install CLI/office. Install how-to: [docs/how-to-docx-cli.md](docs/how-to-docx-cli.md). Word or LibreOffice required for render/import. Prefer **`ensure_toolchain`** façade; cores remain `ensure_docx` / `ensure_office`. **ToolchainReady** is the typed evidence report (pin ok ∧ office ready). DIGESTS = operator verify for the pin only. Posture: [ADR 0011](docs/adr/0011-ADR-skill-scanner-posture-prereqs.md). Optional **themes** (professional / technical / editorial) restyle create output — kits under `skills/docx/references/themes/`; not domain templates.
_Avoid_: agent binary download; `--install` in skill scripts; auto sudo / package-manager install; npx upstream skill install; attack-demo phrases in SKILL.md; inventing ad-hoc brand palettes when a named theme fits

**Universal sprint skill**:
Portable skill for any consumer repo: **`implement`**, **`code-review`**, **`tdd`**, plus soft-coupled **`grill-me`** / **`wait-what`** / **`handoff`**. Validation means the *target* repo’s checks; `upkeep`/`context` run only when installed and those artifacts exist. **`tdd`** covers code seams **and** Agent Skill seams (triggering / functional / baseline — [Skill testing](#skill-testing)). **`implement`** owns build + soft housekeeping (and apply-on-write agent bars when editing skills) and exits via fresh-context review (subagent **`code-review`** or **`handoff`** for code-review); it never stages/commits/pushes — Git is **`commit`** / **`merge`** / **`release`**. **`code-review`** judges only (never calls **`implement`**): gated **`tdd`** load + smallest evidence-run; path-gated agent-artifacts lens; Spec defaults to local diff + local Spec paths (no default tracker/`gh` fetch — [ADR 0011](docs/adr/0011-ADR-skill-scanner-posture-prereqs.md)).
_Avoid_: requiring `quick_validate.py` for ordinary app/lib work; assuming every consumer is a skills monorepo; default issue-body fetch in code-review; treating Git publish as part of **`implement`**; nesting **`implement`** inside **`code-review`**; loading agent-artifacts / **`tdd`** on every review when the gate is false

**Library-specific skill**:
Opinionated for this library (or repos that opted into the convention): **`writing-for-agents`**, **`writing-for-humans`**, **`discovery`**, **`setup-bmurrtech-skills`**, **`docx`**, **`visual-explainer`**, **`create-prd`** / **`create-adr`** homes, **`upkeep`** / **`context`** as glossary/ops maintainers. Local-only experimental **`doop`** is gitignored under `skills/doop/` until stable-ready.
_Avoid_: shipping library layout rules inside universal sprint skills

**Skills release artifact**:
Versioned install tarball of `skills/` + `LICENSE` only. Library `knowledge/` / `CONTEXT.md` / ops / docs stay **tracked** in git but are **excluded** by packaging (`scripts/package_skills.py`). Do not gitignore library OKF to keep consumer installs clean.
_Avoid_: shipping full-repo trees as the install artifact; overlaying library OKF onto consumer roots

**Git lifecycle**:
Composable skills **`commit`** / **`merge`** / **`release`** (catalog group in `skills.sh.json`, README, how-to): durable local change + optional review-branch/PR; integrate a chosen PR under GitHub-enforced gates; prove repo-native build contract then deliberate `v*` tag (existing contract > ecosystem defaults; this library dogfoods ADR 0005). **`commit`** orchestrates maintenance (**`upkeep`** always when applicable; **`roadmap`** status when ledger impact); under `release_intent`, **`commit`** / **`release`** require **`upkeep`** release-cut then **CHANGELOG verify** before stage/commit/push/tag; **`release`** owns version/channel intent + gates, not file mutation; **`merge`** never mutates a reviewed head for missing maintenance.
_Avoid_: one mega-git skill; default push without intent; inventing merge gates beyond GitHub policy; naming **`code-review`** inside **`merge`**; tagging in the same run as first release-workflow bootstrap; alternate packaging when `package_skills.py` + tag workflow exist; inventing version outside the gate table; skipping upkeep or CHANGELOG verify on release cuts

**Version gate** / **publication gate**:
Two deliberate `release` confirmations — authorize version+channel (channel-preserving **recommend** is the default when no override), then authorize exact tag@SHA after validate. Procedure: `skills/release/references/`.
_Avoid_: one overloaded “OK to release?”; treating branch push as publication; inventing versions outside the recommend table; skipping the gate when nothing was stated

**Release context**:
Structured handoff from `release` → `commit`/`upkeep` after the version gate (`release_intent` marks a cut). Field schema: `skills/release/references/version-gate.md`. Soft-skip vs hard-stop + **CHANGELOG verify**: `skills/commit/references/maintenance.md`.
_Avoid_: promoting Unreleased→dated outside `upkeep`; inventing version in `commit`; treating soft “dated somehow” as enough without verify evidence

## Hard rules

1. **Tracked/published skills live only in `skills/`.** Library-local skills may sit under ignored `.agents/skills/` (host-readable; not product; not OKF; not release). Skill-named paths at **repo root** are not SoT (install noise) — never dual-track.
2. **No glossary/ops duplication.** Skill mint/modify/improve **practices** live in [knowledge/agent-skill.md](knowledge/agent-skill.md) + glossary terms above; `AGENTS.md` keeps commands and points here — do not paste the essay into ops.
3. **`docs/prd/` policy** — setup A/B ([ADR 0013](docs/adr/0013-ADR-prd-tracking-choice.md)); this library **A**. Ops bullets in `AGENTS.md`. ADRs stay tracked.
4. **`docs/discovery/` policy** — setup A/B (default ignore; B = private repo); this library **A**. Discovery skill does not own gitignore warnings. ADRs stay tracked.
5. **Release artifacts exclude library OKF/ops/docs** — filter at package time; keep `knowledge/` tracked.

Post-`implement`/`code-review` housekeeping lives in [`AGENTS.md`](AGENTS.md) Boundaries — not restated here.

## See also

- [knowledge/index.md](knowledge/index.md)
- [knowledge/agent-skill.md](knowledge/agent-skill.md) — mint / modify / improve skills
- [docs/adr/index.md](docs/adr/index.md)
- [docs/ROADMAP.md](docs/ROADMAP.md)
- [docs/how-to-bmurrtech-skills.md](docs/how-to-bmurrtech-skills.md)
- [AGENTS.md](AGENTS.md)
