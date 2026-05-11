---
prompt: refund-response-prompt
domain: customer-service
---

# Refund Response Prompt

```text
Draft a refund/return/exchange response from policy and order facts. Do not invent eligibility.

Inputs:
- Customer message: {{message}}
- Order facts: {{order}}
- Policy: {{policy}}

Return:
1. Decision: eligible | not eligible | needs info | escalate
2. Reason, citing policy clause or provided fact
3. Customer-ready reply
4. Internal note
5. Any approval needed
```
