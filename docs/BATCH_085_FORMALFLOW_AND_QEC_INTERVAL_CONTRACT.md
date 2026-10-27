# Batch 085 — FormalFlow, decoder interval contract and physics-informed rollout stability

**Date:** 2026-10-28  
**Canonical starting head:** `a662ae4b4580f3878c5ca14e3fd093bd80f4ff4e`  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Cross-lane owners:** Lane B, C, E, F and H  
**Evidence:** `SOFTWARE_CONTRACT_ONLY` + `LITERATURE_ONLY`; no hardware or commercial evidence  
**Scope:** small finite-candidate decoder-certificate scaffold, focused tests, three dated literature watches, README/handoff integration  
**Paid QPU job:** no

## Starting-state and CI

The newest Batch was discovered from the current repository tree. Required project charter, invariants, goals, README, operating system, open-frontier directive, Kanusanan Pongpanna Model, strategic-reference index, permanent root directives, newest batch/gaps, foundational helpers, equation-discovery helper and current Actions state were inspected.

Starting-head exact checks passed:
- [Prototype/invariant run #1825](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40557306514).
- [Cold-start audit #1036](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40557306716).

These results do not transfer to this new commit. Exact-head CI remains required.

## Lane A — tiny finite-candidate interval contract

Added:
- `software/uqpu-prototype/uqpu/qec_ml_certificate.py`
- `software/uqpu-prototype/tests/test_qec_ml_certificate.py`

The helper provides:
1. an exhaustive minimum-cost oracle over a finite abstract candidate list split into TRUE and COMPETING classes;
2. interval validation and strict-separation outcomes;
3. fail-closed behavior when an interval excludes the exact finite-oracle minimum;
4. explicit UNDECIDED for ties or overlapping intervals;
5. the aggregate error interval `[failure/N, (failure + undecided)/N]`, with width `undecided/N`.

Seven tests cover success, failure, ties, loose intervals, interval exclusion, malformed candidates and aggregate accounting. They passed in an isolated Python harness before publication; the repository CI result is the final acceptance gate.

**Boundary:** this is not a QLDPC decoder, Pauli/syndrome enumerator, circuit-level noise model or branch-and-bound implementation. It does not reproduce the paper's bivariate-bicycle results. The code is a reusable contract scaffold only.

## Literature surveillance

### 1. Long-horizon AI autoformalization

The [FormalFlow watch](literature_watch/2026-10-28-formalflow-long-horizon-autoformalization.md) records Lu et al., [arXiv:2609.19814v3](https://arxiv.org/abs/2609.19814), revised 2026-10-21. The authors report a large Lean 4 proof of quantum soundness for the low individual-degree test and corrections to side conditions/intermediate bounds. The public [MIPStarRE repository snapshot](https://github.com/LionSR/MIPStarRE/tree/95ccdf5a7591d6eb98b4c9c425f1e2d8408d8610) was inspected; it pins Lean/Mathlib v4.35.0-rc2. The pinned commit predates the manuscript's v3 revision by one day, and an exact-head full proof build was not observed. UQPU has not independently reproduced the theorem or its corrections.

**Follow-up:** pin manuscript and code hashes, map three claims through source/blueprint/Lean, rebuild with the pinned toolchain, and independently inspect source-faithfulness, dependencies, axioms and any admitted goals.

### 2. Structurally stable physics-informed operator

The [MPNO watch](literature_watch/2026-10-28-mpno-stable-physics-informed-operator.md) records Du et al., [arXiv:2608.25744](https://arxiv.org/abs/2608.25744), submitted 2026-08-26. The authors propose a normalized graph-Laplacian propagation operator designed to constrain spectral radius and report stable rollouts on selected PDEs. UQPU has not reproduced the results. This does not establish conservation, domain transfer, fusion performance or a new physical law.

**Follow-up:** reproduce one source PDE, compare with baselines on equal data/compute, hold out long trajectories and material/velocity conditions, and measure stability, conservation residuals, error, memory and wall time before any new domain is considered.

The prior GraphED constitutive-law watch is already recorded in the repository and was checked as existing coverage, not mislabeled as a new delta.

### 3. Human-agent experimental design with instrument-grounded memory

The [SPARC literature watch](literature_watch/2026-10-28-sparc-agentic-experiment-design.md) records Liu et al., [arXiv:2609.06887](https://arxiv.org/abs/2609.06887), an external preprint reporting operator-supervised and agent-controlled scanning-probe experiments on a specific ferroelectric film. Its persistent `FINDINGS.md`/`PITFALLS.md` split and pre-write checks are relevant to experiment provenance and failure memory. UQPU has not reproduced the experiment; this does not establish Pangola-carbon substitution, semiconductor performance or transfer to fusion/material systems.


## A–H lane status

- **A:** interval certificate contract and tests added; formalization provenance watch opened.
- **B:** QLDPC decoder-reference gap remains open; no provider job, credentials/pricing check or hardware result.
- **C:** decoder memory/I/O/reconstruction remain unmeasured; proof size and quantum state dimension are not readable classical storage.
- **D:** SPARC is an external instrument-grounded experiment-design watch only; no UQPU device/chip/process/packaging evidence changed.
- **E:** MPNO and SPARC are literature-only; BIO-001 and FUS-001 remain open, with no accepted-liquid or net-electric result.
- **F:** no measured cost per accepted task; resource metrics are required after matched quality/source reproduction.
- **G:** D/G co-design continues; no yield/process-window/cost-per-good-device result.
- **H:** two source watches, batch and integration record published; six-language strategic master-plan links and strategic AI-agent/funding references preserved.

## INV-029–035

- **INV-029:** no Data-Center-to-One-Phone physical compression or lifecycle-cost closure.
- **INV-030:** no Pangola carbon substitution or elemental-transmutation claim.
- **INV-031:** no accepted biomass liquid fuel or full-path ultra-low-cost result.
- **INV-032:** no net reliable delivered fusion-electricity result.
- **INV-033:** no financed-principal/interest/WACC reduction demonstrated.
- **INV-034:** formal proof/source audit is a method-level advancement only.
- **INV-035:** candidate methods remain subordinate to dimensional, symmetry, conservation, causality, held-out, counterexample, proof/experiment and independent-validation gates.

FND-001–006 and EQN-001–006 remain active/evidence-gated. No physical equation, lower bound, anomaly, particle mechanism or physical law is promoted. The two watches inform methods and future falsifiers only.

## Sync debt and next gate

Large append-only `RESEARCH_GAPS.md` and `WORKLOG.md` were left intact to avoid replacing partial history. Focused gaps, the handoff manifest and README were updated. Historical/inaccessible branch reconciliation remains unresolved.

Next gate: run exact-head CI; then extend the toy checker to a real finite binary/correction model only after the source conventions and code/noise inputs are pinned. In parallel, conduct the three-claim FormalFlow source-to-Lean audit, one source-PDE MPNO reproduction, and continue RG-EQN-008, FND-001/FND-003, BIO-001, FUS-001 and FIN-001. Paid QPU execution remains unauthorized.


## Post-publication CI finding and repair

The exact-head cold-start audit `#1037` failed because the handoff manifest used combined/descriptive evidence labels outside the fixed `VALID_EVIDENCE` enum for lanes A/B and `OPEN_GAP` for C/F. The follow-up commit changes only those metadata values to the schema-approved `SOFTWARE_UNIT_TESTS`, `LITERATURE_ONLY` and `SOFTWARE_CONTRACT` classes and records the failure explicitly. This is a governance metadata failure, not evidence that the decoder interval tests failed. The repair commit must pass its own exact-head audit and core matrix before the cycle can be called CI-green.
