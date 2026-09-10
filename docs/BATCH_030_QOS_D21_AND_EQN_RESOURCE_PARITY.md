# Batch 030 — QOS D.21 Composition Budget and EQN-002C Resource-Parity Contract

**Date:** 2026-09-10  
**Programs:** Issue #1 / QOS-AUDIT-003 / EQN-002C-2  
**Evidence:** THEORY_EXECUTABLE_ERROR_BUDGET_AUDIT + THEORY_EXECUTABLE_SENSITIVITY_ANALYSIS + EXTERNAL_METHOD_AUDIT  
**REAL_QPU:** No  
**Quantum advantage:** Not demonstrated  
**UQPU replacement advantage:** Not demonstrated

## Executive result

Batch 030 moves one dependency downstream from the Batch-029 audit of QOS Lemma D.20 to the sparse-index-oracle construction in **Lemma D.21** of `arXiv:2604.07639v1`.

The source proof states that the final sparse-index circuit uses `n + ceil(log2(s_r)) <= 2n` uses of the approximate cumulative-counter oracle and then sets `epsilon_2 = epsilon / n`.

If the stated `epsilon_2` approximation is composed using the standard telescoping/triangle bound, the displayed allocation by itself certifies at most `(n + ceil(log2(s_r))) * epsilon/n`, which can be as large as `2 epsilon`, not `epsilon`.

A direct constant-factor repair is `epsilon_2 = epsilon / (n + ceil(log2(s_r)))`. This does **not** change the asymptotic sample-complexity order. Therefore the correct classification is a **displayed proof/error-budget constant shortfall**, not a counterexample to D.21 as a theorem.

The batch also quantifies how the specific D.20 `sqrt(R)` arithmetic correction from Batch 029 propagates downstream. In the nondegenerate uniform-support regime, `R >= 1/2`, and the visible local coefficient inflation is bounded by about **1.2320006657x (23.20%)**. Thus that specific arithmetic correction alone does not destroy the downstream asymptotic order, although the separate unresolved D.20 proof/interface gaps remain binding.

Finally, the equation-discovery track incorporates a new August-2026 agentic symbolic-regression result, A-SR. Its published protocol uses a fixed **400 evaluated-candidate budget per task** with an 80-candidate profiling phase, while explicitly defining the primary budget in evaluated formulas rather than raw LLM tokens. UQPU therefore strengthens EQN-002C: candidate-count parity is required but is **not sufficient** for compute/cost parity; a second resource ledger is mandatory.

## 1. Source-state check

On 2026-09-10 the arXiv record for Zhao et al., *Exponential quantum advantage in processing massive classical data*, still exposes only `arXiv:2604.07639v1`, submitted 2026-04-08.

Source:
- https://arxiv.org/abs/2604.07639

The associated source repository's latest observed commit remains `haimengzhao/quantum-oracle-sketching@a3fe8d6fe777750749f5e90131180e016088bdaf` from 2026-09-06.

All QOS conclusions in this batch are therefore explicitly scoped to v1.

## 2. Direct D.21 source check

Lemma D.21 states a sparse-index-oracle construction with sample scaling summarized as `O~(R N s_r^3 / epsilon)`.

The proof builds a phase oracle using QSVT from the cumulative-counter unitary of D.20 and obtains an `epsilon_2` approximation to the cumulative-counter phase oracle in Eq. D201. The phase oracle is converted to the XOR cumulative-counter oracle in D202-D203. Binary search then uses the oracle to construct the sparse index and later erase the `k` register.

Source PDF:
- https://arxiv.org/pdf/2604.07639
- PDF pages 61-63, Eqs. D188-D209.

At the end of the construction the source explicitly states:

- number of uses: `q = n + ceil(log2(s_r)) <= 2n`;
- allocation: `epsilon_2 = epsilon/n`.

For sequential channels/operators, the ordinary telescoping estimate allocates a final error no larger than the sum of the per-use errors. Under that accounting,

`q * epsilon_2 = (1 + ceil(log2(s_r))/n) * epsilon`.

This is generally greater than `epsilon` whenever `s_r > 1`.

### Representative executable calibration

New module:

`software/uqpu-prototype/uqpu/qos_d21_audit.py`

For `N = 2^20 = 1,048,576`, `s_r = 1024`, and `epsilon = 0.01`, we have `n = 20`, `m = ceil(log2(s_r)) = 10`, and `q = 30` uses.

The displayed source allocation gives `epsilon_2 = 0.01/20 = 0.0005`. A direct triangle budget is then `30 * 0.0005 = 0.015 = 1.5 epsilon`.

A triangle-safe allocation is `epsilon_2 = 0.01/30 = 0.0003333333333333333`.

In the allowed envelope `s_r <= N`, `m <= n`, so this specific displayed mismatch is bounded by a factor of two. Tightening the per-call precision by this constant factor changes logarithmic arguments/constants but does not change the stated asymptotic order.

Machine classification:

`SOURCE_V1_D21_DISPLAYED_ERROR_BUDGET_SHORTFALL`

