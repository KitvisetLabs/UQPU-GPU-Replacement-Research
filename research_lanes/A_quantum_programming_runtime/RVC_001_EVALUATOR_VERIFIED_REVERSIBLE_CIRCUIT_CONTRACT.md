# Lane A work item RVC-001 — evaluator-verified reversible-circuit co-design

**Primary owner:** Lane A — quantum programming, workloads, compiler and runtime  
**Integration owner:** Lane F — evidence, benchmark and lifecycle economics  
**Publication owner:** Lane H  
**Status:** OPEN / SOFTWARE CONTRACT ONLY  
**Evidence class:** SOFTWARE_CONTRACT_TESTS + LITERATURE_ONLY  
**UQPU resource or cost advantage promoted:** none

## Objective

Test whether evaluator-guided search can find a lower-resource implementation of one reversible primitive while preserving identical function semantics, relative phase, ancilla cleanup, supported input domain and failure budget. The motivating external preprint is Gu et al., arXiv:2610.22367v1, submitted 2026-10-15; its reported improvements are not UQPU results.

## Canonical interface

Implementation: software/uqpu-prototype/uqpu/reversible_circuit_contract.py  
Tests: software/uqpu-prototype/tests/test_reversible_circuit_contract.py  
Gap: docs/RESEARCH_GAP_RG041_EVALUATOR_VERIFIED_REVERSIBLE_CIRCUIT_CO_DESIGN.md  
Literature watch: docs/literature_watch/2026-10-25-llm-evaluator-guided-quantum-circuit-co-design.md  
Integration: integration/INT-20261025-023-LLM-CIRCUIT-CO-DESIGN.json

A candidate record pins the function specification and candidate hashes, generator/evaluator identities and hashes, verification provenance, exhaustive coverage or proof, relative-phase status, ancilla-cleanup status, failure bound/budget, Toffoli count, peak qubits, T-depth, logical depth and optional target identity. The comparator refuses unverified or semantically mismatched candidates and reports Pareto dominance/tradeoff across multiple resource dimensions.

## Required gate sequence

1. Freeze a representative reversible function, baseline, domain, widths, target scope and accepted failure budget.
2. Verify every input/output basis state where tractable, or check a proof artifact with explicit assumptions.
3. Check relative phase and ancilla cleanup/uncomputation separately.
4. Keep failed, incomplete and incomparable candidates as negative evidence.
5. Compare Toffoli count, peak qubits, T-depth, logical depth and failure bound as a Pareto frontier; T×Q is only a descriptive proxy.
6. Lower only verified candidates to target-aware simulation and provider-neutral compilation.
7. Measure accepted useful output and full cost against competitive CPU/GPU/NPU baselines before any economic promotion.

## Integration interfaces

- **A→B:** verified semantics before provider-neutral lowering; no provider or paid QPU job is authorized.
- **A→C:** peak logical qubits and ancilla lifetime are not readable classical RAM/storage; account for host memory, transfers and output reconstruction.
- **A→D/G:** target-native gates, control, QEC, calibration and manufacturing are downstream; D/G co-design remains continuous.
- **A→F:** compare identical accepted outputs, include failure/retry/host/energy/cost, and do not promote logical-resource proxies to total economics.
- **A→E/H:** only a demonstrated workload-to-material/energy/industrial causal path can propagate into BIO-001, FUS-001, FIN-001 or the strategic plan.
- **FND/EQN:** generator output remains a hypothesis; proof, counterexample search, held-out tests and independent validation control promotion.

## Current result and negative boundary

Ten isolated contract tests passed in a Python 3.13 harness. The exact-head GitHub Actions matrix is still required. No representative circuit has been generated or independently verified, and no simulator, provider SDK or real QPU was used. The contract does not prove correctness of an external evaluator or any physical law.

## Falsifier and next gate

RVC-001 fails to advance if no candidate passes correctness/phase/ancilla/failure gates, if no Pareto improvement survives, or if target-native mapping, QEC and accepted-task costs erase the logical gain. The next gate is to freeze one small primitive and baseline, then run an independent exact or proof-backed evaluator before any target-aware simulation.
