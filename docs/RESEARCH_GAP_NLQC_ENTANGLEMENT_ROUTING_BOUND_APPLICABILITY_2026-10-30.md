# Research gap — RG-B-NLQC-ENTANGLEMENT-ROUTING-001: applicability of CDS and f-routing lower bounds

**Opened:** 2026-10-30  
**Work item:** NLQC-BOUND-001  
**Primary owner:** Lane B — cloud/QPU/provider integration  
**Cross-lane owners:** C (state/communication), F (evidence/lower bounds), H (publication)  
**Status:** LITERATURE_ONLY / NOT_REPRODUCED / NOT_APPLICABLE_TO_CURRENT_QAOA_CLOUD_PATH  
**Related:** INV-027, INV-029, INV-034, FND-002; provider-neutral cloud target contract  
**Literature watch:** `literature_watch/2026-10-30-nlqc-cds-frouting-entanglement-lower-bounds.md`

## Objective

Determine whether any future UQPU workload actually requires nonlocal quantum computation or $f$-routing, and if so whether the protocol assumptions in Hasegawa and Mataraarachchi, arXiv:2609.24291v2, apply to that exact workload.

This is an applicability gate, not a claim that the theorem constrains all remote quantum computing.

## What the source establishes

The preprint reports (1) a shared-randomness lower bound for robust conditional disclosure of secrets in terms of logarithmic deterministic SMP communication complexity, tight for equality; and (2) an entanglement-cost lower bound for one-sided-perfect $f$-routing in terms of sign rank, including a linear bound for inner product matching a known upper bound.

The result does not establish a general entanglement lower bound for arbitrary fully robust $f$-routing, arbitrary distributed quantum algorithms, standard cloud QPU APIs or the current signed-Max-Cut QAOA pilot.

## Current UQPU applicability

- Current QAOA pilot: one workload submitted to one target/backend in the proposed execution path; no nonlocal $f$-routing protocol is specified. **The theorem is not currently applicable.**
- Provider-neutral cloud integration: remote submission to a provider is not itself NLQC. A provider's internal network architecture is outside the UQPU workload contract unless a distributed protocol is explicitly exposed and modeled.
- Data-Center-to-One-Phone: any future multi-node architecture must account for external quantum nodes, entanglement distribution, communication, memory lifetime and control, but this paper supplies no direct phone-compression estimate.

## Unlock criteria

1. Identify a concrete workload that is genuinely distributed across quantum nodes rather than merely remotely submitted to one QPU.
2. Specify its function/protocol, input partition, communication model, randomness, error class and entanglement resource.
3. Verify whether it is robust CDS, one-sided-perfect $f$-routing or a different protocol. Do not relabel a generic workload to fit the theorem.
4. Reconstruct the exact proof and check deterministic-SMP/sign-rank assumptions for the selected function.
5. If applicable, compute a task-specific lower bound and compare it with an architecture-specific entanglement/communication budget, including loss, synchronization, error correction and memory lifetime.
6. If the protocol assumptions do not match, record NOT_APPLICABLE and stop; do not transfer the bound by analogy.

## Evidence and nonclaims

Evidence is OFFICIAL_PREPRINT / THEORY_ONLY. UQPU has not reproduced the proof or implemented a relevant nonlocal protocol. This is not a lower bound on generic cloud-QPU jobs, not a classical memory/storage bound, not a device or energy measurement, not a new physical law, and not evidence of quantum advantage or cost reduction.

## Integration

- **INV-029:** only a future distributed architecture may inherit an external-node/entanglement cost obligation; no mission milestone changes.
- **INV-034 / FND-002:** retain as a scoped mathematical resource-bound lead, not a new output-information theorem.
- **INV-035:** no alternative physical equation is proposed.
- **INV-030–033:** no material, fuel, fusion or finance claim follows.
- **A–H:** B owns the protocol-applicability work; C separates entanglement from classical bytes; F owns evidence and resource accounting; all other lanes retain their current status.

**Next action:** no implementation work until a concrete multi-node UQPU workload is proposed. Continue the existing Lane A QAOA path independently.
