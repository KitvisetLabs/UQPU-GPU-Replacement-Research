# Literature watch — 2026-10-25: finite-information ergotropy certification for FND-001

**Accessed:** 2026-10-25 (Asia/Bangkok)  
**Primary owner:** Lane F — evidence, benchmarks, energy economics and integration  
**Priority execution lane:** A — quantum programming, workloads, compiler and runtime  
**Feeds:** A, B, C, E, F, H; FND-001, FND-002, FND-003; EQN-001, EQN-004, EQN-006; INV-025–027 and INV-029–035  
**Evidence class:** LITERATURE_ONLY — peer-reviewed theory/method with a third-party quantum-processor demonstration  
**UQPU evidence promotion:** none

## Primary source and dated evidence

Egle Pagliaro, Leonardo Zambrano, Mir Alimuddin, Alioscia Hamma, Antonio Acín and Donato Farina, “Certifying ergotropy under partial information,” *Physical Review Letters* 137, 130401 (published 2026-09-21), DOI 10.1103/pl26-g6vy. The public arXiv v2 was revised 2026-09-28: https://arxiv.org/abs/2603.18828. The journal record is https://journals.aps.org/prl/abstract/10.1103/pl26-g6vy.

The paper gives a semidefinite-programming (SDP) protocol that lower-bounds the ergotropy of a finite-dimensional state when the Hamiltonian is known but the state is only partially characterized by expectation values of a limited set of observables. For finite shot counts, each observable constraint is widened to a confidence interval. For observables bounded in [-1, 1], the authors use

$$\epsilon_i = \sqrt{\frac{2\log(2K/\delta)}{N_i}}$$

where K is the number of measured observables, N_i is the number of shots for observable i, and 1 - delta is the requested confidence level. The construction yields a certified lower bound on extractable average work, not a measurement of the energy consumed by a computing system.

The reported hardware example uses IBM Quantum processor ibm_perth for a four-qubit GHZ target and an XXZ Hamiltonian. The experiment considers up to 60 Pauli-string constraints (about 23.5% of the 255 non-identity strings for four qubits) and reports 2^14 shots per observable. The authors also show synthetic-data studies and discuss the known-Hamiltonian assumption. These are the paper's results; they are not UQPU runs.

## Genuine novelty and limits

The useful advance for this project is a practical, confidence-aware lower-bound method for a thermodynamic resource under incomplete measurement information. It is not a new thermodynamic law, a universal energy lower bound, or evidence of a cheaper computing workload. It reduces dependence on full state tomography for the specific task of certifying extractable work.

Important limits:

- The certification assumes the system Hamiltonian is known; Hamiltonian uncertainty is identified by the authors as future work.
- The finite-shot guarantee depends on the stated bounded-observable and confidence-interval assumptions. Correlations, drift, calibration errors, state-preparation errors and model mismatch must be handled explicitly in any new implementation.
- The demonstration concerns a small, prepared quantum state and ergotropy. It does not measure facility electricity, cryogenic overhead, host computation, networking, reconstruction cost, or joules per accepted useful task.
- Ergotropy is a work resource of a specified quantum state and Hamiltonian. It must not be subtracted from a processor's metered electricity and called an efficiency gain unless a complete, physically consistent energy/work boundary is independently established.
- The paper does not demonstrate GPU/CPU/NPU/RAM/VRAM/storage replacement, commercial energy savings, new physics, or a Data-Center-to-One-Phone capability.

## Exact UQPU relevance

### FND-001 — thermodynamic-gap accounting

Use the paper as a candidate method for a *separate* state-resource ledger entry: certified ergotropy lower bound, confidence level, Hamiltonian provenance, observable set, shots per observable, solver residuals and calibration assumptions. Keep that entry separate from:

1. metered energy consumed per accepted useful task, including the explicitly declared host/QPU/control/network/cooling boundary;
2. a justified ideal physical lower bound, such as a Landauer term only when the logically irreversible operation count and temperature assumptions are independently established; and
3. the residual gap between quantities that truly share compatible units and system boundaries.

Do not infer energy consumed by the QPU from a bound on extractable work. Do not assume every measured state is a battery or that an ergotropy estimate represents useful computation.

### Lane A and provider-neutral computing

