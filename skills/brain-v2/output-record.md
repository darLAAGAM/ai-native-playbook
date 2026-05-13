---
skill: output-record
domain: brain-v2
complexity: low
prerequisites: Brain v2 output folders, source task or source capture
---

# Output Record

## Purpose

Record durable work produced by an LLM, agent, or employee so the brain knows what was drafted, decided, sent, or shipped.

## Use When

Use when an AI produces a durable draft, brief, plan, decision, sent message, analysis, runbook, or deliverable that future work should reference.

## Inputs

- Output title.
- Output kind: `draft`, `brief`, `plan`, `decision`, or `sent`.
- Content or artifact link.
- Source task path.
- Source capture paths.
- Author.
- Date.
- Status or disposition.
- Entities and domains.

## Procedure

1. Decide whether the output is durable. Skip disposable chat, exploratory notes, and failed attempts unless they document a useful gotcha.
2. Link the output to a task. If no task exists, link to the source capture and explain why no task was needed.
3. Store in the matching folder: `_outputs/drafts/`, `_outputs/briefs/`, `_outputs/plans/`, `_outputs/decisions/`, or `_outputs/sent/`.
4. Add disposition: proposed, accepted, rejected, sent, superseded, or needs review.
5. Move the linked task to `review` or `done` when the output is ready for review or accepted.

## Output

- Output record with source task, sources read, content summary, disposition, and next action.
- Updated task status when appropriate.

## Guardrails

- Do not record private content unless the output is explicitly authorized and stored in a restricted location.
- Do not mark a decision as accepted unless the decision owner approved it.
- Do not leave outputs without a task or source path.

## How to adapt

Add output kinds for your company, such as `spec`, `customer_reply`, `legal_review`, or `finance_model`, while keeping source linkage mandatory.
