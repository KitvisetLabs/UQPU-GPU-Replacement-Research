# UQCS Living Research Gaps

This file is a permanent backlog for limitations, failed paths, unsupported claims and resource/tool/data blockers. A blocked idea is not discarded; it becomes a falsifiable future research target.

## Status taxonomy
- ACHIEVABLE_NOW
- MODEL_ONLY
- SIMULATION_ONLY
- NOT_YET_DEMONSTRATED
- RESOURCE_BLOCKED
- TOOL_BLOCKED
- DATA_BLOCKED
- CURRENTLY_INFEASIBLE
- ECONOMICALLY_NONVIABLE_CURRENT_ASSUMPTIONS
- PHYSICALLY_INCOMPATIBLE_WITH_KNOWN_LAWS

## Gap record schema
Each item should record: objective; status; evidence; blocker; best current alternative; required breakthrough; measurable unlock criteria; proposed experiment/simulation; dependencies; estimated resources; safety/legal constraints; next review trigger.

## RG-001 — General QPU replacement of all CPU/GPU workloads
**Status:** NOT_YET_DEMONSTRATED
**Evidence:** Current cloud QPUs are heterogeneous and limited; repository market snapshot is modality-aware.
**Blockers:** fault tolerance, logical scale, data loading/output, memory, latency, QEC overhead, economics.
**Current alternative:** semantic workload routing + classical/reversible fallback + narrow quantum-native kernels.
**Unlock criteria:** reproducible end-to-end workload contracts with competitive output quality and measured total cost/task advantage.
**Next work:** build workload-by-workload capability matrix and benchmark harness.

## RG-002 — >=100x end-to-end cost advantage
**Status:** MODEL_ONLY
**Blockers:** no measured complete QPU-vs-competitive-stack benchmark yet; provider cost, QEC and I/O can dominate.
**Current alternative:** inverse cost solver.
**Unlock criteria:** reproducible measured baseline and QPU execution showing >=100x total cost/useful-task.
**Next work:** pricing ingestion + real/simulator benchmark pipeline.

## RG-003 — 100,000,000x cost moonshot
**Status:** CURRENTLY_INFEASIBLE for general workloads / MODEL_ONLY as workload-specific target
**Blockers:** extreme subsystem budgets, QEC, I/O, fabrication, energy and utilization.
**Unlock criteria:** a specific workload with independently reproducible full-stack economics at the target ratio.
**Next work:** use inverse design to identify whether any highly structured workload avoids dominant classical costs.

## RG-004 — Quantum replacement of classical RAM/VRAM/storage bit-for-bit
**Status:** CURRENTLY_INFEASIBLE as a universal direct substitute
**Blockers:** measurement, classical addressability, state preparation, lifetime and I/O constraints.
**Current alternative:** semantic materialization avoidance, hybrid memory, compact classical caches, QMEM research.
**Unlock criteria:** application-level memory/storage contract with lower total cost and required read/write semantics.
**Next work:** memory-contract benchmark suite.

## RG-005 — Biomass direct chemical conversion into Au/Cu/Ag/rare-earth elements
**Status:** PHYSICALLY_INCOMPATIBLE_WITH_KNOWN_LAWS for ordinary chemistry
**Blocker:** chemical reactions do not change nuclear elemental identity.
**Current alternative:** functional substitution, mineral minimization, recovery/recycling, hybrid composites.
**Unlock criteria:** none for ordinary chemistry; any nuclear route requires extraordinary evidence and complete energy/economic analysis.
**Next work:** rank biomass-derived functional substitutes by UQCS component.

## RG-006 — Biomass-derived conductor universally replacing copper/gold/silver
**Status:** NOT_YET_DEMONSTRATED
**Blockers:** conductivity, contact resistance, electromigration, purity, reliability and manufacturing integration.
**Current alternative:** metal-minimizing carbon composites/coatings and low-current/EMI/thermal functions.
**Unlock criteria:** component-specific electrical/reliability requirements met at lower lifecycle cost.
**Next work:** function/property/cost matrix.

## RG-007 — In-house EUV-class production scanner/fab
**Status:** RESOURCE_BLOCKED and NOT_YET_DEMONSTRATED
**Blockers:** source/optics/stage/metrology/vacuum/contamination/process integration, capital, specialist supply chain, safety.
**Current alternative:** architecture/model/simulation; mature-node DUV/direct-write/nanoimprint/external foundry routes where requirements permit.
**Unlock criteria:** subsystem prototypes meeting derived throughput/overlay/yield/economic requirements plus appropriate facilities.
**Next work:** lithography route decision model and fab cost/yield decomposition.

## RG-008 — Parallel autonomous research-agent swarm
**Status:** TOOL_BLOCKED when the execution environment does not expose independent sub-agent orchestration.
**Current alternative:** sequential workstream decomposition with explicit integration review.
**Unlock criteria:** supported multi-agent execution environment with auditable outputs and permissions.
**Next work:** maintain workstream interfaces so parallelization can be adopted later.


