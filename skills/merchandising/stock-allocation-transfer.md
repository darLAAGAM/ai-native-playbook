---
skill: stock-allocation-transfer
domain: merchandising
complexity: medium
prerequisites: inventory by location and demand data
---

# Stock Allocation Or Transfer

## Purpose

Recommend how to allocate or transfer stock across channels and locations based on demand and cover.

## Use When

Use when you need to recommend how to allocate or transfer stock across channels and locations based on demand and cover.

## Inputs

- Inventory by SKU/location
- Sales velocity by location
- Incoming stock
- Minimum display or safety stock
- Transfer constraints

## Procedure

1. Calculate weeks of cover per SKU/location.
2. Identify stockouts, overstock, broken variants/sizes, and locations with unmet demand.
3. Protect minimum display/safety stock.
4. Recommend transfers or allocations that improve availability without creating new gaps.
5. Prioritize moves by expected revenue, customer experience, and operational effort.

## Output

- Transfer/allocation table
- Expected impact
- Do-not-move list
- Operational notes

## Guardrails

- Do not transfer stock needed for imminent demand.
- Account for transfer time and handling cost.

## How to adapt

Define your channels, stores, warehouses, minimum stock, and transfer lead times.