The paper suggests a possible finite-shot certificate pattern for a future energy/resource benchmark, but it does not change the current Priority-1 gate. Batch 056 remains a bounded numerical QSVT simulation. The next Lane A gate remains the frozen feasible/infeasible QSP/QSVT test, followed by workload-derived resource accounting, independent SDK checks and target-aware lowering. A real-QPU experiment remains disabled without credentials, a bounded budget and explicit authorization.

### Lanes C, D, E, F, G and H

- C: account for measurement shots, state preparation and classical post-processing; no state-space dimension is readable RAM/storage equivalence.
- D/G: if later implemented on hardware, record target-native circuit resources and device/control overhead; this paper supplies no fabrication or yield evidence.
- E: do not equate extractable work with net fusion electricity, bio-oil energy yield, or a material's functional substitution.
- F: compare confidence-certified quantities, metered energy and accepted-task quality under a common boundary; preserve uncertainty and negative outcomes.
- H: this is a literature lead for strategic research publication only; it does not support a financing, interest-rate, WACC or funding claim.

## Falsifiable follow-up — FND-ERG-001

**Stage 0 — reproduce on paper before implementation.** Re-derive the two-SDP construction and finite-statistics confidence set from the public v2 preprint, including the known-Hamiltonian assumption and the monotonicity safeguard that retains a prior extraction unitary unless a new candidate tightens the bound. Record the exact paper version and equations.

**Stage 1 — synthetic exact-reference test.** Freeze small systems with known density matrices and Hamiltonians. Generate a preregistered set of observable subsets and shot counts. For each case, calculate exact ergotropy from the full state, then calculate the partial-information certificate independently. Require the lower bound never to exceed the exact reference (within declared numerical tolerances), and verify empirical confidence coverage across repeated shot draws at the preregistered delta. Include passive states, rank-deficient states, noisy states, incomplete-observable cases yielding a zero bound, and malformed/non-finite measurement inputs.

**Stage 2 — adversarial and generalization tests.** Test calibration offsets, observable sign/normalization mistakes, duplicated or dependent observables, changed Hamiltonians, shot-budget imbalance, solver tolerance, and added constraints. Reject any implementation that violates positivity/trace constraints, reports a bound above the exact reference, or claims a statistical guarantee after assumptions are broken. Keep a retained failing fixture for every counterexample.

**Stage 3 — system-energy separation.** Only after independent reproduction, define a same-task ledger with accepted-output quality, shots, latency, retries, host work, transfer/I/O and metered energy. Keep ergotropy as a separate state-resource field. A UQPU energy claim requires a matched CPU/GPU/NPU baseline and an identical useful-output contract; this paper alone cannot satisfy that gate.

**Falsifier:** reject the reproduction if a certified lower bound exceeds exact ergotropy beyond the preregistered numerical tolerance, the confidence procedure misses its declared coverage beyond a preregistered statistical test, or the claimed monotonic improvement fails when new constraints are added under the paper's safeguard. Failure to obtain a positive bound in an information-poor case is an allowed negative result, not permission to relax the certificate.

**Independent validation:** a second implementation or reviewer should reproduce the exact-state reference and certificate on frozen data before any optional, separately authorized provider experiment. No paid QPU work is authorized by this literature watch.

## Contribution to permanent invariants

- **INV-029:** improves measurement discipline for a possible energy-accounting subtask; no phone-class physical compression or end-to-end capability result.
- **INV-030:** no Pangola-carbon/material result.
- **INV-031:** no accepted liquid-fuel yield or lifecycle-cost result.
- **INV-032:** no net delivered fusion-electricity result.
- **INV-033:** no principal, financing-duration, interest or WACC result.
- **INV-034:** adds a falsifiable, finite-statistics thermodynamic-resource lead without relaxing established limits.
- **INV-035:** no equation is promoted to a physical law; mathematical certificates, physical interpretation and device/economic claims remain separate evidence stages.
- **INV-025/026/027:** all subsystem moonshots and open-frontier research remain evidence-gated.

## Decision

**Adopt as a literature-only method lead for FND-001. Do not implement by abstract-only inference, do not promote to project evidence, and do not displace Lane A's QSP/QSVT feasibility gate.** The next action is Stage 0 paper-level reproduction and a preregistered exact-reference test design.