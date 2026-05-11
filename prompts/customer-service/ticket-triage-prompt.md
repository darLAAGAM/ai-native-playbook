---
prompt: ticket-triage-prompt
domain: customer-service
---

# Customer Support Ticket Triage Prompt

```text
Classify a support ticket and draft the next action. Return concise structured Markdown.

Context:
- Policies: {{policies}}
- Customer/order data: {{customer_context}}
- Ticket: {{ticket_text}}

Instructions:
1. Identify the customer goal in one sentence.
2. Classify intent and urgency.
3. Check policy fit using only supplied policy context.
4. Recommend owner and next action.
5. Draft a customer reply if enough information exists.
6. State confidence and missing info.

Output:
- Intent
- Urgency
- Policy fit
- Owner
- Customer reply
- Internal note
- Missing info
- Confidence
```
