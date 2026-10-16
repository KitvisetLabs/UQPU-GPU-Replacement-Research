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


## RG-019 — Competitive optimization baseline implementation
**Status:** NOT_YET_DEMONSTRATED / DATA_BLOCKED
**Objective:** Advance the first optimization workload from a correctness fixture to a competitive CPU/GPU baseline suitable for economic comparison.
**Current artifact:** exact tiny-QUBO fixture plus provenance capture.
**Blockers:** optimized solver selection, representative instance corpus, measured CPU/GPU hardware, memory/energy accounting and normalized cost.
**Unlock criteria:** reproducible Level-2 baseline over the same instance/quality contract used by the QPU path.
**Next experiment:** add an established optimized classical solver and representative scalable instance generator before authorized real-QPU comparison.


## RG-020 — Representative optimization benchmark tiers
**Status:** MODEL_ONLY / NOT_YET_CALIBRATED
**Objective:** Define defensible Max-Cut/QUBO size, density and quality tiers that stress competitive CPU/GPU solvers and remain mappable to target quantum modalities.
**Current artifact:** seeded scalable instance generator and stable benchmark contract.
**Blockers:** representative application corpus, solver-specific scaling data, QPU embedding/circuit resource limits and provider execution constraints.
**Unlock criteria:** published/reproducible tier definitions plus measured competitive classical results and mapped QPU resource requirements.
**Next experiment:** construct small/medium/large tier manifests and benchmark an established optimized classical solver.


## RG-021 — Established optimized solver integration
**Status:** TOOL/DATA_PENDING
**Objective:** Produce reproducible measured results from at least one established optimized classical solver on the same Batch-006 contracts.
**Blockers:** dependency selection/version pinning, reproducible execution environment, hardware provenance and later GPU-capable comparison.
**Unlock criteria:** measured artifacts for small/medium/large tiers with solver/version/hardware/runtime/objective/quality provenance.
**Next experiment:** implement an optional optimized-solver adapter without making it a core dependency.


## RG-022 — Measured OR-Tools benchmark artifacts
**Status:** TOOL/EXECUTION_PENDING
**Objective:** Run the optional OR-Tools adapter on Batch-006 small/medium/large contracts and commit measured benchmark artifacts.
**Blockers:** optional solver dependency is not installed in default CI; measured execution requires a benchmark environment with hardware provenance.
**Unlock criteria:** artifact files recording solver version, contract ID, runtime, objective/quality and hardware context for all selected tiers.
**Next experiment:** install benchmark-optional requirements in a dedicated benchmark job or controlled local/cloud runner and execute the tier manifest.


## RG-023 — Reference objectives/bounds for tier acceptance
**Status:** OPEN
**Objective:** Establish defensible reference objectives or bounds for the versioned small/medium/large MaxCut contracts so acceptance is computed rather than assumed.
**Unlock criteria:** each tier has a provenance-bearing reference/bound and the artifact acceptance flag is derived from OptimizationBenchmarkContract.accepts.
**Next experiment:** use the optimized classical solver path to establish or bound tier objectives, starting with small and medium.


## RG-024 — Certified small/medium optimization references
**Status:** OPEN / TOOL_EXECUTION_PENDING
**Objective:** Produce provenance-bearing EXACT_OPTIMUM or PROVEN_LOWER_BOUND certificates for the current small and medium benchmark contracts.
**Current artifact:** reference-certificate schema and quality-assessment gate.
**Blockers:** optimized solver execution environment and proof/bound extraction for larger tiers.
**Unlock criteria:** matching contract IDs with defensible reference objective/bound, method, source and evidence level.
**Next experiment:** run the optional optimized classical path for small first, then medium; record whether optimality is proven or only a best-known feasible objective.


