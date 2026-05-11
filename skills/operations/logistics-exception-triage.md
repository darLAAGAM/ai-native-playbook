---
skill: logistics-exception-triage
domain: operations
complexity: medium
prerequisites: shipment/order tracking data
---

# Logistics Exception Triage

## Purpose

Classify logistics exceptions and route them to the right resolution path.

## Use When

Use when you need to classify logistics exceptions and route them to the right resolution path.

## Inputs

- Order/shipment data
- Carrier status
- Warehouse status
- Customer promise date
- Inventory status

## Procedure

1. Classify exception: delayed, lost, damaged, wrong item, failed delivery, return stuck, warehouse backlog, address issue, customs, or unknown.
2. Determine current blocker and owner: carrier, warehouse, customer, support, finance, or marketplace.
3. Check customer impact: order value, promised date, VIP status, replacement stock availability.
4. Recommend action: wait, trace, reship, refund, address correction, carrier claim, or warehouse investigation.
5. Draft customer update if needed.

## Output

- Exception type
- Owner
- Recommended action
- Customer update
- Evidence

## Guardrails

- Do not reship before checking duplicate shipment and stock availability.
- Keep carrier claim evidence.

## How to adapt

Adapt actions to your carriers, warehouse SLAs, and replacement/refund policy.
