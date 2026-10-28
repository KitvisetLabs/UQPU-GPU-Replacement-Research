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

### RG-033 update — all 64 spectral sectors checked
**Status:** PARTIALLY_UNLOCKED / SIMULATION_INDEPENDENT_SDK_SPECTRAL_SECTOR_CHECK
**Date:** 2026-10-17

QOS-AUDIT-010B10 reduces every ER6 workload eigenvalue to an independent 2x2
Hermitian-involution recurrence. All 64 sectors and seven unique normalized
eigenvalues were checked. Explicit matrix multiplication agrees with the closed
form to `2.7755575615628914e-16`; local pinned Qiskit projected logical and
decomposed diagonal residuals are `1.4004310501204187e-13` and
`1.06356642317011e-13`, below `2e-12`. Projected off-diagonal leakage is also
below threshold.

**Hosted checkpoint:** implementation commit
`14970dc30e5764799ec8aa962aa72eff6fd81a18`, project run #739 and Qiskit job
`117221194290` reproduced all 64 sectors below `2e-12`. Artifact `12078412811`
is persisted with commit/run/job provenance. It records `81.849786336 s` host
runtime, `119178303 bytes` traced peak host memory and `94965 bytes` serialized
OpenQASM 2; provider jobs/shots remain zero and cost/energy null.

**Why still open:** this is a two-query bounded fixture. It does not establish
degree-81 synthesis, stable scaling, target feasibility, accepted workload
quality, energy, cost or advantage.

**Next experiment / unlock:** 3- and 5-query prefixes using the same sector
contract. Record measured runtime, peak host
memory, serialized bytes and raw residuals; stop on tolerance or resource
failure instead of extrapolating to 81 queries.

### RG-033 update — bounded 3/5-query contract implemented
**Status:** PARTIALLY_UNLOCKED / SIMULATION_INDEPENDENT_SDK_BOUNDED_PREFIX_CHECK
**Date:** 2026-10-17

QOS-AUDIT-010B11 evaluates three- and five-query prefixes across all 64 ER6
workload sectors with independent matrix and right-to-left state recurrences.
The maximum residual is `3.0436364816617974e-16` against `2e-12`. Per-prefix
hosted ceilings are frozen at `900 s`, `750,000,000` traced bytes and `500,000`
serialized OpenQASM 2 bytes, with stop-on-first-failure semantics.

**Why still open:** the local environment lacks the pinned optional Qiskit
stack, and the contract alone does not measure logical/decomposed circuit
resources. It remains neither degree-81 synthesis nor accepted workload,
target, provider, energy, cost or advantage evidence.

**Next experiment / unlock:** reproduce the unchanged contract in the isolated
hosted Qiskit job, persist raw per-prefix residual/runtime/memory/bytes with
commit/run/job/artifact provenance, and do not advance if either prefix fails.

**Hosted checkpoint:** implementation commit
`39fa6f99d6cc512555e5613deb182ed79d054f34` passed both prefixes in project
run #741. Three queries measured `203.655504116 s`, `84,791,827` traced bytes,
`141,919` QASM bytes, 3,062 CX and depth 7,076; five queries measured
`342.837898385 s`, `85,003,559` traced bytes, `235,806` QASM bytes, 5,090 CX
and depth 11,762. Maximum raw spectral residuals were
`1.7456727791002127e-13` and `2.7613238692498116e-13`, below `2e-12`.
Artifact `12087010676` is provenance-bound. Jobs/shots are zero and cost/energy
null.

**Revised next experiment / unlock:** preregister the next bounded prefix from
the measured 1/2/3/5-query series, including a resource-growth falsifier and
hard stop. Do not infer degree-81 feasibility from the observed near-linear
generic gate counts.

### RG-033 update — eight-query resource-growth falsifier preregistered
**Status:** PARTIALLY_UNLOCKED / MODEL_ONLY PREREGISTRATION
**Date:** 2026-10-17

QOS-AUDIT-010B12 freezes the next prefix at eight queries using only the
persisted 1/2/3/5-query certificates. The robust affine planning model sets
model-rejection ceilings of 8,132 CX, depth 18,791, decomposed size 26,129 and
376,658 serialized QASM bytes. Runtime and traced memory are diagnostic-only
because hosted runner variance is uncontrolled; absolute stops remain 900 s,
750,000,000 bytes and 500,000 QASM bytes. Raw residual tolerance remains
`2e-12` across 64 sectors and seven unique eigenvalues.

**Why still open:** this artifact is a preregistration and contains no executed
eight-query circuit, target mapping, provider run, energy, cost, accepted useful
output or degree-81 evidence.

**Next experiment / unlock:** run the unchanged eight-query contract in the
isolated pinned-Qiskit job. Persist raw residuals/resources with exact
commit/run/job/artifact provenance. A deterministic-limit exceedance rejects
the growth model; a residual or absolute-limit exceedance stops the ladder.
Neither outcome may be repaired by changing thresholds after execution.

### RG-033 update — eight-query execution path implemented
**Status:** IMPLEMENTED / HOSTED_EXECUTION_PENDING
**Date:** 2026-10-17

QOS-AUDIT-010B13 validates the preregistration before constructing the exact
eight-query prefix, checks independent 2x2 recurrence order, evaluates all 64
projected sectors in pinned Qiskit and records the frozen deterministic and
absolute gates separately. The dedicated CI job uploads an artifact even on
failure and has a 25-minute timeout.

**Why still open:** no hosted certificate exists yet. Local absence of pinned
Qiskit makes execution `TOOL_BLOCKED`; pure recurrence/contract tests pass.
There is still no target-aware schedule, real-QPU run, energy/cost measurement,
accepted transformed workload or degree-81 evidence.

**Next experiment / unlock:** execute the exact PR commit, preserve either
model acceptance or rejection, bind the raw artifact to commit/run/job/digest,
and stop on residual, absolute-resource, basis or authorization failure.

### RG-033 update — eight-query hosted checkpoint accepted
**Status:** PARTIALLY_UNLOCKED / SIMULATION_INDEPENDENT_SDK_BOUNDED_PREFIX_CHECK
**Date:** 2026-10-17

Exact source commit `b1ffc1de9c2a0b02d80886e548d1d4fe6be17213`
passed all ten jobs in project run #745. The eight-query certificate records a
maximum raw residual of `5.491292372342266e-13` against `2e-12`, 8,132 CX,
depth 18,791, size 26,129, 376,644 QASM bytes, `525.450692110 s` host runtime
and 85,858,826 traced bytes. The preregistered deterministic model and absolute
stops both passed; the QASM model had only 14 bytes of headroom. Artifact
`12094185194` is bound to run/job/source/merge/digest provenance. Provider
jobs/shots remain zero and cost/energy null.

**Why still open:** this is generic SDK simulation and serialization, not a
dated target schedule, real-QPU execution, accepted transformed workload,
degree-81 synthesis, energy/cost evidence or advantage. Host runtime/memory are
shared-runner diagnostics.

**Next experiment / unlock:** use the measured point to preregister the next
bounded boundary test below the unchanged 900-second, 750,000,000-byte and
500,000-QASM-byte absolute stops. Preserve any model failure; do not infer
degree-81 feasibility or submit to a provider.

### RG-033 update — ten-query boundary preregistered
**Status:** PARTIALLY_UNLOCKED / MODEL_ONLY PREREGISTRATION
**Date:** 2026-10-17

QOS-AUDIT-010B14 binds the provenance-bearing 1/2/3/5/8-query measurements and
scans 9–81 queries without changing absolute stops. Ten queries is the largest
planning-eligible prefix: conservative upper envelopes are 470,551 QASM bytes,
716.865 seconds and 187,377,521 traced bytes. Eleven queries is blocked by a
517,495-byte QASM envelope. The contract digest is
`47ad5e62cbae93fb613fd3d3a1a3a464f09c06b6eb3e54b2a5e3fabcc39795aa`.

**Why still open:** this is a frozen planning contract, not a ten-query run,
target mapping, accepted transformed workload, degree-81 synthesis, real-QPU,
energy, cost or advantage evidence.

**Next experiment / unlock:** implement and run the unchanged ten-query prefix
in the isolated pinned-Qiskit job. Persist success or failure with raw
residual/resource and commit/run/job/artifact provenance. Eleven queries stays
blocked unless a separately evidenced representation change reduces measured
serialization without relaxing useful-output or evidence contracts.

### RG-033 update — ten-query execution path implemented
**Status:** HOSTED_ACCEPTED / ELEVEN_QUERY_BLOCKED
**Date:** 2026-10-17

