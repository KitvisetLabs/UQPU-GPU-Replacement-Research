# Research Gap RG-046 — transformer formula discovery under matched total-resource budgets

**Primary owner:** Lane F — benchmark/evidence integration  
**Cross-lane owners:** Lane A — equation-discovery runtime; Lane C — memory/resource accounting; Lane E — domain-specific constitutive models; Lane H — publication and strategic integration  
**Date:** 2026-10-25  
**Status:** MODEL_ONLY_BENCHMARK_CONTRACT_READY / DATA_BLOCKED_FOR_EXTERNAL_REPRODUCTION  
**Evidence promoted to project:** none

## Objective

Test whether transformer-based symbolic formula generation generalizes beyond training ranges and reduces total cost per independently accepted equation relative to symbolic search, LLM-guided search and physics-constrained hybrid methods under the same input data, split manifest and declared resource budget.

## Current implementation

The dependency-free helper at software/uqpu-prototype/uqpu/formula_discovery_benchmark.py validates a run record and a matched-method comparison. It requires frozen dataset and split hashes, a shared split-disjointness certificate hash, finite train/held-out/extrapolation errors, positive candidate complexity/count, unique seeds, a minimum seed count per method, a matched wall-clock budget within tolerance, and explicit dimensional/symmetry/conservation/causality outcomes. It preserves false discoveries, failed searches and counterexamples. Optional total cost per accepted formula requires a common cost-basis identifier and includes failed runs in the numerator. Model-training GPU-hours/energy are associated with a model hash and are not double-counted across seeds.

The fifteen local tests use synthetic fixtures only. The default three-seed minimum is a CI contract smoke threshold, not sufficient scientific replication. A confirmatory study should use at least 30 independent seeds.

## Blockers

- The arXiv preprint's model weights, source commit, data revisions and benchmark configurations have not been independently reproduced by this project.
- The audit requires a common split-disjointness certificate hash, but does not independently inspect or prove the row-level certificate; the actual split manifest and validation output must be archived.
- No transformer training, inference, external benchmark run, physical experiment, energy measurement or cost-per-accepted-formula result was performed in this cycle.
- Training, fine-tuning, hosting and amortization costs must be separated from inference latency; the H100 training dependency reported in the preprint is not a UQPU result.
- Formula prediction quality alone does not test the physical validity of an equation.

## Unlock criteria

1. Freeze the benchmark data and exact train/interpolation/extrapolation row IDs; prove the splits disjoint and archive the validation script, manifest hash and dataset license.
2. Pin model weights, source commit, environment, operator grammar, data-generation rules, seeds, timeouts and host resource ceilings.
3. Compare symbolic search, transformer generation, LLM-guided search and a physics-constrained hybrid at matched 10-second, 60-second and 30-minute budgets with identical training observations and held-out splits.
4. Run at least 30 seeds per method; preserve all failed searches, retries and false discoveries. Include noisy-target and unit-rescaling tests, and a scale-shift stress set.
5. Record exact-structure recovery, held-out/extrapolation errors, complexity, dimensional/symmetry/conservation/causality violations, counterexamples, wall/CPU time, peak memory, tokens, energy where measurable, training GPU-hours, model hashes and full cost per accepted equation.
6. Have an independent party reproduce the winning result on a frozen second dataset. A proposed physical law additionally needs a discriminating observable, domain-specific experiment and independent replication.

## Negative-result rule

If the transformer loses its extrapolation advantage at far-shifted scales, after model-training amortization, or under matched total-resource budgets, record that failure and retain the best conventional baseline. Do not reinterpret a failed fit as evidence that incumbent physics is wrong.

## Mission impact

This gap strengthens the generator-to-evaluator boundary under INV-034/035. It does not close any INV-029–033 mission gate: no physical compression, critical-material substitution, accepted bio-oil, net fusion electricity, lower project WACC or commercial cost advantage is demonstrated.
