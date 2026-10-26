# Research Gap RG-049 — structural-verifier calibration for equation discovery

**Date opened:** 2026-10-25  
**Primary owner:** Lane F — evidence and benchmark integration  
**Implementation owner:** Lane A — equation discovery  
**Publication owner:** Lane H  
**Evidence state:** LITERATURE_ONLY + SOFTWARE_DIAGNOSTIC  
**UQPU project evidence promoted:** none

## Objective

Test whether structural guidance adds useful information beyond residual error and standard model-selection criteria, without leaking known target equations or weakening physical constraints.

## Current state

- The newly indexed preprint L2G-SR (arXiv:2610.20685, submitted 2026-10-14) reports improved structure recovery and held-out fit on its evaluated symbolic-regression benchmarks when a learned structural verifier complements numerical error.
- A dependency-free UQPU helper, `uqpu.equation_structure`, canonicalizes a restricted expression grammar and computes a deterministic root-preserving edit metric. It normalizes commutative/associative addition and multiplication and optionally abstracts numeric constants.
- Focused unit tests cover equivalence normalization, preserved constants, different operator structures, restricted syntax and normalized-distance bounds. The smoke artifact is a MODEL_ONLY software diagnostic.
- This helper is deliberately not the paper's learned verifier or exact tree-edit-distance algorithm. It is a transparent baseline that can be evaluated on known-truth fixtures.

## Blockers

1. No learned structural verifier or independently pinned training pipeline has been implemented.
2. No frozen known-law benchmark spans K=1/2/3, correlated/noisy observations, unit transformations, equivalent expressions and scale-shift holdouts.
3. No record-level split certificate prevents leakage across algebraically equivalent expressions from the same law family.
4. No comparison currently measures accepted-candidate yield, false discoveries, constraint violations and total cost under matched search/host-resource budgets.
5. No project-specific constitutive, Pangola, bio-oil, fusion or quantum-workload data have passed this gate.

## Unlock criteria

1. Freeze data, target-law family IDs, formula-equivalence rules, random seeds, candidate budgets and train/validation/held-out partitions before search.
2. Compare residual-only, BIC, blocked holdout, transparent structure metric (post-hoc only) and any independently implemented learned verifier on identical candidate pools and budgets.
3. Measure exact structural recovery, held-out error, scale-shift performance, false-discovery rate, constraint violations, candidate ranking stability and failures/retries.
4. Verify row-level and law-family disjointness; no true target expression or target-distance signal may be exposed to the runtime candidate ranker.
5. Record training plus inference/search cost per accepted formula, counting model-training resources once per pinned model hash and including failed runs.
6. Independently reproduce the benchmark before considering process-specific experimental design.

## Negative-result rule

If structural ranking is unstable under declared algebraic equivalences or unit changes, or improves in-sample fit while worsening held-out generalization or false-discovery rate, retain the residual-only baseline and mark the structural score rejected for that regime. Do not interpret model-selection failure as evidence against established physics.

## Cross-lane and invariant impact

- **A:** equation search instrumentation only; no QPU workload or compiler advantage.
- **B:** no provider adapter or execution change.
- **C:** no memory/storage equivalence or data-movement reduction.
- **D/G:** no device, process, fabrication, yield or manufacturing result.
- **E:** BIO-001 and FUS-001 remain blocked on accepted functional-unit and lifecycle evidence.
- **F:** owns matched-budget calibration and false-discovery accounting.
- **H:** publishes the method boundary and strategic relevance.
- **INV-029–033:** no mission, material, accepted-fuel, net-electricity or financing gate closes.
- **INV-034/035:** mathematics-first hypothesis generation is strengthened while current physics and empirical promotion gates remain binding.

Next action: run the deterministic known-law structural metric through exact-head CI, then build the blinded, split-disjoint benchmark only after review of overlapping equation-discovery PRs.