QOS-AUDIT-010B15 consumes the immutable B14 digest and implements ten block
queries, eleven projector phases, independent 2x2 recurrence, all-64-sector
logical/decomposed comparisons, generic-basis accounting and separate
model/absolute/residual/authorization gates. The local base environment lacks
the pinned SDK, so the result remains `TOOL_BLOCKED` until exact-commit CI runs
`qiskit==2.5.2`.

**Unlock criteria:** persist a success-or-failure artifact with raw residuals,
counts, depth, size, QASM bytes, runtime, traced memory and exact
commit/run/job/artifact provenance. Eleven queries remains blocked regardless.

**Hosted result:** PR run #754 job `117404874404` passed. Maximum raw residual
was `6.798833937237839e-13`; resources were 10,160 CX, depth 23,477, size
32,645, 470,529 QASM bytes, `668.503379153 s` runtime and 86,352,015 traced
bytes. Artifact `12102800531` is provenance-bound. RG-033 remains open for
degree-81 feasibility, target-aware execution, accepted useful output,
energy/cost and advantage. The bounded prefix ladder now stops at ten.

## RG-034 — Identifiability-certified equation-discovery fixture
**Status:** OPEN / SYNTHETIC_FIXTURE_PENDING
**Objective:** Distinguish `NOT_YET_SOLVED` from `LOCALLY_NON_IDENTIFIABLE` and `EXPERIMENT_CLASS_EXHAUSTED` before an AI-generated equation can advance.
**Current evidence:** Cycle 008 requires explicit quantity kind/unit/dimension vectors and separate train/held-out hashes. The 2026-10-15 literature watch identifies deterministic sensitivity-rank/null-space and experiment-class exhaustion as the next bounded control.
The 2026-10-17 AI-generated-mathematics watch adds a
`MATHEMATICAL_INSTRUMENT_CANDIDATE` intake stage: extracted tools remain below
`THEORY` until assumptions, antecedents, counterexamples and independent proof
or proof-assistant checks pass.
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

### RG-033 update — saved-target identity gate implemented
**Status:** HOSTED_IDENTITY_ACCEPTED / TRANSPILATION_NOT_STARTED
**Date:** 2026-10-18

QOS-AUDIT-010B16 binds the accepted ten-query certificate digest to a
deterministic structural fingerprint of pinned `FakeKingston`. It records SDK
versions, target identity, qubit count, operation names, directed coupling
edges and instruction-signature counts while enforcing zero credentials, live
service, network submission, jobs, shots and paid authority. Exact-commit CI
job `117468829435` persisted artifact `12109234748`: 156 qubits, 352 directed
CZ declarations, one variable-width IfElseOp declaration and canonical digest
`88419f3cb82b6d2bf21cb40ef59ae3ac9fbca0c37b0425bd0d8f561cb905ca4e`.
Two failed hosted attempts are retained as tooling negatives: Qiskit uses both
`qargs=None` and class-level property descriptors for variable-width control
flow. Neither failure was evidence of target infeasibility.

**Unlock criteria:** bind the persisted digest in a separate preregistration
for bounded no-submit target transpilation. A saved
target is not live calibration; routed resources, schedule, fidelity, accepted
output, energy, cost and advantage remain open.

### RG-033 update — saved-target no-submit routing resource gate accepted
**Status:** HOSTED_RESOURCE_ACCEPTED / USEFUL_OUTPUT_QUALITY_OPEN
**Date:** 2026-10-18

QOS-AUDIT-010B17 froze the ten-query source certificate, FakeKingston identity,
Qiskit pins, layout 0–9, basic router, seed and hard stops before execution.
QOS-AUDIT-010B18 then measured 41,798 CZ, depth 86,783, size 187,979,
2,267,976 QASM2 bytes, 9.489 s host runtime and 51,277,778 traced bytes with
ten active physical qubits. Every emitted instruction conforms to the saved
target. Job `117517795643`, run #770 and artifact `12116198038` are bound to
source commit `b69f8772ac7db23e6fdcd2f4571e7308a10c56b8`. Provider jobs/shots are
zero and energy/cost null.

**Why still open:** the saved snapshot is not live calibration, and instruction
conformance does not independently establish routed logical equivalence,
accepted workload quality, physical fidelity, schedule, energy, cost or
advantage. Dense 156-qubit operator construction is not an acceptable verifier.

**Next experiment / unlock:** construct a scalable independent semantics check
using logical-token/layout tracking, tensor-network/light-cone comparison or
another preregistered method on the same useful-output contract. Preserve a
counterexample or capacity failure; only afterward consider saved-snapshot
noise/schedule diagnostics. No live service or provider submission.

### RG-033 update — bounded routed-semantics probes preregistered
**Status:** PREREGISTERED / EXECUTION_PENDING / FULL_EQUIVALENCE_OPEN
**Date:** 2026-10-18

QOS-AUDIT-010B19 binds the accepted logical and routing certificate digests,
the exact active wire set, final-layout inversion rule, four deterministic
product-state probes, `1e-9` phase-aligned residual threshold, state-norm and
host-resource stops, and zero-provider authorization before execution.

**Evidence boundary:** passing all probes would be a bounded same-SDK dynamic
check, not a proof of full operator equivalence or an independent-SDK result.
The unlock remains incomplete until the runner executes and, if needed, a
stronger tensor-network, light-cone or independently implemented verifier
covers residual risk. Eleven queries, live calibration and provider execution
remain blocked.

### RG-033 update — routed-semantics runner implemented
**Status:** BOUNDED_PROBES_ACCEPTED / FULL_EQUIVALENCE_OPEN
**Date:** 2026-10-18

QOS-AUDIT-010B20 now reproduces the frozen saved-target route, rejects active
wire drift, compacts only physical wires 0–9, checks the final-layout
bijection, explicitly restores logical amplitude ordering and computes the
four phase-aligned residuals with the preregistered norms, runtime, memory and
zero-provider stops. Unit tests cover bit permutation, non-bijection rejection,
global phase and fail-closed residual evaluation.

Exact-commit job `117572935487` passed all four probes. Phase-aligned L2
residuals were `2.234e-13`, `3.163e-13`, `3.922e-13` and `3.288e-13`; final
layout `[8,7,6,5,0,1,2,3,4,9]` was explicitly inverted. Runtime was 83.694 s
and traced peak memory 48,643,558 bytes. Artifact `12123870315` retained the
certificate; jobs/shots remained zero and cost/energy null.

**Still missing:** an independent implementation or stronger scalable
equivalence method. This passing certificate is a finite same-SDK probe result
only; full operator and independent-SDK equivalence remain false.

### RG-033 update — independent routed-probe experiment preregistered
**Status:** PREREGISTERED / EXECUTION_PENDING / FULL_EQUIVALENCE_OPEN
**Date:** 2026-10-18

QOS-AUDIT-010B21 binds the Delta 18 certificate digest, Qiskit 2.5.2,
Qulacs 0.6.14, the observed layout, active wires, four probes, explicit gate
matrices, `1e-9` residual stop and four mandatory counterexamples. Unknown
operations, gate-set drift, missed counterexamples or authorization signals
fail closed.

**Still missing:** implementation and exact-commit execution. A future pass is
independent-simulator bounded-probe evidence, not full operator equivalence,
hardware fidelity, cost, energy or advantage.

### RG-033 update — independent routed probes passed locally
**Status:** BOUNDED_INDEPENDENT_SIMULATION_ACCEPTED / HOSTED_CONFIRMATION_PENDING / FULL_EQUIVALENCE_OPEN
**Date:** 2026-10-18

QOS-AUDIT-010B22 translated all 187,979 routed operations through explicit
matrices into Qulacs 0.6.14. The four phase-aligned residuals were between
`2.218e-13` and `3.945e-13`, below the frozen `1e-9` limit. Runtime was
48.289 s and traced peak memory 101,543,937 bytes. Reversed RZ, perturbed SX,
altered CZ mapping and omitted layout inversion were rejected with residuals
from `6.995e-4` to `1.414`; jobs/shots remained zero.

The exact reversal of CZ endpoint order was correctly null because CZ is
symmetric. This is retained as a negative result, not hidden or converted to a
false signal. Exact-commit hosted confirmation and a stronger scalable
equivalence verifier remain open. Four finite probes are not full operator
equivalence, hardware fidelity or accepted workload advantage.

### RG-034 — Real-QPU transition lacks explicit authorization and accounting
**Status:** PREREGISTERED / EXECUTION_DISABLED
**Date:** 2026-10-19

QOS-AUDIT-010B23 binds the Delta 20 certificate and separates no-submit
preflight from later authorized execution. The contract requires a fresh
target snapshot and exact-circuit digest, target conformance, frozen shots,
quality and cost ceilings, same-provider pricing/result provenance, full
latency/host/data-movement accounting and cost per accepted useful output.

