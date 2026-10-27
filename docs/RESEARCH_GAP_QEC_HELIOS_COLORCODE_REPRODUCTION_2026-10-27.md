# Research gap RG-QEC-HELIOS-COLORCODE-REPRODUCTION-001 — target-specific logical error suppression

**Opened:** 2026-10-27  
**Status:** OPEN / LITERATURE_ONLY / INDEPENDENT_REPRODUCTION_NOT_RUN  
**Primary owner:** Lane B — cloud/QPU integration and target evidence  
**Co-owners:** Lane A (compiler/runtime), Lane D/G (device/factory co-design), Lane F (benchmark/economics), Lane H (publication)  
**Related:** INV-001/002/004/007/010/013/015/016/019/022/024, FND-003, INV-029/034/035  
**Literature watch:** docs/literature_watch/2026-10-27-quantinuum-helios-color-code-below-threshold.md

## Objective

Independently validate the published Quantinuum Helios color-code logical-memory and logical-Clifford results, then determine whether any target-specific capability transfers into a workload that meets an identical useful-output contract and full-stack cost boundary.

## Evidence available

Lavasani et al., “Quantum error correction well below the color code threshold,” arXiv:2610.24077 (submitted 2026-10-16; updated 2026-10-20), report triangular color-code experiments at distances 3, 5 and 7 on Helios. The preprint reports logical memory error rates down to 5×10^-6 per correction round, suppression factor 12 with uncertainty -2/+3 for successive distance increases, and logical two-qubit Clifford error around 7×10^-5 at distance 5 with suppression factor 9 and uncertainty -3/+8. It compares algorithmic, CNN and Transformer decoders.

Quantinuum's official 2026-10-19 announcement provides a company summary. These are external experimental claims; UQPU has not reproduced the data or executed on this target.

## Blocking unknowns

- Source-data/code availability and reproducibility of the reported uncertainty intervals.
- Exact distinction among logical memory, logical gate, circuit-level and application-level error.
- Whether the studied QEC/decoder configuration is accessible through a supported cloud interface, and at what price and job constraints.
- Total physical-qubit, measurement, decoder, host-compute, energy and data-movement cost for any candidate workload.
- Whether performance remains useful after matching the same accepted output and competitive CPU/GPU baselines.

## Unlock criteria

1. Freeze the paper version, data/code hashes, environment and decoder parameters.
2. Recompute the published logical error estimates and suppression factors from the available primary data; if source artifacts are unavailable, record the precise blocker rather than simulating a reproduction.
3. Keep memory error per round and logical-gate error separate, with confidence intervals and tested code distances.
4. Confirm provider access, SDK/lowering path, pricing and job limits before planning any live run; paid execution requires explicit consent and a bounded budget.
5. Require target-aware compilation/simulation first, then an authorized hardware run only if justified.
6. Evaluate application-level accepted-output quality, latency, throughput, retries, decoder/control overhead, host computation, energy where measurable and total cost per accepted task.

## Falsification / stop rules

Reject the reproduction if source data do not support the stated rates within declared uncertainty or if the error-suppression trend fails under the stated method. Do not promote a memory-only result to logical universal computation or quantum advantage. Stop an economic claim if the QPU path fails the same useful-output threshold or omits physical-qubit, decoder, I/O, host, energy or billing costs.

## Non-claims

No live QPU job was submitted. No universal fault-tolerance, quantum advantage, GPU/CPU/NPU replacement, memory/storage replacement, Data-Center-to-Phone progress, new physical law, material substitution, bio-oil/fusion result or financing-rate effect is established.
