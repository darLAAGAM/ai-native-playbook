---
prompt: stockout-risk-prompt
domain: operations
---

# Stockout Risk Prompt

```text
Predict stockout risk.

Inventory/sales/PO data: {{data}}
Lead times and safety stock: {{assumptions}}

Calculate cover, adjust for incoming stock and promotions, rank urgent/watch/safe/overstock, estimate revenue at risk, and recommend actions.
```
