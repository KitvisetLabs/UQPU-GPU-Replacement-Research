# Lane A contract — open-system invariant toy fixture

**Date:** 2026-10-29  
**Stable ID:** UQPU-OPEN-QSYS-TOY-001  
**Primary owner:** Lane A — quantum programming/workload/runtime  
**Interfaces:** Lane B open-system model assumptions; Lane F evidence/acceptance; Lane H provenance  
**Implementation:** `software/uqpu-prototype/uqpu/open_quantum_invariant_toy.py`  
**Tests:** `software/uqpu-prototype/tests/test_open_quantum_invariant_toy.py`  
**Evidence class:** MODEL_ONLY / deterministic software fixture

## Declared model

Use a single-qubit Pauli coefficient basis ordered `(I, X, Y, Z)). The declared Heisenberg-picture pure-dephasing generator maps (I\mapsto0), (Z\mapsto0), (X\mapsto-\gamma X), and (Y\mapsto-\gamma Y), with finite `gamma >= 0). Candidate basis vectors must be finite, correctly dimensioned, and linearly independent.

The evaluator returns two separate checks:
1. whether each generator image lies in the candidate linear span;
2. whether every pairwise operator product lies in that span.

Both checks are required for `passes_exact_toy_checks`. Passing does not imply measurement identifiability, a decoherence-free structure, experimental confirmation, or physical advantage.

## Deterministic acceptance fixtures

| Candidate span | Expected invariance | Expected algebra closure | Expected result |
|---|---:|---:|---|
| span`{I,Z}` | Pass | Pass | Pass toy checks |
| span`{I,X,Y}` | Pass | Fail | Reject |
| span`{I,X+Z}` | Fail for gamma > 0 | Pass | Reject |
| span`{I,X,Y,Z}`, gamma = 0 | Pass | Pass | Pass toy checks |

The test suite also rejects dependent basis vectors, non-finite coefficients, invalid generator rates, invalid tolerance and malformed vectors. Failed cases remain part of the benchmark rather than being removed.

## Evidence and next gate

Nine test methods passed in the equivalent local standard-library reference harness during this cycle. The repository's committed test file must still pass exact-head GitHub Actions; no full CI result is inferred. This fixture is not the complete Batch 130 structural-identifiability benchmark and contains no shot noise, model inference, hardware, cost or energy measurement.

Next: check exact-head Actions, add a second analytically known generator, then connect the toy oracle to the preregistered family-disjoint benchmark. Keep provider-neutral lowering, reference certificates, competitive classical baselines and total resources per accepted useful task as separate gates.
