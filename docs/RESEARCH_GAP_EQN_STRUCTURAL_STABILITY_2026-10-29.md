# Research gap RG-EQN-STRUCTURAL-STABILITY-001 — numeric robustness and bounded equation search

**Opened:** 2026-10-29  
**Owner:** Lane A; evidence Lane F; publication Lane H  
**Status:** SOFTWARE DIAGNOSTIC ADDED / EXTERNAL REPRODUCTION OPEN / MODEL_ONLY  
**Sources:** https://proceedings.mlr.press/v306/yu26az.html and https://proceedings.mlr.press/v306/soubki26a.html

The ICML/PMLR sources motivate structural-stability checks beyond fit/complexity and explicit search-resource bounds. UQPU added software/uqpu-prototype/uqpu/equation_stability.py, a normalized output-L2-change/input-L2-change proxy using positive predeclared scales, with six synthetic test methods. It rejects invalid numeric inputs and inconsistent zero-input/nonzero-output records.

This is not the published EIC algorithm and does not establish structural rationality, physical truth or a new law.

**Unlock:** pin EIC revision/license/data; freeze known-law equation families and disjoint splits; compare fit-plus-complexity, EIC and the UQPU proxy under equal candidate/time/CPU/memory/precision budgets; include exact-recovery, null and ill-conditioned controls; report held-out error, constraint violations, numerical failures, false discoveries and cost per accepted candidate; repeat on an independent equation family.

**Next gate:** exact-head CI, then a pinned synthetic known-law benchmark. Do not promote a candidate because it has low fit error or low sensitivity alone.


## Source-code provenance audit — 2026-10-29

The official EIC code repository is pinned to main/tree commit 6e3abfcc308f2c71292abfa683ffb404412d022a, dated 2026-03-31. GitHub repository metadata reports license=null, and no root-level LICENSE/COPYING file was found. The repository tree contains nested licenses for PMLB data and third-party subprojects, which do not establish reuse rights for EIC-specific code. The README also reports corrected PySR noise-call and CPU-time comparisons. UQPU did not copy, vendor or execute this code.

A deterministic synthetic fixture now checks a known cancellation failure between algebraically equivalent forms using an 80-digit Decimal intermediate and the UQPU normalized perturbation proxy. This is MODEL_ONLY numeric evidence. The official EIC comparison arm remains blocked until reuse rights/permission and source/data/environment provenance are resolved.

See docs/BATCH_127_EIC_REPRODUCTION_PREFLIGHT.md, research_lanes/A_quantum_programming_runtime/EQUATION_STABILITY_KNOWN_LAW_BENCHMARK_V1.json and integration/DAILY_CYCLE_2026-10-29_EIC_REPRODUCTION_PREFLIGHT.md.

