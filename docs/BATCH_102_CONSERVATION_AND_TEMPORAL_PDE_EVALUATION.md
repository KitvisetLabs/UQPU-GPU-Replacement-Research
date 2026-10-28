# Batch 102 — conservation and boundedness metrics for PDE surrogates

**Date:** 2026-10-28  
**Starting main SHA:** 42e6614db390db7b3e248bc6b383d67e9d00dd3b  
**Primary owner:** Lane A — workload/model acceptance metrics  
**Evidence owner:** Lane F — reproducibility, uncertainty and economics  
**Literature owner:** Lane H — source provenance and publication  
**Cross-lane consumers:** B, C, D, E, G; INV-034/035 feed A–H  
**Evidence class:** SOFTWARE_IMPLEMENTATION + SYNTHETIC_UNIT_FIXTURES + LITERATURE_ONLY  
**Execution boundary:** no external PDE benchmark, no upstream model reproduction, no real QPU, no paid job, no physical experiment

## 1. Dynamic starting-state and invariant audit

The latest observed main commit was resolved dynamically as 42e6614db390db7b3e248bc6b383d67e9d00dd3b. The cycle inspected PROJECT_CHARTER.md, VERSION_INVARIANTS.md, GOALS.md, README.md, docs/RESEARCH_OPERATING_SYSTEM.md, docs/OPEN_FRONTIER_RESEARCH_DIRECTIVE.md, docs/KANUSANAN_PONGPANNA_MODEL.md, STRATEGIC_PLAN_REFERENCES.md, root directives 00_ULTIMATE_NORTH_STAR_DATA_CENTER_TO_PHONE.md and 00A/01–06, the current Batch 101 and 100, RESEARCH_GAPS.md, WORKLOG.md, integration/COLD_START_HANDOFF_MANIFEST.json, current equation-discovery/split-disjointness utilities and tests, and the signed-Max-Cut pinned-SDK gate.

The canonical eight-lane architecture A–H remains in force. INV-025/026/027 and INV-029–035 remain preserved. The six-language Thai/English/Chinese/Japanese/Korean/German strategic-plan links and recorded strategic AI-agent/funding references remain in STRATEGIC_PLAN_REFERENCES.md and the Kanusanan Pongpanna Model context. No root directive or strategy reference was removed or rewritten.

## 2. Fresh literature surveillance

The official PMLR volume for the 43rd International Conference on Machine Learning yielded three methods not previously indexed in this repository:

1. **FluxNet**, Lan et al., PMLR 306:62530–62559 (2026), https://proceedings.mlr.press/v306/lan26c.html. The paper reports a cumulative-transport architecture with exact discrete conservation and structural bounds for its stated mass-conservation task class and four named PDE benchmark families.
2. **TINNs**, Dai et al., PMLR 306:22358–22384 (2026), https://proceedings.mlr.press/v306/dai26a.html. Time-conditioned network weights are reported to improve selected time-dependent PDE results, with paper-reported maxima of 4× relative-L2 error improvement and 10× faster convergence on the authors' tasks.
3. **Heavy-tailed PINNs**, Abijuru et al., PMLR 306:211–239 (2026), https://proceedings.mlr.press/v306/abijuru26b.html. The paper motivates Student-t residual modeling because some PINN residuals are heterogeneous/heavy-tailed and reports improved results on its own benchmark suite.

These sources change methods to evaluate, not the accepted equations of physics. Their reported figures remain external literature, not UQPU reproduction or mission evidence. A dated literature-watch article records the source-specific novelty, limitations and falsifiable follow-up.

Other fresh searches revisited equation discovery, formal theorem search, quantum speed limits, biomass conversion and fusion roadmaps. CoSR's APS-accepted/arXiv-withdrawal status conflict is already recorded in the repository and remains unresolved; no duplicate CoSR article was created. The DOE fusion roadmap remains a commercialization roadmap, not proof of commercially low-cost net electricity. No fresh evidence changed BIO-001, FUS-001 or FIN-001 acceptance status.

## 3. Lane A implementation

Added:

