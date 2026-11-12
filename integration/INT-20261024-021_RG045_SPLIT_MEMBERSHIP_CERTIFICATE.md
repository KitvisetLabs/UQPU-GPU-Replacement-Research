# Integration handoff — INT-20261024-021 RG-045 split-membership certificate

**Date:** 2026-10-24  
**Status:** PROPOSED / HOSTED CI PENDING  
**Primary implementation owner:** Lane A  
**Integration owner:** Lane F  
**Publication/context owner:** Lane H  
**Source:** `research_lanes/A_quantum_programming_runtime/PROGRESSIVE_EQUATION_DISCOVERY_CONTRACT.md`  
**Implementation note:** `docs/RESEARCH_GAP_RG045_IMPLEMENTATION_2026-10-24.md`  
**Canonical main at cycle start:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`

## Shared contract

The progressive equation-discovery plan's `DataSplits` certificate now binds the source-dataset digest, sample-ID namespace, three explicit membership lists, versioned canonicalization, per-split hashes and whole-manifest digest. It rejects cross-split overlap and within-split duplicates before comparing manifest digests. A different hash cannot conceal an overlapping record ID.

## Interface ownership

- Lane A owns the validator and its unit tests.
- Lane F owns the leakage/selection-bias interpretation, evidence labels and any future cost accounting.
- Lane H owns the literature-watch context and the rule that external equation-discovery results are not UQPU execution evidence.
- Lanes B, C, D, E and G consume the status boundaries without duplicating the certificate implementation.

## Evidence and stop conditions

This is an offline software-protocol guard only. The actual loader must verify the source bytes and derive the IDs from those exact bytes. Hosted CI is pending; therefore the change is not yet accepted as a completed gate. RG-045 stays open until exact-commit CI and loader-level provenance tests pass.

No provider calls, QPU jobs, shots, energy measurements, cost measurements or physical-law promotion occurred. No lane may infer a commercial material/fuel/fusion advantage or Data-Center-to-Phone feasibility from this protocol test.
