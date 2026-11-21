# Skill workflow patterns

Read when choosing **how** a skill structures its body — not for prose levers
([levers.md](levers.md)) or layout/frontmatter ([mechanics.md](mechanics.md)).
These are common approaches that work well, not mandatory templates.

## Problem-first vs tool-first

- **Problem-first:** User describes an outcome (“set up a project workspace”).
  The skill orchestrates the right tool/MCP calls in order. Users care about
  results; the skill owns the path.
- **Tool-first:** User already has a tool/MCP connected. The skill teaches
  optimal workflows and domain practice for that surface.

Most skills lean one direction. Pick the framing before drafting steps.

## Pattern 1: Sequential workflow orchestration

**Use when:** multi-step process must run in a fixed order.

```markdown
### 1. Create account
Call tool: create_customer — name, email, company
**Done when:** customer id returned

### 2. Setup payment
Call tool: setup_payment_method — wait for verification
**Done when:** payment method verified

### 3. Create subscription
Call tool: create_subscription — plan_id + customer_id from step 1
**Done when:** subscription active
```

Techniques: explicit order; name dependencies; validate each stage; document
rollback on failure.

## Pattern 2: Multi-MCP / multi-service coordination

**Use when:** one outcome spans several services (design → storage → tasks →
notify).

Techniques: clear **phase** separation; pass data between phases explicitly;
validate before advancing; centralize error handling.

## Pattern 3: Iterative refinement

**Use when:** quality improves with draft → check → fix loops.

Techniques: explicit quality criteria; validation script when exactness
matters; regenerate only affected parts; **know when to stop** (threshold, not
infinite polish).

## Pattern 4: Context-aware tool selection

**Use when:** same outcome, different tools by context (size, collab, code vs
temp).

Techniques: clear decision criteria; fallbacks; tell the user **why** that
path was chosen.

## Pattern 5: Domain-specific intelligence

**Use when:** the skill adds specialized rules beyond raw tool access
(compliance, risk, domain checks).

Techniques: domain checks **before** side effects; document decisions; clear
governance / audit trail when required.

## Testing the pattern

After drafting, run skill TDD under **`tdd`**
([skill-testing.md](../../tdd/references/skill-testing.md)): triggering +
functional cases that match the pattern’s success criteria.
