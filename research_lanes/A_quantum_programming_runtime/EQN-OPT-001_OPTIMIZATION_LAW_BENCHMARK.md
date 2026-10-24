# EQN-OPT-001 — Optimization-law candidate-screen contract

**Primary owner:** Lane A — quantum programming / workloads / compiler-runtime  
**Cross-cutting consumers:** Lane F, Lane H, FND-006, EQN-001–006  
**Status:** IMPLEMENTED SCREENING UTILITY / MODEL_ONLY / NOT A LAW-DISCOVERY RESULT  
**Base main SHA:** c7b5958af58fad04a101ef5c6abf6a29293c867e  
**Date:** 2026-10-24

## Motivation

The 2026-10-23 literature watch already identified optimization-law discovery as a possible generator family. The current scan also found concept-driven and progressive symbolic-law discovery papers, with a source-status conflict for the CoSR preprint. This work therefore adds a small evaluator before adding another generator: it asks whether a candidate objective preserves decision-relevant ordering and optimum sets on held-out contexts.

## Implemented artifact

- software/uqpu-prototype/uqpu/optimization_law_benchmark.py
- software/uqpu-prototype/tests/test_optimization_law_benchmark.py

The evaluator accepts reference and candidate objective callables, frozen-by-caller train and held-out context lists, a shared finite decision grid, optimization direction, and numerical tolerance. It reports pairwise ordering agreement, concordant/discordant pairs, tie disagreements, optimum-set match rate, and split sizes.

## Synthetic checks

The tests cover:
1. Positive affine rescaling plus a context-only offset, which preserves objective ordering and optimum sets.
2. A candidate that agrees on the training context but diverges on held-out contexts.
3. A constant objective that ties every decision and must not be accepted as equivalent.
4. Invalid direction, empty splits, and non-finite outputs.
5. Maximization as well as minimization.

This is a candidate-screening layer, not a complete EQN-002 or RG-034 closure. The split hashes, generator budget, symbolic structure recovery, dimensional vectors, physical constraints, identifiability certificates, proof checks, counterexample search beyond the finite grid, and independent validation remain separate required gates.

## Acceptance and falsifiers

A candidate fails this screen if its held-out optimum set differs from the reference or if held-out pairwise ordering contains discordance/tie disagreement. Passing the screen is only necessary evidence for a decision-equivalent objective over the declared finite grid; it is not sufficient evidence of global equivalence, causal mechanism, a physical law, or a UQPU advantage.

## Reproducibility

From software/uqpu-prototype/, run:

~~~sh
PYTHONPATH=. python -m unittest discover -s tests -p 'test_optimization_law_benchmark.py'
~~~

The source-branch prototype was exercised against six synthetic cases during this run; exact-commit repository CI remains the next verification gate.

## Integration edges

- **A↔F:** same objective, decision grid, held-out contexts, and explicit acceptance metrics can be reused for compiler/runtime objective search and economic model candidate screening. No cross-domain unit or cost inference is automatic.
- **A↔H:** literature-derived generator families become reproducible candidate interfaces rather than claims.
- **FND-006 / EQN-001–006:** adds a measurable objective-order/optimum-set screen before dimensional, symmetry, conservation, causality, scaling, identifiability, and physical-validation gates.
- **B/C/D/G:** no provider call, memory-capacity inference, device requirement, or manufacturing conclusion is created by this finite-grid utility.
- **E:** no BIO-001, FUS-001, Pangola/material, or cooling evidence is created.

## Next gate

Add frozen split hashes and a declared search-budget manifest; compare a direct equation generator with an optimization-law generator and a deliberately non-optimization negative control. Include objective functions with known ground truth, confounded parameters, multiple equally predictive laws, noise, out-of-distribution contexts, and dimensionally inconsistent distractors. Keep every candidate at MODEL_ONLY until independent validation and the relevant downstream experiment pass.
