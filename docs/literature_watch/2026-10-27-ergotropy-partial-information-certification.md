# Literature watch — Certifying ergotropy under partial information

**Reviewed:** 2026-10-27  
**Primary source:** Egle Pagliaro, Leonardo Zambrano, Mir Alimuddin, Alioscia Hamma, Antonio Acín and Donato Farina, “Certifying Ergotropy under Partial Information.”  
**Peer-reviewed version:** *Physical Review Letters* 137, 130401 (published online 2026-09-21; issue dated 2026-09-25), DOI: https://doi.org/10.1103/pl26-g6vy  
**Author preprint:** https://arxiv.org/abs/2603.18828  
**Evidence class:** PEER_REVIEWED_THEORY + AUTHOR-REPORTED EXPERIMENT ON IBM QUANTUM; not independently reproduced by UQPU  
**Primary owner:** Lane H — literature provenance/publication; technical owner: Lane A; evaluation owner: Lane F  
**Cross-cutting:** FND-001, FND-003, INV-034/035

## Material result and exact scope

The authors formulate ergotropy as the maximum energy difference extractable from a finite-dimensional quantum state by a unitary operation, assuming the Hamiltonian is known. Because the state is only partially characterized, they construct a lower certificate compatible with measured observable expectations using a two-stage semidefinite-programming procedure. For finite shot counts, confidence regions derived from Hoeffding's inequality and a union bound provide a stated confidence level for the certificate.

The authors report proof-of-principle examples with synthetic data and experimental measurements from an IBM quantum processor. In the experimental example, they use up to 60 Pauli-string observables for a four-qubit GHZ target and report 2^14 shots per observable. These are the authors' reported results, not UQPU measurements or an independently reproduced result.

## Why it matters to UQPU

This is a useful bridge between partial quantum-state information, finite-shot uncertainty, and a *certified lower bound on extractable work*. It can sharpen the distinction between an ideal resource bound and a quantity supported by noisy measurements.

It does **not** measure the total energy required to run a quantum-computing workload. Ergotropy is not net energy production, wall-plug efficiency, a Landauer bound, a generic gate-time limit, or cost per accepted task. The work required for state preparation, measurement, control, reset, cooling, readout, host computation and data movement remains outside the ergotropy certificate unless explicitly added to a separate system ledger.

## Limitations and evidence boundary

- The paper assumes the system Hamiltonian is fully characterized; Hamiltonian uncertainty is not solved by the cited result.
- A confidence-certified lower bound can be trivial (zero) when the partial information is insufficient.
- The SDP certificate and measurement-confidence assumptions need independent reconstruction and tests before UQPU uses them.
- Observable eigenvalue bounds, shot independence, confidence allocation, solver tolerances and numerical feasibility must be explicit.
- An energy difference inside a system boundary cannot be silently interpreted as total device energy, net work after control overhead, or a commercial advantage.
- No new physical law, quantum advantage, memory replacement, bio-oil/material result, fusion-electricity result, or finance-rate effect follows from the paper.

## Proposed falsifiable reproduction

1. Pin the arXiv source/version, equations, Hamiltonian convention, observable list, code/dependency versions and data provenance.
2. Start with small systems where the density matrix and Hamiltonian are known. Compute exact ergotropy from spectral decompositions as the reference.
3. Reproduce the two-stage SDP lower bound using only a declared subset of observable expectations; include deliberately uninformative measurement sets where the correct certificate may be zero.
4. Generate finite-shot samples with a frozen seed set. Check empirical coverage of the claimed 1-delta confidence level, bound validity against exact ergotropy, and sensitivity to shot count, observable count and confidence parameter.
5. Include solver residuals, infeasible cases, failed runs, runtime, peak memory, observable-grouping/measurement cost and total shots. Verify that the bound never exceeds the exact ergotropy within declared numerical tolerance.
6. Only after independent numerical reproduction, assess whether any real workload can map its measured observables to a meaningful resource certificate. Keep a separate wall-plug energy and accepted-output cost ledger.

**Falsifiers:** any reproducible case in the declared domain where the reported lower certificate exceeds the exact ergotropy beyond numerical tolerance; confidence coverage below the declared rate under the stated sampling assumptions; or a claimed UQPU benefit that disappears once measurement/control/state-preparation costs are included.

## Next gate

Implement and test only the bounded-observable Hoeffding confidence-radius helper first. It is a statistical component of the paper's finite-shot confidence region, not an ergotropy solver. Keep the full SDP reproduction as a separate open gap until its mathematical constraints, solver dependencies and exact reference tests are pinned.