## RG-025 — Dedicated optimized-reference benchmark environment
**Status:** TOOL_BLOCKED / EXECUTION_PENDING
**Objective:** Execute the Batch-010 reference generator with a pinned OR-Tools version and record real CPU/OS/runtime provenance for small and medium contracts.
**Current artifact:** executable reference generator + manifest schema + regression tests.
**Blocker:** OR-Tools is optional and absent from default CI; benchmark hardware provenance must not be fabricated.
**Unlock criteria:** controlled environment records dependency version, CPU/OS context, contract ID, solver status, runtime, objective and certificate ID; OPTIMAL must be independently reproducible before EXACT_OPTIMUM is used downstream.
**Next experiment:** create/run a dedicated benchmark job with pinned optional requirements, small tier first, then medium.


## RG-025 status update — controlled environment demonstrated
**Status:** PARTIALLY_UNLOCKED / MEASURED_LOCAL
GitHub Actions run 34374036120 successfully installed OR-Tools 9.14.6206 and executed the controlled small/medium reference benchmark on Python 3.12.14 x86_64 Linux.

Measured outcomes:
- small: objective -65.0, FEASIBLE, 30.002208606 s;
- medium: objective -433.0, FEASIBLE, 45.003255759 s.

This satisfies the environment/provenance portion of RG-025 but not the proof-quality portion of RG-024.

**Next unlock:** obtain OPTIMAL status or a rigorous proven lower bound for at least the small contract, while preserving the exact same contract ID.


## RG-026 — Independent SDK, noise and provider validation of QAOA
**Status:** PARTIALLY_UNLOCKED / SIMULATION + DRY_RUN_ONLY
**Objective:** Carry identical QUBOs from exact semantics through independent SDK validation, target ISA, sampled decoding and authorized QPU execution.
**Current evidence:** Batch 012 ideal 3/6/8-qubit simulations, independent dense-definition tests, and existing 32/128/512-variable inspection payloads.
**Blocker:** no independent vendor SDK, hardware routing/calibration, noisy results or QPU job evidence in Batch 012. Direct dense simulation is exponentially expensive.
**Unlock criteria:** same input digest/contract, independently agreeing circuit, documented target and layout, measured counts/quality, full overhead and reference provenance.
**Next experiment:** SDK circuit/statevector cross-check without submitting jobs; then noise and finite-shot quality curves.
**Dependencies:** A/B/C/F, RG-024 proof-quality classical references, authorized provider access/budget.
**Review trigger:** next software batch or a target/calibration becoming available.

## RG-027 — Correlation encoding versus direct QAOA
**Status:** RESEARCH_CANDIDATE / NOT_IMPLEMENTED
**Objective:** Test whether fewer qubits produce lower total cost at matched decoded MaxCut quality.
**Evidence:** primary-source review in docs/BATCH_012_SOURCE_REVIEW.md; capacity-only model gives 6/10/19 qubits for 32/128/512 variables under the two-body construction.
**Blocker:** capacity is not representability, optimizer success or useful-output quality; shot/decoding costs are unknown.
**Unlock criteria:** reproducible encoding/loss/measurement/decoding experiment, same original instance digest and reference, equal evaluation/shot budget, recorded negative outcomes.
**Next experiment:** tiny bounded noiseless comparison, followed by shot noise and reachable-quality investigation.
**Dependencies:** A/C/F and RG-026; no hardware fabrication prerequisite.
**Review trigger:** independent circuit verification completed.


## RG-026 update — independent SDK gate passed on bounded fixtures
Batch 013 Qiskit parsing/statevector verification agrees with Batch 012 to <1.4e-16 on the three selected fixtures, including synthetic routing and decoded measurement layout. Larger tier payloads parse successfully.
**Remaining blocker:** actual provider acceptance, calibrated noise/routing, finite-shot quality and authorized QPU evidence. Synthetic line routing of small grows CX 166→1,043; no physical-duration or cost ratio follows.
**Next experiment:** frozen-circuit finite-shot/noise sensitivity, followed by target-specific calibration.


