# Literature watch — 2026-10-28 — exact gate quantum speed limits

**Primary source:** Hunter Nelson and Edwin Barnes, “Exact quantum speed limits for quantum gates from space curve geometry,” *Physical Review A*, accepted 2026-10-15.  
**Official publisher record:** https://journals.aps.org/pra/accepted/10.1103/28zn-ch8y  
**DOI:** https://doi.org/10.1103/28zn-ch8y  
**Accessed:** 2026-10-28  
**Evidence class:** ACCEPTED_THEORETICAL_PAPER / LITERATURE_ONLY for UQPU  
**Primary owner:** Lane A — workload/runtime and comparison contract  
**Cross-lane owners:** Lane D (Hamiltonian/control provenance), Lane F (matched evidence and economics), Lane H (publication); feeds FND-003 and INV-034/035

## Genuine contribution

The accepted-paper record describes a tight quantum speed limit for unitary gate evolution under a bounded Hamiltonian spectral width. The authors apply the framework to gates including Hadamard, CNOT and Toffoli, report that different gates can have different limits even when their entangling power is the same, and interpret time-optimal controls geometrically using space curves with a curvature constraint. The record describes a bottleneck principle: the slowest-evolving operator can set the minimum time for the full gate.

The useful UQPU delta is **gate-specificity**. A generic state-evolution bound may be too coarse for a compiler/runtime question. A verified operator-level bound could provide a more relevant necessary-condition check for a declared gate and Hamiltonian budget. It is a candidate theorem to reconstruct, not a measured performance result.

## Limitations and evidence boundary

- This cycle reviewed the official accepted-paper record and abstract; it did not reconstruct the full theorem, equations, proof, or numerical examples.
- The exact spectral-width convention, endpoint equivalence (including global phase), admissible controls, drift assumptions and gate-time definition must be recovered from the paper before implementation.
- A lower bound is not a predicted or achievable gate time. It does not imply that present hardware approaches the bound.
- Gate duration is not circuit critical-path time, fault-tolerant logical runtime, or end-to-end accepted-task latency.
- The theorem does not itself include error correction, routing, calibration, measurement/reset, classical orchestration, host compute, memory/I/O, cooling, wall-plug energy or provider charges.
- No UQPU experiment, QPU job, new physical law, quantum advantage, or end-to-end cost result is established.

## Exact UQPU relevance

- **Lane A / FND-003:** compare a gate-specific operator bound with matched gate implementations only after the theorem and its assumptions are independently reconstructed. Preserve identical input/output and acceptance contracts.
- **Lane B:** keep target identity, SDK version, native-gate set, calibration snapshot and pricing tied to one provider/target. No target availability or price change is inferred.
- **Lane C / FND-002:** do not infer readable classical storage or output-information capacity from Hilbert-space dimension or gate count.
- **Lane D/G:** the spectral-width/control assumption needs device-specific Hamiltonian and control provenance; no fabrication, control-electronics or yield advantage follows from the theorem.
- **Lane E / FND-001:** theoretical gate-time limits are not measured energy. Measure controller, actuation, readout, reset, refrigeration/cooling and idle-power energy on a consistent boundary.
- **Lane F / FIN-001:** any economic consequence must use accepted-task latency, retries, resource usage and target-specific prices; no principal, interest or WACC reduction is implied.
- **Lane H:** retain the distinction between mathematical bounds, engineering feasibility, strategic ambition and verified milestones.

## Falsifiable follow-up

1. Obtain and pin the full paper/version; transcribe the exact theorem, definitions and proof assumptions without substituting a remembered or guessed formula.
2. Independently check units, endpoint/gate equivalence, spectral-width convention, limiting cases and scaling under a rescaled Hamiltonian.
3. Reproduce the paper's Hadamard, CNOT and Toffoli examples using a separately implemented calculation; archive equations, parameters, tolerances and hashes.
4. Compare with an independently implemented numerical optimal-control search on small, held-out gate families. Record whether the search approaches the bound; do not interpret failure to saturate it as a theorem failure.
5. Use identical target gate, fidelity, leakage tolerance, timing boundary and calibration context for any hardware comparison. Keep gate time, circuit critical path, logical runtime and accepted-task latency as separate fields.
6. Preserve failed reconstructions, counterexamples and inconclusive cases. Independent review must precede any device or economic transfer.

**Decision:** add this source as an FND-003 theorem-reconstruction candidate. Do not implement a numeric bound from the abstract alone. Current physical constraints remain binding, and no new physical law or UQPU advantage is claimed.
