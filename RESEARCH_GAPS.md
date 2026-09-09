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
