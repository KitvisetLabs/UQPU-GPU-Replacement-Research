# Batch 141 — EveNet immutable asset pins and foundational thermodynamics frontier

**Date:** 2026-10-30 09:14 ICT  
**Starting canonical main SHA:** e55f9c3d29429c5850cec79babb5d803787641ad  
**Newest committed batch at start:** Batch 140  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Cross-cutting owners:** FND-001–006, EQN-001–006; lanes B–H  
**Evidence class:** UPSTREAM ASSET METADATA + PEER-REVIEWED LITERATURE + OFFICIAL PREPRINTS / NO PROJECT REPRODUCTION

## 1. Canonical state and preservation audit

Started from the newest main commit, e55f9c3d29429c5850cec79babb5d803787641ad. Read the current PROJECT_CHARTER.md, VERSION_INVARIANTS.md, GOALS.md, README.md, research operating system, open-frontier directive, Ketskaew Chulamani/Kanusanan Pongpanna Model, STRATEGIC_PLAN_REFERENCES.md, permanent root directives, Batch 140 and Batch 139, focused gaps, integration handoff and evidence/CI records.

All high-visibility root directives 00, 00A, and 01–06 are present. docs/KANUSANAN_PONGPANNA_MODEL.md remains canonical. The strategic reference index still includes Thai, English, Chinese, Japanese, Korean and German public master-plan context and the recorded strategic AI-agent/funding references. INV-025/026/027 and the permanent A–H architecture remain preserved.

Batch 140 was the newest committed numbered batch at start. Its FUS-001 maintenance-aware net-electric costing and FIN-001 hurdle-rate/WACC separation remain active; this cycle does not replace or overstate those model-only results.

## 2. Lane A — HEP-EVENET-003 immutable asset pinning

### New verified source metadata

The Lane A asset manifest is research_lanes/A_quantum_programming_runtime/EVENET_ASSET_PIN_MANIFEST_2026-10-30.json.

| Asset | Pinned source | Source metadata verified | Still open |
|---|---|---|---|
| EveNet code | EveNet-HEP/EveNet-Full@06c3181d9a0f7df3e30edbb1c355b6fec8b5a3ad | MIT; Python >=3.12; pyproject dependency list empty; requirements.txt separately pins packages | Clean install/lock; immutable container digest |
| Custom CUDA dependency | AvencastF/torch-linear-assignment@7680e2c8ac1e8ab0d2eabd29fb4eb7b8fd8a2c8b | Apache-2.0 | EveNet Dockerfile clones default branch without pin |
| Model repo | Avencast/EveNet@afba5b47478f0c25c6a5a5755ac30738925d73ad | Model card declares MIT | Exact task-to-checkpoint mapping |
| Checkpoint candidate 1 | SSL.20M.last.ckpt, 220,658,079 bytes, SHA-256 e2ed50ca4f2c44fc1692c07c504ffdbad7d4a2c36a8d6206b6b3e2a7f5f148b2 | File commit 44bbaf06c548b143ca45e4c35e4598881632c6e3 | Local download/rehash; task mapping |
| Checkpoint candidate 2 | checkpoints.20M.a4.last.ckpt, 267,634,251 bytes, SHA-256 3c8b571328112988fd7186953a2f3155f0e22301a9c8d7e24f520881251a5ef2 | File commit 3969201ae20b5353ddb99c1810254ea7115217ed | Local download/rehash; task mapping; isolated pickle load |
| Pretraining dataset | Avencast/EveNet-Pretrain@200a96e9c9d7b3876398169760540f3189df0205 | Current card declares MIT; 541,248,429 rows, about 193 GB, 1,100 columns | Full shard inventory, source-data rights, schema/units, downstream evaluation split |
| One pretraining shard | data_Combined_Balanced_run_0.parquet, 201,065,223 bytes, SHA-256 b9dafebb5ab49b3ed491f050d8eeb9d46bc8aed8d82e046fe42af86c549148cb | File commit e6da3c120f3d74304beb2958aedaa8426fb92a11 | Local download/rehash; this is not a downstream test split |

The hash values above are immutable source-host/Xet/Git-LFS pointer metadata. No dataset or checkpoint bytes were downloaded, no local SHA-256 was recomputed and no independent byte-level hash verification occurred. The dataset's current MIT metadata replaced earlier fair-noncommercial-research-license metadata on 2026-03-30; this repository declaration does not independently resolve every upstream simulated-event/source-data right.

The upstream EveNet Dockerfile uses Python 3.12.3 and CUDA 12.4.1 on Ubuntu 22.04, but its custom torch-linear-assignment clone is not commit-pinned. The documentation points to docker.io/avencast1994/evenet:1.5, but no immutable image digest was verified. The paper's approximately 180 GB Parquet statement and the dataset card's approximately 193 GB must remain a discrepancy until reconciled with pinned files and explicit decimal/binary units.

