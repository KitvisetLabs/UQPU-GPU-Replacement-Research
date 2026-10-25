# FND-001 — accepted-task thermodynamic-gap contract

**Date:** 2026-10-24  
**Primary owner:** Lane F — economics, evidence and integration  
**Starting canonical main:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`  
**Implementation:** `software/uqpu-prototype/uqpu/thermodynamic_gap.py`  
**Focused tests:** `software/uqpu-prototype/tests/test_thermodynamic_gap.py`  
**Integration ID:** `INT-20261024-009-FND001-LANDAUER-GAP`  
**Evidence class:** SOFTWARE_CONTRACT / MODEL_ONLY until populated with measured records  
**Status:** IMPLEMENTED; hosted exact-head CI pending

## Objective

FND-001 requires the project to compare energy per accepted useful result with a carefully scoped Landauer-style irreversible-erasure floor. Existing `fundamental_limits.py` supplies the ideal per-bit floor, but a defensible gap record also needs an accepted-output denominator, energy boundary, temperature basis, an independently justified erased-bit count, and provenance. This artifact adds that missing bookkeeping contract without asserting that wall-plug energy equals heat dissipated by logical erasure.

For a measurement window with total energy (E_{window}), (N_a) accepted outputs, (b_e) independently accounted irreversible erasures per accepted output, and erasure-bath temperature (T):

- (E_{accepted}=E_{window}/N_a), so failed attempts and retries inside the window are charged to accepted outputs.
- (E_{L}=b_e k_B T ln 2), only for the declared logical-erasure accounting and temperature basis.
- (R=E_{accepted}/E_L) is a **diagnostic ratio**, not thermodynamic efficiency, a lower-bound saturation claim, or evidence of advantage.

If no output is accepted, the per-accepted-task ratio is undefined. If erased bits are unknown, the report is `BLOCKED_ERASURE_ACCOUNTING`. If the computed ratio is below one, the report requests `BOUNDARY_AUDIT_REQUIRED`; it does not declare a violation of thermodynamics. If (b_e=0), the ratio is undefined rather than silently divided by zero.

## Fail-closed input contract

The new immutable input record binds:

- stable workload-contract ID;
- attempts, accepted count and total energy for the same window;
- explicit energy scope (full-system wall-plug or named subsystem);
- temperature and the physical basis for that temperature;
- governed evidence label;
- energy, accepted-output and measurement-window provenance for measured evidence;
- optional irreversible erased-bits-per-accepted-task, plus its accounting basis and provenance.

The implementation does **not** infer erased bits from output width, qubit count, Hilbert-space dimension, or the FND-002 output-information lower bound. FND-002's minimum output information and FND-001's irreversible erasure count are different quantities. An absent erasure count remains a visible blocker.

Only a complete, measured full-system record is eligible for FND-001 gap analysis. The function always returns `project_advantage_claim_allowed=false`; the helper cannot certify a mission claim.

## Validation and evidence

Fifteen focused unit-test methods cover the accepted-task denominator, absent erasure accounting, no accepted outputs, zero-erasure floor, below-floor boundary audit, provenance gates, MODEL_ONLY and subsystem exclusions, malformed counts/temperature/energy/erasure inputs, and the explicit no-inference rule. They are committed for hosted execution; no local repository checkout was possible in this environment. Exact-head GitHub Actions remains authoritative and is not presumed to pass.

This is a software-contract result, not a measured FND-001 result. No workload energy, erased-bit count, heat, cooling, quantum device, provider, QPU job, shot, cost or energy advantage was measured by this cycle.

## A–H integration review

| Lane | Interface / result | Current boundary and next gate |
|---|---|---|
| **A — workloads/compiler/runtime** | Uses the same stable workload contract and accepted-output definition as the benchmark. | Bind one frozen QUBO/QAOA or other workload, reference certificate, and competitive CPU/GPU/NPU baseline before collecting energy. |
| **B — cloud/QPU providers** | Provider execution and billable usage remain separate inputs; no provider is called by this helper. | When authorized, retain same-provider/target/calibration/pricing provenance; no paid or unpaid job is authorized here. |
| **C — RAM/VRAM/HBM/storage/state/I/O** | Distinguishes output-information requirements from irreversible erasures and from readable memory. | Add measured host, transfer, reconstruction and storage energy to a complete system boundary; do not equate qubits with classical memory. |
| **D — devices/chips/process/packaging** | Energy scope and temperature basis are explicit fields for future device-level records. | Obtain a same-evolution Hamiltonian/erasure/control measurement before interpreting a device-level gap. |
| **E — biomass/materials/bio-oil/fusion/cooling** | No new material, fuel, fusion, or cooling measurement. | BIO-001 still needs closed Pangola-to-saleable-liquid mass/energy/yield/upgrading/cost evidence; FUS-001 needs lifecycle net-delivered-electricity inputs. |
| **F — economics/evidence/integration** | Owns the accepted-task energy denominator, evidence label and fail-closed ratio. | Populate with measured full-system records and uncertainty; keep provider billing, host energy, retry/reconstruction and financing separate. |
| **G — manufacturing equipment/factory systems** | No fab or factory quantity is inferred from this diagnostic. | D/G co-design requires an independently specified device/process need before cost-per-good-die or lifetime inputs can be connected. |
| **H — strategy/finance/future industries** | Keeps mission ambition separate from measured cost/energy and protects evidence boundaries. | Lower energy may affect OPEX only when measured; it does not independently prove lower principal, interest, WACC or risk premium. |

The current repository also retains Lane I as an auxiliary extension in its manifest; it does not replace or redefine the permanent A–H architecture.

## Foundational and equation-discovery mapping

- **FND-001:** this contract supplies a missing fail-closed accounting interface; actual measured gap remains open.
- **FND-002:** output-information lower bounds remain a separate service/readout contract; no output bits are substituted for erased bits.
- **FND-003:** the matched control-versus-quantum-speed-limit gap still requires energy for the same physical evolution, a valid theorem setting, and scheduled wall-clock duration rather than a serial sum of gate durations.
- **FND-004 / FND-005 / FND-006:** no new primitive, particle/QFT mechanism, theorem or mathematics-first invention is claimed.
- **EQN-001–EQN-006:** no candidate physical equation was generated or promoted. Established Landauer accounting remains binding; the work only makes the comparison auditable.
- **BIO-001 / FUS-001 / FIN-001:** remain evidence-gated. No commercial fuel, net-electric fusion, lower WACC, or financing outcome is inferred.

## INV-029–INV-035 contribution

- **INV-029:** supports future capability/energy accounting but does not demonstrate data-center-to-one-phone physical compression; a remote terminal is not the endpoint.
- **INV-030:** no Pangola carbon material substitution or elemental-transmutation claim.
- **INV-031:** no accepted bio-oil/fuel or cost-per-delivered-energy evidence.
- **INV-032:** no net delivered fusion electricity or lifecycle cost evidence.
- **INV-033:** no measured CAPEX/OPEX/principal/interest/WACC improvement.
- **INV-034:** makes one foundational lower-bound comparison more reproducible and falsifiable.
- **INV-035:** preserves the incumbent equation and its assumptions; no AI-generated equation is presented as a physical law.

INV-025/026/027 remain preserved. The 100× and 100,000,000× targets, universal 100,000,000-unit subsystem replacement, and all mission pillars remain unachieved goals pending end-to-end evidence.

## Literature surveillance and sync discipline

Fresh public surveillance on 2026-10-24 was cross-checked against the canonical 2026-10-23 optimization-law / ancilla-QFI watch and the already-open 2026-10-24 watches for progressive symbolic discovery, formal proof gates, equation-search controls, BIO-001 upgrading and FUS-001 economics. No distinct new high-confidence primary result was found that changes this FND-001 contract, so no duplicate literature article was created. Third-party literature remains literature-only and does not populate project measurements.

The large append-only `RESEARCH_GAPS.md`, `WORKLOG.md`, and scoreboard history were not rewritten. This dated Lane-F artifact records the gap and next gate; canonical-history synchronization remains explicit debt until the normal reviewed merge process reconciles this artifact.

## Next highest-value gate

1. Require exact-head Python 3.10–3.12 and full repository CI.
2. Freeze one accepted-output workload contract and quality threshold.
3. Record total full-system wall-plug energy for all attempts in a defined window, accepted count, temperature basis, meter calibration, uncertainty and independent erasure-accounting provenance.
4. Independently audit the energy boundary and the Landauer assumptions before interpreting (R).
5. Carry the same workload and measurement window into Lane-F total cost per accepted task and Lane-A competitive classical baselines.

No real-QPU execution is authorized by this artifact; any paid QPU work still requires credentials, bounded budget and explicit user consent.
