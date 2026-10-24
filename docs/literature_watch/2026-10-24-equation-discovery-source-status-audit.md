# Literature watch — 2026-10-24: equation-discovery methods and source-status audit

**Accessed:** 2026-10-24  
**Primary owner:** Lane H — strategy / future-industry research and publication  
**Feeds:** Lane A, Lane F, FND-006, EQN-001–006, INV-029, INV-034, INV-035  
**Evidence class:** LITERATURE_ONLY; one accepted journal record plus source-status conflict  
**Project evidence promotion:** none

## Fresh sources and status

### 1. AI-Newton: concept-driven physical-law discovery

The Physical Review Research accepted-paper page lists You-Le Fang, Dong-Shan Jian, Xiang Li, and Yan-Qing Ma, “AI-Newton: A concept-driven physical law discovery system without prior physical knowledge,” accepted 2026-10-09. The abstract describes concept proposals from multi-experiment data and progressive generalization; it reports rediscovery of mechanics laws on a noisy experimental dataset.

The associated arXiv preprint is arXiv:2504.01538, submitted 2025-04-02. The accepted-paper date is a publication-status update, not a newly discovered physical law. This cycle reviewed the official accepted-page abstract and arXiv record, not a complete final-version methods audit. Evidence class remains LITERATURE_ONLY.

Relevance: this is a candidate generator family for EQN-003 and a staged generalization pattern for EQN-006 traceability. The follow-up should test whether concept generation improves out-of-domain structure recovery over direct symbolic regression under the same search, compute, and data budgets. No reported law is treated as a UQPU result.

### 2. CoSR: progressive symbolic-law discovery — unresolved version/status conflict

The Physical Review Research accepted-paper page lists Mingkun Xia and Weiwei Zhang, “Data-driven progressive discovery of physical laws,” accepted 2026-10-06, DOI 10.1103/f2kp-pp4q. It describes Chain of Symbolic Regression (CoSR), which builds a law through a sequence of physically meaningful symbolic units instead of one-step expression search.

However, the official arXiv record for arXiv:2603.13727 explicitly marks the paper withdrawn and states that it needs to be retracted due to methodological flaws found in the Rayleigh–Bénard-convection case. The journal accepted-page record and withdrawn arXiv version are inconsistent in status. This cycle did not resolve the discrepancy and did not inspect a complete version-of-record or correction notice.

**Decision:** do not use CoSR's performance claims as evidence or as a trusted baseline until the final journal version, withdrawal note, and any correction/retraction status are reconciled. Preserve the conflict as a first-class literature-audit result rather than silently selecting the more favorable status.

## What is genuinely new for this repository

- The existing 2026-10-23 watch already covers OptScientist optimization-law discovery and the ancilla-QFI theorem preprint. Those two sources were not counted as new this cycle.
- The new method-family candidate is concept-driven, multi-experiment law discovery (AI-Newton).
- The key negative result is a source-status conflict around CoSR, showing why an accepted-page abstract cannot replace version/provenance review.
- Targeted searches on 2026-10-24 found no additional primary source that changed the current evidence gates for Pangola materials, saleable bio-oil, net fusion electricity, manufacturing, or project financing. This is a bounded search, not an exhaustive systematic review.

## Falsifiable follow-up

1. Retrieve and compare the full accepted AI-Newton version against its 2025 preprint; freeze versions and dataset provenance.
2. Build a matched synthetic benchmark with known generating laws, multiple experiments, noisy measurements, confounded variables, and held-out domains.
3. Compare direct symbolic regression, concept-driven generation, progressive composition, optimization-law discovery, and a non-physics-aware negative control under identical search-wall-clock and host-resource budgets.
4. Score exact structure recovery separately from held-out prediction, unit/dimension validity, symmetry/conservation/causality, limiting cases, counterexamples, identifiability, false-discovery rate, expression complexity, and data-selection leakage.
5. Resolve CoSR's status conflict from the journal version and correction/retraction record before including it as a scored baseline.
6. Any passing synthetic benchmark remains MODEL_ONLY; a physical claim still needs a discriminating observation, proof/experiment where appropriate, independent replication, device/system consequence, and full economics.

## Invariant contribution and non-claims

- **INV-029:** no physical data-center-to-phone compression; only an offline candidate-screen interface.
- **INV-030:** no Pangola carbon, critical-material substitution, recovery, or transmutation claim.
- **INV-031:** no commercial bio-oil/fuel evidence.
- **INV-032:** no net delivered fusion-electricity evidence.
- **INV-033:** no interest-rate, WACC, or project-finance evidence.
- **INV-034:** strengthens source-status discipline and a falsifiable mathematics-first comparison path.
- **INV-035:** expands candidate-generator coverage while preserving incumbent equations, dimensions, symmetry, conservation, causality, held-out predictions, falsifiers, and independent validation as binding gates.

No item in this note is a verified UQPU discovery. It belongs in the literature-watch area, not the root-level INV-037 verified-discovery registry.
