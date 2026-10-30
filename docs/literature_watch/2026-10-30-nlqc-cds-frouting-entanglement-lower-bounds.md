# Literature watch — 2026-10-30: lower bounds for robust CDS and one-sided-perfect f-routing

**Checked:** 2026-10-30  
**Primary owner:** Lane B — cloud/QPU/provider integration  
**Cross-lane interfaces:** C (communication/state accounting), F (lower-bound/evidence integration), H (research publication); INV-027, INV-029, INV-034  
**Evidence class:** OFFICIAL ARXIV PREPRINT / THEORY-ONLY / NOT REPRODUCED BY UQPU

## Primary source and dated status

Atsuya Hasegawa and Ranitha Mataraarachchi, “New lower bounds for CDS and $f$-routing,” arXiv:2609.24291. Official record: https://arxiv.org/abs/2609.24291. Version 1 was submitted 2026-09-21; version 2 was revised 2026-10-12. The source is an arXiv preprint; this watch does not assign peer-reviewed status.

## Genuine mathematical contribution

The preprint gives two related results in narrowly defined non-local quantum computation (NLQC) protocol families:

1. **Robust conditional disclosure of secrets (CDS):** the shared-randomness cost is lower-bounded by the logarithm of deterministic simultaneous-message-passing (SMP) communication complexity, even when communication and private randomness are unrestricted. The authors report that the bound is tight for the equality function.
2. **One-sided-perfect $f$-routing:** for protocols exact on one input class and with constant error on the other, the authors derive an entanglement-cost lower bound in terms of sign rank. For the inner-product function, this yields a linear lower bound in both one-sided-perfect settings and matches the known upper bound.

The result is useful as a proof-method and resource-bound lead: it connects protocol-specific entanglement/randomness costs to classical communication-complexity quantities. It does not solve the fully robust $f$-routing entanglement lower-bound problem in general.

## Scope and limitations

- The robust-CDS statement is a shared-randomness lower bound for the specified CDS task. Its connection to $f$-routing is a reduction/motivation, not a universal entanglement-cost theorem for every NLQC protocol.
- The entanglement result is for **one-sided-perfect** $f$-routing, not arbitrary two-sided-error, fully robust routing.
- The concrete linear lower bound is for the inner-product function under the stated protocol assumptions; it must not be generalized to arbitrary Boolean functions without the sign-rank argument.
- The work is theoretical and preprint-only in this project. UQPU has not reconstructed the proofs, checked the version-2 source independently, or reproduced any protocol.
- These results do not bound ordinary classical cloud API calls, a client submitting a circuit to one remote QPU, generic QAOA, or the cost of a provider's hardware.
- Entanglement cost is not readable RAM/VRAM/HBM/storage, not a physical qubit count by itself, and not an energy or dollar cost.
- No new physical law, device mechanism, QPU advantage or commercial capability follows from the theorem.

## Exact UQPU relevance

- **Lane B / provider integration:** if a future architecture distributes one logical quantum computation across remote nodes using nonlocal routing or position-verification-style protocols, the protocol's entanglement and shared-randomness resources may be lower-bounded. First establish that the actual workload satisfies the theorem's task and error model.
- **Lane C / state and data movement:** entanglement and communication resources must remain separate from classical state bytes, storage and transfer metrics. The theorem does not license a Hilbert-space-to-memory conversion.
- **Lane F / evidence:** lower bounds can eliminate infeasible distributed architectures, but only after exact assumptions and resource definitions are mapped. Do not convert an asymptotic protocol bound into device latency, bandwidth, energy or cost.
- **INV-029:** any external node, network, entanglement distribution, classical control or maintenance needed by a future distributed phone-class architecture must be counted. This paper does not change the current Data-Center-to-One-Phone status.
- **INV-034:** the result is a mathematical/communication-complexity boundary, not an experimental physics result.
- **INV-035:** it is not a newly discovered physical equation and does not relax present physical constraints.

## Falsifiable follow-up and stop rule

1. Classify each proposed Lane B workload as (a) one remote QPU job, (b) hybrid classical/quantum execution on one QPU, or (c) genuinely distributed nonlocal quantum computation.
2. Only for class (c), write the exact function/protocol, input partition, allowed communication, shared/private randomness, error model and entanglement resource being counted.
3. Reconstruct the robust-CDS and one-sided-perfect $f$-routing proof statements from arXiv v2; independently check the deterministic-SMP and sign-rank mappings for the selected function.
4. Calculate a task-specific lower bound only if every theorem assumption is met. Preserve an explicit “not applicable” result otherwise.
5. Compare the bound with an explicit distributed architecture's resource budget; include classical communication, entanglement generation/distribution, memory lifetime, loss, synchronization and error correction separately.
6. Keep all results THEORY / MODEL_ONLY until proof reconstruction and, where relevant, independent protocol implementation are complete.

**Disposition:** new-to-main foundational lower-bound surveillance for Lane B. It is a non-blocking theory lead for current UQPU work; no current cloud-provider, QAOA or Data-Center-to-One-Phone claim changes.
