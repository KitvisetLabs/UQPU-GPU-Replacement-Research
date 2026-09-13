# Batch 035 — QOS D.23 Approximate Projected-Block Robustness Audit

**Date:** 2026-09-13  
**Programs:** Issue #1 / QOS-AUDIT-007 / Lane C evidence gate  
**Evidence:** `THEORY_EXECUTABLE_IMPORTED_ROBUSTNESS_INTERFACE_AUDIT`  
**REAL_QPU:** No  
**Quantum advantage demonstrated by UQPU:** No  
**GPU/NPU/RAM/DRAM/HBM replacement demonstrated:** No

## Research Attribution

- **Research Owner / Principal Investigator / Research Direction:** Kanutsanan Pongpanna
- **Facebook:** https://www.facebook.com/LoveMoneyTH
- **YouTube:** https://www.youtube.com/@LoveMoneyTHOfficial
- **AI Research Agent:** OpenAI GPT-5.6 Sol
- **AI-assisted contribution:** public-literature verification; theorem/interface audit; mathematical derivation; executable implementation; test/reproducibility design; research-note and PR preparation.

Attribution describes the roles in this batch only and does not assign work beyond the contribution actually performed.

## Executive result

Batch 034 repaired the **exact-input** positive-margin endpoint of the D.23 amplification step by targeting `(1-b)A`, but deliberately left approximate projected-block robustness open.

Batch 035 identifies an explicit robustness contract already available in the primary QSVT literature. Gilyen et al., arXiv:1806.01838v1, Lemma 23 gives a **linear** perturbation bound for a degree-`d` singular-value-transformation polynomial when the encoded matrices are sufficiently inside the unit ball.

For the D.23 normalized input block

`B = A/s`, with `||A|| <= 1`,

and an approximate projected block `B_tilde` satisfying

`||B_tilde - B|| <= eta`,

we have

`||B|| <= 1/s`

and, by the triangle inequality,

`||(B+B_tilde)/2|| <= 1/s + eta/2`.

Therefore a sufficient condition for Gilyen et al. Lemma 23 is

`eta + (1/s + eta/2)^2 <= 1`.

This condition has the positive closed-form error cap

`eta <= 2 * (sqrt(2 + 2/s) - 1 - 1/s)`.

For `s=4`, the cap is approximately

`0.6622776601683795`.

Thus the normalized projected block is far from the unit-ball endpoint for the small input errors relevant to D.23. Under this explicit interior contract, Lemma 23 yields

`||P^(SV)(B) - P^(SV)(B_tilde)||`

`<= d * sqrt(2 / (1 - ||(B+B_tilde)/2||^2)) * eta`.

Using only the D.23 information gives the executable sufficient upper bound

`<= d * sqrt(2 / (1 - (1/s + eta/2)^2)) * eta`.

**Classification:** `D23_PROJECTED_BLOCK_LINEAR_ROBUSTNESS_MARGIN_CONTRACT_IDENTIFIED`.

The important correction to the research state is that the source-v1 D.215 form `O(d epsilon_1)` is **not inherently ruled out by generic QSVT robustness**. It is supportable by the imported Lemma-23 interface if the required polynomial contract and interior condition are made explicit. This batch does not claim that the source has already supplied every missing interface detail or that Lemma D.23 as a whole is proved.

## 1. Frozen source state

Primary QOS source:

- Haimeng Zhao et al., *Exponential quantum advantage in processing massive classical data*, `arXiv:2604.07639v1`.
- Public arXiv submission history was rechecked on 2026-09-13 and showed v1 only.
- Relevant source location: Lemma D.23 / Eqs. D214-D215.

The proof first constructs a projected block approximating `A/s`. It then applies a degree-`d` QSVT approximation to a linear amplification map and displays an output error of the form

`epsilon_2 + O(d epsilon_1)`.

Batch 035 audits only whether a linear `d * epsilon_1` projected-block perturbation dependence can be supported by an imported theorem contract.

## 2. Primary robustness theorems

Gilyen et al., *Quantum singular value transformation and beyond*, `arXiv:1806.01838v1`, Section 3.3 gives two relevant levels.

### Evidence level A — generic robustness

Lemma 22 requires no extra interior-margin assumption beyond operator norms at most one and gives

`||P^(SV)(B) - P^(SV)(B_tilde)|| <= 4 d sqrt(eta)`.

This is a valid generic fallback, but it is unnecessarily pessimistic for a block known to have norm at most `1/s`.

### Evidence level A — interior linear robustness

Lemma 23 additionally assumes

`eta + ||(B+B_tilde)/2||^2 <= 1`

and then gives the linear bound

`||P^(SV)(B) - P^(SV)(B_tilde)||`

`<= d * sqrt(2/(1-||(B+B_tilde)/2||^2)) * eta`.

The D.23 normalization `B=A/s` creates an explicit route to verify this condition from `s` and `eta` alone.

The theorem provenance and extracted contracts are pinned in

`benchmarks/external/qsvt-robustness-lemma22-23-provenance-2026-09-13.json`.

