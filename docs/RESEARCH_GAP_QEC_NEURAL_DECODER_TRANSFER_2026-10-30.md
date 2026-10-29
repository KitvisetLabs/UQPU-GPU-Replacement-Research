# Research gap QEC-TRANSFER-001 — modular neural decoder transfer and accepted-output cost

**Opened:** 2026-10-30  
**Primary owner:** Lane B — cloud/QPU/provider evidence integration  
**Co-owners:** Lane A — logical-output acceptance; Lane C — state/memory/data movement; Lane D — device/noise provenance; Lane F — matched benchmark/economics; Lane G — decoder hardware/process interface; Lane H — literature publication  
**Status:** SOURCE PINNED / DATA RETRIEVAL AND REPRODUCTION NOT RUN  
**Evidence class:** EXTERNAL PREPRINT + PUBLIC CODE/DATA REFERENCES / PROJECT CONTRACT ONLY  
**Related:** INV-001/002/004/007/010/019/022/024/025/026/027/029/034/035; FND-003; FIN-001  
**Literature watch:** docs/literature_watch/2026-10-30-modular-neural-qec-decoder-transfer.md  
**Lane contract:** research_lanes/B_cloud_qpu_provider_integration/MODULAR_NEURAL_DECODER_TRANSFER_CONTRACT_2026-10-30.md

## Objective

Determine whether the public modular graph-recurrent surface-code decoder can be reproduced and whether its reported cross-task/device portability survives group-disjoint evaluation while satisfying accepted logical-output quality, streaming latency, memory/I/O, energy and total-cost requirements. The target is a falsifiable decoder workload, not a claim that UQPU has already achieved quantum advantage.

## Source pins observed on 2026-10-30

- Paper: Lange et al., arXiv:2610.03869, submitted 2026-10-02: https://arxiv.org/abs/2610.03869
- Code: https://github.com/LangeMoritz/modular-gnn-rnn-decoder
- Upstream main head observed: afd6e170feb72f7bc99f4fd14cf1495c2731cf5c (2026-10-14)
- Declared code license: MIT.
- Upstream README states trained models and IBM data are CC-BY-4.0; Google source data is linked to DOI 10.5281/zenodo.13273331 and the model/IBM record to DOI 10.5281/zenodo.23335425.
- UQPU has not retrieved the datasets or models, verified asset bytes, run the dependency environment, or reproduced any result. External source commit identity is pinned in this record; the mutable source data assets still need independent SHA-256 verification.

## Work-item contract

- **ID / lane:** QEC-TRANSFER-001 / B, with A/C/D/F/G/H interfaces.
- **Objective:** reproduce a fixed upstream baseline and test generalization across device, noise regime, code patch and logical operation.
- **Input:** pinned source tree, requirements, model checkpoints, Google/IBM syndrome records, detector-error models, circuit/label definitions and exact acquisition/license provenance.
- **Accepted output:** correctly decoded logical observable under the source's experiment-specific label definition, evaluated on a frozen test shot set. Memory, X-stability and ZZ-merge outputs are distinct tasks and cannot be pooled into one accuracy number.
- **Evidence level:** literature-only until assets are verified; then MODEL_ONLY/SOFTWARE_REPRODUCTION for reproduced code/data results; DEVICE_DATA_REANALYSIS for source hardware records. None of these levels by itself establishes new physical law or UQPU real-QPU advantage.
- **Cost boundary:** include training and fine-tuning, validation, inference, CPU/GPU wall time, peak RAM/VRAM, checkpoint and syndrome bytes, transfer, retries, energy when measurable, and amortization policy for training cost. Report cost per accepted logical correction on one declared price basis.
- **Dependencies:** source and data license verification; fixed environment; independent MWPM run using the same shots and detector-error model; test split certificate; exact metric definitions.
- **Status:** READY_FOR_REPRODUCTION_PREFLIGHT; not reproduced.
- **Blocker / unlock:** data/model bytes and hashes, dependency environment and published-result reproduction are not yet verified. Unlock by completing Gate 0 below.
- **Next action:** retrieve and hash the source assets, preserve original upstream results, and run baseline evaluation before any adaptation.
- **Artifacts:** this gap, the Lane B contract, literature watch, daily integration report and machine-readable integration record.

## Gate 0 — provenance and environment

1. Fetch the exact upstream commit above, record the tree SHA and confirm the checkout matches it.
2. Retrieve the Zenodo assets from the links in the upstream README; record record/version identifiers, filenames, byte lengths, SHA-256, license and retrieval timestamp.
3. Verify checkpoint hashes using the upstream download procedure; do not substitute a newer model or calibration.
4. Resolve requirements in an isolated environment. Record Python, CPU/GPU model, accelerator runtime, dependency lock and all warnings. Training requires CUDA according to the source README; evaluation of released models is stated to work on CPU.
5. Preserve the source's published commands and result files before making local changes.