## RG-009 — Calibrated lithography/fab economics
**Status:** DATA_BLOCKED / MODEL_ONLY
**Objective:** Select the least-total-cost fabrication route for each UQCS device using calibrated real economics rather than normalized placeholders.
**Blockers:** public tool purchase/service pricing is incomplete; layer-specific mask/resist/etch/metrology costs, multi-patterning penalties, local utility/cleanroom costs, yield-learning curves and supply-chain terms are not fully available.
**Current alternative:** normalized route-selection model anchored to published capability data.
**Unlock criteria:** validated cost/yield inputs for at least one real fab route and one target UQCS device/process flow.
**Proposed experiments:** collect foundry quotes/public cost data where lawful/available; build layer-by-layer process-flow model; sensitivity analysis for yield, throughput, masks, energy and metrology.
**Dependencies:** device requirements, process flow, fab geography, equipment access.
**Safety/legal constraints:** industrial lithography and semiconductor processing require professional facilities and compliance.
**Next review trigger:** availability of calibrated fab economics or foundry/process-partner data.


## RG-010 — Calibrated full fab process flow
**Status:** DATA_BLOCKED / MODEL_ONLY
**Objective:** Replace the generic process skeleton with calibrated process-step data for at least one real semiconductor, photonic or quantum-device flow.
**Blockers:** detailed foundry recipes, per-step cost/yield/energy/cycle-time, rework, scrap, tool utilization, mask amortization, chemistry/gas/water/abatement, facility overhead and packaging/test yield are not fully public.
**Current alternative:** generic MODEL_ONLY process graph with cumulative yield and cost/good-die accounting.
**Unlock criteria:** validated step-level inputs for a real process plus reproducible cost/good-die calculation.
**Proposed experiments:** collect public/partner process data; calibrate defect-density model; add rework/queueing/tool-availability and packaging-yield models.
**Dependencies:** target device, foundry route, lithography route, package architecture.
**Safety/legal constraints:** no unsafe laboratory processing outside appropriate professional facilities.
**Next review trigger:** access to calibrated foundry/process data or a fabrication partner.


## RG-011 — Calibrated device lifetime/useful-task amortization
**Status:** DATA_BLOCKED / MODEL_ONLY
**Objective:** Calibrate how many useful workload tasks each fabricated UQCS device/package can execute over its economic lifetime so manufacturing cost can be amortized into cost/useful-task.
**Blockers:** device lifetime, duty cycle, calibration downtime, failure/repair rates, workload mix, utilization and package replacement rates are architecture- and modality-specific and not yet measured for a UQCS device.
**Current alternative:** explicit scenario parameter `lifetime_useful_tasks_per_device` with sensitivity analysis.
**Unlock criteria:** measured or independently defensible lifetime/utilization data for a specific device + workload deployment.
**Proposed experiments:** collect provider/device reliability and utilization evidence; simulate lifetime distributions; benchmark workload throughput; couple failure/maintenance models to manufacturing amortization.
**Dependencies:** chosen hardware modality, package architecture, workload contract, cooling/control architecture.
**Next review trigger:** availability of measured prototype/cloud/device uptime or reliability data.


## RG-012 — Calibrated cloud-vs-owned crossover
**Status:** DATA_BLOCKED / MODEL_ONLY
**Objective:** Determine workload-specific economic crossover points between renting cloud QPU access and owning UQCS hardware.
**Blockers:** owned UQCS CAPEX/lifetime/utilization are unknown; provider pricing changes; infrastructure/storage charges may be additional; currency conversion is time-dependent; queue/throughput and workload quality must be normalized.
**Current alternative:** dated official-pricing snapshot plus explicit owned-hardware scenario model.
**Unlock criteria:** workload-specific cloud execution evidence + calibrated owned hardware economics in a common currency and common useful-output contract.
**Proposed experiments:** ingest provider cost reports; add FX conversion with dated source; model queue/utilization; benchmark simulator/real-QPU throughput; sensitivity sweep on CAPEX/lifetime/utilization/power.
**Dependencies:** provider adapter maturity, workload contract, hardware architecture, fabrication budget.
**Next review trigger:** new verified provider pricing or measured owned-prototype economics.


## RG-013 — Uncertainty-calibrated deployment crossover
**Status:** DATA_BLOCKED / MODEL_ONLY
**Objective:** Replace scenario-only cloud-vs-owned comparisons with statistically defensible uncertainty intervals and workload-specific crossover distributions.
**Blockers:** owned UQCS CAPEX/lifetime/utilization/power are not measured; provider queue/throughput data and infrastructure add-ons vary; FX changes; workload execution quality and retries are not yet normalized across providers.
**Current alternative:** deterministic parameter sweeps plus explicit low/central/high cost envelopes.
**Unlock criteria:** empirical distributions or independently defensible ranges for provider runtime/cost and owned-hardware lifecycle variables on a defined workload contract.
**Proposed experiments:** ingest real job cost reports, measured runtime/queue/retry data, prototype utilization/power/lifetime data, and dated FX; run Monte Carlo crossover analysis.
**Dependencies:** provider adapters, benchmark harness, real-QPU execution evidence, owned hardware/fabrication model.
**Next review trigger:** first real-QPU cost dataset or prototype lifecycle dataset.


