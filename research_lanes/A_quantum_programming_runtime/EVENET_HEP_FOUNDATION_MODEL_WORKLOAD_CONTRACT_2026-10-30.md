# Lane A workload contract — HEP-EVENET-001

**Date:** 2026-10-30  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Evidence/accounting owner:** Lane F  
**Publication/strategic owner:** Lane H  
**Cross-lane interfaces:** B provider portability; C state/data; D/G device and manufacturing; E materials/energy; F economics; H strategy; FND-005/006; EQN-001–006  
**Status:** LITERATURE_ONLY / BENCHMARK CONTRACT / SOURCE ASSETS NOT YET VERIFIED  
**Source watch:** ../../docs/literature_watch/2026-10-30-evenet-particle-collision-foundation-model.md  
**Focused gap:** ../../docs/RESEARCH_GAP_EVENET_HEP_FOUNDATION_MODEL_TRANSFER_2026-10-30.md

## Objective

Define a reproducible, task-specific scientific-ML workload for comparing conventional CPU/GPU/NPU execution and, only where mathematically justified, a future quantum subroutine. The contract is based on the published EVENET particle-collision foundation-model study. It is not a claim that the full model is quantum-compatible or that UQPU has reproduced the paper.

## Workload semantics

- **Input:** variable-length, unordered particle clouds representing collider events, including reconstructed object types and kinematic/identification features; event-level quantities and missing transverse momentum where specified by the task.
- **Shared model:** point–edge transformer representation with task-specific heads. The published architecture includes classification, resonance/object assignment, segmentation and diffusion-based reconstruction.
- **Output rule:** every downstream analysis is a separate accepted-output contract. Do not pool SIC, local significance, quantum-correlation observables and reconstruction loss into one score.
- **Physics rule:** preserve the source's object definitions, cuts, collision energy, detector/data provenance, event weights, labels, systematic variations and control samples. Reconstructed outputs must satisfy the source-defined kinematic and conservation checks.

## Task-specific acceptance matrix

| Task | Accepted useful output | Primary metric / control | Required holdout |
|---|---|---|---|
| Heavy-resonance X → YH mass grid | Correctly ranked signal/background events for each declared mass point | Signal-improvement characteristic (SIC), with the source's minimum expected-background requirement; XGBoost and TabPFN controls | Entire mass points, process groups and detector/systematic conditions |
| Exotic Higgs H → aa → 4b | Correct event classification plus source-defined assignment/segmentation outputs | SIC and separate assignment/segmentation metrics; Scratch and SPANet controls | Event groups, signal/background samples and systematic variations |
| Dileptonic top-pair quantum correlations | Source-defined correlation observables with uncertainty and calibration | Observable bias/variance and systematic-response checks against the source's reference analysis | Independent event groups and detector/systematic regimes |
| CMS Open Data Υ rediscovery | Reproducible known-resonance excess under the frozen analysis | Median local significance with pseudo-experiment uncertainty; opposite-sign signal and same-sign controls | Independent data partitions, sidebands and control-channel checks |
| Masked/invisible-object reconstruction | Correctly reconstructed object/event quantities | Source-defined reconstruction loss plus four-momentum/kinematic closure and uncertainty | Event topology, missing-object regime and detector conditions |

The table is a contract map, not a claim that UQPU has run any task. The exact quantum-correlation observable definitions, model checkpoints, data and supplementary procedures must be frozen from the source before Gate 1.

## Source-reported resource envelope (not UQPU measurements)

- Pretraining corpus: approximately 500 million simulated events.
- Version-of-record training report: approximately 100,000 GPU-hours on 512 NVIDIA A100 GPUs.
- Raw simulation to preprocessed Parquet: approximately 4 TB to 180 GB in the paper's pipeline.
- Downstream fine-tuning: a few to tens of GPU-hours per task, as reported by the authors.
- The stated pretraining GPU-hour figure excludes event generation and preprocessing. The complete resource boundary is therefore not yet closed.
- Public code: EveNet-HEP/EveNet-Full at upstream commit 06c3181d9a0f7df3e30edbb1c355b6fec8b5a3ad; code repository declares MIT. Checkpoint and dataset licenses/hashes remain unverified.

Do not infer wall-plug energy, cost, peak memory, inference latency or throughput from GPU-hour counts.

## Matched baseline contract

For each task, freeze the dataset, event IDs, train/validation/test split, model/checkpoint, precision, preprocessing, target, software/driver/runtime, correctness evaluator and timing boundary. Compare:

1. Released pretrained model, after exact provenance verification.
2. Self-supervised-only and scratch ablations, where available.
3. The source's task-specific classical baselines (for example XGBoost, TabPFN or SPANet only where the source comparison is valid).
4. A competitive CPU/GPU/NPU implementation using the same accepted-output definition.
5. A quantum candidate only for a separately specified subproblem with an exact small-instance reference and a defensible algorithmic mapping.

NPU acceptance requires actual neural-workload semantics, quality, precision, latency, throughput, memory/data movement and cost. TOPS alone is insufficient. Do not equate qubit count or Hilbert-space dimension with readable classical event storage.

## Complete cost and resource accounting

Separate shared pretraining costs from task-specific costs:

- Shared: event generation used across tasks, shared preprocessing, pretraining, validation, checkpoint storage and checkpoint transfer.
- Task-specific: task dataset generation, filtering/preprocessing, fine-tuning, inference, CPU/host work, accelerator work, memory, transfers, retries, reconstruction and evaluation.
- Measure wall time, accelerator model/count/hours, CPU hours, peak RAM/VRAM, checkpoint bytes, event bytes, I/O/transfer, p50/p95/p99 latency, sustained throughput, energy and peak power where measurable.
- State the actual number of accepted downstream analyses over which shared pretraining is amortized. Never assume an unlimited reuse count.

A bookkeeping form is:

C_task = C_shared / N_accepted_reuses + C_task_specific

where C_shared contains only costs genuinely shared across the declared analyses, and C_task_specific contains all costs attributable to that task. Price inputs must use one dated, target-specific basis. No external GPU-hour price may be combined with unrelated provider probabilities or QPU prices.

## Quantum execution gate

The full transformer/foundation-model training path is not presumed to be a QPU workload. A quantum arm is considered only after identifying a discrete or otherwise suitable subproblem, defining identical useful outputs, obtaining a reference/bound certificate, beating or matching competitive classical baselines under declared quality, lowering provider-neutrally, checking independent SDK semantics, and running target-aware simulation. Paid QPU execution requires credentials, a bounded budget and explicit owner consent. Execution success alone is not quality acceptance.

## Acceptance, rejection and stop rules

**Gate 0:** pin code, model, dataset, license, environment, versions and hashes.  
**Gate 1:** reproduce one bounded task and its source-defined baseline before adapting the model.  
**Gate 2:** pass group-disjoint generalization, uncertainty, systematic and control-channel checks.  
**Gate 3:** close memory, data movement, latency, throughput, energy-if-measurable and total cost per accepted task.  
**Gate 4:** only then consider a separately justified QPU subroutine.

Reject or retain as a negative result if source assets cannot be verified, a task metric cannot be reproduced, performance disappears under group holdout, control samples show spurious structure, uncertainty/calibration fails, or full cost erases the claimed benefit.

**Non-claims:** this contract establishes no quantum advantage, GPU/NPU replacement, 100-million-unit replacement, new particle, new physical law, material substitution, commercial bio-oil, net fusion electricity, reduced project WACC or Data-Center-to-One-Phone compression.
