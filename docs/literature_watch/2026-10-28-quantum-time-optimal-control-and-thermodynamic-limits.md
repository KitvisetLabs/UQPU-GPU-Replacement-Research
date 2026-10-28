# Literature watch — quantum time-optimal control and thermodynamic limits

**Checked:** 2026-10-28  
**Primary owner:** Lane H — literature surveillance  
**Cross-lane owners:** A (workload/runtime contract), B (quantum target evidence), C (state/memory accounting), D/G (device/control co-design), E (energy/cooling), F (measurement/economics)  
**Evidence class:** LITERATURE_ONLY for UQPU; one source reports a published single-qubit optical experiment  
**Related:** INV-034–035, FND-001, FND-003, FND-004, FND-006, EQN-001–EQN-006

## Fresh primary-source deltas

### 1. Efficient computation of quantum time-optimal control

Andrei A. Stepanenko, Kseniia S. Chernova, Maxim Mazanov and Maxim A. Gorlach, Physical Review A accepted **2026-10-21**, DOI https://doi.org/10.1103/rsjw-pk53. Official source: https://journals.aps.org/pra/accepted/10.1103/rsjw-pk53

The publisher describes a method combining quantum brachistochrone and Lax-pair techniques. Its example is single-particle excitation in a nearest-neighbor-coupled qubit lattice with switchable couplings and a fixed sum of squared couplings; reported analytic/numerical cases include finite lattices up to 10,000 qubits and an effectively infinite ring.

**Novelty relevant here:** a concrete route to compute optimal-time bounds under a declared control budget, potentially useful for checking whether a proposed gate/control schedule is even close to time-optimal.

**Limits:** this is not evidence of a UQPU speedup, real device latency, energy advantage or end-to-end task improvement. Its control assumptions and objective must match the target device before comparing it to a different QSL theorem. The accepted-paper page does not yet supply supplemental material.

### 2. No-go theorem for measurement-only steady-cycle work extraction

Kenta Koshihara and Kazuya Yuasa, Physical Review A accepted **2026-10-26**, DOI https://doi.org/10.1103/4kmf-nzsm. Official source: https://journals.aps.org/pra/accepted/10.1103/4kmf-nzsm

Under the paper's stated scope—a finite-dimensional working substance, bare quantum measurements, no feedback control and no thermal contact—the authors use a Poincaré-like recurrence argument to show that measurements become nondisturbing in the steady regime and cannot yield extractable work there.

**Novelty relevant here:** this is a scoped no-go result for claims that measurement backaction alone is a steady-cycle work source. It strengthens the need to account for feedback, thermal contact, state preparation and measurement/controller resources in FND-001/FND-004 models.

**Limits:** it is not a no-go theorem against all quantum engines or feedback-driven protocols. Changing assumptions must be explicit and the newly introduced resources must be charged to the full energy boundary.

### 3. Fundamental limits for thermodynamic control with quantum feedback

Kaiyuan Ji, Gilad Gour and Mark M. Wilde, Physical Review Letters accepted **2026-10-06**, DOI https://doi.org/10.1103/x67n-33gr. Official source: https://journals.aps.org/prl/accepted/10.1103/x67n-33gr

The publisher describes bounds on work of formation and extractable work with quantum side information, with a conditional-free-energy form of the generalized second law. It explicitly states that consistency with the traditional second law is restored when acquiring, processing and resetting side information are accounted for.

**Relevance:** a strong formal reminder for UQPU thermodynamic and memory/control ledgers: information available to a controller is not free, and reset/processing must remain in the accepted-task energy boundary. This is not a measured UQPU energy result.

### 4. Genuine quantum strong Mpemba effect by eliminating coherence

Xiang Zhan, Huixia Gao, Lei Xiao and Peng Xue, Physical Review Letters **published 2026-10-22**, DOI https://doi.org/10.1103/z9t9-mwgv. Official source: https://journals.aps.org/prl/abstract/10.1103/z9t9-mwgv

The article reports an optical setup simulating a Davies map, verifies the semigroup property, and demonstrates the strong Mpemba effect in a single-qubit system through elimination of coherence in the stated model.

**Evidence distinction:** this is a published experiment in a minimal optical quantum-thermodynamics setup, not a UQPU experiment, a universal relaxation-speed claim, a compute benchmark or proof of lower total energy per accepted task.

### 5. Thermodynamic speed limits in isolated quantum systems

Rikuya Kobashi, Physical Review Research accepted **2026-10-06**, DOI https://doi.org/10.1103/k16k-nx74. Official source: https://journals.aps.org/prresearch/accepted/10.1103/k16k-nx74

The publisher describes lower bounds on operation time using generalized second-law inequalities and a quantum-Wasserstein distance between coarse-grained states, with examples involving system–bath, local-energy and diagonal-entropy coarse-graining. Treat this as a candidate theorem family for FND-003, not a gate/runtime measurement.

## Exact UQPU relevance

- **FND-003 / Lane A-D:** reconstruct the assumptions and equations of gate-specific QSL and optimal-control approaches. Match Hamiltonian spectral width, control norm, allowed couplings, drift, boundary conditions, gate equivalence and error tolerance before comparing bounds. Intrinsic gate time is not accepted-task latency.
- **FND-001 / FND-004 / Lane E-F:** keep measurement, feedback, thermal contact, state preparation, controller operation, readout, reset, rejected attempts, wall-plug electricity and cooling distinct. A no-go theorem applies only within its formal assumptions; it cannot be generalized by slogan.
- **FND-006 / INV-035:** formalize candidate assumptions, check dimensions/symmetries/conservation/causality and limiting cases, search counterexamples, and preregister a discriminating observable before testing any model alternative.
- **INV-029 and cost/economics:** none of these sources demonstrates phone-class physical compression, quantum advantage, lower cost per useful task, lower WACC, cheaper bio-oil or net fusion electricity.

## Falsifiable follow-up

1. Independently transcribe the optimal-control and gate-QSL equations, units, admissible controls and proof assumptions; bind them to source version and hashes.
2. Implement two independent small-lattice solvers and compare time-optimal solutions over held-out sizes and control budgets. Verify objective value and constraints against a trusted reference.
3. Formalize the measurement-only no-go theorem under its exact assumptions. Search small finite-dimensional counterexamples; a valid counterexample must satisfy every stated premise, not silently add feedback or a bath.
4. If feedback or thermal contact is introduced, itemize its acquisition, processing, reset, actuation and dissipation costs and test a complete work/energy balance.
5. Reproduce the strong-Mpemba model only with pinned parameters and initial states; report relaxation observables and model scope separately from computational utility.
6. No claim advances beyond LITERATURE_ONLY for UQPU until independent reconstruction, held-out tests and the relevant device/system/economic gate pass.

**Decision:** these sources sharpen FND-001/003/004 gate design. They do not establish a new physical law or any UQPU, fuel, material, fusion-electricity, cost/task or mission-level advantage.
