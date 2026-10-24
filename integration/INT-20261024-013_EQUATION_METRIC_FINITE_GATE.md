# Integration contract INT-20261024-013 — fail-closed equation-discovery metric validation

**Date:** 2026-10-24  
**Status:** `PROPOSED / CODE_FIX_COMMITTED / HOSTED_CI_PENDING`  
**Primary owner:** Lane F — evidence/benchmark integration  
**Technical owner:** Lane A  
**Cross-cutting:** INV-034, INV-035, FND-006, EQN-001–006  
**Base SHA:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`

## Shared contract

A held-out metric is admissible only when it is a finite, non-negative real number. Missing measurements may remain `None`; they must not be replaced with zero. A malformed metric cannot be used to declare improvement or qualify a candidate equation for a physical-candidate discussion. Independent-validation counts must be non-boolean, non-negative integers.

The change is limited to the software acceptance boundary in `equation_discovery.py` and its tests. It does not modify the candidate equation, baseline physics, evaluation data, experimental result or evidence taxonomy.

## A–H review

| Lane | Cycle status and interface |
|---|---|
| A — quantum programming/workloads/compiler/runtime | **Advanced:** hardened the EQN-002/003/004/005/006 metadata gate against non-finite metric promotion; four focused regression-test methods added. |
| B — cloud/QPU/provider integration | **Reviewed / unchanged:** zero provider calls and zero QPU jobs; simulator/dry-run-first policy preserved. |
| C — memory/state/data movement | **Reviewed / unchanged:** no memory-capacity inference; the metric guard does not equate Hilbert-space dimension with readable classical memory. |
| D — device/chip/process/packaging | **Reviewed / unchanged:** no device requirement, material property or physical primitive is inferred from software validation. |
| E — biomass/materials/bio-oil/fusion/cooling | **Reviewed / unchanged:** BIO-001 and FUS-001 remain without new measured evidence; no saleable-fuel, net-electricity or material-substitution claim. |
| F — economics/benchmarks/evidence/integration | **Advanced:** invalid metric records fail closed; unknown energy/cost remains unknown; CI is the next acceptance gate. |
| G — manufacturing equipment/software/factory systems | **Reviewed / unchanged:** D/G co-design remains active, but no device requirement is ready to translate into process windows, yield or factory economics. |
| H — strategy/finance/future-industry research | **Advanced:** the defect, source provenance, literature boundary and cheapest next validation step are documented without claiming a scientific result or WACC change. |

The repository also carries specialist Lane I in its current manifest. It remains unchanged because this metric-validation defect has no demonstrated causal edge to that lane. This does not replace or suspend the permanent A–H architecture.

## Foundational and equation-discovery trace

- **FND-001:** no measured energy-per-accepted-task update.
- **FND-002:** no change to output-information lower bounds or classical readout requirements.
- **FND-003:** no matched control/quantum-speed-limit experiment.
- **FND-004 / FND-005:** no new physical primitive or particle/QFT mechanism.
- **FND-006:** improves the integrity of a mathematics-first discovery gate.
- **EQN-001:** the initial scan matched the current main watch and pending branches; a subsequent expanded scan found arXiv:2610.29170 on joint target/compiler configuration selection, recorded separately in pending PR #62. This is a literature-only delta and not a new equation or physical-law claim.
- **EQN-002:** protects held-out error accounting from NaN/infinity.
- **EQN-003:** no new generator or physical constraints; current constraints remain binding.
- **EQN-004:** invalid metrics cannot appear to pass the falsification gate.
- **EQN-005:** no established physical assumption is changed.
- **EQN-006:** no downstream device/system/economic consequence is promoted.

## INV-029 through INV-035

- **INV-029:** no phone-class physical-compression or lifecycle-cost evidence.
- **INV-030:** no Pangola-derived functional material substitution; no transmutation claim.
- **INV-031:** no accepted liquid-fuel or commercial bio-oil evidence.
- **INV-032:** no reliable net delivered fusion-electricity or lifecycle-cost evidence.
- **INV-033:** no project principal, interest, WACC or risk-premium measurement.
- **INV-034:** current mathematical/physical constraints remain binding.
- **INV-035:** malformed candidate metrics cannot open the physical-candidate gate; AI-generated equations remain hypotheses until independent proof/experiment and validation.

INV-025/026/027 remain preserved. The 100,000,000-GPU and universal 100,000,000-unit subsystem goals remain falsifiable moonshots, not achieved results.

## Acceptance and rollback

Acceptance requires exact-head CI to pass, including the focused equation-discovery tests and repository invariant/cold-start checks. If it fails, keep the branch open and repair the defect without relaxing the tests. Rollback is a normal revert of this branch; no provider, hardware, material or external system state was changed.

## Canonical memory / sync

This artifact is additive. It does not rewrite `PROJECT_CHARTER.md`, `VERSION_INVARIANTS.md`, `GOALS.md`, `README.md`, `RESEARCH_GAPS.md`, `WORKLOG.md`, the root directives 00–06, or `STRATEGIC_PLAN_REFERENCES.md`. The multilingual master-plan links and recorded strategic AI-agent/funding references remain intact. Until merge, this work is pending-main and must not be described as canonical main-branch content.
