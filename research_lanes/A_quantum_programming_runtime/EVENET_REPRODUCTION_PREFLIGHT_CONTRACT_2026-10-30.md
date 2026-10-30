# Lane A reproduction preflight — EveNet source, runtime and data closure

**Work ID:** HEP-EVENET-002  
**Primary owner:** Lane A — quantum programming / workloads / compiler / runtime  
**Interfaces:** B provider portability; C data/state/memory movement; D device requirements; E energy/material boundaries; F benchmark/economics; G manufacturing; H publication/strategy  
**Date:** 2026-10-30  
**Evidence class:** UPSTREAM SOURCE AUDIT + PUBLIC DATASET METADATA / NO UQPU REPRODUCTION

## 1. Purpose

Advance the existing HEP-EVENET-001 workload contract from paper-only context to a source-pinned reproducibility preflight. EveNet is a classical event-level collider-physics foundation model. It is a candidate GPU/CPU/NPU workload for equivalent-useful-output benchmarking, not a quantum-computing result. No QUBO/QAOA mapping is implied.

## 2. Inspected upstream assets

- Code repository: [EveNet-HEP/EveNet-Full](https://github.com/EveNet-HEP/EveNet-Full), inspected at commit [06c3181d9a0f7df3e30edbb1c355b6fec8b5a3ad](https://github.com/EveNet-HEP/EveNet-Full/tree/06c3181d9a0f7df3e30edbb1c355b6fec8b5a3ad).
- The pinned repository's [LICENSE](https://github.com/EveNet-HEP/EveNet-Full/blob/06c3181d9a0f7df3e30edbb1c355b6fec8b5a3ad/LICENSE) declares MIT for the code repository. This does not by itself establish the license of every checkpoint, dataset or third-party asset.
- The [README](https://github.com/EveNet-HEP/EveNet-Full/blob/06c3181d9a0f7df3e30edbb1c355b6fec8b5a3ad/README.md) describes a Ray + PyTorch Lightning training/inference pipeline and points to pretrained weights at [Avencast/EveNet](https://huggingface.co/Avencast/EveNet).
- The pinned [pyproject.toml](https://github.com/EveNet-HEP/EveNet-Full/blob/06c3181d9a0f7df3e30edbb1c355b6fec8b5a3ad/pyproject.toml) declares package version 0.1.6 and Python >=3.12, but its project dependency list is empty.
- The pinned [requirements.txt](https://github.com/EveNet-HEP/EveNet-Full/blob/06c3181d9a0f7df3e30edbb1c355b6fec8b5a3ad/requirements.txt) separately pins the runtime stack, including Ray 2.44.1, Lightning 2.5.1, NumPy 2.1.3, PyTorch 2.6.0 and PyArrow 19.0.1. The two installation declarations are not equivalent; a package-only install cannot be assumed to recreate the runtime.
- The pinned [prediction entry point](https://github.com/EveNet-HEP/EveNet-Full/blob/06c3181d9a0f7df3e30edbb1c355b6fec8b5a3ad/scripts/predict.py) loads YAML configuration, uses Ray datasets and PyTorch Lightning, and requires an explicit model/pretrained checkpoint path. The training entry point additionally requires WANDB_API_KEY; do not assume training credentials are needed for inference.
- The [Avencast/EveNet-Pretrain dataset card](https://huggingface.co/datasets/Avencast/EveNet-Pretrain), accessed 2026-10-30, labels the dataset MIT and reports 541,248,429 rows, 193 GB total file size and 1,100 columns. Its viewer reports that 1,100 columns exceed the viewer's 1,000-column limit. These are mutable publisher-host metadata, not locally verified bytes or hashes.

The paper's source-reported pipeline figure of approximately 4 TB raw data to approximately 180 GB Parquet is not silently equated with the current dataset card's 193 GB. Resolve exact dataset revision, shard inventory and GB/GiB convention before calculating compression or transfer ratios.

## 3. Provenance and environment blockers

1. The model checkpoint page/revision, file list, SHA-256 values and checkpoint license have not been verified. The README's link is not proof of checkpoint availability or permission.
2. The dataset card is mutable. Its current row/size/license metadata does not pin a revision, every Parquet shard, schema, preprocessing recipe or underlying event-data provenance.
3. The code license, dataset-card license and model-weight license are separate records. Do not infer that MIT on the code repository licenses weights or every upstream event source.
4. The empty dependency list in pyproject.toml conflicts with the pinned requirements file. No lockfile, clean environment installation, import smoke test or inference execution was performed.
5. The public viewer limitation makes a bounded Parquet/streaming path necessary; no full dataset download is proposed for the first reproduction.
6. No event-level split manifest or record/trajectory/source-group disjointness certificate has been verified.

## 4. Required bounded reproduction protocol

### Stage A — immutable asset manifest

Pin and hash:
- upstream code commit and license file;
- model/checkpoint repository revision, every selected checkpoint/config file, size and SHA-256;
- dataset repository revision, selected Parquet shard names, sizes, SHA-256, row counts and schema;
- preprocessing code/config, normalization metadata, event selection and label definitions;
- Python 3.12 environment, complete resolved dependency lock, CUDA/runtime/driver and hardware/software versions.

Record failed downloads, inaccessible files, missing licenses and hash mismatches as negative evidence. Do not substitute a similarly named checkpoint or dataset revision.

### Stage B — one analysis task

Select exactly one task already defined by the paper and its released configuration/data. Freeze the task, source event groups, train/validation/test manifests, output semantics and the source-defined quality metric before running. If the required task assets or acceptance metric cannot be verified, stop at preflight and do not invent a surrogate task.

Use group-disjoint splits at the strongest available provenance level (source sample, generator/configuration, run or event group). Distinct filenames or file hashes alone do not prove disjoint records.

### Stage C — equivalent useful outputs

Run the same pinned checkpoint, input records, preprocessing, precision policy and accepted-output contract on:
- a competitive optimized CPU implementation;
- a competitive GPU implementation;
- an NPU implementation only where the exact model/operators/precision are supported.

Report task quality and calibration under the source-defined metric, precision, latency distribution, accepted-task throughput, failures, retries and output reconstruction. TOPS alone is not an NPU comparison.

Do not compare training on one platform with inference on another and call it a matched benchmark. Do not treat model execution success as accepted scientific output.

### Stage D — full resource and cost accounting

Measure, rather than infer:
- checkpoint bytes, event/input/output bytes, Parquet columns and selected rows;
- peak host RAM, GPU/NPU memory, buffers, cache, data-loader and preprocessing memory;
- storage reads/writes, host-device and network transfer bytes/time;
- preprocessing, inference and postprocessing CPU/GPU/NPU time;
- queue/wait time where a provider is used, retries and failed work;
- energy with a declared meter/boundary and uncertainty;
- provider billing, host compute, storage, transfer and all other priced costs.

Separate historical pretraining cost from task-specific inference. If amortizing pretraining, declare the number and type of accepted downstream analyses over which it is divided. Include event generation and preprocessing where relevant; do not silently omit them. Unknown cost/energy remains unknown, not zero.

## 5. Cross-lane interfaces

- **B:** keep provider identity and price provenance target-specific. No provider or QPU job is required for this classical workload preflight.
- **C:** 541M-row/193GB/1,100-column metadata is a storage and streaming lead, not a measured UQPU memory requirement.
- **D/G:** use only measured precision, throughput, bandwidth, power and memory requirements to derive device/process/metrology needs. No chip or factory conclusion follows from A100 training.
- **E:** no Pangola carbon, bio-oil, fusion or cooling result is inferred from a collider-model paper.
- **F:** compare total cost per accepted scientific analysis, with training amortization and excluded costs explicit.
- **H:** publish reproducible evidence and source licensing boundaries; do not turn source-reported compute into a funding or valuation claim.

## 6. Acceptance and stop rules

The preflight passes only when code, checkpoint, dataset, config, environment and split manifests are pinned; licenses are individually resolved; a clean inference environment is reproducible; and an independent reviewer can verify all hashes.

A task reproduction passes only when the source-defined quality metric and frozen acceptance threshold pass on held-out groups and the full resource record is complete. CPU/GPU/NPU comparisons require identical accepted outputs and equivalent total accounting.

No full pretraining run, cloud spend, paid QPU job or external account credential is authorized by this contract. Any later paid execution requires credentials, a bounded budget and explicit user consent.

## 7. Nonclaims

This source audit does not reproduce EveNet, validate its paper metrics, measure UQPU GPU/NPU performance, establish quantum advantage, replace RAM/VRAM/storage, demonstrate a physical law, reduce critical materials, produce accepted bio-oil, deliver fusion electricity, lower financed principal/WACC, or complete Data-Center-to-One-Phone.
