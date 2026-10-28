# Research gap — exceptional-point speedup under accepted-output resource accounting

**Gap ID:** RG-FND003-NH-EP-001  
**Opened:** 2026-10-28  
**Primary owner:** Lane A — matched workload/control contract  
**Cross-lane owners:** B (target identity), C (state/retry/I/O), D/G (device/control), E (thermodynamics/cooling), F (evidence/economics), H (literature)  
**Status:** OPEN / LITERATURE_ONLY / RECONSTRUCTION_NOT_RUN  
**Related:** RG-FND003-QSL-CONTROL-BUDGET-001; FND-001, FND-003, FND-004, FND-006; EQN-001–EQN-006; INV-029–035  
**Source watch:** [non-Hermitian exceptional-point speedup and transition-rate QSL](literature_watch/2026-10-28-nonhermitian-ep-speedup-and-transition-rate-qsl.md)

## Problem statement

The literature reports faster entanglement generation near an exceptional point relative to an equivalent Hermitian interaction, together with lower success probability. A separate PRL framework derives transition-rate speed limits for general open quantum evolution, including measurements. The UQPU gap is not whether the reported paper result exists; it is whether a comparable, fully resource-accounted route can reduce time, energy or cost **per accepted useful output** under matched output quality and control assumptions.

## Incumbent and candidate

- **Incumbent:** Hermitian/unitary evolution with a declared interaction or spectral-width bound and an explicitly defined target-state fidelity.
- **Candidate:** a non-Hermitian/PT-symmetric effective trajectory near an exceptional point, represented by a consistent open-system or dilation model that includes failed outcomes.
- **Assumption change:** the candidate is not simply a faster closed-system unitary under identical assumptions. Its conditional dynamics, success probability and any added reservoir/control resources must be explicit.

## Mandatory checks

- Units, Hermitian limit, normalization, trace preservation for the complete channel, complete positivity where applicable, causality/no-signalling and resource conservation/accounting.
- Exact target subspace, initial state, fidelity/error tolerance, allowed controls and coupling/spectral-width budget.
- Separate theoretical bound, optimized model time, conditional success time and end-to-end accepted-output time.
- Hold out coupling strengths, exceptional-point detuning, noise and initial-state families. Search for counterexamples near and away from the exceptional point.
- Retain failures, retries, inconclusive cases, calibration sensitivity and all controller/reset/readout/reservoir costs.

## Acceptance and falsification

A model-level result requires two independently implemented evaluators to agree within a predeclared tolerance on frozen cases and to reproduce the appropriate Hermitian limiting behavior. A system-level advantage requires the candidate to improve total time, energy or cost per accepted output at matched quality after all failures and retries are included, followed by independent replication.

**Falsifier:** no robust improvement under the matched contract, or an apparent speedup erased by lower success probability, extra controls, reset, dissipation, measurement or cooling. Do not relax the acceptance criteria after seeing results.

## Evidence boundary

This is a preregistered research gap only. UQPU has not reproduced the trapped-ion experiment, reconstructed the transition-rate bounds, run a target-aware simulation or measured hardware energy/cost. No universal QSL violation, new physical law, QPU advantage or mission-level result is claimed. Paid QPU jobs remain unauthorized without credentials, a bounded budget and explicit user consent.
