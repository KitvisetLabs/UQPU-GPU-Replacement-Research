# Research gap RG-HEP-EVENET-TRANSFER-001 — event-level foundation-model reproduction and resource closure

**Opened:** 2026-10-30  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Co-owners:** B provider/data provenance; C memory and data movement; D/G device and manufacturing; E energy/materials boundary; F benchmark/economics; H publication  
**Status:** OPEN / LITERATURE_ONLY / ASSET RETRIEVAL AND REPRODUCTION NOT RUN  
**Work item:** HEP-EVENET-001  
**Source watch:** docs/literature_watch/2026-10-30-evenet-particle-collision-foundation-model.md  
**Lane contract:** research_lanes/A_quantum_programming_runtime/EVENET_HEP_FOUNDATION_MODEL_WORKLOAD_CONTRACT_2026-10-30.md

## Objective

Determine whether one bounded downstream task from the published EVENET particle-collision foundation model can be independently reproduced and whether its quality, transfer, memory, latency, energy and total cost survive matched comparison with competitive classical baselines. Keep this as a candidate scientific-ML workload; do not presume the full foundation model is suitable for quantum execution.

## Source pins observed on 2026-10-30

- Version of record: Hsu et al., *Nature Machine Intelligence*, published 2026-10-29, DOI 10.1038/s42256-026-01322-9.
- Preprint: arXiv:2601.17126.
- Public code: EveNet-HEP/EveNet-Full, main commit 06c3181d9a0f7df3e30edbb1c355b6fec8b5a3ad (observed via GitHub connector).
- The code repository's LICENSE declares MIT for that code. Its README points to pretrained weights at Avencast/EveNet on Hugging Face. The model checkpoint, dataset, supplementary material and asset licenses have not yet been independently retrieved, hashed or reconciled with the version of record.
- The version of record reports about 500 million pretraining events, about 100,000 GPU-hours on 512 NVIDIA A100 GPUs, and about 4 TB raw simulation converted to about 180 GB Parquet. The GPU-hour figure excludes event generation and preprocessing.

## Current evidence and limitations

The source reports multi-task performance on heavy-resonance searches, exotic-Higgs analysis, dileptonic top-pair quantum-correlation observables and CMS Open Data Υ rediscovery. These are external paper results, not UQPU measurements.

The reported pretraining resource figure is not a full lifecycle cost. Energy, peak accelerator memory, full data-generation/preprocessing cost, model/checkpoint byte sizes, inference latency distributions, sustained throughput, total transfer and cost per accepted analysis remain unclosed. The article also identifies remaining work in explicit detector/theoretical uncertainty propagation, cross-head consistency and stress tests under substantial simulation-data mismatch.

The arXiv manuscript and version of record must be reconciled before exact reproduction. The preprint describes a generated/selected event pipeline in addition to the final retained pretraining corpus; source-version differences must be recorded, not silently merged.

## Blockers

1. Exact paper, code, model-checkpoint and data revisions must be frozen and SHA-256 hashed.
2. Code MIT licensing does not automatically establish the license or provenance of checkpoints, CMS-derived datasets, simulated events or third-party assets.
3. The 500-million-event / 100,000-GPU-hour pretraining run is too large to treat as an assumed first reproduction. Begin with one bounded downstream task using a verified released checkpoint.
4. Source-specific task definitions, cuts, event weights, split IDs, systematic variations, control channels and statistical uncertainty procedures must be reconstructed exactly.
5. No UQPU measurement yet exists for energy, peak RAM/VRAM, I/O, transfer, inference latency, throughput, retries or total cost per accepted useful analysis.
6. No discrete QPU subproblem, provider-neutral lowering or quantum advantage has been established.

## Unlock protocol

### Gate 0 — provenance and licensing

- Pin the Nature version of record, arXiv version, upstream code commit, dependency lock, model checkpoint revision, dataset record IDs and licenses.
- Retrieve all public assets through their official links; record filename, byte count, retrieval date, source revision, license and SHA-256.
- Confirm that the MIT code license does not get incorrectly applied to model weights or data.

### Gate 1 — one-task reproduction

- Select one bounded downstream task and reproduce the published checkpoint evaluation before changing architecture, labels, cuts or metrics.
- Keep the source's train/validation/test event IDs and controls fixed for reproduction.
- Re-run the corresponding source baseline on identical events and event weights.
- Preserve raw predictions, uncertainty estimates, failed runs and all metric denominators.

### Gate 2 — generalization and physics controls

- Add group-disjoint holdouts by mass point, process, detector condition, data-taking period and systematic variation.
- For Υ rediscovery, retain opposite-sign and same-sign controls, sideband definitions and independent pseudo-experiments.
- For quantum-correlation outputs, freeze observable definitions and propagate statistical and detector/theory uncertainties separately.
- Test kinematic closure, object assignment, calibration, systematic robustness and false-positive behavior.

### Gate 3 — resource and economics closure

- Measure event generation, filtering, preprocessing, pretraining amortization, fine-tuning, inference, CPU/host work, GPU/NPU hours, peak RAM/VRAM, checkpoint/event bytes, transfer, p50/p95/p99 latency, throughput, energy if measurable, retries and reconstruction.
- Declare the number of accepted analyses that share pretraining cost. Keep shared and task-specific cost separate.
- Compare cost per accepted useful output under the same dated price basis and equivalent quality.

### Gate 4 — optional quantum subproblem

- Do not attempt to port the full foundation model by analogy.
- Identify a mathematically justified discrete subproblem, then define identical output, reference/bound certificate, classical baseline, provider-neutral lowering, independent SDK check and target-aware simulation.
- No paid hardware job without credentials, bounded budget and explicit consent.

## Falsifiers and stop rules

The transfer/utility hypothesis fails for the selected task if the source result cannot be reproduced, group-disjoint performance collapses, control samples develop spurious signal, uncertainty/calibration is inadequate, the model misses the required task cadence, or complete cost per accepted output exceeds the matched baseline without a compensating accepted capability.

A failure to find a defensible QPU mapping is a valid result; do not force a quantum implementation.

## Cross-lane consequences

- **A:** a task-specific accepted-output workload enters the baseline catalogue; the exact QUBO/QAOA and CPU/GPU/NPU path remains the higher-priority computing gate.
- **B:** source/model/data provenance first; no provider job.
- **C:** particle/event/checkpoint bytes and memory/transfer measurements; no Hilbert-space/readable-memory equivalence.
- **D/G:** only measured precision, memory bandwidth, clock, power, area and process constraints can inform device/factory design.
- **E:** no change to Pangola carbon, BIO-001 or FUS-001 evidence.
- **F:** complete cost per accepted analysis and explicit pretraining amortization.
- **H:** a reproducible source-specific research path, not a funding or commercialization claim.

No paid QPU job is required or authorized for this gap.