## 3. Executable interface certificate

The new module computes:

1. the closed-form sufficient Lemma-23 input-error cap;
2. the generic Lemma-22 square-root bound;
3. the interior Lemma-23 linear bound;
4. deterministic bisection for the largest `eta` fitting a requested projected-transform robustness budget for an **actual caller-supplied polynomial degree**.

Crucially, the executable audit does **not** infer an actual degree from Batch 034's big-O theorem scaling. This prevents an asymptotic proxy from being silently promoted into a circuit-depth or query-count measurement.

For a diagnostic robustness budget `0.01/3` and `s=4`, the canonical results are:

| Actual degree parameter | Lemma-23 linear sufficient `eta` | Generic Lemma-22 sufficient `eta` |
| ---: | ---: | ---: |
| 10 | `2.2821078637028224e-4` | `6.944444444444446e-9` |
| 100 | `2.2821703783458297e-5` | `6.944444444444445e-11` |
| 1,000 | `2.2821766284922683e-6` | `6.944444444444446e-13` |
| 10,000 | `2.282177253493733e-7` | `6.944444444444445e-15` |

These numbers are **theorem-interface diagnostics parameterized by a supplied degree**, not measured hardware results and not the actual degree of the Batch-034 repair.

## 4. What this changes about D.215

Before this audit, a conservative reading could use Lemma 22 and obtain a `sqrt(epsilon_1)` perturbation dependence.

Batch 035 shows that D.23 has additional structure: its pre-amplification block is normalized by `s`. For `s>=2`, that block is interior to the unit ball, and the Lemma-23 margin condition can be enforced for a broad positive interval of `eta`.

Therefore the displayed source-v1 `O(d epsilon_1)` form has a plausible theorem-level support route. The remaining interface obligation is to connect the **specific QSVT polynomial used by the repaired amplification** to the hypotheses of Lemma 23 and to carry an actual degree/constant ledger rather than only big-O notation.

This is a repair-oriented result, not an adversarial escalation.

## 5. What is closed and what is not

### Narrowly established

- A sufficient, explicit interior condition exists for linear propagation of the D.23 **projected-block operator error** through a degree-`d` singular-value transformation.
- For `B=A/s`, the condition can be checked using only `s` and the projected input error `eta`.
- The source's displayed `O(d epsilon_1)` functional dependence is supportable under that imported theorem interface.

### Still open

- The specific repaired Batch-034 QSVT polynomial must be wired explicitly to Corollary-8/Lemma-23 hypotheses.
- Big-O degree scaling still lacks a concrete hidden constant and is not an actual circuit depth.
- Projected-block error is not a full-unitary error or a full-channel/diamond-norm error.
- D.16/D.19/D.20/D.21 findings remain independent gates.
- D.23's complete sample/query/time/logical-qubit ledger has not yet been rebuilt with all repaired constants and error allocations.
- Lane-C capacity/bandwidth/latency/energy/cost consequences remain blocked until that full-stack ledger exists.

## 6. Lane C consequence

This result removes one avoidable ambiguity: approximate **projected-block** error need not automatically incur the generic square-root robustness penalty when the normalized D.23 input is explicitly kept in the Lemma-23 interior regime.

It does not establish any physical memory advantage. The repository rule remains:

`projected-block theorem repair != full-channel implementation != quantum advantage != DRAM/HBM replacement != cost reduction`.

No Lane-C ratio is promoted from this batch.

## 7. Reproducibility artifacts

- `software/uqpu-prototype/uqpu/qos_d23_approx_input_robustness.py`
- `software/uqpu-prototype/tests/test_qos_d23_approx_input_robustness.py`
- `software/uqpu-prototype/examples/run_qos_d23_approx_input_robustness.py`
- `benchmarks/results/batch035-qos-d23-approx-input-robustness.json`
- `benchmarks/external/qsvt-robustness-lemma22-23-provenance-2026-09-13.json`

## 8. Next gate — QOS-AUDIT-008

Build a single repaired D.23 projected-block ledger that composes:

- Batch-034 positive target margin / normalization bias;
- an explicit amplification polynomial satisfying the imported QSVT hypotheses;
- actual polynomial degree or a rigorously instantiated degree upper bound rather than a hidden-constant proxy;
- Batch-035 linear approximate-input robustness bound;
- polynomial approximation error;
- oracle/channel-call accumulation separately from projected-block matrix error.

Only after that projected ledger closes should the work attempt a full-unitary/full-channel distance statement or propagate repaired costs into Lane C.

## Non-claims

Batch 035 does **not** demonstrate or claim:

- a real-QPU experiment;
- quantum advantage;
- proof or refutation of QOS Lemma D.23 as a whole;
- QOS-wide validity or invalidity;
- a full-unitary or diamond-norm channel guarantee;
- measured QSVT circuit depth, runtime, or physical-resource cost;
- GPU/NPU/RAM/DRAM/HBM replacement;
- >=100x advantage;
- >=100,000,000x advantage;
- a new physical law.
