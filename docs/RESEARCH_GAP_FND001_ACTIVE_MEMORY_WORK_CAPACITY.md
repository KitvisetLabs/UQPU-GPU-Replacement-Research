# Research gap — FND001 active-memory work-capacity transfer

**Stable work ID:** FND001-ACTIVE-MEMORY-001  
**Opened:** 2026-10-26  
**Primary owner:** Lane A — workload/runtime benchmark contract  
**Integration owners:** Lane C and Lane F  
**Publication owner:** Lane H  
**Evidence state:** LITERATURE_ONLY + CONTRACT_ONLY  
**UQPU project evidence promoted:** none

## Objective

Test whether the distinction between passive input tapes and action-coupled percept–action environments in Fiderer et al. (PRX, 2026-10-05) has a reproducible consequence for UQPU memory-policy selection under identical accepted-output requirements.

## Current evidence

The source is a peer-reviewed theoretical framework using hidden Markov channels and a model-defined work-capacity objective. It identifies regimes where maximally predictive policies need not maximize that objective when the agent's actions affect future observations. This is not a measured energy result for software or hardware.

The repository's FND-001 adjacent-lag conditional-mutual-information diagnostics and synthetic calibrations remain MODEL_ONLY. They do not independently reproduce the source paper, establish a general memory/thermodynamic law, or show that a runtime policy lowers joules.

A lane-A benchmark contract and a dated literature watch now specify the test boundary. No executable runtime comparison or independent mathematical reproduction has yet been completed.

## Missing evidence

- An exact small-channel fixture with source-faithful transition and thermodynamic assumptions.
- An independent implementation of the source objective and a reference value for at least one tractable channel.
- Held-out comparisons across passive and active environments, matched on useful-output semantics, quality, horizon and total budget.
- Calibration for finite-horizon estimates and policy-selection uncertainty.
- Actual physical memory and energy measurements, if a model-level effect survives.
- An independent replication and a same-boundary cost-per-accepted-output record.

## Next gate

Freeze one finite-state active-feedback channel and its passive-tape control. Preregister `MEMORYLESS`, `PREDICTIVE` and `BOUNDED_MEMORY` policies, exact task quality, seeds, horizon, metrics and counterexamples before generating results. Verify the analytic/model objective independently before any hardware run. Preserve cases where the effect disappears or predictive policy wins.

## Stop rules

Do not proceed to a physical-energy claim if the exact-channel evaluator fails, if held-out policy rankings are unstable, or if quality and resource budgets cannot be matched. Do not call logical state size physical memory; do not infer energy from entropy without a validated physical mapping and calibrated measurement.

## Mission disposition

- **INV-029:** contributes only a proposed state/energy measurement gate; no phone-class compression evidence.
- **INV-030 / INV-031:** no material substitution, accepted liquid fuel or biomass process evidence.
- **INV-032:** no fusion result.
- **INV-033:** no measured CAPEX, financing, interest or WACC effect.
- **INV-034 / INV-035:** advances a falsifiable, mathematics-first research question while leaving established physics binding.
