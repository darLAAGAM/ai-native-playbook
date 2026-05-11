# Content Rescue Map

*Created: 2026-05-11*  
*Scope: source-map for the build-in-public open-source educational portfolio pivot*  
*Positioning rule: not a product, not a repo-first sales page; this is a concrete operator portfolio for consumer SMEs.*

## File Decisions

| File | Status | Notes |
|---|---|---|
| 00-index.md | REGENERIC | Strong model framing, but Compound Operations Model language needs less proprietary/product voice and more open portfolio framing. |
| 00-the-brain.md | RESCUE | Already brain-first and broadly generic; make artifacts downloadable and add cross-vertical examples. |
| 01-introduction.md | REGENERIC | Move first-person/reference-brand story into a generic consumer SME operator narrative. |
| 02-problem.md | REGENERIC | Typical founder/operator day works across beauty, food, home, wellness, pet, outdoor, fashion, and retail. |
| 03-architecture.md | REGENERIC | Keep three-layer brain and MCP topology; move Tailscale/OpenClaw/host-specific setup detail to appendix. |
| 04-agent-cs.md | REGENERIC | Generic CS is strong; broaden examples from fit/returns to ingredients, specs, defects, subscriptions, delivery, and warranties. |
| 05-agent-ops.md | REGENERIC | Convert inventory/ops to cross-vertical operations: replenishment, lead times, 3PL, variants, supplier issues, and channel exceptions. |
| 06-agent-finance.md | RESCUE | P&L, invoices, cash, debt, and reconciliation are universal; only generalize software names. |
| 07-agent-marketing.md | REGENERIC | Keep lifecycle/ads/SEO/GEO; make examples work for drops, replenishment, promos, subscriptions, retail events, and seasonal launches. |
| 08-agent-wholesale.md | DOWNGRADE TO OPTIONAL | Useful but not universal; position as optional for brands with B2B, marketplaces, distributors, or retail partners. |
| 09-agent-retail.md | REGENERIC | Keep retail-channel analysis; replace physical-store/fashion assumptions with retail locations, pop-ups, counters, concessions, and partners. |
| 09b-agent-merchandising.md | REGENERIC | Strong chapter, but all size-curve language must become variant distribution across size, flavor, scent, color, model, bundle, or pack. |
| 09c-agent-hr.md | RESCUE | People ops, onboarding, leave, payroll prep, and policies are generic SME needs. |
| 10-stack.md | MOVE TO APPENDIX | Valuable technical evidence, but too implementation-heavy for the main operator flow. |
| 10b-memory-architecture.md | RESCUE | Generic and central to the thesis; trim internals only where they slow comprehension. |
| 10c-mcp-server.md | RESCUE | Generic architecture chapter; keep as core because MCP is the interface primitive. |
| 10d-advanced-capabilities.md | REGENERIC | Keep content, add concrete “how to start” and downloadable artifact links per capability. |
| 11-implementation.md | REGENERIC | Reframe from adoption/sales paths to open-source build paths: read, copy artifact, run locally, adapt, ask for help. |
| 11b-production-lessons.md | RESCUE | The failures are the credibility asset; repair numbering and keep the direct incident language. |
| 11c-openclaw-setup.md | MOVE TO APPENDIX | Technical runtime setup, useful for engineers, not main narrative. |
| 11d-eu-ai-act-compliance.md | RESCUE | Compliance is relevant to EU SMEs; keep practical, non-legalistic, and action-oriented. |
| 11e-brand-bootstrap.md | MOVE TO APPENDIX | Useful setup artifact, but “bootstrap repo” reads productized; keep as technical appendix/template. |
| 11f-ingest-layer.md | MOVE TO APPENDIX | Important but technical; main flow should explain safe ingest conceptually, appendix covers DLP/ACL/evidence store. |
| 12-roi.md | REGENERIC | Keep honest math, €352/mo, and 18:1 ROI; make value categories cross-vertical and avoid overclaiming. |
| 13-whats-next.md | DISCARD | Current direction is repo/product-first sales positioning; conflicts with portfolio/open-source educational pivot. |
| 14-team-onboarding.md | REGENERIC | Keep as operator chapter; make it about human adoption and AI literacy rather than tool onboarding only. |
| 15-five-pillars.md | REGENERIC | Useful synthesis if stripped of brand/product rhetoric; turn into editorial principles for AI-native consumer SMEs. |
| 16-agentic-governance.md | RESCUE | Governance/meta-agent idea is generic and important; add clearer limits on autonomy and approvals. |
| 17-agent-factory.md | MOVE TO APPENDIX | Strong technical pattern; main flow should mention it, appendix can show factory.yml and sub-agent runtime detail. |
| 18-llm-providers.md | MOVE TO APPENDIX | Provider abstraction matters for builders; too technical for the main operator journey. |
| 19-factory-runtime.md | MOVE TO APPENDIX | Runtime smoke-test detail belongs in technical appendix. |
| 20-mvp-runtime.md | MOVE TO APPENDIX | Keep as proof artifact, not main story; still useful for builders who want runnable event queues. |
| 21-webhooks-digest.md | MOVE TO APPENDIX | Webhooks/digest are concrete but technical; summarize in capability chapter and keep implementation details in appendix. |
| 22-onboarding-experience.md | MOVE TO APPENDIX | repo onboarding language is product-like; rescue only as technical walkthrough if needed. |
| gtm-notes.md | DISCARD | GTM/sales inspiration does not survive the portfolio-first pivot. |
| PLAN-v1.7.md | SOURCE OF TRUTH (internal) | Internal planning reference; mine for gaps and status, do not publish as chapter. |
| PORTFOLIO-INVENTORY.md | SOURCE OF TRUTH (internal) | Verified inventory and counts; keep internal and use as measurement convention source. |
| RESEARCH-2026-04-08.md | SOURCE OF TRUTH (internal) | Audit/research input; mine for missing capabilities and contradictions. |
| RESEARCH-2026-04-10.md | SOURCE OF TRUTH (internal) | Brain scan input; mine for capability coverage and factual corrections. |
| REVIEW-NOTES-2026-03-26.md | SOURCE OF TRUTH (internal) | Historical review notes; useful for evolution timeline, not public chapter. |
| REVIEW-NOTES-2026-04-08.md | SOURCE OF TRUTH (internal) | Historical review notes; use to explain what changed and why. |