**Still missing:** one specified provider/target, completed no-submit preflight,
explicit user consent, credentials, bounded jobs/shots/cost and an execution
record. The execution phase is disabled; this artifact is not QPU evidence or
permission to submit a free or paid job.


### RG-QAOA-PARITY-001 — matched higher-order parity QAOA evidence
**Status:** OPEN / NOT_YET_DEMONSTRATED FOR UQPU  
**Date:** 2026-10-27  
**Primary owner:** Lane A; evidence/integration owner Lane F  
**Source:** Weidinger et al., Higher-order Parity Constraints for Quantum Approximate Optimization, arXiv:2610.26381, submitted 2026-10-19; manuscript dated 2026-10-21.  
**Detailed record:** docs/RESEARCH_GAP_QAOA_PARITY_MATCHED_EVIDENCE_2026-10-27.md  
**Literature watch:** docs/literature_watch/2026-10-27-higher-order-parity-qaoa-equal-budget-evidence.md

The external preprint reports signed-Max-Cut simulations and IBM Heron experiments on selected sparse graphs. Higher-order parity constraints improved reported optimum hits under the paper's conditions but increase two-qubit depth and physical-qubit demand. UQPU has not independently reproduced the result. A new matched-comparison contract records workload/test/acceptance/reference hashes, provider/target/configuration, equal shots and optimizer budget, billable usage, latency/throughput, state/I/O/transfer/memory, retries, reconstruction, energy where measured and full accepted-task cost. No paid QPU job or advantage claim is accepted.

**Unlock:** independent parity mapping and decoder verification on exact small instances; frozen disjoint train/test graph manifest; equal-budget target-aware simulation; then only authorized hardware, with same-provider pricing/calibration provenance and complete cost per accepted useful output.

### RG-QROM-SPARSE-001 — sparse coherent data-access cost
**Status:** OPEN / EXTERNAL THEOREM NOT YET MAPPED TO A UQPU WORKLOAD  
**Date:** 2026-10-27  
**Primary owner:** Lane C; Lane A compiler and Lane F evidence integration  
**Source:** Li et al., Optimal T Counts under Sparsity: from QROM to State Preparation and Block Encoding, arXiv:2607.28260v2, revised 2026-10-01.  
**Detailed record:** docs/RESEARCH_GAP_SPARSE_QROM_MEMORY_COST_2026-10-27.md  
**Literature watch:** docs/literature_watch/2026-10-27-sparse-qrom-state-preparation-lower-bounds.md

The paper proves tight worst-case T-count bounds for sparse QROM in a fixed Clifford+T circuit model and derives sparse state-preparation/block-encoding bounds. This is a circuit-resource lower-bound reference, not a physical memory, wall-clock, energy or dollar-cost theorem. The UQPU gap is to freeze a workload's address width, data width, sparsity, precision and address-promise semantics, then compare dense/direct and sparse routes with preprocessing, ancillas, depth, storage, I/O and output costs included.

**Unlock:** exact small-instance verification, held-out sparsity patterns, explicit MODEL_ONLY/SIMULATION_ONLY evidence labels and end-to-end resource accounting. A promised-address bound may not be used unless the workload contract guarantees the promise.


### RG-STATEPREP-SPARSE-001 — sparse state-preparation theorem model alignment
**Status:** OPEN / MODEL_ALIGNMENT_REQUIRED / MODEL_ONLY  
**Date:** 2026-10-27  
**Primary owner:** Lane A; Lane C state/memory; Lane F evidence; Lane H publication  
**Source:** Luo and Li, Sparse Quantum State Preparation with Sublinear T-Count, arXiv:2608.00414, first posted 2026-08-01.  
**Detailed record:** docs/RESEARCH_GAP_SPARSE_STATEPREP_MODEL_ALIGNMENT_2026-10-27.md  
**Literature watch:** docs/literature_watch/2026-10-27-sparse-stateprep-sublinear-tcount-model-alignment.md

The source abstract reports an O-tilde sparse-state-preparation synthesis upper expression and an Omega lower expression over a restricted support/precision regime. The existing sparse-QROM preprint arXiv:2607.28260v2 also states a sparse-state-preparation corollary. Full theorem assumptions, target-state representation, classical access/preprocessing, precision and synthesis models must be reconciled before comparing the claims. This is a model-alignment question, not a claimed contradiction or theorem improvement. The new helper records symbolic expressions only; exact counts, depth, ancillas, memory, I/O, energy and provider cost remain null.

**Unlock:** full-text assumption matrix; independent small-instance derivation/synthesis; preregistered held-out (n,s,epsilon) tests; explicit counterexample search; workload-level resource and accepted-task cost accounting. No provider execution or evidence promotion is authorized by this gap.


### RG-STATEPREP-NATURAL-001 — natural-proof barrier scope for state-preparation lower bounds
**Status:** OPEN / METHODOLOGY_ONLY / CONDITIONAL_THEOREM_SCOPE  
**Date:** 2026-10-27  
**Primary owner:** Lane A; Lane C memory/state; Lane F evidence; Lane H publication  
**Source:** Li and Parham, arXiv:2610.06826v1, submitted 2026-10-05.  
**Detailed record:** docs/RESEARCH_GAP_STATEPREP_NATURAL_PROOF_BARRIER_2026-10-27.md  
**Literature watch:** docs/literature_watch/2026-10-27-stateprep-natural-proof-barrier.md

The paper gives a conditional natural-proofs barrier for state-preparation lower-bound proof strategies. Its naturalness criteria are largeness over Haar-random states and constructivity from a complete finite-precision amplitude list. The theorem depends on a classically subexponentially secure pseudorandom-function assumption with polynomial-size, depth-d threshold-circuit implementations and applies to a fixed Magic-Hierarchy level in the stated superpolynomial lower-bound regime.

This gap asks whether the actual proof strategies in the existing sparse-state-preparation/QROM theorem comparison satisfy both criteria and the remaining scope conditions. The answer remains unresolved until the full theorem/proof text is reviewed. The barrier restricts a class of proof methods; it does not automatically invalidate a lower-bound claim, prove a replacement bound, or establish physical truth. The new contract records declared scope and digest integrity only.

**Unlock:** pin source versions; classify naturalness criteria separately; record exact cryptographic assumption, circuit hierarchy and approximation regime; reject inconsistent/tampered metadata; independently review theorem assumptions and small-instance/counterexample checks. Keep all unmeasured resources null and all physical/economic claims unpromoted.


## 2026-10-27 — RG-STATEPREP-SPIN-GLASS-001: profile-complexity lower-bound mapping

**Status:** ACTIVE / LITERATURE_ONLY / PROOF_RECONSTRUCTION_PENDING. New-to-main official preprint: Al-Ghattas, Gamarnik and Kiani, “Beyond Light Cones: State Preparation Complexity in Quantum Spin Glasses,” https://arxiv.org/abs/2610.02166 (v1 submitted 2026-10-01). The paper develops effective profile-complexity bounds for specified dense random p-spin Hamiltonians and state classes. It is not a universal workload/QUBO lower bound and is not a measured hardware/economic result.

**Detailed gap:** docs/RESEARCH_GAP_STATEPREP_SPIN_GLASS_PROFILE_2026-10-27.md  
**Literature watch:** docs/literature_watch/2026-10-27-beyond-light-cones-spin-glass-stateprep.md  
**Integration record:** integration/INT-20261027-STATEPREP-SPIN-GLASS-BOUND.json

Unlock by pinning exact theorem text and assumptions, independently reconstructing the proof, and mapping a specific workload to the stated Hamiltonian/state-class/energy/ancilla/asymptotic hypotheses with PASS/FAIL/UNKNOWN. Missing conditions fail closed. Only then compare resource implications against a matched CPU/GPU useful-output baseline. No paid QPU job is authorized by this gap.


## 2026-10-27 — RG-FUS001-HIDRA-LI-VAPOR-001: lithium net retention versus plasma contamination

**Status:** ACTIVE / PEER-REVIEWED EXPERIMENT / REACTOR-TRANSFER-UNVALIDATED. Rizkallah et al., “Rapid Vapor-Driven Plasma Contamination and Suppressed Net Lithium Surface Loss in the HIDRA Stellarator,” *Journal of Fusion Energy* 45, article 39 (published 2026-06-10): https://link.springer.com/article/10.1007/s10894-026-00582-y. HIDRA reports effective lithium net-loss suppression around 0.91 to unity in tested hydrogen/helium cases, while high-temperature lithium release rapidly contaminates the plasma. The paper does not establish reactor-relevant vapor shielding, tritium recovery, net electricity or lifecycle cost.

