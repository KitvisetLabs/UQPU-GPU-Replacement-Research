# Research gap RG-037 — fault-tolerance spacetime and memory-aware thermodynamic inference

**Date opened:** 2026-10-25  
**Primary owner:** Lane A — workload/resource contracts  
**Integration owners:** Lanes C and F  
**Evidence state:** LITERATURE_ONLY + MODEL_ONLY_SCALING_DIAGNOSTIC  
**Project evidence promoted:** no

## Objective

Account for the width–duration reliability term in long-lived coherent quantum workloads, and prevent entropy-production estimates from silently assuming away temporal memory.

## Evidence and scope

- Bharti, Haug and Tanggara, arXiv:2608.26272v1 (2026-08-26), gives a tight asymptotic spacetime-size expression for a specified quantum-memory model under independent erasure noise and stated recovery/error assumptions.
- Schwarz, Kolomeisky and Godec, PRL accepted 2026-09-25, DOI 10.1103/gwf7-6kvr, analyzes memory-order conditions for reliable entropy-production lower-bound inference.

These are external literature results, not UQPU measurements. The asymptotic theorem hides constants and does not directly produce a target-specific hardware cost. The thermodynamic estimator result does not measure UQPU energy or fusion/bio-oil process performance.

## Blockers

- No architecture-specific physical/logical error model, syndrome extraction schedule, decoder, feed-forward, gate-level resource count or energy data.
- No matched measured workload comparing width, duration and target error.
- No calibrated trajectory dataset for testing memory-order sensitivity in a project energy process.
- No independently replicated hardware result or accepted useful-task economics.

## Unlock criteria

1. Unit-tested evaluation of the dimensionless `log(S/epsilon)/K` term with domain checks and explicit model-scope warnings.
2. For target claims, an architecture-specific resource model including all physical operations, time, classical control, I/O, energy and cost.
3. For thermodynamic inference, synthetic known-truth tests followed by calibrated measurements with preregistered observation order, uncertainty and independent replication.

## Best current alternative

Use the scaling term only as a dimensionless diagnostic, retain the source assumptions, and report all target-specific resources as unknown until measured or independently calibrated. Use multi-order trajectory analysis instead of silently applying a first-order Markov estimator to memoryful data.

## Next action

Continue M-QSP constructive decision implementation as Lane A's top algorithmic gate. Independently, extend the FND-001 ledger with a synthetic memory-order coverage benchmark before any physical experiment. Do not overwrite the append-only RESEARCH_GAPS.md or WORKLOG.md from partial content; this artifact records the new gap without truncating canonical history.
