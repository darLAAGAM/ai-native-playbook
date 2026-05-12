---
prompt: campaign-ab-test-plan-prompt
domain: marketing
---

# Campaign A/B Test Plan Prompt

```text
Design an A/B test plan for this campaign.

Hypothesis: {{hypothesis}}
Control: {{control}}
Variant: {{variant}}
Baseline metric: {{baseline_metric}}
Minimum detectable effect: {{mde}}
Daily traffic/impressions: {{traffic}}
Primary metric: {{primary_metric}}
Guardrail metrics: {{guardrails}}

Return the hypothesis, sample size/duration estimate, traffic allocation, launch checklist, monitoring cadence, and decision rules. Do not call a winner before the test is adequately powered.
```
