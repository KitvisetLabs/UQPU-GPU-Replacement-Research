# Batch 044 — FND-007B3 Test-Harness Correction

**Status:** reproducibility correction discovered during pre-merge CI  
**Scope:** Batch 043 lattice-QED cross-check tests and Batch 044 quality-ledger tests

## Research Attribution

- Research Owner / Principal Investigator / Research Direction: **Kanutsanan Pongpanna**
- Facebook: https://www.facebook.com/LoveMoneyTH
- YouTube: https://www.youtube.com/@LoveMoneyTHOfficial
- AI Research Agent: **OpenAI GPT-5.6 Sol**
- AI-assisted contribution: CI failure diagnosis, test-discovery audit, unittest-native repair, reproducibility documentation and re-verification design.

Attribution reflects roles in this correction only.

## What failed

The first pre-merge Batch-044 CI run exposed a test-harness defect rather than a research-model failure:

1. `test_lattice_gauge_qudit_quality_ledger.py` imported `pytest`, but the repository's canonical CI command is `python -m unittest discover -s tests -v` and does not install pytest.
2. The audit then found a more important predecessor issue: Batch-043 `test_lattice_gauge_qudit_independent_crosscheck.py` used module-level bare `test_*` functions. `unittest discover` imported that module but did not execute those bare functions as `unittest.TestCase` methods.

Therefore, the earlier Batch-043 CI success established that the module imported cleanly and that the rest of the repository passed, but it did **not** execute the intended Batch-043 assertions. This correction narrows that earlier CI interpretation rather than hiding it.

## Repair

Both files were converted to native `unittest.TestCase` suites:

- no pytest dependency,
- every intended assertion is now discoverable by the repository's canonical unittest runner,
- parameter-like checks use loops plus `subTest`,
- invalid-input checks use `self.assertRaises`.

The repaired Batch-043 suite now actually executes checks for:

- 18-state projected-sector dimension,
- element-wise equality between the independent tensor-product Hamiltonian and the Batch-042 state-transition builder at five couplings,
- Jacobi eigenpair residuals,
- Batch-042 energy/observable/residual numerical envelope,
- spectrum ordering and ground-state normalization,
- evidence-boundary non-claims.

The repaired Batch-044 suite executes checks for:

- source-context constants,
- frozen resource counts,
- quality-survival monotonicity,
- break-even threshold values and cost equality,
- coherence-exposure arithmetic,
- finite-shot concentration arithmetic,
- heating-rate context,
- evidence-boundary falsifier/non-claims,
- invalid inputs.

## Evidence rule

Batch 043 should only be treated as having a CI-executed independent-cross-check test suite **after the repaired suite passes on the Batch-044 branch and again after merge to `main`**.

No physics result is changed by this correction. It changes the strength of the automated verification claim until re-execution closes the gap.

## Non-claims

This correction does not demonstrate real-QPU reproduction, quantum advantage, direct quark/QCD computing, universal qudit advantage, subsystem replacement, large economic savings, or new physical law.
