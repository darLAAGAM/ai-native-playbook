# Reference Brand AI Portfolio — What We've Actually Built

*Created: 2026-05-11*  
*Scope: internal inventory for a public editorial portfolio rewrite*  
*Anonymization rule: this document uses role names and generic company language. Paths in the reference section are left intact so the work can be verified internally.*

---

## 1 · Executive Summary

The reference brand is a mid-sized direct-to-consumer retail company that has been operating an AI-native internal system for more than a year. The important thing is not that it has chatbots. The important thing is that it built a shared operational substrate: a structured company brain, an MCP interface that exposes real business systems to AI clients, and a domain-specialized agent swarm that reads from and writes back to that substrate.

The system is now closer to an operating layer than a collection of assistants. A customer-service agent can read customer tickets and product policy. A finance agent can reconcile invoices and explain cash movement. A retail agent can connect store traffic to sales conversion. A marketing agent can query ad, email, search, and copy performance. A merchandising agent can reason about sell-through, allocation, and margin. A people-operations agent can answer policy and leave questions. A strategy hub and a technical execution interface sit above them.

The strategic frame is simple: the brain is the primitive. Agents are replaceable. Models change. Tools get added and deprecated. The durable asset is the structured, executable memory of how the business works. The more decisions, bugs, patterns, scripts, policies, and operating lessons get crystallized into the brain, the cheaper it becomes to build the next agent or workflow.

What is notable:

- A live company brain with **1,324 markdown/QMD files in the current filesystem working copy**, **1,341+ docs indexed by the QMD/vector layer according to the MCP metadata**, and **1,665 total files** under the brain directory. Older public playbook pages still cite 409, 968, 1,341, and 44-tool snapshots; the real current system has moved beyond those numbers.
- A production MCP server with **84 registered tool functions in `server.py`**, public Claude/Codex access through `https://mcp.<domain>/mcp` and legacy `/sse`, bearer-key auth in observe mode, tool-call health metrics, and an action ledger for mutations.
- A swarm of **7 domain agents plus a founder/technical interface**, currently validated in the runtime registry: strategy hub, customer service, finance, retail, digital marketing, merchandising/wholesale, HR/people, and Codex/Claude Code for technical execution and orchestration.
- A portfolio of advanced capabilities that were actually built: AutoResearch, LLM Council, Punta de Flecha, Profitability Engine, Profit Throttle, Pattern Library, invoice pipeline, copy engine, GEO, PR tracking, master calendar, factory runtime, helpdesk webhooks, and more.
- A skills library currently exposing **310 skills via `skills_list`**. Separately, the filesystem contains **146 `SKILL.md` files** under the brain; older documents cite 167 or 183 skills. For public claims, use 310 if referring to the tool-exposed methodology library, and 146 if referring strictly to `SKILL.md` files on disk.

The honest status: this is not L4 autonomy. Non-engineers still cannot extend every part of the system by themselves. Some current docs contradict one another. Several capabilities are production-validated inside the reference brand but not yet cleanly packaged for other companies. The system is strong because it has survived real incidents, not because it is neat.

---

## 2 · The Brain: The Substrate

### What it is

The brain is the shared operational memory of the company. It is not a Notion workspace with a better search bar. It is a filesystem-native knowledge base designed to be consumed by agents and humans through tools. Every agent can search it. Claude Desktop users can search it. Codex can search it. Operational scripts can write to it.

The current canonical model has three layers:

1. **Institutional Knowledge**: `brain/knowledge/`, organized by domain. This is the curated source of truth: finance, operations, marketing, retail, team, strategy, product, platform, projects, skills, and lessons.
2. **Working Memory**: `brain/memory/YYYY-MM-DD.md`, where session logs, daily decisions, validations, incident notes, and short-term operational discoveries are captured.
3. **Retrieval / Context Layer**: QMD and vector search, plus ByteRover-style curated memory, make the filesystem searchable from agents and MCP clients.

Earlier architecture docs describe SuperMemory as the semantic memory layer. The production update is more interesting: SuperMemory was removed after it created noise. It had been deleting 90+ duplicates per agent per week and still degraded response quality. The replacement is more deterministic: a context tree, QMD search, working memory, and curated markdown. The lesson is that operational memory needs structure more than it needs vague recall.

### Current scale

Measured on the VPS working copy on 2026-05-11:

| Metric | Current count | Notes |
|---|---:|---|
| Total files under `brain/` | 1,665 | Includes markdown, JSON, configs, logs, and supporting files. |
| Markdown/QMD files under `brain/` | 1,324 | Best filesystem count for public “documents” claim if being conservative. |
| Docs indexed by MCP vector metadata | 1,341+ | Exposed in `brain_vsearch` tool description. This can exceed markdown count because collections include workspace/playbook mirrors. |
| Company-domain knowledge files | 466 | Company operating knowledge. |
| `knowledge/platform` files | 259 | Agents, tools, config, auth, runbooks. |
| `knowledge/projects` files | 48 | compAI and side projects. |
| `knowledge/skills` files | 57 | Core skills folder; only one part of the broader skills library. |
| Tool-exposed skills | 310 | Returned by `skills_list`. |
| Filesystem `SKILL.md` files | 146 | Real current count under `brain/`. |

The discrepancy is not a bug in this inventory; it is a fact about the system. Different docs were written at different stages: 409 docs in March, 968 docs at the April audit, 1,341 docs in the playbook, 1,324 markdown/QMD in the current working copy, 1,341+ in indexed collections, and 1,665 total files. The public portfolio should avoid a single ambiguous “docs” claim unless it specifies the counting method.

### Architecture

The brain lives on the primary VPS under the primary workspace. The secondary-host agents use a shared brain path, with symlinks from each agent workspace. A bidirectional sync runs every 30 minutes. The architectural intent is “one brain, multiple access surfaces.”

The main directory shape is:

```text
brain/
  knowledge/
    company/      company operating knowledge
    platform/     agent, MCP, auth, infra, setup, runbooks
    projects/     compAI and R&D projects
    skills/       executable and reference skills
    areas/        ongoing topic areas
    lessons/      durable lessons
  memory/         daily memory and session logs
  skills/         newer lightweight slash-style skills
  brand/          brand assets and guidelines
  templates/      reusable templates
```

For public-facing prose, the useful abstraction is:

- **Docs** say what is true.
- **Skills** say how to do something.
- **Tools** connect the brain to live systems.
- **Memory** captures what just happened.
- **Mining / learning loops** move durable lessons from memory into docs and skills.

### QMD and semantic search

The system uses QMD as the local markdown search/indexing layer. The May docs describe QMD v2.0.1 and a shift toward semantic search defaults. On 2026-04-17, the second-brain upgrade added:

- `brain_vsearch(query, collection, max_results)` for semantic-only search.
- `brain_query(query, collection, max_results)` for hybrid vector + keyword + reranking.
- `brain_search` retained for exact terms, SKUs, names, paths, and known phrases.

This matters because keyword search stopped being enough once the brain exceeded ~1,000 docs. Exact search is still valuable for identifiers. Semantic search is better when a user asks conceptually, for example “how do we handle VIP returns” when the actual doc says “premium customer exception policy.”

### ACL and RBAC model

The reference implementation evolved from a simple two-role model to ACL groups at the collection boundary.

Older playbook docs describe:

| Role | Read | Write |
|---|---|---|
| Admin | Everything | Everything |
| Team | Brain, memory, APIs | No `brain_write`, no `file_write`, no `shell_exec` |

The later ingest-layer work added a more precise design:

- API keys carry `acl_groups`.
- QMD collections are partitioned by group.
- Retrieval is routed only to collections permitted for the principal.
- ACL is enforced at the index boundary, not by filtering after retrieval.
- Ingested data is written under paths such as `knowledge/<brand>/ingested/<acl_group>/YYYY/MM/...`.