**Detailed gap:** docs/RESEARCH_GAP_FUS001_HIDRA_LITHIUM_VAPOR_CONTROL_2026-10-27.md  
**Literature watch:** docs/literature_watch/2026-10-27-hidra-lithium-vapor-plasma-contamination.md  
**Integration record:** integration/INT-20261027-FUS001-HIDRA-LITHIUM-VAPOR.json

Unlock by reconstructing the source mass balance and uncertainty, then independently testing matched capture/control conditions that measure both net surface loss and plasma impurity/stability. Propagate only replicated evidence through the FUS-001 lifecycle and net-electricity model.


## 2026-10-27 — FND-003 matched comparison contract
**Status:** OPEN / SOFTWARE CONTRACT ONLY. **Primary record:** docs/RESEARCH_GAP_FND003_MATCHED_COMPARISON_2026-10-27.md. The new contract binds control and quantum runs to the same task/output-quality hash, binds a candidate speed limit to a hashed quantum-evolution record, suppresses ratios when quality or measurement gates fail, and keeps wall-plug energy separate. It does not derive a theorem or establish measured advantage. No matched physical experiment, independent theorem reconstruction, or cost-per-accepted-task result exists yet.


## 2026-10-27 — RG-EQN-008: matched cross-method equation-discovery comparison
**Status:** OPEN / NO METHOD INDEPENDENTLY REPRODUCED. The focused record now includes STRIDE (data-aware generation, mixed fitting, critic–executor repair and semantic memory) alongside progressive composition, transformer generation, search control, structural guidance and constrained symbolic regression. Canonical detail: docs/RESEARCH_GAP_EQN008_MATCHED_DISCOVERY_COMPARISON.md. The existing comparison contract is metadata/record validation, not proof of actual group disjointness or physical truth. Unlock with pinned source/data/code, law-family-disjoint holdouts, at least 30 preregistered seeds where compute permits, common total resources, counterexample/false-discovery accounting and independent reproduction.

## 2026-10-27 — RG-047: formal-proof artifact binding
**Status:** PARTIALLY ADDRESSED / INTEGRATION AND PINNED PROOF RUN OPEN. Canonical detail: docs/RESEARCH_GAP_RG047_FORMAL_PROOF_ARTIFACT_BINDING.md. The byte-binding contract exists, but integration into equation-discovery records and a real pinned checker run remain open; PR #132 and its sync record PR #133 remain unmerged. Proof metadata does not establish empirical physics. Synchronization debt was reconciled in this cycle by appending this entry and the corresponding WORKLOG record from complete fetched file contents.

## 2026-10-27 — RG-QAOA-PARITY-001: matched higher-order parity QAOA evidence
**Status:** OPEN / NOT_YET_DEMONSTRATED. Canonical detail: docs/RESEARCH_GAP_QAOA_PARITY_MATCHED_EVIDENCE_2026-10-27.md. The existing paired-comparison contract is not a parity encoder or a reproduced algorithm. Exact small-graph mapping/reference checks, a frozen held-out manifest, equal shots/optimizer evaluations, target-aware simulation and full accepted-task resource accounting remain prerequisites. No paid QPU execution is authorized by this record.


## 2026-10-27 — RG-047 update: formal-proof evidence bound into EquationHypothesis
**Status:** SCHEMA INTEGRATION ADDRESSED; REAL PINNED PROOF RUN AND INDEPENDENT REBUILD OPEN. Canonical detail: docs/RESEARCH_GAP_RG047_FORMAL_PROOF_ARTIFACT_BINDING.md; implementation: software/uqpu-prototype/uqpu/equation_discovery.py. Non-NOT_RUN proof states now require an exact FormalProofEvidence record whose claim ID, claim kind and status agree with the equation hypothesis. This is metadata validation, not proof execution or empirical physics. RG-046 raw-data acquisition and its preregistered >=30-seed comparison remain open. Batch 071 and the integration record preserve the detailed evidence boundary.


## 2026-10-27 — RG-FND001-MEMORY-AWARE-INFERENCE-001: thermodynamic inference with finite memory

**Status:** OPEN / LITERATURE_ONLY / REPRODUCTION_NOT_RUN. **Primary record:** docs/RESEARCH_GAP_FND001_MEMORY_AWARE_THERMODYNAMIC_INFERENCE_2026-10-27.md. Schwarz, Kolomeisky and Godec, arXiv:2410.11819v5 (revised 2026-10-01; accepted for Physical Review Letters 2026-09-25), report a k-th-order entropy-production estimator and conditions for guaranteed dissipation lower bounds under strong non-Markovianity. The UQPU-relevant hypothesis is that memory order, coarse-graining and time-scale-separation assumptions must be explicit before interpreting inferred dissipation in FND-001. No UQPU reproduction or energy measurement exists. Unlock requires a pinned source/equation extraction, independent implementation, known-reference finite-state processes, preregistered held-out process families, >=30 fixed seeds, uncertainty/bias/lower-bound-violation/overestimation reporting and independent rebuild. Direct wall-plug energy accounting remains the alternative; this method does not establish a general quantum bound or new physical law.


## 2026-10-27 — RG-QAOA-PARITY-001 follow-up: exact graph-parity mapping baseline

**Status:** OPEN / BASELINE_MAPPING_TESTED / QAOA_REPRODUCTION_NOT_RUN. **Primary record:** docs/RESEARCH_GAP_QAOA_PARITY_MATCHED_EVIDENCE_2026-10-27.md; implementation: software/uqpu-prototype/uqpu/parity_encoding.py; Batch 073: docs/BATCH_073_PARITY_ENCODING_BASELINE.md. The new classical oracle canonicalizes graph edges, maps vertex bits to edge XORs, constructs independent fundamental-cycle constraints and decodes valid edge assignments with one fixed root bit per component. Seven focused tests passed locally, including exhaustive small-graph enumeration. The parity-QAOA circuit, signed-Max-Cut objective-preservation test, held-out equal-budget comparison, target-aware simulation and real-QPU evidence remain open. No performance or economic advantage is claimed.

## 2026-10-27 — RG-FND001-LEARNING-TO-ERASE-001: reversible learning and thermodynamic work

**Status:** OPEN / THEORY_ONLY / REPRODUCTION_NOT_RUN. **Primary record:** docs/RESEARCH_GAP_FND001_LEARNING_TO_ERASE_2026-10-27.md; source watch: docs/literature_watch/2026-10-27-learning-to-erase-quantum-states.md. Zhao, Zhang and Preskill, npj Quantum Information 12, 137 (2026), DOI 10.1038/s41534-026-01273-4, present a scoped theoretical learning-to-erase construction and a computational no-go result under explicit cryptographic assumptions. UQPU has not independently reconstructed the proof or measured any physical energy. Unlock requires source/supplement pinning, theorem-assumption extraction, independent proof reconstruction, a preregistered finite state family, reversible-uncomputation tests, explicit sample/runtime/workspace accounting and separate boundary-valid energy measurement before any device claim.


## 2026-10-27 — RG-MAT-SYMBOLIC-ENSEMBLE-001: symbolic interatomic-potential ensemble reproduction

**Status:** OPEN / LITERATURE_ONLY / REPRODUCTION_NOT_RUN. **Primary detail:** docs/RESEARCH_GAP_PANGOLA_SYMBOLIC_POTENTIAL_TRANSFER_2026-10-27.md. Varughese et al., *Physical Review Materials* 10, 103802 (published 2026-10-09), DOI 10.1103/gkpd-gtzp, report an EAM-structured EqNN/symbolic ensemble for DFT-referenced aluminum. UQPU has not reproduced the source artifacts or qualified any material. First gate: pin code/data and freeze held-out data; compare incumbent EAM, single symbolic candidates, ensemble and a declared ML potential with matched budgets; report energy and force errors separately, stability/invariance and failed seeds. Carbon-specific/Pangola work is a distinct later gate. No physical law, material substitution or technology/economic benefit is promoted.

## 2026-10-27 — RG-QAOA-PARITY-001 pending independent reference-suite validation

The feature branch adds an independent GF(2) rank implementation and exhaustive signed-edge objective-preservation tests. Status remains OPEN until exact-head hosted CI passes and the counterexamples, if any, are resolved. This is a classical mapping contract only; no parity-QAOA circuit, real-QPU result or cost/energy advantage is claimed.


## 2026-10-27 — RG-MAT-SISSO-SENSITIVITY-001: symbolic materials-gene sensitivity and identifiability

