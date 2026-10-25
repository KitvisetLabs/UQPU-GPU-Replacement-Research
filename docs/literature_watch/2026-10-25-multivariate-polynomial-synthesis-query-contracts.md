# Literature watch — 2026-10-25: multivariate polynomial synthesis and query-model boundaries

**Accessed:** 2026-10-25  
**Primary owner:** Lane A — quantum programming, workloads, compiler and runtime  
**Integration owner:** Lane F — benchmarks, evidence and lifecycle-cost accounting  
**Feeds:** A–H; FND-001–006; EQN-001–006; INV-025–027; INV-029–035  
**Evidence class:** LITERATURE_ONLY + local contract tests  
**Project evidence promotion:** none

## Executive delta

Fresh public-primary-source surveillance found two October 2026 arXiv preprints absent from the canonical repository search: *Multivariate quantum signal processing with optimal query complexity* (submitted 2026-10-02) and *Quantum Algorithms for Multivariable Polynomial Transformations: From Efficient Synthesis to Quantum Channel Transformations* (submitted 2026-10-06). The repository already records Guang Hao Low's 2026-10-01 preprint on multivariate QSP and the peer-reviewed constructive M-QSP decision algorithm. The two new preprints add distinct synthesis constructions and sharpen the need to bind each claimed query count to its exact access model.

These are preprints, not yet independently replicated UQPU results. Their stated query complexities must not be merged into a single universal multivariate-QSP bound: the papers differ in polynomial class, oracle access, normalization and construction. No application speedup, hardware cost, energy saving, physical law, or commercial consequence follows from literature alone.

## Source A — multivariate QSP with optimal query complexity

Mingrui Jing, Xin Wang, Zhan Yu and Lei Zhang, “Multivariate quantum signal processing with optimal query complexity,” arXiv:2610.03393, submitted 2026-10-02: https://arxiv.org/abs/2610.03393.

The preprint describes a circuit for multivariate trigonometric polynomials under its stated signal-access model. It reports that each variable is queried exactly as many times as that variable's degree, and calls this query complexity optimal under the paper's assumptions. It also treats commuting unitaries and discusses trainable rotations/readout-gradient behavior.

**Genuine novelty for UQPU:** a candidate per-variable query accounting model, potentially useful where a workload naturally exposes multiple signal variables. The contract must retain the paper's polynomial class, oracle promises, normalization and commuting/noncommuting assumptions; a per-variable degree count is not a wall-clock or total-cost estimate.

**Limitations:** this is an arXiv preprint. The repository has not implemented or independently checked its construction. Its result cannot be transferred to an arbitrary QUBO/QAOA workload, unknown-channel access, provider APIs, or another paper's oracle model without a matched reduction and proof.

## Source B — multivariable polynomial transformations and channel transformations

Zheyu Shen, Yusen Wu, Xiao Yuan, Xiao-Ming Zhang and Yukun Zhang, “Quantum Algorithms for Multivariable Polynomial Transformations: From Efficient Synthesis to Quantum Channel Transformations,” arXiv:2610.08714, submitted 2026-10-06: https://arxiv.org/abs/2610.08714.

The preprint develops a constructive framework for polynomials contractive on a specified matrix domain under joint block access. It reports an O(D/sqrt(tau)) query upper bound for (1+tau)-optimal normalization and exactly D queries under row-block access, matching a degree lower bound in that setting. It builds on a finite algorithmic Schur–Agler theorem and a semidefinite contractivity certificate. It also describes transformations of quantum channels under coherent Kraus access and fixed-order quantum combs specified by causal Choi data.

**Genuine novelty for UQPU:** a second candidate synthesis route with explicit access-model distinctions and a certificate-based contractivity gate. This could help compare joint-block and row-block interfaces before selecting an algorithm/compiler route.

**Limitations:** the asymptotic O(D/sqrt(tau)) expression is not a measured count with a known hidden constant, and exact D queries applies only to the stated row-block-access setting. Joint block access, coherent Kraus access and causal Choi access are strong interface assumptions that must be checked against an actual target/provider. A semidefinite certificate and polynomial-time classical construction do not establish low compiled depth, fault tolerance, accepted-task quality, low energy or low total cost. The source remains a preprint.

## Relation to the existing repository baseline

The canonical 2026-10-25 QSP/QSVT watch already distinguishes: (1) the peer-reviewed constructive decision algorithm for M-QSP, (2) the adversary-bound formulation for QSP, and (3) unknown-channel QSVT with its own dimension, diamond-norm and query assumptions. The existing Batch-056 degree-81 univariate fixture remains a narrow SIMULATION regression control. These new preprints do not validate or invalidate that fixture and do not replace the need for independent feasible/infeasible M-QSP fixtures.

## Cross-lane implication