The model card describes an event-level point-cloud/global-observable input (up to 18 reconstructed objects with seven per-object features) and reports downstream HEP tasks and metrics. Those metrics remain source-reported. Neither candidate checkpoint has been assigned to a particular downstream benchmark in this cycle. The pretraining shard cannot be used as a held-out downstream test set.

### Remaining Lane A blockers

1. Select one paper-defined downstream task and its exact model checkpoint/configuration.
2. Pin the downstream evaluation dataset revision and every train/validation/test shard; verify event/run/group disjointness.
3. Audit upstream event-data provenance and license terms separately from repository MIT metadata.
4. Pin torch-linear-assignment, the container image digest or a complete reproducible source build, and the resolved Python 3.12/CUDA/PyTorch environment.
5. Download in a controlled environment and recompute all hashes locally; verify Parquet schema, units and row counts.
6. Run one bounded inference task, retain raw outputs and failures, and compare the source-defined quality metric/acceptance threshold.
7. Only then compare CPU/GPU/NPU under identical accepted outputs and full accounting for RAM/VRAM, transfers, host work, latency, throughput, energy and total cost per accepted task.

No inference, model training, GPU/NPU benchmark, SDK validation, simulator run or QPU execution was performed. The asset-pin subgate is advanced, not closed.

## 3. Fresh literature delta

Published the dedicated 2026-10-30 literature watch. Material deltas:

- FND-001: Dago & Bellon, PRL 137, 147101 (2026-09-30), report feedback-shifted nonequilibrium erasure cost below the bath-temperature reference. The result requires full controller/information/resource accounting; it is not a universal Landauer violation.
- FND-001/FND-004: Sundelin et al., arXiv:2609.37149 (2026-09-29), report a quantum thermal-machine TUR ratio 1.71 ± 0.17 against the classical Q >= 2 bound at 81 mK. It remains a preprint; entropy-production boundary and matched classical control require scrutiny.
- FND-004 / D-G: Singh et al., PRA 113, 063735 (2026), arXiv:2602.09495, provide algebraic no-go certificates for specified heralded linear-optical state-generation tasks. Scope is the stated linear-optical assumptions, not all photonics.
- FND-006 / EQN-001–006: Cogentic (arXiv:2609.40324) reports multi-agent formal proof discovery; this is a workflow lead, not a physics result.
- INV-030 / D-G: HDSAI constitutive modeling (DOI 10.1002/nme.70387, first published 2026-07-22) offers a hierarchical symbolic search method. Its local convexity screen is not a global polyconvexity guarantee; no Pangola material is tested.
- INV-031: the 2026 systematic review/meta-analysis of 50 pyrolysis TEAs (DOI 10.1016/j.jaap.2026.107847) reports lower average minimum selling prices for primary pyrolysis liquids than upgraded fuels. It reinforces that crude liquid volume is not accepted finished fuel; no Pangola economics is established.
- Lane A/C: McArdle, Gilyén and Berta, PRL 136, 240603 (2026-06-18), describe function-amplitude state preparation without coherent arithmetic using a low-cost block encoding. Ancilla count alone is not a full resource advantage.

SymbolFit and LLM-PySR were rechecked but not duplicated because they are already indexed in the 2026-10-28 literature watches. No new FND-002 output-information bound, FND-003 matched QSL experiment, FND-005 QFT/particle mechanism, fusion plant result or UQPU financing result changed the existing gaps.

## 4. A–H status

| Lane | Current status this run | Next meaningful gate |
|---|---|---|
| A — Quantum programming/workloads/compiler/runtime | Advanced HEP-EVENET-003 by pinning code/model revisions, two checkpoint hashes and one pretraining shard hash at source. No local bytes or inference. | Pin one downstream task/config/split, close environment, reproduce accepted output. |
| B — Cloud/QPU/provider integration | Provider-neutral paths retained for IBM, Braket, Azure providers, IonQ, Rigetti, D-Wave, IQM, Quantinuum, Pasqal, QuEra, Quandela and OQC. No SDK/target execution or paid job. | Continue simulator/dry-run after a frozen workload contract. |
| C — RAM/VRAM/HBM/storage/state/data movement | 193 GB / 541M-row / 1,100-column dataset metadata informs a streaming/storage question only. No local RAM/VRAM/transfer measurement; Hilbert-space dimension is not classical storage. | Measure projected-column reads, peak memory, checkpoint I/O and transfer on a pinned bounded sample. |
| D — Device/chip/process/fabrication/packaging | Linear-optical no-go and HDSAI material-method literature added; no new chip/device/fabrication result. | Convert exact no-go assumptions and material constitutive constraints into device acceptance tests. |
| E — Biomass/materials/bio-oil/fusion/cooling/infrastructure | New pyrolysis TEA meta-analysis indexed; Batch 140 FUS-001 maintenance cost envelope retained. No Pangola-specific accepted fuel, material substitution or net fusion result. | Normalize study boundaries and test a measured Pangola mass/energy/upgrading case; reproduce FUS-001 separately. |
| F — Economics/benchmarks/evidence/energy economics/finance | Cost boundaries reinforced; no UQPU total cost, project principal, interest, WACC or hurdle-rate result measured. | Populate actual resource/cashflow ledger after a reproduced task; keep model-only estimates separate. |
| G — Quantum-chip manufacturing equipment/software/factory systems | D/G co-design retained; photonic no-go and constitutive-model constraints provide design filters, not manufacturing data. | Tie exact optical resource bounds and measured material/device lifetime to process/metrology requirements. |
| H — Ketskaew Chulamani/Kanusanan Pongpanna Model strategy, finance and publication | New source-specific watch and Batch 141 published; six-language master-plan context and strategic AI-agent/funding references preserved. | Publish independently reproduced evidence without converting strategic targets into facts. |

