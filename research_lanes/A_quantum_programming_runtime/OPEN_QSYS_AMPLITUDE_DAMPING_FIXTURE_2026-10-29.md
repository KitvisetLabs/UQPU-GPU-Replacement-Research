# Lane A contract — amplitude-damping invariant-generator cross-check

**Date:** 2026-10-29  
**Stable ID:** UQPU-OPEN-QSYS-AMPLITUDE-DAMPING-001  
**Primary owner:** Lane A — quantum programming/workload/runtime  
**Interfaces:** Lane B model/target semantics; Lane C state and observable representation; Lane F evidence/acceptance; Lane H provenance  
**Implementation:** `software/uqpu-prototype/uqpu/open_quantum_invariant_toy.py`  
**Tests:** `software/uqpu-prototype/tests/test_open_quantum_invariant_toy.py`  
**Evidence class:** MODEL_ONLY / deterministic analytic software fixture

## Declared incumbent model

Use a one-qubit amplitude-damping Lindblad model toward the +1 eigenstate of Pauli Z, with finite rate gamma >= 0. In the Heisenberg picture and ordered Pauli coefficient basis (I, X, Y, Z):

- L†(I) = 0
- L†(X) = -(gamma/2) X
- L†(Y) = -(gamma/2) Y
- L†(Z) = gamma (I - Z)

For a candidate linear span A, test generator invariance L†(A) subseteq A and operator-product closure separately. The implementation returns a per-basis-image span-membership certificate and the tolerance used.

## Deterministic acceptance cases

| Candidate span | Invariance | Algebra closure | Expected |
|---|---:|---:|---|
| span(I,Z), gamma > 0 | Pass | Pass | Pass toy checks |
| span(I,X,Y), gamma > 0 | Pass | Fail | Reject |
| span(I,X+Z), gamma > 0 | Fail | Pass | Reject |
| span(I,X,Y,Z), gamma = 0 | Pass | Pass | Pass toy checks |

These cases exercise a second analytically known generator and preserve counterexamples to the mistaken inference that invariance alone implies an algebra or a decoherence-free structure.

## Scope and next gate

This extends the earlier pure-dephasing fixture; it does not implement the full restricted-measurement inference benchmark. No shot noise, identifiability, uncertainty calibration, non-Markovian model, device, real-QPU, energy, memory-replacement or cost experiment was run. The benchmark remains PREREGISTERED_NOT_RUN until family/regime holdouts, >=30 seeds, abstention, negative controls and resource accounting are executed.

**Non-claims:** no new physical law, quantum advantage, QPU speedup, readable classical storage, material substitution, accepted bio-oil, net fusion electricity, lower WACC or Data-Center-to-One-Phone closure.
