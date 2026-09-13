# Batch 044 — FND-007B3 Quality-Adjusted Hardware Threshold Ledger

**Status:** source-grounded conditional hardware diagnostic  
**Primary lane:** Lane D — Quantum / Photonic / Semiconductor Devices / Fabrication / Packaging  
**Predecessors:** Batch 042 / FND-007B and Batch 043 / FND-007B2

## Research Attribution

- Research Owner / Principal Investigator / Research Direction: **Kanutsanan Pongpanna**
- Facebook: https://www.facebook.com/LoveMoneyTH
- YouTube: https://www.youtube.com/@LoveMoneyTHOfficial
- AI Research Agent: **OpenAI GPT-5.6 Sol**
- AI-assisted contribution: primary-source hardware-data audit, conditional quality model, finite-shot bounds, coherence-exposure diagnostics, executable implementation/tests, evidence classification and research documentation.

Attribution reflects roles in this batch only.

## Question

Batch 042 established a construction-specific gate/register advantage for native qudits over the paper's one-hot qubit comparator. Batch 043 independently cross-checked the Hamiltonian and observable calculation.

The next question is stricter:

> **Does a smaller entangling-gate count necessarily imply a better hardware execution once finite-shot statistics, gate quality, coherence exposure, readout/control overhead and runtime are considered?**

The answer from this gate is **no, not automatically**. Instead of assuming hardware advantage, Batch 044 converts the gate-count result into explicit break-even thresholds and falsifiers.

## Primary source facts used

Michael Meth et al., *Simulating 2D lattice gauge theories on a qudit quantum computer*, Nature Physics 21, 570–576 (2025), arXiv:2310.12110v3, DOI 10.1038/s41567-025-02797-w.

The article reports:

- trapped `40Ca+` mixed-dimensional qubit/qudit hardware,
- qutrit VQE/statistical results averaged over **150 repetitions**,
- ququint results averaged over **300 repetitions** in the gauge-dimension study,
- time-evolution results averaged over **150 repetitions**,
- axial-mode heating rate `2.7(2)` phonons/s,
- motional coherence time `27.4(4) ms`,
- `D5/2` lifetime `T1 ≈ 1.1 s`,
- optical coherence `T2 = 92(9) ms`,
- a representative blue-sideband Rabi frequency `2π × 4 kHz`,
- experimental results compared with an experimentally motivated noise model.

The source also explains that the controlled qudit rotations use phonon-mediated sideband operations and that state detection uses fluorescence on a CCD camera.

These data establish real hardware context, but they are **not enough by themselves to instantiate a directly comparable end-to-end native-qudit-vs-one-hot-qubit hardware benchmark**. In particular, this batch does not have a pinned apples-to-apples pair of per-entangler fidelity, compiled duration, SPAM confusion matrix, calibration burden and monetary cost for the two competing constructions.

## Frozen d=3 resource pairs from Batch 042

### Full gauge single plaquette

```text
native qudit entangler-equivalent count = 26
one-hot qubit entangling-gate count     = 90
```

### Pure gauge periodic plaquette

```text
native qudit entangler-equivalent count = 8
one-hot qubit entangling-gate count     = 84
```

These remain **source/construction-specific** resource counts.

## Conditional quality model

To make the hardware question falsifiable without inventing unavailable fidelity data, define the intentionally simple diagnostic

```text
circuit survival proxy = p^G
quality-adjusted entangler cost = G / p^G
```

where:

- `G` is the counted entangler or entangler-equivalent burden,
- `p` is a hypothetical independent-identical per-entangler success probability.

This is not a physical noise model. It omits SPAM, coherent/correlated errors, compiler effects, mitigation, parallel schedules, leakage, calibration and cost. Its role is to answer one narrow question:

> How poor could native-qudit entangler quality become before the count advantage disappears under this proxy?

For native-qudit count `G_d`, qubit count `G_b`, and qubit success `p_b`, break-even is

```text
G_d / p_d^G_d = G_b / p_b^G_b
```

so

```text
p_d = [(G_d/G_b) p_b^G_b]^(1/G_d).
```

## Full-gauge d=3 break-even result

For `26` native-qudit entangler-equivalents versus `90` one-hot-qubit entanglers:

| assumed qubit `p_b` | native-qudit break-even `p_d` | equal-fidelity cost ratio, qubit / qudit |
|---:|---:|---:|
| 0.980 | 0.8889710169965934 | 12.612474963585528 |
| 0.990 | 0.9207674043211239 | 6.585923885897566 |
| 0.995 | 0.9369650440258070 | 4.770808603159149 |
| 0.999 | 0.9500682377259113 | 3.690438012779591 |

Example interpretation:

- if the one-hot-qubit entangler proxy were `p_b = 0.99`,
- the native-qudit construction would reach break-even at only `p_d ≈ 0.92077` under this specific `G/p^G` proxy.

This is substantial conditional headroom from the lower count. It is **not** evidence that the actual native-qudit entangler fidelity is 0.92077, nor that the actual qudit hardware is already superior end-to-end.

## Pure-gauge d=3 break-even result

For `8` versus `84`:

