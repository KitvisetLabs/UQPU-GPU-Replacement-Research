# Batch 046 — New-Discovery Article Registry and Promotion Gate

**Status:** repository-governance / executable evidence gate  
**Permanent directive:** INV-037  
**Canonical publication root:** `articles/`  
**Date:** 2026-09-14

## Research Attribution

- Research Owner / Principal Investigator / Research Direction: **Kanutsanan Pongpanna**
- Facebook: https://www.facebook.com/LoveMoneyTH
- YouTube: https://www.youtube.com/@LoveMoneyTHOfficial
- AI Research Agent: **OpenAI GPT-5.6 Sol**
- AI-assisted contribution: evidence-status design, domain-specific discovery promotion rules, executable gate/tests, directory architecture, frozen certificate, documentation and PR preparation.

Attribution in future articles must list only contributors/models/agents that actually participated in that specific result.

## Owner direction

Future genuinely new findings in physics, science and mathematics must be preserved as visible articles in a dedicated repository folder. The publication area must remain easy to find and must expand as research continues.

## Implementation

Batch 046 creates a root-level `articles/` registry with three permanent domains:

- `articles/physics/`
- `articles/science/`
- `articles/mathematics/`

It also creates:

- `00D_NEW_DISCOVERY_ARTICLES.md` — root-level permanent directive;
- `articles/README.md` — canonical index and evidence-status policy;
- `articles/ARTICLE_TEMPLATE.md` — reusable article contract;
- `software/uqpu-prototype/uqpu/discovery_article_gate.py` — executable promotion rules;
- `software/uqpu-prototype/tests/test_discovery_article_gate.py` — domain/status validation tests;
- permanent folder/policy checks in `test_project_invariants.py`;
- `benchmarks/results/batch046-new-discovery-article-gate.json` — frozen governance certificate.

## Evidence ladder

The registry separates five states:

1. `HYPOTHESIS_OR_PROPOSAL`
2. `PROJECT_REPRODUCED_RESULT`
3. `INDEPENDENTLY_REPRODUCED_CANDIDATE`
4. `VERIFIED_DISCOVERY`
5. `ESTABLISHED_EXTERNAL_DISCOVERY`

This allows high-imagination work to be published early without laundering a hypothesis into a discovery claim.

## Promotion gates

### Physics / empirical science

A `VERIFIED_DISCOVERY` record must include independent validation and uncertainty/error analysis in addition to the common novelty/prior-art, reproducibility, falsifier, limitation and attribution fields.

### Mathematics

A `VERIFIED_DISCOVERY` record must include independent validation plus a complete proof or formal artifact. Numerical agreement or symbolic fitting alone cannot satisfy the proof gate.

### External discoveries

`ESTABLISHED_EXTERNAL_DISCOVERY` requires explicit external discoverer/source attribution so the project cannot silently take ownership of public results.

## Publishable result

The publishable result of Batch 046 is **not a new scientific discovery**. It is a reproducible governance mechanism ensuring that future candidate discoveries are preserved visibly while the word `VERIFIED_DISCOVERY` remains evidence-gated.

## Evidence classification

```text
classification:
  NEW_DISCOVERY_ARTICLE_REGISTRY_AND_PROMOTION_GATE

evidence_level:
  RESEARCH_GOVERNANCE_EXECUTABLE
```

## Non-claims

Batch 046 does not retroactively promote any UQPU theory, model, simulation, symbolic-regression output, internal reproduction or AI-generated equation into a verified discovery or new law. It does not establish real-QPU advantage, quantum advantage, GPU/NPU/RAM/DRAM/HBM replacement, `>=100x`, `>=100,000,000x`, or Data-Center-to-One-Phone achievement.

## Next gates

1. Wire the article registry into future research-batch closing procedure: every batch must explicitly answer whether an article trigger fired.
2. For the next genuinely novel candidate result, publish the first domain article at its actual evidence status.
3. Add machine-readable article metadata/schema if article volume grows enough to justify indexing/search automation.
4. When an article is promoted, preserve the prior status and evidence history in Git/GitHub rather than rewriting provenance.
