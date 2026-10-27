# Batch 072 — memory-aware thermodynamic inference for FND-001

**Date:** 2026-10-27  
**Canonical starting main SHA:** 0dadabfb41d18f51e43a8722e6bd938d73961dfe  
**Primary owner:** Lane F — thermodynamic accounting and evidence  
**Publication owner:** Lane H  
**Implementation owner:** Lane A if the reproduction gate is funded  
**Evidence class:** LITERATURE_ONLY; no UQPU reproduction or measured physical/economic result

## Source and genuine novelty

Schwarz, Kolomeisky and Godec, “Consistent time reversal and reliable and accurate inference in the presence of memory,” arXiv:2410.11819v5 (revised 2026-10-01), accepted for Physical Review Letters 2026-09-25. Official source: https://arxiv.org/abs/2410.11819v5. Accepted-paper DOI: https://doi.org/10.1103/gwf7-6kvr.

The authors derive a k-th-order entropy-production estimator from coarse observations and conditions for guaranteed lower bounds under strong non-Markovianity. They report that Markovian estimators without a valid time-scale separation can produce artifacts and that an order that fails to capture the memory duration can overestimate dissipation. The useful delta is a concrete warning for memory-aware measurement design, not a new general physical law or a new quantum speed limit.

## UQPU integration

- **FND-001:** make observation-history length, estimator order, coarse-graining and time-scale-separation assumptions explicit before interpreting inferred dissipation.
- **FND-003:** preserve matched sampling, hidden-state assumptions and the same energy boundary in control-versus-quantum comparisons.
- **Lane C:** do not equate hidden/active process memory with readable classical storage.
- **Lanes E/F:** retain accepted-liquid and net-reliable-electricity accounting for BIO-001/FUS-001; inference cannot replace direct energy measurements.
- **Lane H / FIN-001:** improved uncertainty may reduce time-to-evidence only after independent validation; no rate/WACC result follows.
- **INV-034/035:** candidate method enters a falsifiable, source-pinned pipeline; present physical constraints remain binding.

## Reproduction gate

Pin the v5 paper and exact equations; independently implement the estimator and reference calculation; test finite-state processes with known memory and entropy production; preregister held-out process families and at least 30 seeds; compare saturated versus under-saturated estimator orders; report uncertainty, bias, bound violations, overestimation, resource use and failed cases; obtain independent rebuild. Do not apply to QPU/plant energy claims until a separate boundary-valid experiment exists.

## Non-claims

No UQPU reproduction, thermodynamic measurement, physical law, QPU advantage, phone compression, material substitution, accepted bio-oil, net fusion electricity, or financing benefit is established.
