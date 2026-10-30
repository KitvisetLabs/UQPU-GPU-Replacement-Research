# D/G transfer contract — DG-AGENTIC-CODESIGN-001

**Primary owner:** Lane D  
**Co-owner:** Lane G  
**Date:** 2026-10-30  
**Evidence:** LITERATURE_ONLY; reproduction not run  
**Source:** Chung et al., arXiv:2604.21804v3 (2026-10-20)  
**Gap:** ../../docs/RESEARCH_GAP_DG_AGENTIC_DETECTOR_COSIGN_REPRODUCTION_2026-10-30.md

## Interface

The source method supplies a reusable workflow pattern, not transferable detector physics:

`design variables + physical/process constraints
 -> simulator/full-order model
 -> digitization/control/reconstruction model
 -> deterministic objective + feasibility evaluator
 -> agent proposes next design
 -> held-out validation
 -> measured device/process qualification
 -> lifecycle economics`

The agent is advisory. It does not own simulation truth, constraint validation, acceptance, evidence classification or merge decisions.

## D/G responsibilities

**Lane D — device and process semantics**
- Name the device function and accepted-output metric.
- Define design variables, units, physical domain and calibrated model.
- Supply coherence, fidelity, coupling, loss, power, thermal and reliability constraints as relevant.
- Identify simulation-to-measurement discrepancy and the independent device validation path.

**Lane G — manufacturing and factory constraints**
- Define lithography/deposition/etch/cleaning/assembly/packaging/metrology variables where relevant.
- Supply process windows, critical dimensions, defectivity, throughput, tool availability, wafer/device yield and test limits.
- Reject geometries or process settings that cannot be manufactured or inspected.
- Include equipment utilization, maintenance, consumables and yield-adjusted capital cost.

## Mandatory comparison

Compare agent-guided search with exhaustive enumeration on small spaces, random/LHS, an established optimizer and expert design. Hold fixed the expensive simulation budget, model, data, constraints, objective scaling, seeds, held-out regimes, CPU/GPU/wall-clock/memory budget and monetary/token budget. Record all invalid/failed candidates.

## Acceptance and promotion

A software-level result requires reproducible source/config/data hashes, exact objective and feasibility checks, held-out improvement, counterexample search, equal-budget baselines and exact-head CI. A device/manufacturing claim additionally requires independent measured device/process data and yield-aware lifecycle accounting.

No candidate is a new physical law by declaration. Any changed physical or constitutive model must satisfy INV-035 and the existing FND/EQN hypothesis gates. No calorimeter-specific power, cost or geometry coefficient may be imported as a quantum-chip value.
