# Batch 036 — QOS D.23 Composed Repair Ledger

**Date:** 2026-09-13  
**Programs:** Issue #1 / QOS-AUDIT-008 / Lane C evidence gate  
**Evidence:** `THEORY_EXECUTABLE_IMPORTED_INTERFACE_COMPOSITION`  
**REAL_QPU:** No  
**Quantum advantage demonstrated by UQPU:** No  
**GPU/NPU/RAM/DRAM/HBM replacement demonstrated:** No

## Research Attribution

- **Research Owner / Principal Investigator / Research Direction:** Kanutsanan Pongpanna
- **Facebook:** https://www.facebook.com/LoveMoneyTH
- **YouTube:** https://www.youtube.com/@LoveMoneyTHOfficial
- **AI Research Agent:** OpenAI GPT-5.6 Sol
- **AI-assisted contribution:** primary-source literature verification; theorem/interface and parity audit; mathematical composition; executable implementation; reproducibility-test design; results and research-note preparation.

Attribution describes roles in this batch only and does not assign work beyond the contribution actually performed.

## Executive result

Batch 034 supplied an endpoint-safe **positive-margin** repair for the exact projected input by replacing the target `A` with `(1-b)A`. Batch 035 then established an explicit imported **linear projected-block robustness** route, conditional on a degree-`d` QSVT polynomial satisfying the required interface.

Batch 036 composes those two results against the actual constructive proof of Gilyen et al. Theorem 30 and makes a previously implicit interface explicit.

Theorem 30 does not merely assert existence of an unspecified amplifier. Its proof sets

- `t = (1-delta/2)/gamma`,
- `delta' = delta/(2 gamma)`,
- `epsilon' = epsilon_amp/gamma`,

constructs an even bounded rectangle polynomial `P_rect`, and defines the odd amplification polynomial

`P_amp(x) = gamma * x * P_rect(x)`.

The proof states that `|P_amp(x)| <= 1` on `[-1,1]`, and that it approximates `gamma*x` with the required multiplicative precision on

`[-(1-delta)/gamma, (1-delta)/gamma]`.

For the Batch-034 endpoint repair,

`gamma = s(1-b)`, `delta=b`,

so

`(1-delta)/gamma = 1/s`.

Therefore the imported Theorem-30 polynomial family covers exactly the normalized D.23 endpoint `A/s` while keeping a positive theorem margin.

**Classification:** `D23_REPAIRED_PROJECTED_LEDGER_COMPOSED_NUMERIC_DEGREE_OPEN`.

This closes the polynomial/interface composition **conditionally on an actual degree**. It does not close a certified numerical degree, because the inspected primary construction still exposes the sign/rectangle approximation degree only in asymptotic big-O notation.

## 1. Primary-source interface map

### Gilyen et al. — imported QSVT source

Primary source: Gilyen, Su, Low, Wiebe, *Quantum singular value transformation and beyond*, `arXiv:1806.01838v1`.

Relevant source contracts rechecked on 2026-09-13:

- **Corollary 18:** a real degree-`n` polynomial of parity `n mod 2`, bounded by one on `[-1,1]`, admits a singular-value-transform implementation. Its proof obtains the real transform by lifting to a Corollary-8 polynomial `P` and averaging the transforms for `P` and `P*`.
- **Lemma 23:** under the interior condition, a degree-`n` Corollary-8 polynomial obeys a linear perturbation bound proportional to `n ||A-A_tilde||`.
- **Lemma 29:** constructs the bounded rectangle polynomial used by Theorem 30.
- **Theorem 30:** constructs uniform singular-value amplification using `P_amp(x)=gamma*x*P_rect(x)`.

The theorem and proof are pinned in `benchmarks/external/qsvt-theorem30-composition-provenance-2026-09-13.json`.

### QOS source-v1 local interface

Primary QOS source: Zhao et al., *Exponential quantum advantage in processing massive classical data*, `arXiv:2604.07639v1`.

The local Lemma D.8 as printed requires an **even** real polynomial and even degree. Later, the D.23 proof applies QSVT to the **odd** linear map `f(x)=s*x`.

