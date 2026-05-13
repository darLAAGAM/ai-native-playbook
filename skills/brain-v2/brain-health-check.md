---
skill: brain-health-check
domain: brain-v2
complexity: medium
prerequisites: Brain v2 health folders, search index, capture/task/output tools
---

# Brain Health Check

## Purpose

Detect broken memory loops before operators notice stale search results, missing owners, orphaned outputs, or silent pipeline failures.

## Use When

Use on a schedule, after adding a new capture pipeline, after a major agent run, or when search quality feels worse than expected.

## Inputs

- Capture log.
- Raw and inbox folders.
- Task folders.
- Output folders.
- Capability gap log.
- World model files.
- Source/job health files.
- Search canary result.

## Procedure

1. Check source freshness for Slack, meetings, email, Drive, and manual capture.
2. Count loose captures: inbox items without domain, entity, task, output, or clear disposition.
3. Count raw files without matching capture.
4. Find tasks without owner, due/review date, sources, or acceptance criteria.
5. Find outputs without source task or source capture.
6. Review open capability gaps and confirm each has a linked task.
7. Check world model freshness: `current-state.md`, `customer-signal.md`, `capabilities.md`, `capability-gaps.md`, and `dri-map.md`.
8. Run or read the search canary and mark pass/fail.
9. Write a health report with issues, owners, severity, and next checks.

## Output

- Health report under `_health/issues/` or `_health/jobs/`.
- Counts for captures, raw files, tasks, outputs, gaps, stale files, and search canary.
- Follow-up task cards for high-severity issues.

## Guardrails

- Health is not a vanity dashboard. Report broken links, missing owners, stale jobs, and privacy risks directly.
- Do not auto-close gaps without evidence.
- Do not expose restricted source contents in a health report.

## How to adapt

Add source-specific checks for your stack. Keep the minimum checks: loose captures, raw without capture, tasks without owner, outputs without source, open gaps, stale world model, and search canary.
