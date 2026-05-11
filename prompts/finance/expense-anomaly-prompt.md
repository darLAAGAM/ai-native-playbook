---
prompt: expense-anomaly-prompt
domain: finance
---

# Expense Anomaly Review Prompt

```text
Review expense data for anomalies.

Data: {{expenses}}
Policy/budgets: {{policy}}

Find new vendors, duplicates, missing receipts, spend spikes, off-policy categories, split transactions, and stale subscriptions. Use neutral wording.

Output table: anomaly, evidence, amount, risk, recommended_action, owner, confidence.
```
