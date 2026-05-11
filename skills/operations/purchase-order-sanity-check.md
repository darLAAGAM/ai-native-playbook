---
skill: purchase-order-sanity-check
domain: operations
complexity: medium
prerequisites: PO and demand forecast available
---

# Purchase Order Sanity Check

## Purpose

Review purchase orders before commitment to catch quantity, timing, margin, and cash risks.

## Use When

Use when you need to review purchase orders before commitment to catch quantity, timing, margin, and cash risks.

## Inputs

- Draft PO
- Demand forecast
- Current inventory
- Sales history
- Payment terms
- Lead times

## Procedure

1. Check quantities against forecast, current stock, safety stock, and historical velocity.
2. Check delivery dates against launch, seasonality, promo calendar, and cash needs.
3. Check unit cost, landed cost, margin, MOQ, and payment terms.
4. Flag anomalies: duplicate order, wrong SKU, wrong variant mix, unrealistic lead time, poor margin, or cash crunch.
5. Recommend approve, revise, split, delay, or cancel.

## Output

- PO verdict
- Issue list
- Financial impact
- Recommended revisions

## Guardrails

- Do not approve orders that create avoidable cash stress without owner review.
- Treat forecast uncertainty explicitly.

## How to adapt

Add your margin floors, MOQ policy, sign-off thresholds, and product lifecycle stages.