## RG-026 — Calibrated target-aware QAOA noise evidence
**Status:** DATA/CREDENTIAL_BLOCKED / NOT_YET_DEMONSTRATED
**Objective:** Replace Batch 014's deliberately synthetic readout-only channel with a dated target-specific calibration/noise model while preserving the same circuit, bit mapping and output-quality contract.
**Current evidence:** independent SDK circuit verification plus exact synthetic readout sensitivity for 3/6/8-qubit fixtures.
**Missing:** target calibration snapshot, routed physical circuit, readout assignment data, one-/two-qubit error/coherence assumptions, drift timestamp and mitigation cost.
**Unlock criteria:** reproducible target-aware simulation tied to an identifiable backend calibration snapshot; then an authorized bounded QPU run with job/result/cost provenance.
**Evidence boundary:** synthetic sensitivity cannot be promoted to REAL_QPU or provider performance evidence.


## RG-032 — Degree-81 odd-parity QSP phase synthesis
**Status:** TOOL_BLOCKED / NEGATIVE_RESULT_REPRODUCED
**Objective:** Synthesize and independently reconstruct a full 82-phase QSP response for the frozen degree-81 polynomial fingerprint `4364297169fe219da396c1d663680f474508a03afed93e321dc8e9d8f0bad13a`.
**Evidence:** In an isolated Python 3.12.14 environment, pinned `qsppack==0.3.0` Newton execution raises `ValueError: could not broadcast input array from shape (41,) into shape (42,)`. Source inspection identifies a 41-versus-42 derivative/Jacobian allocation mismatch. QSPPACK also imports undeclared `sympy`; the repository now pins it explicitly.
**Why still open:** this is an implementation failure, not a proof of mathematical infeasibility. No phase vector exists to reconstruct or lower.
**Best current alternative:** preserve the exact coefficients and contract while testing a minimal odd-parity Jacobian correction or an independent maintained implementation. FPI at 2,000 iterations returned error about 5.5491 and LBFGS raised a separate exception, so neither is accepted.
**Unlock criteria:** a declared implementation returns 82 finite phases meeting its `1e-12` residual criterion; repository-owned 2x2 products independently reproduce the frozen polynomial within a predeclared tolerance; convention mapping is explicit.
**Required tool/data:** versioned synthesis source, deterministic environment, coefficient fingerprint, phase list, solver diagnostics and independent reconstruction grid.
**Dependencies:** QOS-AUDIT-010B3, Lane A/F; B/C/D/G remain downstream.
**Next experiment:** expose the odd-parity Jacobian dimensional contract on a small known polynomial, then test the smallest auditable correction or independent solver.
**Review trigger:** first independently reconstructable phase vector or a rigorous mathematical infeasibility certificate.

## RG-032 status update — numerical phase/reconstruction gate passed
**Status:** PARTIALLY_UNLOCKED / SIMULATION
**Date:** 2026-09-25

Pinned `qsppack==0.4.0` returned 82 finite phases for the unchanged degree-81
coefficient fingerprint, reporting Newton residual `2.6281060661048627e-15`.
A repository-owned 2x2 product independently reconstructed the response on
20,001 grid points with maximum real residual `1.2667644710973036e-13` and
maximum unitarity residual `1.554312234475219e-14`. The phase fingerprint is
`268d1809a8d88309df001d2c63b1f78ba5101d2b9e254c304b014ba4e8397445`.

**Why still open:** finite-grid numerical agreement is not a formal uniform
error certificate, independent phase-solver agreement, QSVT workload result,
provider execution or economic evidence. The `0.3.0` failure remains a retained
negative control, not evidence against mathematical feasibility.

**Next experiment / unlock:** QOS-AUDIT-010B4 must map the phases into a bounded
matrix/QSVT fixture, independently verify transformed singular values and
conventions, account for resources/I/O, and obtain second-implementation or
interval/error assurance before provider or hardware promotion.

## RG-032 status update — bounded matrix/QSVT convention passed
**Status:** PARTIALLY_UNLOCKED / SIMULATION
**Date:** 2026-09-26

QOS-AUDIT-010B4 constructed a non-diagonal Hermitian 2x2 contraction inside a
4x4 one-ancilla block encoding. The 82 phases produced the expected real
polynomial transform with maximum block residual `5.440092820663267e-15` and
transformed-unitary residual `1.021405182655144e-14`. A perturbed phase fails.

**Why still open:** this is dense numerical validation on a constructed fixture.
There is no formal uniform certificate, independent SDK circuit, accepted
workload, target calibration, provider execution or economic comparison.