with `D21_THEOREM_REFUTED = false`.

A sharper source-specific composition argument could also close this gap; absent such an argument, the displayed `epsilon/n` choice alone is insufficient for the stated final `epsilon` under the ordinary telescoping bound.

## 3. Conditional propagation of the Batch-029 D.20 arithmetic correction

Batch 029 retained the `sqrt(R)` term visible immediately before source D184. The source displayed local coefficient is

`a_source(R) = ((pi^2 + 4 pi)/2) R`.

The corrected-visible-arithmetic coefficient is

`a_visible(R) = (pi^2/2) R + 2 pi sqrt(R)`.

Their ratio is

`a_visible/a_source = (pi^2/2 + 2 pi/sqrt(R)) / (pi^2/2 + 2 pi)`.

For the nondegenerate uniform hierarchical support used in this audit, `K >= 2` implies `R >= 1 - 1/K >= 1/2`.

The ratio decreases with `R`, because only the `1/sqrt(R)` term varies. Therefore its maximum on the admissible interval `[1/2, 1]` occurs at `R=1/2`:

`max ratio = 1.2320006656581772`.

So the largest inflation from this **specific visible arithmetic correction** is about `23.20006656581772%`.

This is a useful limiting result: the D.183 algebra issue should be fixed, but this issue by itself is not evidence that the claimed downstream `O~(R N s_r^3/epsilon)` scaling must change class.

Important boundary:

- this does not repair the full D.20 proof;
- it does not resolve history-selected-coordinate/interface questions;
- it does not establish D.21 or D.23 correctness;
- it does not establish QOS advantage.

## 4. EQN-002C external-method delta — A-SR

A new relevant preprint is *A-SR: Self-Evolving Agentic LLMs for Symbolic Regression via Hierarchical Coordination*, `arXiv:2608.04872`, submitted 2026-08-05.

The paper reports, across the four LSR-Synth scientific domains, average `Acc@0.01` of **48.30%** for A-SR using Llama3.1-8B-Instruct versus **25.79%** for the stated DE baseline.

More important for UQPU benchmark design than the headline accuracy is the resource protocol:

- maximum evaluated candidates `B = 400` per task;
- early profiling budget `B0 = 80`;
- the primary search budget counts **evaluated formulas**, not raw LLM tokens.

Source:
- https://arxiv.org/abs/2608.04872

UQPU has **not** reproduced this result and must not present it as project evidence.

## 5. Strengthened EQN-002C budget contract

The Batch-029 `BANK / LLM / UNION` separation remains mandatory. Batch 030 adds a second axis of fairness.

### Ledger A — search opportunity

Every method must report and, where the experiment requires direct parity, cap:

- evaluated candidate formulas;
- accepted/rejected candidates;
- continuous-parameter fitting attempts/evaluations;
- random seeds.

### Ledger B — resource consumption

Every method must additionally report when measurable:

- LLM calls;
- prompt tokens;
- completion tokens;
- model/provider and version;
- numerical optimizer evaluations;
- wall time;
- CPU/GPU model and count;
- peak memory;
- monetary API/compute cost when applicable.

Thus `EQUAL_CANDIDATE_BUDGET != EQUAL_COMPUTE_COST`.

Candidate parity is useful for evaluating proposal/search efficiency, but cannot alone support economic or energy claims.

## 6. Canonical artifacts

Executable QOS D.21 audit:

`software/uqpu-prototype/uqpu/qos_d21_audit.py`

Tests:

`software/uqpu-prototype/tests/test_qos_d21_audit.py`

Runner:

`software/uqpu-prototype/examples/run_qos_d21_audit.py`

Machine-readable Batch-030 result:

`benchmarks/results/batch030-qos-d21-and-eqn-budget.json`

A-SR literature provenance:

`benchmarks/external/asr-provenance-2026-09-10.json`

## 7. Next falsifiable gates

### QOS-AUDIT-004

Move downstream to the block-encoding composition in D.23 and explicitly map which guarantees depend on D.19, D.20 and D.21. Separate constant-factor proof accounting, theorem-level counterexamples, interface/clean-ancilla requirements, and source-v1 dependencies that would need rechecking after any v2.

### EQN-002C-3

Until authorized official LLM-SRBench numerical bytes are available, do not fabricate an official external run. Instead, implement the resource ledger and BANK/LLM/UNION evaluator contract on internal/open fixtures, then apply the same frozen contract to the official dataset after revision/checksum pinning.

A-SR can become a future comparator only if its implementation/model requirements can be pinned and its search budget can be made comparable without silently treating evaluated-candidate parity as full compute parity.

## Non-claims

Batch 030 does not claim a refutation of QOS as a whole, a theorem-level counterexample to D.21, a repaired proof of D.20 or D.21, a real-QPU result, demonstrated GPU/NPU/RAM/storage replacement, `>=100x` or `>=100,000,000x` advantage, discovery of a new physical law, or reproduction of A-SR/the official gated LLM-SRBench numerical benchmark.
