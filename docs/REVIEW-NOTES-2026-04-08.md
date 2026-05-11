# Playbook Review Notes — 8 April 2026

*Supersedes REVIEW-NOTES-2026-03-26.md*

## Status: v1.7 SHIPPED

Comprehensive update applied following Implementation Protocol (Research → Plan → Implement). See `RESEARCH-2026-04-08.md` and `PLAN-v1.7.md` for the full audit trail.

---

## What Changed in v1.7

### New Content

| File | Type | Summary |
|---|---|---|
| `10d-advanced-capabilities.md` | **NEW** | 15 specialized capabilities: AutoResearch, LLM Council, Invoice Pipeline, Profitability Engine, Copy Engine, GEO Optimization, Amortization Alerts, Video Transcription, Taskmaster Protocol, Pattern Library, and more |
| `11b-production-lessons.md` | +7 lessons | Lessons 22-28: Anti-prompt-injection hardening, ACK rule, MiniMax pivot, OpenClaw vs systemd, silent API breakage, asyncio event loop collision, heartbeat schema drift |
| `11-implementation.md` | +Implementation Protocol section | 3-phase methodology (Research → Plan → Implement), adapted from boristane.com |
| `13-whats-next.md` | Pattern library is live | Cross-company knowledge system now documented as shipped (was "Coming"), with REST API details and anonymization rules |

### Rewrites

| File | Type | Summary |
|---|---|---|
| `12-roi.md` | Full rewrite | Honest 18:1 ROI based on 62 hours/week saved × loaded labor cost (€77,584/year value / €4,224/year cost). No more loose revenue impact claims. |
| `10-stack.md` | Full rewrite | New model matrix with MiniMax M2.5 primary for 4 domain agents. Infrastructure hardening section (3 LaunchDaemons per agent, loopback binding, port forwarders, openclaw-ops toolrepo). |
| `10c-mcp-server.md` | Major update | 44 tools, 167 skills, 1,341 brain docs, permanent Cloudflare Tunnel, QMD v2.0.1 semantic search, security hardening section |

### Updates

| File | Summary |
|---|---|
| `00-index.md` | v1.7 changelog, Ch.10d added to TOC, updated lessons count (28) and thesis numbers |
| `01-introduction.md` | ROI corrected to 18:1 |
| `03-architecture.md` | Cost refs updated to €352/mo, brain doc count 1,341, 7 agents, honest labor comparison |
| `04-agent-cs.md` | ROI refs updated |
| `10b-memory-architecture.md` | Brain doc count 1,341 |

---

## Critical Items Resolved From March Review

| March Item | Resolution |
|---|---|
| Timeline accuracy (18 months claim) | ✅ Now says "6+ months in production" consistently |
| Revenue claims (8-figure revenue as fact) | ✅ Now "eight-figure revenue" or "a production deployment" — no specific numbers |
| Agent roles mismatch | ✅ Playbook matches reality: 8 agents (7 production + Claude Code founder interface) |
| LLM model assignments | ✅ Ch.10 rewritten with current reality: MiniMax M2.5 primary for 4 agents, Opus for CS, GPT-5.4 for hub |
| Contact email | ✅ hello@useoperai.com everywhere |
| ACP/inter-agent communication | Still described as hub-and-spoke; matches current reality now that ACK rule is live |
| ROI numbers | ✅ Honest 18:1 with full auditable math in Ch.12 |
| MCP server not in playbook | ✅ Full Ch.10c with 44 tools, security hardening, Cloudflare Tunnel |
| Merchandising agent missing | ✅ Ch.09b exists, Merchandising Agent's role is Merchandising & Wholesale |
| Real lessons from production | ✅ 28 lessons total (21 original + 7 new in v1.7) |
| Knowledge Mining cron running? | ✅ Confirmed running daily 06:00 UTC, documented in Ch.10b |

---

## Known Items Still Pending

1. **HR Agent (HR agent) gateway** — still on internal scripts mode, no OpenClaw gateway yet. Ch.09c notes this accurately.
2. **Richpanel API key** — expired/silently broken, pending regeneration. Documented in Lesson 26.
3. **Holded Leaves password** — pending a team member renewal. Microservice documented in Lesson 17.
4. **LinkedIn scraper** — requires interactive browser session on Mac Mini, not fully autonomous yet. Not documented in playbook (low priority).
5. **compai.com/compai.ai domain** — not registered, contact uses hello@useoperai.com as fallback.

---

## Editorial Compliance Audit

All v1.7 content follows the editorial rules in `knowledge/projects/operai/playbook-editorial-rules.md`:

- ✅ NO absolute revenue/EBITDA figures
- ✅ NO location-identifiable data (stores are "Store A", "Store B")
- ✅ NO employee names (agent names are OK — they're the product)
- ✅ NO customer or wholesale account names
- ✅ NO Notion IDs, API endpoints, shop names
- ✅ Third-person voice consistently applied to new content (older chapters may still have "we" in narrative sections like Ch.01 and Ch.13 — this is intentional per the editorial rules exception)
- ✅ Relative metrics only (% improvements, ratios, WoW/MoM deltas)
- ✅ System costs (€352/mo) and infra details are OK to expose

---

## Files in the Playbook Directory (Post v1.7)

```
00-index.md                      v1.7 updated
01-introduction.md               ROI corrected
02-problem.md                    no changes needed
03-architecture.md               costs + doc count updated
04-agent-cs.md                   ROI updated
05-agent-ops.md                  no changes needed
06-agent-finance.md              no changes needed
07-agent-marketing.md            no changes needed
08-agent-wholesale.md            no changes needed
09-agent-retail.md               no changes needed
09b-agent-merchandising.md       no changes needed
09c-agent-hr.md                  no changes needed
10-stack.md                      FULL REWRITE — MiniMax matrix, hardening
10b-memory-architecture.md       doc count updated
10c-mcp-server.md                MAJOR UPDATE — 44 tools, QMD, security
10d-advanced-capabilities.md     NEW — 15 capabilities
11-implementation.md             Implementation Protocol section added
11b-production-lessons.md        +7 lessons (22-28)
12-roi.md                        FULL REWRITE — honest 18:1
13-whats-next.md                 Pattern library moved to "Live"
14-team-onboarding.md            email updated
gtm-notes.md                     unchanged
REVIEW-NOTES-2026-04-08.md       NEW (this file)
RESEARCH-2026-04-08.md           research phase artifact
PLAN-v1.7.md                     plan phase artifact
```

**Total:** 22 markdown files in the playbook + 3 process artifacts (research, plan, review notes).

---

## Sign-off

Playbook v1.7 is ready for distribution. Every number in the ROI chapter is defensible. Every lesson in Ch.11b maps to a real production incident documented in the brain. Every capability in Ch.10d is running in the current deployment.

If someone asks "how did you calculate 18:1?", you walk them through Ch.12 and show them exactly the hours × rate math. No hand-waving.
