# Literature watch — neural QEC decoder accuracy, latency and quantization co-design

**Date reviewed:** 2026-10-30  
**Primary source:** Ge Yan, Shanchuan Li and Yuxuan Du, “Rethink the Role of Neural Decoders in Quantum Error Correction,” arXiv:2605.12046 (submitted 2026-05-12).  
**Official source:** https://arxiv.org/abs/2605.12046  
**Evidence class:** EXTERNAL PREPRINT WITH PAPER-REPORTED SIMULATION AND HLS SYNTHESIS; NOT REPRODUCED BY UQPU  
**Primary owner:** Lane B — QPU/provider integration; interfaces A/C/D/F/G/H  
**Related work item:** QEC-TRANSFER-001  
**Related UQPU source watch:** https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/blob/main/docs/literature_watch/2026-10-30-modular-neural-qec-decoder-transfer.md

## Why this source matters

This paper studies the decoder as a real-time control-path component, not just a classifier. It compares five neural architecture families for rotated surface-code decoding through distance 9, then combines pruning and quantization-aware training (QAT) with FPGA resource analysis. The paper reports that training-data scale and topology-aligned inductive bias matter, and that INT4/QAT is important for meeting microsecond-scale latency in its tested FPGA setting.

One concrete source-reported result is a distance-9 temporal-convolutional decoder synthesized with Vitis HLS for a Versal VP1902: 271 clock cycles, reported as about 0.77 microseconds at 350 MHz under the paper's incremental streaming setup. This is a result reported by the paper, not a UQPU measurement. The paper also uses a conservative analytical resource model and distinguishes estimates from its HLS synthesis check; its target, clock, model and data are not interchangeable with the separate modular graph-recurrent decoder in QEC-TRANSFER-001.

## Limitations and evidence boundary

- The official arXiv HTML was reviewed; UQPU has not independently rebuilt the environment, retrieved and hashed every data/model asset, or reproduced the reported logical-error and HLS results.
- The results are specific to the paper's surface-code experiments, data, noise assumptions, architectures and FPGA targets. The roughly 1-microsecond cycle premise is not universal across all QPU modalities or providers.
- A reported synthesized latency is not the same as end-to-end deployed controller latency, including acquisition, buffering, transport, scheduling, retries and feedback.
- Quantization may reduce model size and latency while changing logical-error rates. INT4 is not an automatic win; it must pass a predeclared quality/non-inferiority test on held-out groups.
- This paper does not demonstrate quantum advantage, a new physical law, or any UQPU improvement.

## Exact UQPU relevance

- **Lane A:** make accepted logical output and per-shot deadline explicit; throughput alone is insufficient for streaming feedback.
- **Lane B:** keep this source as a separate decoder arm. Do not pool its results with the modular GNN-RNN paper or mix data, probabilities, latency and cost across targets.
- **Lane C:** record checkpoint size, syndrome-buffer bytes, on-chip memory use and host/device transfers.
- **Lanes D/G:** co-design model precision, FPGA/accelerator resource limits, clock target and process/device implementation. HLS synthesis is a useful gate, not a substitute for board-level timing closure and end-to-end tests.
- **Lane F:** report logical-error rate and confidence intervals alongside p50/p95/p99 per-shot latency, sustained throughput, energy where measured and total cost per accepted logical correction.
- **Lane H:** retain the method as a reproducible research lead, not a funding or commercialization claim.
- **INV-034/035:** this is a systems/algorithm co-design result, not evidence for alternative physical primitives or a new equation.

## Falsifiable follow-up

After Gate 0 provenance and environment checks for QEC-TRANSFER-001, run separate, source-pinned decoder arms on the same frozen shots and detector-error model. For the latency-oriented paper, reproduce its published split first, then evaluate group-disjoint device/patch/noise holdouts. Compare the published precision/QAT configuration with feasible higher-precision and INT4/QAT arms under equal training and inference budgets. Preserve exact logical-error counts and denominators.

Acceptance requires: (1) independently reproduced baseline metrics within predeclared tolerance; (2) quality meeting the task's declared logical-error threshold with confidence intervals; (3) per-shot p95/p99 latency below the actual target controller deadline, not merely high average throughput; (4) no group leakage; and (5) full memory, transfer, energy-if-measured and cost accounting. Failure on any gate remains a retained negative result.

No new physical equation or project capability is promoted by this watch.
