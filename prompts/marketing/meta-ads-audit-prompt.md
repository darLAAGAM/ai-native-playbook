---
prompt: meta-ads-audit-prompt
domain: marketing
---

# Meta Ads Audit Prompt

```text
Audit Meta Ads performance from exported data.

Data: {{meta_ads_export}}
Targets: {{targets}}
Tracking notes: {{tracking}}

Check: creative fatigue, frequency, CTR/CPM/CPA trend, audience overlap, campaign structure, Pixel/CAPI health, scaling candidates.

Output:
- Account health score /100
- Critical alerts
- Fatigue table
- Audience/structure issues
- Tracking gaps
- Scale/kill/refresh recommendations
- Confidence
```
