# Literature watch — coordinated failure handling for AI-assisted formal proof search

**Checked:** 2026-10-28  
**Primary owner:** Lane H — literature surveillance and publication  
**Cross-lane owners:** Lane A (equation/runtime contract), Lane F (benchmark/evidence/resource accounting)  
**Evidence class:** OFFICIAL_PREPRINT / LITERATURE_ONLY for UQPU  
**Related:** INV-034–035, FND-006, EQN-001–006, RG-EQN-007, RG-EQN-008

## Primary source and version

Haoyu Li, Zeren Shui, Yuhao Zhang, Ferhat Erata, Benjamin Mikek, Murali Krishna Ramanathan and Hao Zhou, **Maestro: Agentic Formal Proof Development by Coordination**, arXiv:2610.25920. Version 1 submitted 2026-10-19; the current v2 was revised 2026-10-27. Official source: https://arxiv.org/abs/2610.25920.

## Genuine methodological delta

The authors describe a Lean proof-development harness in which prover attempts report failure reasons to a coordinator that can change the proof plan globally. The motivation is important for scientific discovery: a failed subgoal may mean insufficient guidance, a false lemma, a flawed decomposition, or a checked counterexample, and these cases call for different actions. The system can guide, retract and replan instead of repeatedly decomposing a false or structurally broken obligation. The authors report results on mathematics and software-verification benchmarks, including 34 of 48 arXivLean theorems for one evaluated configuration; those are paper-reported benchmark claims, not reproduced by UQPU.

## Limitations and evidence boundary

- The source is an arXiv preprint, not an independent UQPU reproduction.
- Formal proof success establishes a frozen proposition under its declared axioms/imports and checker; it does not show that a model describes nature.
- A checked counterexample can refute a formal candidate within the encoded assumptions, but cannot by itself establish the correct replacement physics.
- The source's theorem-proving metrics do not establish a new physical law, quantum advantage, better fuel/material/fusion performance or lower cost.
- Method comparisons can be confounded by different total compute, model calls, retry policies, toolchains and benchmark leakage.

## Exact UQPU relevance

For EQN-001–EQN-006 and FND-006, treat failed proof/discovery attempts as structured outcomes rather than a single boolean: (1) insufficient guidance/resource exhaustion, (2) false or inconsistent lemma, (3) flawed decomposition/assumption interface, (4) verified counterexample, (5) checker/toolchain failure, and (6) inconclusive. This is a candidate workflow contract, not a claim that Maestro's architecture has been validated here. It complements the existing EquationHypothesis gates for incumbent assumptions, dimensional/symmetry/conservation/causality checks, held-out predictions, counterexample search and false-discovery state.

For Lane A, the same discipline motivates pinned SDK semantic tests: distinguish a wrong objective/sign/qubit-order convention from an SDK parse/tool failure and from an actual workload-quality failure. For Lane F, charge all retries, search/model/tool costs and accepted-result reconstruction to the same resource boundary. For Lanes B–E and G, a formal result remains separate from provider, device, material, thermodynamic and manufacturing evidence.

## Falsifiable follow-up

1. Pin arXiv v2, Lean/toolchain versions, benchmark revisions, model identifiers and licenses.
2. Build a small preregistered suite with true lemmas, false lemmas, flawed decompositions, known counterexamples, resource exhaustion and injected checker failures.
3. Compare failure-aware replanning against a fixed recursive-decomposition baseline under identical wall-time, CPU/memory, model-call/token and retry budgets.
4. Score checked proofs, correctly rejected false statements, counterexample recovery, false acceptance, unresolved cases, total cost and time-to-accepted proof; retain every failure.
5. Hold out theorem families and run independent review. A gain that disappears under equal-resource budgets, or increases false acceptance, is rejected.
6. Only after formal-method validation may the pattern be evaluated in the project's equation-discovery workflow. Any physical candidate still requires a discriminating observable, held-out prediction, experiment/proof as appropriate, and independent physical validation.

**Decision:** a useful new method lead for the project's failure ledger and re-planning protocol. No UQPU reproduction, equation promotion or physical claim is made.
