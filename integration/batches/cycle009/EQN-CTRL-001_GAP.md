# Research gap EQN-CTRL-001 — LLM-controlled symbolic-regression search

**Date opened:** 2026-10-23  
**Primary owner:** Lane H (literature and experimental-design proposal); Lane A owns future executable harness; Lane F owns acceptance/evidence accounting  
**Status:** MODEL_ONLY / NOT_YET_REPRODUCED  
**Source:** Xie et al., “Language models guide symbolic equation discovery by controlling search,” arXiv:2607.04156 (2026-07-05)  
**Related:** INV-034/035; FND-006; EQN-001–006; EXP-DESIGN-001 (separate task)

## Objective

Determine whether assigning an LLM to configure a symbolic-regression search improves held-out recovery of known equations at equal total resource cost, without increasing false discoveries or constraint violations. This is a method benchmark only, not a search for a new physical law.

## Incumbent assumptions to test

1. A fixed symbolic-regression grammar/search budget is an adequate baseline.
2. LLM-generated search configurations may improve exploration but can also overfit the benchmark, grammar, preprocessing and held-out split.
3. Equation fit alone is insufficient: dimensional validity, symmetry/conservation/causality where applicable, limiting cases and counterexample survival must be independently checked.
4. The strongest baseline must be selected from preregistered deterministic baselines, not by looking at test outcomes.

## Minimum preregistration

- Freeze candidate grammar, units metadata, coefficient fitting method, code/dependency versions, dataset hashes, seed list, split by complete equation family, stopping rule and total resource budget.
- Compare fixed numerical search, LLM equation author, LLM candidate decider and LLM search controller.
- Keep GOLLuM/EXP-DESIGN-001 separate because it concerns experiment selection, not equation recovery.
- Record exact structural recovery, held-out error, expression complexity, constraint violations, counterexample survival, false discoveries, invalid/duplicate candidates, wall time, tokens, host CPU/GPU, memory and energy where measurable.
- Use known-law recovery before any unknown-physics task. Include noise, rescaling, parameter shifts and out-of-domain inputs.
- Publish negative/null results and the full candidate ledger.

## Acceptance and falsification

**Accept for further MODEL_ONLY research only if** the controller improves the preregistered held-out objective over the strongest baseline under matched total resource budgets and does not worsen preregistered false-discovery or constraint-violation limits.

**Falsify the efficiency hypothesis if** gains disappear on held-out equation families, are explained by extra compute/token budget, fail dimension/symmetry/conservation/causality checks, or do not survive counterexample search. A null result remains useful and must be retained.

Even a pass does not validate a new physical law. Any challenge to established physics still needs an explicit changed assumption, alternative equation, dimensional and symmetry checks, conservation/causality checks, scaling limits, discriminating observable, held-out prediction, proof/experiment and independent replication.

## Current blockers

- No project-owned LLM-PySR reproduction or pinned runtime is recorded.
- Local network checkout was unavailable in this run; branch CI is the required code-validation path.
- No measured UQPU, materials, bio-oil, fusion, electricity, financing or real-QPU outcome is associated with the source paper.
- This dated gap artifact is additive. The large canonical `RESEARCH_GAPS.md` was not replaced or truncated; its synchronization with this new gap remains debt until the owning branch is reviewed/merged and the canonical backlog is safely appended.
