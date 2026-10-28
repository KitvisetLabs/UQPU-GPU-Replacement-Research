# Batch 099 — residual-informed, conjecture-guided and continuous equation discovery

**Date:** 2026-10-28  
**Starting main SHA:** 87d3d332478fac15cf1b1dc76de54de2ff6f284d  
**Primary lane:** A — quantum programming/workloads/compiler/runtime  
**Cross-lane owners:** F — evidence and economics; H — literature and strategic publication  
**Evidence class:** LITERATURE_ONLY + PROTOCOL_UPDATE  
**Execution:** no new matched benchmark, no physical experiment, no real-QPU job and no paid cloud execution

## 1. Canonical starting-state and CI audit

The cycle starts from the newest observed main commit, not a fixed batch number. Inspected the project charter, version invariants, goals, README, Research Operating System, Open-Frontier Directive, Kanusanan Pongpanna Model, strategic references, root directives 00/00A/01–06, current Batch 098, RG-EQN-008, schema-v4 comparator/tests, Lane A track, A–H manifest, handoff manifest, WORKLOG and RESEARCH_GAPS.

At starting SHA 87d3d332478fac15cf1b1dc76de54de2ff6f284d, the exact-head **UQPU Prototype and Project Invariants** run #1933 (ID 40662975073) passed. The exact-head **Autonomous Cold-Start Handoff Audit** run #1183 (ID 40662975151) failed. Its uploaded audit output and job log identify one error only: `missing_commit_trailer:Research-Sync: main`. The audit had checked all A–H lanes and 28 integration pairs. This is a synchronization-policy failure, not a scientific-claim validation. This commit carries the required `Research-Sync: main` trailer; the resulting exact-head Actions runs must still be observed before calling the repair verified.

- Core/invariant run: https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40662975073
- Cold-start run and failure evidence: https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40662975151

The cold-start validator's scope is structural handoff/readability and commit-to-main synchronization. It does not validate physics, benchmark truth, inaccessible branches/forks or external scientific claims.

## 2. Fresh literature surveillance delta

The prior-art search found that RISR had already been cited in the repository's 2026-10-15 equation-discovery identifiability watch, so it is integrated as existing prior art rather than claimed as a new discovery. The official arXiv record dates RISR to 2026-10-08; the older watch's “submitted 2026-10-15” wording was a metadata error and is corrected in this commit. The new-to-repository source additions are SCOPE/ClosureBench and MorphingNet. Together, the three families extend RG-EQN-008 beyond the previous cycle's width-only emphasis:

- Li et al., **RISR**, posted 2026-10-08: https://arxiv.org/abs/2610.11387 — pointwise residual representations guide formula proposals and correction selection.
- Hu et al., **SCOPE / ClosureBench**, posted 2026-10-13: https://arxiv.org/abs/2610.18938 — multiple explicit conjectures and active experiments are evaluated with evidence/mechanism/experiment metrics.
- Gao, Yi and Sun, **MorphingNet**, posted 2026-10-14: https://arxiv.org/abs/2610.19942 — continuous parameterized formula units change the optimization/search formulation.

The new dated literature watch explains genuine novelty, evidence class, limitations, UQPU relevance and a falsifiable follow-up. These are author-reported preprint results, not UQPU evidence. Their metrics are not pooled or ranked across incompatible tasks.

## 3. Lane A protocol advancement

RG-EQN-008 and the Lane A track now distinguish three axes:
1. residual-informed candidate correction;
2. conjecture-level search with active data acquisition;
3. continuous formula parameterization and later structure recovery.

The static equation-recovery comparison and the interactive ClosureBench-style experiment-design comparison remain separate. For static methods, source/license, data acquisition, model/checkpoint, code, prompt/operator bundle, runtime, units, preprocessing and law-family/scale-held-out manifests must be frozen. Require the existing schema-v4 provenance fields, at least 30 shared preregistered seeds, identical per-run ceilings, one cost basis, independent acceptance and false-discovery/counterexample accounting. Where architectures differ, match total resource ceilings rather than pretending model architecture is identical; include training cost.

For the interactive track, equalize experiment/simulation calls and compute budgets, keep tasks blind, and report evidence faithfulness, mechanism insight and experimental effectiveness alongside prediction and physical-constraint checks. Do not combine these outcomes with static SRBench scores.

## 4. Eight-lane review and integration

