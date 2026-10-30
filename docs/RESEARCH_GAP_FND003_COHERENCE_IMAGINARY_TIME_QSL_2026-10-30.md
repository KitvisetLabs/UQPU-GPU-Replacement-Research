# Research gap — RG-FND003-COHERENCE-IMAGINARY-TIME-QSL-001

**Opened:** 2026-10-30  
**Primary owner:** Lane H — literature provenance; technical contract owner Lane D  
**Cross-lane owners:** A (workload/control timing), B (provider timing), C (state/measurement), F (matched evidence and economics)  
**Related:** FND-001, FND-003, EQN-001/005/006, INV-029/034/035  
**Status:** OPEN / PEER-REVIEWED THEORY INDEXED / FULL-TEXT RECONSTRUCTION PENDING  
**Evidence class:** PEER_REVIEWED_THEORY; abstract-level source review only.

## Objective

Determine whether coherence-resolved unitary quantum speed limits or geometric imaginary-time bounds add a valid, workload-relevant comparator to the project's matched control-versus-quantum speed-limit accounting.

## Sources and scope

1. Xiao, Wang and Qiu, “Coherent quantum speed limits,” *Phys. Rev. A* 113, 032438 (2026-03-24), DOI 10.1103/rdpr-db6m; related preprint arXiv:2401.01746. The abstract describes Schatten-p-norm and Hellinger-distance coherence measures relative to the instantaneous energy eigenbasis for general unitary dynamics.
2. Kobayashi, “Saturable quantum speed limits for imaginary-time evolution,” *Phys. Rev. A* 113, 032618 (2026-03-19), DOI 10.1103/bln8-8xzy; related preprint arXiv:2508.10361. The abstract describes a geometric lower bound for a non-unitary imaginary-time Schrödinger evolution, with an explicit saturability condition.

The sources are theoretical results. The full APS papers were not reconstructed in this cycle. The second source concerns imaginary-time evolution and must not be equated with physical wall-clock time or a freely available hardware primitive.

## Missing evidence

- Full theorem statements, definitions, proof assumptions and equality conditions.
- Dimensional, normalization, basis-dependence and limiting-case checks against standard QSL formulations.
- Exact relation to Margolus–Levitin and Mandelstam–Tamm bounds in the workload's regime.
- Reproducible small-Hamiltonian examples with independently implemented calculations.
- For imaginary-time implementation: success probability, normalization, ancilla/postselection, repetitions, state preparation, classical feedback and physical-time/energy overhead.
- For any claimed control comparison: identical useful-output quality, same initial/target states, Hamiltonian/resource boundary, controller and wall-plug accounting.

## Falsifiable follow-up

1. Retrieve full publisher text and any supplementary derivations; hash source versions and record access limitations.
2. Re-derive the bounds and check dimensions, basis covariance, assumptions, equality cases and known limits.
3. Implement a small exact numerical evaluator for fixed two-level and Landau–Zener examples; compare with independent symbolic/numerical code.
4. Add held-out Hamiltonian families and counterexample searches; retain cases where the bound is loose, inapplicable or incorrectly implemented.
5. Design matched control/quantum tasks with identical accepted outputs. Record state distance, coherence measure, energy dispersion, physical evolution time, controller time, wall-plug energy, repetitions, host work and cost.
6. Treat any imaginary-time realization as a separate implementation contract; include normalization and sampling overhead rather than reporting algorithmic imaginary time as hardware speed.

**Non-claims:** no new physical law, device measurement, QPU runtime improvement or useful-output speedup is established.
