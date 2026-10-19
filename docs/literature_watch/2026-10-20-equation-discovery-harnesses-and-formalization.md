# Literature watch — 2026-10-20: equation-discovery harnesses and formal verification

## Sources reviewed

1. **HarnessSR: Learning to Design Symbolic-Regression Solvers** (arXiv:2610.16966, October 2026): https://arxiv.org/abs/2610.16966
2. **The Future of AI-assisted Physics: Discovering, Verifying and Organizing Results via Formalization** (arXiv:2610.14059, 6 October 2026): https://arxiv.org/abs/2610.14059
3. **IBM Quantum Compute client release notes** (observed 20 October 2026): https://quantum.cloud.ibm.com/docs/api/qiskit-ibm-runtime/release-notes

## Evidence class and genuine novelty

- HarnessSR is a public preprint reporting that the *agent harness itself*—roles, prompts, workflow and feedback allocation—can be optimized as part of symbolic regression. Its reported LSR-Synth improvement is benchmark evidence about a method, not discovery of a physical law.
- The formalization paper argues that formal proof infrastructure should sit between AI-generated physics and trusted reuse. It also states an essential limitation: kernel checking a theorem does not prove that its definitions faithfully model nature.
- IBM's official release notes show a live software-interface delta relevant to Lane B: version 0.50.0 (24 September 2026) deprecates server-side EstimatorV2/SamplerV2 in favor of client-side interfaces. This changes implementation planning, not experimental evidence.

## Limitations

- The symbolic-regression results are primarily benchmark results; they do not establish out-of-distribution physical validity, conservation, causality, symmetry, dimensional consistency or independent experimental replication.
- Harness optimization can overfit a benchmark, search budget or feedback representation. A held-out law family and counterexample suite are still required.
- Formal proof validates derivations relative to definitions and axioms; physical adequacy still requires discriminating observations.
- An SDK changelog cannot substitute for a fresh target snapshot, calibration, route certificate, real-QPU quality result or measured economics.

## UQPU relevance and falsifiable follow-up

For EQN-001–006, add the harness configuration to provenance and treat it as a searched object. Compare a fixed baseline harness against an optimized harness on held-out equation families, with identical generator budget, dimensional/symmetry constraints and counterexample search. Pre-register:

- exact train/validation/held-out family split;
- expression/operator grammar and coefficient optimizer;
- dimensional, symmetry, conservation and causality checks;
- structural-recovery score plus numerical residual;
- false-discovery count and counterexample survival;
- proof/simulation path and independent reimplementation.

For Lane B/QOS-AUDIT-010B24, pin the actually installed IBM client during a later authenticated read-only preflight and reject any code path that assumes deprecated primitive interfaces without a compatibility certificate.

## Decision

Material method delta: **yes**. Evidence promotion: **no**. No result reviewed here establishes a new physical law, real-QPU advantage, Data-Center-to-Phone compression, material substitution, commercial bio-oil/fusion or financing advantage.
