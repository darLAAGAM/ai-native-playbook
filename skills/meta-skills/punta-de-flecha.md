---
skill: punta-de-flecha
domain: meta-skills
complexity: high
prerequisites: two independent models or reviewers available
---

# Punta De Flecha Adversarial Review

## Purpose

Use adversarial cross-review for expensive, irreversible, or high-uncertainty decisions.

## Use When

Use this skill when an operator needs a repeatable procedure for use adversarial cross-review for expensive, irreversible, or high-uncertainty decisions.

## Inputs

- Question
- Context
- Evidence pack
- Maximum rounds
- Decision threshold

## Procedure

1. Run independent analysis from two models/reviewers before either sees the other.
2. Force critique rounds: each side attacks assumptions, missing evidence, and weak logic in the other answer.
3. Allow revision after critique.
4. Fact-check key claims and identify unverifiable assumptions.
5. Red-team the emerging consensus.
6. Synthesize consensus, unresolved disagreement, recommendation, and review date.

## Output

- Recommendation
- Consensus
- Resolved divergences
- Unresolved divergences
- Red-team risks
- Confidence

## Guardrails

- Do not use for trivial questions.
- Do not collapse disagreement just to look decisive.
- State when evidence is insufficient.

## How to adapt

Define review thresholds, model/reviewer choices, and polling/job mechanics if run asynchronously.
