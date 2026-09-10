# Batch 028 — QOS D.16 Executable Counterexample Reproduction and External-Benchmark Provenance Gate

**Date:** 2026-09-10  
**Programs:** Issue #1 / QOS adversarial review / EQN-002C provenance  
**Evidence:** THEORY_EXECUTABLE_REPRODUCTION + EXTERNAL_PROVENANCE_AUDIT  
**REAL_QPU:** No  
**Quantum advantage:** Not demonstrated  
**UQPU replacement advantage:** Not demonstrated

## Why this batch

Batch 027 promoted Quantum Oracle Sketching (QOS) to `HIGH_VALUE_ADVERSARIAL_REVIEW_REQUIRED` rather than treating an external preprint as UQPU evidence. Issue #1 then required the source theorem, implementation and public criticism to be checked side by side.

This batch does two things:

1. independently reproduces, in UQPU executable code, the arithmetic/channel certificate for the published repeated-pair witness against the **sufficient threshold printed in Theorem D.16 / Eq. (D99) of `arXiv:2604.07639v1`**;
2. freezes the current LLM-SRBench code provenance and records a 239-versus-240 dataset metadata discrepancy before any external equation-discovery result is promoted.

## Direct source check — QOS v1

The current arXiv record checked on 2026-09-10 still lists only:

`arXiv:2604.07639v1`, submitted 2026-04-08.

Source:
- https://arxiv.org/abs/2604.07639

The source PDF, page 49, prints Theorem D.16 with the sufficient sample condition

`M >= [(t^2 p_max + 2 t sqrt(2 p_max |X|)) / epsilon] R_D`.

The theorem states that this many correlated samples suffice for the channel-error target in Eq. (D100).

The public source-code repository has continued to evolve after the arXiv submission. The latest source-repository commit observed in this batch is:

`haimengzhao/quantum-oracle-sketching@a3fe8d6fe777750749f5e90131180e016088bdaf`  
dated 2026-09-06.

Code evolution is useful for reproducibility but does not itself revise the theorem printed in the still-current arXiv v1.

## Executable repeated-pair witness

The public audit by Carmelo Vellón Gascón gives a finite repeated-pair witness. This batch does not merely cite its conclusion; it implements the relevant source threshold and the averaged-channel coherence in:

`software/uqpu-prototype/uqpu/qos_adversarial_audit.py`

with tests in:

`software/uqpu-prototype/tests/test_qos_adversarial_audit.py`.

The witness uses

- `t = 2*pi`;
- `p_max = 1/2`;
- `|X| = 2`;
- `R_D = 1`;
- `epsilon = 1/20`;
- `M = 752` samples;
- `q = 376` independent fair parent bits, each repeated twice.

### Printed threshold

Substitution into Eq. (D99) gives

`20 * (2*pi^2 + 4*sqrt(2)*pi)`

which evaluates to

`750.2148110962436`.

Therefore `M = 752` satisfies the printed sufficient threshold. It is also the smallest **even** integer above the threshold, matching the repeated-pair construction.

### Averaged channel

For `q=M/2` fair parent bits, each repeated twice, the target differs only by a global phase and the averaged relative off-diagonal coherence is

`c = cos(t/q)^q`.

At the witness parameters:

`c = cos(pi/188)^376 = 0.9488539991849398`.

For this two-dimensional dephasing channel the unnormalized diamond distance from the target identity channel is

`1 - c = 0.051146000815060155`.

This is strictly larger than

`epsilon = 0.05`.

Therefore the same finite witness simultaneously satisfies the sample threshold printed in Eq. (D99) while missing the claimed error target.

Canonical machine-readable artifact:

`benchmarks/results/batch028-qos-d16-counterexample.json`

Reproduction runner:

`software/uqpu-prototype/examples/run_qos_d16_adversarial_audit.py`

## Scope of the result

The correct project classification is:

`SOURCE_V1_SCOPED_COUNTEREXAMPLE_REPRODUCED`

This batch supports a **version- and theorem-scoped** conclusion about the sufficient threshold printed in Theorem D.16 / Eq. (D99) of arXiv v1.

It does **not** establish that:

- Quantum Oracle Sketching as a whole is impossible;
- the IID core is invalid;
- every theorem or numerical experiment in the source paper fails;
- the reported machine-size reductions are all false;
- QOS has or does not have end-to-end practical quantum advantage;
- UQPU can replace GPU/NPU/RAM/VRAM/storage;
- UQPU achieves >=100x or >=100,000,000x advantage.

The public audit used as a cross-check is:

- repository: `gatephys/quantum-oracle-sketching`;
- Version-2 DOI: `10.5281/zenodo.21704142`;
- repository commit observed: `c00a0b5bf2bcfde6a150fd9be6553858e2676ace`.

The UQPU executable reproduction is intentionally small: it verifies the finite arithmetic/channel certificate, not every proof dependency in the audit.

## LLM-SRBench provenance gate

Issue #1 also requires an external symbolic-regression benchmark rather than continued tuning on UQPU-owned toy fixtures.

The official LLM-SRBench code is now pinned at:

`deep-symbolic-mathematics/llm-srbench@6fdbe409b75ea749c0a93c69b6861637d804dec4`

with tree:

`ef351c4c02bc68fdff1f90a31ea02ec5032d090a`.

The official loader points to the Hugging Face dataset:

`nnheui/llm-srbench`

and reads the large sample arrays from `lsr_bench_data.hdf5`.

However, the official dataset requires acceptance of gated-access terms. This interaction therefore did not bypass that gate and did not claim to download the official HDF5.

A second provenance problem was observed in the public metadata:

| split | current metadata count |
|---|---:|
| bio population growth | 24 |
| chemistry reaction | 36 |
| materials science | 25 |
| physics oscillator | 44 |
| transformed Feynman | 111 |
| **total** | **240** |

The paper and dataset prose state **239** total problems, with 128 LSR-Synth tasks and a domain breakdown that reports 43 physics problems. The currently exposed metadata therefore differs by one physics item.

This may have a benign versioning/data explanation, but until it is resolved UQPU must not silently treat “LLM-SRBench 239” and the currently exposed 240-row metadata as identical frozen benchmarks.

Canonical provenance artifact:

`benchmarks/external/llm-srbench-provenance-2026-09-10.json`

Status:

`PROVENANCE_PINNED_DATA_NOT_IMPORTED`

## Research consequence

The adversarial-review rule is doing useful work. A high-value quantum result should be integrated into UQPU only after:

`source theorem -> independent challenge -> project reproduction -> repaired/new source version if any -> implementation reproduction -> full-stack UQPU contract`.

For scientific equation discovery the analogous chain is:

`external benchmark version -> exact dataset revision/checksum -> frozen task IDs -> equal search budget -> structural/OOD metrics -> independent replication`.

## Next falsifiable gates

**QOS-AUDIT-002:** move from the D.16 finite certificate to the next highest-impact dependency that affects a UQPU use case, while keeping each conclusion theorem-scoped. If the QOS authors publish a new arXiv version, diff the revised theorem before carrying any v1 finding forward.

**EQN-002C:** after authorized access to the official gated LLM-SRBench dataset, pin the exact dataset revision and HDF5 checksum, resolve the 239/240 discrepancy, freeze a cross-domain subset, and compare at least two discovery methods under the same evaluation budget.

Until those gates are satisfied, no new-law, quantum-advantage, UQPU-replacement, 100x, 100,000,000x or Data-Center-to-One-Phone claim is promoted.