| assumed qubit `p_b` | native-qudit break-even `p_d` | equal-fidelity cost ratio, qubit / qudit |
|---:|---:|---:|
| 0.980 | 0.6028720257920178 | 48.753696162853274 |
| 0.990 | 0.6706885326500162 | 22.537955115604852 |
| 0.995 | 0.7071209192119038 | 15.368630259007746 |
| 0.999 | 0.7375457486324559 | 11.329537830128677 |

The much larger count gap creates larger conditional headroom. Again, this is only a normalized threshold diagnostic.

## Coherence-exposure ledger

A second count-only diagnostic asks how much **mean serial time per counted entangler** would fit inside one reported coherence interval if every counted operation were serialized.

Using the reported `27.4 ms` motional coherence:

| route | native qudit | one-hot qubit |
|---|---:|---:|
| full gauge d=3 | `1053.85 µs` | `304.44 µs` |
| pure gauge d=3 | `3425.00 µs` | `326.19 µs` |

Using optical `T2 = 92 ms`:

| route | native qudit | one-hot qubit |
|---|---:|---:|
| full gauge d=3 | `3538.46 µs` | `1022.22 µs` |
| pure gauge d=3 | `11500.00 µs` | `1095.24 µs` |

These are **not measured gate durations**. They are count-only serial timing ceilings useful for future compiled-runtime falsification.

At the reported heating rate, the expected rate-times-interval exposure across one motional coherence time is

```text
2.7 phonons/s × 0.0274 s = 0.07398 phonons.
```

This is context only, not a complete motional-noise model.

## Finite-shot ledger

The source's qutrit VQE statistics use 150 repetitions. To avoid pretending to reconstruct the source's Monte-Carlo error bars, Batch 044 adds an independent worst-case concentration diagnostic for a generic observable bounded in `[-1, 1]`.

For `N=150`:

```text
worst-case SEM <= 1/sqrt(150) = 0.0816496581
95% Hoeffding half-width <= 0.2217770488
```

For `N=300`:

```text
worst-case SEM <= 0.0577350269
95% Hoeffding half-width <= 0.1568200551
```

A sufficient 95% Hoeffding repetition count for a generic `[-1,1]` variable is:

| target absolute half-width | sufficient repetitions |
|---:|---:|
| 0.10 | 738 |
| 0.05 | 2,952 |
| 0.02 | 18,445 |
| 0.01 | 73,778 |

These are conservative generic bounds, not claims that the experiment requires those exact shot counts.

## Main research result

The Batch-042 source-scoped native-qudit gate-count advantage has **substantial conditional headroom** under a simple quality-adjusted survival proxy.

However, Batch 044 deliberately does **not** upgrade that result into measured hardware advantage because the required comparable inputs are still open:

- native-qudit vs one-hot-qubit per-entangler fidelity on a controlled target,
- exact compiled gate durations,
- leakage and coherent/correlated errors,
- readout confusion matrices / SPAM,
- serial versus parallel scheduling,
- calibration overhead,
- mitigation/post-selection cost,
- wall-clock throughput,
- monetary/energy cost.

## Falsifier

The central falsifier is explicit:

> If measured native-qudit entangler quality, duration, SPAM, control/calibration burden, or cost crosses the frozen break-even boundary, the construction-specific gate-count advantage **does not survive** as a quality-adjusted hardware advantage.

This converts “qudits use fewer gates” from a promotional statement into an experimentally testable hardware gate.

## Evidence classification

```text
classification:
  LATTICE_QED_QUDIT_QUALITY_ADJUSTED_HARDWARE_THRESHOLD_LEDGER

evidence level:
  SOURCE_GROUNDED_CONDITIONAL_HARDWARE_DIAGNOSTIC
```

## Executable artifacts

- `software/uqpu-prototype/uqpu/lattice_gauge_qudit_quality_ledger.py`
- `software/uqpu-prototype/tests/test_lattice_gauge_qudit_quality_ledger.py`
- `benchmarks/results/batch044-fnd-007b3-quality-adjusted-hardware-ledger.json`
- this note

## Next gates

### FND-007B3B — measured/comparable hardware pin

Before claiming measured quality-adjusted qudit advantage, pin directly comparable experimental or controlled-simulator values for:

- per-entangler quality,
- compiled duration,
- SPAM/readout,
- leakage,
- schedule/parallelism,
- calibration/retry burden,
- wall-clock and cost.

### FND-007B4 — SU(3)/QCD-adjacent symmetry protection

Proceed in parallel to an executable small-model SU(3)/QCD-adjacent symmetry-protection reproduction with an explicit gauge/symmetry-violation metric.

### FND-007C — string/holography mapping

Remain separate until mapped to realizable workload/resource variables.

## Non-claims

This batch does **not** demonstrate:

- measured end-to-end native-qudit hardware advantage,
- real-QPU reproduction by UQPU,
- quantum advantage,
- a direct quark or elementary-particle computer,
- QCD simulation demonstrated by UQPU,
- a universal qudit advantage,
- GPU/NPU/RAM/DRAM/HBM replacement,
- `>=100x` or `>=100,000,000x` savings,
- Data-Center-to-One-Phone achievement,
- a new physical law.

The publishable result is narrower: **the count advantage now has an executable hardware break-even ledger and explicit falsifier, while the missing data needed for an end-to-end hardware claim are separated rather than silently assumed.**
