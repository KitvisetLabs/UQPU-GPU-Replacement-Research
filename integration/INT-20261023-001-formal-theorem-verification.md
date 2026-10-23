# INT-20261023-001 — Formal theorem-discovery provenance gate

**Date:** 2026-10-23  
**Primary owner:** Lane A — software research interface  
**Integration owner:** Lane F  
**Literature/publication owner:** Lane H  
**Canonical starting main SHA:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`  
**Status:** `TESTED_LOCALLY / EXACT-COMMIT-CI-PENDING`

## Purpose and hypothesis

Formal theorem discovery can contribute to FND-006 and EQN-001–006 only if the repository distinguishes a candidate theorem, a complete primary checker record, an independent replay record, and a physical claim. The implementation hypothesis is that a small metadata gate can reject common provenance mismatches before proof-search results enter a physics or technology narrative.

## Inputs

- `software/uqpu-prototype/uqpu/equation_discovery.py` — existing equation-hypothesis contract.
- `software/uqpu-prototype/uqpu/frontier_hypothesis.py` — existing falsifiable frontier contract.
- `06_AI_ASSISTED_PHYSICS_EQUATION_DISCOVERY.md` and `05_FOUNDATIONAL_PHYSICS_MATHEMATICS_DEEP_FRONTIER.md`.
- Ota et al., arXiv:2606.28747; Garmaev et al., arXiv:2605.03841.
- Evidence policy: metadata, formal proof, physical experiment, engineering feasibility, and economics are separate evidence types.

## Interface added

`software/uqpu-prototype/uqpu/formal_proof_gate.py` provides `FormalProofRecord` and `sha256_hex`.

A complete primary checker record requires statement, axiom-set digest, proof-object digest, checker identity/version, checker image digest, result, zero exit code, and log digest. An independent replay record additionally requires a distinct checker identity and image digest, with matching theorem-statement, axiom-set, and proof-object digests.

The interface validates record consistency only. It does not parse proof objects, invoke a proof assistant, authenticate logs, or establish theorem truth. Its status strings intentionally say `...METADATA_COMPLETE`, never `PROVEN_PHYSICAL_LAW`.

## Local verification

Command: `PYTHONPATH=software/uqpu-prototype python -m unittest discover -s software/uqpu-prototype/tests -p 'test_formal_proof_gate.py'`

Result: **9 passed, 0 failed** in an isolated Python 3.13.5 environment using the staged module/test contents. This is not the full repository test suite and not exact-commit GitHub Actions CI.

Negative controls include missing checker data, a same-checker “independent” replay, mismatched axiom/proof/statement digests, malformed digest, nonzero exit under `PASS`, and an explicitly rejected candidate.

## Cross-lane interfaces

| Lane | Relationship | Measurable output / boundary |
|---|---|---|
| A | Owns the executable metadata gate and tests. | Deterministic status and mismatch rejection; no workload-performance claim. |
| B | Reviews provider evidence provenance only. | No target call, credentials, jobs, shots, or billing. |
| C | Consumes no memory-capacity claim from proof metadata. | No RAM/VRAM/storage/state equivalence. |
| D | May consume a future mathematically verified device bound. | No device or process requirement until physical assumptions are mapped. |
| E | May consume a future theorem only through separate material/energy contracts. | BIO-001/FUS-001 remain unchanged and unpromoted. |
| F | Owns evidence labels, false-discovery accounting, and end-to-end economics. | Proof-search/checker runtime and memory must be measured later; no cost result yet. |
| G | Requires a validated device requirement before factory co-design can respond. | No manufacturing implication yet; D/G co-design remains active. |
| H | Publishes the literature watch and staged strategic relevance. | Reusable, self-contained source and falsifier record. |

FND-001–006 and EQN-001–006 remain upstream across A–H. D/G co-design is explicitly retained. Lane I's existing vehicle/levitation program was reviewed as supplemental repository scope and remains `MODEL_ONLY`; it does not replace any A–H lane.

## Falsifier and next gate

Reject the interface if a single checker is accepted as independent replay, a changed theorem/axiom/proof digest passes, or a metadata-complete record is represented as a physical law. Next: run exact-commit CI, then add a bounded theorem fixture with false-claim controls and two independent proof-checker backends. Only after that should the discovery system be evaluated on held-out theorem families and total proof-search cost.
