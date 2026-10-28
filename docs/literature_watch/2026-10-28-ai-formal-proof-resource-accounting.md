# Literature watch — formal proof discovery, counterexample recovery and cost per accepted proof

**Checked:** 2026-10-28  
**Primary owner:** Lane H — literature surveillance and publication  
**Cross-lane owners:** Lane A (equation/runtime contract), Lane F (benchmark/resource accounting), Lane E (physical-model transfer)  
**Evidence class:** OFFICIAL_PREPRINT / LITERATURE_ONLY for UQPU  
**Related:** INV-034–035, FND-006, EQN-001–008, RG-EQN-007, RG-EQN-008

## Source 1 — automated conjecture resolution with formal verification

Haocheng Ju et al., “Automated Conjecture Resolution with Formal Verification,” arXiv:2604.03789, version 2 dated 2026-06-03. Official source: https://arxiv.org/abs/2604.03789. The reported system separates informal proof search (Rethlas with Matlas theorem retrieval) from formalization and Lean 4 proof checking (Archon with LeanSearch). The authors report resolving a 2014 commutative-algebra problem and checking the formal result; source code and results are linked from the preprint.

**Genuine novelty for this project:** the workflow makes candidate construction, theorem retrieval, formalization and kernel-checked proof distinct artifacts. The formal checker can catch gaps in an informal proof and make the mathematical obligation auditable.

**Limitations:** this is an arXiv report, not a UQPU reproduction. Formal correctness applies to the frozen formal statement, axioms, imports and checker. It does not guarantee that a natural-language claim was formalized faithfully, and it does not validate a constitutive equation, physical law, device or economic claim.

## Source 2 — repeated AI-generated proofs with explicit gap disclosure

Yichen Huang, “Autonomous disproofs of the sum-product conjecture over R with GPT-5.5 Pro,” arXiv:2607.20525, submitted 2026-07-09. Official source: https://arxiv.org/abs/2607.20525. The author reports a three-stage proof-plan / proof-construction / critical-review pipeline; seven correct proofs in eight independent trials; and one incomplete trial that identified its unresolved gap rather than reporting success. Reported average reasoning use was 132.4k tokens per trial, with code, intermediate outputs and proofs released.

**Genuine novelty for this project:** independent repetitions reveal variability and motivate treating an explicit unresolved proof gap as a distinct outcome rather than a success/failure boolean. The paper's result is reproducible in principle because the source reports releasing the run artifacts.

**Important scope limitation:** the paper itself explains that the target theorem already states the existence of counterexamples and that the human disproof had appeared. The experiment therefore tests autonomous construction/recovery of a proof for a specified target, not a blind choice between proving and disproving an unknown conjecture. The sample is only eight trials; the reported 7/8 rate is imprecise (a rough Wilson 95% interval is about 0.53–0.98). Token count is not financial cost, and the study is not a physical-law discovery.

## Cross-source synthesis

The useful methodological lesson is not “AI proves physics.” It is that discovery should separate:
1. candidate generation and search;
2. formal statement and provenance;
3. kernel-checked proof or explicit counterexample;
4. faithfulness of the formal statement to the intended physical model;
5. dimensional, symmetry, conservation, causality and limiting-case checks;
6. held-out prediction and adversarial counterexample search;
7. discriminating experiment and independent physical replication;
8. device/system consequence and full economics.

A proof checker can certify the encoded theorem under declared axioms. It cannot by itself establish that the theorem's variables describe nature, nor that a fitted equation is a physical law.

## Exact UQPU relevance

- **Lane A / EQN-007:** retain formal-proof provenance and status separately from equation acceptance. Classify objective mismatch, proof gap, formalization mismatch, parser/tool failure and resource exhaustion separately.
- **Lane F / EQN-008 / FIN-001:** measure wall time, model identity and price basis, calls/tokens, CPU/GPU/RAM, checker/toolchain, retries, human verification, abstentions, false acceptance and cost per accepted proof. Do not compare costs from unmatched provider/pricing bases.
- **Lane E / INV-030–032:** physical constitutive models for Pangola-derived materials, bio-oil upgrading or fusion auxiliaries need measured data and independent validation after the formal gate; the papers provide no evidence of material substitution, saleable fuel or net electricity.
- **Lanes B–D and G:** no provider, device, fabrication or target execution result follows from a proof-search paper.
- **INV-029 / INV-033:** proof-workflow efficiency might reduce time-to-evidence only if measured; this article does not show phone-class physical compression, lower financed principal, lower interest, lower WACC or a commercial advantage.
- **INV-034–035:** imagination stays broad during hypothesis generation, but mathematical verification and physical evidence govern technology claims.

## Falsifiable follow-up

1. Freeze a small test suite containing true obligations, false statements, false lemmas, known counterexamples, formalization mismatches, parser/checker failures, timeouts and resource exhaustion.
2. Compare a fixed generate-review baseline against a formal-verifier/failure-aware-replanning pipeline under equal wall-time, model-call/token, CPU/memory and retry budgets.
3. Record verified proofs, correct rejections, false acceptance, false discovery, abstentions, unresolved cases, retries, checker resources, energy where measurable, and cost per accepted proof.
4. Hold out theorem families, preserve all failed attempts, and obtain independent review. Reject any gain that disappears under equal budgets or increases false acceptance.
5. Only then test one candidate physical equation with explicit units, symmetries, conservation, causality, scaling/limiting cases, grouped held-out prediction, counterexample search and a discriminating experiment.

**Decision:** method lead for EQN-007/008 and the evidence ledger only. No UQPU reproduction, new physical law, quantum advantage, material/fuel/fusion result or economic benefit is claimed.
