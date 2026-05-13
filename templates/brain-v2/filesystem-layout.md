# Brain v2 Filesystem Layout

Brain v2 separates raw input, promoted signals, tasks, outputs, health, and the current world model. Start with this shape and adapt names to your company.

```text
knowledge/company/
├── _inbox/
│   └── Normalized captures that agents should search and read.
├── _raw/
│   └── Original source payloads kept for audit or reprocessing.
├── _indexes/
│   └── Logs and indexes that make captures, entities, and sources findable.
├── entities/
│   ├── people/
│   │   └── Explicit people referenced in durable business context.
│   ├── companies/
│   │   └── Customers, partners, vendors, and other organizations.
│   ├── projects/
│   │   └── Projects, launches, initiatives, migrations, and workstreams.
│   ├── campaigns/
│   │   └── Marketing, lifecycle, sales, or customer campaigns.
│   ├── customers/
│   │   └── Customer accounts, segments, or anonymized customer patterns.
│   ├── suppliers/
│   │   └── Vendors or operational partners.
│   └── stores/
│       └── Physical locations, regions, or operational sites when relevant.
├── _tasks/
│   ├── todo/
│   │   └── Accepted tasks not yet handed off.
│   ├── handoff/
│   │   └── Tasks assigned to a person or agent with execution context.
│   ├── review/
│   │   └── Tasks with an output waiting for QA, approval, or decision.
│   ├── done/
│   │   └── Closed tasks with evidence of completion.
│   └── archived/
│       └── Dropped, obsolete, or duplicate tasks.
├── _outputs/
│   ├── drafts/
│   │   └── Durable drafts that may be edited, reviewed, or reused.
│   ├── briefs/
│   │   └── Summaries and execution briefs.
│   ├── plans/
│   │   └── Proposed plans, roadmaps, and operating sequences.
│   ├── decisions/
│   │   └── Accepted decisions with owner, date, and evidence.
│   └── sent/
│       └── Customer, vendor, team, or public-facing outputs that were sent.
├── _health/
│   ├── sources/
│   │   └── Source freshness and pipeline status.
│   ├── jobs/
│   │   └── Scheduled job runs, failures, and canaries.
│   └── issues/
│       └── Health findings that need owner attention.
├── _templates/
│   └── Reusable templates for captures, tasks, outputs, and health reports.
└── _world-model/
    ├── current-state.md
    ├── customer-signal.md
    ├── capabilities.md
    ├── capability-gaps.md
    └── dri-map.md
```

Minimum operating rule: if a signal matters, it should have a path from source to capture, and then to a task, output, decision, health issue, or world model update.