## RG-033 — Independent SDK and explicit QSVT circuit/resource reproduction
**Status:** OPEN / TOOL_EXECUTION_PENDING
**Objective:** Reproduce QOS-AUDIT-010B4 in an independent pinned SDK and export
an explicit provider-neutral circuit/resource artifact.
**Current artifact:** repository-owned 4x4 dense block-encoding/QSVT certificate
plus model-only query, ancilla and byte ledger.
**Missing:** SDK convention mapping; decomposed one-/two-qubit gates; depth;
serialized bytes; measured host runtime/memory; independent output agreement.
**Unlock criteria:** unchanged fixture/phase contract, independent projected-block
agreement within `2e-12`, explicit circuit and reproducible resource provenance.
**Dependencies:** Lane A/B/C/F; D/G consume the result only after this gate.
**Next experiment:** QOS-AUDIT-010B5 pinned SDK reconstruction and serialization.
**Review trigger:** independently executable circuit artifact or a documented SDK
convention blocker.

### RG-033 update — independent SDK circuit gate passed, scalable oracle remains open
**Status:** PARTIALLY_UNLOCKED / SIMULATION_INDEPENDENT_SDK_CHECK
**Date:** 2026-10-16

Pinned Qiskit 2.5.2 independently reproduced QOS-AUDIT-010B4 with repository-vs-SDK residual `1.3429224847042392e-15`, decomposed-vs-repository residual `9.147089449167083e-14`, depth 811, 162 CX gates and 25,234 serialized OpenQASM 2 bytes. GitHub Actions provenance is bound in `benchmarks/results/cycle008-delta03-qos-audit-010b5-qiskit.json`.

**Why still open:** the 4x4 signal unitary is supplied as a dense two-qubit instruction. This proves the bounded convention/decomposition, not a scalable workload oracle or block encoding. No target, layout, routing, schedule, calibration, shots, execution ID, energy or bill exists.

**Next experiment / unlock:** construct the signal unitary from an explicit frozen workload oracle, demonstrate resource scaling, then transpile against a dated backend target/snapshot while keeping paid submission disabled.

### RG-033 update — workload-derived algebraic LCU contract passed; circuit remains open
**Status:** PARTIALLY_UNLOCKED / SIMULATION_ALGEBRAIC_BLOCK_ENCODING_CONTRACT
**Date:** 2026-10-16

QOS-AUDIT-010B6 replaces the supplied dense signal unitary at the operator-contract layer with an explicit ER6 MaxCut LCU: one identity plus nine signed `ZZ` terms, `alpha=9`, six system qubits, four select qubits and 16 padded select states. Exhaustive comparison over all 64 basis states passed with maximum projected-diagonal residual `1.1102230246251565e-16`; provenance and mutation checks are executable.

**Why still open:** PREP and SELECT have not been synthesized. Gate count, depth, QROM realization, precision dependence, serialized bytes, target mapping, runtime, energy and cost therefore remain unknown. Published sparse-QROM bounds are not applied as measured resources. This result is neither a scalability proof nor QSVT/provider execution.

**Next experiment / unlock:** QOS-AUDIT-010B7 provider-neutral PREP/SELECT synthesis, pinned independent-SDK projected-operator reconstruction and measured decomposition scaling, followed by dated target-aware no-submit transpilation.

### RG-033 update — PREP/SELECT circuit contract implemented; hosted SDK gate pending
**Status:** PARTIALLY_UNLOCKED / SIMULATION_PROVIDER_NEUTRAL_CIRCUIT_CONTRACT
**Date:** 2026-10-16

QOS-AUDIT-010B7 fixes a ten-qubit `PREP -> SELECT -> PREP_DAGGER` circuit for the unchanged ER6 LCU. It commits all 16 PREP amplitudes, ten SELECT branches, six padded identity addresses, register endianness, the expected 64-state projected diagonal and fail-closed provider authorization. Core construction, artifact and mutation tests pass.

