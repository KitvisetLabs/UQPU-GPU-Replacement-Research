# Batch 029 — QOS D.20 Boundary/Arithmetic Audit and LLM-SRBench Count Reconciliation

**Date:** 2026-09-10  
**Programs:** Issue #1 / QOS-AUDIT-002 / EQN-002C  
**Evidence:** THEORY_EXECUTABLE_REPRODUCTION + PUBLIC_METADATA_AUDIT  
**REAL_QPU:** No  
**Quantum advantage:** Not demonstrated  
**UQPU replacement advantage:** Not demonstrated

## Executive result

Batch 028 independently reproduced the finite repeated-pair counterexample to the sufficient threshold printed in QOS Theorem D.16 / Eq. D99. Batch 029 advances one dependency downstream to the cumulative-counter construction in **Lemma D.20** of `arXiv:2604.07639v1`.

Two source-v1-scoped findings are made executable:

1. **D185 boundary:** the printed sample prescription evaluates to zero at the allowed `R=0` boundary, while a zero-sample compiler cannot uniformly approximate two admissible target cumulative unitaries within the stated `epsilon=1/2`.
2. **D183 displayed arithmetic:** the source proof visibly obtains a term proportional to `sqrt(R)/M` and then writes it as `R/M`. For `0<R<1`, these quantities are unequal. Retaining `sqrt(R)` increases the sufficient sample count in the displayed arithmetic.

This batch also strengthens the LLM-SRBench provenance conclusion: the official paper/prose states 239 tasks, while current public official dataset metadata exposes split counts summing to 240. A July-2026 independent arXiv study reports using the current 129-task LSR-Synth snapshot and, more importantly for EQN-002C design, shows why an LLM-specific scientific-prior claim must be separated from ordinary *library reachability*.

No result in this batch demonstrates a QOS-wide failure, a repaired D.20 theorem, a quantum speedup, UQPU replacement, or the project's >=100x / 10^8x targets.

## 1. Source-state check

On 2026-09-10, the arXiv record for Zhao et al., **Exponential quantum advantage in processing massive classical data**, still lists only:

`arXiv:2604.07639v1` — submitted 2026-04-08.

Source:
- https://arxiv.org/abs/2604.07639

The associated public implementation repository still had latest observed commit:

`haimengzhao/quantum-oracle-sketching@a3fe8d6fe777750749f5e90131180e016088bdaf`  
dated 2026-09-06.

Because no source v2 is public at the time of this check, the present findings remain explicitly scoped to source v1.

## 2. Direct D.20 source check

The source PDF defines the cumulative-counter unitary in Lemma D.20 and states sample scaling `M = O(R N s_r / epsilon)` in Eq. D160.

Direct source:
- https://arxiv.org/pdf/2604.07639
- PDF page 57, Eqs. D158-D161.

Near the end of the proof, source Eq. D183 contains the chain

`sqrt((1/K) * K R) / M`

and then replaces this dependence with `R/M`. The next displayed bound D184 and sample prescription D185 are linear in `R`.

Direct source:
- same PDF, page 60, Eqs. D183-D186.

For `0<R<1`,

`sqrt(R) > R`.

Therefore that algebraic replacement is not an identity or a valid upper bound in the required direction without an additional assumption/constant argument.

The independent version-specific audit reaches the same classification and derives a corrected **visible-arithmetic-only** bound while explicitly not claiming a repaired D.20 theorem:
- https://github.com/gatephys/quantum-oracle-sketching/blob/main/Paper_A_Technical_Supplement_v2.md
- Version-2 DOI: https://doi.org/10.5281/zenodo.21704142

## 3. Executable D185 zero-sample boundary certificate

New module:

`software/uqpu-prototype/uqpu/qos_d20_audit.py`

For the public-parameter witness

- `N = 4`
- `s_r = 1`
- `K = 1`
- `R = 0`
- `epsilon = 1/2`

the sample expression printed in D185 evaluates to

`M_printed = 0`.

A stream-dependent empirical-frequency construction is not meaningful with `M=0`. More strongly, the audit's two target cumulative unitaries produce, on the same `|+>` input, pure output states of overlap `1/2`. Their unnormalized trace-norm distance is

`sqrt(3) = 1.7320508075688772`.

By triangle inequality, any common zero-sample channel must therefore be at unnormalized diamond distance at least

`sqrt(3)/2 = 0.8660254037844386`

from at least one target, which is strictly greater than `epsilon=0.5`.

Machine-readable conclusion:

`SOURCE_V1_D20_D185_BOUNDARY_REPRODUCED`

This is a boundary refutation of the printed prescription under the audited stream-compiler interpretation, not a statement that QOS is impossible.

## 4. Executable D183 visible-arithmetic certificate

The source proof's final displayed D184 bound after the substitution is

`((pi^2 + 4*pi) K R) / (2 M)`.

Retaining the preceding `sqrt(R)` term instead gives the local visible-arithmetic expression

`pi^2 K R / (2 M) + 2*pi*K*sqrt(R)/M`.

This is **not** promoted as a repaired theorem because the separate history-selected-coordinate issue remains.

For the nondegenerate legal calibration

- `K = 2`
- `R = 0.5`
- `epsilon = 0.05`

the uniform-support constraint `R >= 1 - 1/K` is exactly saturated.

The substitution gap is

`sqrt(R)/R = sqrt(2) = 1.4142135623730951`.