**Gate 0 fails** if source/data provenance is unavailable, the model or dataset cannot be legally used, hashes do not match, or the pinned environment cannot be reconstructed. Do not silently replace the asset.

## Gate 1 — exact reproduction

- Reproduce logical error rates for each published IBM and Google experiment using the released model and the same test shots.
- Run MWPM on exactly the same shots with the source's calibrated detector-error model. Keep source-reported AlphaQubit comparisons distinct unless the exact same records and evaluation definition are available.
- Verify labels for memory, X-stability and ZZ merge, including the parity/correlation acceptance rule for lattice surgery.
- Report shot counts, missing/censored records, exact integer error counts, uncertainty intervals, all retries and failed runs.
- A mismatch beyond a preregistered tolerance triggers a discrepancy report; do not tune against the test set to force agreement.

## Gate 2 — generalization and operational acceptance

After Gate 1 passes, preregister group-disjoint splits with whole device/patch groups, operation types and noise/measurement regimes held out. The source's 80/10/10 random-permutation split (seed 42) is preserved for reproducing its results but is not sufficient alone for a transfer claim.

Measure:
- logical error rate and uncertainty for each distinct task;
- accepted logical outputs per second and cost per accepted logical correction;
- p50, p95 and p99 latency under a frozen batch/streaming policy;
- sustained throughput against the target syndrome cadence;
- CPU/GPU time, model parameters/checkpoint bytes, peak RAM/VRAM, syndrome/input/output bytes and host-device transfer;
- energy only when measured at a stated boundary;
- training/fine-tuning cost, retries, storage and engineering amortization assumptions.

The upstream paper explicitly reports no latency or throughput benchmarks. Constant per-round algorithmic cost does not prove real-time performance.

## Falsifiers and stop rules

Reject a portability or utility claim if any of the following holds:

- exact upstream results cannot be reproduced from pinned assets;
- MWPM is not evaluated on identical shots and detector-error information;
- a gain vanishes on preregistered held-out devices, operations or noise regimes;
- task labels or test records leak into training/selection;
- p95 latency or sustained throughput fails the declared cadence;
- memory, transfer, training, energy or retry cost erases the accuracy gain;
- uncertainty intervals do not support the declared improvement;
- results depend on an unrecorded calibration or asset change.

## Cross-lane integration and non-claims

- A: treat logical memory, stability and lattice surgery as separate useful-output contracts.
- B: preserve provider/target and raw-data provenance; public records first, no live QPU job needed.
- C: record classical bytes and data movement; never equate qubits or Hilbert-space dimension with readable storage.
- D/G: convert decoder timing/memory/power requirements into future device/control-electronics constraints only after measurement.
- E: no new BIO-001, Pangola-carbon or FUS-001 evidence is produced by this task.
- F: use identical cost basis and accepted-output denominators; no mixed-provider pricing.
- H: preserve source attribution and the Thai/English/Chinese/Japanese/Korean/German master-plan links.
- INV-029: this is only a software/hardware subsystem workload; remote QPUs, servers, controllers, cooling, networking and power remain external dependencies and must be counted.
- INV-030–033: no material, saleable-fuel, net-electricity or financing-rate result is established.
- INV-034/035: no new physical law is proposed. AI/software methods remain hypotheses and tools subject to falsification and independent validation.

No paid QPU job is required or authorized for this gap.

## Related evidence delta — accuracy/latency/quantization co-design (2026-10-30)

A fresh public-source review found Yan, Li and Du, “Rethink the Role of Neural Decoders in Quantum Error Correction,” https://arxiv.org/abs/2605.12046 (submitted 2026-05-12). The paper reports surface-code neural-decoder studies through distance 9 and a Vitis HLS-synthesized TCN configuration at 271 cycles, approximately 0.77 microseconds at 350 MHz, on a Versal VP1902. It argues for hardware-aware QAT/INT4 under its own test conditions. This is an external source-reported result, not a UQPU reproduction, and is not numerically pooled with the separate modular GNN-RNN decoder paper.

### Additional falsification gate for streaming targets

- Reproduce the paper-specific baseline, source revision, model and data first; retain hashes and licenses.
- Measure per-shot p50/p95/p99 latency separately from throughput, against the actual target controller deadline.
- Compare precision/QAT arms under equal budgets; reject INT4 if accepted logical-output quality fails the predeclared threshold or uncertainty criterion.
- Preserve the paper's source-specific task, data, noise model and code distance. Use group-disjoint device/patch/noise holdouts for transfer claims.
- Separate analytical resource estimates, HLS synthesis, board timing closure and full end-to-end feedback latency. Include buffering, memory/I/O, energy where measured and cost per accepted logical correction.

**Status remains:** SOURCE PINNED / DATA RETRIEVAL AND REPRODUCTION NOT RUN. This comparator does not remove Gate 0 or establish UQPU performance, quantum advantage or a physical law.
