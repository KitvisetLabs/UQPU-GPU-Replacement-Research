# Literature watch — 2026-10-27: natural-proof barrier for state-preparation lower bounds

**Date searched:** 2026-10-27  
**Primary source:** Christine Li and Natalie Parham, “Natural proofs for quantum state preparation lower bounds,” arXiv:2610.06826v1, submitted 2026-10-05.  
**Official source:** https://arxiv.org/abs/2610.06826  
**Evidence class:** OFFICIAL PREPRINT / CONDITIONAL COMPLEXITY-THEOREM CLAIM; not an independent UQPU reproduction  
**Publication owner:** Lane H  
**Implementation owner:** Lane A — proof/equation evidence contracts  
**Evaluation owner:** Lane F — provenance, counterexamples and evidence classification  
**Cross-cutting:** RG-STATEPREP-SPARSE-001, FND-002, FND-006, EQN-004, EQN-005, INV-034, INV-035

## Executive delta

The paper develops a quantum analogue of the Razborov–Rudich natural-proofs barrier for state-preparation lower bounds. Its definition of a natural property has two parts:

1. **Largeness:** the property holds for a sufficiently large fraction of Haar-random states.
2. **Constructivity:** given a sufficiently precise list of all state amplitudes, a classical algorithm can test the property efficiently in the length of that amplitude list. The list itself is exponentially long in qubit count, so this is not a claim of efficient physical measurement or efficient computation in qubit count.

The full-text informal Theorem 1.1 assumes a classically subexponentially secure pseudorandom-function family that has polynomial-size, depth-d threshold-circuit implementations. Under that assumption, no natural property can prove that a state is not e-to-the-minus-n approximately preparable by polynomial-size circuits in the (8d+20)th level of the Magic Hierarchy. The paper's Naor–Reingold corollary specializes this to level 52 under its stated cryptographic assumption. This is a conditional limit on a class of proof strategies, not a refutation of any lower-bound statement.

The authors identify approximate-degree arguments, arguments based on not being a unique ground state of a local Hamiltonian, and mutual-information arguments as examples that are natural under their definition. UQPU records this as the authors' classification, not as an independent audit of each technique.

## Genuine novelty and limitations

The useful delta is methodological: lower-bound discovery must record not only the circuit model and resource measure, but also the proof technique and whether its property meets both naturalness criteria. A plausible argument can be blocked by a meta-complexity barrier even when the target theorem is important.

Limitations:

- The result is a conditional theorem in an arXiv preprint, not a demonstrated physical limitation or a proof that its cryptographic assumption holds.
- It does not say that all state-preparation lower bounds are impossible. It restricts natural-property proof strategies within the stated circuit/precision regime and assumption.
- It does not automatically invalidate a lower-bound theorem, an upper-bound algorithm, or the sparse-state-preparation and sparse-QROM results in arXiv:2608.00414 and arXiv:2607.28260v2.
- The paper discusses unitary implementation separately and does not establish the corresponding cryptographic construction there.
- No UQPU reproduction, theorem proof, hardware result or performance result is claimed.

## Exact UQPU relevance

- **Lane A:** add an explicit proof-method scope check before treating a lower-bound search as an admissible route to a stronger state-preparation theorem.
- **Lane C:** keep state amplitudes, sparse support, QROM description/access, classical readable storage and physical memory as separate resources. The complete-amplitude-list definition is a proof-complexity input model, not a memory-equivalence claim.
- **Lane F:** preserve the cryptographic assumption, naturalness criteria, target circuit class, precision and source version as auditable metadata; unknown fields must remain unresolved.
- **Lane H:** publish the conditional theorem and its limitations without converting the external result into a UQPU result.
- **FND-002 / FND-006 / EQN-004 / EQN-005:** treat proof barriers as search-space information. A failed proof strategy is a first-class negative result; it is not evidence that a mathematical claim is false.
- **Lanes B, D, E and G:** no provider, device, material, fuel, electricity or manufacturing evidence follows directly from this theorem. Their gates remain unchanged.

## Falsifiable follow-up — RG-STATEPREP-NATURAL-001

1. Read and pin the full theorem and proof sections for both sparse-state-preparation sources. Do not infer a proof technique from an abstract or title.
2. For each candidate lower-bound argument, record whether its property is large over Haar-random states and constructively testable from the full amplitude list. Use UNRESOLVED when the evidence is insufficient.
3. Record the exact cryptographic assumption, approximation error, resource target, fixed circuit hierarchy/level and polynomial-size condition. The scope checker must return UNRESOLVED if a required field is unknown.
4. If the stated barrier applies, mark the proof strategy as barrier-limited under that assumption. Do not reject the theorem claim or silently substitute a different assumption.
5. Compare independent proof strategies and test small cases/counterexamples where possible. A successful scope classification is metadata only; proof correctness and model alignment require separate review.

**Falsifier for the workflow:** a record that labels a method NATURAL without both criteria, or claims the barrier applies without the circuit/complexity/cryptographic scope, must fail validation. A record must never report that the barrier itself establishes empirical physics or automatically rejects the claim.

## Disposition

**LITERATURE_ONLY / CONDITIONAL_METHOD_BARRIER / NO TECHNOLOGY PROMOTION.** The contract added in this cycle is a software metadata guard. No new physical law, real-QPU advantage, readable-memory replacement, material substitution, accepted bio-oil, net fusion electricity, lower financing rate, interest saving or Data-Center-to-One-Phone achievement is claimed.
