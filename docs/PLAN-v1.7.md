# Playbook v1.7 Update Plan

*Based on RESEARCH-2026-04-08.md. Needs the founder approval before executing.*

---

## Scope

Update the compAI playbook from v1.6 → v1.7 with everything learned and shipped in April 2026 (operational audit, MiniMax pivot, new lessons, honest ROI, openclaw-ops toolrepo, 15 hidden capabilities, Implementation Protocol methodology, pattern library).

**Editorial compliance:** All updates follow `knowledge/projects/operai/playbook-editorial-rules.md` — no absolute revenue, no employee names, no location identifiers. Third-person voice.

---

## Execution Order

### Phase A — Core ROI & Cost Alignment (HIGH)

**A1. Rewrite Ch.12 (ROI)**
- Replace human team table with honest hours-saved math
- Show €77,584/year value from 62 hours/week across 8 agents
- Use €21/h loaded labor cost (from BP Personnel €1.5M / 35 FTE) and €40/h founder opportunity cost
- Final ratio: **18:1** (€77.6K / €4.2K)
- Keep "speed", "coverage", "intelligence" sections as qualitative wins (not claimed as ROI)
- Remove revenue impact claims that aren't verifiable (recovered AR, prevented stockouts estimates)
- Add ROI Calculator section matching the live.html breakdown

**A2. Update Ch.3 (Architecture) cost references**
- Replace "€200-400/month" with "€352/month"
- Replace "€12,000-15,000/month human equivalent" with "roughly €6,500/month in saved labor hours"
- Update diagram footer: 1,341 brain docs, 44 MCP tools, 167 skills

### Phase B — Stack & Model Reality (HIGH)

**B1. Rewrite Ch.10 (Stack) model matrix**
- New table:
  | Role | Primary | Fallback 1 | Fallback 2 | Why |
  |---|---|---|---|---|
  | Hub | GPT-5.4 | Opus 4.6 | MiniMax M2.5 | Orchestration needs top reasoning |
  | CS | Opus 4.6 | Sonnet 4 | MiniMax M2.5 | Customer-facing tone non-negotiable |
  | Finance | MiniMax M2.5 | Qwen 3.6 Plus (paid) | Sonnet 4 | Structured reporting |
  | Retail | MiniMax M2.5 | Qwen 3.6 Plus | Sonnet 4 | Data extraction + alerts |
  | Marketing | MiniMax M2.5 | Qwen 3.6 Plus | Sonnet 4 | Analysis + segmentation |
  | Merch | MiniMax M2.5 | Qwen 3.6 Plus | Sonnet 4 | Allocation + sell-through |
  | HR | MiniMax M2.5 | Qwen 3.6 Plus | Sonnet 4 | Admin + payroll prep |
- Add paragraph: "We tested free-tier models (Qwen 3.6 Plus, Kimi K2.5) for 2 weeks. Both saturated with rate limits during peak hours. MiniMax M2.5 at $0.12/M input tokens is the sweet spot — cheap enough to matter, stable enough to trust."
- Add "Infrastructure Hardening" subsection: 3 LaunchDaemons per agent (gateway + watchdog + port forwarder), openclaw-ops toolrepo, Cloudflare Tunnel for MCP, loopback binding + asyncio TCP proxy pattern

**B2. Update Ch.10c (MCP Server)**
- Update counts: 44 tools (from 41), 167 skills (from 152), 1,341 brain docs indexed
- Add QMD (Quoted Markdown) v2.0.1 section: hourly cron, 128+ vectors, 4-tier retrieval
- Add security hardening: `chmod -R 755`, `chown` not `chmod` principle, `openclaw security-scan` baseline scores
- Update Cloudflare Tunnel section to reflect permanent systemd deployment

### Phase C — New Production Lessons (HIGH)

**C1. Add Lessons 22-28 to Ch.11b**

- **Lesson 22: The Anti-Prompt-Injection Hardening Rollout**  
  Story: All SOULs got a standard anti-injection section in April. CS agent got extra because it processes customer-facing tickets. Prevention > detection. Template applied identically across the fleet.

- **Lesson 23: The ACK Rule — Never in Silence**  
  Story: Agents were starting work silently without confirming receipt of a human message. Humans assumed the message was lost and re-sent, causing duplicate work. Fix: immediate ACK as a hard SOUL rule, with per-agent personality for warmth. Result: zero "did you get my message?" pings in 1 week.

- **Lesson 24: Free-Tier LLMs Don't Scale — The MiniMax Pivot**  
  Story: Qwen 3.6 Plus free and Kimi K2.5 free were saturated with rate limits during peak operational hours. The "free tier strategy" lasted 3 weeks before we pivoted to MiniMax M2.5 at $0.12/M input. Cheap enough to matter, stable enough to trust. Free-tier remains a fallback, not primary.

- **Lesson 25: OpenClaw ≠ systemd Type=simple**  
  Story: Attempted to run Strategy Agent's gateway under systemd on the Linux VPS. Infinite restart loop. OpenClaw's parent process forks a child and exits cleanly — systemd interprets exit 1 as failure, kills the child, restarts the parent. Rule: on Linux VPS use `cron @reboot`, never systemd Type=simple for OpenClaw. On macOS, LaunchDaemons work perfectly.

- **Lesson 26: When the API Exists But Is Silently Broken**  
  Story: Richpanel API returned HTTP 403 on all endpoints from one day to the next. Auth was identical to yesterday. Vendor had silently changed auth format or expired keys with no notification. Learning: every external API needs a health check cron that alerts on status changes — not just when it breaks, but when the baseline response shape changes.

