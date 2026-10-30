# Research gap RG-HEP-EVENET-PREFLIGHT-001 — checkpoint, dataset and runtime provenance closure

**Opened:** 2026-10-30  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Evidence/accounting owner:** Lane F  
**Cross-lane consumers:** B, C, D, E, G, H; INV-034/035  
**Status:** UPSTREAM CODE/DATA METADATA AUDITED / CHECKPOINT AND SHARD HASHES UNVERIFIED / REPRODUCTION NOT RUN  
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
