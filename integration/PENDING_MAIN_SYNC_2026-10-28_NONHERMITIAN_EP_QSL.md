# Pending-main synchronization — FND003 non-Hermitian exceptional-point QSL cycle

**Record date:** 2026-10-28  
**Status:** PENDING REVIEW / SOURCE WORK NOT YET ON MAIN  
**Canonical main SHA at source start:** `b3252a556b61b7e566d5e057606c1f2e917d79e8`  
**Source PR:** [#146 — FND003: non-Hermitian exceptional-point speedup with accepted-output accounting](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/pull/146)  
**Source branch:** `research/2026-10-28-nonhermitian-ep-qsl`  
**Source head:** `fbd797fc5e25922da0b55e84aa947599a4d6eadb`  
**Work item:** `FND003-NH-EP-001`; `RG-FND003-NH-EP-001`; `INT-20261028-FND003-NH-EP-001`

## Source commits mapped for reconciliation

- `8e043a70164c2f509db783b3c5787b3b5def399e` — official APS literature watch.
- `971bb8e01714d06e8b848927f4df9bf68d3747d9` — focused gap.
- `b5b8d094b3318fa23a25fa409b065f86cfa1b24f` — Batch 095.
- `bb251a39de3e450a08abf836a07e3ca0d6109724` — integration report.
- `e21057511ecce464c16465070eeaf81923942d88` — machine-readable integration record.
- `0bc47e325d105855f2e2e97859312dbb689b77b2` — README cycle index.
- `fbd797fc5e25922da0b55e84aa947599a4d6eadb` — related FND-003 gap link.

## Summary of pending source work

The source PR adds a Lane H literature watch for two *Physical Review Letters* sources published 2026-05-28: a trapped-ion exceptional-point experiment reporting faster entanglement generation relative to an equivalent Hermitian interaction with a success-probability trade-off, and a transition-rate/QSL framework for open processes including measurements. It adds a falsifiable Lane A follow-up that requires matched initial/target states and control budgets, complete open-system accounting, held-out perturbations and total time/energy/cost per accepted output.

This is **literature plus a preregistered gap only**. No UQPU reproduction, new physical law, universal QSL violation, QPU advantage, material substitution, accepted bio-oil, net fusion electricity, financing/WACC improvement or Data-Center-to-One-Phone milestone is claimed.

## CI and review status at record creation

- Source PR #146 exact-head workflow run: [run 40630888102](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40630888102), **IN PROGRESS** at record creation. The three Python 3.10/3.11/3.12 jobs were executing unit/invariant tests; later smoke and benchmark steps were pending.
- Do not merge the source PR until its required exact-head checks and review complete.
- This pending-main record does not assert that any source artifact above exists on canonical main.

## Files expected after source merge

- `docs/literature_watch/2026-10-28-nonhermitian-ep-speedup-and-transition-rate-qsl.md`
- `docs/RESEARCH_GAP_FND003_NONHERMITIAN_EP_2026-10-28.md`
- `docs/BATCH_095_NONHERMITIAN_EP_QSL_ACCEPTED_TASK_GATE.md`
- `integration/DAILY_CYCLE_2026-10-28_NONHERMITIAN_EP_QSL.md`
- `integration/INT-20261028-FND003-NH-EP-001.json`
- README cycle summary and a link from the existing FND-003 QSL gap.

## Permanent invariants and next step

INV-025/026/027 and INV-029–035 remain preserved. Root directives 00, 00A and 01–06, the Kanusanan Pongpanna Model, six-language public plan references, and strategic AI-agent/funding references remain untouched. Large append-only `WORKLOG.md` and `RESEARCH_GAPS.md` were not overwritten.

**Next step:** complete source PR CI/review, merge only when authorized, then reconcile every source SHA to the resulting main SHA and safely append the worklog/gap history in a follow-up.