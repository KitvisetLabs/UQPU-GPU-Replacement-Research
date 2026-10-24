# Literature watch — 2026-10-25: QSP/QSVT feasibility, constructive synthesis, and oracle-cost boundaries

**Accessed:** 2026-10-25  
**Primary owner:** Lane A — quantum programming, workloads, compiler and runtime  
**Integration owner:** Lane F — benchmark, evidence and lifecycle-cost accounting  
**Feeds:** A–H; FND-001–006; EQN-001–006; INV-025–027; INV-029–035  
**Evidence class:** `LITERATURE_ONLY` (peer-reviewed theory papers)  
**Canonical starting main:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`  
**Project evidence promotion:** none

## Executive delta

The current main-branch Batch 056 fixture validates a specific univariate QSVT matrix convention numerically. It records degree 81, 81 signal/block-encoding queries, 82 phase rotations, one signal ancilla, zero provider jobs/shots, and no native-gate decomposition or energy/cost measurement. Fresh repository-scoped surveillance found three peer-reviewed results that sharpen the *next* feasibility and resource gates but do not change that evidence classification.

The useful distinction is between (1) deciding whether a proposed signal-processing polynomial is implementable, (2) synthesizing and verifying its phases, (3) compiling the resulting circuit to a target, and (4) measuring accepted useful output and total cost. Passing one layer does not imply the next. These papers are prior publications newly incorporated into this cycle's project analysis, not claims of papers published on 2026-10-25. Targeted searches did not identify a directly relevant primary paper dated 2026-10-24 or 2026-10-25 that changes the current project evidence.

## Sources and evidence classes

### 1. Constructive decision algorithm for multivariable QSP

Yuki Ito, Hitomi Mori, Kazuki Sakamoto and Keisuke Fujii, “Polynomial time constructive decision algorithm for multivariable quantum signal processing,” *Quantum* 10, 2102, published 2026-05-12. Official journal: https://quantum-journal.org/papers/q-2026-05-12-2102/ ; DOI: https://doi.org/10.22331/q-2026-05-12-2102 ; preprint history: arXiv:2410.02332v3.

The paper proposes a classical decision algorithm for whether a specified pair of multivariable Laurent polynomials can be implemented by multivariable QSP (M-QSP). Its abstract states that the necessary-and-sufficient condition is returned by the algorithm and that the method also constructs parameters, with polynomial runtime in the number of variables and signal operators.

**UQPU relevance:** this is a candidate *pre-synthesis admissibility gate* for future genuinely multivariable signal-processing workloads. It can prevent an optimizer from spending phase-synthesis, compilation and target-evaluation resources on an inadmissible polynomial pair.

**Scope limits:** the result is about the formal polynomial class and algorithm stated in the paper. It does not certify arbitrary quantum algorithms, the correctness of an application's semantic transformation, target-specific compilability, physical fidelity, energy, cost, or quantum advantage. A polynomial-time classical decision procedure does not make the quantum circuit itself cheap.

### 2. Adversary-bound characterization for QSP

Lorenzo Laneve, “An adversary bound for quantum signal processing,” *Quantum* 10, article 2025 (2026), DOI: https://doi.org/10.22331/q-2026-03-13-2025. Public institutional record: https://search.usi.ch/en/publications/67791.

The paper reformulates univariate QSP as a state-conversion problem over a function space and reports that the resulting adversary bound characterizes all and only the univariate QSP protocols in that setting. For multiple variables, feasibility of the stated adversary-bound formulation implies an M-QSP protocol; minimizing space is reduced to a rank-minimization problem.

**UQPU relevance:** the result offers a second theoretical lens for checking feasibility and space requirements, and it gives a principled cross-check for a future implementation of the constructive M-QSP decision algorithm. It also cautions against treating “a polynomial was fitted” as equivalent to “a realizable signal-processing sequence exists.”

**Scope limits:** the univariate characterization and multivariate feasibility implication are not identical claims. A feasible relaxation/condition in the multivariate setting must not be silently described as a complete necessary-and-sufficient characterization unless the exact theorem says so. The result is not a device, compiler, hardware, or cost measurement.

### 3. Singular-value transformation of unknown quantum channels

Ryotaro Niwa, Zane Marius Rossi, Philip Taranto and Mio Murao, “Singular value transformation for unknown quantum channels,” *Physical Review A* 114, L030401, published 2026-09-01. Official APS page: https://journals.aps.org/pra/abstract/10.1103/321q-k5dh ; DOI: https://doi.org/10.1103/321q-k5dh.

Given black-box access to a channel on a (d)-dimensional system, the authors construct an approximate block encoding of a Hermitized Liouville representation, then apply QSVT to its singular values. For constructing a channel (delta)-close in diamond norm to the specified block encoding, the paper reports an (O(d^3/\delta)) query upper bound and an \(\Omega(d/\delta)\) lower bound.

**UQPU relevance:** any future unknown-channel QSVT path needs an explicit oracle/query contract, dimension definition, approximation metric and error tolerance before resource or economic claims. The upper/lower bounds help prevent a black-box oracle from being treated as free input data. They may inform Lane B provider requirements and Lane F query-cost envelopes.

**Scope limits:** these bounds apply to the paper's specified construction and oracle model, not every QSVT use case. They do not establish a practical speedup, a low-cost implementation, a readable-memory/storage replacement, or a measured provider result. A Hilbert-space dimension (d) is not a count of classically readable bits.

## Reconciliation with current UQPU evidence

The latest canonical artifact on main, `docs/BATCH_056_BOUNDED_QSVT_MATRIX_FIXTURE.md` and `benchmarks/results/batch056-qos-qsvt-matrix-fixture.json`, reports a constructed 2×2 Hermitian contraction, a 4×4 one-ancilla block encoding, a fixed 81-query/82-phase polynomial sequence and numerical residuals below the predeclared tolerances. It explicitly labels the result `SIMULATION`, with provider jobs and shots equal to zero and gate decomposition, energy and cost not measured.

These papers do **not** invalidate that fixture and do **not** promote it. The fixture is univariate and fixed; the M-QSP decision algorithm is not needed to retroactively validate that narrow numerical contract. Unknown-channel QSVT is a different oracle setting and must not be inferred from a static matrix fixture.

## Falsifiable follow-up: QOS-QSVT-FEAS-001

**Objective:** determine whether an explicit feasibility gate reduces wasted synthesis/compilation effort and correctly rejects inadmissible signal-processing requests, without changing the meaning of existing univariate certificates.

1. Freeze a manifest of univariate and multivariate polynomial fixtures, exact source references, coefficient/statement hashes, domains, variables, operator counts, and expected classifications before running the candidate implementation.
2. Keep the existing univariate Batch-056 fixture as a regression control; require its current numerical certificate and evidence label to remain unchanged.
3. For M-QSP, implement the published constructive decision algorithm only from its full mathematical specification, with pinned code/dependencies. Include independently sourced feasible and infeasible fixtures; compare decisions and constructed parameters against a separate adversary-bound check where the theorem's scope permits it.
4. Reject the implementation if it accepts a known-infeasible fixture, rejects a valid fixture without a stated scope reason, changes results under semantically irrelevant input reordering, or fails deterministic replay. Record counterexamples and failed attempts.
5. For unknown-channel QSVT, create a separate oracle ledger containing (d), (delta), query count, diamond-norm criterion, channel-access assumptions and classical preprocessing. Do not reuse the static-matrix fixture's resource values.
6. Only after these checks, lower a selected circuit to provider-neutral IR, record native-gate counts/depth, target identity and calibration snapshot, memory/I/O, host work, retries, accepted-output quality, energy where measurable, and same-provider total cost per accepted task. No paid QPU submission without credentials, a bounded budget and explicit user consent.

**Falsifier:** the feasibility gate does not improve rejection correctness or synthesis/compile resource accounting under a frozen matched workload set, or the implementation cannot independently reproduce the cited theorem's decision conditions. In that case, keep the existing narrower univariate path and record the failed extension.

## A–H review and cross-lane interfaces

| Lane | Contribution / interface | Boundary and next gate |
|---|---|---|
| **A — programming/workloads/compiler/runtime** | Adds feasibility classification before future M-QSP phase synthesis; preserves the Batch-056 univariate control. | Implement and independently cross-check the decision gate; then lower one accepted circuit. No speedup claim. |
| **B — cloud/QPU/provider integration** | Defines an oracle/query contract for any future unknown-channel target path. | No provider calls or QPU jobs in this watch; target-specific execution remains closed. |
| **C — memory/state/storage/data movement** | Separates operator/state dimension from readable classical memory and records query/phase payloads separately. | Measure full host/state/I/O costs after lowering; no RAM/VRAM/HBM/storage equivalence inferred. |
| **D — device/chip/process/packaging** | Converts future accepted circuits into explicit gate, depth, ancilla and control requirements. | No physical-device requirement before target-aware native decomposition and calibration. |
| **E — biomass/materials/bio-oil/fusion/energy** | Identifies no new material or energy consequence; retains BIO-001 and FUS-001 cost boundaries. | No Pangola material, saleable liquid fuel, net fusion electricity or cooling measurement. |
| **F — economics/benchmarks/evidence/integration** | Separates decision cost, synthesis cost, query count, compilation cost and cost per accepted useful output. | Matched classical baseline and complete same-target accounting remain absent. |
| **G — manufacturing equipment/factory systems** | D/G handoff can consume validated native-gate and control requirements after A/B/D gates pass. | No fabrication or factory requirement derived from asymptotic theory alone. |
| **H — strategy/finance/publication** | Preserves reproducible sources and the no-overclaim boundary for future industry/finance planning. | No principal, interest, WACC, commercial or mission-level effect measured. |

The repository's manifest also contains auxiliary Lane I. It remains auxiliary and is not substituted for or used to suppress permanent A–H review. D/G co-design remains active. Use `research_lanes/` for the primary lane artifact and `integration/` for the shared contract; keep directory depth within 16 levels.

## Foundational and equation-discovery status

- **FND-001:** no wall-plug energy or irreversible-erasure measurement; the thermodynamic-gap contract remains a separate, currently open PR.
- **FND-002:** no change to output-information lower bounds; (d), qubit count and Hilbert-space dimension are not readable classical storage.
- **FND-003:** no matched control-versus-quantum-speed-limit measurement.
- **FND-004:** no alternative physical primitive demonstrated.
- **FND-005:** no QFT/particle mechanism or credible anomaly established by these QSP/QSVT papers.
- **FND-006:** formal feasibility and adversary formulations are mathematics-first tools, not evidence of new physics.
- **EQN-001–006:** these results sharpen algorithmic feasibility/verification boundaries; they propose no new physical equation and do not change incumbent physical laws.

## INV-029–INV-035 impact

- **INV-029:** no Data-Center-to-One-Phone closure; this is a narrow algorithmic feasibility step only.
- **INV-030:** no Pangola/agricultural-residue carbon substitution, recovery, hybridization or elemental-transmutation claim.
- **INV-031:** no accepted biomass liquid-energy product, yield, upgrading or full-cost result.
- **INV-032:** no net reliable delivered fusion electricity or lifecycle-cost result.
- **INV-033:** no measured CAPEX/OPEX, financed principal, interest, time-to-evidence or WACC effect.
- **INV-034:** strengthens explicit mathematical feasibility checks while keeping system/experiment gates intact.
- **INV-035:** demonstrates the correct role for mathematics—characterize candidate algorithms under stated assumptions, then validate implementation and physical consequences independently. No AI-generated equation is promoted as a physical law.

INV-025/026/027 remain evidence-gated. The 100× and 100,000,000× targets, universal subsystem replacement, commercial low-cost bio-oil/fusion and phone-class physical compression remain goals. The multilingual Thai, English, Chinese, Japanese, Korean and German master-plan references and root directives 00–06 are preserved unchanged.

## Next highest-value gate

Implement `QOS-QSVT-FEAS-001` as a separate, pinned preflight contract and tests. Keep the current univariate fixture as a regression control; add multivariate feasibility only after the full decision algorithm and theorem-scoped negative controls are independently reproducible. Then continue to provider-neutral lowering and a same-useful-output target-aware resource ledger. Until then, classify this contribution as `LITERATURE_ONLY`; no hardware, energy, economic, new-law or mission claim is supported.
