# AI Onboarding Checklist

Use this for a new employee's first month with the company Brain.

## Pre-arrival

- Manager chooses the first real AI-assisted task.
- Manager confirms the employee has access to [AI_CHANNEL], [BRAIN_HELP_CHANNEL], and required source systems.
- Manager prepares the company-specific master prompt link.
- IT confirms Claude Desktop or the approved AI client can be installed.

## Day 1 Morning

- Install the approved AI client.
- Run the 1-click setup:

```bash
curl -fsSL https://your-mcp.example/setup.sh | bash
```

Windows:

```powershell
irm https://your-mcp.example/setup.ps1 | iex
```

- Restart the AI client.
- Confirm the company Brain tools are visible.

## Day 1 Afternoon

- Paste the current master prompt into the AI client.
- Run the first `brain_search` for a real company question.
- Read at least one Brain path returned by the search.
- Share a short note in [AI_CHANNEL]: what they searched, what they found, and what was missing.

## Week 1

- Complete one real task with AI using at least one Brain read and one source-system check.
- Record one useful learning, gap, or reusable output back into the Brain.
- Manager reviews the output and gives feedback on tool use, evidence, and privacy.

## Day 30

- Run the L0-L3 maturity check.
- Confirm the employee has exited L0.
- Identify one workflow they can automate or document next.
- Capture any onboarding friction as a capability gap or setup improvement task.