This is an interface mismatch in the displayed local route: the printed D.8 statement does not itself cover the later odd linear polynomial. It is **not** a D.23 refutation, because the cited Gilyen framework contains Corollary 18, which does provide the needed odd-real-polynomial implementation route.

Batch 036 therefore records the repaired interface explicitly rather than silently treating D.8 as if it covered both parities.

## 2. Corollary-18 to Lemma-23 robustness bridge

Batch 035 used the Lemma-23 linear robustness contract. Theorem 30's amplifier is stated through Corollary 18 rather than directly as a Corollary-8 polynomial, so this bridge must be checked.

Corollary 18 proves that for real `P_amp` there is a Corollary-8 polynomial `P` such that the desired real singular-value transform is the average of the transforms associated with `P` and `P*`.

Apply Lemma 23 to both `P` and `P*`. They have the same degree and the same matrix-margin hypothesis. By triangle inequality, averaging the two perturbation bounds gives the same coefficient:

`||P_amp^(SV)(B) - P_amp^(SV)(B_tilde)||`

`<= d * sqrt(2/(1-||(B+B_tilde)/2||^2)) * ||B-B_tilde||`.

Thus no additional factor of two is required merely to pass from the Corollary-8 lift to the real Corollary-18 polynomial.

This closes the specific **Batch-034 polynomial family -> Batch-035 robustness theorem** interface, conditional on the polynomial degree and the Lemma-23 interior hypothesis.

## 3. Reproducible projected-error ledger

For a canonical total projected-block error target `epsilon=0.01`, Batch 036 uses an intentionally transparent three-way split:

- normalization bias: `epsilon/3`,
- Theorem-30 amplification approximation: `epsilon/3`,
- approximate projected-input robustness: `epsilon/3`.

At `s=4` this gives

- `b = 0.003333333333333333`,
- `target_scale = 0.9966666666666667`,
- `gamma = 3.986666666666667`,
- `delta = 0.003333333333333333`,
- `t = 0.25041806020066887`,
- `delta' = 0.00041806020066889626`,
- `epsilon' = 0.0008361204013377925`,
- `(1-delta)/gamma = 0.25 = 1/s`.

The total sufficient projected error bound is

`bias + target_scale * epsilon_amp + robustness`

`= 0.00998888888888889 <= 0.01`.

The slight slack appears because Theorem 30 controls relative amplification error on the retained target, whose norm is `target_scale < 1`.

## 4. Conditional actual-degree certificates

The source does not provide a certified numerical universal constant for Theorem-30 degree, so Batch 036 does **not** invent one. Instead the executable artifact accepts an **actual caller-supplied odd degree** and computes the required upstream tolerances.

For `s=4`, projected target error `0.01`, and robustness budget `0.01/3`:

| Actual odd degree parameter | Max sufficient projected input error `eta` | Sufficient per-query diamond budget for separate `0.01` channel target |
| ---: | ---: | ---: |
| 101 | `2.2595747001045743e-5` | `9.900990099009902e-5` |
| 1,001 | `2.2798967324535688e-6` | `9.99000999000999e-6` |
| 10,001 | `2.2819490585948172e-7` | `9.99900009999e-7` |

These are theorem-interface calculations for supplied degree values. They are not measurements and are not claims about the actual degree of the repaired D.23 circuit.

## 5. New asymptotic consequence for the sufficient repair route

The positive-margin route of Batch 034 has

`d = O((s/epsilon) log(s/epsilon))`

for fixed positive error-budget fractions.

Batch 035 linear robustness then requires, up to margin constants,

`d * eta = O(epsilon)`,

so a sufficient upstream projected-block tolerance scales as

`eta = O(epsilon/d)`

`= O(epsilon^2 / (s log(s/epsilon)))`.

The source D.216 separately accumulates approximate-oracle **channel** error over `O(d)` calls. Under the same ordinary diamond-norm subadditivity used by the source, a sufficient per-call channel tolerance has the same scaling

`epsilon_3 = O(epsilon/d)`.

The D.217 sample-count structure before substituting a particular `d` can therefore be written schematically as

`M = O(R^2 n^2 s^3 d^2 polylog / epsilon)`.

Substituting the sufficient positive-margin repair degree gives the conditional structure