The current MCP health response shows auth mode as `observe`, 20 API keys loaded, and no warnings. That means the auth layer exists, observes access, and keys are loaded, but some requests still arrive as anonymous. This should be presented honestly: bearer auth and ACL infrastructure exist; full enforcement and client migration are still ongoing.

### Self-updating mechanisms

The brain updates through several loops:

- **Manual `brain_write`**: agents and Claude/Codex write durable docs when they discover something new.
- **Daily memory**: session logs and operational outcomes are written to `memory/`.
- **Knowledge Mining**: earlier docs describe a cron that reads recent memory, extracts durable decisions, routes each finding to the right domain, and updates indexes.
- **`/learn` / `brain_learn`**: shipped on 2026-04-17 to let operators capture a gotcha, pattern, decision, bug, insight, or tool behavior directly into the brain with less friction.
- **Weekly digest concept**: the May AI-pilled execution plan proposes using the action ledger plus recent searches to suggest new skills or patterns for approval.
- **Pattern Library extraction**: a weekly cron extracts anonymized cross-company patterns from memory and audit docs into the pattern library.

The principle is more important than any one mechanism: if the brain does not update itself, it dies. This was not theoretical; stale knowledge caused agents to answer with old product and policy information. Knowledge updates are now part of product-launch and operational checklists.

### How it is accessed

The brain is accessed through:

- Filesystem on the VPS for scripts and the strategy hub.
- Filesystem on the secondary host for domain agents.
- MCP tools: `brain_search`, `brain_vsearch`, `brain_query`, `brain_read`, `brain_write`, `brain_list`, `brain_capture`, `brain_learn`.
- Claude Desktop and Codex via the MCP server.
- QMD indexes for fast retrieval.
- Skills and slash commands for procedural access.

The important portfolio point: a human does not need to know where the file lives. They ask their AI client. The client searches the brain and calls the right API.

---

## 3 · MCP Server: The Interface

### What it is

The MCP server is the interface between AI clients and the company’s real systems. It exposes the brain, business APIs, agent control, filesystem, shell, memory, skills, and specialized workflows as callable tools.

It is the layer that turns “Claude can answer questions” into “Claude can read the company brain, query orders, inspect ads, read finance docs, ask an agent, write a durable learning, and produce a verified answer.”

### Current architecture

The current MCP guide says the server runs on the primary VPS, behind a Cloudflare Tunnel, with hybrid transport:

| Endpoint | Protocol | Current doc status |
|---|---|---|
| `/mcp` | Streamable HTTP | Preferred in the May 2026 MCP guide. Currently used by this Codex session. |
| `/sse` | Legacy SSE | Still supported for older Claude/OpenClaw clients. |

There is a contradiction in the April Codex setup doc: it says `/mcp` returns 404 and `/sse` is correct. That was true at the time of the doc. The May MCP guide and this run show `/mcp` is now live. Public docs should not copy the April setup section without updating it.

The server is implemented in Python/FastMCP in the primary workspace, with supporting utilities in `utils.py`. It runs as the brand MCP service and is exposed via Cloudflare Tunnel.

### Tool count

The real current code count on 2026-05-11 is **84 registered `@mcp.tool()` functions** in `server.py`.

Older docs cite:

- 44 tools in the early playbook.
- 56 tools in one section of the MCP guide.
- 69 tools in the Codex setup doc.
- 70 or 71 tools in May guide/changelog snippets.
- 84 registered functions in current source.

For public claims: use **“80+ MCP tools”** or **“84 registered tool functions as of 2026-05-11”**. Do not claim 44 unless referring to the early deployment.

Registered tools include:

```text
brain_search, brain_read, brain_write, brain_list, brain_capture, read_megadoc,
brain_vsearch, brain_query, brain_learn, me_read, me_write,
file_read, file_write, file_list, shell_exec,
memory_read, memory_write, memory_list_recent,
agent_status, agent_send,
council_query, consult_opus,
shopify_query, shopify_graphql, shopify_search_products, shopify_product_detail, shopify_store_info,
stockagile_query, klaviyo_query, holded_query,
meta_ads_query, meta_cli, tiktok_ads_query, tiktok_query,
payhawk_query, amphora_query, richpanel_query,
slack_search, slack_list_channels, slack_read_channel, slack_read_thread, brain_capture_slack_thread, slack_send_message, slack_user_info,
notion_query, tc_analytics_query,
punta_de_flecha, punta_de_flecha_status, punta_de_flecha_list,
gsc_search_analytics, gsc_top_queries, gsc_top_pages, gsc_inspect_url, gsc_sitemaps,
ga4_query, google_workspace,
cash_position_today, cash_position_history, cash_position_set_manual, cash_position_reconcile, cash_position_anomalies,
holded_leaves, exa_search, vercel_query,
krea_generate, krea_status, upstash_redis, wow_sales_query,
skills_list, skill_read, skill_search,
pinterest_ads_query, mcp_health, action_ledger_tail,
mcp_auth_observe_tail, mcp_auth_inventory,
rever_query, marketing_calendar_refresh, marketing_calendar_status,
copy_generate, copy_rate, copy_stats, copy_refine, copy_link_campaign
```

### ACL groups and auth

The current server has:

- Bearer-key auth support.
- API key inventory: 20 keys loaded in current health output.
- Auth observe logs in the brand MCP state directory.
- Mutation action ledger in the brand MCP state directory.
- ACL groups in the compAI repo and ingest layer design.
- Key management in the repo via `operai-init key create/list/revoke`.

The current session could not read `action_ledger_tail` or `mcp_auth_inventory` through normal MCP because admin token was required. Direct filesystem access showed the action ledger exists and contains mutation records. This is a good sign: admin observability exists, and non-admin clients cannot casually inspect it.

### Audit trail

The action ledger records mutation-class events such as `shell_exec`, `brain_write`, `file_write`, `brain_learn`, `memory_write`, `agent_send`, `punta_de_flecha`, and `council_query`.

A quick parse of the MCP service log found 10,562 INFO tool log lines, dominated by high-risk or mutation-style tools:

| Logged tool | Count in log parse | Interpretation |
|---|---:|---|
| `shell_exec` | 9,408 | Heavily used for technical execution and VPS work. |
| `brain_write` | 616 | Durable knowledge capture is real, not aspirational. |
| `file_write` | 306 | Filesystem mutation path exists. |
| `brain_learn` | 60 | Lightweight learning capture has been used. |
| `memory_write` | 55 | Daily/session memory writes. |
| `agent_send` | 39 | Cross-agent calls via MCP. |
| `punta_de_flecha` | 21 | Adversarial cross-model deliberations. |
| `council_query` | 13 | Multi-perspective council calls. |
| `consult_opus` | 10 | Second-model consulting. |
| `me_write` | 4 | Personal context write path. |

This is not a complete usage ranking for read-only tools, because not every read call appears in the mutation/audit log. The current `mcp_health` endpoint exposes last-hour call counts, but this run contaminated that window with the portfolio sweep. Public claims should say “top logged mutation tools” unless a clean longer-window analytics export is produced.

### Top operational tools

The tools that matter most to the operating model are:

1. **`brain_search` / `brain_query` / `brain_vsearch`**: find knowledge in the company brain.
2. **`brain_read`**: read authoritative docs once a path is known.
3. **`brain_write` / `brain_learn`**: capture durable knowledge, decisions, and gotchas.
4. **`shopify_query` / `shopify_graphql`**: source of truth for orders, products, inventory, and sales.
5. **`stockagile_query`**: inventory, warehouse, transfers, and wholesale operations.
6. **`klaviyo_query`**: email campaigns, flows, segments, and lifecycle performance.
7. **`holded_query` / `holded_leaves`**: accounting, invoices, and reverse-engineered absence data.
8. **`meta_cli` / `meta_ads_query`**: paid media performance and campaign operations.
9. **`google_workspace`**: Gmail, Drive, Docs, Sheets, Calendar, and service-account automations.
10. **`agent_send`**: ask the correct domain agent instead of forcing a generic assistant to answer.

