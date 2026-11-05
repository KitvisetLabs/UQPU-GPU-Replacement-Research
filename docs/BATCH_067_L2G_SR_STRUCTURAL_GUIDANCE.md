# Eight-Lane Research Batch 067 — L2G-SR structural guidance and fail-closed equation diagnostics

**Cycle date:** 2026-10-25  
**Canonical starting main SHA:** b5aac63f295c2b586f044bcbb228ad0ffb0660ef  
**Source branch:** `research/2026-10-25-l2g-sr-structural-guidance`  
**Primary owner:** Lane F — benchmarks, evidence and economics  
**Implementation owner:** Lane A — equation-discovery tooling  
**Publication owner:** Lane H  
**Evidence class:** SOFTWARE HELPER + UNIT TESTS + LITERATURE WATCH + MODEL_ONLY SMOKE  
**Promotion:** no physical law, quantum advantage, material/fuel/fusion result, economic advantage or Data-Center-to-Phone result promoted

## Starting-state and invariant audit

The current main head was refreshed from GitHub at `b5aac63f295c2b586f044bcbb228ad0ffb0660ef`. The following canonical documents were read: `PROJECT_CHARTER.md`, `VERSION_INVARIANTS.md`, `GOALS.md`, `README.md`, `docs/RESEARCH_OPERATING_SYSTEM.md`, `docs/OPEN_FRONTIER_RESEARCH_DIRECTIVE.md`, `docs/KANUSANAN_PONGPANNA_MODEL.md`, `STRATEGIC_PLAN_REFERENCES.md`, `RESEARCH_GAPS.md`, Batch 061, Batch 062, Batch 063, RG-037, RG-039, the main commit-sync policy, and the latest available canonical reconciliation record. The eight high-visibility root directives 00, 00A and 01–06 were fetched and confirmed present. The six public master-plan language editions (Thai, English, Chinese, Japanese, Korean and German), strategic AI-agent/funding references, INV-025/026/027 and INV-029–035 remain preserved.

The current main branch contains Batch 063 as its latest merged numbered batch. An audit of open pull requests showed that Batch 064, Batch 065 and Batch 066 are already used by separate unmerged branches; this cycle uses Batch 067 to avoid collisions. Large append-only `RESEARCH_GAPS.md` and `WORKLOG.md` were not rewritten from excerpts.

The current main commit's combined-status endpoint returned no status entries. Historical run 40165065031 now shows its listed prototype, Python matrix, QSP/QSVT, Qiskit, reference-benchmark and target-snapshot jobs successful; cold-start audit 40165064989 is also successful. These are historical observations, not validation of this new branch or a CI pass on current main. Exact-head CI for this branch is still required.

## Fresh literature surveillance

The official arXiv preprint **L2G-SR: Learning to Guide LLM-based Symbolic Regression**, arXiv:2610.20685 (submitted 2026-10-14), was not indexed on the current main head. It reports a learned structural verifier that complements numerical fit when choosing symbolic-regression search parents. The reported matched Physics ablation (three seeds, 44 tasks/seed, 400 slots) improves test NMSE, Acc_0.01 and mean true tree-edit distance over a validation-MSE-only control. These are author-reported benchmark results, not a UQPU reproduction. The paper also reports only moderate, domain-dependent verifier correlations; structural feedback is not proof of a correct physical law.

OptScientist (arXiv:2610.28562, 2026-10-20) is already recorded in the main-branch 2026-10-23 watch and was not duplicated. This search did not find new primary evidence that closes BIO-001 accepted-liquid yield/upgrading/cost, FUS-001 net delivered electricity/lifecycle cost, FIN-001 project financing, or any real-QPU advantage. No credible new physical anomaly or physical law was established.

## Implementation and reproducible result

Added:

- `software/uqpu-prototype/uqpu/equation_structure.py`: dependency-free parser for a restricted expression grammar; canonicalizes associative/commutative addition and multiplication; optionally abstracts numeric constants; calculates a transparent root-preserving tree-edit metric.
- `software/uqpu-prototype/tests/test_equation_structure.py`: nine focused tests covering equivalent rewrites, constant policy, structural mismatch, syntax rejection and normalized-distance bounds.
- `benchmarks/results/equation-structure-smoke-2026-10-25.json`: deterministic known-truth smoke artifact.
- `docs/literature_watch/2026-10-25-l2g-sr-structural-guidance.md`: source, novelty, limitations, exact project relevance and falsifiable follow-up.
- `docs/RESEARCH_GAP_RG049_STRUCTURAL_VERIFIER_CALIBRATION.md` and `research_lanes/F_economics_benchmark_evidence/EQN_STRUCTURE_001_CALIBRATION_WORKITEM.md`.
- `integration/INT-20261025-028-STRUCTURAL-GUIDANCE.json`: machine-readable cross-lane handoff.

