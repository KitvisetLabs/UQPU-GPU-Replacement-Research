# Lane B contract — modular neural QEC decoder transfer

**Date:** 2026-10-30  
**Primary owner:** Lane B — cloud/QPU/provider integration  
**Evidence owner:** Lane F  
**Workload owner:** Lane A  
**Cross-lane interfaces:** C syndrome/state bytes; D device and noise provenance; G decoder hardware/process constraints; H publication; INV-034/035  
**Status:** READY_FOR_REPRODUCTION_PREFLIGHT / NOT REPRODUCED  
**Work item:** QEC-TRANSFER-001  
**Canonical gap:** docs/RESEARCH_GAP_QEC_NEURAL_DECODER_TRANSFER_2026-10-30.md

## Source identity

Paper: Lange et al., “Modular Neural Decoder for Surface Code Memory and Logic on Superconducting Processors,” arXiv:2610.03869, submitted 2026-10-02.

Code repository: https://github.com/LangeMoritz/modular-gnn-rnn-decoder  
Pinned observed upstream commit: afd6e170feb72f7bc99f4fd14cf1495c2731cf5c  
Declared licenses: MIT code; CC-BY-4.0 trained models and IBM data.  
Data leads: Zenodo DOI 10.5281/zenodo.13273331 (Google data) and DOI 10.5281/zenodo.23335425 (models/IBM data), as linked by the upstream README.

The external repository is not yet imported into UQPU. No source assets or model/data bytes have been verified locally.

## Required interfaces

### Input contract

A frozen shot record must identify source/version/hash, device and patch, code distance, operation (memory, stability or merge), syndrome record, detector-error model, experiment-specific logical label, training/validation/test group, and any acquisition/calibration metadata. Keep raw shot identifiers and group membership so split disjointness can be independently checked.

### Output contract

Return a predicted logical observable or task-defined parity plus an explicit abstention/error state where input or model provenance is invalid. Evaluation must retain exact integer error counts and shot denominators. Do not pool memory error rates, stability success and lattice-surgery correlation as if they were one metric.

### Baselines

1. Reproduce the released neural decoder with the pinned model and published split.
2. Run MWPM using the same shots and detector-error model.
3. Keep any AlphaQubit comparison source-attributed unless the same data and scoring contract are available.
4. After reproduction, add group-disjoint holdouts for device/patch, operation and noise regime. Do not treat a random shot split as a portability certificate.

### Resource/cost record

For every arm record source revision, environment hashes, model/checkpoint bytes, training/fine-tuning cost, CPU/GPU time, peak RAM/VRAM, syndrome and output bytes, host-device transfer, latency p50/p95/p99, sustained throughput, retry/failure count, energy if measured, and cost per accepted logical correction. Use one declared cost basis and amortization policy. Record absent measurements as NOT_MEASURED, not zero.

### Acceptance and falsification

Acceptance requires exact baseline reproduction, independent metric verification, a preregistered test manifest, correct labels, matched shots and MWPM inputs, confidence intervals, no split leakage, and target-specific latency/throughput measurements before any real-time claim.

Reject transfer if gains vanish on held-out groups, if the target cadence is missed, if uncertainty fails the predeclared criterion, or if full resource/cost accounting erases the useful-output improvement.

## Execution boundary

Use public data and local evaluation first. No provider calls or QPU submissions are needed. Paid hardware execution remains forbidden without credentials, bounded budget and explicit user consent.

## Related source-specific latency comparator — 2026-10-30

A separate external preprint, Yan, Li and Du, “Rethink the Role of Neural Decoders in Quantum Error Correction” (https://arxiv.org/abs/2605.12046), reports accuracy/latency co-design through surface-code distance 9 and a Vitis HLS-synthesized TCN result of 271 cycles (~0.77 microseconds at 350 MHz) on a Versal VP1902. UQPU has not reproduced this result. This is a separate source arm and must not be merged numerically with the modular GNN-RNN paper's metrics or data.

For any streaming/active-feedback target, add these acceptance requirements after reproducing the source baseline:

1. Record per-shot latency p50/p95/p99 and sustained throughput separately; an average throughput number cannot certify an immediate feedback deadline.
2. State the actual target controller cycle and timing path. The source's approximately 1-microsecond superconducting-cycle premise is not universal across providers or modalities.
3. Compare source-published precision/QAT with feasible precision alternatives under equal training/inference budgets. INT4/QAT passes only if the held-out logical-error criterion remains satisfied with uncertainty reported.
4. Distinguish analytical FPGA resource estimates, HLS synthesis, board-level timing closure and end-to-end deployed latency. Record model/checkpoint bytes, syndrome buffering, memory, transfers, energy when measured and total cost per accepted correction.
5. Preserve separate source/data/model identities and group-disjoint device/patch/noise holdouts. Do not combine source-reported probability with another target's pricing.

**Evidence boundary:** this addition refines the test contract only. It does not establish a UQPU decoder result, a general real-time guarantee, or a quantum advantage.
