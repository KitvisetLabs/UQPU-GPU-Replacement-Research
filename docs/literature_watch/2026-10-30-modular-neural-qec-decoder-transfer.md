# Literature watch — 2026-10-30: modular neural decoder transfer across QEC tasks

**Checked:** 2026-10-30  
**Primary owner:** Lane H — literature surveillance and publication  
**Implementation owner:** Lane B — provider/hardware evidence integration; Lane A owns workload and output acceptance  
**Cross-lane interfaces:** C decoder memory and syndrome I/O; D device/noise provenance; F matched quality, latency, energy and cost; G decoder-accelerator/process constraints; INV-034/035  
**Evidence class:** OFFICIAL ARXIV PREPRINT + PUBLIC SOURCE CODE/DATA REFERENCES; NOT REPRODUCED BY UQPU  
**Work item:** QEC-TRANSFER-001  
**Focused gap:** docs/RESEARCH_GAP_QEC_NEURAL_DECODER_TRANSFER_2026-10-30.md

## Source and provenance

Moritz Lange, Ole Fjeldså, Gustaf Jonasson Johansson and Mats Granath, “Modular Neural Decoder for Surface Code Memory and Logic on Superconducting Processors,” arXiv:2610.03869, submitted 2026-10-02; manuscript dated 2026-10-07: https://arxiv.org/abs/2610.03869.

The authors publish code, trained models and reproduction instructions at https://github.com/LangeMoritz/modular-gnn-rnn-decoder. The upstream repository head observed for this watch is afd6e170feb72f7bc99f4fd14cf1495c2731cf5c (2026-10-14). The code repository declares MIT for code and CC-BY-4.0 for trained models and IBM data. Its README points to the Google public-data record DOI 10.5281/zenodo.13273331 and a Zenodo record DOI 10.5281/zenodo.23335425 for models and IBM data. These source assets have not been downloaded or hash-verified by UQPU.

## Genuine methodological delta

The paper describes a modular graph-neural-network/recurrent decoder. A shared local encoder processes small space-time windows of surface-code detection events; spatial tiling and aggregation adapt the same base representation to larger patches and a two-patch ZZ merge, while a recurrent component processes time. The authors report results for:

- IBM superconducting hardware memory data at code distances 3 and 5, where the fine-tuned decoder outperforms minimum-weight perfect matching (MWPM) in the reported comparisons;
- public Google below-threshold hardware data for Z-basis memory, where the reported logical-error rates approach those of AlphaQubit;
- an X-type stability experiment across 17 duration/measurement-rotation settings using a jointly fine-tuned decoder;
- an IBM distance-3 ZZ lattice-surgery merge, where the authors report improved decoded parity correlation relative to MWPM.

This is a useful portability signal because the work extends beyond a single memory task to stability and a logical-operation primitive. It is not evidence that one fixed set of weights works zero-shot everywhere: the paper describes staged pretraining and hardware/experiment-specific fine-tuning, with labels and small aggregation modules adapted to the task.

## Important limitations

1. The results are source-reported preprint results. UQPU has not rerun the public code, regenerated the data, checked the raw hardware records, or independently reproduced the reported error rates.
2. The authors explicitly report no latency or throughput benchmarks. A constant per-round operation count is compatible with real-time operation but does not establish it. A decoder must keep pace with the target system's syndrome cadence under a declared end-to-end boundary.
3. IBM results stop at distance 5 in the paper; the authors attribute the limitation to available patch quality/size. The Google results discussed in the paper cover the Z basis, not every basis or hardware regime.
4. The source README describes an 80/10/10 split of recorded data using a fixed random permutation (seed 42). Such a split is useful for reproducing its stated test set, but it does not alone establish generalization to an unseen device, patch, noise regime, or logical operation. UQPU must add group-disjoint transfer tests.
5. The models were trained on one NVIDIA GH200 GPU, with training ranging from GPU-hours to GPU-days for the largest simulated models. That is a source-reported resource description, not a measured UQPU cost result or a proof of low-latency deployment.
6. The paper does not establish lower total lifecycle cost per accepted logical operation, lower wall-plug energy, universal decoder portability, or an advantage over every classical baseline.

## Exact UQPU relevance

- **A — workloads/runtime:** a concrete accepted-output workload for logical memory, stability and lattice-surgery parity. Compare accepted logical outcomes, not circuit execution success alone.
- **B — cloud/QPU integration:** preserve device, target, calibration, acquisition, shot and pricing provenance. Public hardware data is the first reproduction route; no live provider job is needed.
- **C — state/memory/I/O:** record syndrome bytes, input windowing, output labels, model/checkpoint bytes, host transfers, peak RAM/VRAM and any batching/reconstruction. Qubit count is not a substitute for readable classical memory or decoder state bytes.
- **D/G — device and manufacturing co-design:** decoder cadence, memory footprint, precision, accelerator area/power and interface bandwidth are candidate constraints for future control electronics. No chip or factory advantage is established.
- **E — materials/energy:** this result does not alter BIO-001, INV-030, FUS-001 or net-electricity evidence. Only a later measured deployment-energy boundary could inform infrastructure economics.
- **F — evidence/economics:** include training, validation, inference, hardware/host resources, data movement, energy when measurable, retries and cost per accepted logical output.
- **H — strategic publication:** record a reproducible gate rather than treating an external paper as UQPU evidence.

The result is a systems/decoding method, not a new physical law. It contributes no direct evidence for INV-029 physical compression, Pangola-carbon substitution, commercial bio-oil, commercial fusion, or reduced WACC. INV-034/035 remain binding: no equation or physical claim is promoted from this literature watch.

## Proposed falsifiable follow-up

1. Pin the upstream source commit, record dependency and model versions, retrieve the named public datasets, verify license compatibility and calculate SHA-256 for every downloaded asset.
2. Run the published evaluation commands first, without changing source, and compare the released-model logical error rate with MWPM on the identical held-out shots and calibrated detector-error model. Preserve the authors' original split for reproduction only.
3. Add preregistered group-disjoint tests: hold out entire device/patch groups, operation types and noise/measurement regimes. Keep training, validation and final test labels disjoint; do not tune on the final test.
4. Report binomial uncertainty for logical error rate, task-specific parity/correlation metrics, all failures and missing shots, plus CPU/GPU training and inference time, peak memory, checkpoint size, syndrome bytes, throughput, p50/p95/p99 latency, energy if measured, and total cost per accepted logical correction.
5. Test streaming throughput against an explicitly declared target cadence. The source paper does not provide this latency gate.
6. Stop any portability/utility claim if the source results cannot be reproduced, the gain disappears on held-out groups, the comparison uses different shots or decoder information, or the decoder cannot meet cadence within the declared resource/cost boundary.

No paid QPU execution is needed or authorized for this gate. A future hardware job would require separate credentials, a bounded budget and explicit user consent.