- software/uqpu-prototype/uqpu/pde_surrogate_metrics.py
- software/uqpu-prototype/tests/test_pde_surrogate_metrics.py

The function score_conservative_bounded_trajectory accepts an initial discrete field, predicted fields at successive times, optional positive cell weights, optional caller-justified lower/upper bounds, a same-unit conservation scale and predeclared tolerances. It reports:

- the initial and per-time-step discrete conserved totals;
- maximum and mean absolute conservation drift;
- maximum and mean dimensionless normalized drift;
- whether the declared drift tolerance passes;
- count/rate of lower/upper bound violations and maximum raw violation;
- whether bounds were applicable and, if applicable, whether the supplied predictions pass them.

The scale is derived only from the initial weighted field unless explicitly provided. A zero-magnitude initial field requires an explicit positive scale. Boolean, malformed, non-finite, inconsistent-shape and overflow inputs fail closed. If the caller supplies no physical bounds, the result explicitly reports bounds as not applicable rather than implying acceptance.

Nine isolated unit tests passed in Python 3.12. They cover exact conservation and bounds, detectable conservation drift, weighted discrete integrals, lower/upper bound violations, tolerance semantics, zero-scale behavior, malformed shapes, non-finite/boolean/overflow rejection and the no-bounds case. These are synthetic software fixtures; no PDE was solved and no scientific model was calibrated.

## 4. New focused gap — RG-PDE-SURROGATE-001

**Status:** OPEN / SOFTWARE_METRIC_IMPLEMENTED / SYNTHETIC_TESTS_PASS / SCIENTIFIC_BENCHMARK_NOT_RUN  
**Primary owner:** Lane A  
**Evidence owner:** Lane F  
**Publication owner:** Lane H  
**Objective:** prevent low training loss or a good mean prediction score from hiding conservation drift, physical-bound violations or poor temporal generalization in PDE-surrogate work.

**Unlock criteria:**

1. Pin a public source revision and license for the selected upstream model before execution.
2. Pin the scientific dataset, acquisition/provenance record, PDE, initial/boundary conditions, discretization, cell weights, parameter domain, reference solver and acceptance rules.
3. Validate on a synthetic known-solution PDE before any public benchmark; preserve time-block and parameter/geometry group holdouts.
4. Compare only within the same task class and identical resource envelopes. Do not pool solver tasks with symbolic equation-discovery tasks.
5. Record held-out relative L2 error, PDE residual, initial/boundary errors, normalized conservation drift, bound-violation rate/max, long-rollout stability, wall/CPU/accelerator time, peak memory, failures and total cost per accepted output.
6. Retain failed seeds and counterexamples. A metric PASS certifies only the supplied discrete fields against the declared contract; it does not prove that the selected physical quantity is conserved by nature or that the surrogate solves the governing PDE.

The large append-only root RESEARCH_GAPS.md and WORKLOG.md were not rewritten wholesale. This standalone dated Batch 102 record is the detailed gap until safe canonical index synchronization; that sync debt is explicit.

## 5. A–H status

| Lane | Status this cycle | Next gate |
|---|---|---|
| A — quantum programming/workloads/compiler/runtime | Added conservation/bound trajectory metrics and 9 synthetic tests. Priority-1 signed-Max-Cut pinned-SDK reconstruction remains higher execution priority. | Exact-head CI, then run the pinned Qiskit 2.5.2 operator reconstruction against exhaustive direct/QUBO/Ising scores and the complete argmax set. Separately run a synthetic known-solution PDE before upstream model reproduction. |
| B — cloud/QPU/provider integration | Provider-neutral adapters and no-submit boundary preserved; no credentials or paid job used. | Simulator/dry-run first; never mix provider/target probability and another target's price. |
| C — RAM/VRAM/HBM/storage/state/data movement | No state-to-classical-storage equivalence inferred. | Future solver/model comparison must record field/state bytes, cell weights, peak memory, transfers and output reconstruction. |
| D — device/chip/process/fabrication/packaging | Scope preserved; no device result. | Bind any future model to real discretization, device/control, reliability and process constraints. |
| E — Pangola/materials/bio-oil/fusion/cooling/infrastructure | BIO-001 and FUS-001 remain open; no material, accepted-liquid or net-electricity result. | Only transfer a PDE surrogate after the governing balance, data provenance and process boundary are justified. |
| F — economics/benchmarks/evidence/integration | Added explicit conservation/bounds metrics; no benchmark winner or economics measured. | Matched budgets, full compute cost and source/data provenance; keep model fit distinct from accepted useful output. |
| G — chip manufacturing equipment/factory systems | Continuous D/G co-design preserved; no yield/cost-per-good-device evidence. | Any surrogate must be tied to metrology/process data and a validated factory objective before economic transfer. |
| H — strategy/finance/future industries/publication | Published the dated PMLR literature watch; multilingual strategic links and agent/funding references remain intact. | Keep external papers as literature leads until independent reproduction and lawful source audit. |

