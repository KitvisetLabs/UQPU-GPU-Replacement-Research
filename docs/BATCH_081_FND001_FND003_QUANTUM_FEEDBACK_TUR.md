# Batch 081 — FND-003 quantum-feedback TUR and precision-cost accounting

**Date:** 2026-10-27  
**Starting main SHA:** `74c7bad129a662e844d959ff3f7b86331a2261b4`  
**Primary technical owner:** Lane A — equation reconstruction and reference contract  
**Evidence/economics owner:** Lane F  
**Publication owner:** Lane H  
**Cross-lane review:** A–H explicitly; specialized Lane I reviewed and not materially coupled  
**Evidence class:** PEER_REVIEWED_THEORETICAL_RESULT / OFFICIAL PREPRINT; not independently reproduced by UQPU

## Research question

Can the project turn a newly published quantum-feedback thermodynamic uncertainty relation into a falsifiable, finite-dimensional reference test without treating information as free or mistaking precision bounds for compute speed, wall-plug energy, or cost/task?

## Fresh literature delta

Honma and Vu, “Thermodynamic Uncertainty Relation with Quantum Feedback,” *Physical Review Letters* 137, 160406, published 2026-10-16, DOI [10.1103/6d8l-94pv](https://doi.org/10.1103/6d8l-94pv); official preprint [arXiv:2602.22651v2](https://arxiv.org/abs/2602.22651v2), revised 2026-10-22. The paper derives a finite-time TUR for time-integrated currents in a finite-dimensional open quantum system with monitored quantum jumps and Markovian feedback. The bound includes entropy production and quantum mutual information exploited by feedback. Its model assumes weak thermal coupling, local detailed balance, instantaneous feedback, unital feedback maps, and a GKSL no-feedback baseline. The derivation uses \(\hbar=k_B=1\).

The source's central bound and correction term are recorded in the dated literature watch. This is distinct from Batch 080's conditional work-of-formation/extractable-work bounds. Neither result is a UQPU measurement.

## Work completed

- Added a primary-source literature watch that captures the paper's genuine novelty, model assumptions, equation boundary, limitations and exact UQPU relevance.
- Opened `RG-FND003-QUANTUM-FEEDBACK-TUR-REPRODUCTION-001` with a preregistered reproduction protocol and falsification conditions.
- Added a machine-readable A–I integration contract and a human-readable integration record, including all 36 lane-pair reviews.
- Updated README, WORKLOG and the cold-start handoff manifest in the same commit.
- Left the large append-only `RESEARCH_GAPS.md` unchanged; the focused gap is canonical and aggregate synchronization debt remains explicit.

## A–H lane status

| Lane | This cycle's status | Next gate |
|---|---|---|
| A — programming/workloads/compiler/runtime | Pinned the TUR equations and assumptions; no implementation promoted | Reconstruct the three-level clock and finite-time/limiting-case reference |
| B — cloud/QPU integration | Provider-neutral routes preserved; no target-specific mapping or execution | Only consider target mapping after a valid device boundary is specified |
| C — memory/state/data movement | Jump-outcome memory and state representation explicitly separated from classical-readable capacity | Define record bytes, transfers, retention and reset separately if simulated/implemented |
| D — devices/chips/fabrication/packaging | No new hardware result | Derive measurable readout/control/reset requirements only if a physical mapping is justified |
| E — biomass/materials/bio-oil/fusion/cooling | No direct technical result; no material/fuel/electricity claim | Keep BIO-001 and FUS-001 independent and active |
| F — economics/benchmarks/evidence | Separated \(\Sigma\), current variance, wall-plug energy and currency boundaries | Build matched estimator with uncertainty and accepted-task ledger after reproduction |
| G — manufacturing/factory systems | D/G co-design preserved; no process/yield result | Convert only validated device requirements into metrology/factory inputs |
| H — strategy/publication | Published source watch, focused gap, batch and integration record | Maintain cold-start discoverability and preserve strategic references |

INV-034/035 are upstream cross-cutting gates for A–H. Specialized Lane I was reviewed and marked not materially coupled to this quantum-feedback source.

## Integration and evidence

- **FND-001:** explicit information/entropy accounting; no information-free feedback assumption.
- **FND-003:** adds a theory-defined precision-cost comparator, not a quantum-speed-limit or runtime bound.
- **FND-006/EQN-001–006:** use the existing generator → constraints → evaluator → held-out test → counterexample → proof/simulation → discriminating experiment → independent replication → system/economics process.
- **INV-029–033:** no measured mission/pillar contribution. The US$10T–US$100T ambition remains a proxy requiring useful-service, energy, physical and lifecycle-cost contracts; no phone-compression, material-substitution, accepted bio-oil, net fusion electricity, lower financed principal or lower WACC is claimed.
- **INV-025–027:** preserve the falsifiable 100,000,000-GPU and universal 100,000,000-unit goals, equivalent-useful-output contracts, and the distinction between Hilbert-space size and readable classical memory.
- All eight high-visibility root directives, the Kanusanan Pongpanna Model, multilingual Thai/English/Chinese/Japanese/Korean/German plan links and recorded strategic AI-agent/funding references remain preserved.

## CI and synchronization

At the validated starting head `74c7bad129a662e844d959ff3f7b86331a2261b4`, prototype/invariant workflow [#1815](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40517537998) passed all 15 jobs and cold-start audit [#1023](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40517538004) passed. These validate the starting head only. Exact-head CI for the Batch 081 commit is the immediate gate. No paid QPU job was submitted.

## Next highest-value gate

Independently reconstruct Eqs. 1–18 from arXiv v2, freeze the three-level-clock parameter set, implement the tilted-Liouvillian and trajectory estimators separately, then test Eq. 15, Eq. 17, the no-feedback/classical limits, units and \(\Sigma\geq0\). Do not implement a formula-only helper before these checks pass. Continue Batch 080's work-bound reproduction, ergotropy SDP reproduction, Helios QEC reproduction, EQN-008 matched discovery comparison, BIO-001 and FUS-001.
