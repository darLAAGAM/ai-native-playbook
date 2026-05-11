---
skill: knowledge-gap-mining
domain: brain-ops
complexity: medium
prerequisites: search/index and usage logs
---

# Knowledge Gap Mining

## Purpose

Find missing or stale knowledge that is causing repeated agent failures or human interruptions.

## Use When

Use when you need to find missing or stale knowledge that is causing repeated agent failures or human interruptions.

## Inputs

- Search logs
- Agent failure notes
- Support/internal questions
- Brain index

## Procedure

1. Cluster unanswered questions, low-confidence answers, and repeated Slack/email asks.
2. Search the brain for each cluster to see whether knowledge is missing, stale, fragmented, or hard to find.
3. Prioritize gaps by frequency, decision impact, and operational risk.
4. Create docs or update existing docs with owner and source-of-truth links.
5. Add tags/aliases so future retrieval finds the answer.

## Output

- Gap list
- Priority
- Recommended doc changes
- Owner

## Guardrails

- Do not create duplicate docs when an update would solve the problem.
- Mark stale docs rather than silently trusting them.

## How to adapt

Use your own logs and incident tags to identify retrieval misses.
