# Batch 050 — QOS-AUDIT-007 Approximate-Input Robustness Contract

**Status:** executable theorem/interface audit  
**Parent:** Issue #1 / Batch 034 positive-margin D.23 repair  
**Date:** 2026-09-14

## Question

Batch 034 repaired the source-v1 D.23 endpoint only for an exact projected block. The next required gate is whether an explicitly approximate projected block can pass through the high-gain QSVT route under a reproducible error contract without silently promoting projected-block error into a full-channel statement.

## Published robustness inputs

Gilyen et al. give a general degree-`n` QSVT robustness bound of the form

`||P^SV(X)-P^SV(X_tilde)|| <= 4 n sqrt(eta)`

for `eta = ||X-X_tilde||` under the theorem premises. This is useful but can demand extremely small `eta`.

Chakraborty, Morolia and Peduri, *Quantum* 7, 988 (2023), Theorem 8, derive a stronger sufficient robust-QSVT contract in the half-norm regime: if the ideal normalized matrix obeys `||X|| <= 1/2`, input block-encoding error `eta <= delta_out/(2n)` is sufficient for output error at most `delta_out`.

For the sparse normalization used in the D.23 route,

`X = A/s`, with `||A|| <= 1` and `s >= 2`,

so `||X|| <= 1/s <= 1/2`. This closes a **conditional projected-block robustness interface** once the actual QSVT polynomial degree `n` is supplied.

## Frozen canonical ledger

Use `s=4`, `||A||<=1`, total additive target `epsilon=0.01`, split as:

- normalization bias: `0.0025`;
- ideal-input amplification approximation: `0.0025`;
- approximate-input robustness: `0.005`.

The exact-input contribution is `0.0025 + 0.9975*0.0025 = 0.00499375`, leaving the `0.005` robustness budget and total upper ledger `0.00999375 <= 0.01`.

Degree-conditioned sufficient input errors from Theorem 8 are:

| degree `n` | `eta_max = 0.005/(2n)` | general Lemma-22 `eta_max` |
|---:|---:|---:|
| 64 | `3.90625e-5` | `3.814697265625e-10` |
| 256 | `9.765625e-6` | `2.384185791015625e-11` |
| 1024 | `2.44140625e-6` | `1.4901161193847657e-12` |
| 4096 | `6.103515625e-7` | `9.313225746154786e-14` |

These rows are **conditioning diagnostics**. They do not say that the D.23 polynomial has any one of these degrees.

## Evidence level

`PUBLISHED_THEOREM_DERIVED_EXECUTABLE_SUFFICIENT_CONTRACT`

What is now closed:

- a sufficient operator-norm accuracy requirement for the approximate normalized projected block, conditional on explicit polynomial degree;
- separation of the general square-root robustness route from the stronger half-norm linear route;
- an executable error-budget ledger that preserves the Batch-034 positive-margin bias term.

What remains open:

- exact QSVT polynomial/phase synthesis and certified degree for the repaired target;
- projected-block error versus full-unitary error;
- full-unitary error versus full-channel/diamond distance;
- earlier D.16/D.19/D.20/D.21 dependencies;
- query-to-gate/time/fault-tolerance compilation;
- Lane-C capacity, bandwidth, latency, energy, hardware and lifecycle-cost contracts.

## Falsifier / interface rule

For any claimed implementation degree `n`, if the normalized projected-block error exceeds the selected published sufficient threshold, this Batch-050 certificate cannot be used to close approximate-input robustness. A different robustness proof or a tighter implementation must be supplied.

## Artifacts

- `software/uqpu-prototype/uqpu/qos_d23_approx_input_robustness.py`
- `software/uqpu-prototype/tests/test_qos_d23_approx_input_robustness.py`
- `benchmarks/results/batch050-qos-d23-approx-input-robustness.json`
- `benchmarks/external/qos-d23-robustness-provenance-2026-09-14.json`

## Next gate

`QOS-AUDIT-008`: synthesize or otherwise certify an explicit bounded polynomial for one repaired D.23 instance, pin its actual degree/phase convention, then test the projected-block robustness ledger numerically on small matrices. Only after that should the result be propagated into gate/time/fault-tolerance and Lane-C memory/economics ledgers.

## Non-claims

No exact QSVT degree or depth has been measured. No real-QPU result, quantum advantage, QOS-wide validity, GPU/NPU/RAM/DRAM/HBM replacement, `>=100x`, `>=100,000,000x`, Data-Center-to-One-Phone result, economic advantage, or new physical law is claimed.
