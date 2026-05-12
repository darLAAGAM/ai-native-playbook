---
prompt: analytics-tracking-plan-prompt
domain: data-analysis
---

# Analytics Tracking Plan Prompt

```text
Create an analytics tracking plan.

Business questions: {{business_questions}}
Journey/funnel: {{funnel}}
Current analytics stack: {{tools}}
Key conversions: {{conversions}}
Privacy/consent requirements: {{privacy}}
Implementation owner: {{owner}}

Return an event table with event name, description, properties, trigger, conversion status, and QA steps. Include naming conventions and guardrails against PII.
```
