# Literature watch — quEStab extended-tableau multi-GPU simulation

**Date checked:** 2026-10-29  
**Primary owner:** Lane H — literature surveillance/publication  
**Interfaces:** A (workloads/simulators), B (backend portability), C (memory/data movement), F (benchmark economics), D/G (device/manufacturing co-design)  
**Evidence class:** PEER-REVIEWED COMPUTATIONAL PAPER / LITERATURE_ONLY FOR UQPU  
**Related:** INV-025/026/027, INV-029, INV-034/035, RG-QAOA-PARITY-001, RG-A-QUASARQ-STABILIZER-REPRO-001

## Source and publication status

- Paper: “quEStab: Towards Scalable Quantum Circuit Simulation on Multi-GPU using an Extended Stabilizer Formalism.”
- Publisher: ACM, Proceedings of the 40th ACM International Conference on Supercomputing (ICS '26), published 2026-07-05.
- DOI and publisher record: https://doi.org/10.1145/3797905.3816723

This paper was newly identified for the UQPU literature ledger during the 2026-10-29 surveillance pass. It complements, rather than supersedes, the already-recorded QuaSARQ Clifford/stabilizer simulator result.

## Genuine technical contribution reported

The paper describes an extended stabilizer-tableau representation that branches into weighted Pauli rows for non-Clifford operations, merges rows where possible, and distributes Pauli groups across multiple GPUs. It reports 78.1% overall QASMBench circuit coverage (100/128), execution up to 30,000 qubits on selected structured circuits, and very large peak-memory reductions against state-vector simulation in selected cases.

The important methodological distinction is that resource use is driven by the number of active tableau rows and the ability to merge them—not by qubit count alone. The authors discuss rapid row growth as a practical limit for intricate non-Clifford circuits. This makes the representation a candidate for workload-specific testing, not a general guarantee of efficient arbitrary-circuit simulation.

## Source-audit issue to resolve

The publisher-indexed text also reports 69/97 circuits (71.1%) in a separate passage before later reporting 100/128 (78.1%). These may refer to different experiment subsets or stages; the inspected text does not clearly reconcile that denominator transition. Do not label this a proven contradiction, and do not silently select the more favorable denominator. Reproduction must map each number to its exact benchmark subset, transpilation stage, timeout and success definition.

## Exact UQPU relevance

- **Lane A / parity-QAOA:** a non-Clifford-capable simulator may be a candidate for small, frozen parity-QAOA circuits only after confirming exact semantics for parameterized rotations, measurement, objective reconstruction and accepted-output predicates. It does not replace exact objective/argmax certificates or matched baselines.
- **Lane B:** simulator execution is distinct from provider lowering and physical-QPU execution. Provider-specific prices or probabilities must not be mixed.
- **Lane C:** report peak host/device memory, active-row count, transfers and reconstruction. A compact tableau or mathematical state representation is not readable classical RAM/storage equivalence.
- **Lanes D/G:** the paper informs GPU-memory and multi-GPU co-design questions, but supplies no quantum-device fabrication, packaging, yield or manufacturing evidence.
- **Lane F:** evaluate end-to-end cost per accepted useful task, including transpilation/setup, host work, memory pressure, transfers, failures/retries and measured energy where available.
- **INV-029:** simulator throughput is a stepping stone only; it does not demonstrate physical compression of a data center into a phone.
- **INV-034/035:** representation and scaling hypotheses remain subject to explicit assumptions, counterexamples, held-out circuits and independent reproduction. No new physical law is proposed.

## Limitations and nonclaims

This is a third-party computational result, not a UQPU reproduction. Coverage and memory ratios are benchmark- and baseline-specific. Exact simulation can still become infeasible when active-row branching grows; high qubit count alone is not a general performance metric. No real-QPU advantage, generic QAOA advantage, 100x/100,000,000x economics, universal memory replacement, commercial fuel, net fusion electricity, lower WACC, material substitution or Data-Center-to-One-Phone closure follows.

## Falsifiable follow-up

1. Pin the exact upstream source commit, build recipe, dependencies, compiler/CUDA versions, GPU model and benchmark input hashes before timing.
2. Reconcile the 69/97 and 100/128 counts to named subsets and success criteria.
3. Run a frozen, tractable suite spanning Clifford-only, T-gate and parameterized-rotation circuits; include small parity-QAOA instances at multiple depths.
4. Compare outputs with independent exact references within declared tolerance; check decoded objective values and argmax-set equivalence where required.
5. Measure active tableau rows, peak host/device memory, transfers, host work, setup, latency, throughput, failures/retries and energy with an explicit boundary. Unknown energy components remain UNKNOWN, not zero.
6. Hold out at least one circuit family and one non-Clifford-density regime. Record failures and resource exhaustion as first-class outcomes.
7. Do not submit a paid QPU job as part of this simulator reproduction.
