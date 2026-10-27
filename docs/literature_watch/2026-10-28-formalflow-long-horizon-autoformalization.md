# Literature watch — long-horizon AI autoformalization of a quantum-complexity theorem

**Watch date:** 2026-10-28  
**Primary source:** Sirui Lu, Ruixuan Deng, Yanqiao Zhu and Zhengfeng Ji, “Long-horizon autoformalization of a core theorem underlying MIP* = RE,” arXiv:2609.19814v3, revised 2026-10-21.  
**Official record:** https://arxiv.org/abs/2609.19814  
**Associated Lean repository:** https://github.com/LionSR/MIPStarRE  
**Pinned source snapshot inspected:** `LionSR/MIPStarRE@95ccdf5a7591d6eb98b4c9c425f1e2d8408d8610` (commit dated 2026-10-20).  
**Evidence class:** `LITERATURE_ONLY` for UQPU; the paper reports a machine-checked Lean development, but UQPU has not independently rebuilt or audited it.

## Genuine methodological contribution

The authors describe FormalFlow, a human-supervised, multi-agent process using a shared proof blueprint and nested planning, proving and review loops to control statement drift over a long formalization. They report completing a Lean 4 proof of quantum soundness for the classical low individual-degree test in 63 days, with 126,367 lines of agent-generated Lean code. They also report corrections to side conditions and intermediate error bounds in the published proof and an improved exponent in the main theorem.

This is relevant because it demonstrates a concrete workflow for coordinating a large proof while retaining a kernel-checkable artifact, not because an AI-generated proof is automatically novel, source-faithful or physically meaningful.

## Source and reproducibility audit

The public repository snapshot exposes `leanprover/lean4:v4.35.0-rc2` in `lean-toolchain` and requests Mathlib revision `v4.35.0-rc2` in `lakefile.toml`. The pinned commit is dated one day before the paper's v3 revision; therefore it is a useful source pin, **not yet proof that the snapshot exactly matches every v3 claim**. The observed actions history includes a successful scheduled housekeeping run on 2026-10-27 and a successful full-documentation run on 2026-10-25, but no exact-head PR-CI build was observed for the pinned commit in this audit.

The paper's machine checking is source-reported evidence about the authors' artifact. It is not an independent UQPU reproduction. Kernel acceptance establishes that a formal statement follows from the Lean environment and imported axioms; source-faithfulness, theorem novelty, the correctness of the paper-to-formal translation and relevance to a physical model remain separate questions.

## Limitations and non-claims

- The arXiv paper is a preprint; UQPU has not reproduced the claimed corrected side conditions, error bounds or exponent.
- The code snapshot and v3 manuscript are not yet shown to be byte-aligned.
- A successful build cannot alone prove that a formal statement faithfully captures the intended paper theorem or that every imported axiom is appropriate.
- The result concerns mathematical quantum-complexity proof infrastructure. It does not show real-QPU speedup, quantum hardware capability, a new physical law, a material/fuel/electricity advantage or lower project financing cost.

## Exact UQPU relevance

- **Lane A / INV-034–035:** use blueprint ownership, exact statement hashes, dependency tracking, source-to-formal statement comparison and independent proof review as a candidate workflow for EQN-001–006. Retain failed attempts and unresolved premises.
- **Lane B:** theorem formalization is not a provider/target benchmark. It supplies no QPU access, calibration, price or hardware result.
- **Lane C:** proof-line count, AST size and quantum state dimension are not interchangeable with readable RAM/storage. Formalization resource costs must be measured separately.
- **Lane D/G:** no device, chip, process, packaging or manufacturing result follows.
- **Lane E:** no Pangola-carbon, accepted bio-oil, fusion net-electricity or cooling result follows.
- **Lane F:** any workflow-efficiency comparison must pin the same theorem set, source revision, toolchain, automation settings, human review and success predicate, then report compute/time/memory/retries only when measured.
- **Lane H:** the project can adopt a durable agent handoff and publication protocol without treating strategic or speculative claims as scientific evidence.

## Falsifiable follow-up

1. Pin the v3 manuscript PDF/TeX hashes and the Lean repository commit separately; record the mismatch if no matching source snapshot exists.
2. Select three claims: one core theorem statement, one reported side-condition correction and one intermediate error bound.
3. Trace each claim through the paper source, blueprint entry and Lean declaration; compare hypotheses and conclusions exactly.
4. Rebuild using the pinned Lean/Mathlib toolchain and record every missing dependency, `sorry`, admitted axiom, failed target or environment mismatch. Do not infer a complete proof from a partial build.
5. Have an independent reviewer reconstruct the three source-to-formal mappings and assess whether the reported correction is genuinely necessary.
6. Only after these checks pass may a small controlled study compare proof completion time/resource use; no metric may replace correctness, source-faithfulness or held-out mathematical adequacy.

**Decision:** extend RG-048 with a source-faithfulness/reproducibility branch. No new theorem, equation or physical-law status is assigned by this watch.
