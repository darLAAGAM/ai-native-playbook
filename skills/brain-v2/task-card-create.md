---
skill: task-card-create
domain: brain-v2
complexity: medium
prerequisites: Brain v2 task folders, captured signal, task template
---

# Task Card Create

## Purpose

Convert a captured signal into an actionable task card with enough context for a human or agent to execute without rediscovering the source.

## Use When

Use when a capture contains a concrete action, risk, gap, owner handoff, deadline, decision follow-up, or repeated manual workflow worth operationalizing.

## Inputs

- Captured signal path.
- Task title.
- Owner or owner candidate.
- Due date or review date.
- Domain.
- Source links and source paths.
- Acceptance criteria.
- Context summary.
- Sensitivity.
- Dependencies and blockers.

## Procedure

1. Read the capture and any linked raw source before creating the card.
2. Write the task as an action, not a topic. Use a verb and expected outcome.
3. Add required fields: owner, due date, source paths, acceptance criteria, current status, domain, sensitivity, and confidence.
4. Put the file in `_tasks/todo/` unless it is already assigned for cross-person transfer, in which case use `_tasks/handoff/`.
5. Move flow:
   - `todo`: accepted but not actively handed off.
   - `handoff`: assigned to a person or agent with enough context to execute.
   - `review`: output exists and needs approval or QA.
   - `done`: accepted, shipped, or closed with evidence.
   - `archived`: obsolete, duplicate, or intentionally dropped.
6. Link any resulting output record back to the task.

## Output

- Markdown task card in `_tasks/todo/`, `_tasks/handoff/`, `_tasks/review/`, `_tasks/done/`, or `_tasks/archived/`.
- Clear acceptance criteria and source references.
- Optional linked output path.

## Guardrails

- Do not create tasks from weak signals without an action.
- Do not assign an owner unless the source or operating model supports it. Use `owner_candidate` when unsure.
- Do not remove source links; tasks without sources become unreliable memory.
- Do not put private details in the task body.

## How to adapt

Map statuses to your own workflow if needed, but keep a visible path from signal to task to output to done.
