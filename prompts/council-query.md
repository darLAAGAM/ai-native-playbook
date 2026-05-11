---
prompt: council-query
domain: strategy
---

# Council Query Prompt

```text
Use six operating perspectives: strategy, customer, finance, growth, operations, and product/category. Adapt perspectives to the business.

Question:
{{question}}

Context:
{{context}}

Instructions:
1. Each perspective answers independently.
2. Each perspective states recommendation, risks, evidence needed, and confidence.
3. Blind-review the answers for accuracy, insight, and actionability.
4. Synthesize final answer with consensus, dissent, decision, next step, and what would change the conclusion.

Output:
- Recommendation
- Confidence
- Consensus
- Dissent
- Risks
- Evidence missing
- Next action
- Decision record draft
```
