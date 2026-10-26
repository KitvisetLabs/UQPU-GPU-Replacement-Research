# Research gap — FND001 active-memory work-capacity transfer

**Stable work ID:** FND001-ACTIVE-MEMORY-001  
**Opened:** 2026-10-26  
**Primary owner:** Lane A — workload/runtime benchmark contract  
**Integration owners:** Lane C and Lane F  
**Publication owner:** Lane H  
**Evidence state:** MODEL_ONLY_ANALYTIC_REFERENCE_REPRODUCTION + LITERATURE_ONLY  
**UQPU project evidence promoted:** none

## Objective

Test whether the distinction between passive input tapes and action-coupled percept–action environments in Fiderer et al. (PRX, 2026-10-05) has a reproducible consequence for UQPU memory-policy selection under identical accepted-output requirements.

## Current evidence

The source is a peer-reviewed theoretical framework using hidden Markov channels and a model-defined work-capacity objective. It identifies regimes where maximally predictive policies need not maximize that objective when the agent's actions affect future observations. This is not a measured energy result for software or hardware.

The repository now independently evaluates the paper's tractable binary memoryless invariant channel. With `P(A=0)=1/sqrt(2)`, the computed normalized work rate is `0.27155330316361204 k_B T ln(2)` per round, agreeing with the published analytic expression `0.2715533031636119` within `1.11e-16`. A passive IID-tape control with the same output marginal at this operating point gives `0.39912396330714384 k_B T ln(2)` per round. This is a contrast between different environment assumptions, not a matched physical experiment or an energy-saving claim.

A new *Nature Physics* experiment published 2026-10-16 reports work extraction from environmental memory in an optically trapped Brownian-particle system. It is an empirical thermodynamic result for that system/protocol, not validation of UQPU's software model or energy savings.

The repository's adjacent-lag conditional-mutual-information diagnostics and synthetic calibrations remain MODEL_ONLY. No general finite-memory policy comparison, physical memory measurement, calibrated energy measurement or independent replication has been completed.

## Missing evidence

- A finite-state memoryful agent/environment evaluator with a separately calculated stationary/asymptotic reference.
- Held-out comparisons across passive and active environments, matched on useful-output semantics, quality, horizon and total budget.
- Calibration for finite-horizon estimates and policy-selection uncertainty.
- Actual physical memory and energy measurements, if a model-level effect survives.
- An independent replication and a same-boundary cost-per-accepted-output record.

## Next gate

Extend the evaluator to a finite-state memoryful channel and verify its stationary/asymptotic work rate with an independent calculation. Then preregister `MEMORYLESS`, `PREDICTIVE` and `BOUNDED_MEMORY` policies, exact task quality, seeds, horizon, metrics and counterexamples before generating held-out results. Preserve cases where the effect disappears or predictive policy wins.

## Stop rules

Do not proceed to a physical-energy claim if the exact-channel evaluator fails, if held-out policy rankings are unstable, or if quality and resource budgets cannot be matched. Do not call logical state size physical memory; do not infer energy from entropy without a validated physical mapping and calibrated measurement.

## Mission disposition

- **INV-029:** contributes only a proposed state/energy measurement gate; no phone-class compression evidence.
- **INV-030 / INV-031:** no material substitution, accepted liquid fuel or biomass process evidence.
- **INV-032:** no fusion result.
- **INV-033:** no measured CAPEX, financing, interest or WACC effect.
- **INV-034 / INV-035:** advances a falsifiable, mathematics-first research question while leaving established physics binding.
