# Research gap RG-STATEPREP-TOFFOLI-001 — sparse state-preparation Toffoli model alignment

**Opened:** 2026-10-29  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Interfaces:** Lane C state/memory/data movement; Lane F benchmark/evidence/cost; Lane B provider adapters; Lanes D/G device and manufacturing resource models; Lane H publication/provenance  
**Status:** OPEN / LITERATURE-ONLY / INDEPENDENT REPRODUCTION REQUIRED  
**Source:** Rupprecht and Wölk, *Quantum* 10, 2208 (2026), DOI 10.22331/q-2026-09-10-2208.  
**Related:** RG-STATEPREP-SPARSE-001, RG-QROM-SPARSE-001, INV-025/026/027, INV-029, INV-034/035.

## Objective

Determine whether the peer-reviewed improved sparse-isometry construction yields a reproducible reduction in complete state-preparation resources for a frozen UQPU workload after aligning target-state semantics, support promises, amplitude representation, approximation error, classical preprocessing and gate-cost model.

## Current evidence

The publisher abstract reports an isometry circuit with worst-case Toffoli cost approximately 2s for sufficiently large n, and random-state numerical costs closer to s. These are external algorithmic/resource results. UQPU has not independently reproduced the circuits or verified the resource comparison. No project-specific runtime, energy, memory, provider price or accepted-task advantage is measured.

The existing software/uqpu-prototype/uqpu/sparse_stateprep_bounds.py records the Luo–Li asymptotic theorem symbolically and explicitly marks comparison with sparse-QROM as NOT_ESTABLISHED. The Rupprecht–Wölk Toffoli result must be added as a separate model until the theorem and gate models are reconciled. Do not overwrite the existing bound or infer a contradiction from different metrics.

## Blocking unknowns

- Exact construction, input promise and assumptions needed to use the sparse isometry.
- Whether the authors' code/assets reproduce the reported small cases and resource tables.
- Toffoli-to-T-count decomposition and the effect of target gate set, depth, routing, ancillas and fault-tolerant factory resources.
- Classical preprocessing time, support discovery, amplitude-description bytes and storage/transfer cost.
- Accuracy/fidelity and the cost of downstream measurements and output reconstruction.
- Held-out behavior for real/complex amplitudes, highly nonuniform distributions and support-boundary cases.
- A frozen useful-output workload and competitive classical baseline.

## Acceptance gate

1. Pin the paper version and code/assets; retain hashes and provenance.
2. Reproduce exact small instances against an independent classical reference.
3. Compare the Rupprecht–Wölk, Luo–Li and sparse-QROM statements in a theorem/assumption matrix; keep Toffoli and T-count columns separate.
4. Freeze disjoint training/validation/held-out (n, s, epsilon) cases and search counterexamples at support and precision boundaries.
5. Record correctness/fidelity, Toffoli count, decomposed T-count, depth, ancillas, classical preprocessing, input-description bytes, transfer, host work and reconstruction.
6. Only then evaluate cost per accepted useful task against a competitive classical baseline. Hardware execution remains simulator/dry-run first; paid execution requires credentials, a bounded budget and explicit user consent.

## Explicit nonclaims

This gap establishes no universal state-preparation improvement, no lower bound beyond the cited theorem's scope, no readable classical-memory equivalence, no 100,000,000-unit replacement, no physical law, and no UQPU hardware, energy or cost advantage.