## 5. Foundational physics and equation-discovery status

| Workstream | This cycle |
|---|---|
| FND-001 thermodynamic-gap accounting | Advanced literature boundary: feedback/controller resources and quantum TUR assumptions; no project measurement. |
| FND-002 output-information lower bounds | No new lower bound; existing output-information accounting remains binding. |
| FND-003 matched control vs quantum-speed-limit measurement | No new matched experiment; existing matched-output contract remains open. |
| FND-004 alternative physical primitives | Added a scoped linear-optical no-go and a quantum-TUR experiment lead; no new device primitive validated. |
| FND-005 QFT/elementary-particle mechanism scans | No new mechanism or particle result. |
| FND-006 mathematics-first invention | Added formal proof-discovery workflow and hierarchical constitutive search as candidate methods; no new physical theorem/law. |
| EQN-001–006 | No equation promoted. All candidates still require units, symmetry, conservation, causality, limiting cases, held-out prediction, counterexample search, proof/simulation, discriminating experiment and independent replication. |

Current physical laws remain binding for present engineering claims. AI and symbolic systems may generate candidates, but neither proof discovery, fit quality nor a model's own physical-consistency screen declares a new law.

## 6. INV-029 through INV-035 and legacy moonshots

- INV-029: no Data-Center-to-One-Phone service, physical-compression, energy or lifecycle-cost gate passed.
- INV-030: no Pangola carbon functional substitution, critical-material reduction or transmutation.
- INV-031: no accepted Pangola-derived liquid fuel or commercial ultra-low-cost bio-oil result.
- INV-032: Batch 140's maintenance-aware accounting remains a cost-model contract; no reliable net delivered fusion electricity or commercial LCOE is demonstrated.
- INV-033: principal, absolute interest, internal hurdle rate, financial cost of capital and WACC remain separate; no UQPU reduction measured.
- INV-034: foundational mathematics/physics remains active and evidence-gated.
- INV-035: equation generation remains open-ended; no AI-generated equation is promoted to physical law.
- INV-025/026/027: 100,000,000-GPU and universal 100,000,000-unit GPU/CPU/NPU/RAM/VRAM/storage targets remain falsifiable goals. No Hilbert-space-to-readable-memory equivalence is claimed; NPU comparison requires real neural-workload semantics and full resource accounting.

## 7. Integration, GitHub sync and CI

- New Lane A asset manifest: HEP-EVENET-003.
- New literature watch: docs/literature_watch/2026-10-30-nonequilibrium-thermodynamics-and-equation-discovery.md.
- Focused gap RG-HEP-EVENET-PREFLIGHT-001 updated with exact source pins and remaining task/runtime blockers.
- integration/README.md and root README.md link the new batch, watch and asset manifest.
- Large append-only WORKLOG.md and RESEARCH_GAPS.md were not rewritten from partial snapshots. Their aggregate reconciliation remains explicit sync debt; the focused gap is the detailed current record.

Starting-head combined-status returned no status contexts; the available commit-workflow-run endpoint returned no PR-triggered workflow runs for the starting SHA. This does not prove CI passed or failed. Batch 140 recorded starting-head cold-start audit #1385 passed and core/invariant run #2105 in progress; those observations do not transfer to Batch 141. Exact-head CI for every new commit must be observed before declaring green.

PR #152 (Batch 138) remains draft/open and PR #153 remains open/unmerged; no claim of full historical branch/fork reconciliation is made.

No paid QPU job, cloud expenditure, fusion experiment, material test or external account credential was used.

## 8. Next highest-value gate

Close one complete EveNet downstream inference reproduction before expanding to a wider workload. Pin the exact task/config/checkpoint/test split and upstream rights; pin the custom CUDA dependency and image digest; create a clean Python 3.12/CUDA/PyTorch environment; download and independently rehash all assets; verify group/run disjointness; run one bounded prediction; compare the paper-defined metric and acceptance threshold; then capture peak RAM/VRAM, checkpoint/input/output I/O, host preprocessing/reconstruction, latency, throughput, retries, energy boundary and total cost per accepted useful analysis. Only after this gate should CPU/GPU/NPU comparisons proceed.

In parallel, reproduce the Dago–Bellon full-cycle feedback accounting and the Sundelin quantum-TUR measurement model on paper/simulation with explicit resource boundaries; no physical-law or technology claim is promoted without discriminating measurement and independent replication.
