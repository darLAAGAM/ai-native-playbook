---
skill: inventory-stockout-risk
domain: operations
complexity: medium
prerequisites: inventory and sales velocity data
---

# Inventory Stockout Risk

## Purpose

Predict near-term stockouts and prioritize replenishment or allocation actions.

## Use When

Use when you need to predict near-term stockouts and prioritize replenishment or allocation actions.

## Inputs

- Inventory on hand
- Open purchase orders
- Sales velocity
- Lead times
- Safety stock thresholds

## Procedure

1. Calculate days/weeks of cover by SKU/channel/location.
2. Adjust for incoming stock, promo plans, seasonality, and recent trend.
3. Flag stockout risk tiers: urgent, watch, safe, overstock.
4. Recommend actions: expedite PO, transfer stock, pause ads, update PDP messaging, substitute product, or accept stockout.
5. Quantify revenue at risk where possible.

## Output

- Risk table
- Revenue at risk
- Recommended actions
- Owner

## Guardrails

- Do not drive traffic to items likely to stock out unless scarcity is intended.
- State confidence when lead times are uncertain.

## How to adapt

Set safety stock and lead-time assumptions by supplier/category.
