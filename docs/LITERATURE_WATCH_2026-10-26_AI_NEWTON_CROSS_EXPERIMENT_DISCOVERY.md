# Literature Watch — AI-Newton and Cross-Experiment Equation Discovery

**Date observed:** 2026-10-26  
**Primary source:** You-Le Fang, Dong-Shan Jian, Xiang Li, and Yan-Qing Ma, “AI-Newton: A concept-driven physical law discovery system without prior physical knowledge,” *Physical Review Research*, APS accepted-paper record dated 2026-10-09.  
**Source:** https://journals.aps.org/prresearch/accepted/2a079YedZ1d1fd9af2aa0817e6bd8b9d84964ade7  
**DOI:** https://doi.org/10.1103/dvvc-4rsr  
**Related primary source:** Mingkun Xia and Weiwei Zhang, “Data-driven progressive discovery of physical laws,” *Physical Review Research*, APS accepted-paper record dated 2026-10-06.  
**Source:** https://journals.aps.org/prresearch/accepted/10.1103/f2kp-pp4q  
**DOI:** https://doi.org/10.1103/f2kp-pp4q  
**Methodological caution source:** Ying Xie, “What the Machine Invented: Mining New Mathematical Instruments from OpenAI's October 2026 Release of AI-Generated Mathematics,” arXiv:2610.17090, posted 2026-10-12. https://arxiv.org/abs/2610.17090  
**Evidence class:** APS-accepted third-party methods papers + arXiv methodological survey; LITERATURE_ONLY for UQPU. No independent UQPU reproduction or physical-law promotion.

## Fresh literature delta

The AI-Newton paper studies a concept-driven workflow that proposes interpretable physical concepts from raw data spanning multiple experiments, then attempts to generalize laws across broader domains. Its reported demonstrations rediscover familiar mechanics relations from noisy multi-experiment data. The project-relevant novelty is the explicit emphasis on *cross-experiment concept formation and generalization*, rather than fitting each experiment in isolation.

The CoSR paper frames discovery as a progressive chain of interpretable symbolic knowledge units, combining them in a structured order from simpler relationships toward more complex laws. It reports applications to Rayleigh–Bénard convection, pipe flow, laser–metal interaction and aircraft aerodynamic-coefficient scaling. CoSR is already the subject of open PR #56 (EQN-COSR-001); this watch does not duplicate that implementation or claim that PR is merged.

These methods suggest complementary search operators:
- **concept-driven cross-experiment generalization** (AI-Newton);
- **progressive composition of interpretable law fragments** (CoSR);
- **LLM-guided search-space control with numerical fitting and deterministic retention** (LLM-PySR, arXiv:2607.04156);
- **one-shot symbolic regression** as a matched baseline.

The arXiv survey of AI-generated mathematics is a useful caution rather than a proof source: it explicitly describes novelty assessments as provisional and reports that the surveyed Lean developments were not compiled/kernel-checked. An AI-produced argument must not be counted as a formal proof until the relevant proof artifact is independently checked.

## Limitations and nonclaims

1. Rediscovering known laws on selected datasets is evidence about a discovery method, not evidence for a new law of nature.
2. Multi-experiment input does not by itself establish out-of-domain validity. The split must hold out entire experiment conditions or law families; random-row splits can leak the same mechanism into training and test sets.
3. “Without prior physical knowledge” describes the paper's method design, not a guarantee that data selection, preprocessing, candidate grammar, evaluation or human choices contain no assumptions.
4. A compact equation may be non-identifiable, dimensionally invalid, non-causal, unstable under noise, or merely interpolate a limited domain.
5. The accepted-paper records are not an independent replication by this project. No UQPU implementation, real-QPU job, device measurement, material experiment, fuel test, fusion plant result, cost advantage or new physical law follows from this watch.

## Exact UQPU relevance

- **Lane A / FND-006 / EQN-001–006:** use the papers to improve candidate-generation strategy, not to relax acceptance gates. A candidate must still pass typed variables/units, dimensional and symmetry checks, conservation/causality checks where applicable, known-limit tests, held-out prediction, counterexample search and independent validation.
- **Lane B:** any later quantum-workload/resource model must be checked on provider- and target-matched evidence. No simulated probability may be combined with another provider's price.
- **Lane C:** any discovered state/memory law must include readable output, state preparation, data movement, I/O, lifetime and host-memory costs; Hilbert-space dimension is not readable classical storage.
- **Lanes D/G:** a candidate can affect device/factory design only after it yields a measurable device-level prediction and a feasible metrology/process test. No fabrication or device claim is made here.
- **Lane E / INV-030–032:** biomass mass/energy balances, accepted bio-oil yield/upgrading and fusion net-electric cost models are possible future application domains only after suitable measured datasets exist. This watch contributes no Pangola substitution, accepted-fuel or net-fusion-electricity evidence.
- **Lane F / INV-033:** count search evaluations, failed candidates, wall time, compute/API usage, energy where measurable, uncertainty and total cost per accepted formula. No WACC or project-finance effect is inferred.
- **Lane H:** preserve staged investment: fund only the next cheapest decisive validation step; do not capitalize a symbolic fit as a technology result.
- **INV-029:** this method may eventually help discover more efficient algorithms or resource models, but it does not demonstrate data-center-to-phone physical compression.

## Proposed falsifiable follow-up — EQN-AINEWTON-001

Run a preregistered comparison of four arms:
1. one-shot symbolic regression;
2. CoSR-style progressive composition;
3. AI-Newton-style concept-driven cross-experiment generalization;
4. LLM-PySR-style search control with deterministic numerical retention.

**Protocol**
- Freeze the source-data hashes, variable definitions, units, candidate grammar, evaluation rules, seeds, budgets and split manifest before revealing held-out outcomes.
- Use a small synthetic known-law suite for implementation checks, then a public multi-experiment dataset. Hold out entire experiment conditions and, in a separate harder test, an entire law family; never use random-row splitting as the only generalization test.
- Match total search budget across arms: candidate evaluations, CPU/GPU time, memory limit, wall time, model/API calls and monetary cost. Report energy only where directly measured. Do not compare unequal search budgets as if the method alone caused a gain.
- Score held-out normalized error, calibration/uncertainty, expression complexity, dimensional validity, applicable symmetries/conservation laws, counterexample survival, stability across independent seeds, false-discovery rate, failed-candidate count and cost per accepted formula.
- Freeze negative controls: dimensionally inconsistent expressions, shuffled targets, split leakage, duplicated observations, scale shifts, noise perturbations and deliberately over-flexible candidate grammars.
- Have an independent implementation or reviewer reproduce the scoring and a subset of candidate predictions. For physical-law claims, require a discriminating observable and independent experiment; a benchmark win alone remains a method result.

**Falsifier:** if concept-driven or progressive methods do not improve held-out experiment/law-family performance or stability over the matched one-shot baseline within the same budget—or if apparent gains disappear under leakage, scaling, noise or counterexample controls—do not adopt the added complexity as an improvement. Retain the null result and false discoveries.

## Integration decision

Adopt cross-experiment generalization as a candidate *benchmark dimension* for EQN-001–006, alongside the existing CoSR and search-control work. Do not replace the existing PR #56 contract, merge pending work implicitly, or treat any AI-generated expression as a physical law. The next decisive gate is a frozen, budget-matched, law-family-disjoint experiment with explicit null and counterexample controls.
