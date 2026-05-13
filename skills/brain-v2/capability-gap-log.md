---
skill: capability-gap-log
domain: brain-v2
complexity: low
prerequisites: Brain v2 capability gap tool or task template
---

# Capability Gap Log

## Purpose

Record the exact reason the system cannot complete a useful task, then turn that gap into an owned improvement task.

## Use When

Use when an agent or employee is blocked by missing API access, missing permissions, missing connector fields, brittle auth, absent data, unclear ownership, insufficient documentation, or a tool behavior that prevents reliable execution.

## Inputs

- Gap title.
- What the user or agent tried to do.
- What failed.
- Missing capability.
- Evidence or error message.
- Impact.
- Workaround if any.
- Suggested owner.
- Source task or conversation path.
- Severity.

## Procedure

1. State the gap as a missing capability, not as a vague complaint.
2. Include the exact blocker: missing token, missing scope, unavailable endpoint, bad schema, manual approval, stale docs, or platform limitation.
3. Record evidence: command output, tool error, source path, or reproduction steps.
4. Add impact and frequency so the gap can be prioritized.
5. Create or update a capability gap record.
6. Create a task automatically when the gap is actionable.
7. Link the task back to the gap and the source work.

## Output

- Capability gap record.
- Task card in `_tasks/todo/` when actionable.
- Updated `_world-model/capability-gaps.md` on the next refresh.

## Guardrails

- Do not log secrets, tokens, private customer data, or employee personal details.
- Do not create duplicate gaps; update the existing one if the same blocker recurs.
- Do not call a one-off user preference a capability gap.

## How to adapt

Use your own severity scale and ownership map. Keep every gap tied to evidence and a next action.