### Production hardening

Several hardening changes have already shipped:

- Rate limiting on public setup and health endpoints after an April audit.
- Per-handler rate limiting instead of global middleware because SSE streaming broke under `BaseHTTPMiddleware`.
- Process supervision for child processes after MCP RSS grew toward multi-GB memory usage. `run_child_process` and `spawn_detached_child` now enforce process groups, timeouts, SIGTERM/SIGKILL, pipe closure, and metrics.
- Weekly preventive MCP restart timer for historical memory leak risk.
- Health endpoint now returns RSS, child process counts, uptime, last-hour tool counts, and warnings.
- Sync tools are wrapped so they do not block the FastMCP async event loop.

The live health snapshot during this inventory showed: `status=ok`, RSS ~80 MB, no child processes, no warnings, and uptime ~39 minutes.

---

## 4 · The Agents

### Current validated fleet

The canonical runtime registry as of 2026-05-06 lists seven production agents:

| Public role | Domain owned | Current validated runtime | Host | Main channel |
|---|---|---|---|---|
| Strategy Hub | Strategy, founder support, coordination, brain stewardship | GPT-5.5 via Codex/OpenAI OAuth | Primary VPS | MCP / Slack / messaging relay |
| CS Agent | Customer service, ticket drafting, policy-grounded replies | Claude Sonnet 4 with GPT fallback | Secondary host | Slack + messaging app |
| Finance Agent | Reporting, cash, invoices, treasury, reconciliation | GPT-5.5 via Codex/OpenAI OAuth | Secondary host | Slack |
| Retail Agent | Store sales, traffic, POS, retail intelligence | GPT-5.5 via Codex/OpenAI OAuth | Secondary host | Slack |
| Digital Marketing Agent | Ads, web, SEO, analytics, email lifecycle | GPT-5.5 via Codex/OpenAI OAuth | Secondary host | Slack |
| Merchandising Agent | Assortment, allocation, pricing, wholesale ops | GPT-5.5 via Codex/OpenAI OAuth | Secondary host | Slack |
| HR / People Agent | Onboarding, leave, policies, payroll prep, expenses | GPT-5.5 via Codex/OpenAI OAuth | Secondary host | MCP / Slack pending auth review |

There is also a founder-facing **Claude Code interface** and a **Codex technical executor**. Those are not domain agents. They are the orchestration and technical execution layer: strategy synthesis, code, scripts, debugging, adversarial review, and bulk processing.

### Strategy Hub

**Domain owned:** strategy, founder support, cross-agent coordination, reminders, brain updates, and high-level operations.

**Tools available:** essentially the full MCP surface: brain, shell, files, Shopify, finance systems, Slack, Google Workspace, agents, research tools, council, and Punta de Flecha.

**Autonomy threshold:** high for research, synthesis, reminders, routing, and documentation. Lower for financial mutations, external sends, or irreversible business actions.

**Key wins:**

- Became the central route for asking the company questions across systems.
- Owns memory capture and cross-agent handoffs.
- Coordinates high-stakes deliberation via Council or Punta de Flecha.
- Handles founder-facing workflows that used to require jumping between tools.

**Failures and fixes:**

- Took on too much technical execution before role boundaries were formalized. The 2026-04-27 role-boundary doc fixed this: Claude orchestrates, Codex executes technical work, swarm agents own domains.
- Earlier model/provider configurations became stale. The runtime registry now wins over older docs.

### CS Agent

**Domain owned:** customer-service tickets, customer policy questions, refund/change workflows, tracking issues, tone, and escalation.

**Tools available:** brain, store policy search, product search/detail, Richpanel tickets, Shopify orders, logistics/3PL data, Slack/internal notes.

**Autonomy threshold:** public playbook describes tiering: routine tickets autonomous or drafted, higher-value or policy-sensitive cases reviewed, edge cases escalated. The internal current rule is stricter: the agent drafts internal notes and does not directly send to customers without a human layer in the current reference setup.

**Key wins:**

- Customer-service knowledge base and response guide were codified.
- Tracking and order-status workflows became parallel API lookups instead of manual dashboard work.
- AutoResearch improved a tracking-query category to 94.7% accuracy over three months.
- Anti-prompt-injection hardening was added because customer text is untrusted input.

**Failures and fixes:**

- Shadow mode proved mandatory after an international shipping edge case escaped the first test window.
- Messaging integrations can replay queued messages after reconnecting. Unused channels are now disabled.
- WhatsApp required plugin installation and stale-session cleanup before it was restored.

### Finance Agent

**Domain owned:** cash position, weekly reporting, invoice intake, treasury calendar, payables, reconciliations, credit-line alerts, financial anomalies.

**Tools available:** Holded, Payhawk, Google Workspace, Drive/Sheets, Shopify, banking exports through available connectors, brain finance docs, cash-position tools, invoice pipeline, amortization alerts.

**Autonomy threshold:** high for read, reporting, reconciliation checks, alerts, and draft summaries. Human confirmation remains required for payments, approvals, and sensitive decisions.

**Key wins:**

- Invoice pipeline processes supplier invoices from email into Drive and Sheets. Initial backfill processed 100 emails and registered 117 invoices.
- Cash and amortization alerting tracks active debt schedules and warns before deadlines.
- Profitability Engine gives the finance and marketing teams daily DTC contribution-margin visibility.
- Weekly P&L work moved from manual spreadsheet interpretation toward narrative reporting and anomaly detection.

**Failures and fixes:**

- OAuth and model routing changed multiple times. The current pattern uses existing human ChatGPT subscriptions through OAuth where reliable.
- External finance APIs sometimes lack endpoints; the team built microservices where necessary, notably for leave data.

### Retail Agent

**Domain owned:** physical store performance, traffic, conversion, POS, staffing patterns, retail stock, and channel-specific diagnosis.

**Tools available:** Shopify POS, Stockagile, TC Analytics, brain retail docs, Google Sheets/Workspace, Slack.

**Autonomy threshold:** high for reporting, diagnosis, weekly snapshots, and recommendations. Lower for staffing decisions, partner escalations, and inventory movements that change stock position.

**Key wins:**

- Retail intelligence moved beyond “sales were up/down” into a four-lever model: exterior traffic × attraction × conversion × ticket.
- TC Analytics integration unlocked foot-traffic and conversion analysis for stores with sensors.
- Hit Dependency Index gives a way to classify stores as hit-driven boutiques or broader flagship-style locations.
- The agent can detect when a partner/channel operational change affects all stores versus one store.

**Failures and fixes:**

- Retail data sources were fragmented and inconsistent. The retail principles doc now names source-of-truth per channel.
- Some channels still require manual exports; the system explicitly flags those instead of pretending every API is live.

### Digital Marketing Agent

**Domain owned:** paid media, lifecycle email, SEO/GEO, analytics, copy performance, campaign calendars, PR tracking, and web performance.

**Tools available:** Klaviyo, Meta, Pinterest, Google Ads through GA4, GA4, GSC, Shopify, Google Workspace, Slack, PR tracking sheets, copy engine, GEO tooling, marketing calendar refresh.

**Autonomy threshold:** high for analysis, alerting, reporting, drafts, taxonomy, and recommendations. Human judgment remains necessary for creative direction and major budget moves.

**Key wins:**

- Copy Engine analyzed campaign history and extracted reusable copy patterns.
- GEO research reframed SEO for AI answer engines and deprioritized low-impact `llms.txt` work.
- PR tracking automated social and press clipping capture, with a dedicated sheet and story capture before 24-hour expiry.
- Marketing calendar sync consolidated sources into a shared Google Calendar surface.
- Ads audit system codifies 46 Meta checks and 74 Google checks with weighted scoring.

