# QCOMP-CONFIG-001 — Joint target and compiler configuration benchmark contract

**Primary owner:** Lane A — quantum programming / workloads / compiler / runtime  
**Cross-lane owners:** B (target metadata), C (state/I/O), F (acceptance/economics), H (literature provenance)  
**Status:** `PROPOSED / NOT EXECUTED / MODEL_ONLY`  
**Date:** 2026-10-24  
**Motivation:** Zhong et al., arXiv:2610.29170 (2026-10-21), literature-only

## Question

For the same accepted useful-output contract, does joint selection of a quantum hardware target and compiler configuration improve blind-set accepted quality or total cost per accepted task compared with a target-first policy under the same configuration-evaluation budget?

This contract is inspired by a third-party preprint and does not reproduce its benchmark or claim that its method works for UQPU.

## Comparison arms

1. **Default:** documented SDK/compiler defaults for each eligible target.
2. **Target-first:** choose target by a preregistered target policy, then tune compiler settings on that target.
3. **Joint top-down:** select target and compiler settings together from the same allowed configuration set.
4. **Oracle upper bound:** exhaustive search over the frozen small configuration set; report as an offline upper bound, never as an executable production policy.
5. **Optional direct LLM:** separate inference/runtime budget and provenance; do not merge its cost into other arms.

## Freeze before evaluation

- Workload ID, source-circuit hash, semantics and accepted output-quality threshold.
- Train/validation/blind-test circuit-family and target-family splits.
- Provider, target, SDK/compiler versions, configuration schema and calibration snapshot identity where relevant.
- Configuration candidate list and its SHA-256 digest.
- Selection/search evaluation budget, timeout, seed schedule and stopping rule.
- Primary metric and direction; quality failure is not rescued by lower compilation time.
- Pricing context for each exact provider/target; no cross-provider quality/price mixing.
- Zero paid QPU jobs in the initial phase. Any later paid execution requires credentials, a bounded budget and explicit consent.

## Required outputs

- Selection decision latency and compiler wall time.
- Predicted versus observed quality; held-out regret against the offline oracle.
- One-/two-qubit gate counts, circuit depth, routing/SWAP overhead and failure/timeout rate.
- Accepted useful tasks, throughput, latency, shots and retries where applicable.
- Host compute, memory, state/input loading, transfer/I/O and reconstruction.
- Total cost per accepted task and energy per accepted task when measured; otherwise explicit unknowns.
- Results by held-out circuit family and target/device family, including all failed selections.

## Pass/fail

A candidate policy advances only if it improves the preregistered blind-set accepted-output or total-cost objective over the target-first baseline under equal selection budgets, with no hidden degradation in quality or unreported overhead. Oracle proximity, fidelity alone, compile-time savings, or an LLM score is insufficient. If the policy fails on new targets, calibration drift or circuit families, preserve the negative result and narrow the applicability claim.

## Downstream gates

- **Simulator/dry-run:** first; no provider credentials required.
- **Independent SDK check:** same circuit and output contract, independently reproduced.
- **Target-aware simulation:** target-specific assumptions and provenance recorded.
- **Real QPU:** only after the prior gates and explicit authorization; bind quality and price to the same provider/target.
- **System economics:** compare total cost per accepted useful task against competitive CPU/GPU/NPU baselines and include all host/I/O/reconstruction/energy terms.

## Evidence and non-claims

Current status is `MODEL_ONLY / NOT EXECUTED`. No UQPU advantage, real-QPU result, GPU/NPU/CPU replacement, RAM/VRAM/storage replacement, physical-law discovery, material substitution, commercial bio-oil, low-cost fusion electricity, reduced financing rate/WACC or Data-Center-to-Phone feasibility is established.
