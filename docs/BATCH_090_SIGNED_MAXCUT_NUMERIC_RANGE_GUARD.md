# Batch 090 — signed Max-Cut numeric-range guard

**Date:** 2026-10-28  
**Canonical starting main:** `ac1a947cefcde185a9b4a41902dec1af9bdea3b7`  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Cross-lane owners:** B/C/D/E/F/G/H; FND-001–006; EQN-001–006  
**Evidence class:** SOFTWARE_CONTRACT_ONLY / CODE-LEVEL COUNTEREXAMPLE  
**Hardware:** no real QPU, no paid job, no physical experiment

## Starting-state audit

The latest main SHA was resolved from GitHub. The mandatory charter, invariants, goals, README, operating system, open-frontier directive, Kanusanan Pongpanna Model, strategic reference links and permanent root directives 00/00A/01–06 were inspected, together with Batches 089 and 088, the current Lane A signed-Max-Cut objective and tests, the gate-specific QSL contract/gap, current evidence/gaps and exact-head CI. Main's pre-change prototype/invariant workflow [#40600344171](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40600344171) and cold-start audit [#40600344313](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40600344313) passed. This change requires its own exact-head checks.

The A–H operating policy and legacy A–I manifest discrepancy remains open; no lane aliases or historical records were deleted. Thai, English, Chinese, Japanese, Korean and German master-plan links and the strategic AI-agent/funding references remain preserved. The large append-only WORKLOG.md and RESEARCH_GAPS.md were fetched in full and appended without truncating prior history.

## Lane A — discovered numeric-range defect

The existing reference rejects non-finite input weights, but finite inputs alone do not guarantee that their derived representation remains finite in binary64:

1. A weight near (10^{308}) can make the QUBO pair coefficient (-2w) overflow to infinity.
2. Several individually representable weights (for example, three (8\times10^{307}) incident edges) can overflow an accumulated QUBO linear coefficient.
3. Even when every compiled coefficient is finite, a valid bit assignment can make the direct, QUBO or Ising objective sum exceed the representable floating-point range.
4. Converting an integer far outside the float range can raise `OverflowError` before the old `isfinite` validation.

These are numeric-representation failures, not a failure of the underlying Max-Cut mathematics. Returning infinity or accepting a non-finite coefficient would break the promise that direct, QUBO and Ising scores share one auditable objective contract.

## Change implemented

In `software/uqpu-prototype/uqpu/signed_maxcut_objective.py`:

- added a finite-sum helper that normalizes `math.fsum` overflow and non-finite results to a clear `ValueError`;
- checks derived QUBO and Ising coefficients before storing them;
- checks accumulated QUBO linear coefficients and computes the Ising constant from individually halved weights;
- applies the finite-sum guard to direct, QUBO and Ising scoring;
- normalizes huge-integer float-conversion overflow to the same fail-closed input-validation contract.

In `software/uqpu-prototype/tests/test_signed_maxcut_objective.py`, regression tests cover derived-pair overflow, linear-coefficient overflow, out-of-range integer conversion, and score overflow in all three representations. Existing signed-weight, empty-graph, objective-equivalence, maximizer-set and malformed-input tests are preserved.

## Evidence and falsification

The finding is a code-level counterexample discovered by inspecting arithmetic paths. The fix is accepted only if the exact-head core CI and cold-start handoff audit pass. A failing regression means the affected arithmetic path remains unverified; it must not be waived because ordinary small fixtures pass.

This is not a QAOA circuit, provider-neutral SDK lowering, target-aware simulation, real-QPU result or quantum advantage. The next Lane A gate remains an independent pinned-SDK reconstruction of the signed-Max-Cut Hamiltonian/sign convention against exhaustive tiny-instance objective values and the full argmax set.

## Fresh literature surveillance

Fresh searches covered AI-assisted mathematical/theorem discovery, symbolic regression and progressive equation discovery, gate-specific quantum speed limits, physics-informed neural operators, certified QLDPC-decoder references, automated experiment design, thermodynamic logic-gate energy, fusion cost drivers and biomass-liquid upgrading. Material sources found in this search were already recorded in main and were checked rather than duplicated:

