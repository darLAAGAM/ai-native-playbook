# Profit Throttle Calculator

## Inputs

| Input | Value | Source | Freshness |
|---|---:|---|---|
| Net revenue |  | Ecommerce/POS |  |
| Paid spend |  | Ads platforms / finance |  |
| COGS ratio |  | ERP / product master |  |
| Return ratio |  | Ecommerce / accounting |  |
| Logistics ratio |  | 3PL / accounting |  |
| Payment fee ratio |  | PSP / accounting |  |
| Variable ops ratio |  | Finance |  |
| Target profit floor |  | Management decision |  |

## Formula

```text
allowable_marketing_ratio =
  1
  - COGS ratio
  - return ratio
  - logistics ratio
  - payment fee ratio
  - variable ops ratio
  - target profit floor

break_even_mer = 1 / allowable_marketing_ratio
blended_mer = net_revenue / paid_spend
marginal_mer = incremental_net_revenue / incremental_paid_spend
```

## Traffic light

| Signal | Rule |
|---|---|
| Green | Blended and marginal MER above break-even with buffer |
| Yellow | Blended above break-even, marginal near/below break-even |
| Red | Blended near/below break-even |
| Black | Missing or stale data |

