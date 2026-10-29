# RG-A-TINN-TIME-DEPENDENT-PDE-001 — held-out generalization and total-resource accounting for TINNs

**Created:** 2026-10-29  
**Owner:** Lane A  
**Cross-lane consumers:** C, D, E, F, G, H  
**Status:** OPEN / LITERATURE_ONLY / DATA_BLOCKED FOR UQPU REPRODUCTION  
**Source:** https://proceedings.mlr.press/v306/dai26a.html

## Objective

Determine whether the time-conditioned neural-network architecture reported in TINNs improves accepted predictions for a known time-dependent PDE under grouped, genuinely held-out physical regimes and a matched total resource budget.

## Current evidence

The ICML/PMLR publisher record reports up to 4× relative L2-error improvement and up to 10× faster convergence on the paper's evaluated tasks. These are external author-reported results. UQPU has not reproduced them, and they are not a physical-law, device, energy, or economic result.

## Blockers

- Pinned source revision, data and dependency/license review not yet completed.
- No UQPU-owned, frozen, known-law PDE benchmark and held-out regime manifest has been executed for this architecture.
- A relative error summary can hide worst-case failure, conservation drift, invalid states, reference-solver error or extra optimization work.
- Training/inference compute, memory, data movement, energy and cost-per-accepted-result are not yet matched or measured.

## Unlock criteria

1. Pin source code/data and record provenance and license status; otherwise remain DATA_BLOCKED.
2. Freeze a known-law PDE, trusted reference and solver-convergence tolerance.
3. Split by complete trajectories/physical regimes; publish and validate immutable manifests before fitting.
4. Compare conventional PINN, TINN, a compatible neural-operator-splitting comparator if available, and the trusted solver under a preregistered equal optimizer/resource budget.
5. Measure median/worst-case held-out error, PDE residual, conservation/bounds, failures, wall time, peak memory, bytes moved and energy where instrumented.
6. Independently reproduce the selected result before any downstream D/E/G use.
7. Keep all failures, negative outcomes and false discoveries in the record.

## Next gate

Run the contract at research_lanes/A_quantum_programming_runtime/TINN_TIME_DEPENDENT_PDE_ACCEPTANCE_CONTRACT_2026-10-29.md on a synthetic known-law PDE with an independently converged numerical reference. Do not start with an uncalibrated Pangola reactor or fusion-cooling model.

**Non-claims:** no UQPU reproduction, physical law, material substitution, accepted fuel, net fusion electricity, QPU advantage, financing-rate change or mission-level compression is established.
