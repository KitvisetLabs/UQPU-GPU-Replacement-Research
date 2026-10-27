# Research gap RG-FND001-MEMORY-AWARE-INFERENCE-001 — thermodynamic inference with finite memory

**Opened:** 2026-10-27  
**Status:** OPEN / LITERATURE_ONLY / REPRODUCTION_NOT_RUN  
**Primary owner:** Lane F — thermodynamic accounting, uncertainty, and evidence  
**Source owner:** Lane H — literature publication  
**Implementation owner if unlocked:** Lane A  
**Cross-lane consumers:** C, D, E, F, H; FND-001 and FND-003

## Objective

Test whether a memory-order-aware entropy-production estimator can improve the reliability of thermodynamic inference from coarse trajectories without replacing direct energy measurements or promoting a model result to a physical bound.

## Evidence

Schwarz, Kolomeisky and Godec, “Consistent time reversal and reliable and accurate inference in the presence of memory,” arXiv:2410.11819v5, revised 2026-10-01 and accepted for Physical Review Letters on 2026-09-25. [Official arXiv source](https://arxiv.org/abs/2410.11819v5); [APS accepted-paper record](https://doi.org/10.1103/gwf7-6kvr).

The authors report a k-th-order estimator and necessary/sufficient conditions for guaranteed lower bounds on dissipation in strongly non-Markovian settings. They warn that a first-order Markov estimator without time-scale separation can create artifacts, and that an estimator order insufficient to capture the relevant memory can overestimate dissipation. UQPU has not reproduced this result.

## Blockers and current alternative

The exact theorem assumptions and estimator equations have not been independently reconstructed in this cycle. There is no UQPU trace dataset with a verified ground-truth entropy-production rate, no pinned reproduction, and no device/plant energy measurement. The current alternative is direct, boundary-complete energy accounting; model-inferred dissipation remains a separate diagnostic.

## Unlock criteria

- Pin source version, assumptions, equation text, code/data provenance, and license.
- Independently implement the estimator and reference calculation.
- Use preregistered finite-state process families with known memory and exact reference entropy production.
- Test memory-order saturation and time-scale-separation conditions on held-out trajectories and process families.
- Report uncertainty, bias, lower-bound violations, overestimation frequency, failures, runtime, and all resource use across at least 30 fixed seeds.
- Independently rebuild the result before applying the method to lab traces.
- Keep classical coarse-grained inference distinct from quantum-process claims and direct wall-plug energy.

## Falsifier and stop rules

Reject a proposed benefit if it disappears under held-out process families, depends on post-hoc choice of memory order, violates the source theorem's assumptions, overestimates dissipation outside its stated guarantees, or cannot be independently rebuilt. Do not use this method as a substitute for direct energy metering. No claim of a new law, Landauer-bound improvement, quantum speedup, or commercial energy/cost reduction is permitted.

## Dependencies and next review trigger

Depends on FND-001 active-memory accounting, FND-003 matched control/quantum boundary contract, exact source-text inspection, and reproducible synthetic trajectories. Review after the pinned estimator implementation and independent reference test exist; until then this is a literature-only gap.
