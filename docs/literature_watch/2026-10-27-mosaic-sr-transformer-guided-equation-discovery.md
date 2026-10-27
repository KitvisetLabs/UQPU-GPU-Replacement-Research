# Literature watch — MOSAIC-SR transformer-guided symbolic regression

**Reviewed:** 2026-10-27  
**Primary source:** Peiyi Zheng, Yanming Kang, Hans De Sterck and Giang Tran, “MOSAIC-SR: Transformer-Guided Symbolic Regression for Scientific Equation Recovery.”  
**Official source:** https://arxiv.org/abs/2609.20997  
**Source date:** arXiv submission 2026-09-17  
**Evidence class:** OFFICIAL PREPRINT / EXTERNAL BENCHMARK REPORT; not independently reproduced by UQPU  
**Primary owner:** Lane H (literature/publication); technical follow-up owner: Lane A; evaluation owner: Lane F  
**Cross-cutting:** FND-006, EQN-001–006, INV-034/035; no physical-law promotion

## Material delta

MOSAIC-SR uses a pretrained Transformer to propose several initial equation sketches. These seed multiple symbolic-search regions; each search jointly optimizes constants with scale-aware optimization and applies local symbolic repair. The authors report results on SRSD-Feynman, including variants with irrelevant dummy inputs, and six additional benchmarks. They report the highest symbolic solution rate on the evaluated datasets while ranking among the top two methods in predictive accuracy.

The useful methodological claim is narrow: learned priors may improve where symbolic search begins, while deterministic numerical and symbolic checks remain responsible for candidate acceptance. This complements—not replaces—the project's existing progressive symbolic-composition, LLM search-control, and sensitivity/identifiability tracks.

## Limitations and evidence boundary

- This is an arXiv preprint; UQPU has not reproduced its code, data, benchmark splits, seed distribution, or compute budget.
- Benchmark equation recovery is not proof of physical causality or a new law of nature.
- A symbolic solution-rate gain may depend on grammar, preprocessing, variable/unit representation, training data, search budget, repair rules, or benchmark familiarity.
- Predictive accuracy, exact structural recovery, dimensional consistency, conservation/symmetry/causality, extrapolation to held-out scales, formal proof and empirical physical validity are separate outcomes.
- No inference about Pangola carbon, semiconductor substitution, quantum advantage, fusion electricity, bio-oil cost, WACC or phone-scale physical compression follows from the preprint.

## Exact UQPU relevance

- **Lane A:** include transformer multi-start sketches plus symbolic repair as a method arm in the EQN-008 matched comparison; retain the existing workload/compiler/runtime priority.
- **Lane B:** no provider adapter or QPU job is involved. If a later quantum workload is proposed, retain provider/target-specific evidence and pricing.
- **Lane C:** compact expressions or fewer symbolic terms are not readable RAM/VRAM/HBM/storage and do not remove state-preparation or data-movement cost.
- **Lane D:** candidate constitutive/material equations still need domain, dimensional, symmetry and limiting-case checks before any device/material inference.
- **Lane E:** no transfer to Pangola-derived carbon, accepted bio-oil or fusion is justified without task-specific data and experiments.
- **Lane F:** compare total search/training/inference cost, wall time, seeds, retries, failure rate, held-out accuracy, structural recovery, calibration/uncertainty and constraint violations under a matched budget.
- **Lane G:** no process window, yield, metrology or cost-per-good-device evidence is added; D/G co-design remains continuous.
- **Lane H:** preserve the primary-source trail and the Kanusanan Pongpanna Model as strategic context, not scientific proof.

## Falsifiable follow-up

Freeze source/data/code hashes, preprocessing, variable and unit map, expression grammar, train/validation/test membership grouped by equation family, and a fixed total compute/inference budget before tuning. Compare (1) one-shot symbolic regression, (2) MOSAIC-SR-style transformer multi-start plus repair, (3) progressive symbolic composition, and (4) LLM-guided search control. Use at least 30 preregistered seeds where compute permits; report every failed run. Hold out equation families and scale transformations. Search counterexamples, equivalent-form instability, unit violations and known-law limit failures.

The method-advantage hypothesis is falsified if the apparent gain disappears on law-family-disjoint or held-out-scale tests, is explained by leakage/unequal compute, or increases accepted-equation cost without improving the predeclared acceptance metric. A candidate equation may only be promoted toward physical testing after the full INV-035 sequence; no symbolic fit alone is a physical law.

## Next gate

Execute the matched, preregistered benchmark in RG-EQN-008 after source pinning and budget freeze. Until then, this watch is literature-only and all UQPU/physics/energy/material/finance claims remain unchanged.
