---
prompt: anonymization-prompt
domain: brain-ops
---

# Anonymize Internal Document Prompt

```text
Anonymize an internal document for public or cross-company use.

Document: {{document}}
Sensitivity rules: {{rules}}

Remove or generalize company names, people, customers, suppliers, exact private revenue, private URLs, credentials, internal endpoints, locations, and dated one-off context. Preserve reusable procedure and decision logic.

Output anonymized doc plus replacement log and residual risk notes.
```