## 6. Foundations, equations and permanent mission

- **FND-001:** thermodynamic-gap accounting remains active. The new metric helper is not a thermodynamic result.
- **FND-002:** output-information and reconstruction costs remain binding; a PDE field or model state is not automatically a readable useful output.
- **FND-003:** matched control-versus-quantum-speed-limit measurement remains open; no timing claim is inferred from surrogate papers.
- **FND-004:** alternative physical primitives remain hypotheses until a causal, discriminating experiment exists.
- **FND-005:** QFT/elementary-particle mechanism scans remain active but have no new physical evidence from this cycle.
- **FND-006:** mathematics-first invention advances through a stricter surrogate acceptance contract, not a new law.
- **EQN-001–EQN-010:** the existing discovery/evaluation gates remain evidence-gated. The new utility does not fit equations, establish calibration or rank methods.
- **INV-029:** no Data-Center-to-One-Phone physical-compression milestone; useful-service, energy, form-factor and lifecycle-cost closure remains required.
- **INV-030:** no Pangola-carbon functional substitution or elemental transmutation claim.
- **INV-031:** no accepted liquid-fuel yield/full-cost claim.
- **INV-032:** no reliable net-delivered fusion-electricity or lifecycle-cost claim.
- **INV-033:** no measured reduction in financed principal, absolute interest, project WACC or economy-wide rates.
- **INV-034/035:** current physics remains binding; AI/model candidates require dimensional, symmetry, conservation, causality, held-out, counterexample, experiment/proof and independent-validation gates.

The 100×/100,000,000× targets and INV-025/026 universal 100,000,000-unit GPU/CPU/NPU/RAM/VRAM/storage moonshots remain falsifiable goals, not results. No Hilbert-space-to-classical-memory equivalence or NPU-TOPS-only claim is introduced.

## 7. CI, synchronization and next highest-value gate

At cycle start, the prior base SHA f3ca3c12b20b4fa28adfb276ae5804427f9ca2a8 had core/invariant run #1945 and cold-start audit #1204 pass. The first Batch 101 commit's new-head run #1946 and audit #1205 failed because the manifest referenced docs/RESEARCH_GAPS.md instead of root RESEARCH_GAPS.md. Commit 42e6614db390db7b3e248bc6b383d67e9d00dd3b corrected that path. The connector's combined-status response contained no status entries, and its workflow-run wrapper only returns PR-triggered runs; therefore the repair commit's exact-head Actions state was not independently verified in this cycle. Do not call CI green until the actual Actions page shows both required workflows passing on the final head.

The new files use Research-Sync: main commit trailers. README.md will index this cycle. The large RESEARCH_GAPS.md and WORKLOG.md remain untouched to avoid replacing unseen append-only history; this batch is the focused gap record and the index sync remains debt.

**Next highest-value gate:** verify exact-head prototype/invariant and cold-start CI; then run the pinned-SDK signed-Max-Cut reconstruction before provider-neutral lowering and target-aware simulation. For RG-PDE-SURROGATE-001, run a synthetic known-solution conservative PDE with fixed cell weights and independently computed reference totals before auditing or executing any upstream model.

**Non-claims:** no real-QPU job, no QPU advantage, no new physical law, no material substitution, no accepted commercial bio-oil, no net fusion electricity, no lower WACC and no phone-class physical compression.
