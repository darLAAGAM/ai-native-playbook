---
skill: triage-ticket
domain: customer-service
complexity: low
prerequisites: shared inbox or helpdesk export
---

# Triage Customer Support Tickets

## Purpose

Classify new support tickets by intent, urgency, revenue risk, and next action.

## Use When

Use this skill when an operator needs a repeatable procedure for classify new support tickets by intent, urgency, revenue risk, and next action.

## Inputs

- Ticket text
- Customer history if available
- Order status and policy docs

## Procedure

1. Read the full thread and identify the customer goal in one sentence.
2. Classify intent: order status, return, refund, exchange, product question, damaged item, delivery issue, complaint, wholesale, spam, or other.
3. Assign urgency: critical when legal, safety, chargeback, VIP, public escalation, or shipment blocker; high when order value or churn risk is high; normal otherwise.
4. Check policy fit before drafting: returns window, shipping promise, warranty, refund method, and exceptions.
5. Choose the next owner: support, logistics, finance, store team, or founder escalation.
6. Draft the first response or internal note with evidence links and unresolved questions.

## Output

- Intent
- Urgency
- Owner
- Policy evidence
- Suggested reply
- Open questions

## Guardrails

- Do not promise refunds, discounts, reships, or exceptions without policy or approval.
- Do not expose internal notes to the customer.
- Escalate abusive, legal, or safety-related tickets.

## How to adapt

Replace the intent taxonomy with your helpdesk tags and define what counts as VIP, high-value, or legal escalation in your business.
