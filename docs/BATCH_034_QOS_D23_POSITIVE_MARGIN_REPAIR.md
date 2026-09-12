# Batch 034 — QOS D.23 Positive-Margin Repair Audit

**Date:** 2026-09-12  
**Programs:** Issue #1 / QOS-AUDIT-006 / Lane C  
**Evidence:** THEORY_EXECUTABLE_SUFFICIENT_REPAIR_CONTRACT  
**REAL_QPU:** No  
**Quantum advantage demonstrated by UQPU:** No  
**GPU/NPU/DRAM/HBM replacement demonstrated:** No

## Executive result

Batch 033 showed that the displayed source-v1 D.23 amplification `A/s -> A` reaches the saturation endpoint `||A||=1`, where the standard positive-margin uniform singular-value-amplification theorem is not directly applicable.

Batch 034 constructs one explicit theorem-compatible repair for the **exact projected-input contract**: deliberately under-amplify to `(1-b)A`, using the lost scale `b` as an additive normalization-bias budget.

For `||A||=1`, starting from `A/s`, choose

- target scale `c = 1-b`,
- amplification `gamma = s(1-b)`,
- maximal positive theorem margin `delta = b`.

Then

`1/s = (1-delta)/gamma`,

so the endpoint singular value lies exactly at the allowed boundary of Gilyen et al. Theorem 30 while `delta>0`.

**Classification:** `D23_ENDPOINT_POSITIVE_MARGIN_REPAIR_EXACT_INPUT_ONLY`.

This closes only the endpoint applicability problem for an exact input block under this under-amplified target. It does not close approximate-input robustness, full-channel distance, or the earlier D.16/D.19/D.20/D.21 dependencies.

## Error budget

If total additive target error is `epsilon`, Batch 034 uses the reproducible half split

`b = epsilon/2`, `epsilon_amp = epsilon/2`.

The target bias is at most `b||A||`. Theorem 30 gives multiplicative amplification error on the retained target singular values, so for `||A||=1` the exact-input additive ledger is bounded by

`b + (1-b) epsilon_amp <= epsilon`.

This is a sufficient ledger, not an optimal allocation.

## Resource consequence

Theorem 30 states degree/query scaling

`O((gamma/delta) log(gamma/epsilon_amp))`.

For the repair above,

`gamma/delta = s(1-b)/b`.

With `b=Theta(epsilon)`, this sufficient route therefore has scaling

`O((s/epsilon) log(s/epsilon))`,

rather than the source-displayed `O(s log(1/epsilon))` endpoint expression.

This is **not** a lower bound on every possible D.23 repair. It is the resource cost of this explicit theorem-compatible positive-margin route, up to the theorem's hidden constant.

For `s=4` and the 50/50 error split, the dimensionless theorem scaling proxy `(gamma/delta) log(gamma/epsilon_amp)` is:

- `epsilon=0.05`: `787.7775371309278`;
- `epsilon=0.01`: `5316.960951932129`;
- `epsilon=0.001`: `71857.62677817984`;
- `epsilon=0.0001`: `903133.3940648285`.

The corresponding ratios to the diagnostic source proxy `s log(s/epsilon)` are about `44.94x`, `221.86x`, `2165.94x`, and `21307.08x`. These are scaling proxies without hidden constants and must not be interpreted as measured circuit depths or runtimes.

## Imported theorem provenance

Gilyen et al., *Quantum singular value transformation and beyond*, arXiv:1806.01838, Theorem 30 states uniform singular-value amplification for `gamma>1`, positive `delta`, and singular values at most `(1-delta)/gamma`, with degree

`O((gamma/delta) log(gamma/epsilon))`.

The public arXiv source was rechecked on 2026-09-12 and is pinned in `benchmarks/external/qsvt-theorem30-positive-margin-provenance-2026-09-12.json`.

## What is closed

For an exact projected encoding of `A/s` at `||A||=1`, an explicit positive-margin target `(1-b)A` exists and fits the standard imported theorem contract for any `b>0`.

## What remains open

1. **Approximate input block robustness.** D.23 first constructs an approximate projected block. Batch 034 does not yet propagate that input error through the high-gain QSVT sequence.
2. **Full-channel/unitary distance.** Projected-block approximation must not be silently promoted to a full-unitary or diamond-norm statement.
3. **Earlier dependencies.** D.16/D.19/D.20/D.21 audit findings remain independent gates.
4. **Resource propagation.** Any repaired D.23 theorem must propagate the additional `1/epsilon`-type sufficient-route overhead into sample, query, gate, logical-qubit, time, and Lane-C memory/economic ledgers before downstream advantage claims are considered.

## Lane C consequence

The repair demonstrates a mathematically available endpoint-safe route, but it is not free. Therefore source machine-size formulas that assume the original endpoint `O(s log(1/epsilon))` step cannot be directly reused for DRAM/HBM capacity, bandwidth, energy, latency, or cost claims without recomputing the repaired full-stack ledger.

`machine-size reduction != DRAM/HBM replacement != cost reduction` remains enforced.

## Reproducibility artifacts

- `software/uqpu-prototype/uqpu/qos_d23_positive_margin_repair.py`
- `software/uqpu-prototype/tests/test_qos_d23_positive_margin_repair.py`
- `software/uqpu-prototype/examples/run_qos_d23_positive_margin_repair.py`
- `benchmarks/results/batch034-qos-d23-positive-margin-repair.json`
- `benchmarks/external/qsvt-theorem30-positive-margin-provenance-2026-09-12.json`

## Next gate — QOS-AUDIT-007

Propagate an explicit approximate projected-block error through the repaired positive-margin route. Separate at least:

- input projected-block error,
- amplification theorem error,
- normalization bias,
- robustness amplification with degree/query growth,
- projected-block norm versus full-unitary/full-channel distance.

Only after that ledger closes should repaired D.23 sample/query/time consequences be propagated into Lane C.

## Non-claims

Batch 034 does not demonstrate a real-QPU result, quantum advantage, universal QOS invalidity, a D.23 theorem proof or refutation, GPU/NPU/RAM/DRAM/HBM replacement, >=100x advantage, >=100,000,000x advantage, measured QSVT circuit depth, or a new physical law.
