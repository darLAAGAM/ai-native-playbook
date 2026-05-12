---
skill: no-api-data-extractor
domain: operations
complexity: high
prerequisites: permission to access the web app and a repeatable data need
---

# No-API Data Extractor

## Purpose

Turn a web app with no usable API into a repeatable data extraction workflow.

## Use When

Use when operational data is trapped behind login screens, reports, date filters, legacy portals, or manual download buttons.

## Inputs

- Target site or portal
- Data needed and frequency
- Login and permission constraints
- Date range or filters
- Desired output format
- Destination system or folder

## Procedure

1. Confirm there is no official API, export, webhook, or vendor-supported integration.
2. Document the manual workflow: login, navigation, filters, download, and cleanup.
3. Identify stable selectors, URLs, forms, hidden tokens, iframes, and download behavior.
4. Build an automation using a browser tool or headless browser.
5. Externalize credentials and configuration.
6. Add retries, timeout handling, empty-data checks, and session-expiry recovery.
7. Parse, clean, persist, and log each run.

## Output

- Extraction workflow spec
- Automation script or runbook
- Output schema
- Error-handling checklist
- Deployment and monitoring notes

## Guardrails

- Do not bypass access controls or scrape data you are not authorized to use.
- Do not hardcode credentials.
- Do not automate fragile flows without monitoring and failure alerts.

## How to adapt

Customize browser tooling, credential storage, schedule, output destination, data retention, and vendor terms-of-use constraints.
