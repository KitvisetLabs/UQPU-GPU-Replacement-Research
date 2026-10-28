# Literature watch — AI-assisted physics formalization and the AxQM benchmark

**Date checked:** 2026-10-28  
**Primary owner:** Lane H — literature surveillance and publication  
**Cross-lane interfaces:** A (workload/semantic contracts), D (device-model mapping), E (physical process models), F (evidence gates), H (reusable research infrastructure)  
**Evidence class:** OFFICIAL PREPRINTS / EXTERNAL BENCHMARK DESCRIPTION / LITERATURE_ONLY  
**Related:** INV-034–035, FND-006, EQN-001–EQN-006, RG-EQN-PHYSICS-SEMANTIC-FAITHFULNESS-001

## Sources and date status

1. Sven Krippendorf, Leopoldo Sarra and Joseph Tooby-Smith, “The Future of AI-assisted Physics: Discovering, Verifying and Organizing Results via Formalization,” arXiv:2610.14059, submitted 2026-10-06; the current HTML text is dated 2026-10-15. https://arxiv.org/abs/2610.14059
2. Weichen Winston Yin, Jacob M. Taylor, Dirk R. Englund and Frank H. L. Koppens, “AxQM: A Textbook-Scale Benchmark for Formal Proof Synthesis in a Library of Finite-Dimensional Quantum Mechanics,” arXiv:2609.05157, submitted 2026-09-04; paper text dated 2026-09-07. https://arxiv.org/abs/2609.05157

These are external preprints/benchmark reports. UQPU did not run AxQM, reproduce a proof-synthesis score, or independently audit its formal library in this cycle.

## Genuine methodological advance

The formalization perspective distinguishes three tasks that are often conflated:

- **Proof discovery:** propose a derivation or proof.
- **Formal verification:** have a small trusted kernel check that the proof establishes a particular formal statement from its stated definitions and assumptions.
- **Physical faithfulness:** independently establish that those definitions, assumptions, approximations and observables actually represent the intended physical system.

AxQM reports 1,019 kernel-checkable proof-synthesis tasks across 479 items derived from finite-dimensional quantum information and computation. The stated grading checks compilation, absence of Lean's sorry placeholder in the dependency closure, and absence of newly introduced axioms. The authors also explicitly discuss semantic failure modes: a formal statement can compile while defining the conclusion rather than deriving it, weakening a quantifier, or placing a crucial step in the hypotheses. The kernel cannot detect a mismatch between a valid formal proof and the intended physical meaning.

The useful new project-level insight is therefore not “AI proves physics.” It is that **formal proof evidence and the physical interpretation of the formal statement need separate, auditable acceptance gates**.

## Limitations and evidence boundary

- The sources are not UQPU reproductions and do not establish a new physical law, a quantum advantage, or an engineering/economic benefit.
- AxQM is deliberately restricted to finite-dimensional Hilbert spaces; infinite-dimensional systems and unbounded operators are outside its stated scope.
- Kernel acceptance proves the encoded statement, not the truth of the assumptions, the correctness of the model-to-physics dictionary, or agreement with an experiment.
- A proof can be perfectly valid and physically irrelevant if its formalization is vacuous or circular.
- Benchmark size and proof success are not measures of real-device runtime, energy, cost per accepted task, or AI research productivity without matched resource accounting.

## Exact UQPU relevance

- **INV-035 / EQN-001–EQN-006 / FND-006:** equation candidates need both proof/data provenance and independent review of the mapping from variables, units, assumptions and observables to the intended physical system.
- **Lane A:** a correct SDK or circuit transformation is not sufficient if the workload objective, optimizer sign, bit order or accepted-output meaning is wrong. The signed-Max-Cut portable-QAOA integration test added in Batch 097 is a software analogue of this semantic distinction.
- **Lane D/G:** a formal device/control model must still be tied to measured device, process, metrology and packaging conditions.
- **Lane E / BIO-001 / FUS-001:** formal derivations of mass/energy or thermal-fluid models do not establish that a biomass or fusion process follows those assumptions in a real plant.
- **Lane F / FIN-001:** formalization effort must be costed separately from proof-checker resources, human review, failed attempts and cost/time per accepted useful result. No finance saving is claimed here.
- **Lane H:** shared formal libraries can improve cold-start reuse only if definitions, dependencies, source revisions and review history are preserved.

## Falsifiable follow-up

1. Require an explicit physical-interpretation review status and notes, independent from formal proof status and independent empirical replication. This is implemented as a conservative promotion guard in software/uqpu-prototype/uqpu/equation_discovery.py; its tests are pending exact-head CI on the Batch 097 branch.
2. Use a small known-law exemplar such as constant acceleration: formalize a trajectory \(x(t)\), assumptions \(x''(t)=a\), \(x(0)=0\), \(x'(0)=0\), and derive \(x(t)=\frac12 at^2\). Separately audit that the physical assumptions are appropriate to the claimed regime.
3. Seed deliberately vacuous and weakened statements and verify that the review checklist rejects them even when the proof kernel accepts them.
4. Preserve failed, inconclusive and reviewer-disagreement outcomes; do not turn the review status into a model-confidence score.
5. Keep formal verification, held-out predictive tests, counterexample search, experiment/replication, device consequences and economics as separate gates.

## Decision

**LITERATURE_ONLY.** The source supports strengthening the project’s proof-versus-physical-meaning contract. No AI-generated equation is promoted, and no physical, QPU, material, fuel, fusion-electricity, cost, WACC or Data-Center-to-Phone claim is advanced by these external reports alone.
