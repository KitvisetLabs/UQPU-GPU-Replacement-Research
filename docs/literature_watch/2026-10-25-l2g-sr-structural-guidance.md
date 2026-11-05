# Literature watch — 2026-10-25: structural feedback for symbolic equation search

**Accessed:** 2026-10-25  
**Primary owner:** Lane H — research publication  
**Implementation owner:** Lane A — equation-search instrumentation  
**Integration owner:** Lane F — benchmarks, evidence and economics  
**Feeds:** FND-006; EQN-001–006; INV-034/035; lanes A, D, E, F, G and H  
**Evidence class:** OFFICIAL ARXIV PREPRINT + DETERMINISTIC SOFTWARE DIAGNOSTIC  
**Project evidence promoted:** none

## Source and date

Letian Huang, Xiangyu Wang, Haowei Lin and Di He, “L2G-SR: Learning to Guide LLM-based Symbolic Regression,” arXiv:2610.20685, submitted 2026-10-14. Official source: https://arxiv.org/abs/2610.20685.

This source is newly indexed in this project review; a repository-wide search for the arXiv identifier and “L2G-SR” returned no existing record on the current main head. The nearby OptScientist optimization-law paper (arXiv:2610.28562, 2026-10-20) is already recorded in the 2026-10-23 watch and is not duplicated here.

## Genuine methodological delta

L2G-SR adds a learned structural verifier to LLM-guided symbolic-regression search. Its score estimates a candidate formula's structural distance from an unseen target expression and complements numerical validation error when selecting search parents. The paper defines a modified tree-edit-distance target that abstracts constants and accommodates commutative/associative expression variants. This is a meaningful design distinction from selecting candidates by residual error alone: two equations can fit a finite sample similarly while representing different structures.

The paper reports, for a matched Physics-domain ablation over three seeds and 44 tasks per seed with 400 candidate slots, lower mean test NMSE for TED feedback than the validation-MSE-only control (2.702×10^-4 versus 2.264×10^-3), higher Acc_0.01 (89.39% versus 74.24%), and lower mean true TED (0.239 versus 0.361). These are the authors' reported benchmark values, not an independent UQPU reproduction. The target formula is hidden at search time; true structural distance is available only for supervised construction/evaluation, not as a runtime oracle for unknown physical laws.

## Limitations and evidence boundary

- This is an arXiv preprint, not a peer-reviewed version of record verified by this cycle.
- The structural verifier's candidate-level correlations with true distance are reported as moderate and domain-dependent. A ranking signal may help without being a reliable absolute distance estimate.
- Results cover the paper's benchmark, evaluated LLM backbones and resource protocol; they do not establish universal generalization, physical validity, or causal mechanisms.
- A structural score can reward the wrong target if formula normalization, units, domain assumptions or the candidate grammar are mis-specified. Numeric fit, structural match, dimensional/symmetry/conservation/causality checks, counterexamples and held-out scale shifts must remain separate metrics.
- The UQPU helper added in this branch is a transparent, deterministic, root-preserving expression-tree edit metric. It is **not** L2G-SR, does not train a verifier, does not implement the paper's exact metric, and does not certify a physical law.

## Exact project relevance

- **Lane A / EQN-001–006:** adds a candidate diagnostic to the equation-discovery pipeline, but candidate generation and selection remain separate from proof and physical promotion.
- **Lane F / RG-049:** motivates a matched-budget, known-truth calibration for structure scores, false discoveries and candidate-count stability.
- **Lane E / INV-030–032:** symbolic constitutive/material, biomass-conversion and fusion submodels could be searched with this kind of diagnostic only after process-specific data and physical constraints are declared. The paper contains no Pangola, bio-oil, fusion or UQPU measurements.
- **Lane D/G:** equation structure could eventually help compare constitutive/device models, but it supplies no material qualification, device/process window, yield or manufacturing-cost evidence.
- **INV-033 / FIN-001:** token count is not total research cost. A fair comparison must include training amortization, inference/search, host compute, retries, energy where measured, failed runs and the number of independently accepted formulas.
- **INV-029:** no service-capability, physical-compression, lifecycle-cost or phone-class result follows from this method paper.

## Proposed falsifiable follow-up — EQN-STRUCTURE-001

Run a deterministic known-law benchmark before using project data. Freeze equation families and formula-equivalence rules; generate train/validation/held-out domains with noise, correlated samples, distractor variables, unit rescaling, algebraically equivalent forms and planted structurally wrong near-fit candidates. Compare, under matched candidate-evaluation and host-resource budgets:

1. residual-only selection;
2. BIC / blocked held-out-error baselines;
3. the transparent canonical-structure metric as a **post-hoc known-truth diagnostic only**;
4. a learned structural verifier only if its implementation, training protocol and data provenance can be independently pinned and audited;
5. a physics-constrained hybrid that checks units, symmetries, conservation, causality, positivity/stability and limiting cases.

Split by law family and formula-equivalence class, not merely by randomly sampled rows. The target expression and true structural distance must never leak into runtime ranking. Report exact structure recovery, held-out prediction, extrapolation, false-discovery rate, constraint violations, rank stability under unit/commutative/associative rewrites, counterexample survival, wall-clock, tokens, host memory/compute, energy where measurable, and total cost per accepted formula. Include all failed searches and retries.

**Null hypothesis:** structural guidance does not improve accepted-candidate yield under the same total budget.  
**Falsifier:** reject or disable the structural score if its ranking advantage vanishes on blinded law-family or scale-shift holdouts, or if it increases false discoveries/constraint violations.  
**Promotion gate:** independent implementation and reproduction, held-out improvement, stable ranking under declared equivalences, and no increase in false discoveries. Physical-law claims still require a discriminating experiment and independent replication.

No QPU job, wet-lab test, fabrication run, funding action or physical experiment is authorized by this watch.
