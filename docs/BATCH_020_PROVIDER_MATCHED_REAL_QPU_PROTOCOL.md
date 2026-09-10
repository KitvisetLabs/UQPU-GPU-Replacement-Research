# Batch 020 — Provider-Matched Real-QPU Falsification Protocol

**Date:** 2026-09-10  
**Status:** PROTOCOL_FROZEN / EXECUTION_REQUIRES_AUTHORIZATION  
**Primary lanes:** A + B + F, integrated with C/D/G/H  
**Paid QPU submitted:** No

## Purpose

Batch 019 found that a CVaR-selected p=1 QAOA circuit for ER6 retained a higher exact-optimum probability than the mean-energy-selected circuit under the saved IBM FakeKingston target-noise model. Batch 020 freezes the next experiment before seeing live-hardware results so that a favorable outcome cannot be manufactured by changing the contract after execution.

Machine-readable protocol: `benchmarks/experiments/batch020-er6-mean-vs-cvar-real-qpu-protocol.json`.

## Frozen workload and candidates

Workload contract: `8efaa94bb3306d25`, ER6 MaxCut/QUBO, six variables, exact reference objective `-7`.

- **Mean-energy candidate:** gamma `0.5235987755982988`, beta `1.3089969389957472`.
- **CVaR alpha=0.5 candidate:** gamma `0.6544984694978736`, beta `2.748893571891069`.

The parameter pairs are now frozen from Batch 019. Live-QPU comparison must not retune one candidate while leaving the other fixed and then call that a fair paired test.

## Fairness gate

Both candidates must use the same provider, backend, calibration window, shot budget, result decoder, acceptance rule, transpilation policy, mitigation policy and execution class as far as the provider permits. The preferred initial budget is **8,192 shots per candidate**, matching the saved-target comparison.

If calibration drifts materially between the two jobs, the run must be marked confounded or repeated as a paired experiment rather than silently combining the results.

## Required provenance

The evidence record must preserve backend and provider identity, job IDs, timestamps, calibration provenance, physical layout, transpiled depth/two-qubit gate count, requested/completed shots, raw counts or provider result reference, optimum hits, accepted-output probability, sampling interval, QPU time if reported, wall-clock/queue time, billed cost/currency, retries/failures, mitigation, host orchestration and output-reconstruction cost where measurable.

## Falsification rule

Primary hypothesis: the frozen CVaR circuit has higher **real-QPU exact-optimum probability** than the frozen mean-energy circuit under the equal-shot provider-matched contract.

If the gain disappears, reverses, or cannot be separated from calibration/execution uncertainty, that negative/inconclusive outcome is retained. A successful execution alone is not acceptance of the hypothesis.

## Economic and North-Star boundaries

Even a positive paired hardware result would not by itself prove quantum advantage. Economic comparison requires provider-matched **cost per accepted useful result** plus a competitive classical baseline under the same useful-output contract.

This six-qubit experiment cannot establish >=100x, >=100,000,000x, 100-million-unit replacement, or Data-Center-to-One-Phone equivalence. It is one evidence step toward reducing repetitions/work per accepted solution.

## Authorization gate

No paid real-QPU job is submitted by this protocol. If execution incurs cost, provider credentials, target access and an explicit bounded spending authorization are required before submission.