**Failures and fixes:**

- Vendor APIs can silently change or expire. Richpanel and Pinterest both forced defensive health checks and token handling.
- Story webhooks can die silently; monitoring and metadata persistence were added after missed mentions.

### Merchandising Agent

**Domain owned:** assortment, sell-through, allocation, stock health, pricing/markdowns, reorder logic, wholesale operational support.

**Tools available:** Shopify, Stockagile, 3PL, profitability outputs, sell-through docs, wholesale rules, brain product/finance/retail knowledge.

**Autonomy threshold:** high for analysis, weekly sell-through reporting, allocation recommendations, and flagging markdown risk. Human judgment remains required for taste, buying, supplier negotiation, and major assortment changes.

**Key wins:**

- Moves merchandising from spreadsheet-based retrospectives to daily/weekly operating signals.
- Connects product performance to channel, location, margin, and stock position.
- Supports wholesale order creation through Stockagile v3 for bounded cases.
- Uses profitability and retail signals to inform allocation and markdown decisions.

**Failures and fixes:**

- Product and category knowledge goes stale quickly. Product launch checklists now need explicit brain updates.
- Wholesale and inventory systems have endpoint gotchas; Stockagile URLs must avoid trailing slashes.

### HR / People Agent

**Domain owned:** onboarding, leave, payroll prep, employee policies, expenses, org chart, and people ops self-service.

**Tools available:** Notion, Holded, reverse-engineered Holded leaves microservice, Payhawk, Google Workspace, Slack, brain HR/team docs.

**Autonomy threshold:** high for answering policy questions, drafting onboarding/offboarding checklists, leave summaries, payroll prep drafts, and expense reports. Low for approvals: no vacation approvals, salary decisions, or employee-sensitive actions without human confirmation.

**Key wins:**

- The company moved from ad hoc HR processes toward documented policies and self-service answers.
- Reverse-engineered leave data made absences queryable despite the official API not exposing leave endpoints.
- New-hire AI onboarding became mandatory: install Claude Desktop, connect MCP, run an initialization prompt, complete a real AI task in week one.

**Failures and fixes:**

- HR was pre-deployment in older audit docs. It is now operational through MCP/agent_send, but Slack auth still needs review if `invalid_auth` appears.
- Reverse-engineered browser/session APIs are fragile; health endpoints and relogin fallback are necessary.

### Claude Code and Codex interface

This is the technical execution and orchestration layer rather than a business-domain agent.

**Claude Code owns:** intent capture, strategy conversation, orchestration, synthesis, short docs, routing tasks to agents or Codex.

**Codex owns:** scripts over 30 lines, sync pipelines, debugging, bulk processing, refactors, code review, and adversarial technical review.

The 2026-04-27 role-boundary doc is a major organizational artifact. It acknowledges a real failure: Claude spent hours on technical work that should have gone to Codex. The formal rule fixed the operating model.

---

## 5 · Advanced Capabilities

### AutoResearch

AutoResearch is a self-evolving prompt loop. The CS agent scores its own output quality by category, generates prompt mutations when a category underperforms, tests mutations against historical tickets, and promotes a mutation when it beats baseline by more than 5%.

How it works:

1. Every response is scored by a separate model on correctness, tone, and policy compliance.
2. Scores are aggregated by category: tracking, returns, sizing, order changes, complaints.
3. Underperforming categories trigger 3-5 prompt mutations.
4. Mutations are tested against the last 100 tickets in that category.
5. Winning mutations are promoted; failed rounds alert a human.

Value captured: prompt quality becomes empirical. The system reached 94.7% accuracy in one tracking-query category after three months, up from 89% at launch.

### LLM Council

The LLM Council is a multi-perspective deliberation tool. It launches six domain perspectives, blind-reviews their answers, then synthesizes a final answer with confidence, consensus, disagreements, next steps, and what would change the answer.

The six perspectives are strategy, customer service, finance, retail, digital marketing, and merchandising. The important part is blind peer review: responses are shuffled and anonymized before reviewers score them on accuracy, insight, and actionability.

Value captured: it reduces single-model “yes-man” failure for high-stakes but not irreversible questions. It is useful for vendor choices, positioning, market entry, budget debates, or post-mortems. It is not for quick factual lookup.

### Punta de Flecha

Punta de Flecha is cross-model adversarial convergence. Instead of six personas inside one model, it forces different architectures to criticize each other across rounds. The current skill has evolved into an async protocol with status/list tools.

Protocol:

1. Model A and Model B analyze independently.
2. Each critiques the other.
3. Rounds continue until the delta is cosmetic or max rounds hit.
4. A final synthesis records consensus, resolved divergences, unresolved divergences, confidence, and red-team issues.

Value captured: it found concrete errors in the Profit Throttle Framework, including static threshold mistakes, the need for dynamic break-even, and the need for marginal MER. It also lowered an overly optimistic AI-native maturity assessment. This is a real adversarial review loop, not a brainstorm.

### Pattern Library

The Pattern Library is the cross-deployment knowledge system. It stores anonymized patterns that new deployments can inherit instead of starting from zero.

Current documented status:

- 21 patterns across 9 domains.
- YAML schema with domain and confidence levels.
- REST API on port 18830 via `operai-patterns.service`.
- Endpoints: `/patterns`, `/patterns/{domain}`, `/stats`, `POST /patterns/contribute`.
- Weekly auto-extraction from memory and audits, followed by anonymization and review.
- Rules: no brand names, no employee names, no absolute financials, no location identifiers; only ratios, workflows, thresholds, and templates.

Value captured: month-one deployments can start with month-six operational wisdom. This is one of the few real compounding moats in the system.

### Profitability Engine v3

The Profitability Engine is a daily DTC profitability system. It calculates contribution margin down to operational decision level and validates against monthly accounting close.

Current status from the master doc: production validated, with March 2026 delta of -0.4% versus the accounting P&L actual.

Architecture:

- Google Sheets business plan is auto-downloaded before snapshot generation.
- Shopify provides orders, revenue, fulfillment locations, refunds, and channel signals.
- Meta, Pinterest, Google/GA4, and TikTok-related data provide paid spend and attribution.
- GA4 supports channel revenue attribution.
- Proxies cover COGS, logistics, TPV/payment costs, cross-border fees, and brand marketing allocation.
- Frontend exists as a standalone dashboard and as an embedded tab in the broader performance dashboard.

Major bugs fixed:

- VAT included in Shopify `subtotal_price`; fixed by subtracting `total_tax`.
- Web orders fulfilled from physical locations were incorrectly counted as DTC; fixed with DTC fulfillment-location filtering.
- Business plan Excel was stale; fixed with Google Sheet auto-refresh.
- Meta pagination required `limit=500` and manual paging.
- Pinterest API has a 90-day limit; fixed with clamping.
- Google Ads aggregation needed campaign breakdown, not total aggregate.
- Brand marketing attribution needed proportional DTC share.
- Validation needed YTD lookback, not short rolling windows.

Value captured: marketing, finance, and merchandising make daily spend and product decisions against contribution margin, not vanity ROAS.

### Profit Throttle Framework

Profit Throttle is the decision layer on top of profitability. It uses two metrics:

- **Blended MER**: overall efficiency.
- **Marginal MER**: efficiency of the latest spend change.

The key correction from adversarial review was that blended MER cannot answer “should we scale?” by itself. A blended MER can look acceptable while the last increment of spend destroys value.

The framework recalculates dynamic break-even MER daily based on returns, COGS, logistics, payment costs, brand ratio, and target profit floor. It produces traffic-light signals: green, yellow, red, black. The production engine later integrates this with a target CM3 on net revenue.

Value captured: paid marketing moves from fixed ROAS targets to dynamic contribution-margin thresholds.