`M = O(R^2 n^2 s^5 polylog / epsilon^3)`.

Here `polylog` intentionally absorbs the source's existing logarithmic factors and the repaired logarithms. This is **not** a lower bound, not an exact sample count, and not a claim that every possible D.23 repair has this cost. It is the consequence of this explicit sufficient repair route.

## 6. Diagnostic proxy ratios

To expose the size of the asymptotic change without pretending the hidden constants are known, the executable result compares

- repair proxy: `(gamma/delta) log(gamma/epsilon_amp)`,
- source displayed proxy: `s log(2/epsilon)`.

At `s=4`, the degree-proxy ratio and the corresponding D.217 common-factor proxy ratio (its square) are:

| `epsilon` | degree-proxy ratio | D.217 common-factor proxy ratio |
| ---: | ---: | ---: |
| `0.05` | `87.3886177378336` | `7636.770510129205` |
| `0.01` | `399.925956832441` | `159940.77094834344` |
| `0.001` | `3705.8222284783524` | `13733118.38908426` |
| `0.0001` | `35426.38020812423` | `1255028414.6505764` |

These ratios are **dimensionless diagnostic proxies with hidden constants omitted**. They are not measured runtimes, depths, sample counts, speedups, slowdowns, or hardware-resource ratios.

## 7. What is closed and what remains open

### Narrowly closed in Batch 036

- The Batch-034 positive-margin repair can be mapped into the **actual polynomial form used in the proof** of imported Theorem 30.
- The certified linear domain endpoint is exactly `1/s` for the endpoint repair.
- The odd real Theorem-30 polynomial can be connected to Batch-035 Lemma-23 robustness through the Corollary-18 lift/average argument.
- The local QOS D.8 parity restriction is explicitly separated from the imported odd-polynomial route.
- A deterministic ledger now maps any supplied actual odd degree to projected-input and per-query channel tolerances.

### Still open

- A certified **numerical degree** for the constructive Theorem-30 polynomial remains open because the inspected primary sign/rectangle approximation result uses hidden big-O constants.
- No concrete QSP phase sequence has been synthesized and independently checked for this repaired polynomial.
- Earlier D.16/D.19/D.20/D.21 findings remain independent gates.
- The projected-block error ledger is not a full-unitary or full-channel repaired D.23 proof.
- Lane-C capacity, bandwidth, latency, energy and economics remain blocked from promotion.

## 8. Reproducibility artifacts

- `software/uqpu-prototype/uqpu/qos_d23_composed_repair_ledger.py`
- `software/uqpu-prototype/tests/test_qos_d23_composed_repair_ledger.py`
- `software/uqpu-prototype/examples/run_qos_d23_composed_repair_ledger.py`
- `benchmarks/results/batch036-qos-d23-composed-repair-ledger.json`
- `benchmarks/external/qsvt-theorem30-composition-provenance-2026-09-13.json`

## Next gate — QOS-AUDIT-009

Highest-information next step:

1. recover or construct a **numerically explicit bounded odd amplification polynomial** with a concrete certified degree for at least one frozen `(s, epsilon, b)` case;
2. verify global boundedness and the target-domain approximation independently;
3. if possible, synthesize/verify a corresponding QSP/QSVT phase sequence without calling it hardware execution;
4. only then replace the conditional degree parameter in this ledger and propagate a concrete repaired query/sample upper bound;
5. keep full-channel and Lane-C physical/economic claims separately gated.

If a primary-source or independently certifiable numerical degree constant cannot be obtained, the correct result is to keep the degree gate open rather than manufacture a circuit-resource claim.

## Non-claims

Batch 036 does **not** demonstrate or claim:

- a real-QPU experiment;
- quantum advantage;
- proof or refutation of QOS Lemma D.23 as a whole;
- QOS-wide validity or invalidity;
- a certified numerical QSVT degree from the primary source;
- measured circuit depth, runtime, or physical-resource cost;
- a full-unitary or full-channel/diamond repaired D.23 guarantee;
- GPU/NPU/RAM/DRAM/HBM replacement;
- >=100x advantage;
- >=100,000,000x advantage;
- a new physical law.
