# Literature watch — 2026-10-23: LLMs as symbolic-regression search controllers

**Accessed:** 2026-10-23  
**Primary owner:** Lane H — strategic development / future-industry research  
**Cross-lane interfaces:** Lane A (equation-search/runtime), Lane F (evidence and compute-cost accounting), INV-034/035  
**Evidence class:** THIRD_PARTY_PREPRINT / BENCHMARK_METHOD  
**Project evidence promotion:** none

## Primary source and date

Zikai Xie, Wenmei Li, Man Luo, Jun Jiang and Linjiang Chen, “Language models guide symbolic equation discovery by controlling search,” arXiv:2607.04156, submitted 2026-07-05. Official preprint: https://arxiv.org/abs/2607.04156.

The paper compares LLM roles as equation author, candidate decider and search controller. In its LLM-PySR controller configuration, the LLM proposes variables, operators, transformations and search depth; symbolic regression enumerates/fits candidate expressions; deterministic metrics govern retention. The authors report tests on 74 AI-Feynman equations and seven complex formula-recovery tasks, plus a piecewise-linear relationship on an independent battery dataset.

## Genuine methodological delta

The useful distinction is **who proposes the search strategy versus who decides that an equation survives**. It complements (but is not identical to) the October 2026 HarnessSR work already tracked in the repository and the peer-reviewed GOLLuM experimental-optimization study recorded separately in EXP-DESIGN-001. LLM-PySR targets symbolic-expression search; GOLLuM targets selection of physical experiments through uncertainty-aware Bayesian optimization. Their metrics and claims must not be pooled.

For UQPU, the actionable idea is to treat search configuration as a candidate object while leaving expression fitting, physics checks, held-out scoring and counterexample retention to deterministic tools. This maps most directly to EQN-002 (known-law recovery), EQN-003 (constraint-aware generation), EQN-004 (counterexample/falsification), EQN-005 (new-physics escalation) and EQN-006 (equation-to-technology traceability).

## Limitations and non-claims

- This is third-party preprint evidence, not an independent UQPU reproduction or proof that the method generalizes to all physical domains.
- Recovery on known formula sets can overfit a grammar, split, noise level, scoring function or search budget. The independent battery result is not evidence for Pangola materials, bio-oil, fusion, quantum hardware or UQPU economics.
- A low numerical residual does not establish dimensional consistency, symmetry, conservation, causality, a valid mechanism, or a new law. Candidate families and preprocessing choices can encode substantial human prior knowledge.
- Search-controller overhead, LLM tokens, host CPU/GPU time, memory, energy and failed/invalid candidates must be counted. A more sample-efficient equation search is not automatically cheaper end-to-end.
- No real-QPU run, device result, material qualification, accepted fuel, net delivered electricity, financing-rate effect or Data-Center-to-Phone capability was produced by this literature review.

## Proposed falsifiable follow-up: EQN-CTRL-001

Run an offline, frozen, reproducible comparison before applying any controller to unknown physics.

### Arms

1. **Numerical baseline:** fixed expression grammar and fixed search budget, with no LLM.
2. **LLM-author:** LLM proposes complete equations; deterministic evaluator decides acceptance.
3. **LLM-decider:** numerical search generates candidates; LLM ranks them, but deterministic gates still decide retention.
4. **LLM-controller:** LLM proposes variables/operators/transforms/search depth; a pinned symbolic-regression engine generates/fits expressions and deterministic metrics decide retention.

Keep EXP-DESIGN-001/GOLLuM separate: it is a candidate-selection method for experiments, not the same algorithm as symbolic equation recovery. A later combined arm must be preregistered rather than retroactively blended.

### Preregistered controls and metrics

- Freeze code versions, dependency lock, grammar, coefficient optimizer, seed list, dataset hashes, train/validation/held-out **law-family** split and compute/token budgets before running.
- Begin with known-law recovery fixtures already covered by EQN-002; hold out complete law families, not merely random rows from the same formula.
- Enforce unit/dimensional checks and applicable symmetry, conservation, causality and limiting-case checks before scoring. Reject invalid candidates rather than repairing them silently.
- Search for counterexamples and test noise, rescaling, parameter shifts and out-of-domain inputs.
- Report exact structural recovery, held-out residual, complexity/parsimony, constraint violations, counterexample survival, false-discovery count, invalid/duplicate candidates, wall time, tokens, host compute, memory and energy where measurable.
- Use multiple preregistered seeds and publish all failures/null results. Acceptance requires a held-out improvement over the strongest baseline under matched total resource budgets without a worse false-discovery or constraint-violation rate.
- A pass promotes only the search method to further MODEL_ONLY study. Any claim about new physics still requires a distinct observable, derivation, experiment/proof and independent validation; device/system and economic consequences remain separate gates.

## Cross-lane and permanent-invariant contribution

- **A:** a testable way to organize EQN-002/003 candidate generation without trusting model-authored equations.
- **B:** no provider or QPU interface change; all work is offline.
- **C:** require search memory/representation and data movement to be included in later resource accounting; no Hilbert-space-to-classical-memory equivalence follows.
- **D/G:** no device or manufacturing specification is justified until a candidate mechanism survives physical and system gates; D/G co-design remains active but unchanged by this paper.
- **E:** future use on biomass/material/fuel/fusion surrogates is only a hypothesis until each task has its own validated data and functional unit.
- **F:** matched resource budgets, strongest-baseline comparison, provenance and false-discovery accounting are mandatory.
- **H:** adds a dated, source-linked method review to the strategic research program while preserving the multilingual master-plan context.
- **INV-029:** possible future reduction in search time is only an indirect research input; no physical compression demonstrated.
- **INV-030–033:** no material, liquid-fuel, net-electricity or finance-rate result.
- **INV-034/035:** supports mathematics-first exploration while keeping established physics binding for present engineering claims and preventing AI-generated equations from being declared laws.

**Decision:** material method worth testing; project evidence promotion = none. The next gate is the frozen EQN-CTRL-001 offline benchmark, not hardware execution or commercial extrapolation.
