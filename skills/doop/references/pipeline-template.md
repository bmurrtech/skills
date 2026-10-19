# Pipeline template (Doop)

**Need:** transform / stage chain (lead funnel, ETL, approval chain).

## Layout

- Left → right primary spine of stages.
- Each stage: noun box (title + optional owning system).
- Arrows labeled with the trigger/event between stages.
- Fan-out/fan-in below the spine for parallel enrichment or channels.
- Terminal outcomes as end caps (Bought / Declined / Stale).

## HTML hints

Flex/grid row; stage cards ~180px; arrow labels 11–12px muted; bottom legend (solid = primary, dashed = optional).

## Example spine (lead funnel)

CTA click → lead created → DB write (+ metadata) → enrich (brokers) → status trigger → outreach (email/SMS) → book call → sales follow-up → terminal status.
