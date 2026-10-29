# Daily integration — 2026-10-29 — sparse state-preparation asset provenance preflight

**Batch:** [135](../docs/BATCH_135_SPARSE_STATEPREP_ASSET_PROVENANCE_PREFLIGHT.md)  
**Primary owner:** Lane A  
**Evidence/economics owner:** Lane F  
**Provenance owner:** Lane H  
**Starting main SHA:** `12d59c9854d7783e4161ad38008f916f94b1a6fc`

## Integrated decision

The upstream code/asset metadata for the peer-reviewed sparse-state-preparation result is now recorded as a source-pinned manifest. The Zenodo record reports Apache-2.0 source code, Python/Rust tests, a 950.9 kB ZIP and MD5 `c58634ba415b4e3fb729648460f32ad7`. It also warns about an `nbconvert <= 7.16.6` dependency security issue at upload time, so dependency review must precede installation.

The archive download failed in this execution environment. The manifest correctly records that no local bytes, recomputed checksum, dependency audit, upstream test or independent circuit reproduction exists. A regression test prevents those states from being reported as complete without changing the manifest explicitly.

## A–H integration

- **A:** source provenance preflight and test added; small-instance reproduction remains blocked.
- **B:** no QPU target or execution; provider-neutral path preserved.
- **C:** classical description bytes, state dimension, transfer and reconstruction remain separate.
- **D/G:** logical-to-physical mapping waits for reproduced gate counts and a target model; co-design remains active.
- **E:** BIO-001/FUS-001 and material work unchanged; no energy/fuel claim is inferred.
- **F:** source metadata is not promoted to a reproduced algorithm or economic result.
- **H:** strategic references and multilingual master-plan context preserved.

## Decision and next gate

Keep the external Toffoli result at literature-only status. Retrieve the archive in a controlled environment, recompute hashes, inspect dependencies, run upstream tests and reproduce small instances against an independent classical reference. No paid QPU job was submitted.