**Status:** OPEN / LITERATURE_ONLY / REPRODUCTION_NOT_RUN. **Primary detail:** docs/RESEARCH_GAP_SISSO_MATERIALS_GENE_IDENTIFIABILITY_2026-10-27.md; source watch: docs/literature_watch/2026-10-27-sisso-materials-gene-sensitivity.md. Foppa and Scheffler, *Physical Review Materials* 10, 093601 (published 2026-09-08), DOI 10.1103/gk23-cfh1, present derivative-based sensitivity analysis for SISSO materials genes and discuss equivalent descriptor combinations in a perovskite example. UQPU has not reproduced the code/data. Unlock requires source pinning, independent perovskite reproduction, finite-difference checks, frozen held-out material/property families, matched budgets and reparameterization/correlation stress tests. No causal-law, Pangola-carbon, device, fuel, fusion or economic claim is promoted.


### RG-BIO-001 — accepted-liquid mass, energy and full-cost closure
**Status:** OPEN / MODEL_ONLY CONTRACT IMPLEMENTED / PANGOLA DATA MISSING  
**Date:** 2026-10-27  
**Primary owner:** Lane E; evidence/integration owner Lane F  
**Detailed record:** docs/RESEARCH_GAP_BIO001_ACCEPTED_LIQUID_COST_2026-10-27.md  
**Implementation:** software/uqpu-prototype/uqpu/energy_finance.py (BioOilBatchCostInputs, bio_oil_batch_cost)

The batch contract prices final accepted liquid energy rather than raw bio-oil mass. It records wet/dry feedstock, preprocessing/logistics, hydrogen, catalyst, utilities, other OPEX, plant CAPEX recovery, capacity factor/lifetime, separate R&D capital-lockup interest and disjoint net coproduct credits. A rejected batch has no accepted-fuel cost/MJ. Calculated output is always MODEL_ONLY.

**Blocking data:** no traceable Pangola mass/energy closure, accepted-product assay/LHV/density, hydrogen/catalyst/utility dataset, local feedstock/logistics quotes, verified coproduct revenue or commercial financing terms.

**Unlock:** pin one lot and acceptance-spec SHA-256; record all output streams and process inputs; close mass/energy ledgers within a preregistered tolerance; independently repeat the batch; then compare only on the same accepted-fuel function and financing boundary. Do not infer a lower WACC from reduced principal.


## 2026-10-28 — RG-LBE-PINO-REPRO-001: physics-informed lattice-Boltzmann surrogate reproduction

**Status:** OPEN / LITERATURE_ONLY / SOURCE-DATA-AND-CODE-PINNING-PENDING.  
**Primary owner:** Lane E; cross-lane owners A, C, D/G, F and H.  
**Source:** Xue et al., *Nature Communications* 17, 9243 (2026), https://doi.org/10.1038/s41467-026-75730-1.  
**Objective:** reproduce one declared lattice-Boltzmann trajectory using the paper's physics-informed neural operator, then test long-horizon error, moment constraints, lattice equivariance, held-out configurations, peak memory, data/training/inference cost and break-even query count.  
**Blockers:** source data/code revision and license must be pinned; no UQPU reproduction or domain-transfer evidence exists. The paper's per-case speedups are external simulation results and its own discussion describes narrow training geometry/parameter bands.  
**Unlock:** independently reproduce a pinned reference case; pass predeclared quality/invariant thresholds on held-out trajectories/configurations; report all failed seeds, uncertainty, memory/I/O, data generation, training, validation, inference and energy where measurable.  
**Nonclaims:** no Pangola process, accepted bio-oil, fusion, cooling-device, QPU or Data-Center-to-One-Phone result; no new physical law. See `docs/RESEARCH_GAP_LBE_PINO_REPRODUCTION_2026-10-28.md`.


## 2026-10-28 — RG-A-SIGNED-MAXCUT-NUMERIC-RANGE-001: finite arithmetic and fail-closed score contract

**Status:** CODE FIX COMMITTED; exact-head CI verification follows the commit.  
**Primary owner:** Lane A — objective/compiler/runtime semantics.  
**Cross-lane owners:** B (SDK/target identity), C (output/state accounting), D/G (later Hamiltonian/device mapping), F (reference/evidence/economics), H (handoff/publication).  
**Related:** Batch 088–090; INV-025–027 and INV-029–035; FND-006.

A static counterexample audit found that individually finite signed edge weights are not sufficient to guarantee finite derived QUBO/Ising coefficients or finite accumulated objective values. For example, weight magnitude (10^{308}) can make the QUBO pair coefficient overflow; several (8\times10^{307}) edges can overflow a vertex's linear term or a full score. A very large integer can also fail during float conversion before the existing finite-value check.

**Resolution in Batch 090:** the compiler checks derived coefficients and accumulated coefficients; all three objective-score paths use a finite-sum guard; conversion overflow is normalized to a clear `ValueError`. Added regression tests cover derived-coefficient overflow, linear-coefficient overflow, huge-integer conversion and direct/QUBO/Ising score overflow.

**Acceptance:** exact-head core workflow and cold-start audit must pass. The focused tests are necessary but do not validate QAOA, SDK sign conventions, provider execution or quantum advantage. The next still-open Lane A gate is independent pinned-SDK Hamiltonian reconstruction against exhaustive references, including the full argmax set.

**Evidence boundary:** software numeric-range robustness only; no new physical law, QPU, material, fuel, electricity, financing/WACC or Data-Center-to-One-Phone result.


## 2026-10-28 — RG-EQN-AI-COSMIC-STRING-INTEGRAL-001

**Status:** OPEN / NOT_REPRODUCED.  
**Primary record:** docs/RESEARCH_GAP_AI_COSMIC_STRING_INTEGRAL_REPRODUCTION_2026-10-28.md.  
**Source watch:** docs/literature_watch/2026-10-28-ai-assisted-cosmic-string-integral-discovery.md.  
**Integration:** integration/DAILY_CYCLE_2026-10-28_AI_DISCOVERY_AND_AH_REPAIR.md.

The official preprint arXiv:2603.04735 reports LLM-guided tree search and numerical verification for a cosmic-string radiation integral. UQPU has not reproduced the result. The gate requires independent high-precision evaluators, predeclared held-out N/angle points, parity and endpoint/large-harmonic stress cases, explicit failure/undecided accounting, and independent symbolic review. Numerical agreement alone is not proof and does not establish a new physical law.

## 2026-10-28 — A–H operational manifest reconciliation

**Status:** IMPLEMENTED / EXACT-HEAD CI UNVERIFIED.  
The operational lane manifest and cold-start validator now define exactly A–H and 28 unordered review pairs. The historical Lane I vehicle/levitation directory remains preserved as a legacy workstream and is not deleted or silently merged into another lane. See docs/RESEARCH_GAP_AH_ARCHITECTURE_RECONCILIATION_2026-10-28.md and Batch 091. Close only after exact-head cold-start and prototype/invariant CI pass.


## 2026-10-28 — A–H operating-document reconciliation follow-up

**Status:** IMPLEMENTED / EXACT-HEAD CI UNVERIFIED.  
Batch 091 reconciles AGENTS.md, the prime handoff principle, commit-sync policy, continuous cross-lane protocol, active scoreboard and DECISIONS.md to the permanent A–H operational architecture. D109 supersedes D108 only on the question of whether Lane I is a permanent operational lane. Lane I records remain preserved as a legacy workstream, and the historical nine-lane scoreboard is archived rather than deleted. Exact-head cold-start and prototype/invariant workflows remain the acceptance gate.

## 2026-10-28 — RG-EQN-METHOD-PROVENANCE-001 / RG-EQN-SYMBOLIC-DIMENSIONALITY-REPRO-001

**Status:** OPEN / SOFTWARE_CONTRACT_HARDENED / EXACT_HEAD_CI_UNVERIFIED / METHOD_REPRODUCTION_NOT_RUN.  
**Primary owner:** Lane F — reproducibility and evidence contract.  
**Method/publication owner:** Lane H. **Execution owner:** Lane A.  
**Canonical details:** `docs/RESEARCH_GAP_EQN008_MATCHED_DISCOVERY_COMPARISON.md`, `docs/BATCH_097_METHOD_PROVENANCE_BOUNDARY.md`, and `docs/RESEARCH_GAP_EQN_SYMBOLIC_DIMENSIONALITY_REPRO_2026-10-28.md`.

The matched equation-discovery comparator now uses schema v4. `dataset_provenance_sha256` must match across methods; `method_revision_sha256`, `method_config_sha256` and `runtime_environment_sha256` must each remain fixed across all preregistered seeds within each method. Regression fixtures cover method source/config/environment drift, invalid hashes and mismatched dataset source/license provenance. The code and tests are on main, but exact-head prototype/invariant and cold-start CI have not been verified.

