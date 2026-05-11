---
skill: detect-vip-customer
domain: customer-service
complexity: medium
prerequisites: customer/order history connected
---

# Detect VIP Or High-Risk Customer

## Purpose

Identify customers who deserve priority handling because of lifetime value, influence, complaint risk, or active revenue impact.

## Use When

Use when you need to identify customers who deserve priority handling because of lifetime value, influence, complaint risk, or active revenue impact.

## Inputs

- Customer profile
- Order history
- Ticket history
- Public/social context if available

## Procedure

1. Calculate signals: lifetime spend, order count, recency, refund rate, current open order value, and subscription or loyalty status.
2. Review qualitative signals: tone, prior escalations, influencer/press/partner status, and whether the issue is blocking an urgent use case.
3. Classify as VIP, high-risk, standard, or abusive/high-risk.
4. Recommend handling: priority queue, senior agent, logistics escalation, founder note, or firm boundary.
5. Attach the evidence that justifies the classification.

## Output

- Classification
- Evidence table
- Recommended service level
- Suggested next action

## Guardrails

- Do not use protected attributes or assumptions about personal identity.
- Do not give VIP treatment that violates consumer law or published terms.
- Record why priority was granted.

## How to adapt

Define VIP thresholds using your own LTV distribution, average order value, and service capacity.
