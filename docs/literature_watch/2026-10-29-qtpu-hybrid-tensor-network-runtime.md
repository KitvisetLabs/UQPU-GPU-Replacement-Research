# Literature watch — qTPU hybrid tensor-network compiler/runtime

**Recorded:** 2026-10-29  
**Primary source:** Nathaniel Tornow, Emmanouil Giortamis, Dennis Sprokholt, Christian Mendl, and Pramod Bhatotia, “qTPU: Hybrid Tensor Networks for Quantum-Classical Acceleration,” USENIX OSDI 2026, pp. 2367–2388.  
**Official proceedings page:** https://www.usenix.org/conference/osdi26/presentation/tornow  
**Open artifact repository:** https://github.com/TUM-DSE/qtpu  
**Inspected artifact revision:** `TUM-DSE/qtpu@3f68fc96e5de9c336c96e82d4af0a2f7a96b5a22` (latest visible commit returned by the repository connector); README blob SHA `4b2e2cb6d0a9910962fdf6b98e283c2d651a30e3`.  
**Artifact licence:** Apache-2.0 at the inspected repository root.  
**Evidence class:** PEER-REVIEWED SYSTEMS PAPER + PUBLIC ARTIFACT DOCUMENTATION; AUTHOR-REPORTED BENCHMARKS; NO UQPU REPRODUCTION.

## Genuine method delta

qTPU represents hybrid quantum/classical execution as a hybrid tensor network (hTN), then jointly optimizes a compiler trade-off between classical contraction overhead and quantum execution error. Its runtime supports heterogeneous QPU/classical-accelerator execution. This is a concrete systems-level alternative to treating circuit partitioning, quantum execution and classical reconstruction as separately optimized stages.

The official OSDI page reports large gains on the authors' workloads, including reduced classical overhead, faster compilation and end-to-end speedups. The artifact README further reports comparisons for error-mitigation compilation/code size. These are **source-attributed results**, not independent measurements by UQPU. The repository documents pre-collected logs for plot reproduction; re-running the IBM Marrakesh hardware arm requires IBM credentials. This cycle inspected the official proceedings page, artifact README, reproduction guide, dependency manifest and licence, but did not execute the artifact, inspect every log row, or reproduce any figure.

## Exact UQPU relevance

- **Lane A — compiler/runtime:** evaluate hTN as an optional lowering/partitioning strategy behind the provider-neutral workload contract, not as a replacement for the semantic IR by declaration.
- **Lane B — providers:** keep hardware results tied to the exact IBM target and run. A single-provider hardware result cannot establish provider-neutral portability or be combined with another provider's prices.
- **Lane C — state and movement:** include tensor-network bond/cut metadata, classical intermediate sizes, contraction memory, host-device transfers and reconstruction; never equate tensor dimension with readable persistent storage.
- **Lane D/G — device and factory co-design:** use measured gate/connectivity/noise and control constraints only after reproducing a target-specific result. No fabrication or device claim follows from the paper.
- **Lane E — energy/infrastructure:** capture host and QPU energy when measurable; the source's speed/error metrics alone do not establish lower lifecycle energy or fusion economics.
- **Lane F — evidence/economics:** compare accepted useful output at matched quality, workload, target, budget and failure policy; count compilation, classical contraction, shots, retries, postprocessing, transfer, wall time and total cost per accepted task.
- **Lane H / INV-034–035:** preserve the source as a reproducible external systems result, separate its formal/algorithmic assumptions from physical claims, and retain a falsifiable follow-up rather than promoting vendor or author metrics.

## Limitations and unresolved questions

1. The reported gains are workload- and baseline-specific; they do not establish universal quantum advantage, a 100×/100,000,000× cost reduction, or a Data-Center-to-One-Phone path.
2. The published/pre-collected result tables are not an independent reproduction; source commit, logs, scripts, dependency versions and raw hardware provenance must be pinned together before any numerical transfer.
3. Quantum error, classical contraction cost and end-to-end task success are different metrics. A compiler Pareto improvement may still lose after shots, reconstruction, host compute, memory, transfer, billable usage and failures are included.
4. The IBM hardware arm needs credentials and must not be run as part of this cycle without separate owner consent and a bounded budget.
5. UQPU did not copy or vendor qTPU code; no code-reuse claim is made.

## Proposed falsifiable follow-up

Create a small provider-neutral benchmark manifest with identical accepted outputs and an independently checked reference/bound. Compare (a) current UQPU lowering, (b) a classical tensor-network/contraction baseline, and (c) an hTN-inspired optional partitioning arm where licence/interface permits. First use fixed synthetic circuits and dry-run/simulation; hold out whole circuit families and target/noise regimes. Freeze quality tolerance, seeds, cut/partition budget, contraction optimizer, shot ceiling and timeout before runs. Retain failed runs. Report accepted-task rate, quality, compilation time, circuit/subcircuit count, shots, host compute, peak memory, transfers, retries, reconstruction, target-specific QPU usage, energy where measurable and total cost per accepted useful task.

**Promotion rule:** literature and source-code inspection are not UQPU execution evidence. No paid hardware job without credentials, explicit owner consent and a bounded budget; no advantage claim unless the same-target, same-output, full-resource comparison passes.
