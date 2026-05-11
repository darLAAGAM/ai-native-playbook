# Skill: Answer Customer Policy Question

## Trigger

A customer or teammate asks about returns, shipping, warranty, subscription, sizing/specs, or exceptions.

## Inputs

- Question
- Order ID if relevant
- Customer context if relevant

## Procedure

1. Search `knowledge/policies/`.
2. Search product or operations docs if the answer depends on product type or delivery state.
3. Draft the answer with cited source files.
4. Escalate if policy is missing, contradictory, legal/safety-sensitive, or high-value.

## Output

- Short answer
- Source files
- Confidence: high / medium / low
- Escalation needed: yes / no

