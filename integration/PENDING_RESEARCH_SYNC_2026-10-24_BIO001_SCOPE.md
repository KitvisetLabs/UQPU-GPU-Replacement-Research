# Pending-main sync — BIO-001 detailed cost ledger and EQN-SCOPE-001

**Record date:** 2026-10-24  
**Status:** PENDING REVIEW / NOT MERGED  
**Canonical base checked:** main at c7b5958af58fad04a101ef5c6abf6a29293c867e  
**Source PR:** https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/pull/63  
**Source branch:** research/2026-10-24-bio-oil-cost-ledger-scope-watch  
**Latest source SHA:** 63080d1f11f6e38112baa84130f614b91c4c89eb

## Source commits covered

- b749367714100bdb48409dd54b8e3194cd41afc4 — add component-resolved accepted bio-oil cost ledger to software/uqpu-prototype/uqpu/energy_finance.py.
- 63c49d6f0e6680bbf531b1de47cb2ec368ec9a0c — add synthetic BIO-001 component-accounting tests.
- 497fe6725fcace986cedbb374237ff88549a66c7 — remove unused test import.
- 226d597b4a7f703fb8fc61dc9326addf2b2f71ca — add Lane E BIO-001 functional-unit and evidence-gate document.
- bf717b772df90e91c74407c7ec90aed7f6964245 — add Lane H literature watch on SCOPE and ClosureBench.
- 11da6a7d0f21516a6f2dd087b683990b422df009 — add A-H / INV-029–035 integration handoff.
- 3346c270ccac03849a52976ca93fbdedcadbede2 — add required pending-main commit trailer and record initial cold-start audit failure.
- 63080d1f11f6e38112baa84130f614b91c4c89eb — cross-link the separately pending PR #49 BIO-TEA-001 / FUS-ECON-001 cost-driver work.

## Objective and method

Expose a detailed accepted-liquid cost ledger without breaking the existing aggregate API. Costs are normalized to final accepted liquid after required upgrading, with separate components for feedstock, collection/transport, preprocessing, CAPEX recovery, fixed O&M, conversion, upgrading, hydrogen, catalysts, utilities, logistics, compliance/storage, working-capital carrying cost and separately reported coproduct credits. Add synthetic tests for reconciliation, accepted-yield normalization, energy-unit conversion, single credit subtraction and fail-closed invalid inputs.

The literature watch reviews the SCOPE/ClosureBench conjecture-guided equation-discovery preprint. It proposes EQN-SCOPE-001, a falsifiable matched-budget benchmark with held-out equation families, physical constraints, counterexamples, false-discovery accounting and explicit experiment costs.

## Results and negative evidence

- The branch has created the proposed software, tests and documentation; this is not a merged-main result.
- Unit tests were added, but exact-head UQPU CI was queued at the latest check. The first cold-start audit failed only because the latest commit lacked the required Research-Sync trailer; the follow-up commit added Research-Sync: pending-main and its rerun passed.
- The cost model is MODEL_ONLY and the tests use synthetic values. No Pangola mass/energy balance, saleable-fuel assay, material substitution, commercial fuel, fusion electricity, financing-rate change, quantum advantage, or new physical law is demonstrated.
- SCOPE/ClosureBench is third-party preprint evidence, not independent project validation.
- Related PR #49 proposes BIO-TEA-001 and FUS-ECON-001 from literature; those follow-ups remain unexecuted and that PR remains separate.

## Evidence class and invariant impact

Evidence class: MODEL_ONLY + SYNTHETIC_UNIT_TESTS + LITERATURE_ONLY.

- INV-029: accounting interface only; no Data-Center-to-Phone result.
- INV-030: no Pangola carbon qualification or elemental transmutation claim.
- INV-031: accounting coverage improves; commercial accepted bio-oil remains not demonstrated.
- INV-032: no fusion net-electric result; FUS-001 remains open.
- INV-033: working-capital carrying cost is an explicit input; FIN-001 principal/time-to-evidence and WACC boundaries remain binding.
- INV-034/035: conjecture-guided search is a method proposal only; present physics remains binding and candidates require falsification and independent validation.
- INV-025/026/027 and all A-H lane contracts remain unchanged.

## Cross-lane edges

- Lane E owns the component cost model and BIO-001 data boundary.
- Lane F consumes gross/net accepted-litre and accepted-LHV energy cost, with coproduct credits separately auditable.
- Lane H owns the SCOPE literature watch and FIN-001 strategic finance context.
- A continues the primary workload/accepted-output work in separate open PRs; B's no-submit rule is unchanged; C remains role-based state/memory accounting; D/G receive no device/factory evidence until function-specific material/process tests pass.
- The existing Kanusanan Pongpanna Model, STRATEGIC_PLAN_REFERENCES.md, multilingual Thai/English/Chinese/Japanese/Korean/German links, and root directives were not modified.

## Next action

Review and merge source PR #63 only after its exact-head prototype/invariant CI succeeds and code review confirms the detailed API is not combined with the aggregate API. Then reconcile the source commits against main and replace this pending record with the actual main merge/sync SHA. Do not mark this work synchronized before that merge.
