# Punta de Flecha Prompt

Use for adversarial cross-model review of expensive, irreversible, or publishable decisions.

Question / claim:

Context:

Round 0:
- Model A answers independently.
- Model B answers independently.

Round N:
- Model A critiques Model B: errors, missing evidence, weak assumptions.
- Model B critiques Model A: errors, missing evidence, weak assumptions.
- Each model revises.

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

