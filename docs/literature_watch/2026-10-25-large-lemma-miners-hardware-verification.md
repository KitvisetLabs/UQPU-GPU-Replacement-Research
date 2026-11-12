# Literature watch — 2026-10-25: neural-symbolic lemma mining for hardware proof obligations

**Source date:** IJCAI 2026 proceedings (Main Track, pp. 3988–3998)  
**Primary owner:** Lane H — strategic research and publication  
**Integration owner:** Lane F — evidence, reproducibility and economics  
**Feeds:** Lane A compiler/runtime correctness; Lane D/G device and manufacturing-control verification; FND-006; EQN-001–006; INV-034–035  
**Evidence class:** PEER-REVIEWED FORMAL-VERIFICATION METHOD  
**UQPU evidence promoted:** none

## Primary source and genuine novelty

Romy Peled, Daniel Kroening, Michael Tautschnig and Yakir Vizel, “Large Lemma Miners: Can LLMs Do Induction Proofs for Hardware?”, Proceedings of the Thirty-Fifth International Joint Conference on Artificial Intelligence (IJCAI 2026), Main Track, pp. 3988–3998. Official proceedings page: https://ijcai.org/proceedings/2026/444. DOI: https://doi.org/10.24963/ijcai.2026/444.

The paper combines two LLM prompting configurations—few-shot and agentic—to generate candidate auxiliary lemmas for SystemVerilog safety properties, then uses a formal symbolic procedure to filter candidates and assemble inductive strengthenings. The reported benchmark contains 109 verification tasks; for 90% of those tasks, at least one prompting setup produced a provably correct inductive argument after sufficient reprompting. The central contribution is not that an LLM's text is trusted, but that candidate generation is placed upstream of a formal checker that rejects invalid, non-inductive or irrelevant candidates.

## Limitations and evidence boundary

- The result is scoped to the paper's mid-size open-source RTL verification task set and formal properties; it is not a universal success rate for arbitrary industrial designs.
- The 90% figure means at least one prompting setup succeeded for a task after repeated attempts. It is not a per-sample success probability, a claim that 90% of generated lemmas were correct, or a guarantee of low runtime/cost.
- The proof establishes the encoded property for the encoded transition system. Incorrect specifications, faulty RTL-to-model translation, missing environmental assumptions or an incomplete property can still make a formally proved result irrelevant to the intended device.
- The paper does not demonstrate UQPU compiler correctness, QSP/QSVT synthesis correctness, a real-QPU workload, a new physical law, or a technology/economic advantage.

## Exact UQPU relevance

**Lane A — programming/runtime:** adopt the method as a candidate workflow for small, sharply scoped invariants around provider-neutral IR rewrites, circuit lowering and result-contract preservation. Candidate lemmas must be checked by a trusted solver/proof engine; natural-language explanations are not certificates.

**Lane D/G — device and manufacturing co-design:** the same pattern can be tested on a small RTL controller or manufacturing-tool interlock only after the transition system, reset assumptions and safety property are frozen. No fabrication or yield conclusion follows from an RTL proof.

**Lane F — evidence discipline:** record the source revision, property hash, checker/tool version, solver outcome, counterexamples, reprompt count and proof runtime. Keep “generated candidate”, “solver checked”, “independently reproduced”, “verified implementation” and “validated physical behavior” as separate states.

**FND-006 / EQN-001–006 / INV-034–035:** formal verification can establish a mathematical implication inside a faithful formalization. It does not establish that an equation models nature. The equation-discovery ladder remains generator → constraints → evaluator → held-out test → counterexample search → proof/simulation → discriminating experiment → independent replication → system/economics consequence.

## Proposed falsifiable follow-up

1. Freeze one small provider-neutral compiler rewrite and its pre/postcondition, including exact numeric and measurement semantics.
2. Ask a candidate generator for auxiliary invariants under a fixed prompt budget; preserve malformed and rejected outputs.
3. Require the formal tool to prove initiation, consecution and implication to the target property. Retain counterexamples and all timeouts.
4. Compare with a manually written baseline on the same pinned test cases. Record proof rate, checker time, human repair time and resource cost.
5. Re-run the accepted proof using an independent checker path or independently encoded reference model.
6. For any proposed physical equation, add dimensional/symmetry/conservation/causality checks, held-out predictions and a discriminating experiment; never promote from formal proof alone.

**Acceptance rule:** zero unchecked candidate lemmas may enter the trusted path. A timeout is TOOL_BLOCKED, not proof of falsehood or infeasibility. Any counterexample that violates the target property blocks promotion until resolved. No paid QPU jobs or external actions are required for this follow-up.

## Surveillance conclusion

This is a useful, peer-reviewed method result for proof-guided candidate filtering. It improves the project's verification strategy, not its measured computing capability. No new QPU, memory/storage, Pangola material, accepted bio-oil, fusion net-electricity, finance-rate or Data-Center-to-Phone evidence is established.
