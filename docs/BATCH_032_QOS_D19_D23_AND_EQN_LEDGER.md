# Batch 032 — QOS D.19 -> D.23 Dependency Audit and EQN Resource Ledger

**Date:** 2026-09-10  
**Programs:** Issue #1 / QOS-AUDIT-004 / EQN-002C-3 / Lane C  
**Evidence:** THEORY_EXECUTABLE_INTERFACE_WITNESS + THEORY_DEPENDENCY_AUDIT + EXECUTABLE_BENCHMARK_PROTOCOL  
**REAL_QPU:** No  
**Quantum advantage demonstrated by UQPU:** No  
**UQPU GPU/NPU/DRAM/HBM replacement demonstrated:** No

## Executive result

This batch advances two open gates without promoting external claims beyond evidence.

1. The D.19 sparse-element-oracle proof in `arXiv:2604.07639v1` obtains a per-bit marginal channel guarantee in Eq. D148 and then assembles all `b` bit channels into the word/XOR oracle in Eq. D150 using the same sampled realization. A new executable UQPU shared-realization witness shows that even making the *sum* of marginal average errors equal the requested final epsilon does not, by itself, control the joint channel when the hidden realization is shared.
2. Lemma D.23 explicitly instantiates its sparse oracles through D.19 and D.21. Because the UQPU evidence ledger now contains unresolved D.19 shared-realization composition, the reproduced D.21 composition-budget gap, and a source-v1 D.16 counterexample used upstream by D.19/D.20, D.23 is classified `DEPENDENCY_NOT_CLOSED`, not `THEOREM_REFUTED`.
3. The QOS paper's machine-size plots count logical qubits for quantum and floating-point memory units for classical systems. Under Batch 031 this is not enough to establish physical DRAM/HBM/SRAM replacement or cost advantage. A machine-size-to-memory translation gate is now executable.
4. EQN-002C now includes a fourth method arm, `LLM_GUIDED_SEARCH_SPACE`, motivated by InsightSR (`arXiv:2608.25291v1`). This captures methods where the LLM modifies the grammar/features/search space rather than directly outputting equations. The resource ledger is executable and keeps candidate-count parity separate from compute/cost parity.

## 1. Frozen QOS source

Primary source:

- H. Zhao et al., *Exponential quantum advantage in processing massive classical data*, `arXiv:2604.07639v1`, submitted 2026-04-08.
- Source PDF checked on 2026-09-10: https://arxiv.org/pdf/2604.07639

The arXiv record checked for this batch still exposes v1. All theorem labels below are version-scoped.

## 2. D.19 source observation

D.19 represents each matrix element by a `b`-bit string. For every sampled nonzero matrix entry, the construction applies a phase operation for every bit position `a in [b]`. The proof then invokes D.16 to obtain the displayed per-bit guarantee in D148 and converts the bit phase oracles into the XOR/word oracle in D150.

The important interface fact is that the bit channels are built from the same sample stream. Therefore a proof of the final joint channel requires more than separate marginal average-channel bounds unless an additional factorization, fresh-sample, direct-joint-concentration, or conditional repeated-use theorem applies with all of its hypotheses established.

This batch does **not** claim that the specific D.19 matrix stream has been counterexampled. It tests the logical inference from marginal shared-realization guarantees to a joint channel.

## 3. Executable shared-realization witness

Let a hidden sign `S` be uniform on `{-1,+1}` and define a one-slot unitary

`U_S = exp(i S theta Z / 2)`.

The sign-averaged one-slot channel has unnormalized diamond error from identity

`e_1 = 1 - cos(theta)`.

If the same hidden sign is reused across `b` slots, the joint averaged channel has error

`e_b = 1 - cos(b theta)`.

For the canonical Batch-032 witness:

- `b = 8`
- target `epsilon = 0.001`
- choose `theta = acos(1 - epsilon/b) = 0.01581155300743842`

This makes the marginal-average error sum exactly the target to floating precision:

