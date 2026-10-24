# Pending-main handoff — RG-045 split-disjointness certificate

**Status:** `PENDING-MAIN / REVIEW REQUIRED`  
**Date:** 2026-10-24  
**Source repository:** `KitvisetLabs/UQPU-GPU-Replacement-Research`  
**Source branch:** `research/2026-10-24-rg045-split-disjointness`  
**Canonical main at cycle start:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`  
**Related issue:** #68  
**Related pending source work:** PR #56, head `5a502c72eef157b1e43def1312033dd32611febd`  
**Primary owner:** integration hub for routing only; Lane A owns the protocol implementation

## What changed

Adds `docs/RESEARCH_GAP_RG045_SPLIT_DISJOINTNESS_CERTIFICATE.md`, documenting why three distinct file hashes do not establish disjoint train/validation/held-out records and specifying the required manifest-bound partition certificate, adversarial tests, evidence boundary and unlock criteria.

This is a gap/handoff artifact only. It does not alter the unmerged PR #56 implementation, does not claim that the new validator exists, and does not modify large append-only `RESEARCH_GAPS.md`.

## Validation and evidence

- Main source SHA was re-read immediately before branch creation: `c7b5958af58fad04a101ef5c6abf6a29293c867e`.
- PR #56's existing hosted tests passed at head `5a502c72eef157b1e43def1312033dd32611febd`; that validates its current tests, not true split disjointness or a CoSR benchmark run.
- This handoff adds no executed benchmark, dataset, physical experiment, provider call or QPU job.
- Evidence class: `SOFTWARE_PROTOCOL_GAP`; RG-045 remains open pending implementation and exact-commit CI.

## Integration edges

- A + F: a data-partition certificate is an upstream requirement for valid held-out equation-search metrics and false-discovery estimates.
- H + INV-034/035: literature and AI-generated mathematical candidates remain third-party/context or hypotheses until the correct proof/experiment gate passes.
- B: zero cloud-provider interactions.
- C/D/E/G: no state-capacity, device, material, fuel, fusion, fabrication or energy advantage follows from this protocol artifact.

## Sync debt

This source commit is **not on main**. The dated PR to main is the required synchronization route. Do not report the artifact as canonical until that PR is reviewed and merged. After merge, record source-SHA-to-main-SHA mapping and rerun the cold-start handoff audit. The ledger-only commit can be reconciled in the next checkpoint to avoid recursion.

## Next action

Implement the manifest-bound disjointness validator and adversarial tests, run exact-commit CI, then close RG-045 only after the overlapping-ID negative test fails closed and the disjoint partition positive test passes.
