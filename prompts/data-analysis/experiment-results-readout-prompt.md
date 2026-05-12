---
prompt: experiment-results-readout-prompt
domain: data-analysis
---

# Experiment Results Readout Prompt

```text
Interpret these experiment results.

Original hypothesis: {{hypothesis}}
Test dates/allocation: {{test_setup}}
Sample size by variant: {{sample_size}}
Primary metric results: {{primary_results}}
Secondary metrics: {{secondary_results}}
Guardrail metrics: {{guardrails}}
External events: {{external_events}}

Decide whether to implement, reject, rerun, or mark inconclusive. Explain confidence, practical significance, caveats, and the next test or rollout action.
```
