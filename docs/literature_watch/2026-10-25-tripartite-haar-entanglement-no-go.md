# Literature watch — 2026-10-25: tripartite Haar-state entanglement no-go

**Accessed:** 2026-10-25  
**Primary publication owner:** Lane H — research publication  
**Implementation owner:** Lane A — quantum programming/runtime scope guard  
**Cross-cutting:** Lane B/C/F, FND-006, EQN-001–006  
**Evidence class:** PEER-REVIEWED PRIMARY THEOREM / LITERATURE_ONLY  
**UQPU project evidence promoted:** none

## Source and date

Zhi Li, Takato Mori and Beni Yoshida, “Tripartite Haar Random State Has No Bipartite Entanglement,” *Physical Review X* 16, 041013, published 2026-10-13. DOI: 10.1103/d7b9-ctw2. Official publisher source: https://journals.aps.org/prx/abstract/10.1103/d7b9-ctw2.

## Genuine result

The paper proves a scope-specific no-go result for tripartite Haar-random pure states: when each subsystem contains fewer than half of the total qubits, EPR-like bipartite entanglement cannot be distilled with the local operations/local-unitary models covered by the theorem, except with a probability bounded to be doubly exponentially small in system size at the specified fidelity tolerance. The authors also interpret the state as a random encoding for which neither output subsystem supports a nontrivial logical operator under the stated dimension conditions.

The important distinction is that strong global or pairwise correlations do not automatically imply a usable pairwise distilled resource. The paper's result is about a defined random-state ensemble, partition sizes, operations and fidelity notion—not every entangled state or every distributed-QPU protocol.

## Limitations and evidence boundary

- This is a peer-reviewed theoretical result; UQPU has not independently reproduced its proof or asymptotic probability bound.
- The size predicate alone cannot establish that a workload's prepared state is Haar-random or that its operations match the paper.
- Structured resource states, non-Haar distributions, nonlocal operations, different task definitions or conditions outside the theorem's scope require separate analysis; they are not automatically ruled out.
- Absence of distillable EPR-like entanglement is not absence of all correlations, and the theorem does not by itself determine an architecture's throughput, latency, error rate, energy or cost.
- No new physical law, QPU advantage, memory replacement, Data-Center-to-Phone result or commercial consequence is claimed.

## Exact UQPU relevance

- **Lane A:** prevent a compiler/runtime or workload plan from treating subsystem-size compatibility as proof of a usable distributed entanglement resource.
- **Lane B:** provider-neutral network plans must record state family, partitions, permitted operations, fidelity, success probability and state-preparation/communication costs before making a repeater or distributed-QPU claim.
- **Lane C / FND-002:** preserve the distinction between quantum correlations, distilled usable resources and application-visible classical output/storage. Neither qubit count nor Hilbert-space dimension is readable RAM/VRAM/storage.
- **Lanes D/G:** any hardware consequence is downstream of a validated workload and resource protocol; this paper supplies no device or manufacturing evidence.
- **Lane E:** no biomass, fuel, material or fusion inference follows.
- **Lane F:** include preparation, communication, retries, decoding and accepted-task quality in any future end-to-end comparison.
- **Lane H:** this is strategic-context literature, not a financing or commercialization result.
- **INV-034/035:** a rigorous conditional theorem narrows a stated model class; a proposal outside that class must name its changed assumption and derive a discriminating prediction.

## Executable scope guard and falsifiable follow-up

The new helper `tripartite_haar_no_go_size_condition_applies(n_a,n_b,n_c)` checks only the strict arithmetic condition `2*n_i < n_a+n_b+n_c` for all three subsystems. Its return value is an applicability preflight, not a theorem verifier. Unit tests cover strict-boundary handling, permutation invariance and invalid inputs.

Next:
1. Attach explicit state-distribution and operation-model metadata to any distributed-QPU workload that invokes this guard.
2. Freeze subsystem sizes, target EPR fidelity, local-operation set, success-probability accounting and state-preparation/communication costs before simulation.
3. Compare a Haar-random control family with a separately specified structured-state family on held-out seeds. Report finite-size behavior without treating small-system numerics as proof of an asymptotic theorem.
4. Independently check the paper's derivation or reproduce its probability bound before promoting theorem-level reproduction.
5. If an architecture relies on a state family or operation outside the theorem, state that changed assumption and test a distinct observable rather than claiming the no-go is bypassed by declaration.

**Pass condition:** the scope guard fails closed on invalid sizes, and any theorem-level replication is independently checked with the paper's full assumptions.  
**Failure condition:** an in-scope workload is silently classified as proven Haar-random, or a result outside the size/operation assumptions is mislabeled as covered.  
**Promotion boundary:** no hardware, engineering, economic or new-law claim is promoted.