**Still open:** no SymFM, PiT-PO, STRIDE, LLM-PySR, MOSAIC-SR or other external method has been independently reproduced by this project; no matched 30-seed benchmark has been executed. The v4 hashes bind declared artifacts but do not authenticate them. The next gate requires pinned source/config/model/runtime manifests, source/license/data hashes, a verified group-disjoint split certificate, equal hard resource budgets, held-out law-family/scale tests, counterexample and false-discovery accounting, independent review and exact-head CI.

**Nonclaims:** no physical equation/law promotion, QPU advantage, material/fuel/electricity result, lower WACC, or Data-Center-to-One-Phone result. No paid QPU execution is authorized. The 100×/100,000,000× targets and INV-025–035 remain evidence-gated.



## 2026-10-28 — RG-FND003-QUANTUM-DYNAMICAL-ENTROPY-001

**Status:** OPEN / LITERATURE_ONLY / FULL_TEXT_AND_REPRODUCTION_PENDING. The new source-bounded watch is `docs/literature_watch/2026-10-28-planckian-quantum-dynamical-entropy-fnd003.md`. Cao, *Phys. Rev. Lett.* 137, 030402 (2026-07-13), DOI 10.1103/wd91-v58h, reports an entropy rate for continuous monitoring in terms of two-point correlations and conjectures a universal Planckian bound. The full paper/supplement was not independently reconstructed in this cycle. Do not implement the conjecture as a universal limit or conflate it with the separate thermalization-machine theorem. Next gate: retrieve full derivation; check units, assumptions and classical/large-N/finite-size limits; reproduce one exactly solvable model; preregister held-out regimes and counterexample search; separate system entropy from measurement/controller/reset/cooling energy. This source does not establish generic gate-time, accepted-task, wall-plug-energy or UQPU-advantage claims.


### Source-access correction — 2026-10-28

The official full manuscript was subsequently opened at https://arxiv.org/abs/2507.20914. The gap is therefore not blocked on access to the main manuscript; it remains open for faithful supplementary-derivation review and independent reproduction. Preserve the scope distinction: rate formula for the stated mesoscopic Gaussian-monitoring/noncritical thermal regime and ordered limits; \(\beta s_{CNT}\lesssim0.57\) when FDT is ignored; numerically optimized FDT-constrained value near 0.375; broad universality remains conjectural. The original abstract-only note is retained as history, but this correction supersedes its access limitation. No UQPU reproduction or physical-law promotion is implied.


## 2026-10-28 — RG-EQN-008 test-time scaling / search-width factor
**Status:** OPEN; literature-informed protocol update only.  
**Primary owner:** Lane A; Lane F evidence/cost contract; Lane H publication.  
**Source:** Lin et al., “Test-Time Scaling for Scientific Equation Discovery,” EMNLP 2026, https://aclanthology.org/2026.emnlp-main.354/ ; related preprint https://arxiv.org/abs/2608.28660.  
**New information:** the paper reports search width as the dominant compute-allocation parameter on its tested LLM-SRBench tasks under fixed budgets. UQPU has not reproduced the result.  
**Next gate:** preregister width arms under matched data provenance, whole-law-family/scale holdouts, shared seeds, pinned per-arm source/config/runtime hashes and equal total wall-clock/CPU/memory/accelerator/candidate/token/cost ceilings. Report accepted candidates, held-out error, uncertainty, constraints, counterexamples, false discoveries, failed searches/retries and total cost.  
**Falsifier:** the width effect disappears on held-out families/scales, is caused by leakage/unequal resources, raises false discoveries, or improves wall-clock without improving accepted equations per total resource/cost. Hash declarations alone do not authenticate source bytes; manifest content validation remains open.  
**Non-claims:** no UQPU benchmark, new physical law, quantum advantage, energy/material/fuel/fusion/finance result, or Data-Center-to-Phone result.


## 2026-10-28 — RG-EQN-008 literature delta: residual feedback, conjecture discovery and continuous formulas