### Knowledge Mining cron and `/learn`

Knowledge Mining distills short-term memory into durable knowledge. The older memory architecture describes a daily cron that reads `memory/`, extracts durable patterns, routes them to the correct context-tree folder, updates indexes, and announces the mined changes.

The April second-brain upgrade added `brain_learn` and a `/learn` skill. Instead of making a human decide where a lesson belongs, the tool accepts a category, location, title, and content, then writes to the right place with timestamping.

Value captured: the system reduces the lag between “we learned something” and “every future agent can use it.”

### Invoice Pipeline

The invoice pipeline scans finance/admin inboxes, detects supplier invoices, extracts invoice data, uploads PDFs to Drive, and appends structured rows to a tracking Sheet.

Flow:

1. Gmail API finds emails with PDF attachments.
2. PDF text is extracted.
3. Regex and heuristics classify invoice documents.
4. Supplier, tax ID, invoice number, concept, base, VAT, total, dates, and payment terms are extracted.
5. PDF is filed by month and origin account.
6. Sheet row is appended with link and confidence.

Initial backfill: 100 emails processed, 117 invoices registered. The current limitation is scanned PDFs and complex tables; OCR and better document parsing remain future improvements.

Value captured: invoice intake becomes daily, structured, searchable, and reviewable.

### Copy Engine

The Copy Engine logs email and web copy performance, then extracts patterns for future campaign creation.

Documented findings include:

- Direct “NEW IN” / “NEW ARRIVALS” subjects outperform narrative storytelling for drops without a supporting editorial campaign.
- If an editorial campaign is coming later, the earlier product drop should not burn the seasonal concept in the subject line.
- In the broader playbook, 1,114 campaigns were analyzed and several subject/body/CTA patterns were identified.

Value captured: creative work gets a memory. Copy decisions cite prior evidence instead of relying only on taste.

### GEO Optimization

The marketing system tracks and optimizes visibility inside AI search engines. Promptwatch research changed the roadmap:

- `llms.txt` was deprioritized because there was no evidence of meaningful ranking impact.
- AI search queries are contextual and comparison-heavy.
- Citable content needs definitions, structured lists, concise answers, question headings, tables, and expert signals.
- GEO is not classic SEO; being cited matters more than ranking for a keyword.

Value captured: the brand prepares for discovery through ChatGPT, Perplexity, Claude, Gemini, and AI Overviews rather than only Google SERPs.

### PR Tracking

The PR tracking system captures tagged social posts, stories, digital clippings, and print clipping inputs into a shared Google Sheet.

Built pieces:

- Instagram posts sheet with metrics, image previews, engagement, and social media value.
- Story capture before 24-hour expiry through webhook and media download.
- Digital clipping sheet with hundreds of verified historical articles.
- Daily workflow that updates sheets, captures stories, and sends an email digest.

Failure captured: webhook downtime caused lost story mentions because stories expire after 24 hours. The system now treats story capture as time-sensitive infrastructure.

### Master Calendar

The Master Calendar consolidated operational, marketing, ecommerce, wholesale, finance, retail, and cross-department events into seven Google sub-calendars.

The critical product lesson: the first Notion timeline/calendar attempts were rejected because they did not match how the team works. The winning solution was native Google Calendar, because the team already uses it.

Current architecture:

- Four source systems feed a Notion master DB or cached markdown.
- Timers run every six hours.
- A final sync writes to seven Google Calendars.
- The team sees read-only native calendars.
- Current snapshot showed 319 events across the seven calendars.

Value captured: operational dates moved from fragmented docs into the surface the team already checks.

### Agent Factory

The Agent Factory pattern decomposes one domain agent into specialized sub-agents. The CS reference implementation shipped with 10 sub-agents and a `factory.yml` declaring inputs, outputs, and order.

What shipped:

- CS factory templates.
- `operai-init factory enable/disable/list/show/status`.
- Ten sub-agent SOULs.
- Documentation in the playbook.

What did not initially ship: runtime orchestration. The first factory release was static artifacts plus CLI install. Later releases added runtime.

Value captured: it points to a future where a single business domain is not one giant prompt, but a factory of specialized workers.

### Factory Runtime and Autonomous MVP

The v0.9.0 runtime converted the Agent Factory into a runnable system:

- `run-once` CLI.
- Mock LLM mode.
- Sequential sub-agent execution.
- Markdown and JSON traces.
- Sample CS tickets.

The v3.0-beta autonomous MVP added:

- Filesystem event queue.
- Brain auto-lookup.
- Brand pre/post hooks.
- Parallel sub-agent dispatch respecting `max_parallel`.
- Review queue.
- Trace JSON to brain memory.
- Event archival.

Smoke tests showed the daemon could pick up an event, run 10 sub-agents, write review output and trace, and archive the event.

Value captured: the repo moved from installable infrastructure to a demonstrable autonomous event processor.

### Webhooks and Slack Digest

The v3.0 stable repo added helpdesk webhooks and daily digest:

- HTTP webhook receiver on localhost service.
- Normalizers for Richpanel, Gorgias, Zendesk, and Intercom.
- HMAC verification per provider, constant-time comparison, fail-closed.
- Canonical ticket events written to the factory queue.
- Daily Slack digest with counters from review and event folders.

Scope still not done: action executor, retries, cost budget enforcement, guardrail meta-agent, dashboard, and six other domain factories.

Value captured: customer events can enter the agent system automatically instead of via manual file drops.

### Agent with corporate card

A lightweight but symbolically important capability: the strategy hub has a limited corporate card for approved autonomous purchases. The documented limit is small, deliberately bounded.

Value captured: autonomy is not just “answering.” It can include controlled spend, but only after explicit guardrails.

---

## 6 · Skills Library

### Current counts

The skills story has three different counting layers:

| Layer | Count | Source |
|---|---:|---|
| Tool-exposed skills | 310 | `skills_list` output on 2026-05-11. |
| Filesystem `SKILL.md` files | 146 | `find brain -path '*/SKILL.md'`. |
| Core `knowledge/skills` docs | 57 files, 21 `SKILL.md` | Current folder count. |
| Older public docs | 167 or 183+ | Historical snapshots; do not use as current truth. |

For the portfolio, the clean claim is: **“310 skills exposed through the internal skills tool; 146 filesystem skill definitions currently present in the brain.”** If that sounds too complicated for a public page, say “300+ internal skills” and put the footnote in a methods section.

### Categories returned by `skills_list`

- Ads crew: 5
- Ads diagnostics: 26
- Ads optimization: 17
- Ads reporting: 11
- Ads other: 7
- AI tools: 3
- Analytics: 3
- Content: 4
- CRO: 7
- Design: 8
- Development: 8
- Ecommerce: 6
- Google Workspace: 18
- Integrations: 10
- Marketing: 12
- Platform: 6
- Research: 9
- SEO: 5
- Other: 145

### 30 high-impact skills