## New Chapter Suggestions

| Suggested chapter | Why it should exist | Likely artifact |
|---|---|---|
| The 30-Second Company Brain | The site needs a first-screen primitive any non-technical CEO can understand fast. | One-page brain diagram, folder template, starter README. |
| Downloadable Artifacts Index | The new positioning depends on letting operators take the actual templates, prompts, schemas, and skills. | Artifact catalog with license and usage notes. |
| Profit Throttle | The portfolio currently hides one of the strongest business-value mechanisms inside advanced capabilities. | MER calculator, threshold rubric, dashboard schema. |
| Pattern Library | This is the compounding layer and maps directly to the G-Brain thesis for SMEs. | YAML schema, examples, anonymization rules, weekly extraction prompt. |
| Council vs Punta de Flecha | Operators need to know when to use multi-perspective deliberation versus adversarial convergence. | Decision matrix and two runnable prompts. |
| Knowledge Mining Loop | The brain only compounds if memory turns into durable docs and skills. | `/learn` template, mining checklist, weekly digest spec. |
| Invoice Pipeline | Concrete back-office automation with immediate SME value and low conceptual friction. | Gmail-to-Drive-to-Sheet schema and extraction prompt. |
| Master Calendar | Strong adoption lesson: use the surface the team already uses. | Event taxonomy, sync spec, calendar naming convention. |
| Live Dashboard Tour | The live dashboard is the wow factor; it needs its own narrative page with what is live and what is still manual. | Screenshot map, metric glossary, data-source table. |
| Capability Maturity Ladder | Honest positioning needs to show what is read-only, draft-only, human-approved, and autonomous. | Autonomy-level rubric and workflow assessment sheet. |
| Consumer SME Stack Map | Readers use different tools; map Shopify/Klaviyo/Holded/Stockagile roles to alternatives. | Integration role matrix by system category. |
| Failure Ledger | The Stripe/Basecamp-style credibility comes from incidents, not polish. | Production lesson index with incident, fix, and reusable rule. |

## Editorial Notes

- Main flow should be brain-first: brain, tools, agents, capabilities, lessons, artifacts, live dashboard.
- Technical appendix should keep the repo/runtime material without letting it dominate the operator story.
- Wholesale stays optional. Retail stays optional by channel, but retail-location logic still matters for many consumer SMEs.
- Avoid a single ambiguous “docs” claim. Use the measurement convention from `PORTFOLIO-INVENTORY.md`.