## RG-014 — Real-QPU verification of all cloud adapters
**Status:** RESOURCE_BLOCKED / CREDENTIAL_BLOCKED / NOT_YET_DEMONSTRATED
**Objective:** Promote every software-prepared provider path from dry-run/serialization to simulator and real-QPU verification with reproducible job IDs, normalized results and actual billed cost.
**Blockers:** provider accounts, credentials, quotas, target availability, paid-execution budget and some account-specific direct APIs are not available in the repository environment.
**Current alternative:** concrete adapter layer, health diagnostics, dry-run validation and aggregator routing through Braket/Azure where supported.
**Unlock criteria:** credentialed smoke test for each active route, with explicit paid-execution consent where required, followed by committed job/result/cost evidence.
**Proposed experiments:** simulator-first smoke tests; then bounded real-QPU jobs per provider; validate status/result normalization and actual billing.
**Dependencies:** provider accounts, SDK versions, target access, explicit execution budget.
**Next review trigger:** credentials/account entitlement or newly available free/simulator access.

## RG-015 — Quandela and OQC direct-runtime account integration
**Status:** ACCOUNT_CONFIG_BLOCKED
**Objective:** Complete direct account-specific submission/result paths for Quandela and OQC in addition to current serialization/dry-run readiness.
**Blockers:** account-specific endpoint/RPC/runtime configuration and entitlement are not available in the current execution environment.
**Current alternative:** provider-neutral lowering/dry-run; use supported partner/official access routes when available.
**Unlock criteria:** official account credentials/configuration plus a documented supported submission endpoint/client version.
**Next review trigger:** account access or updated public SDK/API documentation.


## RG-016 — First verified workload win
**Status:** NOT_YET_DEMONSTRATED
**Objective:** Obtain the first reproducible workload where a current cloud-QPU/hybrid path satisfies a defined useful output contract and is compared end-to-end against a competitive classical baseline.
**Blockers:** no credentialed QPU result/cost dataset yet; state preparation, retries, output reconstruction and provider cost must be measured.
**Current alternative:** workload contracts, provider adapters, simulator/dry-run paths and cost models.
**Unlock criteria:** one workload with reproducible classical baseline, authorized cloud execution, validated output quality and measured total cost/useful-task.
**Proposed experiments:** start with combinatorial optimization and structured estimation candidates; simulator first; then smallest bounded cloud execution when credentials/consent exist.
**Dependencies:** Lane A contracts, Lane B adapter verification, Lane C state accounting and Lane F benchmark economics.
**Next review trigger:** simulator benchmark completion or credentialed cloud access.


## RG-017 — Provider throughput-normalized workload economics
**Status:** DATA_BLOCKED / NOT_YET_DEMONSTRATED
**Objective:** Add provider throughput/reset/repetition metrics to workload routing and determine whether higher circuit throughput lowers total cost/useful-task for Priority #1 workloads.
**Blockers:** public throughput metrics are provider-specific and not uniformly defined; workload-level billed runtime and retry behavior are not yet measured across providers.
**Current alternative:** qualitative provider notes plus billing/runtime models.
**Unlock criteria:** common workload benchmark with measured circuit throughput, output quality and billed cost on at least two providers.
**Proposed experiments:** extend HardwareSnapshot with throughput metrics; run simulator/authorized cloud benchmark; normalize by useful accepted outputs rather than raw circuits.
**Dependencies:** Lane A workload contracts, Lane B provider adapters, Lane F benchmark evidence.
**Next review trigger:** first authorized provider benchmark or additional official throughput data.


## RG-018 — Benchmark harness calibration against real classical baselines
**Status:** DATA_BLOCKED / NOT_YET_DEMONSTRATED
**Objective:** Populate Batch 003 benchmark plans with measured competitive CPU/GPU baseline runtime, cost, memory/state movement and output-quality data.
**Blockers:** no current measured baseline dataset is yet committed for the first candidate workload.
**Current alternative:** machine-readable workload contracts, provider-fit model, state accounting and evidence gate.
**Unlock criteria:** reproducible classical baseline artifact for one candidate workload, including hardware/software configuration, runtime, cost/task, input/output and memory/state accounting.
**Proposed experiments:** implement a small exact/heuristic combinatorial-optimization baseline and record hardware/runtime/cost assumptions.
**Dependencies:** Lane A benchmark definition and Lane F economics.
**Next review trigger:** first committed classical benchmark dataset.
