---
skill: experiment-results-readout
domain: data-analysis
complexity: medium
prerequisites: experiment plan and final results by variant
---

# Experiment Results Readout

## Purpose

Interpret experiment results without overclaiming weak or noisy data.

## Use When

Use after an A/B test, holdout test, rollout, pricing test, landing page test, or campaign experiment.

## Inputs

- Original hypothesis
- Test dates and allocation
- Sample size by variant
- Primary and secondary metrics
- Guardrail metrics
- Segment results
- External events during the test

## Procedure

1. Confirm the test ran as planned and tracking was reliable.
2. Check whether sample size and minimum duration were reached.
3. Compare primary metric, effect size, confidence interval, and practical significance.
4. Review secondary and guardrail metrics for contradictions.
5. Inspect segments only as exploratory unless pre-registered.
6. Classify result as implement, reject, inconclusive, or retest.
7. Capture what was learned and the next experiment.

## Output

- Results summary
- Decision
- Metric table
- Caveats and confidence level
- Learning log entry
- Next action

## Guardrails

- Do not cherry-pick a winning segment after the fact.
- Do not confuse statistical significance with business significance.
- Do not ignore broken tracking or implementation issues.

## How to adapt

Set your statistical thresholds, minimum detectable effect, segment rules, and experiment repository format.