1. **qmd**: search local markdown knowledge and indexed docs.
2. **autoresearch**: optimize a measurable target through autonomous iteration.
3. **adversarial-prompting**: generate, critique, fix, and consolidate a solution.
4. **thinking-partner**: structured reasoning for complex decisions.
5. **google-workspace**: Gmail, Calendar, Drive, Docs, and Sheets workflows.
6. **gws-sheets**: read and write structured spreadsheet data.
7. **gws-calendar**: create and manage calendar events.
8. **gws-gmail-triage**: summarize unread inbox state.
9. **klaviyo**: lifecycle email operations and analysis.
10. **shopify-liquid-themes**: generate Shopify theme sections, snippets, and schema.
11. **liquid-theme-standards**: enforce frontend standards in Liquid themes.
12. **liquid-theme-a11y**: accessibility patterns for ecommerce components.
13. **pricing-strategy**: pricing, packaging, and monetization decisions.
14. **copywriting**: write and improve marketing copy.
15. **copy-editing**: edit existing marketing copy with stronger voice and clarity.
16. **email-sequence**: design lifecycle and nurture sequences.
17. **geo-optimization**: optimize content for AI search visibility.
18. **gsc**: query Google Search Console for pages, queries, CTR, and inspection.
19. **seo-audit**: diagnose technical and content SEO issues.
20. **programmatic-seo**: plan scalable SEO pages using templates and data.
21. **ads-meta-ads-audit**: detect Meta structure, fatigue, overlap, and scaling issues.
22. **ads-google-ads-audit**: find wasted spend, keyword gaps, and bid issues.
23. **ads-ad-spend-allocator**: allocate budget using MER, marginal ROAS, and diminishing returns.
24. **ads-creative-fatigue-detection**: monitor creative exhaustion before performance collapses.
25. **ads-weekly-account-summary**: produce weekly paid-media summaries.
26. **analytics-tracking**: set up or audit analytics and measurement.
27. **page-cro**: optimize landing pages and conversion pages.
28. **ui-audit**: review UI quality, hierarchy, accessibility, and cognitive load.
29. **openclaw-ops**: install, troubleshoot, and harden OpenClaw gateways.
30. **skill-creator**: create and maintain skill definitions.

The important pattern: skills turn tacit methodology into callable procedures. They are the “how” layer that sits between static docs and live tools.

---

## 7 · Infrastructure & Stack

### Production stack

The production system runs on a dual-host architecture:

- **Primary VPS in the EU**: strategy hub, MCP server, brain working copy, crons, dashboards, scripts, public tunnel, operational services.
- **Secondary host on Apple Silicon**: domain agents, local services, port forwarders, browser/session-dependent integrations.
- **Tailscale private network**: connects hosts and admin machines over a private mesh.
- **Cloudflare Tunnel**: exposes the MCP server over HTTPS without opening inbound ports.
- **Google Workspace**: Drive, Docs, Sheets, Calendar, Gmail, service-account domain-wide delegation.
- **OpenClaw**: agent runtime and channels.
- **QMD**: markdown search/indexing.
- **FastMCP / Starlette / Uvicorn**: MCP server implementation.
- **Systemd and LaunchDaemons**: Linux and macOS service management.
- **Vercel**: public/demo web surfaces and dashboards.
- **Business systems**: ecommerce, inventory, ERP/accounting, email marketing, ads, analytics, customer support, logistics, expense management, docs, Slack.

### Cost

The playbook’s current total system cost is **€352/month all-in**. Components documented in the stack chapter:

| Component | Monthly cost |
|---|---:|
| Primary VPS | €15 |
| Secondary host amortization | €22 |
| Mesh networking | €17 |
| Public tunnel | €0 |
| Founder interface subscription | €185 |
| Hub subscription | €20 |
| LLM API usage | ~€93 |
| Total | **€352** |

The key cost insight: several agents run through existing employee ChatGPT subscriptions via OAuth, so incremental API cost drops without relying on unreliable free-tier models.

### Model strategy

The model routing changed over time:

- Phase 1: mostly high-end API models; reliable but costs climbed.
- Phase 2: free/cheap model experiments; looked fine under light load but failed under operational peaks.
- Phase 3: reuse existing team subscriptions via ChatGPT OAuth for several agents; keep Claude Sonnet for customer-facing/sensitive workflows.

The current validated registry says most domain agents run GPT-5.5 via Codex/OpenAI OAuth, while CS uses Claude Sonnet 4 with GPT fallback. Older docs mention GPT-5.4, MiniMax, Kimi, Qwen, and OpenRouter. Those should be treated as historical unless confirmed in the runtime registry.

---

## 8 · Production Lessons

The public playbook says 32 lessons. The current `11b-production-lessons.md` file visibly includes lessons 1-21 and a duplicated lesson 32, while research/plan artifacts document lessons 22-31. For the public portfolio, list all 32 but note internally that the canonical chapter needs repair.

1. **OAuth Token Death Spiral**: shared tokens caused cascading rate-limit failures across agents; fix is one token per agent and capped retries.
2. **Ghost in the Config**: hidden cached OAuth credentials overrode environment settings; always inspect the true auth priority chain.
3. **LaunchDaemons vs LaunchAgents**: macOS services need the right service type and explicit `HOME`.
4. **Config Crash Loop**: one invalid runtime config key can crash an agent; run doctor/validation after edits.
5. **Messaging Reconnection Storm**: unused channels replay messages and cause API storms; minimize channel surface area.
6. **API Header Formats Are Not Universal**: Stockagile required exact token header format; test auth with curl before coding.
7. **Memory Pollution Is Real**: indiscriminate semantic memory degraded responses; dedup and curation are mandatory.
8. **Knowledge Base Is Never Done**: product and policy updates must update the brain or agents go stale.
9. **Shadow Mode Is Non-Negotiable**: roll out autonomy gradually; one bad automated reply costs more than a slower launch.
10. **2FA Dependency Trap**: reverse-engineered web sessions need health checks and relogin plans.
11. **Remove Features That Hurt**: SuperMemory was removed after noise outweighed recall value.
12. **Dual-Host Architecture**: one VPS could not comfortably run the full fleet; split hub and domain agents.
13. **Cloudflare Tunnel for MCP**: public HTTPS access improved team rollout versus VPN-dependent access.
14. **Environment Variables in Cron**: cron has a minimal environment; scripts must source config explicitly.
15. **Skills as Institutional Knowledge**: skills should be shared via MCP, not trapped inside one agent workspace.
16. **ByteRover Config Compatibility**: plugin config must extend existing configs, not replace them with minimal files.
17. **When the API Does Not Exist**: build a microservice when an important workflow has no official endpoint.
18. **Headless Permission Modes**: interactive approval modes hang unattended agents; configure headless-safe permissions.
19. **Never `chmod 777` Plugin Paths**: fix ownership, not world-writable permissions.
20. **Loopback Gateway Port Forwarding**: secure local bindings require explicit private-network proxies for monitoring and MCP access.
21. **Cheap Models Under Load**: free-tier models fail at operational peaks; cheapest reliable routing beats cheapest tokens.
22. **Anti-Prompt-Injection Rollout**: all agent prompts need standard injection hardening; customer-facing agents need extra protection.
23. **ACK Rule**: agents must acknowledge receipt immediately so humans do not resend and duplicate work.
24. **Free-Tier LLMs Do Not Scale**: free/cheap models are fine as fallback, not as primary production runtime.
25. **OpenClaw Is Not `systemd Type=simple`**: forking gateway behavior can create restart loops; use the correct process manager pattern.
26. **APIs Can Be Silently Broken**: vendors can change auth or expire keys without notice; health checks need to watch successful semantics, not just server availability.
27. **Async Event Loop Collision**: Playwright/async scrapers inside async MCP tools need process isolation.
28. **Heartbeat Schema Drift**: runtime upgrades can reject legacy config keys; doctor/fix after upgrades.
29. **ChatGPT OAuth Strategy**: reuse existing subscriptions where reliable; it can reduce incremental API costs.
30. **Cross-Model Personality Anchoring**: model migrations need SOUL/prompt tuning, not only provider swaps.
31. **Swarm Update Procedure**: major runtime changes need staged config fixes and validation across the fleet.
32. **Node Version Compatibility**: Node 25 broke streaming CLI behavior; pin wrappers to Node 22 LTS for affected tools.

---

## 9 · Evolution Timeline

### Late 2025: First useful assistant

The first durable value came from one strategy/personal-assistant style agent, not from a grand architecture. It handled founder context, reminders, synthesis, and operational lookup. This proved the company had enough repeat operational context to justify a brain.

### February-March 2026: Domain agents and shared brain

