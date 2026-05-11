---
skill: expense-anomaly-review
domain: finance
complexity: medium
prerequisites: expense/payment data export
---

# Expense Anomaly Review

## Purpose

Detect unusual spend patterns and convert them into approvals, cuts, or investigation tasks.

## Use When

Use when you need to detect unusual spend patterns and convert them into approvals, cuts, or investigation tasks.

## Inputs

- Expense export
- Vendor list
- Budgets or prior periods
- Cardholder/owner data

## Procedure

1. Aggregate spend by vendor, category, owner, card, and week/month.
2. Compare each bucket against budget, prior period, and trailing average.
3. Flag anomalies: new vendor, spend spike, duplicate charge, subscription creep, off-policy category, split transactions, or missing receipt.
4. Estimate financial impact and rank by urgency.
5. Assign each anomaly to approve, investigate, cancel, reclassify, or ignore.

## Output

- Anomaly table
- Impact estimate
- Recommended action
- Owner
- Evidence

## Guardrails

- Do not accuse employees; describe transaction evidence neutrally.
- Do not cancel services without owner approval.

## How to adapt

Replace policy categories and approval thresholds with your finance rules.