`b * e_1 = 0.001000000000000334`.

But the shared-realization joint error is

`e_b = 0.00798950524871378`,

which is approximately

`7.9895052487 * epsilon`.

Therefore:

`sum of marginal average errors <= epsilon`

is **not sufficient** to imply

`shared-realization joint average-channel error <= epsilon`.

This is stronger than merely noting a missing factor `b`: tightening each marginal-average target to `epsilon/b` still does not repair a shared-realization composition proof by itself.

A correct route can use, for example, a direct joint-channel analysis, fresh/independent realizations with a justified factorization, or conditional full-channel errors compatible with a repeated-use hybrid such as the source's D.17 framework.

**Classification:** `THEORY_EXECUTABLE_INTERFACE_WITNESS`.

**Non-claim:** this abstract witness is not asserted to be the exact D.19 source process and does not refute Lemma D.19 as a theorem.

## 4. D.23 dependency consequence

The source proof of Lemma D.23 explicitly says it instantiates the sparse oracles of the standard sparse block-encoding construction using D.19 and D.21. It then applies QSVT and again replaces repeated sparse-oracle calls by sample-built channel approximations.

UQPU's current source-v1 dependency ledger is therefore:

```text
D.16 -> D.19 -----------+
                         |
D.16 -> D.20 -> D.21 ---+-> D.23
                         |
standard D.22 -----------+
```

Current UQPU evidence state:

- `D.16`: finite source-v1 counterexample reproduced in Batch 028.
- `D.19`: marginal-to-joint shared-realization interface is not closed by the displayed argument; Batch 032 adds an abstract executable witness showing why the inference needs more.
- `D.20`: zero-sample boundary and displayed `sqrt(R) -> R` arithmetic issues reproduced in Batch 029.
- `D.21`: displayed final composition budget shortfall reproduced in Batch 030; this did not refute the theorem.
- `D.22`: imported standard sparse-oracle-to-block-encoding module; not independently reaudited in this batch.
- `D.23`: downstream dependency chain is not closed.

Accordingly the UQPU status is:

`SOURCE_V1_D23_DEPENDENCY_NOT_CLOSED`

and **not** `D23_THEOREM_REFUTED`.

The sample-complexity expression printed for D.23 must not yet be used by UQPU as verified evidence of a quantum, NPU, GPU, RAM/DRAM or HBM advantage.

## 5. Independent audit cross-check

An independent version-specific audit by Carmelo Vellon Gascon, *Exact Counterexamples and Interface Gaps in Quantum Oracle Sketching* / Technical Supplement v2, separately classifies D.19 as a shared-realization proof/interface gap and D.23 as a proof/interface gap. Its technical supplement also records a small-error shared-realization rotation witness and additional QSVT contract questions.

Public research mirror:

https://github.com/gatephys/quantum-oracle-sketching

Version-2 DOI reported by that project:

https://doi.org/10.5281/zenodo.21704142

UQPU uses this as an external adversarial cross-check, not as a substitute for its own executable evidence. The Batch-032 numeric witness is generated by UQPU code. Additional D.23 QSVT margin/block-to-channel concerns from the external audit remain a next-gate item until independently verified by UQPU.

## 6. DRAM/HBM memory translation gate

The source paper defines machine size in its numerical plots using fundamental memory units: logical qubits for quantum machines and floating-point numbers for classical machines.

That metric can be scientifically useful for a space-complexity comparison, but it is not a physical memory-system equivalence contract.

Following Batch 031, UQPU must not translate a logical-qubit-versus-float reduction directly into `DRAM replacement`, `HBM replacement`, `memory-energy advantage`, or `memory-cost advantage` without recording the memory roles and physical implementation costs.

The new executable gate requires fields covering:

- system DRAM capacity, bandwidth and latency;
- DRAM refresh/idle energy;
- accelerator HBM/GDDR/VRAM footprint;
- SRAM/cache;
- host/accelerator data movement and energy;
- logical and estimated physical qubits;
- QEC/control memory;
- wall time;
- memory cost per accepted task;
- total cost per accepted task.

