# Literature watch — symbolic-regression-guided inverse design of high-hardness multi-principal-element alloys

**Date checked:** 2026-10-29  
**Primary owner:** Lane E — advanced materials and functional substitution  
**Interfaces:** D device/material function; G manufacturability and process/yield; F evidence and economics; H publication  
**Evidence class:** PUBLISHER-HOSTED EARLY-ACCESS RESEARCH ARTICLE / THIRD-PARTY MODEL RESULTS / NOT REPRODUCED BY UQPU  
**Stable ID:** LIT-2026-10-23-MPEA-SYMBOLIC-INVERSE-DESIGN

## Source and dated status

Peiyi Li, “Machine learning-driven inverse design of high-hardness multi-principal element alloys through symbolic regression,” *Scientific Reports*, published 2026-10-23. DOI and publisher record: https://doi.org/10.1038/s41598-026-74491-7 and https://www.nature.com/articles/s41598-026-74491-7. The publisher labels this an early-access accepted article that may receive further edits.

## Reported result and genuine novelty

The paper combines a descriptor library, genetic-programming symbolic regression, CatBoost prediction and three metaheuristic optimizers for inverse composition search. Its abstract reports reducing 39 input features to three symbolic descriptors and a test-set (R^2=0.885) with RMSE 77.2 Vickers-hardness units. The proposed descriptors are used to support a constrained four- or five-principal-element composition search.

The useful methodological signal is the explicit coupling of interpretable feature construction with an inverse-design loop, rather than relying on a black-box predictor alone. The reported score is a source-reported test result, not a UQPU reproduction or proof that a candidate alloy is manufacturable or commercially superior.

## Limitations and evidence boundary

- A test-set score does not establish a new physical law or causal mechanism.
- Inverse optimizers can exploit surrogate errors; a high predicted hardness is not itself an independently measured material property.
- The checked abstract does not establish UQPU replication, prospective synthesis/measurement, production yield, lifecycle cost, critical-mineral reduction or commercial qualification.
- Multi-principal-element alloys are a different material family from Pangola-derived carbon. Their descriptors must not be transferred to biomass carbon or diamond claims without separate data and validation.

## Exact UQPU relevance

**INV-030 / Lane E:** this is a process-method analogue for searching functional material alternatives. It does not demonstrate that Pangola carbon can replace an alloying element, semiconductor material, magnet, diamond or any other critical material. Functional equivalence must be defined per application and may include hardness, thermal/electrical properties, radiation damage, stability, purity, manufacturability, recycling and lifecycle cost.

**Lanes D/G:** a promising composition must pass phase/structure feasibility, synthesis, process-window, yield, packaging and reliability gates before it becomes a technology option.

**Lane F:** compare cost per accepted function, not predicted hardness or raw feedstock price. Include precursor costs, energy, processing, quality-control, rejects, lifetime and recycling.

**Lanes A–C:** no computing-performance or memory-substitution result follows from the material model. H preserves the strategic master-plan context without upgrading a third-party result to project evidence.

## Proposed falsifiable follow-up

1. Reproduce the source's data provenance, descriptor generation, split strategy and baseline metrics where data are available.
2. Use grouped composition/family holdouts to test leakage and extrapolation; compare against simple physics-informed baselines and uncertainty-calibrated models.
3. Apply hard composition constraints and screen candidates for known phase/processing feasibility before optimization.
4. Require prospective synthesis and blinded hardness/other application-specific tests before claiming material performance.
5. For Pangola-derived carbon, start a separate dataset and function-specific contract; do not transfer the alloy equation or its metrics.

This watch adds a candidate research method only. It establishes no material substitution, fuel/electricity benefit or economic result.
