---
prompt: punta-de-flecha
domain: meta
---

# Punta De Flecha Prompt

```text
Use for adversarial cross-model review of expensive, irreversible, or publishable decisions.

Question / claim:
{{question}}

Context:
{{context}}

Evidence:
{{evidence}}

Round 0:
- Model A answers independently.
- Model B answers independently.

Round N:
- Model A critiques Model B: errors, missing evidence, weak assumptions, and failure modes.
- Model B critiques Model A: errors, missing evidence, weak assumptions, and failure modes.
- Each model revises.

Fact-check:
- Mark key claims as verified, inferred, or unknown.

Red team:
- Attack the emerging consensus before final synthesis.

Stop when:
- Remaining delta is cosmetic, or
- Maximum rounds reached, or
- Both models state they cannot improve materially.

Final output:
- Recommendation
- Consensus points
- Resolved divergences
- Unresolved divergences
- Confidence
- Red-team risks
- Owner decision
- Review date
```