- Nelson & Barnes, *Physical Review A* accepted 2026-10-15, exact gate quantum speed limits, [official APS record](https://journals.aps.org/pra/accepted/10.1103/28zn-ch8y): still requires full theorem/proof reconstruction and independent optimal-control checks.
- Xia & Zhang, *Physical Review Research* accepted 2026-10-06, progressive symbolic discovery of physical laws (CoSR), [official APS record](https://journals.aps.org/prresearch/accepted/10.1103/f2kp-pp4q): reported symbolic-regression fit remains external evidence, not a physical-law discovery by UQPU.
- Banfi et al., certified non-degenerate ML benchmarking for quantum LDPC decoders, [official arXiv preprint](https://arxiv.org/abs/2610.28008), submitted 2026-10-20: the non-degenerate reference and undecided shots must remain explicitly scoped.
- Xue et al., physics-informed lattice-Boltzmann neural operators, [Nature Communications DOI](https://doi.org/10.1038/s41467-026-75730-1): reported speedups are simulation-case-specific and still require reproduction and break-even accounting.
- Whitelam, thermodynamic logic gates and heat emission, *Physical Review E* 114, 034135, published 2026-09-21, [DOI](https://doi.org/10.1103/9lv8-drtp): heat emission is not automatically wall-plug electricity.

No additional material source was found that was both relevant and unrecorded in canonical main; therefore no duplicate literature-watch article was created this cycle. None of these external results is UQPU project evidence.

## A–H status ledger

- **A — Quantum programming/workloads/compiler/runtime (Priority #1):** numeric overflow now fails closed in the signed-Max-Cut classical reference; regression coverage added. Independent pinned-SDK Hamiltonian reconstruction remains open.
- **B — Cloud/QPU/provider integration:** provider-neutral architecture unchanged; no provider, target, price or calibration was validated and no job was submitted. Keep IBM Quantum, Amazon Braket, Azure Quantum/providers, IonQ, Rigetti QCS, D-Wave Leap, IQM, Quantinuum, Pasqal, QuEra, Quandela, OQC and emerging providers distinct by target and billing context.
- **C — RAM/VRAM/HBM/storage/state/data movement:** objective arithmetic guards improve input/result integrity only; no readable-storage, output-information or state-space equivalence is inferred.
- **D — Device/chip/process/fabrication/packaging:** no device or fabrication result. Future Hamiltonian mapping still needs target-specific control, fidelity, leakage and coefficient-convention provenance.
- **E — Biomass/materials/bio-oil/fusion/cooling/infrastructure:** BIO-001 accepted-liquid and FUS-001 net-electricity evidence remains open; no Pangola material qualification, accepted fuel or delivered fusion electricity.
- **F — Economics/benchmarks/evidence/integration:** non-finite scores are invalid comparison evidence and now fail closed. No measured energy, cost/task advantage, financing principal/interest or WACC result.
- **G — Manufacturing equipment/software/factory systems:** continuous D/G co-design remains active; no equipment, yield, cost-per-good-device or factory evidence.
- **H — Kanusanan Pongpanna Model strategy/finance/future industries/publication:** README, WORKLOG, RESEARCH_GAPS and integration hub now expose this cycle; all multilingual master-plan links and recorded strategic agent/funding references are preserved.

## Foundational and equation-discovery status

- **FND-001:** no measured work, heat or wall-plug energy; objective-score validity is not a thermodynamic measurement.
- **FND-002:** no output-information or readable-memory lower bound changed.
- **FND-003:** gate-specific QSL remains an external theorem candidate pending reconstruction and matched optimal-control comparison.
- **FND-004:** no alternative physical primitive was demonstrated.
- **FND-005:** no validated QFT/elementary-particle mechanism delta.
- **FND-006:** advances the mathematics-first counterexample pattern: identify an incumbent assumption, construct an explicit failure case, enforce constraints, and preserve regression tests.
- **EQN-001–006:** no candidate is promoted to a physical law. The change is a finite-arithmetic software guard, not an equation-discovery result.

## INV-029 through INV-035 and moonshot boundary

- **INV-029:** no phone-class physical-compression evidence; a remote terminal remains insufficient.
- **INV-030:** no Pangola-carbon functional substitution or material qualification.
- **INV-031:** no accepted bio-oil/fuel cost or commercial process result.
- **INV-032:** no reliable net delivered fusion-electricity result.
- **INV-033:** no measured financed-principal, absolute-interest, project-risk-premium or WACC result.
- **INV-034:** foundational search and falsification discipline remain active.
- **INV-035:** mathematical/AI hypothesis generation remains open, while current physics and evidence gate technology claims.

INV-025/026/027 and the 100,000,000-GPU / universal 100,000,000-unit GPU/CPU/NPU/RAM/VRAM/storage targets remain falsifiable goals. No Hilbert-space-to-classical-memory equivalence or NPU-TOPS-only comparison is claimed.

## Integration, synchronization and next gate

The source change, tests, Batch 090, focused gap, integration report, README latest-cycle summary and append-only WORKLOG/RESEARCH_GAPS updates are designed for one atomic main-branch commit with a `Research-Sync: main` trailer. Exact-head CI must be inspected after the commit. The pre-existing manifest A–I mismatch and any unmerged PR/branch sync debt remain explicit rather than being hidden by a partial migration.

**Next highest-value gate:** run the exact-head regression/architecture workflows; then independently lower the signed-Max-Cut objective into a pinned SDK Hamiltonian, compare all tiny-instance energies and complete argmax sets with the exhaustive oracle, and proceed to target-aware simulation only if the reference, quality and resource contracts pass. Paid QPU jobs remain prohibited without credentials, a bounded budget and explicit user consent.
