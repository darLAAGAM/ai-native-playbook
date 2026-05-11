# Playbook Review Notes — 26 March 2026

## Status: NEEDS UPDATES BEFORE LAUNCH

### Critical Fixes Required

#### 1. Timeline Accuracy (Multiple chapters)
- **Problem:** Playbook says "18 months in production" (Ch.1, Ch.12, case study)
- **Reality:** System deployed ~Q3 2025 = ~6-9 months, not 18
- **Fix:** Change to "6+ months" or "since mid-2025" — more defensible
- **Files:** 01-introduction.md, 12-roi.md, case-study/consumer-brand-case-study.md

#### 2. Revenue Claims (Ch.1, Ch.12, case study)
- **Problem:** States 8-figure revenue as fact, "doubled revenue"
- **Reality:** 2025 was ~€5M. 2026 TARGET is €10.1M but we're in March — not achieved yet
- **Fix:** Use "€8M revenue, targeting 8-figure" or "on track for 8-figure revenue" — never state as accomplished
- **Files:** 01-introduction.md, 12-roi.md, case-study header, 00-index.md

#### 3. Agent Roles Don't Match Reality (Ch.3-9)
- **Problem:** Playbook describes 6 agents: CS, Ops/Inventory, Finance, Marketing, Wholesale, Retail
- **Reality:** 6 agents: Strategy Agent (strategy/PA), CS Agent (CS), Finance Agent (Finance), Retail Agent (Retail), Marketing Agent (Digital), Merchandising Agent (Merchandising)
- **Missing:** No dedicated Wholesale agent, no dedicated Ops/Inventory agent
- **Extra:** Merchandising Agent (Merchandising) is a role not in the playbook at all
- **Fix options:** 
  - A) Update playbook to match reality (risky — exposes some gaps)
  - B) Keep playbook as aspirational/generalized framework (safer — it's a product, not documentation)
  - **Recommendation: Option B** — The playbook describes the model, not the exact implementation. But add a note somewhere that real deployments may combine/split roles differently.

#### 4. LLM Model Assignments (Ch.10)
- **Problem:** Says CS uses Opus, Retail uses Gemini Flash
- **Reality:** ALL agents except Strategy Agent use Claude Sonnet-4. Only Strategy Agent uses Opus.
- **Fix:** Update Ch.10 model assignments or generalize ("use your best model for high-stakes, cheaper for routine")

#### 5. Contact Email (Ch.13)
- **Problem:** Uses strategy_agent@oper.ai throughout
- **Reality:** No domain registered. oper.ai was discarded. Name is compAI.
- **Fix:** Update to correct email once domain is registered. For now, use placeholder.

#### 6. ACP/Inter-Agent Communication (Ch.3)
- **Problem:** Describes sophisticated hub-and-spoke routing via ACP
- **Reality:** Agents mostly communicate via Slack, with the founder as intermediary. ACP is configured but rarely used for inter-agent coordination.
- **Fix:** Tone down the sophistication of the orchestration description, or frame it as the target architecture

#### 7. ROI Numbers (Ch.12, case study)
- **Problem:** Some numbers feel optimistic
  - "Recovered wholesale AR €67K" — not verified
  - "Revenue impact €220K" — sum of estimates
  - ROI "54:1" when including revenue impact
- **Fix:** Lead with the solid cost-savings ROI (24:1) which is defensible. Put revenue impact as "additional potential" not hard numbers. Or verify each line.

### Nice-to-Have Updates

#### 8. Add MCP Server Architecture (Ch.10 or new section)
The MCP server (32 tools, SSE endpoint, Tailscale HTTPS, team-wide access) is a significant innovation not documented in the playbook. This is a selling point for managed service clients.

#### 9. Add Merchandising Agent Chapter
Merchandising Agent's role (assortment, pricing, allocation, sell-through analysis) is unique and not covered. Could replace or complement the Wholesale chapter.

#### 10. Add Real Lessons from Production
The brain's `lessons.md` has gold:
- OAuth token death spirals between agents sharing tokens
- LaunchDaemon vs LaunchAgent differences
- `.claude.json` OAuth cache priority over env vars
- `openclaw doctor --fix` as first troubleshooting step
- Stockagile auth header format (`Token X` not `Bearer X`)
These would make Ch.11 (Implementation) much more credible.

#### 11. Knowledge Mining Cron
Ch.10b describes it in detail but unclear if it's actually running in production. If not, either implement it or soften the language.

### Decision Needed from the founder

1. **Revenue claims:** Use 8-figure revenue language?
2. **Agent roles:** Match reality or keep generalized?
3. **Domain:** Register before updating contact info
4. **Metrics verification:** Do we have Richpanel/Shopify data to verify the CS and inventory metrics?

---

## Editorial Rules (Permanent — Apply to ALL Future Updates)

*Added: 1 April 2026*

### The Playbook Sells the SETUP, Not the Brand

compAI's playbook is a guide for how retail/brands should use AI agents to operate more efficiently. It is NOT a case study of any specific brand.

### Data Rules:
1. **NO absolute revenue/sales/EBITDA figures** — use % changes, ratios, multiples only
2. **NO location-identifiable data** — use "Store A (flagship)", "Store B (neighborhood)" etc.
3. **NO employee names** — use roles: "the CS lead", "the finance manager", "the buyer"
4. **NO specific city/country pairs tied to stores** — anonymize geography
5. **NO Notion IDs, API endpoints, Shopify shop names** — implementation details stay internal
6. **NO customer names or wholesale account names**

### What IS OK:
- Agent names (CS Agent, Finance Agent, Retail Agent, etc.) — they're the product
- Rounded credibility markers: "8-figure brand", "€1M+ EBITDA", "50%+ growth"
- Relative metrics: conversion rates, % improvements, ROI multiples, WoW/MoM deltas
- System costs (€610/mo) and infrastructure details (Hetzner VPS, Mac Mini)
- Process descriptions and SOUL.md structures
- Production lessons (anonymized)

### Voice:
- Third person: "the brand", "a production deployment", "in this deployment"
- NOT first person: "our brand", "at our company", "we deployed"
- Exception: Ch.01 Introduction and Ch.13 About section can use "we" for narrative warmth
