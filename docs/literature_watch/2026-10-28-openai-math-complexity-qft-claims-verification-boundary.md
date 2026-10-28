# Literature watch — external AI-generated mathematics, complexity and QFT claims

**Watch date:** 2026-10-28  
**Primary source/date:** OpenAI, “Working with academic communities to build scientific understanding,” published 2026-10-26  
**Evidence class:** OFFICIAL_ORGANIZATION_ANNOUNCEMENT; PUBLIC_FORMAL_ARTIFACTS_AVAILABLE_FOR_MATH_AND_CS; PHYSICS_ARTIFACT_PENDING; NOT_INDEPENDENTLY_VALIDATED_BY_UQPU  
**Primary owner:** Lane H — literature surveillance and publication  
**Cross-lane owners:** Lane A — formal/equation tooling; Lane F — evidence and resource accounting; Lane D/E — only if a later physical consequence is independently established  
**Related:** INV-034, INV-035, FND-006, EQN-007, EQN-001–008  
**Focused gap:** [RG-EQN-009](../RESEARCH_GAP_EQN009_EXTERNAL_AI_THEOREM_CLAIMS_2026-10-28.md)

## Primary source and exact artifacts

- OpenAI announcement, dated 2026-10-26: https://openai.com/index/building-scientific-understanding-with-academic-communities/
- Public mathematics manuscript: https://github.com/openai/math/blob/main/preprints/Local-smoothing-for-the-Euclidean-wave-equation-October-25-2026/paper.pdf
- Public Lean formalization scope for the mathematics result: https://github.com/openai/math/blob/main/lean/docs/079.md
- Public computer-science manuscript: https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf
- Public Lean formalization scope for the computer-science result: https://github.com/openai/math/blob/main/lean/docs/378.md

The announcement says the physics collaboration is deferring release of its AI-produced artifacts while an external group examines the claimed constructive-QFT result. Therefore no public proof artifact for that physics claim was available to audit in this cycle.

## What is genuinely new

The 2026-10-26 announcement places three high-consequence claims into different evidence-release paths:

1. **Mathematics:** OpenAI reports a proof of the Euclidean-wave local-smoothing conjecture in every dimension, with stated implications for Kakeya and Stein restriction conjectures. A natural-language write-up and Lean formalization are public.
2. **Computational complexity:** OpenAI reports a refutation of the Exponential Time Hypothesis (ETH), with a public manuscript and Lean formalization. The linked formalization describes a deterministic subexponential-time exact-counting result for fixed-width CNF inputs under its encoded input/resource model. If independently validated, the implications for conditional lower bounds and algorithm design would be substantial; practical runtime consequences are a separate question.
3. **Mathematical physics:** OpenAI reports a constructive-QFT existence result covering specified four-dimensional gauge-field/fermion theories, including QCD and a completion of the Standard Model, and a pure Yang–Mills subproblem. The announced external review and delayed artifact release mean the claim is currently not reproducible from public project inputs.

The methodological delta for UQPU is the need to keep the following as separate records: source claim, exact formal statement, proof artifact, proof environment/axioms, independent mathematical review, physical correspondence, and downstream engineering/economic consequence. A formal proof can establish a theorem relative to its formal statement and environment; it does not by itself establish that the statement faithfully captures the intended physical system or that a practical device benefit follows.

## Evidence boundary and limitations

- These are claims reported by the originating organization. Public Lean artifacts improve inspectability, but UQPU has not compiled or independently reconstructed them, and this watch does not certify the proofs.
- The Lean scope pages are useful maps of the formalized statements, not independent validation or a full review of theorem assumptions, imported axioms, dependency chains, proof admissions, or correspondence with the natural-language manuscripts.
- The ETH result requires independent complexity-theory review of the algorithm, encoding, asymptotic bounds, exact-counting claim, and implications for related hardness results. A theorem about asymptotic complexity does not automatically imply a useful speedup on a finite UQPU workload.
- The QFT claim remains artifact-blocked until the collaborators release sufficient definitions, proof sources, dependency/environment data and explanatory material for independent reconstruction.
- No claim in this announcement establishes a new UQPU physical law, real-QPU advantage, RAM/storage replacement, material substitution, bio-oil yield, fusion net-electricity, commercial cost reduction, or lower project WACC.

## Exact UQPU relevance

- **INV-034 / FND-006:** strengthen mathematics-first triage by tracking candidate statements, reusable lemmas, dependencies, formal status and independent reviewers.
- **INV-035 / EQN-007:** reinforce the mandatory separation between formal verification and physical prediction. The incumbent physical equations remain binding for present engineering claims.
- **Lane A:** formal proof and complexity artifacts may inform future algorithmic search only after the exact theorem and practical workload mapping are checked. They do not displace the Priority-1 signed-Max-Cut/QUBO reference-certificate, provider-neutral lowering and target-aware simulation gate.
- **Lane F / FIN-001:** any later claimed computational improvement must be measured against the same accepted useful output and full resource/cost boundary; no cost or financing benefit is inferred from a theorem announcement.
- **Lanes D/E:** the QFT claim may be scientifically relevant to fundamental theory, but it supplies no present device, material, biomass, fuel or fusion engineering result. The latter require their own observables and experimental gates.
- **Lanes B/C/G:** no provider execution, memory/storage replacement or manufacturing capability follows from these mathematical claims. Provider/target price and probability must never be mixed across systems.

## Falsifiable follow-up

1. Freeze source repository commit, manuscript bytes and SHA-256 hashes; pin Lean version, dependencies, build commands, imported axioms/admissions and environment/container identity.
2. Independently clone and compile the math and ETH developments. Preserve logs and distinguish compilation success from independent theorem review.
3. Have independent reviewers compare the formal statements to the manuscripts and assess definitions, hypotheses, dependency graph, prior literature and novelty. Mutated invalid controls should fail.
4. For the ETH claim, independently reconstruct the algorithm and prove each resource bound under the exact input encoding; separately assess which conditional lower bounds change and whether any finite benchmark improves.
5. For the QFT claim, wait for public artifacts; then freeze definitions, assumptions, axioms, dependency/environment data and a reviewer-authored reconstruction before changing any physics model.
6. Any proposed engineering consequence must state its own measurable prediction, baseline, resource accounting and falsifier. Formal acceptance alone cannot promote an equation to an empirical physical law.

**Disposition:** literature-only triage and a reproducibility target. No theorem, physical law, UQPU advantage, or mission-level result is accepted by this watch.
