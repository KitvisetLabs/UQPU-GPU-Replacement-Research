# Batch 037 — QOS D.23 Explicit Polynomial Candidate

**Date:** 2026-09-13  
**Program:** Issue #1 / QOS-AUDIT-009  
**Evidence level:** `NUMERICALLY_EXPLICIT_POLYNOMIAL_CANDIDATE_WITH_INDEPENDENT_DENSE_AND_CRITICAL_POINT_CHECKS`  
**REAL_QPU:** No  
**Quantum advantage demonstrated:** No  
**GPU/NPU/RAM/DRAM/HBM replacement demonstrated:** No

## Research Attribution

- **Research Owner / Principal Investigator / Research Direction:** Kanutsanan Pongpanna
- **Facebook:** https://www.facebook.com/LoveMoneyTH
- **YouTube:** https://www.youtube.com/@LoveMoneyTHOfficial
- **AI Research Agent:** OpenAI GPT-5.6 Sol
- **AI-assisted contribution:** QOS-AUDIT-009 candidate construction, numerical optimization, independent verification design, executable implementation, tests, provenance, documentation and PR preparation.

Attribution describes roles in this batch only.

## Executive result

Batch 036 closed the constructive Theorem-30 interface only conditionally on an actual odd polynomial degree. The primary theorem chain still exposed degree through asymptotic big-O constants, so it did not justify selecting a concrete circuit degree.

Batch 037 advances that gate by constructing and freezing one **numerically explicit odd polynomial candidate** for the canonical repaired case

- `s = 4`,
- projected error target `epsilon = 0.01`,
- normalization bias `b = epsilon/3`,
- `gamma = s(1-b) = 3.986666666666667`,
- target domain `[-1/s,1/s] = [-0.25,0.25]`,
- amplification approximation budget `epsilon/3 = 0.0033333333333333335`.

The candidate is represented directly in an odd Chebyshev basis,

`P_81(x) = sum_{k odd, 1<=k<=81} c_k T_k(x)`,

with all 41 nonzero coefficients frozen in the executable artifact.

Independent numerical checks give

- degree: `81`,
- dense-grid global maximum: `0.9990000451669641`,
- critical-point global maximum: `0.9990000715936669`,
- dense target-domain max error versus `gamma*x`: `0.0024171473863981996`,
- critical-point target-domain max error: `0.002417147392736352`.

Thus the frozen candidate clears the `epsilon/3` approximation budget and the unit-amplitude bound **numerically with visible slack**.

**Classification:** `D23_EXPLICIT_NUMERICAL_POLYNOMIAL_CANDIDATE_DEGREE_81_PHASES_OPEN`.

This is progress beyond a big-O degree proxy: degree 81 is now attached to an explicit coefficient vector that can be independently evaluated. It is not yet promoted to a theorem-certified QSVT circuit degree because the remaining phase-synthesis/admissibility verification step has not been completed.

## 1. Construction method

The candidate was generated in the odd Chebyshev basis using a linear program minimizing the maximum target-domain error subject to sampled global constraints. A cutting-plane loop then located numerically detected critical-point violations of the current polynomial and added those points back to the global constraint set.

This matters because a single fixed uniform grid was insufficient: an early degree-81 solution appeared to satisfy a `0.999` sampled bound but independent derivative-root analysis found narrow peaks above one. The cutting-plane refinement removed those detected overshoots. The final frozen candidate was then checked independently on a much denser grid and by roots of the Chebyshev derivative.

That failed-first-candidate behavior is part of the evidence: it demonstrates why a grid-only certificate must not be silently treated as a formal global proof.

## 2. Independent numerical verification

Two distinct numerical verification routes were used before freezing the result.

### Dense-grid route

- global grid: `200001` points over `[-1,1]`;
- target grid: `100001` points over `[-0.25,0.25]`;
- observed global max `|P_81| = 0.9990000451669641`;
- observed target max `|P_81(x)-gamma*x| = 0.0024171473863981996`.

### Critical-point route

Using NumPy's Chebyshev derivative/root machinery independently of the repository's standard-library evaluator:

