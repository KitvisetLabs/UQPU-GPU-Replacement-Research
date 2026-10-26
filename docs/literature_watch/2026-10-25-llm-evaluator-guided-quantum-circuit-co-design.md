# Literature watch — 2026-10-25: evaluator-guided quantum-circuit co-design

**Accessed:** 2026-10-25  
**Primary owner:** Lane A — quantum programming, workloads, compiler and runtime  
**Integration owner:** Lane F — evidence, benchmarking and lifecycle economics  
**Publication integration:** Lane H  
**Feeds:** A–H; INV-025/026/027; INV-029–035; FND-006; EQN-001–006  
**Evidence class:** ARXIV_PREPRINT / LITERATURE_ONLY  
**UQPU project evidence promoted:** none

## Source and date

Andi Gu, Alek H. Kemeny, Susanne F. Yelin and Mikhail D. Lukin, “Discovering state-of-the-art quantum circuits with large language models,” arXiv:2610.22367v1, submitted 2026-10-15. Official source: https://arxiv.org/abs/2610.22367. The paper is a preprint; this watch does not assert peer-reviewed acceptance or independent UQPU reproduction.

## Genuine novelty

The work couples LLM-generated candidate architectures with a separate programmatic evaluator rather than accepting the generator's own correctness or resource claims. The authors report lower Toffoli counts and peak-qubit counts in seven of eight studied compilation tasks, and a different reversible architecture for prime-field modular inversion in the eighth. The search starts from high-level algorithm families, then iteratively revises implementations using correctness and resource feedback.

Three design ideas are particularly relevant:
1. **Conditional routing:** route branch-dependent data through a shared expensive arithmetic kernel when the required transformations admit a suitable representation, instead of controlling duplicate arithmetic blocks.
2. **State-derived uncomputation:** exploit invariants of reachable intermediate states to recover branch decisions, potentially reducing explicit history/ancilla storage.
3. **Bounded-failure resource tradeoffs:** spend an explicit, workload-distribution-specific failure budget to reduce worst-case resource allocation only when the supported input distribution and acceptance contract justify it.

These are algorithm and circuit co-design ideas, not a claim that an LLM has discovered a new physical law.

## Evidence class and limitations

The source is an author-reported preprint result, not a UQPU reproduction. Its evaluator is well suited to the studied reversible implementations of classical functions because the specified gate operations permit basis-state tracking. That scope must not be generalized to arbitrary quantum circuits or to equivalence checks that ignore relative phase.

The reported logical metrics include Toffoli count and peak qubits, with a Toffoli-times-qubits product used as a resource proxy. That proxy is not total cost. It does not by itself account for target-native gate decomposition, T-depth and scheduling, routing, error-correction overhead, calibration, control hardware, ancilla lifetime, host computation, data movement, retries, energy, output reconstruction or cost per accepted useful task. Any allowed failure probability depends on the exact workload distribution and cannot silently weaken worst-case guarantees.

UQPU did not run the paper's generator, reproduce its circuits, verify its full proofs, lower candidates to a provider SDK or execute a QPU job.

## Exact UQPU relevance

- **Lane A / INV-025–027:** a candidate-search pattern for selected reversible subroutines. It does not establish 100,000,000-GPU replacement or universal subsystem replacement.
- **Lane B:** only after semantic and verification gates pass should a candidate be lowered through provider-neutral adapters; no provider execution or pricing result is implied.
- **Lane C:** peak logical qubits and temporary-state lifetime are useful resource dimensions, but neither is readable classical RAM/storage capacity.
- **Lanes D/G:** native-gate mapping, physical qubit/control requirements, packaging, yield and manufacturing cost remain downstream and must be co-designed rather than inferred from logical counts.
- **Lanes E/F:** material, energy, fusion and finance consequences require a causal workload connection and full lifecycle accounting. No BIO-001, FUS-001 or FIN-001 evidence is added by this paper.
- **Lane H:** preserve the strategic path from computation to industrial and financing consequences, without converting a logical-resource reduction into a commercial claim.
- **INV-034/035:** the paper supports an evaluator-first research method. It does not challenge established physics and is not a new physical equation.

## Proposed falsifiable follow-up — RVC-001

Choose one small, explicitly specified reversible primitive relevant to the current UQPU compiler/workload stack. Freeze the function specification and SHA-256, input/output widths, baseline implementation, supported input domain, allowed failure probability, and target scope before candidate generation.

For every candidate:
1. Record generator identity, candidate hash, evaluator identity/hash, and verification artifact hash.
2. Check the complete input/output basis domain where tractable, or provide a proof artifact with explicit assumptions. Test relative-phase semantics and ancilla cleanup separately; a basis-state output match alone is not sufficient if phase behavior is unchecked.
3. Retain failed and incomparable candidates. Reject missing provenance, inconsistent semantics, incomplete exhaustive coverage, unverified phase/ancilla state, or failure bounds above the frozen budget.
4. Compare the Pareto frontier over Toffoli count, peak qubits, T-depth, logical depth and failure bound. Do not reduce it to a single T×Q score.
5. Only after this gate, run target-aware simulation and provider-neutral lowering. A real-QPU test would still require credentials, bounded budget and explicit authorization.
6. Measure accepted useful output, latency, throughput, shots/billable usage, host and transfer costs, reconstruction, retries, energy where measurable, and total cost per accepted task against a competitive classical baseline.

**Falsifiers:** no candidate passes semantic/phase/ancilla verification; the candidate is not Pareto-better than the frozen baseline; the resource gain disappears after target-native mapping and error correction; or total cost per accepted useful task does not improve. A failure is retained as a negative result.

## Status

**LITERATURE_ONLY.** The accompanying RVC-001 software contract is a metadata and comparison gate; it does not simulate a circuit or certify a physical, QPU, material, fuel, fusion, energy or economic advantage.
