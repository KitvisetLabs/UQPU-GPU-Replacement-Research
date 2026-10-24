# Integration record — INT-20261025-001

**Date:** 2026-10-25  
**Source main SHA:** c7b5958af58fad04a101ef5c6abf6a29293c867e  
**Status:** TESTING (analytic scalar check only); spin–photon transfer edge PROPOSED  
**Primary owners:** Lane A for the response-audit code; Lane H for literature provenance; Lane D/E for any future interface/material follow-up  
**Evidence class:** MODEL_ONLY + LITERATURE_ONLY; no physical or commercial evidence promotion

## Stable inputs and outputs

- FND-QFI-002 — software/uqpu-prototype/uqpu/qfi_response_bound.py
- Unit tests — software/uqpu-prototype/tests/test_qfi_response_bound.py
- Result — benchmarks/results/fnd-qfi-response-bound-2026-10-25.json
- Literature source — docs/literature_watch/2026-10-25-qfi-response-bound-and-spin-photon-interface.md
- Source paper — https://arxiv.org/abs/2610.14454
- Material/interface paper — https://arxiv.org/abs/2610.24925

## Candidate edge A ↔ FND/EQN

**Hypothesis:** a QFI-directional-response audit may help diagnose whether an optimizer's first-order physical response is absent before debugging measurement, feature-span, readout or task-projection losses.

**Contract:** for the same state, observable, parameterization, sample and direction \(v\), audit
\[
|D_v\langle O\rangle|^2 \le (v^\top F_Qv)\operatorname{Var}(O).
\]
The analytic pure-qubit fixture saturates this inequality for X and Z observables at four parameter values. Negative controls reject nonzero response when the supplied directional QFI is zero and reject a slope above the envelope.

**What this does not test:** QFI calculation from arbitrary density matrices, the full retrained-loss gradient bound, a QPU workload, QOS/QSVT route conformance, speedup, total cost or energy. The next gate is a separate mixed-state implementation with independent finite-difference validation and rank/zero-eigenvalue counterexamples.

## Candidate edge D ↔ E

**Hypothesis:** the reported symmetry-breaking ligand-field approach may be a useful interface-design reference if a concrete device requires optical access to a molecular-spin state.

**Boundary:** the preprint uses aqueous Cu(II) with EDTA. It does not show Pangola carbon replacing copper or EDTA, nor a UQPU chip integration. No material substitution edge is accepted yet.

**Unlock criterion:** a lane-owned device requirement and matched functional contract must exist first; any later comparison needs controlled concentration, optical geometry, temperature/field, coherence, selectivity, power, lifetime, manufacturing and lifecycle cost.

## Finance and system integration

Lane F/H retain full-system cost and financing boundaries. Neither preprint provides measured UQPU accepted-task economics, a lower required principal, lower absolute interest expense, or a reduced WACC. No speculative efficiency factors may be multiplied together.

## A–I pair scan (36 pairs)

| Pair | Screen result |
|---|---|
| A–B | Existing provider-neutral adapter boundary retained; no provider call. |
| A–C | State/data-movement accounting remains required; QFI is not memory equivalence. |
| A–D | No device requirement derived from the scalar audit. |
| A–E | No biomass/energy path from this optimizer result. |
| A–F | Selected edge: QFI-response diagnostic contract; MODEL_ONLY. |
| A–G | No fabrication process requirement. |
| A–H | Literature-to-runtime hypothesis handoff retained. |
| A–I | No vehicle-control or propulsion consequence. |
| B–C | No target snapshot or transfer measurement. |
| B–D | No calibrated target/device interface. |
| B–E | No energy/material measurement. |
| B–F | Provider-matched economics remains blocked. |
| B–G | No hardware target/process response. |
| B–H | No access or funding consequence. |
| B–I | No provider/vehicle integration. |
| C–D | No state-interface-to-device requirement. |
| C–E | No new storage/thermal/material integration. |
| C–F | No memory/I/O cost measurement. |
| C–G | No memory-device manufacturing requirement. |
| C–H | No strategic storage-cost evidence. |
| C–I | No vehicle power/data/thermal evidence. |
| D–E | Proposed interface-design lead only; no accepted material substitution. |
| D–F | No device lifecycle-cost data. |
| D–G | Continuous co-design retained; no new process window or yield input. |
| D–H | No manufacturing capital or funding change. |
| D–I | No propulsion device consequence. |
| E–F | BIO-001/FUS-001 accepted-function cost gates unchanged. |
| E–G | No process equipment or material qualification. |
| E–H | Strategic material/energy pathway unchanged; no financing evidence. |
| E–I | No biomass/propulsion integration evidence. |
| F–G | No factory CAPEX/yield model update. |
| F–H | Finance boundary reaffirmed: principal/time/risk distinct from WACC. |
| F–I | No passenger-km economics. |
| G–H | No factory-finance consequence. |
| G–I | No manufacturing/vehicle interface. |
| H–I | No strategic-finance/vehicle consequence. |

## Invariant review

- INV-029: no physical phone-class compression claim.
- INV-030: no elemental transmutation or universal material substitution.
- INV-031: no commercial low-cost bio-oil result.
- INV-032: no net delivered fusion-electricity result.
- INV-033: no principal/interest/WACC result.
- INV-034: present limits remain binding; the QFI inequality is an assumption-scoped audit.
- INV-035: AI may propose candidates; independent proof/experiment and replication remain mandatory.
- INV-025/026/027: no moonshot promotion; Hilbert-space size is not readable classical memory.

## Negative evidence and next gate

The local isolated unit suite passed six test methods. The full repository suite and hosted CI were not available to this run's local environment. GitHub commit-status lookup for the source main SHA returned no status entries, and the available workflow-run connector returned no runs for this merge commit; this is **unknown CI state**, not a pass.

Next: merge this branch only after the PR's repository checks validate the package and cold-start provenance; then implement the mixed-state QFI test harness. No paid QPU, provider session, material purchase, hazardous experiment or financing action is authorized by this record.
