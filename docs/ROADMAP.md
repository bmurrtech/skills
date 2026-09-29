# Roadmap

This document captures ideas worth preserving for future exploration, refinement, or implementation.

It is intentionally **unordered and undated**. Inclusion means an idea is worth retaining—not that it is prioritized, scheduled, approved for a sprint, or ready to implement.

## Conventions

- **Ideas are not commitments.**
- **Order does not imply priority.**
- **No dates, estimates, or sprint assignments.**

---

<!-- Entries append below this rule. Do not remove the header above. -->

## Durable Debug and Regression Knowledge

**Domain:** `developer tooling / knowledge`

**Intent**  
Separate debugging and regression knowledge from general issue tracking so future coding sessions can recover relevant failure knowledge without requiring prior conversational context.

**Scope**
- Provide a dedicated `/debug` capability for capturing bugs, diagnoses, fixes, and regression knowledge.
- Publish durable debugging knowledge into `/knowledge`.
- Support relevant retrieval across fresh coding sessions (OKF-shaped progressive disclosure).
- Allow debug findings to branch into issues, PRDs, or `/handoffs` when needed.

**Boundaries**
- `/debug` is not the general issue tracker.
- Feature requests and non-bug work remain issue-management concerns.
- PRDs may consume debug findings but should not own bug tracking.
- Do not default-load historical bugs into every session context.

**Constraints**
- Historical debugging knowledge must not be loaded indiscriminately into the active context window.
- Relevant knowledge should be retrieved selectively.

**Open Questions**
- Whether OKF is the appropriate retrieval mechanism for contextual debug recall.

**Interfaces**
- GitHub: issues arising from confirmed bugs
- PRD / handoff: escalation into planned implementation work
- Knowledge: durable regression and debugging knowledge

**Notes**
- Existing bug tracking embedded in the PRD template (`to-prd` Bug Appendix) should be evaluated for extraction.

## Issue Tracking Automation (GitHub First, Fizzy Later)

**Domain:** `developer tooling / integrations`

**Intent**  
Automate issue capture and triage with GitHub as the first integration path, keeping local scratch available, and optionally syncing durable intent to self-hosted Fizzy without coupling issues to PRD ownership.

**Scope**
- GitHub Issues as primary tracked-work surface for bugs and feature requests.
- Local `.scratch` capture for pre-issue drafts.
- Breakout into related PRD sprint sessions via `/handoffs` when an issue warrants product work.
- Explicit publish path from roadmap entries to GitHub and (later) Fizzy cards.
- Leverage OKF for intelligent cross-references once debug knowledge exists.

**Boundaries**
- Issue tracker is not `/debug` — issues may be feature requests or other non-bug work.
- Fizzy/GitHub artifacts require explicit publish intent (never inferred from scratch capture or roadmap promotion).
- Does not replace `docs/ROADMAP.md` as the durable idea ledger.

**Constraints**
- GitHub path ships before Fizzy automation.
- Self-hosted Fizzy ([fizzy.do](https://www.fizzy.do/)) integration must respect separate promote vs publish commitment levels.

**Open Questions**
- How much of prior “Matt’s skills” issue automation to reuse versus rewrite against OKF.

**Interfaces**
- GitHub: Issues / Discussions
- Fizzy: self-hosted boards/cards (API/webhooks TBD)
- PRD / handoff: sprint breakouts from issues
- Knowledge: cross-links to debug/regression concepts when relevant

## Debug Context-Bloat Research and Test Spikes

**Domain:** `knowledge / OKF / evaluation`

**Intent**  
Validate that durable debug and regression knowledge can be recalled when relevant without bloating the agent context window in ordinary sessions.

**Scope**
- Research spike: map OKF (or alternative) retrieval patterns for bug/regression concepts.
- Test spike: measure or otherwise evidence that irrelevant debug knowledge stays out of default context load.
- Document findings as OKF concepts and/or ADRs before minting a full `/debug` skill.

**Boundaries**
- Spikes are not the `/debug` product skill itself.
- Spikes do not implement issue-tracker automation.

**Constraints**
- No design that requires loading the full bug corpus every session.
- Ship criteria for `/debug` must include a passing context-bloat check from these spikes.

**Interfaces**
- Knowledge: future debug/regression concepts + `knowledge/index.md` pointers
- Roadmap: pairs with Durable Debug and Regression Knowledge

## OMX Ultrawork and Ralph Library Integration

**Domain:** `agent orchestration / skills`

**Intent**  
Research and later mint library-native skills that take the best of existing OMX/host **ultrawork** (parallel high-throughput execution) and **ralph** (persistence loop until verified completion) patterns, fitted to this library’s skill shape.

**Scope**
- Research spike: inventory host/OMX ultrawork + ralph behaviors worth keeping (parallel delegation, evidence lanes, architect verification, context snapshots, deslop/regression gates).
- Design spike: map those behaviors onto `writing-for-agents` levers and this repo’s soft-gates (`implement` → `upkeep`/`context` when present).
- Future mint: `skills/ultrawork/` and `skills/ralph/` only after research settles a minimal useful contract — not before.

**Boundaries**
- Do not mint stub/placeholder skills under `skills/` for these names until research + design spikes complete.
- Do not fork OMX wholesale or treat host-local OMX installs as catalog SoT.
- Do not invent a full orchestration runtime in a first cut.

**Constraints**
- Tracked/published skills live only under `skills/`.
- Any library skill must remain lean: progressive disclosure, checkable Done when, hard Boundaries.

**Open Questions**
- Which OMX behaviors are essential vs host-specific ceremony?
- One combined orchestration skill vs separate `ultrawork` + `ralph`?

**Interfaces**
- Knowledge: future orchestration concepts when decisions settle
- Related skills (today): `implement`, `tdd`, `code-review`, `writing-for-agents`, `handoff`

**Notes**
- Key research refs (host/OMX, not library SoT): oh-my-codex / OMX **ultrawork** and **ralph** skill bodies; agent-tier / state persistence patterns those skills document.
- Sprint breakout: grill → optional PRD/handoff → mint via skill-create only after spikes.

## Release skill (tag-triggered GitHub Releases)

**Status:** Done — absorbed into **`release`** (with **`commit`** / **`merge`**); suite shipped in **0.2.0**; gates + maintenance orchestration in **0.2.1-rc1**.

**Domain:** `skills / release / CI/CD`

Shipped under `skills/release/`. Tag-triggered `v*` + filtered artifact dogfood:
ADR 0005. Remaining open questions (multi-target matrices, draft releases): see
`.scratch/ideas/release-skill.md`.
