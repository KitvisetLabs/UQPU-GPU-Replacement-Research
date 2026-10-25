# Eight-Lane Research Batch 061 — fault-tolerance spacetime scaling and memory-aware thermodynamics

**Cycle date:** 2026-10-25  
**Canonical starting main:** 6667def60af2d426e16f6aaa6bc5b9461fc70071  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Integration owners:** Lane C — state/memory/data movement; Lane F — evidence/economics  
**Publication owner:** Lane H  
**Evidence class:** software helper + unit tests + literature-only sources  
**Promotion:** no algorithmic advantage, hardware, physical-law, material, fuel, fusion, energy or economic claim promoted

## Starting-state and invariant audit

The newest committed main was inspected before changes. Required charter, version invariants, goals, README, Research Operating System, open-frontier directive, Kanusanan Pongpanna Model, strategic plan references, Batches 056–060, research gaps/work log and current Actions state were reviewed. All eight high-visibility root directives (00, 00A and 01–06) are present. The six Thai/English/Chinese/Japanese/Korean/German strategic-plan links remain in STRATEGIC_PLAN_REFERENCES.md. INV-025/026/027 and INV-029–035 remain present; INV-036/037 are also retained.

At the starting main commit, the UQPU prototype workflow completed successfully across Python 3.10, 3.11 and 3.12 plus the QSP/QSVT, reference-benchmark and target-snapshot jobs; the cold-start handoff audit also passed. This starting-state CI result does not pre-validate this new commit; its own Actions run must complete separately.

## Highest-value delta

Fresh source review identified an unindexed quantum-memory spacetime lower-bound preprint and a recent PRL-accepted thermodynamic-inference paper. Their relevance is to resource/evidence accounting, not to a claim of new physics.

Lane A's `fundamental_limits.py` now includes `fault_tolerance_memory_log_overhead_term(K,S,epsilon)`, returning only the dimensionless term `log(S/epsilon)/K` from the stated width–duration scaling. It validates positive integer width and duration and a finite target error in (0,1). The docstring explicitly says that the result is not an exact overhead or hardware prediction and that the theorem's full assumptions must be checked.

Three regression tests cover the published illustrative scale, monotonicity with duration/target error/width, and invalid input rejection. This is a model-scoped screening aid, not a physical lower-bound implementation for arbitrary noise models.

## Literature delta

New dated article: `docs/literature_watch/2026-10-25-ftqc-spacetime-and-memory-aware-thermodynamic-inference.md`.

- Bharti, Haug and Tanggara, arXiv:2608.26272v1, submitted 2026-08-26: the stated independent-erasure memory model has `C_min = Theta(S*(K + log(S/epsilon)))`; relative overhead scales as `Theta(1 + log(S/epsilon)/K)`. Constants and architecture-specific operations are not provided by the scaling helper.
- Schwarz, Kolomeisky and Godec, PRL accepted 2026-09-25, DOI 10.1103/gwf7-6kvr: entropy-production inference in strongly non-Markovian observations requires adequate memory-order treatment; first-order Markov estimates can be artifactual without justified time-scale separation.

Neither result is a project measurement. No duplicate article was created for previously indexed M-QSP, LLM-guided equation discovery or fusion lithium-retention sources.

## A–H status

- **A — Quantum programming/workloads/compiler/runtime (Priority #1):** added a tested dimensionless width–duration screening term for long-lived coherent workloads. The M-QSP constructive decision algorithm, independently reconstructed feasible/infeasible fixtures and provider-neutral lowering remain open.
- **B — Cloud/QPU/provider integration:** no provider capability or price inference added. No QPU job submitted; provider/target identity and authorization remain required.
- **C — RAM/VRAM/HBM/storage/state/data movement:** explicit width and duration now have a small reusable diagnostic; readable classical memory, state preparation, output and I/O remain separate and unmeasured.
- **D — Device/chip/process/fabrication/packaging:** no device result; any target-specific resource claim must include architecture-specific noise, control and process constraints.
- **E — Biomass/materials/bio-oil/fusion/cooling/infrastructure:** no material, saleable-fuel, fuel-retention, or net-electricity result. BIO-001 and FUS-001 remain open.
- **F — Economics/benchmarks/evidence/energy/finance/integration:** model-scope and hidden-constant caveats are explicit; no accepted-task cost, energy advantage, principal reduction, interest saving or WACC change measured.
- **G — Manufacturing equipment/software/factory systems:** no fabrication result. D/G co-design is preserved; resource asymptotics alone do not establish process or equipment requirements.
- **H — Kanusanan Pongpanna Model/strategy/finance/publication:** published a dated literature watch, batch and integration record while preserving all multilingual master-plan references and strategic context.

Auxiliary Lane I remains auxiliary and does not replace A–H. INV-034/035 remain upstream cross-cutting layers; no AI-generated equation is promoted.

## Foundational and equation-discovery status

- **FND-001:** literature indicates memory-order requirements for thermodynamic inference; no UQPU wall-plug or erasure-energy measurement.
- **FND-002:** the QEC spacetime theorem adds a scoped width–duration resource term; no readable-classical-output lower bound or storage replacement result.
- **FND-003:** no matched control-versus-quantum-speed-limit measurement.
- **FND-004:** no alternative physical primitive demonstrated.
- **FND-005:** no new QFT/particle mechanism or discriminating anomaly.
- **FND-006:** formal/model validation discipline retained; no new theorem proved by this code change.
- **EQN-001–006:** no candidate physical equation promoted. Equation generation remains separate from constraints, held-out tests, counterexamples, proof, experiment, replication and economics.

## Gap and synchronization

New gap artifact: `docs/RESEARCH_GAP_RG037_QEC_SPACETIME_AND_MEMORY_AWARE_THERMODYNAMIC_INFERENCE.md`.

Large append-only RESEARCH_GAPS.md and WORKLOG.md were not rewritten from partial reads. The dated gap artifact records this cycle's new blocker and unlock criteria; canonical history synchronization debt remains explicit. The verified-discovery index is unchanged because no new physical discovery was made.

## Next highest-value gate

Implement and independently audit the published M-QSP constructive decision algorithm on frozen feasible/infeasible fixtures. Separately, build a synthetic known-truth memory-order benchmark for FND-001 before proposing any physical measurement. No paid QPU, material, fabrication, funding or fusion action is authorized.