**Status:** OPEN; literature-only, no independent UQPU reproduction.  
**Sources:** RISR (2026-10-08, https://arxiv.org/abs/2610.11387), SCOPE/ClosureBench (2026-10-13, https://arxiv.org/abs/2610.18938), MorphingNet (2026-10-14, https://arxiv.org/abs/2610.19942). See `docs/literature_watch/2026-10-28-residual-conjecture-continuous-equation-discovery.md` and Batch 099.

The sources add distinct candidate method families: pointwise residual-conditioned proposals/corrections; explicit conjecture trajectories plus active experiments; and continuously parameterized formula units with post-fit structure recovery. Their reported metrics and task classes are not directly comparable. Do not create a cross-paper ranking or pool static LLM-SRBench outcomes with interactive ClosureBench outcomes.

**Next experiment:** first verify code/license and retrievable artifact bytes; then use a static, law-family/scale-held-out dataset with fixed provenance, common acceptance rules, at least 30 shared preregistered seeds, equal hard per-run resource ceilings and one cost basis to compare available static methods. Keep active experiment design in a separate track with equal simulation/experiment-call budgets and blind tasks. Report held-out error, structural recovery where a known target exists, complexity, constraints, counterexamples, false discoveries, failed runs, retries, memory, I/O, tokens, training+inference cost and energy where measurable.

**Falsifier:** reject method advantage if it disappears under held-out law families/scales, depends on leakage or unequal budgets, or increases counterexamples/constraint failures/false discoveries. Hashes do not authenticate artifact bytes; independently verify the source, dataset and held-out records. No candidate equation or physical law is promoted.


## RG-EQN-008 addendum — SymbolFit uncertainty-aware HEP fitting (2026-10-28)

**Status:** OPEN / LITERATURE_ONLY / PROTOCOL_ONLY. New-to-repository source: Tsoi et al., SymbolFit, arXiv:2607.19750 (v2 revised 2026-10-19), https://arxiv.org/abs/2607.19750. The focused canonical record remains `docs/RESEARCH_GAP_EQN008_MATCHED_DISCOVERY_COMPARISON.md`; Lane A preregistration: `research_lanes/A_quantum_programming_runtime/SYMBOLFIT_UNCERTAINTY_PROTOCOL_V1.json`; integration: `integration/DAILY_CYCLE_2026-10-28_SYMBOLFIT_UNCERTAINTY_GATE.md`.

**Gap:** the existing schema-v4 comparator summarizes accepted-candidate rate uncertainty and paired seed counts, but does not by itself certify predictive-interval calibration. Before a real-data comparison, verify code/data/license bytes, then implement/test coverage jointly with interval width and a proper predictive score on synthetic known-function and null controls. Require frozen group-disjoint splits, >=30 shared preregistered seeds where feasible, equal hard resource ceilings, one cost basis, full training+inference accounting, false-positive/counterexample/failure retention and preregistered endpoints/tolerances.

**Falsifier / stop:** no advantage claim if calibration under-covers, wins only with uninformatively wide intervals, worsens null-control false positives, or disappears under blind held-out conditions/equal resources. Do not pool HEP binned-fit scores with general equation-recovery or active-experiment-design tasks. No new physical law, QPU advantage or commercial energy/material/economic result is established.


## RG-DG-VORTEXOP-2026-10-28 — physics-guided active design for manufactured structures

**Status:** LITERATURE_ONLY / DATA_BLOCKED until source artifacts are obtained.  
**Primary owner:** Lane D — device/material/process co-design. **Co-owners:** Lane G — equipment/manufacturing/yield; Lane E — candidate materials; Lane F — evidence/economics.  
**Source:** Moeinnia, Islam and Kim, “VortexOp: Autonomous Physics-Guided Discovery of Functionally Graded Metamaterials,” *Journal of Computational Design and Engineering*, published 2026-09-21, corrected/typeset 2026-10-21, DOI https://doi.org/10.1093/jcde/qwag085. Literature watch: `docs/literature_watch/2026-10-28-vortexop-physics-guided-metamaterial-design.md`. Cross-lane record: `integration/DAILY_CYCLE_2026-10-28_SYMBOLFIT_UNCERTAINTY_GATE.md`.

**Objective:** test whether solver-in-the-loop active design can reduce mass or improve a matched structural acceptance metric for a real device/package/fixture under measured loads and manufacturing constraints. VortexOp is a methodology candidate only; its published tests are geometry/load/material-specific and it did not test Pangola or biomass carbon.

**Evidence / limitation:** the paper reports mesh-specific failure-index reductions but only one specimen per architecture/volume-fraction configuration, no established systematic mesh-refinement stability, and a linear-static/small-strain solver that does not fully model nonlinear collapse. The paper states its code and generated data were not publicly accessible at submission and are available on request. Exact source/data access is therefore the first gate.

**Unlock criteria:** (1) obtain and hash code, solver, material data, meshes, settings and raw traces or mark DATA_BLOCKED; (2) reproduce a simple geometry/load case against an independent trusted solver; (3) establish mesh convergence; (4) test multiple specimens and preregister the primary endpoint; (5) use blind held-out geometry/load/scale and process conditions; (6) include process-aware printability, metrology, failed-build/rework, yield, equipment/energy/time and lifecycle cost per accepted part; (7) only then test a separately characterized carbon-rich candidate against a functionally matched incumbent.

**Falsifier / stop rule:** reject transfer if benefits vanish under mesh refinement, independent solver checks, replicated specimens or held-out conditions, or if a proxy failure index does not predict the real acceptance metric. Do not claim biomass-carbon substitution, lower cost per good part, a new constitutive law or a factory/device advantage from the external paper alone. Carbon processing is not elemental transmutation.

## RG-EQN-009 — independent audit of high-impact external AI theorem claims

**Status:** OPEN / EXTERNAL_CLAIMS_PENDING_INDEPENDENT_REVIEW  
**Opened:** 2026-10-28  
**Canonical detail:** [docs/RESEARCH_GAP_EQN009_EXTERNAL_AI_THEOREM_CLAIMS_2026-10-28.md](docs/RESEARCH_GAP_EQN009_EXTERNAL_AI_THEOREM_CLAIMS_2026-10-28.md)  
**Literature watch:** [2026-10-28 external AI mathematics, complexity and QFT claims](docs/literature_watch/2026-10-28-openai-math-complexity-qft-claims-verification-boundary.md)  
**Related:** INV-034–035, FND-006, EQN-007, RG-EQN-008, INV-029–033

**Objective:** independently audit the high-impact mathematics, ETH and constructive-QFT claims announced 2026-10-26, keeping source claims, exact formal statements, proof artifacts, kernel checks, expert review, physical validation and engineering advantage as separate evidence stages.

**Current evidence:** public Lean/math artifacts are linked for the mathematics and computational-complexity claims; UQPU has not cloned, hash-pinned, compiled or independently reviewed them. The QFT proof artifacts remain unavailable pending external review. This is literature triage, not a UQPU theorem or technology result.

**Unlock criteria:** pin exact source bytes, revisions, toolchains and dependencies; independently compile the public math/ETH developments; audit imported axioms, admissions, dependencies and statement fidelity; obtain independent expert review; keep QFT blocked until reviewable public artifacts exist; require separate physical and end-to-end engineering evidence before any mission claim changes.



## RG-EQN-010 — predictive interval scoring and synthetic control gate

**Status:** OPEN / METRIC_IMPLEMENTED / BENCHMARK_NOT_RUN  
**Opened:** 2026-10-28  
**Primary owner:** Lane A — equation-discovery metrics  
**Cross-lane owners:** Lane F — matched resources and evidence acceptance; Lane H — source provenance  
**Canonical detail:** docs/BATCH_101_PREDICTIVE_INTERVAL_METRICS.md  
**Integration:** integration/DAILY_CYCLE_2026-10-28_PREDICTIVE_INTERVAL_METRICS.md  
**Related:** INV-034–035, EQN-008, SymbolFit preregistration

**Objective:** evaluate predictive intervals with empirical coverage, coverage error, mean width and a proper interval score, without allowing arbitrarily wide intervals to win solely on coverage.

**Implementation:** software/uqpu-prototype/uqpu/predictive_interval_metrics.py provides a fail-closed central-interval scorer. Deterministic tests cover a known-function positive control, a null/no-signal interval fixture, width penalties, out-of-interval penalties and invalid numeric inputs.

**Evidence boundary:** source code and synthetic unit fixtures only. No project test suite is claimed passed until exact-head CI completes. The fixtures do not fit or calibrate a model, estimate false-discovery rate, authenticate source/data/license bytes, or establish a physical law.

**Unlock criteria:** (1) exact-head prototype/invariant and cold-start Actions pass; (2) verify exact SymbolFit source/code/data/license bytes; (3) predeclare coverage tolerance, proper-score endpoint, multiplicity and grouped holdout; (4) test 0.68 and 0.95 levels on synthetic known-function, null and blinded-signal controls across preregistered seeds; (5) retain every failed seed and false discovery; (6) only then consider a blind real-data comparison with matched total resources and one cost basis.

**Non-claims:** no equation-discovery method winner, new physical law, real-QPU advantage, material/fuel/electricity benefit, lower financing rate or Data-Center-to-One-Phone progress is established. Priority-1 signed-Max-Cut SDK reconstruction remains the higher execution gate.


**CI correction update — 2026-10-28:** Batch 101's first commit failed core/invariant run #1946 and cold-start audit #1205 because the handoff manifest referenced docs/RESEARCH_GAPS.md instead of root RESEARCH_GAPS.md. The new predictive-interval unit tests passed in Python 3.12; the overall suite failed on the cold-start manifest assertion. The follow-up commit corrects the path. Exact-head CI remains required, and the failure is retained as negative evidence.


## 2026-10-28 — RG-A-TEMPORAL-HOLDOUT-ORDERING-001: chronological split certificate

**Status:** IMPLEMENTED CONTRACT / EXACT-HEAD CI PENDING / REAL-DATA GENERALIZATION OPEN.  
**Primary owner:** Lane A — model-evaluation contract.  
**Artifacts:** [Batch 103](docs/BATCH_103_TEMPORAL_HOLDOUT_CERTIFICATE_AND_OPERATOR_SPLITTING.md) · [focused gap](docs/RESEARCH_GAP_TEMPORAL_HOLDOUT_ORDERING_2026-10-28.md) · [Lane A contract](research_lanes/A_quantum_programming_runtime/TEMPORAL_HOLDOUT_ACCEPTANCE_CONTRACT.md) · [implementation](software/uqpu-prototype/uqpu/temporal_holdout.py) · [tests](software/uqpu-prototype/tests/test_temporal_holdout.py).

The existing group-disjoint TIME_BLOCK manifest did not itself require chronological ordering. The new helper binds raw records to the canonical manifest, normalizes timezone-aware timestamps to UTC, requires strictly ordered train/validation/test windows and enforces a declared embargo. Eleven synthetic tests cover positive, reordered, malformed, overlapping, leaking and insufficient-embargo cases. The local clone failed due DNS resolution, so no local test pass is claimed; exact-head Actions remain the acceptance gate. A PASS certifies the supplied split metadata only, not source authenticity or scientific generalization.

**Next gate:** pass exact-head CI; pin a real dataset/license/loader; preregister future-time plus relevant coefficient/geometry holdouts; compare methods against an independent numerical reference under matched resource ceilings. No equation, physical law, QPU advantage, material/fuel/electricity advantage or financing-rate effect is promoted.


## 2026-10-28 — BIO-001 literature update: pilot char recovery and ANN yield basis

**Status:** LITERATURE LEADS / PANGOLA ACCEPTED-LIQUID COST OPEN.  
**Details:** [BIO-001 focused gap](docs/RESEARCH_GAP_BIO001_PILOT_YIELD_BASIS_2026-10-28.md) · [literature watch](docs/literature_watch/2026-10-28-biomass-pyrolysis-pilot-and-ann-models.md) · [Batch 104](docs/BATCH_104_BIOMASS_FUSION_COSTING_LITERATURE_DELTA.md).

The pilot-scale pine-sawdust study reports char recovery and a scenario-specific minimum selling price; the bagasse ANN reports in-range yield prediction. Neither is a Pangola experiment or accepted finished-fuel cost. Reconcile dry-feed/moisture basis, mass versus volumetric yield, product quality/upgrading, energy balance, finance and non-double-counted coproduct credits; require chronological/feedstock/scale holdouts before using ANN predictions.

## 2026-10-28 — FUS-001 literature update: pyFECONs cost-account reference

**Status:** PUBLIC REFERENCE IDENTIFIED / PINNED REPRODUCTION OPEN.  
**Details:** [FUS-001 focused gap](docs/RESEARCH_GAP_FUS001_PYFECONS_ACCOUNT_MAPPING_2026-10-28.md) · [literature watch](docs/literature_watch/2026-10-28-pyfecons-fusion-costing-and-uncertainty.md) · [Batch 104](docs/BATCH_104_BIOMASS_FUSION_COSTING_LITERATURE_DELTA.md).

The official preprints describe standardized account-based fusion costing, architecture-specific driver tracks, uncertainty and finance/value metrics. Pin the exact code/data/license and reproduce a public case before adoption. Preserve net-electric normalization, recirculating power, component lifetime/replacement, fuel cycle, remote handling, cooling, grid, construction, decommissioning and financing. WACC/risk-premium changes remain scenarios until separately evidenced.


## RG-BIO001-CATALYST-BIOCHAR-001 — accepted liquid-energy and catalyst-loaded char functional gate
**Opened:** 2026-10-28  
**Status:** OPEN / LITERATURE_ONLY / NO PANGOLA TRANSFER  
**Primary owner:** Lane E; evidence owner Lane F; method interface Lane A  
**Canonical detail:** docs/RESEARCH_GAP_BIO001_CATALYST_BIOCHAR_FUNCTIONAL_ACCEPTANCE_2026-10-28.md  
**Source:** https://doi.org/10.1016/j.biombioe.2026.109296

A 2026 *Biomass and Bioenergy* study reports catalytic microalgae/hardwood co-pyrolysis, 23.9/23.5 wt% oil yields, 25.27 MJ/kg reported in-situ-oil HHV and 96.6% methylene-blue removal by catalyst-loaded biochar under its tested conditions. UQPU has not reproduced it. Transfer to Pangola is blocked pending source/data pinning, feedstock characterization, dry-basis mass/energy closure, accepted-fuel/upgrading analysis, catalyst recovery/regeneration/lifetime/leaching tests, repeat-cycle solid-service validation and full lifecycle costing. Coproduct and carbon credits must not be double counted. This gap is not commercial-fuel, material-substitution or physical-law evidence.

## RG-D-PHOTONIC-INSPIRE-END-TO-END-001 — physical photonic training acceptance
**Opened:** 2026-10-29  
**Status:** OPEN / THIRD_PARTY_EXPERIMENT / UQPU_REPRODUCTION_NOT_STARTED  
**Primary owner:** Lane D; interfaces A/C/F/G  
**Canonical detail:** `docs/RESEARCH_GAP_PHOTONIC_INSPIRE_END_TO_END_2026-10-29.md`  
**Source:** https://doi.org/10.1038/s43588-026-01057-y

The 2026-10-05 *Nature Computational Science* INSPIRE paper reports in-situ physical-gradient training on photonic integrated circuits, 0.26% relative error for trained matrices, training through scattering media beyond the native tunable-element count, 251-fold model compression and 136-fold task-specific training acceleration. These are source-reported, task-specific experimental results, not UQPU reproduction or end-to-end energy/cost evidence.

Gate: pin and hash the paper data and https://doi.org/10.5281/zenodo.21918485; reproduce the stated matrix metric; freeze a shared useful-workload/quality predicate for digital, in-silico photonic and in-situ training; test a second device plus held-out topology/wavelength/temperature; count optical source/loss, tuning/control, detector/readout, ADC/DAC, host, calibration, data movement, yield, packaging, drift, service life and capital allocation. Compare energy and total cost per accepted task; reject the advantage hypothesis if overheads or held-out failures erase it. No new physical law, universal accelerator replacement, phone-compression, bio-oil, fusion, WACC or paid-QPU claim follows.

## 2026-10-29 — RG-A-QUASARQ-STABILIZER-REPRO-001 — GPU stabilizer simulation

**Status:** OPEN / LITERATURE_ONLY / UQPU_REPRODUCTION_NOT_STARTED.  
**Primary owner:** Lane A; interfaces B/C/F/H.  
**Source:** Osama, Thanos and Laarman, *Quantum* 10, 2225 (2026-10-01), https://doi.org/10.22331/q-2026-10-01-2225.  
**Objective:** reproduce a bounded QuaSARQ stabilizer/Clifford workload with pinned source/environment, exact output or syndrome checks, matched Stim/other baseline versions, held-out circuits, runtime/throughput, peak host/device memory, transfer bytes/time, host work, retries and energy where measurable.  
**Blockers:** UQPU has not pinned or reproduced the source code, environment, hardware or benchmark suite. Reported up-to-105x runtime speedup and over-80% energy reduction are source-reported on selected cases only.  
**Scope boundary:** classical stabilizer simulation, not real-QPU execution and not a generic simulator for arbitrary non-Clifford QAOA rotations. Do not substitute for the parity-QAOA simulation gate.  
**Unlock:** exact correctness on a frozen subset, reproducible measurements, a held-out circuit family, complete task-boundary accounting and independent review. Unknown energy components remain unknown, not zero.  
**Nonclaims:** no QPU advantage, GPU replacement, readable classical-memory equivalence, new physical law, commercial fuel/fusion, lower WACC or Data-Center-to-One-Phone result. See `docs/RESEARCH_GAP_QUASARQ_STABILIZER_REPRODUCTION_2026-10-29.md`.


## 2026-10-29 — RG-A-QUESTAB-EXTENDED-TABLEAU-REPRO-001

**Status:** OPEN / LITERATURE_ONLY / SOURCE-PINNING-NOT-STARTED.  
**Primary owner:** Lane A; interfaces B/C/F/D/G/H.  
**Source:** ACM ICS '26, “quEStab: Towards Scalable Quantum Circuit Simulation on Multi-GPU using an Extended Stabilizer Formalism,” published 2026-07-05, https://doi.org/10.1145/3797905.3816723.  
**Objective:** reproduce a bounded, exact circuit suite for the extended-tableau multi-GPU simulator and test whether active-row growth, memory/I/O and host overhead preserve any end-to-end benefit.  
**Source-audit item:** the publisher-indexed text reports 69/97 (71.1%) and 100/128 (78.1%) coverage in separate passages. They may describe different subsets/stages; reconcile each numerator/denominator, preprocessing stage, timeout and success predicate before comparison.  
**Gate:** pin source/dependencies/build/hardware; compare Clifford, T-gate, parameterized-rotation and small parity-QAOA circuits against independent exact references; measure active rows, peak host/device memory, transfer, setup, latency, throughput, failures/retries and energy where measurable; hold out circuit families. Unknown costs/energy remain unknown, not zero.  
**Nonclaims:** no real-QPU advantage, general QAOA scaling, readable classical-memory equivalence, 100x/100,000,000x economics, new physical law, material substitution, commercial bio-oil, net fusion electricity, lower WACC or Data-Center-to-One-Phone closure. Canonical detail: docs/RESEARCH_GAP_QUESTAB_EXTENDED_TABLEAU_REPRODUCTION_2026-10-29.md.


## 2026-10-29 — RG-FND006-AI-FORMAL-DISCOVERY-REPRO-001

**Status:** OPEN / PREPRINTS-ONLY / UQPU-REPRODUCTION-NOT-STARTED.  
**Primary owner:** Lane H; interfaces A/F and all lanes through INV-034/035.  
**Sources:** https://arxiv.org/abs/2610.22603 ; https://arxiv.org/abs/2610.08329 ; https://arxiv.org/abs/2610.14059.  
**Objective:** separate candidate novelty, formal correctness, physical validity, engineering consequence and mission economics in a reproducible AI-assisted discovery protocol.  
**Evidence:** the Busy Beaver preprint reports Lean-checked execution-acceleration rules for eleven BB(6) machines, with novel, rediscovered and proof-only cases; the Poincaré preprint formalizes an established theorem using milestone-driven human/AI work; a physics-formalization perspective warns that proof checking does not validate physical semantics. UQPU has not reproduced these workflows.  
**Gate:** compare unconstrained and staged physics-constrained candidate search on a synthetic known-law dataset under matched compute budgets and a frozen held-out regime; bind proof results to exact source/theorem hashes and proof-assistant versions; retain false discoveries and failed/undecided proofs; require a discriminating observable and independent experiment before any physical claim.  
**Nonclaims:** no new physical law, material/fuel/electricity result, QPU advantage, lower WACC or Data-Center-to-One-Phone closure. Canonical detail: docs/RESEARCH_GAP_FND006_AI_FORMAL_DISCOVERY_REPRO_2026-10-29.md.


## 2026-10-29 — RG-QAOA-PARITY-001 implementation update

**Status:** OPEN / PROTOTYPE-ADDED / MATCHED-BENCHMARK-NOT-RUN.  
**Primary owner:** Lane A; evidence/integration owner Lane F.  
**New artifacts:** software/uqpu-prototype/uqpu/parity_qaoa.py and software/uqpu-prototype/tests/test_parity_qaoa.py; canonical detail in docs/BATCH_110_PARITY_QAOA_CIRCUIT_AND_REFERENCE_CERTIFICATE.md.  
**Advance:** a higher-order cycle-parity objective, CNOT/RZ phase-gadget lowering, fail-closed penalty threshold, exact small-instance certificate and dense-statevector regression test have been added. The product-RX mixer is not feasibility-preserving; outputs must be parity-checked and decoded.  
**Remaining blockers:** exact-head CI for this commit, independent SDK/lowering checks, target-aware simulation, matched direct-vs-parity tests on held-out graph families, quality acceptance, and complete resource/energy/cost accounting.  
**Nonclaims:** no real-QPU advantage, scalable resource reduction, 100x/100,000,000x economics or mission-level replacement result.
