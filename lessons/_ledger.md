# Failure Ledger

| # | What failed | Fix | One-rule lesson |
|---:|---|---|---|
| 1 | Shared OAuth tokens caused rate-limit cascades | One token per agent | Isolate credentials by worker |
| 2 | Cached auth overrode env vars | Inspect auth priority chain | Debug the credential actually used |
| 3 | Service manager launched with wrong context | Explicit service config and HOME | Service managers are part of the app |
| 4 | Invalid config created crash loops | Config doctor and validation | Validate before restart |
| 5 | Unused channels replayed messages | Reduce channel surface | Fewer channels, fewer failures |
| 6 | API header assumptions failed | Test auth with curl | Vendor auth differs |
| 7 | Memory pollution degraded answers | Deduplicate and curate | Memory needs hygiene |
| 8 | Brain went stale after policy changes | Add brain updates to checklists | If it is not in the brain, agents do not know it |
| 9 | Autonomy moved too fast | Shadow mode and review queues | Draft first, automate last |
| 10 | 2FA/session dependency broke flows | Session health checks | Browser sessions are dependencies |
| 11 | A memory feature hurt quality | Remove it | Kill harmful features |
| 12 | One host could not run full fleet | Split host roles | Architecture follows load |
| 13 | VPN-only access slowed adoption | Public HTTPS tunnel with auth | Access friction kills adoption |
| 14 | Cron lacked environment variables | Source config explicitly | Cron is not your shell |
| 15 | Skills trapped in one workspace | Share via brain/MCP | Procedures are infrastructure |
| 16 | Plugin config clobbered settings | Merge configs | Merge, do not replace |
| 17 | No official API existed | Build small adapter | Own critical adapters |
| 18 | Interactive permissions hung agents | Headless-safe permissions | Background agents cannot wait |
| 19 | Permissions fixed with chmod 777 | Fix ownership | Never use world-writable shortcuts |
| 20 | Loopback services unreachable safely | Private-network forwarding | Reachability needs design |
| 21 | Cheap models failed under load | Route by reliability | Cheapest reliable wins |
| 22 | Prompt injection hardening uneven | Standard hardening | Assume hostile input |
| 23 | Silent agents caused duplicate asks | ACK rule | Acknowledge fast |
| 24 | Free-tier models treated as production | Fallback only | Free tiers are not infrastructure |
| 25 | Process manager pattern mismatched runtime | Correct service type | Know whether it forks |
| 26 | APIs broke semantically with 200s | Semantic health checks | Uptime is not correctness |
| 27 | Async tool blocked MCP loop | Process isolation | Keep tool servers responsive |
| 28 | Heartbeat schema drift | Doctor/fix after upgrade | Migrate schemas deliberately |
| 29 | Existing paid seats unused | Route through reliable seats | Cost optimization can be architectural |
| 30 | Model swap changed behavior | Retune prompts/SOULs | Provider swaps change behavior |
| 31 | Fleet update too broad | Staged rollout | Update in waves |
| 32 | Node version broke streaming | Pin Node 22 LTS | Pin runtimes that affect IO |

