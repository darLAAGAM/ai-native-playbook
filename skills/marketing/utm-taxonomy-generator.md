---
skill: utm-taxonomy-generator
domain: marketing
complexity: low
prerequisites: campaign plan
---

# UTM Taxonomy Generator

## Purpose

Create consistent UTM parameters, event names, and campaign naming conventions across channels.

## Use When

Use when you need to create consistent UTM parameters, event names, and campaign naming conventions across channels.

## Inputs

- Campaign goal
- Channels
- Audience
- Offer
- Landing pages

## Procedure

1. Define one campaign name using lowercase, consistent separators, geography, date/season, audience, and offer.
2. Generate UTM parameters for each channel: source, medium, campaign, content, term.
3. Use platform dynamic parameters where available.
4. Define GA4 events and conversion names using snake_case and no PII.
5. Produce a QA checklist for clicking links and validating events.

## Output

- Campaign naming spec
- UTM table
- Full URLs
- GA4 event spec
- QA checklist

## Guardrails

- Never include personal data in URLs.
- Document every exception to naming rules.
- Test links before launch.

## How to adapt

Pick one separator convention and add your standard channel/source vocabulary.
