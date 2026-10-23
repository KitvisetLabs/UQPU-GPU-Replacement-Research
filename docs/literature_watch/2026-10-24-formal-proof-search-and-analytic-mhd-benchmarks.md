# Literature watch — 2026-10-24: formal proof search and exact 3D MHD benchmark families

**Primary owner:** Lane H — foundational-method and strategic research publication  
**Integration owner:** Lane F — evidence, reproducibility and cross-lane gates  
**Evidence class:** PEER-REVIEWED FORMAL-METHOD RESULT + THIRD-PARTY ANALYTIC MODEL  
**UQPU evidence promotion:** none

## Executive delta

Two developments can improve the project's research method without changing any technology claim:

1. AI-generated proof search paired with a proof assistant has been evaluated on open mathematical problems at research scale.
2. New closed-form families solve the established ideal magnetohydrodynamic (MHD) equilibrium equations without stellarator symmetry, offering candidate exact reference cases for three-dimensional equilibrium solvers.

These results are different in kind. A formal proof checks a proposition inside specified axioms and a formalization; an analytic MHD solution supplies a mathematical reference state. Neither by itself validates a new physical law, reactor performance, commercial fusion electricity, quantum advantage or UQPU economics.

## Source A — AI-assisted formal proof search

George Tsoukalas et al., “Advancing mathematics research with AI-driven formal proof search,” Science 394(6820), 234–239, published 2026-10-08, DOI 10.1126/science.aej2213. The authors report an agent resolving 9 of 353 attempted open Erdős problems and proving 44 of 492 OEIS conjectures using formal proof search with Lean verification.

- Peer-reviewed bibliographic record: https://pubmed.ncbi.nlm.nih.gov/42848891/
- Authors' preprint: https://arxiv.org/abs/2605.22763

### Genuine novelty and limitations

The useful design principle is that a language model proposes proof steps while a formal kernel checks the proof object. This can reject invalid mathematical derivations. The reported successes are subsets of attempted benchmark collections, not a guarantee of general theorem discovery. Formal validity is relative to the encoded definitions, axioms and statement; it does not establish that the formal statement accurately models nature.

### Proposed falsifiable follow-up: EQN-PROOF-001

- Formalize the finite-distribution identity for strictly positive probabilities: q_i = p_i'/p_i and I = sum_i p_i q_i^2. For a group G_k of equal scores, P_k = sum_{i in G_k} p_i and P_k' = q_k P_k, so grouping preserves classical Fisher information exactly.
- State the domain explicitly: finite support, p_i > 0, differentiability, normalized probabilities and derivatives, and equal scores within each group.
- Separately formalize the dimension lower bound that follows from pairwise orthogonality. Do not infer sufficiency for arbitrary controlled-unitary protocols from a count alone.
- Keep q = 0 and support-changing boundaries as separate cases. Require a machine-checked proof term, an independent exact-rational implementation and counterexample search.
- Passing validates only the formalized mathematics; it does not demonstrate physical QFI transfer or change the scope of arXiv:2610.29146 without a full independent derivation.

## Source B — analytic non-stellarator-symmetric ideal-MHD equilibria

Opal Issan, Jonathan Citrin, Matt Landreman and Brendan Tracey, “Analytic non-axisymmetric 3D MHD equilibria without stellarator symmetry,” arXiv:2610.07304, submitted 2026-10-05: https://arxiv.org/abs/2610.07304.

The preprint constructs two parameterized families of non-axisymmetric ideal-MHD equilibria that break stellarator symmetry while retaining the specified nested-flux-surface structure within their stated parameter domains. Setting the symmetry-breaking parameters to zero recovers the symmetric reference cases. The paper proposes the families as exact reference cases for testing three-dimensional equilibrium solvers whose symmetry assumptions otherwise exclude such cases.

### Genuine novelty and limitations

The result broadens the available analytic test fixtures for solver validation. It does not report an independent UQPU reproduction, solver performance comparison, experimental plasma validation, dynamic stability, reactor viability, net electric output, lifecycle cost or a new physical law. An exact equilibrium is not equivalent to dynamic stability or an engineering-ready reactor.

### Proposed falsifiable follow-up: FUS-MHD-BENCH-001

- Independently transcribe both families and freeze source version, parameter fixtures and admissible domains.
- Check the incumbent equations (curl B) cross B = grad p and div B = 0 symbolically where tractable and by independent high-precision residual evaluations over interior points and parameter sweeps.
- Include the zero-asymmetry limit, positive and negative symmetry-breaking values, boundary-domain checks and convergence under increased numerical resolution.
- Compare a solver with the relevant symmetry restriction against a representation that permits symmetry-breaking terms. Report residual norms, convergence, failure cases, runtime and resources. Make no solver-advantage claim before executing this test.
- A passing benchmark is solver-validation evidence only. Any reactor or FUS-001 cost consequence requires separate stability, engineering, net-electricity and economic evidence.

## Cross-lane relevance

- **A:** proof-carrying algebraic checks can guard equation promotion; no accepted workload win follows.
- **B:** offline gates only; no provider integration or QPU job.
- **C:** no conversion from mathematical state-space dimension to readable classical memory.
- **D/G:** exact MHD fixtures may eventually validate modeling tools; no chip or factory requirement is inferred.
- **E:** FUS-MHD-BENCH-001 is solver verification, not fusion-energy evidence. BIO-001 and Pangola-material gates are unchanged.
- **F:** retain assumptions, source versions, independent implementations, failed cases and full resource accounting.
- **H:** strengthen proof and exact-reference-model research while preserving the multilingual strategic plan.
- **INV-029–035:** methodological contribution only; none of their end-to-end evidence gates passes because of these publications.

## Required evidence discipline

Keep third-party results separate from project evidence. Retain nulls and counterexamples. No generated equation becomes a physical law by declaration. Any challenge to established physics must specify the incumbent assumption, alternative equation, dimensional/symmetry/conservation/causality checks, limiting cases, falsifier, discriminating observable, held-out prediction, experiment or proof, and independent validation path.
