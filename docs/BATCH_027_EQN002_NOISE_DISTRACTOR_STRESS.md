# Batch 027 — EQN-002 Noise, Distractor and False-Discovery Stress Test

**Date:** 2026-09-10  
**Program:** INV-035 / EQN-002 / RG-031  
**Evidence:** MODEL_ONLY_SYNTHETIC + EXECUTABLE SOFTWARE  
**REAL_QPU:** No  
**New physical law:** No  
**Quantum advantage:** No

## Research question

Does the Batch-026 known-law recovery baseline remain trustworthy once dimensional analysis no longer reveals the answer and the search space contains unit-consistent over-parameterized distractor equations under noise?

## Experimental design

The new module `software/uqpu-prototype/uqpu/equation_recovery_stress.py` hides the synthetic law

`y = 1.5 * z^2`

where `z` is explicitly dimensionless. Because `z` is dimensionless, every polynomial distractor in the bounded grammar is dimensionally admissible when its fitted coefficient carries the output unit. This removes the Batch-026 shortcut in which dimensional analysis uniquely selected the correct exponent.

The candidate grammar includes single powers and mixed polynomial structures such as

`z`, `z^2`, `z^3`, `z^4`, `z + z^2`, `z^2 + z^3`, `z + z^2 + z^4`, and related bounded distractors.

Coefficients are fitted only on a training subset. Candidate selection sees a disjoint holdout subset. A further higher-range subset is reserved for extrapolation diagnostics. Multiplicative Gaussian noise is added with deterministic repeated seeds.

Two selectors are compared under the same candidate/evaluation budget:

1. `error_only` — minimum held-out RMSE;
2. `parsimony_regularized` — held-out error plus an explicit complexity penalty.

The regularized score is BIC-inspired but is deliberately not called canonical BIC because the complexity coefficient is configurable and is set to `4.0` in this calibration.

## Reproducible 256-seed result

Canonical artifact: `benchmarks/results/batch027-equation-recovery-stress.json`.

| Multiplicative noise sigma | Error-only recovery | Error-only FDR | Parsimony recovery | Parsimony FDR |
|---:|---:|---:|---:|---:|
| 0.01 | 48.05% | 51.95% | **87.89%** | **12.11%** |
| 0.05 | 44.53% | 55.47% | **87.11%** | **12.89%** |
| 0.10 | 41.80% | 58.20% | **83.20%** | **16.80%** |
| 0.20 | 40.23% | 59.77% | **69.53%** | **30.47%** |

The regularized selector accepts slightly worse median in-domain holdout fit in some regimes in exchange for a much higher probability of recovering the true compact structure. It also reduces median extrapolation RMSE relative to error-only selection in all four recorded noise regimes.

## Scientific interpretation

The important result is negative for naive equation discovery:

`best held-out curve fit != reliable physical-structure recovery`

Even in this small synthetic grammar, error-only selection chooses a false structure in more than half of the 256 trials at every tested noise level. A complexity prior materially reduces false discovery, but does not eliminate it: at 20% multiplicative noise the false-discovery rate remains about 30.5%.

Therefore INV-035 must not promote an AI-generated equation merely because it has the smallest validation error. Structure complexity, extrapolation, physics constraints, counterexamples and independent evidence remain mandatory.

## External benchmark delta

### LLM-SRBench

Shojaee et al., **LLM-SRBench: A New Benchmark for Scientific Equation Discovery with Large Language Models**, ICML 2025 Oral, provides 239 problems across four scientific domains and explicitly targets memorization-resistant equation discovery. The reported best-performing system achieves only 31.5% symbolic accuracy.

Sources:
- https://proceedings.mlr.press/v267/shojaee25a.html
- https://github.com/deep-symbolic-mathematics/llm-srbench

**Project consequence:** the internal kinetic-energy/polynomial fixtures are calibration only. RG-031 should next include an externally maintained benchmark subset with pinned problem IDs and versions so that project-specific tuning cannot define success.

### SRBench

SRBench is a living open benchmark for symbolic regression with multiple modern methods and a standardized comparison interface.

Source: https://github.com/cavalab/srbench

**Project consequence:** future claims about AI-assisted equation discovery should include strong conventional symbolic-regression baselines rather than only internal enumeration.

## Quantum Oracle Sketching research watch

A separate high-value UQPU-relevant result, Zhao et al. **Exponential quantum advantage in processing massive classical data**, arXiv:2604.07639, proposes Quantum Oracle Sketching (QOS) and reports four-to-six orders of magnitude machine-size reduction in real-data examples with fewer than 60 logical qubits.

Sources:
- https://arxiv.org/abs/2604.07639
- https://github.com/haimengzhao/quantum-oracle-sketching

This is highly relevant to UQPU Lane A/C because it targets classical-data access and memory footprint rather than gate-for-gate GPU emulation. However, machine-size advantage is not automatically end-to-end cost, throughput, energy, physical-qubit or NPU/GPU replacement advantage.

A public independent version-specific audit by C. Vellón Gascón claims an explicit finite counterexample to the sufficient threshold printed in Theorem D.16 / Eq. D.99 of `arXiv:2604.07639v1`, while explicitly stating that it does not claim QOS is impossible or invalidate every result.

Source:
- https://github.com/gatephys/quantum-oracle-sketching

**Project consequence:** QOS is promoted to `HIGH_VALUE_ADVERSARIAL_REVIEW_REQUIRED`, not to verified UQPU evidence. The source theorem, implementation and independent criticism must be checked side-by-side before a UQPU reproduction or architecture decision relies on the strongest claim.

## RG-031 progress

Batch 027 closes several previously open sub-gaps:

- noisy hidden-law fixtures: **DONE for bounded scalar polynomial calibration**;
- unit-consistent distractor equations: **DONE for bounded polynomial grammar**;
- repeated-seed statistics: **DONE (256 seeds)**;
- false-discovery rate: **DONE for current fixture**;
- extrapolation stress: **DONE for current fixture**;
- complexity/parsimony scoring: **DONE as a calibration selector**.

Still open:

- at least one external LLM-SRBench/SRBench subset;
- ODE/PDE equation-recovery fixture;
- conventional production symbolic-regression baseline under a frozen budget;
- AI-assisted generator under the same frozen budget;
- broader grammars and nuisance/dummy variables;
- repeated benchmark families rather than one synthetic law;
- independent replication outside the project implementation.

## Next gate — EQN-002C

Implement a version-pinned external benchmark adapter and run at least two search methods under a frozen evaluation budget. Record exact/symbolic recovery, normalized structural distance where available, held-out error, extrapolation error, physical-constraint violations, wall time and false-discovery rate. Preserve failed equations as first-class artifacts.

In parallel, open an adversarial QOS audit track that reproduces the simplest oracle-sketching construction and checks the v1 theorem/interface assumptions before using QOS as a UQPU memory/NPU-compression premise.

No new law of nature, real-QPU advantage, >=100x advantage, >=100,000,000x advantage, subsystem replacement or Data-Center-to-One-Phone feasibility is demonstrated by Batch 027.
