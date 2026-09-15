# Batch 052 — QOS phase-synthesis interface contract

**Date:** 2026-09-15  
**Program:** Issue #1 / QOS-AUDIT-010B1  
**Evidence level:** `PUBLIC_IMPLEMENTATION_INTERFACE_AND_CONVENTION_CONTRACT`  
**REAL_QPU:** No  
**Quantum advantage demonstrated:** No  
**GPU/NPU/RAM/DRAM/HBM replacement demonstrated:** No

## Result

Batch 051 closed exact all-real boundedness for the frozen degree-81 runtime polynomial but left phase synthesis open. Batch 052 performs the next narrow interface audit before any phase vector is allowed to become a resource input.

Public QSPPACK documentation exposes `qsppack.solve(coef, parity, opts)` for a definite-parity polynomial. It specifies that `coef` contains only the nonzero-parity Chebyshev coefficients in low-to-high order, and documents `parity`, `criteria`, `targetPre`, `method`, and `typePhi`. The documented minimal odd example uses `parity=1`, `method=Newton`, `targetPre=True`, and `typePhi=full`.

The repository now freezes that interface for the unchanged Batch-051 fingerprint:

`4364297169fe219da396c1d663680f474508a03afed93e321dc8e9d8f0bad13a`

with contract:

- package: `qsppack==0.3.0`;
- entry point: `qsppack.solve`;
- input: the 41 nonzero odd Chebyshev coefficients, low degree to high degree;
- parity: `1`;
- method: `Newton`;
- stopping criterion: `1e-12`;
- `targetPre=True`;
- `typePhi=full`;
- expected phase count on a converged degree-81 full sequence: `82`.

The executable adapter is fail-closed: a missing package, version mismatch, solver exception, or non-convergence cannot be promoted to synthesized phases. Even a converged solver return leaves `independent_reconstruction_passed=False` until a separate implementation reconstructs the response.

## Why this is publishable progress but not synthesis success

The previous gate said to pin a public implementation/version and exact convention before synthesis. This batch closes that interface/provenance sub-gate and makes the failure states executable. It does **not** claim that `qsppack==0.3.0` has yet converged on this degree-81 candidate in repository CI, because the current repository environment does not pin/install that external package.

This separation prevents an unpinned local environment or an implementation's own evaluator from silently becoming evidence for the phase gate.

## Public literature/software check

Checked 2026-09-15:

- QSPPACK solver documentation describes the Chebyshev coefficient order, parity argument, Newton/LBFGS/FPI/NLFT methods, `targetPre`, `typePhi`, convergence diagnostics, and a `0.5*x` odd-polynomial example.
- QSPPACK's public repository describes optimization-based and direct phase-factor solvers.
- pyQSP remains a useful independent implementation family and documents distinct Wx/Wz conventions; this reinforces the need to freeze convention mapping rather than compare phase vectors naively.

These are software/interface sources, not evidence of UQPU hardware performance.

## Artifacts

- `software/uqpu-prototype/uqpu/qos_d23_phase_synthesis_contract.py`
- `software/uqpu-prototype/tests/test_qos_d23_phase_synthesis_contract.py`
- `benchmarks/results/batch052-qos-phase-synthesis-interface-contract.json`
- `docs/BATCH_052_QOS_PHASE_SYNTHESIS_INTERFACE_CONTRACT.md`

## Next gate — QOS-AUDIT-010B2

1. add an isolated job that installs exactly `qsppack==0.3.0`;
2. execute `solve()` on the unchanged fingerprinted degree-81 coefficients;
3. freeze convergence diagnostics and all 82 phases only if the solver reports convergence;
4. independently reconstruct the QSP response using repository-owned 2x2 matrix products, not `qsppack.get_entry`;
5. compare reconstruction to the frozen polynomial on a declared grid and preserve maximum residual;
6. only then map the phase convention to the Batch-036 QSVT interface.

If synthesis fails, preserve the failure and return to polynomial construction/feasibility instead of weakening the gate.

## Non-claims

No real-QPU execution, quantum advantage, synthesized phase sequence, independently verified QSP response, full-channel repaired D.23, measured runtime/energy/memory/cost, GPU/NPU/RAM/DRAM/HBM replacement, >=100x, >=100,000,000x, or new physical law is claimed.
