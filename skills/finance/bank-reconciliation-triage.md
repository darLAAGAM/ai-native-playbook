---
skill: bank-reconciliation-triage
domain: finance
complexity: medium
prerequisites: bank export and ledger export
---

# Bank Reconciliation Triage

## Purpose

Find unmatched bank transactions, duplicates, and suspicious entries before month close.

## Use When

Use this skill when an operator needs a repeatable procedure for find unmatched bank transactions, duplicates, and suspicious entries before month close.

## Inputs

- Bank statement export
- Ledger/accounting export
- Payment processor payouts
- Date range

## Procedure

1. Normalize dates, amounts, currencies, references, and counterparty names.
2. Match exact transactions first by amount/date/reference.
3. Fuzzy-match remaining transactions by amount tolerance, date window, and counterparty similarity.
4. Classify unmatched items: bank fee, payout, supplier payment, payroll, tax, refund, transfer, duplicate, or unknown.
5. Flag high-risk anomalies: duplicate payments, unexpected counterparties, round-number withdrawals, old unreconciled items, and currency mismatches.

## Output

- Matched count
- Unmatched list
- Duplicate candidates
- Anomaly list
- Close blockers

## Guardrails

- Do not delete or edit accounting records automatically.
- Keep a reversible audit trail.
- Escalate suspicious transactions to finance owner.

## How to adapt

Tune date windows, amount tolerances, and categories to your bank/payment stack.
