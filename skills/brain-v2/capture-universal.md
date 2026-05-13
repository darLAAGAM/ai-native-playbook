---
skill: brain_capture
domain: brain-v2
complexity: medium
prerequisites: Brain v2 filesystem, capture tool, privacy policy
---

# Universal Brain Capture

## Purpose

Turn useful work context into structured memory without dumping private or low-value material into the brain.

## Use When

Use when a Slack thread, meeting note, email, Drive document, customer signal, decision, incident, or agent session contains durable business context that should become searchable.

## Inputs

- `title`: short descriptive title.
- `body`: normalized content or summary.
- `source_type`: `slack`, `meeting`, `email`, `drive`, `manual`, `agent`, or another source label.
- `source_url`: canonical URL or source id.
- `occurred_at`: ISO date or timestamp when the source happened.
- `author`: person, team, or system that produced the source.
- `domains`: business domains affected.
- `sensitivity`: `public`, `internal`, `restricted`, or `private`.
- `entities`: explicit people, companies, projects, campaigns, suppliers, stores, or customers.
- `create_task`: boolean for actionable signals.

## Procedure

1. Decide whether the source is worth capturing: decisions, metrics, owners, deadlines, risks, customer feedback, process changes, or reusable context.
2. Apply privacy filtering before capture. Promote business context, not personal context.
3. Use raw storage only when auditability matters or the original source may need reprocessing. Use inbox for the normalized capture that agents should read.
4. Call `brain_capture` with the required fields. Keep `body` concise, factual, and source-linked.
5. Set `create_task=true` only when the signal has a clear next action, owner candidate, deadline, or operational risk.
6. Verify the capture path, raw path if created, capture log entry, entity updates, and task path if created.

## Output

- Inbox capture under `_inbox/YYYY-MM-DD/`.
- Optional raw artifact under `_raw/YYYY-MM-DD/`.
- Capture-log entry under `_indexes/`.
- Entity notes updated when explicit entities are present.
- Optional task card under `_tasks/todo/`.

## Guardrails

- Never promote HR sensitive content, recruiting details, CVs, interviews, payroll, compensation, health, family/private context, maternity/paternity or other leaves, personal legal matters, or anything marked confidential.
- Do not capture full mailboxes, full chat logs, or noisy social chatter.
- Do not infer entities that are not explicitly present.
- If sensitivity is unclear, mark `restricted` and avoid task creation until reviewed.

## How to adapt

Rename domains, entity folders, and source types to match your company. Keep the raw/inbox split and privacy hard-stops intact.
