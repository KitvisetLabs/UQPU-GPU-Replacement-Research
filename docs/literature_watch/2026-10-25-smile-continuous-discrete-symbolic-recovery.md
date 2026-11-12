# Literature watch — 2026-10-25: continuous-to-symbolic recovery for equation discovery

**Accessed:** 2026-10-25  
**Primary owner:** Lane H — foundational research publication and strategic integration  
**Implementation owner:** Lane A — equation-discovery tools  
**Integration owner:** Lane F — benchmark and evidence accounting  
**Feeds:** A, C, D, E, F, G, H; FND-001–006; EQN-001–006; INV-029–035  
**Evidence class:** `LITERATURE_ONLY` (arXiv preprint)  
**Project evidence promotion:** none

## Source and genuine novelty

Mansooreh Montazerin, Antonio Ortega and Ajitesh Srivastava, “SMILE: Bridging Continuous Optimization and Discrete Symbolic Recovery,” arXiv:2609.04639, first submitted 2026-09-04: https://arxiv.org/abs/2609.04639.

SMILE combines three stages: structural analysis of the target expression, continuous gradient-based parameter optimization using interpretable activations, and discrete symbolic recovery by structured pruning, coefficient optimization and rounding. The authors report evaluations on SRBench ground-truth and black-box datasets, ablations, and improved symbolic solution rates at high noise with an accuracy-versus-complexity trade-off competitive with evaluated methods.

The useful methodological distinction is that a continuous surrogate can guide the search, but the final symbolic expression is still a candidate requiring independent scoring and testing. This is complementary to UQPU's existing equation-candidate contract and the BIC model-count baseline introduced in Batch 063; it does not replace them.

## Evidence class and limitations

This is a preprint claim, not independent UQPU reproduction and not a new physical law. The reported SRBench results are bounded by the paper's operator vocabulary, data-generation and split choices, target families, noise regimes and compute budget. Exact symbolic recovery on benchmark equations does not establish causal identification, uniqueness, global validity, or out-of-domain physical prediction. A compact expression may be observationally equivalent to several mechanisms.

Before considering a scientific application, the repository must inspect the full method and supplementary material, pin source/code/data versions, audit train/validation/test disjointness, reproduce the stated baselines under matched compute and energy budgets, and run held-out scale/noise/operator tests. Candidate selection must include failed searches and false discoveries.

## Exact relevance to UQPU and the permanent missions

- **Lane A / EQN-001–006 / FND-006:** a potential candidate generator or search controller; compare its symbolic output against known-law recovery and the current BIC candidate-count baseline.
- **Lane C / FND-001–002:** all input-state, memory, output-information and reconstruction costs remain part of the end-to-end contract; formula size is not a memory or quantum-capacity claim.
- **Lane D/G / INV-030:** a material constitutive equation can guide a Pangola-carbon substitution hypothesis only after units, symmetries, conservation, held-out loading conditions and independent materials measurements pass. No element is transmuted.
- **Lane E / INV-031–032:** a fitted expression cannot certify saleable bio-oil yield, upgrading cost, fusion fuel retention or net delivered electricity. Those remain mass/energy-balance and experiment-gated problems.
- **Lane F / INV-033:** charge search, training, retries, host compute, energy, and failed candidates to the same accepted-output accounting; do not infer lower WACC or commercial economics from symbolic fit.
- **INV-029:** no implication for physical data-center-to-phone compression unless an end-to-end useful-service, energy, form-factor and lifecycle-cost contract passes.

## Falsifiable UQPU follow-up

1. Freeze a small suite of known equations with explicit units, symmetries, conservation laws, and limiting cases; publish the exact split and source hashes.
2. Compare SMILE (if code and weights are available) with the current baseline under matched wall-clock, CPU/GPU-hours, memory and energy accounting. Include simpler symbolic-regression baselines and an intentionally misspecified candidate pool.
3. Repeat over preregistered independent seeds and noise levels. Record the candidate-count selection for every replicate, not only the best run; report selection frequency and tie/instability cases.
4. Evaluate held-out input scales, altered regimes and distractor variables. Search counterexamples and test dimensional/symmetry constraints before interpreting any candidate.
5. Keep every outcome at `MODEL_ONLY` until independent data, proof where applicable, and a discriminating experiment support a specific claim.

The current cycle implements a generic replicate-stability diagnostic around BIC candidate-count selection. It is a reusable evaluation aid, not a reproduction of SMILE or the Physical Law Ecology preprint and not evidence that any equation describes nature.
