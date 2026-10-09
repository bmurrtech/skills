---
name: discovery
description: >
  Discovery for solution creators: turn meetings, transcripts, or notes into
  ranked use cases and requirements (pain → map → prioritize → requirements →
  recap → reassess). Use on initial / pain / kickoff; map the pains; follow up /
  prioritize / which first; requirements / good enough / POC / MVP; recap /
  score / rank; rerank / re-score / things changed; recall last decision. Not
  for PRD, ADR, tickets, or roadmap authoring.
disable-model-invocation: true
---

# discovery

Business-analysis aid for **solution creators**. Fewer, higher-value
opportunities. Stay on the problem until value and constraints are clear.
Do not pitch a solution early. Stakeholder name stays blank for a human.

## Boundaries

- Do **not** fill the **Stakeholder:** line (even if a transcript names someone).
- Do **not** copy raw transcripts into the committed bundle — cite a local path.
- Do **not** author PRDs, ADRs, tickets, or roadmap entries — point at
  **`to-prd`**, **`to-adr`**, or **`roadmap`**.
- Do **not** run a requirements workshop on the first pain meeting.
- Do **not** invent KPI numbers or clear gates with assumptions.
- Do **not** treat department jargon as the schema — keep field names generic.
- Do **not** ask twenty questions — one highest-value missing ask when thin.

## Workflow

### 1. Route cycle + team home

Infer cycle from the ask + bundle evidence:

| Signal | Cycle | Load |
|--------|-------|------|
| `new`, initial, pain, kickoff; no pains on file | Initial | [pain-point-finder-template.md](references/pain-point-finder-template.md) |
| Pains clear; same meeting; map / use cases | Map | [discovery-template.md](references/discovery-template.md) |
| follow up, prioritize, priority, which first | Prioritize | [prioritization-template.md](references/prioritization-template.md) |
| requirements, good enough, POC, MVP | Requirements | [requirements-gathering-template.md](references/requirements-gathering-template.md) |
| recap, score, rank them | Recap | [prioritization-meeting-recap.md](references/prioritization-meeting-recap.md) + [priority-formula.md](references/priority-formula.md) |
| rerank, re-score, things changed, didn't deliver | Reassess | Same recap + formula; append delta (no blank rediscovery) |
| last time, what did we decide | Recall | Read bundle; write only if something changed |

Bundle home: `docs/discovery/<team>/` (OKF v0.2). Read
[okf-discovery.md](references/okf-discovery.md) before first write.

**Team:** infer from ask, materials, or existing folder. If the user said
`new` and named a team/client/company → use that slug. If `new` with no
name → ask once with brief dynamic examples (department, client, company).
Do not re-ask when the folder is already clear.

**Materials:** expect a path or ref to notes/transcripts/supporting docs.
Synthesize from them. Infer when evidence supports it; ask only when a
high-value field is unclear and the ask would unblock prioritization or
the next meeting — keep the run as zero-shot as possible.

**Done when:** cycle chosen; team bundle path known or asked once; materials
loaded or noted missing.

### 2. Run the cycle template

Follow the loaded template. Placeholder style: `[guidance]`. Drop blocks the
source does not support. Expand a question only when the answer is too
ambiguous to prioritize, book a follow-up, or start a POC.

On prioritize: confirm external vs internal with the room; re-ask priority
in different frames until consensus; record the frame that settled it.

On requirements: winners only (or explicit ask).

**Done when:** template artifact drafted; thin fields flagged with one next ask.

### 3. Score when ranking or reassessing

Assign bands K / P / F / S (1–5) and gates from evidence — see
[priority-formula.md](references/priority-formula.md). Run the skill script
(do not hand-compute N / P-level):

```bash
python3 <this-skill>/scripts/priority_score.py --stdin <<'EOF'
{"candidates":[{"id":"example","K":4,"P":5,"F":4,"S":5,"confidence":"H"}]}
EOF
```

Library checkout: `skills/discovery/scripts/priority_score.py`.

Reassess: re-score only dimensions new evidence touches; keep old P/N
visible; append a Reassessment block — do not rewrite history in place.

**Done when:** script JSON applied to recap table + use-case frontmatter;
judgment gaps named in one line each.

### 4. Write the OKF bundle

Create or update `docs/discovery/<team>/` per
[okf-discovery.md](references/okf-discovery.md). Update parent
`docs/discovery/index.md` team list when minting a new team. Rebuild
`catalog.json` from Markdown. Link concepts with bundle-relative `/…` paths.

**Done when:** session/recap and touched use cases/decisions on disk; indexes
and catalog current; stakeholder lines blank.

## Further reading

- Consumer how-to: [docs/how-to-discovery.md](https://github.com/bmurrtech/skills/blob/main/docs/how-to-discovery.md)
- Script vs LLM: [knowledge/skill-scripts.md](https://github.com/bmurrtech/skills/blob/main/knowledge/skill-scripts.md)