- evaluate `P_81` at all numerically real derivative roots in `[-1,1]` plus endpoints;
- evaluate `P_81-gamma*x` at all numerically real derivative roots in `[-0.25,0.25]` plus endpoints.

Observed extrema were

- global max `|P_81| = 0.9990000715936669`;
- target max error `0.002417147392736352`.

The two routes agree to the expected numerical level and both retain substantial room below `1` and below the `0.003333...` target error budget.

## 3. What this closes

Batch 037 closes a narrower statement than the full QOS gate:

- there exists a **concrete frozen degree-81 odd coefficient vector** found by the stated numerical procedure;
- the repository can reproduce its values without SciPy/NumPy using a standard-library Clenshaw evaluator;
- dense-grid verification reproduces the global and target-domain numerical behavior;
- a separate derivative-root calculation independently checks the extrema numerically;
- degree is no longer merely a caller-supplied placeholder for this one frozen candidate.

## 4. What remains open

The following remain open and are deliberately represented as `false` in the executable certificate:

1. **Formal global boundedness proof.** Numerical critical-point verification is strong computational evidence, but this batch does not claim interval-arithmetic or symbolic proof of `|P_81(x)|<=1` for every real `x`.
2. **QSP/QSVT phase synthesis.** No phase list is yet frozen for this candidate.
3. **Independent phase verification.** Consequently there is not yet an independently reconstructed QSP response matching the coefficient vector.
4. **Full repaired D.23 channel statement.** This remains separate from the projected polynomial block.
5. Earlier D.16/D.19/D.20/D.21 gates and Lane-C physical/economic gates remain independent.

## 5. Phase-synthesis literature check

Public literature and tooling were rechecked on 2026-09-13.

- Chao, Ding, Gilyen, Huang and Szegedy, `arXiv:2003.02831`, provide a constructive classical method for finding QSP angles and report machine-precision recovery for long angle sequences.
- Dong, Meng, Whaley and Lin, `arXiv:2002.11649` / *Phys. Rev. A* 103, 042419, give an optimization-based phase-factor method and report high-degree numerical demonstrations in double precision.
- The public `ichuang/pyqsp` package exposes phase-angle generation implementations based on these methods.

These sources justify making phase synthesis the next high-information gate; they do **not** by themselves certify the specific Batch-037 polynomial or turn this numerical candidate into a hardware result.

Provenance is pinned in `benchmarks/external/qsp-phase-synthesis-provenance-2026-09-13.json`.

## 6. Reproducibility artifacts

- `software/uqpu-prototype/uqpu/qos_d23_explicit_polynomial_candidate.py`
- `software/uqpu-prototype/tests/test_qos_d23_explicit_polynomial_candidate.py`
- `software/uqpu-prototype/examples/run_qos_d23_explicit_polynomial_candidate.py`
- `benchmarks/results/batch037-qos-d23-explicit-polynomial-candidate.json`
- `benchmarks/external/qsp-phase-synthesis-provenance-2026-09-13.json`

## Next gate — QOS-AUDIT-010

Highest-information next step:

1. run at least one independent QSP phase-synthesis implementation against the frozen degree-81 coefficient vector;
2. freeze the resulting phase sequence and implementation/version provenance;
3. reconstruct the QSP polynomial from those phases and compare it against the frozen coefficient vector and `gamma*x` target;
4. independently verify parity, amplitude and phase-convention mapping to the Corollary-18/QSVT interface used in Batch 036;
5. if phase synthesis fails because the candidate violates a hidden QSP feasibility condition, preserve that failure as the result and return to constrained polynomial construction rather than modifying claims.

A formal interval or symbolic bound on the frozen polynomial would further strengthen the candidate and should be added before using degree 81 as a theorem-grade resource number.

## Non-claims

Batch 037 does **not** demonstrate or claim:

- real-QPU execution;
- quantum advantage;
- proof or refutation of QOS D.23 as a whole;
- a theorem-certified degree-81 QSVT implementation;
- an actual QSP/QSVT phase sequence;
- measured circuit depth, runtime, energy or physical resource cost;
- a full-unitary/full-channel repaired D.23 guarantee;
- GPU/NPU/RAM/DRAM/HBM replacement;
- >=100x advantage;
- >=100,000,000x advantage;
- a new physical law.
