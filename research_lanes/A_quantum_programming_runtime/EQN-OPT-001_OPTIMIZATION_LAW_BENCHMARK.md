# EQN-OPT-001 — Optimization-law candidate-screen contract

**Primary owner:** Lane A — quantum programming / workloads / compiler-runtime  
**Cross-cutting consumers:** Lane F, Lane H, FND-006, EQN-001–006  
**Status:** IMPLEMENTED SCREENING UTILITY / MODEL_ONLY / NOT A LAW-DISCOVERY RESULT  
**Base main SHA:** c7b5958af58fad04a101ef5c6abf6a29293c867e  
**Date:** 2026-10-24

## Motivation

The 2026-10-23 literature watch identified optimization-law discovery as a possible generator family. The current scan also covers concept-driven and progressive symbolic-law discovery, physics-informed policy optimization, and LLM-guided symbolic-regression search. Before adding another generator, this evaluator asks whether a candidate objective preserves decision-relevant ordering and optimum sets on held-out contexts.

## Implemented artifact

- `software/uqpu-prototype/uqpu/optimization_law_benchmark.py`
- `software/uqpu-prototype/tests/test_optimization_law_benchmark.py`

The evaluator accepts reference and candidate objective callables, train and held-out context lists, a shared finite decision grid, optimization direction, and numerical tolerance. It reports pairwise ordering agreement, concordant/discordant pairs, tie disagreements, optimum-set match rate, and split sizes.

It now also:
- rejects duplicate contexts within either split and duplicate decision values, preventing repeated grid entries from silently overweighting scores;
- rejects overlap between numeric train and held-out contexts;
- returns SHA-256 fingerprints for the train contexts, held-out contexts, decision grid, and combined numeric-grid/scoring-settings contract.

**Fingerprint boundary:** these hashes cover the numeric lists and scoring settings only. They do not prove when the split was selected, bind source-dataset provenance, hash the reference/candidate callable implementation, or certify search-budget parity. Those remain explicit upstream requirements.

## Synthetic checks

The tests cover:
1. Positive affine rescaling plus a context-only offset, which preserves objective ordering and optimum sets.
2. A candidate that agrees on the training context but diverges on held-out contexts.
3. A constant objective that ties every decision and must not be accepted as equivalent.
4. Invalid direction, empty splits, and non-finite outputs.
5. Maximization as well as minimization.
6. Stable grid fingerprints and sensitivity to scoring-contract changes.
7. Rejection of duplicate grid entries and train/held-out overlap.

These deterministic cases remain synthetic MODEL_ONLY tests, not a discovery result.

## Acceptance and falsifiers

A candidate fails this screen if its held-out optimum set differs from the reference or if held-out pairwise ordering contains discordance/tie disagreement. Passing is only necessary evidence for decision-equivalence over the declared finite grid; it is not sufficient evidence of global equivalence, causal mechanism, a physical law, or a UQPU advantage.

## Reproducibility

From `software/uqpu-prototype/`, run:

~~~sh
PYTHONPATH=. python -m unittest discover -s tests -p 'test_optimization_law_benchmark.py'
~~~

The exact updated branch head must pass repository CI before acceptance or main synchronization.

## Integration edges

- **A↔F:** identical objective, context/decision grids, held-out contexts, fingerprints, and acceptance metrics can screen compiler/control/economic objective candidates. No cross-domain unit or cost inference is automatic.
- **A↔H:** literature-derived generator families become reproducible candidate interfaces rather than claims.
- **FND-006 / EQN-001–006:** adds a measurable objective-order/optimum-set screen before dimensional, symmetry, conservation, causality, scaling, identifiability, proof, and physical-validation gates.
- **B/C/D/G:** no provider call, memory-capacity inference, device requirement, or manufacturing conclusion is created by this finite-grid utility.
- **E:** no BIO-001, FUS-001, Pangola/material, or cooling evidence is created.

## Next gate

Add a preregistered search-budget manifest and source-data/split-generation provenance; compare direct equation generation, LLM-controlled symbolic-regression search, physics-informed adaptive generation, and a deliberately non-optimization negative control under identical wall-clock, host-resource, data and candidate-evaluation budgets. Include known ground-truth laws, confounded parameters, multiple equally predictive laws, noise, out-of-distribution contexts, and dimensionally inconsistent distractors. Keep every candidate at MODEL_ONLY until independent validation and the relevant downstream experiment pass.
