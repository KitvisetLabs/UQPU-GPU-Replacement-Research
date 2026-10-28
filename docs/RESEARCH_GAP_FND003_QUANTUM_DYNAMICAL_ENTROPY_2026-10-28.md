# Research gap — quantum dynamical entropy and the conjectured Planckian rate

**Gap ID:** RG-FND003-QUANTUM-DYNAMICAL-ENTROPY-001  
**Opened:** 2026-10-28  
**Primary owner:** Lane H — source provenance / literature  
**Cross-lane owners:** Lane A (matched control protocol), Lane B (provider/readout interface), Lane C (measurement/state/I/O), Lane F (evidence and cost gate)  
**Status:** OPEN / LITERATURE_ONLY / FULL_TEXT_AND_REPRODUCTION_PENDING  
**Source:** Cao, *Phys. Rev. Lett.* 137, 030402 (2026-07-13), DOI https://doi.org/10.1103/wd91-v58h  
**Evidence boundary:** peer-reviewed theory; the universal Planckian entropy-rate bound is presented as a conjecture in the accessible abstract.

## Question

Can the observable-specific dynamical-entropy rate for continuous monitoring of thermal fluctuations be independently reconstructed and tested in a finite, controlled many-body model, with its assumptions separated from generic gate-time and end-to-end useful-task claims?

## Known from the official abstract

The work defines a simplified quantum dynamical entropy associated with continuously monitoring an observable, calculates a thermodynamic/long-time entropy rate in terms of two-point correlation functions, and conjectures a universal Planckian rate bound. It also discusses purification rate. This source is not the same theorem as the separate Planckian thermalization-machine bound already tracked under FND-003.

## Missing evidence

1. Full-text and supplement access sufficient to verify definitions, constants, assumptions, and the exact conjecture.
2. Independent symbolic derivation and dimensional checks.
3. Finite-size/finite-time numerical reproduction with uncertainty and held-out parameter regimes.
4. Counterexample search, including classical and large-system limits and changes in observation bandwidth.
5. A discriminating observable and experimental protocol before any hardware claim.
6. Separate accounting for measurement/control, state preparation, reset, cooling, host processing, I/O, and accepted-output reconstruction.

## Acceptance contract

- Do not encode the conjecture as a universal lower-bound function in `fundamental_limits.py` until the exact expression and scope are reconstructed.
- Keep entropy rate, thermodynamic heat/work, detector energy, wall-plug energy, gate duration, and accepted-task latency as distinct quantities.
- Use a matched null/control model, preregistered held-out regimes, and an independent implementation.
- A fit or simulation is MODEL_ONLY/SIMULATION, not a new physical law or UQPU advantage.
- Failure to reproduce the formula or any counterexample must be retained as a negative result.

## Next cheapest decisive action

Obtain and review the full paper/supplement, reconstruct one exactly solvable model, then run a deterministic finite-size/finite-time test with unit, limit, and counterexample checks. No QPU submission is required or authorized for this gate.
