---
skill: quick-csv-analysis
domain: data-analysis
complexity: low
prerequisites: CSV, spreadsheet export, JSON, or parquet file
---

# Quick CSV Analysis

## Purpose

Inspect, summarize, and convert flat data files quickly using SQL-style analysis.

## Use When

Use for operational exports, ad reports, order files, finance CSVs, survey results, or one-off data investigations.

## Inputs

- Data file
- Business question
- Key columns if known
- Desired output format
- Data quality concerns

## Procedure

1. Preview rows and infer schema.
2. Check row count, missing values, duplicates, and obvious type issues.
3. Calculate summary statistics relevant to the business question.
4. Group by the most important dimensions.
5. Join additional files only when needed.
6. Export the useful result to CSV, markdown, or parquet.
7. Document assumptions and data quality issues.

## Output

- Schema summary
- Data quality notes
- Key tables or aggregations
- Answer to the business question
- Reusable query if applicable

## Guardrails

- Do not trust inferred types without spot checks.
- Do not overwrite source files.
- Do not hide missing or malformed data.

## How to adapt

Define standard export formats, canonical column names, reusable queries, and your preferred local analysis tool.
