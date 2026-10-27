# Eight-Lane cycle — Batch 085: FormalFlow, QEC interval contract, MPNO and SPARC

**Date:** 2026-10-28  
**Canonical starting head:** `a662ae4b4580f3878c5ca14e3fd093bd80f4ff4e`  
**Primary owner:** Lane A — quantum programming/workload/reference contracts  
**Cross-lane owners:** B (decoder/provider boundary), C (memory/I/O accounting), E (materials/energy model surveillance), F (evidence/economics), H (publication and strategic continuity)  
**Evidence classes:** `SOFTWARE_CONTRACT_ONLY` and `LITERATURE_ONLY`  
**Paid QPU execution:** not authorized and not attempted

## Starting-state audit

The current main head was resolved dynamically from GitHub. The required charter, invariant ledger, goals, README, Research Operating System, open-frontier directive, Kanusanan Pongpanna Model, strategic references, all eight permanent root directives, latest Batch documents, focused gaps, `fundamental_limits.py`, `frontier_hypothesis.py`, `equation_discovery.py`, lane interface contract and CI state were inspected. The newest prior batch was discovered from the repository tree rather than assumed.

Exact starting-head Actions:
- [Prototype/invariant run #1825](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40557306514): success.
- [Cold-start handoff audit #1036](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40557306716): success.
- These checks apply to the starting head, not this new commit.

## Implemented Lane A contract

Added `uqpu/qec_ml_certificate.py` and `tests/test_qec_ml_certificate.py`:
- exact minima for a supplied finite set of abstract TRUE/COMPETING candidate costs;
- interval validation and conservative strict-separation classification;
- ties and overlapping intervals remain UNDECIDED;
- a valid interval must contain the exact finite-oracle minimum;
- aggregate logical-error interval `[failure/N, (failure + undecided)/N]`, with width exactly `undecided/N`;
- malformed candidates, excluded exact minima and invalid counts fail closed.

Seven focused unit tests were exercised in an isolated Python harness before publication. The repository's exact-head CI remains the acceptance gate. This is not a QLDPC implementation: it does not enumerate Pauli errors or syndromes, model circuit-level noise, implement branch-and-bound, or reproduce the source paper's bivariate-bicycle examples.

## Literature surveillance deltas

1. **FormalFlow / long-horizon autoformalization:** [arXiv:2609.19814v3](https://arxiv.org/abs/2609.19814), revised 2026-10-21. The authors report a large Lean 4 proof and corrections to side conditions/intermediate bounds. The associated [MIPStarRE source](https://github.com/LionSR/MIPStarRE/tree/95ccdf5a7591d6eb98b4c9c425f1e2d8408d8610) was inspected; its Lean/Mathlib pin is v4.35.0-rc2. The source commit predates v3 by one day, and no exact-head full proof build was observed. UQPU reproduction and independent source-faithfulness review remain open.
2. **MPNO / structural rollout stability:** [arXiv:2608.25744](https://arxiv.org/abs/2608.25744), submitted 2026-08-26. The proposed normalized graph-Laplacian propagator is intended to constrain spectral radius and improve rollout stability on the paper's tested PDEs. No UQPU reproduction or transfer to plasma/fusion/material systems is claimed. Stability, conservation, held-out accuracy and economic value must be tested separately.

The previously published GraphED constitutive-law watch, AI-mathematical-instrument corpus audit and certified QLDPC decoder source remain in force; they were not recast as project results.

### 3. Human-agent experimental design with instrument-grounded memory

The [SPARC literature watch](literature_watch/2026-10-28-sparc-agentic-experiment-design.md) records Liu et al., [arXiv:2609.06887](https://arxiv.org/abs/2609.06887), an external preprint reporting operator-supervised and agent-controlled scanning-probe experiments on a specific ferroelectric film. Its persistent `FINDINGS.md`/`PITFALLS.md` split and pre-write checks are relevant to experiment provenance and failure memory. UQPU has not reproduced the experiment; this does not establish Pangola-carbon substitution, semiconductor performance or transfer to fusion/material systems.


## A–H status

| Lane | Status this cycle | Next gate |
|---|---|---|
| **A — Quantum programming/workloads/compiler/runtime** | Added generic interval/certificate checks and seven tests; FormalFlow source audit extends RG-048. | Run exact-head CI; then build a code-matrix/bit-vector exhaustive oracle only after source conventions and inputs are pinned. |
| **B — Cloud/QPU/provider integration** | Decoder benchmark remains a literature-derived quality-reference gap. No provider, SDK, calibration or price was newly validated; no QPU job. | Reproduce tiny reference semantics first; keep provider/target/probability/price boundaries separate. |
| **C — RAM/VRAM/HBM/storage/state/data movement** | Decoder memory, syndrome I/O and reconstruction remain unmeasured; proof bytes, Hilbert dimension and readable storage remain distinct. | Measure peak memory, I/O and reconstruction on identical samples after source-level reproduction. |
| **D — Device/chip/process/packaging** | SPARC adds an external experiment-design watch only; no UQPU device or fabrication evidence. | Keep connectivity/noise assumptions tied to a concrete device only after software gates pass. |
| **E — Biomass/materials/bio-oil/fusion/cooling** | MPNO and SPARC are literature watches only; BIO-001 and FUS-001 remain open. | Test a source PDE and an instrument-grounded protocol on held-out controls before any domain transfer; continue accepted-liquid and net-electric cost contracts. |
| **F — Economics/benchmarks/evidence/integration** | No cost per accepted useful task measured; the interval helper is a correctness scaffold, not economic evidence. | Count search nodes, runtime, memory, retries and measured energy where available under matched quality. |
| **G — Chip manufacturing equipment/software/factory systems** | D/G co-design retained; no process-window, yield or cost-per-good-device result. | Tie any future model to actual process constraints and reproducible data. |
| **H — Kanusanan Pongpanna Model, finance and publication** | Published two source watches and an integration record; multilingual strategic references and agent/funding context preserved. | Convert evidence into staged milestones without implying lower WACC or mission closure. |

## INV-029–035 and foundational disposition

- **INV-029:** no physical data-center-to-phone compression or lifecycle-cost closure.
- **INV-030:** no Pangola-carbon material substitution, recovery or critical-material reduction demonstrated.
- **INV-031:** no accepted liquid fuel or full-path commercial cost demonstrated.
- **INV-032:** no reliable net-delivered fusion-electricity or lifecycle-cost result.
- **INV-033:** no reduction in financed principal, absolute interest or WACC demonstrated by this cycle.
- **INV-034:** strengthened the formal-method and source-to-proof audit path; no new physical mechanism or theorem accepted by UQPU.
- **INV-035:** proof/equation provenance, held-out tests, counterexamples, independent validation and explicit non-claims remain mandatory; no AI-generated equation is promoted to a law.

FND-001 thermodynamic-gap accounting, FND-002 output-information lower bounds, FND-003 matched control/quantum-speed-limit measurement, FND-004 alternative primitives, FND-005 QFT/particle mechanism scans and FND-006 mathematics-first invention remain active. The two new sources change methods to investigate, not the accepted physical constraints. EQN-001–006 remain evidence-gated; no equation passes to physical-law status.

BIO-001, FUS-001 and FIN-001 are unchanged/open. The MPNO source offers a possible stability constraint for later reduced-order-model testing, not evidence of fusion performance or lower energy cost. Finance still requires measured principal, rate/tenor, construction or evidence time, cash flows and risk; lower principal can reduce absolute interest at unchanged terms, but WACC reduction needs separate evidence.

## Sync and next highest-value gate

The large append-only `RESEARCH_GAPS.md` and `WORKLOG.md` were not rewritten from partial snapshots. The focused QEC gap and RG-048 were updated, the handoff manifest was synchronized, and this README is the main-page progress record. Historical/inaccessible branch reconciliation remains open.

Next:
1. Verify this exact commit's core Python matrix, extended reference/QSVT checks and cold-start audit.
2. Pin the Banfi paper version and exact code/noise/shot inputs; compare generic helper semantics against exhaustive tiny cases, then reconstruct source examples only if inputs are recoverable.
3. Pin FormalFlow's v3 source/Lean/blueprint mapping and independently audit three claims.
4. Reproduce one MPNO PDE result before considering a held-out, conservation-aware thermal/transport application.
5. Continue in parallel with RG-EQN-008, FND-001/FND-003, BIO-001, FUS-001 and FIN-001. Never submit a paid QPU job without credentials, bounded budget and explicit user consent.


## CI repair note

Exact-head cold-start audit [#1037](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40567389772) failed on handoff-manifest evidence labels outside the audit enum for lanes A/B/C/F. The repair normalizes the labels to supported classes without changing scientific claims or code. The core matrix was still in progress at the last observation; the repair commit requires fresh exact-head checks.


## CI status sync

Cold-start audit [#1038](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40567586577) passed on repair commit `d370e78f30def3cfa2a89cee812d4140c4e91f2d`; core run [#1827](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40567586481) passed the Python 3.10/3.11/3.12 matrix while extended QSVT/Qiskit jobs were still running. Cold-start audit [#1039](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40567972009) passed on the SPARC-watch commit `b5ebf5b7ad9e04df03d5c831b7bda95362e1c530`; core run [#1828](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40567972051) was still in progress. This count-correction commit requires its own exact-head checks.
