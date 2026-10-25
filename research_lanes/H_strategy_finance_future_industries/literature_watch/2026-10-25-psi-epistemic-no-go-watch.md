# Literature watch — 2026-10-25: two-state qubit no-go theorem for maximally ψ-epistemic models

**Accessed:** 2026-10-25  
**Primary owner:** Lane H — foundational research publication and strategic synthesis  
**Integration owner:** Lane F — evidence, benchmark and cross-lane accounting  
**Feeds:** A–H; especially FND-005/FND-006 and EQN-005/EQN-006  
**Evidence class:** APS_ACCEPTED_PAPER (accepted 2026-10-15; APS labels it an accepted paper, not a verified version of record)  
**Project evidence promotion:** none  
**Canonical starting main:** b5aac63f295c2b586f044bcbb228ad0ffb0660ef

## Source and genuine delta

Sagnik Ray, Anubhav Chaturvedi and Debashis Saha, “No-go theorem for maximally ψ-epistemic models using two pure states of a qubit,” Physical Review A, accepted 15 October 2026. DOI: https://doi.org/10.1103/x382-1cwk. Official APS accepted-paper record: https://journals.aps.org/pra/accepted/10.1103/x382-1cwk.

The result is a scoped quantum-foundations theorem. The authors report that a maximally ψ-epistemic model cannot reproduce the relevant statistics for non-projective measurements on a pair of single-qubit pure states, despite the Kochen–Specker model's maximally ψ-epistemic construction for a single qubit under projective measurements. Their construction uses a two-input, three-output game (RAD), two pure states and their equal mixture; the analysis generalizes operational/ontological overlap quantities and optimizes a difference of generalized overlaps.

The useful delta for UQPU is not a new computational primitive. It is a sharper, operationally specified exclusion result that can help prevent informal assumptions about quantum-state interpretations from being treated as interchangeable across measurement classes.

## Evidence and limitations

- This is a mathematical result reported in an APS accepted-paper record. The project has not independently reconstructed the proof or reproduced its optimization.
- The theorem is about the stated maximally ψ-epistemic model class and measurement/state assumptions. It does not rule out every ontological model, settle every interpretation of quantum mechanics, or modify the Born rule.
- The result does not establish a new physical law, computational speedup, better QPU, new elementary particle, lower energy, or improved material.
- An operational score gap is not by itself a device-independent experiment: state preparation, measurement implementation, calibration, finite statistics and the precise game assumptions still need to be bounded.
- This paper is distinct from the already tracked tripartite-Haar entanglement and Gaussian-repeater no-go results. Those theorems have different premises and conclusions and must not be conflated.

## Proposed falsifiable follow-up: FND-005-PSI-EPISTEMIC-001

1. Freeze the accepted-paper version, theorem statement, definitions of the two states, allowed non-projective measurement, RAD payoff and all assumptions. Record a source hash and any later version-of-record change.
2. Independently derive the relevant overlap inequality and RAD score bound. Use exact arithmetic where possible; otherwise use interval arithmetic with a preregistered numerical tolerance. Archive the derivation and executable fixture.
3. Build positive and negative controls: the projective-measurement case, the specified non-projective case, exchanged state labels, and perturbations of the mixture probability. Search for counterexamples within the theorem's stated assumptions rather than changing the assumptions silently.
4. Compare the reproduced bound against a separate implementation and independent reviewer. A numerical optimizer returning the same score is not a proof of the theorem.
5. Only if an operational test is useful, preregister a calibrated single-qubit experiment with state-preparation/measurement error, finite-shot confidence intervals, leakage and drift accounted for. The observable is the RAD score distribution versus the bound; failure to resolve the predicted gap is a negative/underpowered result, not evidence for an alternative ontology.
6. Keep all proof, simulation and laboratory evidence labels separate. Any claim about computation, energy or economics requires its own matched useful-output benchmark.

**Falsifier for the reproduction gate:** an independently checked derivation or counterexample shows that the source's stated inequality does not follow from its definitions and assumptions, or a frozen numerical fixture violates the derived bound beyond the declared error budget. Any source-version or assumption mismatch blocks the gate rather than being patched after observing results.

## Lane and invariant impact

- **A — programming/workloads/compiler/runtime:** no compiler or algorithm change. A formal fixture may later be useful for measurement-semantics regression.
- **B — cloud/QPU/provider integration:** no credentials, provider calls, jobs, shots or billing.
- **C — memory/state/data movement:** no readable-memory equivalence claim; ontology does not change output-information accounting.
- **D — devices/chips/process/packaging:** no hardware or fabrication consequence established.
- **E — materials/biomass/bio-oil/fusion/cooling:** no Pangola substitution, accepted fuel, net-electric fusion or cooling result.
- **F — economics/evidence/integration:** record source provenance and all reproduction failures; no measured cost or financing effect.
- **G — manufacturing/factory systems:** no process-window, yield or tooling consequence.
- **H — strategy/publication:** primary owner of this scoped literature watch. The strategic plans remain context, not scientific proof.

## Foundational and mission boundary

- **FND-001–004:** no thermodynamic, output-information, matched speed-limit or alternative-primitive measurement is supplied.
- **FND-005:** adds a quantum-foundations theorem lead; it does not establish a QFT/particle mechanism or anomaly.
- **FND-006 / EQN-001–006:** supports mathematics-first, assumption-explicit reasoning; it does not generate or validate a new physical equation.
- **INV-029:** no Data-Center-to-One-Phone closure.
- **INV-030:** no elemental transmutation or critical-material substitution.
- **INV-031:** no saleable bio-oil yield or full cost.
- **INV-032:** no reliable net-electric fusion or lifecycle-cost result.
- **INV-033:** no financed-principal, interest, WACC or time-to-evidence change.
- **INV-034:** foundational mathematics remains an upstream research layer.
- **INV-035:** established physical equations remain binding; a theorem about model classes is not a declaration of a new physical law.

No paid QPU job, physical experiment, purchase, funding action or external spending was authorized. The 100× and 100,000,000× targets and all mission outcomes remain unproven until their independent evidence gates pass.

## Next gate

Implement the frozen analytic/numerical reproduction only after the source version and assumptions are pinned. Keep this literature lead LITERATURE_ONLY until an independent proof/replication exists; even a successful theorem reproduction is not a technology or economic result.