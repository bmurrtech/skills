# Topology template (Doop)

**Need:** present-state stack — servers, services, SaaS/PaaS, DBs, triggers, trust boundaries.

## Layout

- Horizontal **bands** (top→bottom): Client / Edge / App / Data / External SaaS (adjust to intel).
- Boxes inside bands; dependency arrows labeled (HTTPS, webhook, queue, sync).
- Hard boundary boxes for VPC / private / compliance plane.
- Certainty tags per compose (`[Existing]`, `[Assumption]`, …).

## HTML hints

Full-width band sections; node cards 160–220px with `search_icons` + name + one-line role; avoid unexplained edge crossings.