The smoke fixture returns distance 0 for identical structure and commutative `x+y` / `y+x), distance 0 for `2*x+3` / `5*x+7` under explicit numeric-constant abstraction, and distance 9 (normalized 0.75) for `x**2` versus `x**2 + 0.001*x**3`. This tests only the deterministic metric's behavior. It does not compute numeric fit, train a structural verifier, evaluate generalization, or reproduce L2G-SR. The metric is explicitly not the paper's exact TED implementation.

## A–H status

| Lane | Progress in this cycle | Evidence boundary / next gate |
|---|---|---|
| A — quantum programming/workloads/compiler/runtime | Added restricted equation-structure helper and nine tests; preserved the priority QOS-QSVT-FEAS-001 / M-QSP independent-implementation gate. | No QPU, algorithmic advantage, provider lowering, or accepted useful-task result. Run exact-head CI, then continue frozen feasible/infeasible fixtures and scalable oracle/block-encoding accounting. |
| B — cloud/QPU/provider integration | Provider-neutral paths and no-submit boundary unchanged. | No credentials used, no provider job, no shots/billable usage; never mix provider-target probability and price. |
| C — RAM/VRAM/HBM/storage/state/data movement | Structural helper is small and dependency-free. | No readable-classical-memory equivalence, storage replacement or measured data-movement reduction. |
| D — devices/chip/process/fabrication/packaging | Kept downstream of validated mathematical and target-native requirements. | No device, material, process-window, reliability or packaging evidence; co-design with G remains active. |
| E — biomass/materials/bio-oil/fusion/cooling/infrastructure | Fresh surveillance did not close BIO-001 or FUS-001. | No Pangola substitution, accepted liquid fuel, net delivered fusion electricity, or lifecycle-cost result. |
| F — economics/benchmarks/evidence/integration | Owns RG-049 and EQN-STRUCTURE-001; explicit matched-budget, no-leakage and false-discovery criteria recorded. | No accepted-formula cost or financial result yet; include failed searches and training/inference resources when measured. |
| G — manufacturing equipment/software/factory systems | D/G co-design invariant preserved. | No equipment/process/yield/factory-cost result; do not infer manufacturability from equation similarity. |
| H — strategy/finance/future-industry/publication | Added dated literature watch, batch, gap and integration record; strategic master plan and multilingual links unchanged. | No investment, WACC or macro-interest-rate claim; no strategic source is treated as technical proof. |

## Foundational and equation-discovery progress

- **FND-001:** no new Landauer/thermodynamic-gap measurement; current CMI memory-order calibration remains synthetic and does not infer heat or wall-plug energy.
- **FND-002:** no new output-information lower bound; Hilbert-space dimension/qubit count remains distinct from readable classical memory.
- **FND-003:** no matched control-versus-quantum-speed-limit measurement.
- **FND-004:** no alternative physical primitive demonstrated.
- **FND-005:** no new QFT/elementary-particle mechanism or credible anomaly established.
- **FND-006:** adds a deterministic structure diagnostic for known-law fixtures; this is a mathematics/software instrument, not a new physical result.
- **EQN-001–006:** equation candidate structure, numeric fit, dimensional/symmetry/conservation/causality constraints, held-out generalization, counterexamples, proof/simulation, experiment, independent replication and economics remain distinct gates. Hidden target structure may be used only for post-hoc synthetic evaluation, never runtime selection.

## INV-029 through INV-035

- **INV-029:** no measurable service/capability, physical-support, energy, lifecycle-cost or phone-compression gate passed.
- **INV-030:** no Pangola/agricultural-residue carbon substitution, recovery/recycling or critical-material reduction measured; no elemental-transmutation claim.
- **INV-031:** BIO-001 still lacks accepted liquid-energy/fuel cost after preprocessing, yield, upgrading, H2/catalysts, utilities, CAPEX/OPEX, logistics, financing and non-double-counted coproducts.
- **INV-032:** FUS-001 still lacks reliable net delivered electricity and full lifecycle/financing accounting including recirculating load and component replacement.
- **INV-033:** no financed-principal, interest, capital-lock-up, time-to-evidence, project risk premium or WACC change measured.
- **INV-034:** mathematics-first structural diagnostics are now explicit and falsifiable; no new foundational physical result.
- **INV-035:** no AI-generated equation is promoted to a physical law; incumbent physics remains binding for engineering claims.

INV-025/026/027 and the 100,000,000-GPU and universal 100,000,000-unit GPU/CPU/NPU/RAM/VRAM/storage moonshots remain preserved as falsifiable goals. NPU equivalence still requires real neural-workload semantics, quality, precision, latency, throughput, memory/data movement and cost—not TOPS alone.

## Integration, synchronization and next gate

Cross-lane record: `integration/INT-20261025-028-STRUCTURAL-GUIDANCE.json`. Large append-only histories were not rewritten. This branch has not yet been merged to canonical main. Source code/test commits are `909ba97d1f4cf1656b22756513fb52b158962648` and `af3bfc49df827f62cc61a5023dc2f7c649dee843`; exact final branch head and PR metadata are recorded after publication.

Next highest-value gate: exact-head Python 3.10/3.11/3.12 and cold-start handoff CI. After CI, run a preregistered, law-family-disjoint synthetic benchmark with K=1/2/3, unit/equivalence transformations, noise/correlation, blocked holdouts and matched total budgets. Do not overlap or silently merge pending Batch 064–066 work. No paid QPU job, physical experiment, fabrication, purchase or funding action was authorized.

**Research-Sync:** pending-main