The system expanded into specialized domain agents. Customer service, finance, retail, marketing, and merchandising each got a workspace, SOUL, channel, tools, and access to shared knowledge. The brain started as hundreds of markdown files and grew quickly through operational use.

By late March, the Brain Protocol described the shared brain as the source of truth for agents and AI clients. The doc count was 409 at that time.

### March 2026: OpenClaw, QMD, memory lessons

The team learned the hard parts of running agents: macOS service management, OAuth isolation, config drift, memory pollution, plugin compatibility, and cross-agent communication. QMD and structured context trees became more important than fuzzy semantic memory.

### Early April 2026: Advanced capabilities discovered

A full swarm audit and compAI update sprint surfaced 15 hidden capabilities that were not clearly represented in the public materials: AutoResearch, invoice pipeline, Council, PR tracking, GEO, profitability, amortization alerts, copy engine, transcription, agent card, wholesale order creation, model optimization, injection hardening, multi-currency, and Taskmaster.

This was the moment the story shifted from “we have agents” to “we have an operating system with accumulated capabilities.”

### 7-17 April 2026: Audits, security, and team rollout

The April 17 audit found 21 issues across agents, MCP, brain, infra, onboarding, credentials, and docs. Ten fixes were executed immediately. The most important lessons: audit agents produce false positives; credential rotation needs operational windows; rate limiting can break SSE if implemented globally; and public setup scripts need to work on real employee machines.

During this period, the MCP server became the team access layer. AI onboarding became mandatory for new hires.

### 17 April 2026: Second-brain upgrade

The Ryan/Mercury-inspired second-brain pass shipped three P0 upgrades:

- Vector/hybrid search tools.
- `/learn` and `brain_learn` for low-friction knowledge capture.
- Per-person `me.md` memory scaffolding.

This moved the system closer to AI-native company behavior: humans and agents can both extend memory.

### 18-21 April 2026: compAI repo build-out

compAI moved through rapid repo versions:

- v2.1 brand bootstrap: one-command install, 25-question discovery, brain skeleton, systemd templates.
- v2.2 CLI: integrations, tunnel, team join, status.
- v2.3 MCP server: 11 tools, bearer auth, roles, key CLI.
- v2.4 ingest layer: DLP, subject registry, evidence store, allowlist, ACL at index boundary.
- v2.5 agentic organization alignment and meta-agents.
- v2.7 CS agent factory reference.
- v2.8 LLM abstraction and usage tracking.
- v2.9 factory runtime run-once.
- v3.0 beta autonomous daemon.
- v3.0 stable helpdesk webhooks and Slack digest.

The strongest part of this phase is not that every piece was complete. It is that each release documented scope boundaries and smoke tests.

### 20-27 April 2026: Profitability Engine closes the loop

The Profitability Engine and Profit Throttle Framework connected the agent system to daily economic decision-making. The engine was validated against accounting actuals, with March matching within 0.4%. This turned the swarm from “ops assistance” into a margin-aware operating layer.

### 24-27 April 2026: Role boundaries and calendar pivot

The Master Calendar project showed a different kind of lesson: adoption beats clever UI. Notion timelines were rejected. Google Calendar shipped because it matched the team’s existing behavior.

On 2026-04-27, the formal role boundary was written: Claude orchestrates, Codex executes technical work, domain agents own operating domains.

### May 2026: AI-native execution plan

The latest strategy doc places the company around L2.1 on the AI-native maturity frame: real agents, real brain, real workflows, but not yet non-engineer-extensible or L4 autonomous. The plan is deliberately anti-bureaucratic: domain `CLAUDE.md` files, simple skill headers, personal memory, semantic search default, action ledger, weekly digest, and `/learn`.

Current status: AI-native in operating behavior, not yet fully AI-native in organization design.

---

## 10 · What Each Employee Now Does Differently

### The CS lead

Before AI: the CS lead answered repetitive “where is my order,” return, size, policy, and complaint questions by switching between helpdesk, ecommerce admin, logistics, and internal docs. Policy edge cases lived in memory or Slack.

Now: the CS lead reviews agent drafts, handles escalations, improves policy docs, and looks for patterns. Routine tracking questions can be resolved through parallel order + logistics lookup. The agent remembers policy and writes internal notes. The human spends more time on VIP cases, tone, and exceptions.

### The finance lead

Before AI: invoices arrived in inboxes, PDFs were manually saved, spreadsheets were updated late, and weekly reporting depended on spreadsheet assembly. Cash and amortization awareness required calendar discipline.

Now: invoice intake runs daily, PDFs are organized, key fields enter Sheets, amortization alerts fire before due dates, and the finance agent can answer natural-language questions against accounting, expense, and cash docs. The human reviews exceptions, approves payments, and makes judgments.

### The retail lead

Before AI: store performance meant revenue reports, anecdotal staff feedback, and delayed diagnosis. Traffic, attraction, conversion, and ticket size were not always decomposed.

Now: store performance can be decomposed into exterior traffic, attraction, conversion, and average ticket. The retail lead can ask which lever changed, not just whether sales changed. Partner/channel reports are treated with source-of-truth rules.

### The digital marketing lead

Before AI: marketing analysis required pulling from Klaviyo, Meta, GA4, GSC, Shopify, and spreadsheets. Copy learnings lived in taste and scattered retrospectives.

Now: campaign performance, copy patterns, GEO opportunities, paid-media health checks, and PR tracking are queryable. The marketing lead uses AI to detect fatigue, summarize performance, draft campaign copy with cited patterns, and prioritize content work.

### The buyer / merchandising lead

Before AI: sell-through, allocation, markdown risk, and channel splits were spreadsheet-heavy and often late.

Now: the merchandising agent can pull product, stock, location, sales, and profitability signals into one analysis. The human still makes taste and buying decisions, but the analytical foundation is faster and more consistent.

### The people / office owner

Before AI: onboarding, leave, policies, expenses, and payroll prep were ad hoc or founder-dependent.

Now: new hires get AI onboarding on day one. Policies live in the brain. Leave data is queryable through a custom microservice. Payroll and expense prep can be drafted for review.

### The founder

Before AI: the founder was the router, memory holder, analyst, and escalation point for too many workflows.

Now: the founder can ask the brain, route to agents, run Council or Punta de Flecha for important decisions, delegate technical work to Codex, and rely on the system to document what was learned. The founder is still a bottleneck for strategy and approvals, but less for retrieval and first-pass analysis.

### The technical operator

Before AI: every integration or data task meant bespoke scripting, manual context gathering, and one-off debugging.

Now: Codex can read the brain, execute on the VPS, inspect source, write scripts, validate, and write back lessons. Claude Code stays closer to orchestration and synthesis. The role boundary prevents technical work from consuming strategic conversation.

---

## 11 · Open Questions / What We're Still Solving

1. **The public numbers are inconsistent.** Docs cite 44, 56, 69, 70, 71, and 84 tools; 167, 183, 146, and 310 skills; 409, 968, 1,324, 1,341, and 1,665 docs/files. This inventory resolves them, but the public site needs a clear measurement convention.

2. **Non-engineers still cannot extend everything.** `/learn` helps, but writing robust skills, connectors, ACL rules, and workflows remains technical. This is the main ceiling on AI-native maturity.

3. **The brain is strong but still founder/technical-operator maintained.** Domain owners do not yet consistently own their own `CLAUDE.md`, skills, and memory hygiene.

4. **Auth is partly in observe mode.** Bearer auth, API keys, ACL groups, and ledgers exist, but current health shows anonymous calls and admin-only inventory. Full enforcement and migration need careful rollout.

5. **Some docs are stale or contradictory.** The Codex setup doc says `/mcp` is 404; the May MCP guide says `/mcp` is preferred. Runtime docs cite GPT-5.4 while registry says GPT-5.5. Public docs need an update pass.

