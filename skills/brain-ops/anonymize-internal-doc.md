---
skill: anonymize-internal-doc
domain: brain-ops
complexity: medium
prerequisites: source doc
---

# Anonymize Internal Doc

## Purpose

Turn internal knowledge into a public or cross-company artifact without leaking private context.

## Use When

Use this skill when an operator needs a repeatable procedure for turn internal knowledge into a public or cross-company artifact without leaking private context.

## Inputs

- Source document
- Audience
- Sensitivity rules
- Replacement vocabulary

## Procedure

1. Scan for company, employee, customer, supplier, location, URL, credentials, revenue, dates, and internal tool names.
2. Decide what to remove, generalize, or keep as generic structure.
3. Replace named agents/people with roles. Replace brand-specific examples with category-neutral examples.
4. Keep procedures, decision logic, and templates intact where possible.
5. Run a final leak check for identifiers and sensitive facts.

## Output

- Anonymized document
- Replacement log
- Residual risk notes

## Guardrails

- Never publish secrets, personal data, private customer details, or exact internal financials.
- Do not over-sanitize the procedure into useless abstraction.

## How to adapt

Define your banned terms, allowed public examples, and review owner.
