# Literature Watch — Cold-Start Research Agents and Scalable Block Encoding

**Accessed:** 2026-10-16  
**Evidence class:** `LITERATURE_ONLY`  
**Project evidence promotion:** none

## Material deltas

1. Li, Ou, Wang, Yao, Yuan and Zhang, *Optimal T Counts under Sparsity: from QROM to State Preparation and Block Encoding*, arXiv:2607.28260v2 (revised 2026-10-01), https://arxiv.org/abs/2607.28260. The paper supplies asymptotically matching Clifford+T bounds for sparse QROM, state preparation and sparse block encoding. For a row/column-sparse matrix it reports a block-encoding T-count scaling with the address size, sparsity and encoding error, and propagates that cost into QSVT.
2. Li et al., *Coupled Harness--Model Evolution for Scientific Equation Discovery*, arXiv:2610.17740v1 (submitted 2026-10-13), https://arxiv.org/abs/2610.17740. The system freezes an evolved tool harness before evaluation, keeps selection separate from test data, uses held-out promotion checks and retains failed extensions. This is relevant to EQN-001..006 and the repository's cold-start handoff culture, but benchmark scores are not evidence of physical-law discovery.
3. Reed et al., *Principles and Techniques for Agentic Research in Experimental Physics*, arXiv:2610.17193v1 (submitted 2026-10-12), https://arxiv.org/abs/2610.17193. The authors describe human-directed closed-loop physics agents and case studies. It supports treating reproducible scaffolding, goal definitions and validation as part of the research instrument; it does not establish that autonomous agents independently validate their own claims.

## Concrete project decisions

- **Lane A / RG-033:** do not treat the existing dense two-qubit `UnitaryGate` fixture as a scalable oracle. The next workload block-encoding artifact must declare matrix dimension `2^n`, row/column sparsity `s`, encoding error, normalization, QROM data representation, query count and measured decomposed resources. Compare measured scaling with the cited sparse-QROM bounds; do not claim an advantage from an asymptotic theorem alone.
- **FND/EQN / RG-034:** add an immutable harness version, a candidate-library version, distinct fit/selection/test hashes, a held-out tool-promotion set and an explicit regression suite. A harness edit that improves a score but breaks a previously accepted control is rejected.
- **Autonomous handoff:** implement the repository-owned cold-start audit and commit-sync trailer check. This is process verification only; it cannot prove scientific correctness or see inaccessible forks.

## Limits and falsifiable follow-ups

- The papers are preprints, not project measurements. No QPU, device, material, vehicle, fuel, fusion or economic result follows.
- Sparse-block-encoding theory becomes operationally relevant only after a frozen useful-output workload exposes an explicit sparse matrix/oracle. **Falsifier:** measured construction lacks the assumed access model or scales outside the declared resource envelope.
- Harness evolution becomes relevant to UQPU equation discovery only if the frozen split commitments prevent leakage and the controls recover known null directions. **Falsifier:** a mutation reads held-out data, fails a known-law control, or cannot reproduce the exact committed candidate.

No third-party percentage, theorem or case study is promoted to UQPU evidence.