6. **Action execution remains bounded.** Several systems can draft or queue actions, but final sends, payments, approvals, and irreversible state changes still require humans. This is correct for now, but should be explicit.

7. **compAI repo is not the same as the internal swarm.** The repo productized a large share of the architecture, but several internal advantages depend on brand-specific workflows, accumulated data, and custom integrations.

8. **CS factory is ahead of other factories.** The factory pattern exists and CS reference shipped. Other domains remain planned or partially ported.

9. **Webhook receiver does not yet send replies.** v3.0 stable gets events into review queues. Action executor, retries, guardrails, budget enforcement, and dashboard are roadmap.

10. **Ingest Phase 2 is deliberately frozen.** Gmail, Slack, Notion, Drive, and Richpanel ingest require employee-scope exclusion, special-category detection, registry hardening, ACL proof, and encryption review.

11. **Monitoring still evolves after incidents.** MCP event-loop blocking, child-process leaks, webhook downtime, and Node compatibility all required production fixes. The system is resilient because it documents incidents, not because incidents stopped happening.

12. **Agent autonomy is uneven by domain.** CS, finance, and marketing have richer workflows. HR is newer. Retail depends on source coverage. Merchandising has strong analysis but less safe mutation.

13. **Some source systems still require manual exports.** Not every partner or channel has a robust API. The system names these gaps instead of hiding them.

14. **The org chart is still traditional.** The swarm supports teams, but the company has not fully reorganized around human-agent pods or L4 workflows.

15. **The portfolio pivot needs editorial discipline.** The most credible story is not “buy our AI system.” It is “here is what we built, what broke, what worked, and what remains unsolved.”

---

## 12 · References

### Architecture, MCP, agents, and config

- `knowledge/platform/strategy/ai-pilled-execution-simple.md`
- `knowledge/platform/config/audit-swarm-17-abril-2026.md`
- `knowledge/platform/agents/role-boundaries.md`
- `knowledge/platform/tools/mcp-server-guide.md`
- `knowledge/platform/tools/council-query-guide.md`
- `knowledge/platform/tools/council-skill-guide.md`
- `knowledge/platform/tools/laagam-mcp.md`
- `knowledge/platform/tools/laagam-mcp-troubleshooting.md`
- `knowledge/platform/tools/shopify-mcp-integration.md`
- `knowledge/platform/tools/codex-cli-setup.md`
- `knowledge/platform/BRAIN_PROTOCOL.md`
- `knowledge/platform/config/brain-architecture.md`
- `knowledge/platform/config/memory-architecture-playbook.md`
- `knowledge/platform/config/lessons.md`
- `knowledge/platform/agents/agents.md`
- `knowledge/platform/agents/agents-areas.md`
- `knowledge/platform/agents/agent-runtime-registry.md`

### compAI playbook and project docs

- `compai/playbook/00-the-brain.md`
- `compai/playbook/03-architecture.md`
- `compai/playbook/04-agent-cs.md`
- `compai/playbook/05-agent-ops.md`
- `compai/playbook/06-agent-finance.md`
- `compai/playbook/07-agent-marketing.md`
- `compai/playbook/09-agent-retail.md`
- `compai/playbook/09b-agent-merchandising.md`
- `compai/playbook/09c-agent-hr.md`
- `compai/playbook/10-stack.md`
- `compai/playbook/10b-memory-architecture.md`
- `compai/playbook/10c-mcp-server.md`
- `compai/playbook/10d-advanced-capabilities.md`
- `compai/playbook/11b-production-lessons.md`
- `compai/playbook/11f-ingest-layer.md`
- `compai/playbook/16-agentic-governance.md`
- `compai/playbook/17-agent-factory.md`
- `compai/playbook/18-llm-providers.md`
- `compai/playbook/19-factory-runtime.md`
- `compai/playbook/20-mvp-runtime.md`
- `compai/playbook/21-webhooks-digest.md`
- `compai/playbook/22-onboarding-experience.md`
- `compai/playbook/PLAN-v1.7.md`
- `compai/playbook/RESEARCH-2026-04-08.md`
- `compai/playbook/RESEARCH-2026-04-10.md`
- `knowledge/projects/operai/_index.md`
- `knowledge/projects/operai/2026-04-27-anonymization-phase-complete.md`
- `knowledge/projects/operai/agent-factory-v0.6.md`
- `knowledge/projects/operai/brand-bootstrap-v0.1.md`
- `knowledge/projects/operai/brand-bootstrap-v0.2.md`
- `knowledge/projects/operai/brand-bootstrap-v0.3.md`
- `knowledge/projects/operai/brand-bootstrap-v0.4.md`
- `knowledge/projects/operai/brand-bootstrap-v0.5.md`
- `knowledge/projects/operai/factory-runtime-v0.9.0.md`
- `knowledge/projects/operai/repo-v3.0-beta-mvp.md`
- `knowledge/projects/operai/repo-v3.0-stable.md`
- `knowledge/projects/operai/playbook-v1.7-update.md`
- `knowledge/projects/operai/audits/day1-crosscheck-2026-04-26.md`
- `knowledge/projects/operai/audits/playbook-buyer-nontechnical-audit-2026-04-27.md`

### Company operating samples

- `knowledge/laagam/finance/profitability-engine-master.md`
- `knowledge/laagam/finance/profit-throttle-framework.md`
- `knowledge/laagam/finance/invoice-pipeline-2026.md`
- `knowledge/laagam/finance/agent_credit_card.md`
- `knowledge/laagam/operations/master-calendar-laagam.md`
- `knowledge/laagam/marketing/copy-engine-nl-web-insights.md`
- `knowledge/laagam/marketing/geo-promptwatch-learnings.md`
- `knowledge/laagam/marketing/pr-tracking-system.md`
- `knowledge/laagam/retail/00_retail_intelligence_principles.md`
- `knowledge/laagam/team/onboarding-ai-obligatorio.md`

### Memory files examined

- `memory/2026-04-12-codex-seo-top-queries.md`
- `memory/2026-04-13-diego-weekly-email-gap.md`
- `memory/2026-04-13-diego-weekly-emails-2026.md`
- `memory/2026-04-13-ow-launch-draft-full-validation.md`
- `memory/2026-04-13-wow-monday-sunday-gross-breakdown.md`
- `memory/2026-04-13-wow-ow-csv-validation.md`
- `memory/2026-04-13-wow-weekly-april-breakdown.md`
- `memory/2026-04-17-audit-and-refactor.md`
- `memory/2026-04-17-mcp-event-loop-fix.md`
- `memory/2026-04-17-second-brain-upgrade.md`
- `memory/2026-04-20-wow-weekly-13-19-april.md`
- `memory/2026-04-25.md`
- `memory/2026-04-26.md`
- `memory/2026-04-27.md`
- `memory/2026-04-27-weekly-2704-data.md`

### Counts and verification commands run

- `find brain -type f | wc -l`
- `find brain -type f \( -name '*.md' -o -name '*.qmd' \) | wc -l`
- `find brain/knowledge -mindepth 1 -maxdepth 1 -type d...`
- Regex parse of `services/laagam-mcp/server.py` for `@mcp.tool()` registrations.
- `skills_list` MCP call for tool-exposed skills.
- `find brain -path '*/SKILL.md' | wc -l`
- `mcp_health` for runtime health snapshot.
- Direct parse of `/var/log/laagam-mcp.log` for logged tool-call counts.

---

## Final Notes for the Web Redesign

The strongest public story is not “we built a perfect AI company.” It is:

1. We built a company brain.
2. We connected it to real systems through MCP.
3. We put specialized agents on top.
4. We shipped dozens of operational capabilities.
5. We documented what broke.
6. We are still solving extension, governance, auth rollout, and deeper autonomy.

That is credible. It is also harder for competitors to fake than a landing page full of generic agent language.