**Why still open:** the optional pinned SDK has not yet executed on this commit. No decomposed counts, depth, bytes or independent projected-operator residual may be accepted until hosted Qiskit produces them. The circuit remains generic, not target-aware, fault-tolerant, executed or economic evidence.

**Next experiment / unlock:** run Qiskit 2.5.2 on the exact commit, require projected and decomposed residuals <= `2e-12`, persist the provenance-bound result, then integrate one verified block-encoding query with the frozen QSVT sequence. Target-aware no-submit transpilation follows only after that composition.

**First hosted result:** run #731 reproduced the logical projected block (`5.397791942558855e-14`) but the generic decomposition differed by an apparent global phase near pi: raw projected residual `1.5555555555555465` and raw full-operator residual `1.9444444444443676`. This is a failed raw matrix-equivalence gate, not provider/hardware failure. The repair records raw and phase-aligned residuals separately; controlled/QSVT composition remains blocked until the relative-phase convention is explicit.

**Second hosted result:** run #732 measured phase offset `-9.726339682289133e-14` rad while the same large raw residuals remained, disproving the single-global-phase diagnosis. The next repair replaces synthesized `Z.control(4)` with an explicit five-qubit `MCPhase(pi)` for each conditional Pauli-Z phase and restores raw matrix equality as the acceptance gate.

**Third hosted result / circuit gate passed:** commit `6a7af8a94929ff5eae786144b2dbd6ad1cc88a4b`, run #733. Explicit `MCPhase(pi)` SELECT passed raw projected/full residuals `2.870763895486062e-14`/`7.031200573645607e-14`. Generic decomposition measured 994 CX, 1,845 RZ, 312 SX, 42 X, depth 2,300 and 45,937 OpenQASM 2 bytes on ten logical qubits. RG-033 remains open because the 81-query QSVT composition, target-aware mapping, shots, provider execution, energy and accepted-task economics are absent.

**Next experiment:** integrate one verified PREP/SELECT query into the frozen QSVT phase convention and test the composed projected transform before multiplying generic resources by 81. A simple multiplication is a bound/proxy, not a synthesized end-to-end circuit.

### RG-033 update — bounded one-query projector-phase composition implemented
**Status:** PARTIALLY_UNLOCKED / SIMULATION_PROVIDER_NEUTRAL_ONE_QUERY_CONTRACT
**Date:** 2026-10-17

QOS-AUDIT-010B8 fixes `P(phi_0) U_ER6 P(phi_1)` using the frozen phase fingerprint
and the four-select-qubit projector `Pi=|0000><0000| tensor I`. Local pinned
Qiskit 2.5.2 passed the projected fragment at `5.6158631957729706e-14`, the
decomposed projected fragment at `3.6061746050468526e-14`, and the raw full
operator at `7.75091532099517e-14` against `2e-12`.

**Why still open:** exact-commit hosted reproduction and provenance persistence
are pending. One query does not establish the alternating recurrence or final
degree-81 transformed block. The local 1,034 CX/depth-2,390 generic result is
not target, fault-tolerant, QPU, energy or economic evidence.

**Next experiment / unlock:** require hosted raw-matrix agreement; persist its
certificate; then verify two queries and three projector phases against an
independently assembled matrix. Only after recurrence agreement should the full
81-query circuit be synthesized. Never substitute count multiplication for
end-to-end verification.

**Hosted gate passed:** commit `9d7e5d761fc8ddf18a0fec4a9564ce836e617e96`,
project run #735, Qiskit job `117173121884`. Raw logical projected, decomposed
projected and full-operator residuals were `5.4646887015828417e-14`,
`3.6424960685225636e-14` and `7.593998529073269e-14`. The certificate is bound
to artifact `12072606869`; provider jobs/shots are zero and cost/energy null.
RG-033 remains open at the two-query recurrence and full composed transform.

### RG-033 update — two-query recurrence implemented
**Status:** PARTIALLY_UNLOCKED / SIMULATION_INDEPENDENT_SDK_TWO_QUERY_CHECK
**Date:** 2026-10-17