| Lane | Useful contribution | Required boundary |
|---|---|---|
| A — programming/workloads/compiler/runtime | Added a typed query-contract model for joint-block, row-block, per-variable signal, M-QSP and channel-access claims. | Contract tests do not implement either preprint's synthesis algorithm. |
| B — cloud/QPU/provider integration | Makes oracle-access assumptions explicit before adapter design. | No provider has been shown here to expose the required coherent multi-oracle interface. No job submitted. |
| C — state/memory/storage/data movement | Records variable degrees and target-polynomial/output hashes separately from classical storage. | Hilbert-space dimension is not readable RAM/VRAM/HBM/SSD capacity; coefficient loading and host memory remain unmeasured. |
| D — device/chip/process/packaging | Provides eventual inputs for query, ancilla and control-resource accounting. | Native gates, depth, calibration, fidelity and process-window data are not supplied by the preprints. |
| E — biomass/materials/bio-oil/fusion/energy | No direct material, fuel, fusion or cooling result. | BIO-001 and FUS-001 remain separate empirical/economic gates. |
| F — economics/benchmarks/evidence/integration | Enforces matching polynomial/output, theorem scope, oracle model, normalization, error and evidence class before comparing query claims. | Query counts are not cost per accepted useful task; preprocessing, state preparation, synthesis, host compute, I/O, retries, energy and same-provider pricing remain open. |
| G — chip manufacturing equipment/factory systems | Can consume validated target-native control requirements after Lane D. | No fab/equipment requirement follows from query asymptotics alone; D/G co-design remains required. |
| H — strategic plan/finance/publication | Preserves a traceable literature-to-feasibility gate and the multilingual strategic-plan context. | No CAPEX, financed-principal, interest, WACC or mission-level outcome is measured. |

## Falsifiable follow-up: QOS-MULTIQUERY-001

1. Freeze exact source/version references and hashes for each preprint and create a fixture manifest with polynomial/output hashes, variable names and degrees, matrix domain, normalization, error metric and oracle-access model.
2. Keep Batch-056 as the univariate regression control. Keep the M-QSP constructive decision algorithm as a separate feasibility route; do not substitute it for the two new synthesis constructions.
3. Add small finite controls for joint-block access, row-block access, per-variable signal queries, commuting unitaries, and a noncommuting case where the source assumptions permit it. Record known-feasible and known-infeasible cases only where the relevant theorem defines them.
4. Independently reconstruct the smallest circuits/operators from the full mathematical specifications, compare against a separate numerical evaluator, and require deterministic replay and invariance under semantically irrelevant input reordering.
5. Track per-oracle queries, normalization, degree vector, classical preprocessing, state preparation, ancillas, phase synthesis, circuit depth/native gates, readout/reconstruction, memory/I/O and accepted-output quality. Never combine one model's query bound with another model's price or access promise.
6. Promote nothing beyond MODEL_ONLY/SIMULATION until an independent check passes; real-QPU execution remains disabled absent credentials, bounded budget and explicit user consent.

**Falsifier:** a candidate implementation fails its theorem-scoped feasible/infeasible controls, changes classification under irrelevant reordering, disagrees with an independent operator check, or cannot reproduce the source's query statement under the exact access assumptions. If so, retain the narrower univariate baseline and record the failed extension.

The new executable contract is deliberately a metadata/evidence guard, not an implementation of either paper. Its local unit suite passed 16/16 tests. That is software-contract evidence only.

## Foundational and equation-discovery status

- FND-001: no wall-plug energy or irreversible-erasure measurement.
- FND-002: no changed output-information lower bound; operator dimension is not readable classical storage.
- FND-003: no matched control-versus-quantum-speed-limit measurement.
- FND-004: no alternative physical primitive demonstrated.
- FND-005: no QFT/elementary-particle mechanism or credible anomaly established by these preprints.
- FND-006: mathematical synthesis and certificate generation are useful mathematics-first tools, not new physics.
- EQN-001–006: no new physical equation proposed; current physical limits remain binding.

## INV-029–INV-035 impact

- INV-029: no phone-class physical compression or end-to-end service/cost closure.
- INV-030: no Pangola-carbon functional substitution or elemental transmutation.
- INV-031: no accepted liquid-energy product, mass/energy closure or full bio-oil cost.
- INV-032: no net reliable delivered fusion electricity or lifecycle-cost result.
- INV-033: no measured principal, interest, time-to-evidence or WACC effect.
- INV-034: improves mathematical contract traceability without relaxing physics constraints.
- INV-035: reinforces that AI/math-generated candidates remain hypotheses until theorem, counterexample, held-out and independent checks pass.

INV-025/026/027 remain preserved and evidence-gated. The eight high-visibility root directives, docs/KANUSANAN_PONGPANNA_MODEL.md, STRATEGIC_PLAN_REFERENCES.md and the Thai, English, Chinese, Japanese, Korean and German public plan links remain unchanged. No paid QPU job, material experiment, fabrication, purchase or funding action was authorized.
