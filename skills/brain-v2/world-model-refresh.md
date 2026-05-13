---
skill: world-model-refresh
domain: brain-v2
complexity: high
prerequisites: Brain v2 world model, completed tasks, output records, source intelligence
---

# World Model Refresh

## Purpose

Refresh the company's current operating picture from real work signals instead of relying on stale strategy docs.

## Use When

Use weekly, after major planning cycles, after operational incidents, or when agents appear to be working from outdated assumptions.

## Inputs

- Tasks in `done` and `review`.
- Outputs in `decisions` and `sent`.
- Slack high-signal captures.
- Meeting intelligence.
- Email intelligence.
- Drive digests.
- Capability gaps.
- Customer signals.
- DRI or ownership changes.

## Procedure

1. Read the latest health report first. Do not refresh confidently if core sources are stale or failing.
2. Review completed tasks and accepted outputs since the last refresh.
3. Pull durable signals from Slack, meetings, email, and Drive digests. Ignore chatter and low-life-span updates.
4. Update `_world-model/current-state.md` with what is true now, what changed, and confidence.
5. Update `_world-model/customer-signal.md` with repeated customer pains, language, demand signals, and objections.
6. Update `_world-model/capabilities.md` with what the company can now do reliably.
7. Update `_world-model/capability-gaps.md` with open blockers, owners, and linked tasks.
8. Update `_world-model/dri-map.md` with current owner mapping by domain or system.
9. Record source paths and the refresh date.

## Output

- Refreshed `current-state.md`.
- Refreshed `customer-signal.md`.
- Refreshed `capabilities.md`.
- Refreshed `capability-gaps.md`.
- Refreshed `dri-map.md`.
- Optional task cards for stale, conflicting, or missing ownership areas.

## Guardrails

- Do not overstate weak signals. Mark confidence explicitly.
- Do not include sensitive personal context.
- Do not rewrite strategy from preference; use source-linked evidence.
- If sources are stale, say so at the top of the refresh.

## How to adapt

Change the world model files to match your operating domains, but keep the weekly loop from tasks, outputs, source signals, gaps, and health.
