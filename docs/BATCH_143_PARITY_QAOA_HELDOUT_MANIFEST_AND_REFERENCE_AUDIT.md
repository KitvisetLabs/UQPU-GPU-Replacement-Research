# Batch 143 — parity-QAOA held-out manifest and exact-reference audit

**Date:** 2026-10-30  
**Canonical starting main SHA:** 420c29c56be07ec799766f947d36a3eec78db618  
**Newest committed numbered batch at start:** Batch 142, resolved dynamically from the current main README and tree  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Integration owner:** Lane F — evidence/benchmark accounting  
**Cross-lane interfaces:** B/C/D/E/G/H and FND-001–006 / EQN-001–006  
**Evidence class:** SOFTWARE_CONTRACT + MODEL_ONLY_EXACT_SMALL_INSTANCE_REFERENCE  
**No paid QPU job, target execution, physical experiment, material test, fuel production or financing transaction was performed.**

## 1. Canonical cold start and CI

Started from current main SHA 420c29c56be07ec799766f947d36a3eec78db618, not a remembered batch number. Inspected the charter, invariants, goals, README, research operating system, open-frontier directive, Kanusanan Pongpanna Model, strategic references, newest batches, research gaps, all A–H lane workspaces, integration records, foundational/equation-discovery code and Actions state. The eight high-visibility root directives 00, 00A and 01–06 are present. The six-language Thai, English, Chinese, Japanese, Korean and German public master-plan links and strategic AI-agent/funding references remain preserved.

