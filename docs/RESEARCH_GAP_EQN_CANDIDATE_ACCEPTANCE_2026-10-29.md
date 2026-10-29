# Research gap RG-EQN-CANDIDATE-ACCEPTANCE-001 — accuracy and stability must pass jointly

**Opened:** 2026-10-29  
**Owner:** Lane A; evidence/resource accounting Lane F; source/provenance Lane H  
**Status:** SOFTWARE GATE ADDED / GROUPED DISCOVERY BENCHMARK NOT RUN / MODEL_ONLY  
**Related:** RG-EQN-STRUCTURAL-STABILITY-001; FND-006; EQN-002–EQN-004; INV-034/035

## Objective

Prevent symbolic or AI-generated equation candidates from passing because of a single attractive metric. In particular, zero or low perturbation amplification can be produced by a constant or otherwise uninformative candidate. Held-out accuracy, stability, constraints and numerical reliability must be checked together.

## Current implementation

`software/uqpu-prototype/uqpu/equation_candidate_gate.py` computes normalized RMS error using positive, predeclared output scales and requires both the error and separately measured perturbation amplification to pass frozen thresholds. Any constraint violation or numerical failure is a hard stop. Six unit tests cover a passing exact synthetic candidate, a constant zero-sensitivity counterexample, a high-sensitivity candidate, hard-stop counts, non-finite output and invalid thresholds.

## Evidence boundary

This is a software diagnostic over synthetic values. It does not reproduce EIC, run a symbolic-regression method comparison, establish semantic equivalence, prove a physical law, or demonstrate QPU/material/fuel/fusion/finance advantage. The EIC arm remains blocked pending reuse rights and source/data/environment pinning.

## Unlock criteria

1. Freeze known-law equation families, output scales and family-specific acceptance thresholds before candidate generation.
2. Split by whole equation family/system and held-out domain; no random-point-only split.
3. Compare fit-plus-complexity, the UQPU perturbation proxy and any legally/reproducibly available EIC implementation under equal budgets.
4. Include exact-recovery, constant/null, ill-conditioned-equivalent and constraint-violating controls.
5. Retain every failed candidate and report held-out error, stability, constraint violations, numerical failures, false discoveries, search cost and cost per accepted candidate where a defensible cost basis exists.
6. Use at least 30 preregistered seeds and independently repeat on a separate equation family.

## Next gate

Pass exact-head Actions, then execute the frozen synthetic grouped benchmark. No physical-law claim is permitted from this gate alone.
