# Batch 046 — Verified New-Discovery Article Registry and Admission Gate

**Status:** repository-governance / executable evidence gate  
**Permanent directive:** INV-037  
**Canonical publication root:** `articles/`  
**Date:** 2026-09-14

## Research Attribution

- Research Owner / Principal Investigator / Research Direction: **Kanutsanan Pongpanna**
- Facebook: https://www.facebook.com/LoveMoneyTH
- YouTube: https://www.youtube.com/@LoveMoneyTHOfficial
- AI Research Agent: **OpenAI GPT-5.6 Sol**
- AI-assisted contribution: verified-discovery publication design, domain-specific admission rules, executable gate/tests, directory architecture, frozen certificate, documentation and PR preparation.

Attribution in future articles must list only contributors/models/agents that actually participated in that specific discovery.

## Owner direction — corrected boundary

The `articles/` folder is **not** for new ideas, hypotheses, candidate discoveries or intermediate research results. It is reserved only for results that have already been established as genuinely new discoveries in physics, science or mathematics.

Ideas, hypotheses, simulations, candidate equations, project-only reproductions, preliminary observations and literature findings remain in ordinary research locations such as `docs/`, the owning research lane, benchmark/result folders or issues until the full discovery gate has passed.

## Implementation

Batch 046 creates a root-level verified-discovery registry with three permanent domains:

- `articles/physics/`
- `articles/science/`
- `articles/mathematics/`

It also creates:

- `00D_NEW_DISCOVERY_ARTICLES.md` — root-level permanent directive;
- `articles/README.md` — canonical verified-only admission policy;
- `articles/ARTICLE_TEMPLATE.md` — template usable only after admission passes;
- `software/uqpu-prototype/uqpu/discovery_article_gate.py` — executable verified-discovery admission rules;
- `software/uqpu-prototype/tests/test_discovery_article_gate.py` — positive and negative admission tests;
- permanent folder/policy checks in `test_project_invariants.py`;
- `benchmarks/results/batch046-new-discovery-article-gate.json` — frozen governance certificate.

## Hard admission rule

The only allowed project-article status is:

```text
VERIFIED_DISCOVERY
```

The following remain outside `articles/`:

- `HYPOTHESIS_OR_PROPOSAL`
- `PROJECT_REPRODUCED_RESULT`
- `INDEPENDENTLY_REPRODUCED_CANDIDATE`
- preliminary/internal results
- external literature summaries

The result must already be verified before the article is created.

## Physics / empirical science gate

Admission requires documented prior-art/novelty review, reproducible primary evidence, falsification/alternative-explanation analysis, uncertainty/error analysis and independent validation appropriate to the domain. Theory, simulation, AI generation or project-only reproduction alone cannot qualify.

## Mathematics gate

Admission requires a precise theorem/result and assumptions, complete proof or equivalently strong formal artifact where applicable, counterexample/boundary analysis, prior-art/novelty review and independent proof checking/review. Numerical agreement or symbolic fitting alone cannot qualify.

## External discoveries

Discoveries made by other researchers are essential research inputs but ordinary literature summaries do not enter this project's verified-new-discovery `articles/` registry. They remain literature/research notes with proper original attribution. A genuinely new UQPU extension may enter only after passing the same full gate.

## Publishable result

The publishable result of Batch 046 is **not a new scientific or mathematical discovery**. It is a reproducible governance mechanism that reserves a prominent repository area for future discoveries only after they are genuinely verified as new.

## Evidence classification

```text
classification:
  VERIFIED_NEW_DISCOVERY_ARTICLE_REGISTRY_AND_ADMISSION_GATE

evidence_level:
  RESEARCH_GOVERNANCE_EXECUTABLE
```

## Non-claims

Batch 046 does not retroactively promote any UQPU theory, model, simulation, symbolic-regression output, internal reproduction or AI-generated equation into a discovery or new law. It does not establish real-QPU advantage, quantum advantage, GPU/NPU/RAM/DRAM/HBM replacement, `>=100x`, `>=100,000,000x`, or Data-Center-to-One-Phone achievement.

## Next gates

1. Wire the verified-discovery registry into future research-batch closing procedure: every batch must explicitly answer whether the strict article-admission gate passed.
2. Do not create the first substantive discovery article until a result actually satisfies the full verified-discovery contract.
3. Add machine-readable article metadata/schema only after the first verified article or when indexing becomes necessary.
4. Preserve correction/retraction history if later evidence overturns or narrows any published discovery.
