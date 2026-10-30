# Research gap RG-HEP-EVENET-PREFLIGHT-001 — checkpoint, dataset and runtime provenance closure

**Opened:** 2026-10-30  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Evidence/accounting owner:** Lane F  
**Cross-lane consumers:** B, C, D, E, G, H; INV-034/035  
**Status:** CODE/MODEL/TWO CHECKPOINTS/ONE PRETRAIN SHARD PINNED AT SOURCE; DOWNSTREAM TASK DATA, RUNTIME LOCK AND REPRODUCTION OPEN  
**Related work:** HEP-EVENET-001; HEP-EVENET-002; INV-025/026/027; INV-029–035.

## What is now verified at source-metadata level

1. The upstream EveNet code repository was inspected at commit `06c3181d9a0f7df3e30edbb1c355b6fec8b5a3ad`. Its LICENSE declares MIT for that code repository.
2. Its README describes Ray + PyTorch Lightning and points to a separate Hugging Face checkpoint repository.
3. Its pyproject declares Python >=3.12 and an empty project dependency list, while requirements.txt separately pins the runtime dependencies. This is a reproducibility/install-path mismatch to resolve, not proof that the code cannot run.
4. Its prediction entry point uses Ray datasets, YAML configuration and a configured checkpoint path. Training separately requires WANDB_API_KEY.
5. The Hugging Face pretraining dataset card currently reports MIT, 541,248,429 rows, 193 GB and 1,100 columns. The public dataset viewer reports a 1,000-column limit. These are publisher-host metadata; no local file bytes, hashes or schema were independently verified.
6. The paper's approximate 4 TB raw -> 180 GB Parquet figure and the dataset card's 193 GB listing must be reconciled against a pinned revision and explicit decimal/binary units. They must not be used as one exact compression ratio.

## Open blockers

- The linked checkpoint/model repository revision, exact checkpoint files, hashes and model-weight license remain unverified.
- Dataset revision, full shard list, per-shard hashes, schema, underlying event-data terms and preprocessing provenance remain unverified.
- The runtime dependency list is not declared in pyproject; no clean Python 3.12 installation, lockfile or import smoke test exists.
- No bounded inference task has been run. No source metric, quality threshold, group-disjoint split or output acceptance record has been independently reconstructed.
- No CPU/GPU/NPU comparison exists under an identical output contract.
- No local RAM/VRAM, transfer, energy, latency, throughput or total cost per accepted analysis has been measured.
- Paper-reported pretraining GPU-hours exclude event generation and preprocessing; no complete training/inference lifecycle cost is available.

## Unlock criteria

1. Pin the model/checkpoint repository revision, checkpoint/config file inventory, byte sizes, SHA-256 values and separate model-weight license.
2. Pin the dataset revision and all selected Parquet shard hashes; verify row counts, schema, units, source provenance and the 180 GB/193 GB discrepancy.
3. Build a clean Python 3.12 environment from a complete lock generated from the inspected requirements; record every resolved dependency and accelerator/runtime version.
4. Freeze one paper-defined analysis task and its source-defined metric/acceptance threshold. Verify event/sample/run group disjointness; distinct files alone are insufficient.
5. Reproduce one bounded inference task and retain raw predictions, logs, failed runs and exact environment.
6. Compare CPU/GPU and, if genuinely supported, NPU on the same checkpoint, inputs, precision and accepted-output contract.
7. Record input/output/checkpoint bytes, peak RAM/VRAM, transfers, preprocessing/host work, inference latency/throughput, retries, energy boundary, billable usage and all-in cost per accepted task.
8. Have an independent reviewer reproduce the hashes and one bounded result before any claim is promoted.

## Evidence boundary and nonclaims

This gap is not an EveNet reproduction and not UQPU evidence. It establishes no QPU execution or advantage, no GPU/NPU replacement, no readable classical-memory/storage equivalence, no new physical law, no Pangola material substitution, no accepted biomass fuel, no net fusion electricity, no lower financed principal/WACC and no Data-Center-to-One-Phone milestone.

Large append-only `RESEARCH_GAPS.md` and `WORKLOG.md` were not rewritten from partial snapshots. This focused gap is the canonical detailed blocker; aggregate synchronization remains explicit debt.


## 2026-10-30 Batch 141 update — source asset pins partially resolved

The following source-level pins supersede the corresponding unverified-hash statements above. Canonical detailed manifest: ../research_lanes/A_quantum_programming_runtime/EVENET_ASSET_PIN_MANIFEST_2026-10-30.json.

- Code: EveNet-HEP/EveNet-Full@06c3181d9a0f7df3e30edbb1c355b6fec8b5a3ad, MIT. Python >=3.12; pyproject.toml has an empty dependency list while requirements.txt separately pins packages.
- Model: Avencast/EveNet@afba5b47478f0c25c6a5a5755ac30738925d73ad, model-card MIT.
- Candidate SSL.20M.last.ckpt: file commit 44bbaf06c548b143ca45e4c35e4598881632c6e3, 220658079 bytes, publisher SHA-256 e2ed50ca4f2c44fc1692c07c504ffdbad7d4a2c36a8d6206b6b3e2a7f5f148b2.
- Candidate checkpoints.20M.a4.last.ckpt: file commit 3969201ae20b5353ddb99c1810254ea7115217ed, 267634251 bytes, publisher SHA-256 3c8b571328112988fd7186953a2f3155f0e22301a9c8d7e24f520881251a5ef2.
- Pretraining dataset: Avencast/EveNet-Pretrain@200a96e9c9d7b3876398169760540f3189df0205, current card declares MIT; one shard data_Combined_Balanced_run_0.parquet at file commit e6da3c120f3d74304beb2958aedaa8426fb92a11, 201065223 bytes, publisher SHA-256 b9dafebb5ab49b3ed491f050d8eeb9d46bc8aed8d82e046fe42af86c549148cb.
- Custom dependency: AvencastF/torch-linear-assignment@7680e2c8ac1e8ab0d2eabd29fb4eb7b8fd8a2c8b, Apache-2.0, but EveNet's Dockerfile still clones the default branch without pinning it.
- The Docker documentation uses tag docker.io/avencast1994/evenet:1.5; no immutable image digest is recorded. The Dockerfile uses Python 3.12.3 and CUDA 12.4.1 on Ubuntu 22.04.

Hash boundary: these SHA-256 values were read from Hugging Face Xet/Git-LFS pointer metadata. No bytes were downloaded and no local recomputation or independent byte-level verification occurred. The selected shard is a pretraining shard, not a downstream held-out test split. The dataset's current MIT card metadata replaced earlier fair-noncommercial-research-license metadata on 2026-03-30; upstream source-data rights still require audit.

Still open: select the exact task/checkpoint/config; pin all downstream evaluation splits and hashes; resolve upstream data rights; pin the custom dependency and image digest; reconcile approximately 180 GB in the paper versus approximately 193 GB on the dataset card; build a clean Python 3.12 environment; download/rehash; verify schema and group/run disjointness; run bounded inference and independent reproduction; then perform identical-output CPU/GPU/NPU and full resource-cost comparisons.

This update does not establish an EveNet reproduction, QPU/GPU/NPU advantage, or any INV-029–035 technology milestone.
