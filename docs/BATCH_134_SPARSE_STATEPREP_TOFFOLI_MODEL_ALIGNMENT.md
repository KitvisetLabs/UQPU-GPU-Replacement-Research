# Batch 134 — sparse state-preparation Toffoli-cost model alignment

**Date:** 2026-10-29  
**Starting canonical main SHA:** 091c159584ee5a3adbdbe1aaaf00bf29059c3582  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Integration owner:** Lane F — benchmark, evidence and economics  
**Interfaces:** Lane C state/data movement; Lane B provider portability; Lanes D/G device and manufacturing; Lane H provenance/strategy  
**Evidence class:** PEER-REVIEWED EXTERNAL ALGORITHM + PREREGISTERED CONTRACT / NO UQPU REPRODUCTION

## 1. Canonical state and governance

The cycle began at the dynamically resolved main head 091c159584ee5a3adbdbe1aaaf00bf29059c3582, after Batch 133. It inspected the charter, version invariants, goals, README, operating system, open-frontier directive, strategic model and reference set, the permanent 00/00A/01–06 directives, latest Batch 132/133, state-preparation gaps, the eight-lane manifest, and the current CI state. The canonical A–H structure and 16-level depth rule remain unchanged. The multilingual Thai, English, Chinese, Japanese, Korean and German strategic-plan context and recorded strategic AI-agent/funding references are preserved; no strategic source was edited.

Before this change, both current-head GitHub Actions workflows succeeded:
- [Autonomous Cold-Start Handoff Audit](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40889615896)
- [UQPU Prototype and Project Invariants](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40889615921)

## 2. Fresh literature surveillance and delta

Fresh public-source checks covered equation discovery/formal theorem verification, quantum state preparation and sparse-QROM cost, biomass pyrolysis TEA, photonic/device inverse design, fusion economics and R&D finance. Most recent project watches already covered the broad AI-proof, equation-discovery and biomass topics; this pass found a source-specific state-preparation result not indexed in the repository.

Rupprecht and Wölk's peer-reviewed *Quantum* paper (published 2026-09-10; DOI 10.22331/q-2026-09-10-2208) reports an improved sparse-isometry construction and an approximately 2s worst-case Toffoli count for sufficiently large n, with author-reported numerical costs closer to s. The exact theorem/resource assumptions and code assets have not been independently reproduced by UQPU. Repository search for the DOI, article identifier and title returned no match, so this is new-to-repository rather than a claim that the paper was newly published today.

The source-specific watch records novelty, resource metric, limitations, project relevance and falsifiable follow-up. Toffoli count is kept separate from T-count, depth, ancillas and physical cost.

## 3. Lane A work and reproducibility contract

Added the preregistered comparison contract at research_lanes/A_quantum_programming_runtime/SPARSE_STATEPREP_TOFFOLI_BENCHMARK_V1.json and a standard-library regression test that checks source pinning, held-out/reproduction gates, cost metrics, memory semantics and the paid-QPU guard.

The contract keeps three related sources distinct:
- Rupprecht–Wölk, peer-reviewed sparse-isometry Toffoli construction;
- Luo–Li, arXiv:2608.00414, symbolic sparse-state-preparation T-count theorem contract;
- Li et al., arXiv:2607.28260v2, sparse-QROM/state-preparation result with its own input-access model.

No formula from one paper is substituted for another. No numeric resource saving is claimed. The test validates the preregistration schema, not the external theorem or a quantum circuit.

## 4. A–H status

| Lane | This cycle's advancement | Evidence boundary / next gate |
|---|---|---|
| **A — programming/workloads/compiler/runtime** | Added a source-pinned sparse-state-preparation benchmark contract and regression guard for the next exact small-instance comparison. | Reproduce circuits and align theorem assumptions before claiming savings. |
| **B — cloud/QPU/provider integration** | Provider-neutral execution path preserved; no target run or paid job. | Simulator/dry-run first; bind circuit, target, calibration, output and price to the same run. |
| **C — RAM/VRAM/HBM/storage/state/data movement** | Contract explicitly records classical description bytes, support discovery, transfers and output reconstruction separately from quantum state-space size. | Do not equate Hilbert-space dimension with readable classical memory. |
| **D — device/chip/process/fabrication/packaging** | Added translation requirements from logical Toffoli/T counts to depth, routing, ancillas, QEC and physical target assumptions. | No device-level performance inferred from gate count alone. |
| **E — biomass/materials/bio-oil/fusion/cooling/infrastructure** | Literature surveillance retained the current BIO-001/FUS-001 evidence boundaries; no new fuel, material or fusion claim. | Continue accepted-liquid-energy reconstruction and net-electricity accounting separately. |
| **F — economics/benchmarks/evidence/integration** | Added matched-output, held-out, provenance and full cost-per-accepted-task gates. | No end-to-end economic advantage measured. |
| **G — manufacturing equipment/software/factory systems** | D/G co-design remains active; manufacturing metrics are listed as downstream requirements, not inferred. | Require physical depth, yield, uptime and cost-per-good-output evidence. |
| **H — strategy/finance/future industries** | Kept strategic master-plan context and multilingual public references untouched; no financial or market effect inferred. | Integrate only after reproducible workload results and capital/time-to-evidence accounting. |

All 28 unordered A–H pairs remain part of the integration review rule. INV-034/035 remain upstream cross-cutting foundations. The legacy auxiliary Lane I is not reclassified or moved by this batch.

## 5. INV-029 through INV-035

- **INV-029:** state-preparation resource efficiency is only a possible subroutine contribution; no Data-Center-to-One-Phone service, energy, physical-compression or lifecycle-cost contract has passed.
- **INV-030:** no critical-material substitution or elemental-transmutation claim.
- **INV-031:** no accepted Pangola liquid fuel or commercial bio-oil economics.
- **INV-032:** no net reliable delivered fusion electricity result.
- **INV-033:** no lower financed principal, interest, project WACC or economy-wide rate measured.
- **INV-034:** theorem/model assumptions and small-instance counterexamples remain upstream mathematical work.
- **INV-035:** external algorithmic claims remain hypotheses to reproduce, not physical laws; preserve units, domain, falsifiers, held-out cases and independent verification.

INV-025/026/027 remain falsifiable and evidence-gated. Neither state-space dimension nor qubit count is treated as readable classical memory, and no 100x/100,000,000x target is reported as achieved.

## 6. Integration, tests and next gate

The benchmark contract and regression test were added with this batch. The test is intended to run under the existing prototype test suite. Current-head CI is reported separately after the commit; pre-change CI was green.

**Next highest-value gate:** retrieve/hash the official paper and assets, reproduce small-n circuits against an independent classical reference, then align the Toffoli, T-count and sparse-QROM theorem models on disjoint held-out (n, s, epsilon) cases. Only a matched useful-output workload can determine whether the subroutine improves total cost per accepted task.

No paid QPU job was submitted. No independent circuit reproduction, physical memory result, energy saving, quantum advantage, new physical law, material substitution, commercial fuel, fusion electricity or financing effect is claimed.