QOS-AUDIT-010B9 implements `P0 U_ER6 P1 U_ER6 P2` and compares it with an
independently assembled 1024x1024 operator. Local Qiskit 2.5.2 passed logical
full/projected residuals `1.487709209519727e-14`/`6.4373790806034785e-15` and
decomposed full/projected residuals `1.555229087579905e-13`/
`1.4686258498911463e-13` against `2e-12`.

**Hosted checkpoint:** commit `2bf019cf21efd43ec7ae9f8196ec03e5734e7945`,
project run #737 and Qiskit job `117198147300` reproduced all four raw residuals
below `2e-12`; certificate artifact `12075997394` is persisted. Provider
jobs/shots are zero and cost/energy null.

**Why still open:** the independent reference reuses the already verified ER6
block primitive, and two-query ordering does not
yet prove that the projected recurrence equals the intended scalar QSP response
for every workload eigenvalue. It is not full degree-81 synthesis.

**Next experiment / unlock:** an independent 2x2 spectral-sector recurrence
over all 64 ER6 eigenvalues. Only
after that passes should a bounded prefix ladder (for example 3 and 5 queries)
be used to test recurrence scaling and memory limits.

## RG-034 — Identifiability-certified equation-discovery fixture
**Status:** OPEN / SYNTHETIC_FIXTURE_PENDING
**Objective:** Distinguish `NOT_YET_SOLVED` from `LOCALLY_NON_IDENTIFIABLE` and `EXPERIMENT_CLASS_EXHAUSTED` before an AI-generated equation can advance.
**Current evidence:** Cycle 008 requires explicit quantity kind/unit/dimension vectors and separate train/held-out hashes. The 2026-10-15 literature watch identifies deterministic sensitivity-rank/null-space and experiment-class exhaustion as the next bounded control.
**Missing:** frozen confounded ODE, two observation protocols, known null direction, exact split commitments, counterexample search and independently checked rank/exhaustion result.
**Best current alternative:** keep all generated equations at `MODEL_ONLY` and reject test leakage or dimension imbalance.
**Unlock criteria:** repository code recovers the known null direction under the non-identifiable protocol, removes it under the discriminating protocol, rejects test-set selection, and issues exhaustion only after enumerating the declared bounded design class.
**Required tool/data:** synthetic ODE generator, deterministic automatic differentiation or verified finite differences, exact protocol manifest, fit/selection/test hashes and numerical-rank sensitivity analysis.
**Dependencies:** FND-006, EQN-001–006, INV-035, Lane F.
**Next experiment:** implement the two-protocol confounded-parameter fixture and perturbation/counterexample tests.
**Review trigger:** reproducible local certificate plus exact-commit CI.

## RG-035 — Autonomous handoff and commit-to-main reconciliation coverage
**Status:** PARTIALLY_UNLOCKED / PROCESS_VERIFICATION
**Date:** 2026-10-16
**Objective:** Make a memoryless agent able to resume from canonical `main`, and detect substantive commits whose research details are not synchronized to main.
**Current evidence:** machine-readable A–I handoff manifest; deterministic cold-start validator; all-push GitHub Actions workflow; branch-specific `Research-Sync` commit trailer contract; focused positive/negative tests.
**Evidence boundary:** the audit validates repository structure and declared boundaries. It does not verify scientific claims, automatically merge branches, enumerate inaccessible forks, or prove that historical commits are all reconciled.
**Missing:** registered-branch inventory, source-SHA-to-main mapping ledger, safe GitHub API reconciliation, deduplicated sync-debt reporting and protected-branch review of any automated write.
**Unlock criteria:** exact-commit CI passes; a read-only reconciler enumerates accessible registered branches/PRs, matches every substantive source SHA to a detailed main record, emits deterministic debt, and passes fixtures for squash/rebase, force-push, inaccessible fork and ledger-recursion cases.
**Next experiment:** implement a read-only branch/PR snapshot artifact and offline reconciliation fixtures; keep automatic main writes disabled until permissions, conflict handling and review are proven.
**Dependencies:** H/F governance, A–I manifest, GitHub read permissions.
**Review trigger:** first exact-commit cold-start CI plus reconciler fixture.
