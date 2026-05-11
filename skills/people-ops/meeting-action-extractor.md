---
skill: meeting-action-extractor
domain: people-ops
complexity: low
prerequisites: meeting notes or transcript
---

# Meeting Action Extractor

## Purpose

Extract decisions, action items, owners, deadlines, and open questions from messy meeting notes.

## Use When

Use when you need to extract decisions, action items, owners, deadlines, and open questions from messy meeting notes.

## Inputs

- Transcript or notes
- Participant list if available
- Project context

## Procedure

1. Identify explicit decisions and who made them.
2. Extract action items with owner, deadline, priority, and dependency.
3. Detect implicit commitments phrased as “I’ll”, “we should”, or “can someone”.
4. List open questions and unresolved disagreements.
5. Create a follow-up message for the team.

## Output

- Decisions
- Actions
- Open questions
- Follow-up message

## Guardrails

- Do not invent deadlines.
- Mark uncertain owners as “unassigned”.
- Preserve sensitive HR content in private channels only.

## How to adapt

Map priority labels and task destinations to your team tools.