Integerizing the source displayed linear-R bound gives:

`M_source = 225`.

At `M=225`:

- source displayed D184 value: `0.049857722256552287 <= 0.05`
- corrected visible arithmetic: `0.06142474700827294 > 0.05`

The corrected visible arithmetic requires:

`M_visible = 277`

for which its value is

`0.0498937475698968 <= 0.05`.

So, in this calibration, the displayed linear-R arithmetic understates the sample budget by 52 samples (about 23.1%).

Again, this corrects only the visible algebra. It does not repair the complete proof of D.20.

## 5. LLM-SRBench denominator reconciliation

The ICML 2025 paper states:

- 239 total problems;
- four scientific domains;
- best reported symbolic accuracy 31.5%.

Source:
- https://proceedings.mlr.press/v267/shojaee25a.html

The current public README metadata of the **official gated dataset** `nnheui/llm-srbench` exposes:

- Biology: 24
- Chemistry: 36
- Materials: 25
- Physical oscillations: 44
- LSR-Transform: 111

Total:

`24 + 36 + 25 + 44 + 111 = 240`.

Source:
- https://huggingface.co/datasets/nnheui/llm-srbench/blob/main/README.md

The dataset remains gated for numerical file access, so UQPU has **not** directly executed or checksummed the official numerical bytes in this batch.

A separate July-2026 arXiv study, **Library Reachability in LSR-Synth**, reports using **129 LSR-Synth tasks** from a current local snapshot and separates fixed semantics-free candidate libraries from LLM-generated candidates:
- https://arxiv.org/abs/2607.28684

This independently supports treating the released-snapshot count as 129 Synth + 111 Transform = 240 for provenance discussion, while the original paper's prose remains 128 Synth + 111 = 239.

UQPU policy is therefore:

`PUBLIC_RELEASE_COUNT = 240` for metadata/provenance discussions.

But:

`OFFICIAL_BYTE_EXECUTION = NOT YET COMPLETED`.

We will not invent a post-hoc 239-task slice because no first-party exclusion rule has yet been established in our directly accessed evidence.

## 6. New experimental-design consequence for EQN-002C

The July-2026 LSR-Synth analysis adds a more important methodological warning than the one-task count discrepancy.

A correct future EQN-002C comparison must distinguish at least:

1. **BANK:** semantics-free fixed operator/candidate library;
2. **LLM:** candidates generated with scientific context;
3. **UNION:** fixed library plus LLM-generated candidates.

Otherwise, a high recovery score can be misinterpreted as evidence that an LLM supplied useful scientific priors when the target was already reachable by a conventional fixed library under the same fitting/search budget.

Therefore the next external benchmark protocol will record:

- candidate-library provenance;
- semantic access/blinding;
- equal search/evaluation budget;
- ID and OOD numerical error;
- symbolic/structural recovery;
- false-discovery rate;
- wall time and candidate evaluations;
- incremental success of UNION over BANK, task-paired rather than only aggregate.

This strengthens the existing rule:

`good fit != discovered law`

into:

`good symbolic score != evidence of LLM-specific scientific prior`

unless candidate-space reachability is controlled.

## 7. Files and reproducibility

Executable modules:

- `software/uqpu-prototype/uqpu/qos_d20_audit.py`
- `software/uqpu-prototype/uqpu/external_benchmark_provenance.py`

Tests:

- `software/uqpu-prototype/tests/test_qos_d20_audit.py`
- `software/uqpu-prototype/tests/test_external_benchmark_provenance.py`

Runner:

- `software/uqpu-prototype/examples/run_batch029_qos_and_provenance.py`

Canonical machine-readable artifact:

- `benchmarks/results/batch029-qos-d20-and-provenance.json`

## 8. Research status after Batch 029

### QOS

- D.16/D99 repeated-pair counterexample: **UQPU EXECUTABLY REPRODUCED**
- D.20/D185 zero-sample boundary: **UQPU EXECUTABLY REPRODUCED**
- D.183 sqrt(R)->R displayed arithmetic: **UQPU EXECUTABLY AUDITED**
- full repaired correlated-sample QOS chain: **NOT ESTABLISHED**
- QOS as a whole invalid: **NOT CLAIMED**
- machine-size claims reproduced by UQPU: **NOT YET**
- real-QPU QOS experiment: **NOT YET**

### EQN-002C

- official evaluator code commit pinned: **DONE**
- 239/240 discrepancy: **RECONCILED FOR PUBLIC-METADATA PURPOSES AS 240 RELEASED ENTRIES**
- official gated numerical bytes directly pinned by UQPU: **OPEN**
- semantics-free BANK baseline requirement: **ADDED**
- equal-budget external benchmark execution: **OPEN**
- ODE/PDE + nuisance-variable external stress: **OPEN**

## 9. Next falsifiable gates

**QOS-AUDIT-003:** inspect the next dependency with direct UQPU relevance, prioritizing D.19 shared-realization multi-bit composition or D.21 cumulative-counter-to-index conversion. Reproduce only statements that can be made executable without silently importing disputed assumptions.

**EQN-002C-2:** once authorized official data bytes are available, freeze exact revision/checksums and execute a small cross-domain subset under BANK/LLM/UNION equal-budget conditions before scaling to the released 240-task snapshot.

Until these gates are satisfied, no new-law, quantum-advantage, UQPU-replacement, >=100x, >=100,000,000x or Data-Center-to-One-Phone claim is promoted.
