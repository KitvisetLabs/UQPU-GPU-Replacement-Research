# Research gap — exact gate-specific quantum speed-limit reconstruction

**Gap ID:** RG-FND003-GATE-QSL-RECONSTRUCTION-001  
**Opened:** 2026-10-28  
**Primary owner:** Lane A — gate/runtime comparison contract  
**Cross-lane owners:** Lane D (Hamiltonian/control provenance), Lane F (measurement/economics), Lane H (publication)  
**Related:** FND-001, FND-003, FND-006, EQN-001–006, INV-029–035  
**Status:** OPEN / LITERATURE_ONLY / THEOREM NOT RECONSTRUCTED

## Question

Can a gate-specific operator quantum-speed-limit theorem provide a more informative necessary-condition check for UQPU gate scheduling than a generic state-based bound, while preserving the distinction between intrinsic gate evolution and end-to-end accepted-task performance?

## Incumbent assumption and candidate alternative

- **Incumbent comparison practice to challenge:** using one generic state-evolution limit or a nominal gate duration as though it were a gate-specific lower bound.
- **Candidate alternative:** Nelson and Barnes' accepted *Physical Review A* result, which the publisher record describes as a tight bound for unitary gate evolution under bounded Hamiltonian spectral width, with gate-dependent examples.
- **Scope:** theorem reconstruction only. This is not a proposal that established quantum mechanics is wrong and not a new physical law.

## Current evidence

The official APS accepted-paper record is https://journals.aps.org/pra/accepted/10.1103/28zn-ch8y (accepted 2026-10-15; DOI https://doi.org/10.1103/28zn-ch8y). It reports gate-specific limits for Hadamard, CNOT and Toffoli and a geometric space-curve interpretation. UQPU has not yet recovered the complete equations and assumptions, reproduced the calculations, or compared them with an independent optimal-control reference.

## Blocking unknowns

- Exact theorem statement, definitions, spectral-width convention and proof assumptions have not been independently transcribed.
- Gate equivalence convention (including global phase), allowed Hamiltonian controls, drift, control switching and duration boundary are not yet pinned.
- No independently coded reconstruction or counterexample search has run.
- No matched optimal-control comparison or device-specific Hamiltonian provenance exists.
- No physical gate latency, accepted-task latency, wall-plug energy, cost, or QPU result is produced by the source watch.

## Required mathematical and physical checks

1. **Dimensions:** spectral width has energy units; the characteristic time scale must be dimensionally consistent with Planck's constant divided by an energy scale. Use the exact theorem, not this dimensional check, for numerical evaluation.
2. **Symmetry/equivalence:** verify the paper's definition of identical unitary gates, including whether global phase is ignored; test basis changes only where the theorem states invariance.
3. **Conservation/causality:** preserve the theorem's unitary-evolution and bounded-resource assumptions. Do not extrapolate it to open-system, measurement, reset or dissipative operations without a separate theorem.
4. **Scaling/limits:** check the paper's exact scaling when the Hamiltonian is rescaled; inspect identity/trivial evolution and degenerate spectral-width cases under the theorem's stated domain.
5. **Counterexamples:** search small-dimensional gate/control cases and compare independent numerical bounds. A mismatch first triggers formula, convention, optimization and numerical-error audits.
6. **Held-out prediction:** after fixing the implementation, test gate families and control budgets not used to reconstruct the examples.
7. **Independent validation:** obtain a separate proof review and reproduce the numerical cases from pinned inputs.

## Acceptance protocol

1. Pin the accepted-paper version and store a source hash and equation-by-equation reconstruction.
2. Independently implement the theorem and its assumptions checks; tests must fail closed for missing spectral-width, endpoint, gate-equivalence or control metadata.
3. Reproduce the published gate examples within predeclared tolerances and archive negative/inconclusive results.
4. Compare against a distinct numerical optimal-control implementation on small instances and held-out gates.
5. For later device work, bind target, native gate, calibration, Hamiltonian/control model, fidelity/leakage, timing boundary and output contract to one immutable record.
6. Record separately: theorem lower bound; physical pulse duration; compiled circuit critical path; fault-tolerant logical runtime; full accepted-task latency; shots/retries; host compute; memory/I/O; measured energy boundary; provider price; total cost per accepted useful task.
7. Only after these gates pass may any result inform a hardware or economic hypothesis. Paid QPU execution still requires credentials, a bounded budget and explicit user consent.

## Falsifiers and stop rules

- If the theorem cannot be reconstructed from the source, stop before implementing a numerical bound.
- If an independent derivation fails the published examples, classify the reproduction as failed/inconclusive and retain the counterexample; do not silently tune the formula to fit.
- If an observed evolution appears faster than the bound, first audit the exact assumptions, endpoint equivalence, Hamiltonian norm/spectral width, time boundary and numerical uncertainty. Only a verified contradiction under all assumptions merits scientific escalation.
- A bound that is valid but far below measured gate times is still only a necessary limit; it does not establish practical speedup.
- No mismatch-free gate-level result alone proves a quantum algorithm advantage or Data-Center-to-One-Phone capability.

## Mission boundary

No evidence is added for INV-029 phone-class physical compression, INV-030 Pangola material substitution, INV-031 accepted bio-oil, INV-032 net delivered fusion electricity, or INV-033 reduced financed principal/interest/WACC. FND-001 still requires measured whole-system energy, FND-002 still requires output-information accounting, and EQN-001–006 remain evidence-gated. Current physical limits remain binding.
