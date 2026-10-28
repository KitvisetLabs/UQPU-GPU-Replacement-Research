# Literature watch — non-Hermitian exceptional-point speedup and transition-rate quantum speed limits

**Accessed:** 2026-10-28  
**Primary owner:** Lane H — foundational research publication and strategic integration  
**Implementation owner:** Lane A — matched workload/control contract  
**Cross-lane owners:** B (target identity), C (state/retry/I/O), D/G (device/control co-design), E (dissipation/cooling), F (evidence/economics)  
**Evidence class:** `LITERATURE_ONLY` — one peer-reviewed trapped-ion experiment and one peer-reviewed theoretical framework  
**UQPU project evidence promotion:** none  
**Canonical starting main:** `b3252a556b61b7e566d5e057606c1f2e917d79e8`

## Primary sources and source-reported results

### 1. Experimental non-Hermitian exceptional-point route

W. F. Yuan et al., “Beating Hermitian Speed Limits for Entanglement Generation via Exceptional Points in a Trapped-Ion System,” *Physical Review Letters* **136**, 210201, published 28 May 2026 (issue dated 29 May 2026). DOI: [10.1103/g8v5-rbq7](https://doi.org/10.1103/g8v5-rbq7). Official publisher record: https://journals.aps.org/prl/abstract/10.1103/g8v5-rbq7.

The authors report a two-trapped-ion experiment implementing a parity-time-symmetric effective Hamiltonian near an exceptional point. They report faster maximally entangled-state generation than the bound for an equivalent Hermitian interaction, accompanied by lower success probability as the exceptional point is approached.

**Correct interpretation:** this is a result relative to a specified Hermitian comparison, not evidence that every universal quantum speed limit has been violated. The conditional/non-Hermitian description and its success-probability trade-off must be evaluated against the complete physical protocol, including unsuccessful outcomes and the resources needed to repeat them.

### 2. Transition-rate quantum speed limits for open processes

Adolfo del Campo, András Grabarits, Dmitrii E. Makarov and Seong-Ho Shinn, “Quantum Transition Rates in Arbitrary Physical Processes,” *Physical Review Letters* **136**, 210202, published 28 May 2026. DOI: [10.1103/l7dq-n61h](https://doi.org/10.1103/l7dq-n61h). Official publisher record: https://journals.aps.org/prl/abstract/10.1103/l7dq-n61h.

The authors define time-dependent transition rates between an initial subspace and a target subspace using flux-flux correlators, derive two complementary quantum speed limits, and describe an extension to arbitrary open quantum evolution including measurements. Counterdiabatic driving is given as a control example.

This is a theoretical framework, not a UQPU reproduction or a measurement of device-level latency, energy or cost.

## Genuine relevance to UQPU

The two papers suggest a useful paired audit for FND-003: distinguish (a) a bound under a stated Hamiltonian and control budget, (b) an optimized model trajectory, (c) conditional success time, and (d) total resources per accepted useful output. A faster successful trajectory may lose at the system level if success probability falls or if control, reset, measurement, reservoir, retry and cooling resources dominate.

This supports FND-001 thermodynamic-gap accounting and FND-004 alternative-primitive research, while keeping the current physics and the precise premises of each bound binding. It also strengthens Lane A's requirement that execution success is not output-quality acceptance.

## Limits and non-claims

- The trapped-ion experiment is specific to its engineered two-ion protocol and comparison Hamiltonian. It does not establish a general speedup for arbitrary algorithms, a quantum advantage over a classical baseline, or a faster accepted UQPU workload.
- The effective non-Hermitian description must not be treated as a closed, trace-preserving physical process by itself. A reproduction must include the failed outcomes and a consistent open-system/dilation description.
- The transition-rate paper supplies a framework and derived bounds; UQPU has not independently reconstructed its derivations or verified a target-specific control schedule.
- No UQPU hardware was contacted. No QPU job, shots, physical experiment, wall-plug energy, cost per accepted task, or commercial result was measured.
- These sources do not establish a new physical law, Pangola-carbon substitution, accepted bio-oil, net fusion electricity, lower financing rates, or Data-Center-to-One-Phone feasibility.

## Falsifiable follow-up — FND003-NH-EP-001

1. Pin the paper versions, model equations, source parameters, solver versions and numerical tolerances. Retain the precise Hermitian incumbent and its declared coupling/spectral-width/control budget.
2. Build two independent open-system evaluators for a small model: one based on the declared master-equation/dilation formulation and one independently implemented trajectory or direct numerical route. Validate both against a simple Hermitian limit.
3. Freeze identical initial states, target subspace, target fidelity/error, allowed controls and measurement boundary for the Hermitian and exceptional-point arms. Do not compare a conditional state-transfer time with an unconditional accepted-output time.
4. Sweep held-out coupling strengths, exceptional-point detuning, noise and initial states. Include calibration uncertainty, imperfect control, leakage, failed trajectories, reset/readout and the resource cost of unsuccessful attempts.
5. Report separately: theoretical QSL, optimized model time, conditional success time, success probability, accepted-output quality, empirical wall-clock time per accepted output, measured energy if available, and total cost. Use actual totals and accepted counts; do not infer system advantage from gate time alone.
6. Check units, normalization, trace preservation for the complete physical channel, complete positivity where applicable, causality/no-signalling, the Hermitian limiting case and all energy flows into the controller/reservoir. Keep every failed or inconclusive run.
7. Require independent replay before accepting a model-level result. A model or simulation result remains `MODEL_ONLY`/`SIMULATION`; a technology claim needs an authorized, target-matched experiment and complete accepted-task accounting.

**Falsifier:** reject the proposed system-level advantage if the faster conditional trajectory disappears under matched controls and quality, or if retries, failed outputs, control/reset, dissipation, energy or cost erase the gain. If only the source-specific trajectory effect is reproduced, report only that narrower result.

## A–H and permanent-invariant interface

- **A:** define the same accepted-output/control contract; this is secondary to the open exact-head signed-Max-Cut SDK gate.
- **B:** preserve provider-neutral adapters; any future provider result must retain its own target, calibration, billing and job provenance.
- **C:** account for quantum state, readout, failed outcomes, reset, reconstruction, memory and data movement; Hilbert-space dimension is not readable classical storage.
- **D/G:** co-design control bandwidth, coupling, dissipation, calibration and manufacturability; no device or yield claim follows from the papers.
- **E:** charge controller, reservoir, dissipation and cooling in the thermodynamic boundary; no material, fuel or fusion result.
- **F:** compare measured total time/energy/cost per accepted output; do not combine a probability from one target with another target's price.
- **H:** preserve source provenance, multilingual strategic references and the Kanusanan Pongpanna Model; literature is context, not project evidence.

INV-029 remains the physical-compression North Star; INV-030–032 remain material/accepted-liquid/net-electricity evidence gates; INV-033 keeps principal and capital-lock-up effects distinct from WACC/rate claims; INV-034–035 keep foundational alternatives open while requiring explicit assumptions, constraints, falsifiers, held-out predictions and independent validation. INV-025/026/027 remain intact.

## Next highest-value gate

First verify exact-head CI for the current pinned-Qiskit signed-Max-Cut gate. In parallel, run the small, offline FND003-NH-EP-001 reconstruction with frozen assumptions and two independent numerical routes. No paid hardware execution is authorized by this literature watch.