Therefore the correct relation is:

`machine-size reduction != DRAM/HBM replacement != cost reduction`.

Each arrow requires its own evidence.

## 7. EQN-002C-3 — resource-ledger implementation

Batch 030 established:

`equal candidate budget != equal compute cost`.

Batch 032 makes this executable through `uqpu.eqn_resource_ledger`.

Frozen method arms are now:

- `BANK`
- `LLM_DIRECT`
- `UNION`
- `LLM_GUIDED_SEARCH_SPACE`

Every method record must include candidate evaluations, optimizer evaluations, LLM calls, prompt/completion tokens, wall time, peak memory, hardware description and monetary cost when measured.

A comparison is marked resource-ready only when all ledgers are complete, method arms are unique, and candidate budgets are equal. This does **not** mean the methods used equal compute; it means the resource differences are exposed rather than hidden.

## 8. New literature delta — InsightSR

New relevant preprint:

- Y. Ling, W. Cun, Z. Chen, *InsightSR: Refining Symbolic Regression Search Spaces via Parallel Semantic and Structural LLM Guidance*, `arXiv:2608.25291v1`, submitted 2026-08-26.
- https://arxiv.org/abs/2608.25291

The abstract reports 95% exact recovery on the Feynman benchmark and 80.18% accuracy on LLM-SRBench LSR-Transform. The methodological point relevant to UQPU is that the LLM guides PySR through semantic seeds and structural feature transformations rather than functioning only as a direct formula generator.

**UQPU status:** `LITERATURE_ONLY_NOT_EXECUTED_BY_UQPU`.

The reported numbers are not UQPU results. Public code was not verified by this batch. This paper motivates the fourth comparator arm because a `BANK vs LLM_DIRECT vs UNION` protocol alone would fail to represent search-space-guidance methods fairly.

## 9. Reproducibility artifacts

Executable QOS audit:

`software/uqpu-prototype/uqpu/qos_d19_d23_audit.py`

Tests:

`software/uqpu-prototype/tests/test_qos_d19_d23_audit.py`

Runner:

`software/uqpu-prototype/examples/run_qos_d19_d23_audit.py`

EQN resource ledger:

`software/uqpu-prototype/uqpu/eqn_resource_ledger.py`

Tests:

`software/uqpu-prototype/tests/test_eqn_resource_ledger.py`

Runner:

`software/uqpu-prototype/examples/run_eqn_resource_ledger.py`

Canonical result:

`benchmarks/results/batch032-qos-d19-d23-and-eqn-ledger.json`

InsightSR provenance:

`benchmarks/external/insightsr-provenance-2026-09-10.json`

## 10. Next gates

### QOS-AUDIT-005

Independently audit the D.23 QSVT amplification contract and the distinction between projected-block error and full-channel error. A useful first falsifier is the endpoint/margin case where `||A|| = 1`; classify any result separately as imported-theorem contract, local repair, or theorem counterexample.

### EQN-002C-4

Run a frozen four-arm protocol on open/internal fixtures before official gated LLM-SRBench bytes are available. Preserve candidate reachability, exact structural recovery, holdout/extrapolation error, false discoveries and the full resource ledger. Do not change evaluation criteria after seeing results.

### Lane C

Attach the Batch-031 memory-role fields to the first QOS/UQPU workload translation. Keep `R_capacity`, `R_bandwidth`, `R_latency`, `R_energy`, `R_cost` and `R_materialized_bytes` separate until a workload contract justifies aggregation.

## Non-claims

Batch 032 does not demonstrate a real-QPU result, quantum advantage, universal QOS invalidity, D.19 or D.23 theorem refutation, UQPU GPU/NPU/RAM/DRAM/HBM replacement, >=100x advantage, >=100,000,000x advantage, or a new law of physics.
