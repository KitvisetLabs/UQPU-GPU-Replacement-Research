# Batch 051 — QOS D.23 Exact Bernstein Boundedness Certificate

**Date:** 2026-09-14  
**Program:** Issue #1 / QOS-AUDIT-010A  
**Evidence level:** `EXACT_RATIONAL_BERNSTEIN_CERTIFICATE_FOR_FROZEN_RUNTIME_FLOAT_POLYNOMIAL`  
**REAL_QPU:** No  
**Quantum advantage demonstrated:** No  
**GPU/NPU/RAM/DRAM/HBM replacement demonstrated:** No

## Research Attribution

- **Research Owner / Principal Investigator / Research Direction:** Kanutsanan Pongpanna
- **AI Research Agent:** OpenAI GPT-5.6 Sol
- **AI-assisted contribution:** gate prioritization, exact-certificate design, executable implementation/tests, evidence scoping, CI/PR preparation.

Attribution describes roles in this batch only.

## Executive result

Batch 037 froze a degree-81 odd Chebyshev polynomial candidate and verified it numerically on dense grids and numerical critical points, while explicitly leaving formal all-real boundedness and QSP/QSVT phase synthesis open.

Batch 051 closes **one narrower upstream uncertainty** without pretending to close phase synthesis:

> For the exact binary rational polynomial instantiated by the frozen Python `float` coefficients in `qos_d23_explicit_polynomial_candidate.py`, exact rational Bernstein arithmetic certifies `|P_81(x)| <= 1` for every real `x in [-1,1]` and certifies `|P_81(x)-gamma*x| <= epsilon/3` for every real `x in [-0.25,0.25]`.

The coefficient/runtime contract is bound by SHA-256 fingerprint:

`4364297169fe219da396c1d663680f474508a03afed93e321dc8e9d8f0bad13a`

Classification:

`D23_FROZEN_FLOAT_POLYNOMIAL_EXACT_BERNSTEIN_BOUNDEDNESS_CERTIFIED_PHASES_OPEN`

## Why this is stronger than the Batch-037 grid check

The Batch-037 checks sampled dense grids and numerically located derivative roots. Those are useful computational evidence but do not by themselves establish the inequality for every real point.

Batch 051 instead uses only exact rational operations after reading the frozen runtime floats:

1. `Fraction.from_float` captures each IEEE-style Python float value as its exact binary rational value.
2. The Chebyshev recurrence is expanded into an exact rational power basis.
3. The domain is mapped affinely to `t in [0,1]` with exact rationals.
4. The power polynomial is converted exactly to Bernstein coefficients.
5. Exact de Casteljau subdivision at `t=1/2` recursively refines intervals.
6. On each accepted leaf, the Bernstein convex-hull property bounds the polynomial everywhere on that interval.

No NumPy, SciPy, optimizer, root finder, interval floating-point package, or external solver is needed for the certificate.

## Frozen results

### Global amplitude gate

For `x in [-1,1]`:

- threshold: `1`;
- exact certificate: **PASS**;
- accepted Bernstein leaf intervals: `196`;
- maximum dyadic subdivision depth: `13`;
- smallest certified Bernstein-hull slack among accepted leaves: approximately `3.7988558217421443e-06`.

The last number is a conservative Bernstein-hull margin, **not** a claim that the true maximum polynomial amplitude is `1 - 3.798...e-06`. Batch 037's numerical critical-point maximum remains a separate numerical diagnostic.

### Target approximation gate

For `x in [-0.25,0.25]`:

- target: `gamma*x`, with the exact runtime `gamma` value inherited from Batch 037;
- threshold: the exact runtime value of `epsilon/3 = 0.0033333333333333335`;
- exact certificate: **PASS**;
- accepted Bernstein leaf intervals: `6`;
- maximum dyadic subdivision depth: `3`;
- smallest certified Bernstein-hull slack among accepted leaves: approximately `0.00034946208732517816`.

## Evidence boundary

This is a formal certificate for the **frozen runtime polynomial artifact**, not a general theorem about every polynomial produced by the Batch-037 construction method and not a proof of QOS D.23 as a whole.

It closes these two artifact-scoped gates:

- `formal_global_boundedness_for_frozen_runtime_polynomial_closed = true`;
- `formal_target_error_bound_for_frozen_runtime_polynomial_closed = true`.

It leaves these gates open:

- actual QSP phase synthesis for the degree-81 candidate;
- independent reconstruction of the QSP response from a frozen phase list;
- phase-convention mapping to the Batch-036 QSVT interface;
- a full-channel repaired D.23 statement;
- earlier independent D.16/D.19/D.20/D.21 theorem/interface questions;
- logical-to-physical resources and Lane-C capacity/bandwidth/latency/energy/cost measurements.

## Reproducibility artifacts

- `software/uqpu-prototype/uqpu/qos_d23_exact_bernstein_certificate.py`
- `software/uqpu-prototype/tests/test_qos_d23_exact_bernstein_certificate.py`
- `benchmarks/results/batch051-qos-d23-exact-bernstein-certificate.json`
- `docs/BATCH_051_QOS_D23_EXACT_BERNSTEIN_BOUNDEDNESS.md`

The test suite also deliberately checks that an insufficient subdivision-depth cap is reported as failure rather than silently promoted.

## Next gate — QOS-AUDIT-010B

The highest-information next step is now narrower:

1. pin a public phase-synthesis implementation/version and the exact phase convention;
2. synthesize phases for the fingerprinted degree-81 polynomial without changing its coefficients;
3. freeze the phase vector and synthesis diagnostics;
4. independently reconstruct the QSP response from the phase vector and compare it against the frozen polynomial;
5. map the convention to the Batch-036 QSVT/Corollary-18 interface;
6. if synthesis fails, preserve the failure and return to polynomial construction rather than weakening the evidence gate.

Only after this phase/reconstruction gate closes should degree 81 be propagated further as a concrete QSP circuit resource input.

## Non-claims

Batch 051 does **not** demonstrate or claim:

- real-QPU execution;
- quantum advantage;
- a QSP/QSVT phase sequence;
- measured circuit depth, runtime, energy, memory or cost;
- a full-channel repaired D.23 guarantee;
- GPU/NPU/RAM/DRAM/HBM replacement;
- >=100x advantage;
- >=100,000,000x advantage;
- a new physical law.
