# Literature watch — Stabilizer testing and learning under limited coherent quantum memory

**Date recorded:** 2026-10-27  
**Primary owner:** Lane H — literature watch and strategic publication  
**Cross-lane consumers:** Lane A (workload/compiler/runtime), Lane C (coherent memory and data movement), Lane F (resource accounting and evidence)  
**Shared IDs:** FND-002, INV-025/026/027, INV-029, INV-034/035  
**Evidence class:** OFFICIAL ARXIV PREPRINT / MATHEMATICAL RESOURCE BOUNDS  
**UQPU promotion:** literature relevance only; no UQPU benchmark, hardware advantage, or new physical law promoted

## Source and date

Srinivasan Arunachalam and Louis Schatzki, “Optimal Stabilizer Testing and Learning with Limited Quantum Memory,” arXiv:2607.02444, first submitted 2026-07-02.  
Official source: https://arxiv.org/abs/2607.02444

This source was newly identified for this project during the 2026-10-27 surveillance pass; the paper itself is not newly published today. It is an arXiv preprint, and this watch does not assert peer-reviewed publication or independent UQPU reproduction.

## Material result and its exact scope

The paper studies sequential access to copies of an unknown n-qubit stabilizer state when an algorithm can retain at most k qubits of coherent quantum memory between measurements. Within that formal model, it reports:

- stabilizer-state testing sample complexity Θ(n − k);
- non-adaptive stabilizer-state learning sample complexity Θ(n²/k); and
- an exponential lower bound for purity testing, including a setting where memory remains coherent throughout the protocol.

The important resource signal is a tradeoff between coherent memory and the number of state copies/samples required by particular testing or learning tasks. It is not a claim that a qubit stores a fixed amount of readable classical RAM, nor a demonstration of quantum advantage for UQPU workloads.

## Limitations and evidence boundary

- These are model-scoped mathematical sample-complexity results. Their assumptions, task definitions, access model, and proof must be checked before transferring a bound to another workload.
- Sample count is not equivalent to wall-clock latency, total energy, billable QPU usage, physical memory capacity, or cost per accepted task.
- The result does not establish that the bound is tight for arbitrary quantum algorithms, noisy devices, provider interfaces, QAOA/QUBO, or UQPU's general workload family.
- No source-code reproduction, proof-assistant check, device measurement, or independent theorem audit was performed in this cycle.
- Hilbert-space dimension and coherent register width must never be re-labelled as readable classical storage.

## Exact UQPU relevance

- **Lane A:** separate testing from learning in workload semantics; an accepted answer must specify the target decision/reconstruction quality, not merely successful circuit execution.
- **Lane C / FND-002:** extend resource records to keep coherent-memory width k, state size n, copies/samples, measurements, reset/repreparation, classical working memory, communication, output bits, and reconstruction work as separate quantities. Do not fold the theorem into the existing output-information bound; they are different lower-bound families.
- **Lane F:** cost and energy comparison remains blocked until actual execution/energy/accounting data exist. A sample-complexity asymptotic is not an economic result.
- **INV-029:** any eventual phone-class comparison must include coherent-memory lifetime/control, measurement, classical support, networking, and reconstruction inside the physical boundary.
- **INV-034/035:** treat the theorem as an incumbent-model constraint to reproduce and scope, not as a newly discovered physical law. Alternative equations cannot be promoted without explicit assumptions, counterexamples, held-out predictions, and independent proof/experiment.

No new claim is made for INV-030 Pangola carbon, INV-031 accepted bio-oil, INV-032 net fusion electricity, or INV-033 lower financing principal/interest/WACC.

## Falsifiable follow-up

1. Pin the source version and formal task/access definitions; independently reconstruct the proof or a theorem-level derivation.
2. Build a small-n synthetic diagnostic over several k/n settings, recording copies, coherent-memory width, measurements, classical memory, output quality and failures. Label it MODEL_ONLY; it is a sanity check, not a proof of the asymptotic theorem.
3. If a suitable implementation is available, preregister identical-output testing and learning baselines with classical controls, fixed shot/sample budgets, and complete memory/I/O/latency/cost fields.
4. Reject transfer of the result to another workload unless its assumptions and reduction are written explicitly and independently checked.

**Next gate:** a source-pinned theorem audit plus an explicit Lane A/C workload record that separates coherent memory, samples, readable output and accepted-task quality.