- **Lesson 27: TC Analytics + MCP Event Loop Collision**  
  Story: TC Analytics scraper uses Playwright (asyncio). Runs fine standalone. When wrapped as an MCP tool (also asyncio), the event loops collide and the scraper hangs. Fix: `subprocess.Popen(..., start_new_session=True)` to fork a clean process. Rule: if an MCP tool needs asyncio for its work, isolate it in a subprocess.

- **Lesson 28: Heartbeat Config Schema Drift**  
  Story: OpenClaw v2026.4+ tightened its config schema. Legacy keys in heartbeat config (`intervalMinutes`, `interval`) were silently accepted in v2026.3 but rejected in v2026.4 — `openclaw doctor` fails loudly with "Unrecognized keys". Always run `openclaw doctor --fix` after any runtime upgrade, and keep configs minimal.

### Phase D — New Content: Advanced Capabilities (MED)

**D1. Create new Ch.10d — Advanced Operational Capabilities**

Structure:
- Intro: "Most AI agent demos show one capability at a time. This chapter documents the 15+ specialized capabilities that have accumulated in the system over 6+ months."
- Sections:
  1. **AutoResearch** — self-evolving prompts, 94.7% CS accuracy
  2. **LLM Council** — 6 domain experts + blind peer review, ~$1/deliberation
  3. **Invoice Pipeline** — email OCR → Drive → Sheet reconciliation
  4. **Profitability Engine** — CM3 per product across 9 APIs
  5. **Copy Engine** — campaign analysis (1,114 campaigns), learned patterns
  6. **GEO Optimization** — AI search engine ranking (ChatGPT/Perplexity)
  7. **Amortization Alerts** — 48h advance warning on credit lines
  8. **Video Transcription** — local faster-whisper, zero cost
  9. **Taskmaster Protocol** — cascading contracts between agent steps
  10. **Anti-Prompt-Injection CS** — hardened ticket processing
  11. **Multi-Currency Operations** — 6 currencies via Revolut
  12. **3-Tier Model Optimization** — MiniMax primary, Sonnet/Opus escalation

**D2. Document the Pattern Library**

New subsection in Ch.13 (What's Next):
- **The Cold-Start Advantage** — how accumulated operational wisdom transfers to new clients
- Level 1: curated patterns (21 across 9 domains)
- Level 2: automated extraction cron + REST API
- Anonymization rules (no brands, no names, no absolute numbers)
- Client flow: pull baseline → agents start with accumulated wisdom → contribute new patterns back

### Phase E — Methodology (LOW)

**E1. Add Implementation Protocol section to Ch.11**

New H2 section at the top of the Implementation chapter:
- "How to Build With AI-Assisted Development"
- The 3-phase rule: Research → Plan → Implement
- Why it works: the creative work happens in planning, implementation should be boring
- When to skip: trivial fixes, urgent production issues
- The annotation cycle as the value multiplier

### Phase F — Final Polish (LOW)

**F1. Update 00-index.md**
- Bump to v1.7
- Update changelog line:
  > Version 1.7 · April 2026 — Honest 18:1 ROI with justified math, MiniMax M2.5 pivot (free tiers don't scale), 7 new production lessons (lessons 22-28), openclaw-ops toolrepo, advanced capabilities chapter (Ch.10d), Implementation Protocol methodology, cross-company pattern library, anti-prompt-injection hardening, ACK rule.

**F2. Editorial pass**
- Ch.3, Ch.10, Ch.12: replace any remaining "we"/"our brand" with third-person
- Check all hard numbers against audit doc
- Verify no employee names, no specific geography, no absolute revenue

**F3. Update REVIEW-NOTES-2026-03-26.md → REVIEW-NOTES-2026-04-08.md**
- Mark resolved items from March review
- Note what's new in v1.7

---

## Files Touched

| File | Action |
|---|---|
| `00-index.md` | Update version line, add Ch.10d to TOC |
| `03-architecture.md` | Update cost refs, diagram numbers |
| `10-stack.md` | Rewrite model matrix, add hardening section |
| `10c-mcp-server.md` | Update tool/skill counts, add QMD, add security |
| `10d-advanced-capabilities.md` | **NEW** — 15 capabilities documented |
| `11-implementation.md` | Add Implementation Protocol section |
| `11b-production-lessons.md` | Add Lessons 22-28 |
| `12-roi.md` | Rewrite with honest math |
| `13-whats-next.md` | Add pattern library section |
| `REVIEW-NOTES-2026-04-08.md` | **NEW** — supersedes March review |

**Total:** 9 files updated + 2 new files.

---

## Open Questions (same as research doc — need the founder's call)

1. **ROI number:** 18:1 honest (€77K/€4.2K) or keep higher with revenue impact?
2. **Ch.10d new chapter or fold into existing?** Prefer new chapter for discoverability.
3. **Pattern library:** Public differentiator or internal tool?
4. **Version number:** v1.7 or v2.0?
5. **Lesson anonymization:** Keep agent names (they're the product) or genericize?

**My recommendations:**
1. **18:1 honest** — sales conversations survive scrutiny, the higher number doesn't
2. **New Ch.10d** — 15 capabilities need their own home, folding would bury them
3. **Public differentiator** — this is the compounding moat, lead with it
4. **v1.7** — scope doesn't warrant 2.0; save that for a structural rewrite
5. **Keep agent names** — they're already anonymized (Strategy Hub, CS Agent, etc.) in the lessons — match the live.html convention

---

## Estimated Scope

- ~2,000-3,000 words of new content
- ~1,500 words of revisions
- No code changes (pure documentation)
- Editorial pass across 9 existing files
