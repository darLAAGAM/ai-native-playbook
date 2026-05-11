---
prompt: utm-taxonomy-prompt
domain: marketing
---

# UTM Taxonomy Prompt

```text
Generate a tracking spec for this campaign.

Campaign: {{campaign}}
Channels: {{channels}}
Landing pages: {{urls}}

Rules: lowercase, no spaces, no PII, consistent separator, platform dynamic parameters where useful.

Output:
- Campaign name
- UTM table by channel
- Full URLs
- GA4 events and parameters
- QA checklist
```
