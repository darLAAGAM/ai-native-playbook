#!/usr/bin/env python3
"""Build a single-file HTML version of the AI-Native Playbook.

This repo snapshot did not include the original site builder, so this script is
intentionally dependency-free. It validates the chapter list and emits a readable
HTML artifact at `site/playbook/index.html`.
"""

from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "site" / "playbook" / "index.html"


CHAPTERS = [
    ("Index", "00-index.md", "Table of Contents"),
    ("Overview", "00-the-brain.md", "The Company Brain"),
    ("Overview", "00a-30-second-brain.md", "The 30-Second Company Brain"),
    ("Overview", "00b-live-dashboard.md", "Live Dashboard Tour"),
    ("Overview", "00c-artifacts-index.md", "Downloadable Artifacts Index"),
    ("Overview", "00d-maturity-ladder.md", "Capability Maturity Ladder"),
    ("Overview", "01-introduction.md", "Introduction"),
    ("Overview", "02-problem.md", "The Problem"),
    ("Overview", "03-architecture.md", "Architecture"),
    ("Agents", "04-agent-cs.md", "Agent: Customer Intelligence"),
    ("Agents", "05-agent-ops.md", "Agent: Inventory & Supply Chain"),
    ("Agents", "06-agent-finance.md", "Agent: Finance & Reporting"),
    ("Agents", "07-agent-marketing.md", "Agent: Marketing & Lifecycle"),
    ("Agents", "08-agent-wholesale.md", "Agent: Wholesale & B2B"),
    ("Agents", "09-agent-retail.md", "Agent: Retail & Physical"),
    ("Agents", "09b-agent-merchandising.md", "Agent: Merchandising, Wholesale & Assortment"),
    ("Agents", "09c-agent-hr.md", "Agent: HR & People Ops"),
    ("Results", "10-stack.md", "The Technology Stack"),
    ("Results", "10b-memory-architecture.md", "Memory Architecture"),
    ("Results", "10c-mcp-server.md", "The MCP Server"),
    ("Results", "10d-advanced-capabilities.md", "Advanced Operational Capabilities"),
    ("Results", "10e-profit-throttle.md", "Profit Throttle"),
    ("Results", "10f-pattern-library.md", "The Pattern Library"),
    ("Results", "10g-knowledge-mining.md", "The Knowledge Mining Loop"),
    ("Results", "10h-council-vs-flecha.md", "Council vs Punta de Flecha"),
    ("Results", "10i-invoice-pipeline.md", "The Invoice Pipeline"),
    ("Results", "10j-master-calendar.md", "The Master Calendar"),
    ("Results", "10k-stack-map.md", "Consumer SME Stack Map"),
    ("Results", "11-implementation.md", "Implementation Paths"),
    ("Results", "11b-production-lessons.md", "Lessons from Production"),
    ("Results", "11g-failure-ledger.md", "The Failure Ledger"),
    ("Results", "11c-openclaw-setup.md", "OpenClaw Runtime Setup"),
    ("Results", "11d-eu-ai-act-compliance.md", "EU AI Act Compliance"),
    ("Results", "11e-brand-bootstrap.md", "Brand Bootstrap"),
    ("Results", "11f-ingest-layer.md", "Ingest Layer"),
    ("Results", "12-roi.md", "ROI Analysis"),
    ("Results", "14-team-onboarding.md", "Team Onboarding"),
    ("Future", "15-five-pillars.md", "The 5 Pillars"),
    ("Future", "16-agentic-governance.md", "Agentic Governance"),
    ("Future", "17-agent-factory.md", "Agent Factory Pattern"),
    ("Future", "18-llm-providers.md", "LLM Provider Abstraction"),
    ("Future", "19-factory-runtime.md", "Factory Runtime"),
    ("Future", "20-mvp-runtime.md", "MVP Runtime"),
    ("Future", "21-webhooks-digest.md", "Webhooks + Slack Digest"),
    ("Future", "22-onboarding-experience.md", "The Onboarding Experience"),
]


def slug(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def render_markdown(md: str) -> str:
    """Small markdown renderer for headings, paragraphs, fences, and tables."""
    blocks: list[str] = []
    in_code = False
    code_lines: list[str] = []
    para: list[str] = []

    def flush_para() -> None:
        if para:
            blocks.append(f"<p>{html.escape(' '.join(para))}</p>")
            para.clear()

    for raw in md.splitlines():
        line = raw.rstrip()
        if line.startswith("```"):
            if in_code:
                blocks.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
                code_lines.clear()
                in_code = False
            else:
                flush_para()
                in_code = True
            continue
        if in_code:
            code_lines.append(line)
            continue
        if not line:
            flush_para()
            continue
        if line.startswith("#"):
            flush_para()
            level = min(len(line) - len(line.lstrip("#")), 3)
            text = line.lstrip("#").strip()
            ident = slug(text)
            blocks.append(f'<h{level} id="{ident}">{html.escape(text)}</h{level}>')
            continue
        if line.startswith("|"):
            flush_para()
            blocks.append(f"<pre>{html.escape(line)}</pre>")
            continue
        para.append(line)

    flush_para()
    if code_lines:
        blocks.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
    return "\n".join(blocks)


def main() -> int:
    missing = [name for _, name, _ in CHAPTERS if not (DOCS / name).exists()]
    if missing:
        print("ERROR missing chapters:")
        for name in missing:
            print(f" - {name}")
        return 1

    nav = []
    current_section = None
    body = []
    for section, filename, title in CHAPTERS:
        if section != current_section:
            if current_section is not None:
                nav.append("</ul>")
            nav.append(f"<h3>{html.escape(section)}</h3><ul>")
            current_section = section
        anchor = slug(filename.removesuffix(".md"))
        nav.append(f'<li><a href="#{anchor}">{html.escape(title)}</a></li>')
        source = (DOCS / filename).read_text(encoding="utf-8")
        body.append(f'<article id="{anchor}" data-source="{html.escape(filename)}">')
        body.append(render_markdown(source))
        body.append("</article>")
    nav.append("</ul>")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        "<!doctype html>\n"
        "<html lang=\"en\"><head><meta charset=\"utf-8\">"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
        "<title>AI-Native Playbook</title>"
        "<style>"
        "body{font-family:-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif;margin:0;color:#151515;background:#fafafa;}"
        "main{max-width:920px;margin:0 auto;padding:48px 22px 80px;background:white;}"
        "nav{max-width:920px;margin:0 auto;padding:24px 22px;background:#f0f0ed;border-bottom:1px solid #ddd;}"
        "article{padding-top:36px;border-top:1px solid #e4e4e0;margin-top:36px;}"
        "h1,h2,h3{line-height:1.15;}p{line-height:1.65;}pre{white-space:pre-wrap;background:#f6f6f3;padding:12px;border-radius:6px;overflow:auto;}"
        "a{color:#174ea6;}code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;}"
        "</style></head><body><nav><h1>AI-Native Playbook</h1>"
        + "\n".join(nav)
        + "</nav><main>"
        + "\n".join(body)
        + "</main></body></html>\n",
        encoding="utf-8",
    )
    print(f"Built {OUTPUT.relative_to(ROOT)}")
    print(f"Chapters: {len(CHAPTERS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