The starting head had exact-head core run [#2137](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40996048424) successful with all 16 check-runs green, and cold-start audit [#1427](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40996048508) successful. These validate the starting SHA only; this Batch 143 commit requires its own Actions observation. PR #152 remains open/draft/unmerged; PR #153 remains open/unmerged. Neither was merged.

## 2. Priority-1 Lane A advance

Created a frozen pilot manifest for workload contract SIGNED-MAXCUT-PARITY-QAOA-001 and acceptance contract SIGNED-MAXCUT-PARITY-QAOA-ACCEPTANCE-001:

- 10 signed-weight graphs: 4 train, 3 validation and 3 test;
- graph families are split-disjoint: tree/cycle; grid/prism/complete-bipartite; wheel/complete-minus-matching;
- canonical sorted undirected edges and signed weights are preserved;
- exact classical logical references enumerate all 2^|V| assignments, totaling 688 logical assignments across the 10 fixtures;
- the exact reference file records each optimum score and the complete argmax set;
- common output is one decoded logical vertex bitstring scored by the same signed objective;
- parity samples must satisfy every fundamental-cycle even-parity constraint before decoding;
- normalized regret is max(0,C*−C(x))/max(1,Σ|w|), with a preregistered quality threshold of 0.05;
- proposed p=1 comparison budget is 8,192 shots, 32 optimizer evaluations and 10 independent repetitions per instance/method, identical for direct and parity encodings.

The public exact references are available for audit and final scoring, not for method/hyperparameter selection. The test set is not secret; governance requires that test optima/reference certificates do not inform selection. The manifest is PREREGISTERED_NOT_EXECUTED. No direct/parity QAOA optimization, SDK cross-check, target-aware simulation, real-QPU execution or CPU/GPU/NPU comparison was run.

The exact logical reference scores are: train star-5 5.0, cycle-4 2.5, path-6 6.0, branch-6 4.2; validation grid-2x4 8.0, prism-6 5.3, K2,3 3.5; test wheel-5 5.2, wheel-6 5.7 and K6-minus-matching 4.7. These are bounded classical objective certificates, not algorithm-performance evidence.

The manifest SHA-256 is b38bd65557b011a5519eae7a1360ed72cc31d9f141f16ad1f7bfa72a5c72ef7d. The exact-reference JSON SHA-256 is 573ad3150cff7032d9325c864417b9c08f57ceda7777796f0f8d0abc9cbd52ee. Six local isolated tests passed for hash binding, split/family disjointness, canonical signed graph inputs, exhaustive optimum/argmax recomputation, acceptance/budget schema and test-selection/no-paid-job guards. Repository exact-head CI remains the release gate.

## 3. Fresh literature surveillance

Fresh public searches covered symbolic regression, neural-symbolic equation discovery, AI-assisted mathematical/theorem discovery, differentiable and physics-informed modeling, automated experiment design, effective/constitutive laws, no-go/lower bounds, QEC decoder systems, particle/QFT, biomass conversion, fusion costing and R&D finance.

No new-to-main primary source was found that warrants a duplicate literature-watch article. The current literature trail already covers:

- Hsu et al., EVENET, *Nature Machine Intelligence*, version of record published 2026-10-29, DOI 10.1038/s42256-026-01322-9. The paper reports pretraining on about 500 million simulated collision events, approximately 10^5 GPU-hours on 512 A100 GPUs and 4 TB raw simulation reduced to about 180 GB of training data. Its downstream fine-tuning comparison excludes the one-time pretraining cost. This is external classical foundation-model evidence; any UQPU lifecycle comparison must explicitly amortize pretraining, preprocessing, storage, transfer and deployment over accepted tasks rather than treating the initial investment as free.
- Regazzoni's peer-reviewed Neural-DFEM article, published 2026-09-06, DOI 10.1007/s00466-026-02850-2; its reported validation is synthetic and same-solver, with isotropic path-independent hyperelastic scope.
- Hoshisashi et al., derivative-constrained PINNs, *Physical Review E* 113, 055301, published 2026-05-04, DOI 10.1103/5bbf-p6zk.
- Yan et al., neural QEC decoder accuracy/latency/quantization study, arXiv:2605.12046, submitted 2026-05-12.
- ProofEvolve, arXiv:2608.26334, submitted 2026-08-26; SymbolFit v2, arXiv:2607.19750 revised 2026-10-19; and the CoSR/AI theorem-discovery watches already indexed in main.

These remain third-party literature. No external result was converted into UQPU evidence, a new physical law, material substitution, accepted fuel, net fusion electricity or a financing result.

## 4. Explicit A–H status

| Lane | Status this cycle | Next highest-value gate |
|---|---|---|
| **A — Quantum programming/workloads/compiler/runtime (Priority #1)** | Added the 10-instance signed-Max-Cut train/validation/test manifest, exact logical references and six manifest/reference tests. Existing parity circuit/statevector prototype remains. Matched direct-versus-parity algorithm run is not executed. | Implement the paired runner; verify the complete logical-to-physical mapping and decoder; compare on the frozen split with equal shots/optimizer budgets and exact references. |
| **B — Cloud/QPU/provider integration** | Provider-neutral routes remain for IBM Quantum, Amazon Braket, Azure providers, IonQ, Rigetti, D-Wave Leap, IQM, Quantinuum, Pasqal, QuEra, Quandela and OQC. No provider job or paid execution. | SDK cross-check and target-aware simulator/dry-run first; bind target, calibration and price to the same run. |
| **C — RAM/VRAM/HBM/storage/state/data movement** | No new RAM/VRAM/HBM, storage, transfer or state-materialization measurement. Logical enumeration counts are not classical memory claims. | Record peak memory, state representation bytes, input/output/transfer, host preprocessing, reconstruction and I/O for the same accepted-output contract. |
| **D — Device/chip/process/fabrication/packaging** | Existing parity phase-gadget prototype remains a software model; no device, native-gate, fabrication or packaging result. Neural-DFEM remains literature-only. | Map the direct/parity circuits to a specified native gate set/topology/noise model and measure routing/depth; retain MAT-NEURAL-DFEM-001's source/material-class gate. |
| **E — Biomass/materials/bio-oil/fusion/cooling/infrastructure** | BIO-001 and FUS-001 remain open. No Pangola functional substitution, accepted liquid fuel or net delivered fusion electricity. | Measure accepted liquid mass/energy/quality and net reliable delivered fusion electricity under full lifecycle boundaries. |
| **F — Economics/benchmarks/evidence/integration** | Added a hash-bound workload manifest and exact reference certificate with equal-budget and accepted-output definitions. No provider price, energy, cost/task or project-finance measurement. | Populate every resource/cost field from paired runs; unknown costs stay unknown; never mix providers or calibration epochs. |
| **G — Manufacturing equipment/software/factory systems** | D/G co-design remains explicit; no process window, equipment throughput, yield or cost-per-good-device result. | Translate measured native-gate/device requirements into process/metrology and equipment budgets only after a device acceptance envelope exists. |
| **H — Ketskaew Chulamani/Kanusanan Pongpananna Model strategy/finance/publication** | This batch, daily report and machine record are linked from README and the integration hub. Strategic model and six-language plan links remain preserved. | Publish only independently reproduced computing/material/energy/finance evidence; maintain AI-agent/funding provenance. |

## 5. Foundational physics and equation discovery

FND-001 thermodynamic-gap accounting, FND-002 output-information lower bounds, FND-003 matched control-versus-quantum-speed-limit measurement, FND-004 alternative physical primitives, FND-005 QFT/elementary-particle mechanism scans and FND-006 mathematics-first invention remain active and evidence-gated. The existing fundamental_limits.py, frontier_hypothesis.py and equation_discovery.py helpers were inspected. No new thermodynamic measurement, physical bound, particle mechanism, theorem, equation or experimental anomaly was established in this cycle.

EQN-001 through EQN-006 remain subject to the generator → explicit constraints → evaluator → held-out test → counterexample search → proof/simulation → discriminating experiment → independent replication → device/system consequence → economics pipeline. Current physical equations remain binding for present engineering claims. AI-generated equations, symbolic fits and formal proof structures are not promoted to physical law by declaration.

## 6. INV-029 through INV-035 and INV-025/026/027

- **INV-029:** advances only a bounded software workload contract and reference path. No data-center service replacement, phone-class physical compression or cost capability is demonstrated.
- **INV-030:** no Pangola-derived material qualification or functional substitution; ordinary chemistry is not elemental transmutation.
- **INV-031:** no accepted saleable bio-oil/fuel; BIO-001 remains open.
- **INV-032:** no reliable net delivered fusion electricity; FUS-001 remains open.
- **INV-033:** no project principal, interest, WACC or hurdle-rate reduction measured. Lower financed principal and lower rates remain separate evidence questions.
- **INV-034:** strengthens a bounded mathematical reference and reproducibility gate; no new foundational physical result.
- **INV-035:** preserves the permanent equation-discovery discipline and records positive/negative evidence boundaries; no AI-generated physical law is accepted.
- **INV-025/026/027:** the 100,000,000-GPU and universal 100,000,000-unit GPU/CPU/NPU/RAM/VRAM/storage goals remain falsifiable moonshots. No subsystem replacement or NPU advantage is established; future NPU comparisons must use real neural-workload quality, precision, latency, throughput, memory/data movement and cost, not TOPS alone.

## 7. Integration, synchronization and next gate

Updated the canonical README front page, focused RG-QAOA-PARITY-001 gap, A-lane README, integration index, cold-start handoff manifest, WORKLOG.md and RESEARCH_GAPS.md. The complete pre-update WORKLOG.md and RESEARCH_GAPS.md snapshots were fetched; their UTF-8 byte counts matched the Git tree sizes before append, preserving their historical prefixes. This cycle's aggregate gap/worklog sync is complete. Older historical branch/fork and previously recorded sync debt remains open; no inaccessible history is claimed reconciled.

The repository continues to use docs/gap records and benchmark artifacts for evidence; no unsupported root evidence directory or fabricated measurement was created. No paid QPU job was submitted. No PR was merged.

**Next highest-value gate:** implement and run the matched direct-versus-parity QAOA pilot on the frozen manifest, first with exact classical references and independent SDK reconstruction, then target-aware simulation. Record accepted quality, shots, optimizer evaluations, latency, throughput, qubits, native/routed gates/depth, memory/state/I/O/transfer, retries, decoding/reconstruction, host compute, billable usage, energy where measurable and total cost per accepted task. Real-QPU execution remains blocked until explicit user consent, credentials and a bounded budget exist.
