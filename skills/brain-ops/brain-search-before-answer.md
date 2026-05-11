---
skill: brain-search-before-answer
domain: brain-ops
complexity: low
prerequisites: knowledge base/search available
---

# Brain Search Before Answer

## Purpose

Force agents to retrieve institutional context before answering company-specific questions.

## Use When

Use this skill when an operator needs a repeatable procedure for force agents to retrieve institutional context before answering company-specific questions.

## Inputs

- User question
- Brain/search tool
- Relevant collections

## Procedure

1. Classify whether the question is about the business, customers, policies, tools, prior decisions, or private operating context.
2. Search the brain before answering. Use lexical search for exact names/metrics and semantic search for concepts.
3. Read the most relevant documents, not just snippets, when the answer depends on detail.
4. Answer with citations or source paths where useful.
5. State what is verified, inferred, or unknown.

## Output

- Search query used
- Sources checked
- Answer
- Confidence

## Guardrails

- Do not invent internal facts.
- If search fails, say so and ask or inspect source systems.

## How to adapt

Define which topics require search and which collections/tools are source of truth.