| Lane | Status | This-cycle work / next gate |
|---|---|---|
| A — quantum programming/workloads/compiler/runtime | **Advanced: protocol** | Add residual-feedback, conjecture-level and continuous-parameterization families to RG-EQN-008 without displacing Priority-1 provider-neutral lowering and exact signed-Max-Cut reference/simulator comparison. |
| B — cloud/QPU/provider integration | Reviewed / maintained | Keep adapters provider-neutral and dry-run-first for IBM Quantum, Braket, Azure providers, IonQ, Rigetti, D-Wave, IQM, Quantinuum, Pasqal, QuEra, Quandela, OQC and emerging providers. No paid job authorized. |
| C — memory/state/data movement | Reviewed / maintained | Include residual data, generated tokens, memory, I/O, reconstruction, host compute and data movement in total resource accounting. Hilbert-space dimension is not classical readable storage. |
| D — device/chip/process/fabrication/packaging | Reviewed / maintained | No device claim; future constitutive/process models need measurement traceability, metrology, process windows, yield and reliability. |
| E — biomass/materials/bio-oil/fusion/cooling | Reviewed / maintained | BIO-001 still needs feedstock-specific accepted-liquid mass/energy/upgrading/full-cost evidence; FUS-001 still needs reliable net delivered electricity and lifecycle cost. New equation-discovery papers provide no such evidence. |
| F — economics/benchmarks/evidence/integration | **Advanced: acceptance protocol** | Keep static and interactive tasks separate; account for training plus inference, full resources, cost per accepted candidate and false discoveries. |
| G — manufacturing equipment/software/factory systems | Reviewed / maintained; continuous D/G co-design | Tie any later process-equation result to equipment, metrology, process control, yield and cost per good die/package. |
| H — strategy/finance/publication | **Advanced: literature publication and handoff** | Publish dated source synthesis; preserve Thai/English/Chinese/Japanese/Korean/German master-plan links and strategic AI-agent/funding references as context, not scientific evidence. |

All 28 unordered A–H interfaces remain under review: A↔B/C/D/E/F/G/H; B↔C/D/E/F/G/H; C↔D/E/F/G/H; D↔E/F/G/H; E↔F/G/H; F↔G/H; G↔H. Coupling is accepted only where a causal interface exists. D/G co-design remains continuous.

## 5. Foundations, invariants and economics

FND-001 thermodynamic-gap accounting, FND-002 output-information lower bounds, FND-003 matched control-versus-speed-limit measurement, FND-004 alternative physical primitives, FND-005 QFT/particle mechanism scans, FND-006 mathematics-first invention and EQN-001–008 remain active. No candidate equation was added to the physical-limits code and no physical law was promoted.

INV-029–035 and INV-025/026/027 remain preserved. The US$10T–US$100T figure remains an ambition-scale proxy; physical phone-class compression, 100×/100,000,000× advantages, universal subsystem replacement, Pangola material substitution, commercial ultra-low-cost bio-oil, commercial ultra-low-cost fusion and lower project WACC remain unachieved evidence-gated goals. Lower principal can lower absolute interest at unchanged terms; a lower WACC requires separate evidence.

BIO-001, FUS-001 and FIN-001 remain open. No accepted fuel, reliable net electricity, financing improvement or commercial result follows from symbolic-regression papers.

## 6. Exact next gate

1. Confirm the cold-start audit passes on the new main SHA with this commit's `Research-Sync: main` trailer; also confirm core/invariant CI on that exact SHA.
2. If both pass, verify source/license/code/data availability for RISR and MorphingNet before selecting a static benchmark adapter.
3. Freeze source and environment hashes, group-disjoint split certificates and budgets before preregistering the 30+ seed static comparison.
4. Keep SCOPE/ClosureBench as a separate active-experiment track with equal experiment budgets.
5. Continue Lane A's Priority-1 signed-Max-Cut provider-neutral lowering/reference/simulator path in parallel.

**Negative evidence / stop rules:** no result is accepted if its advantage vanishes under held-out law-family or scale shifts, relies on leakage/unequal budgets, or increases constraint failures, counterexamples or false discoveries. A fit, formal proof or AI-generated expression alone is not a physical-law or technology claim.


## 7. Literature provenance correction

The repository search found RISR already cited in the 2026-10-15 identifiability watch. Batch 099 does not count RISR as newly discovered; it integrates the existing source into the current matched-comparison protocol alongside the new-to-repository SCOPE/ClosureBench and MorphingNet sources. Official arXiv metadata gives RISR's posting date as 2026-10-08. The older watch's contrary date label has been corrected. Evidence classification remains LITERATURE_ONLY.
