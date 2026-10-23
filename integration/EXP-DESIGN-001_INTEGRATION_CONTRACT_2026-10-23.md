# EXP-DESIGN-001 integration contract — 2026-10-23

**Literature source:** Ranković, Griffiths & Schwaller, Nature Machine Intelligence (2026-08-28), DOI 10.1038/s42256-026-01283-z  
**Primary owner:** Lane H — literature and experiment-design protocol  
**Lane F interface:** economics/evidence acceptance and resource accounting  
**Evidence class:** literature only; project evidence promotion = none

## Stable interface

Input: frozen candidate space, objective/constraints, initial observations, baseline versions, data split hashes, resource budget and stop criteria.

Output: candidate selection trace; uncertainty/calibration record; held-out score; top-5% coverage/regret; invalid/duplicate/out-of-space count; time/tokens/host compute/energy where measurable; and explicit evidence class. The same objective and budget must be used for every compared method. A generated recommendation never executes a physical experiment or provider job by itself.

## Active cross-lane edges

- A ↔ F: use identical useful-output and total-cost contracts; benchmark search cost separately from task success.
- A ↔ H: convert the published method into a falsifiable offline search protocol, not an assumed UQPU benefit.
- E ↔ F: later apply only to frozen MODEL_ONLY BIO-001/FUS-001 surrogates; keep feedstock/fuel/net-electric functions and complete lifecycle cost explicit.
- F ↔ H: measure time-to-evidence and capital-at-risk per validated milestone; do not infer a lower WACC.
- D ↔ G: reviewed but no coupling is justified yet because no accepted physical device or process requirement exists.
- B ↔ F: no provider activity occurred; future resource accounting must keep provider/target pricing and success probabilities matched.

All other cross-lane links are N/A for this result because no physical device, quantum provider, memory-service, vehicle-lift or validated material mechanism is involved. The all-pairs A–I review remains recorded in FND-QFI-001's integration contract; this article does not duplicate that ledger.

## Acceptance and falsification

Accept the method for further model-only study only if it improves a frozen held-out objective against the strongest baseline under matched candidate-evaluation and compute budgets, while calibration and invalid-proposal rates meet preregistered thresholds. Otherwise record the negative result. Do not promote to LAB_RESULT, commercial fuel/material/electricity evidence, quantum advantage, or new physical law.
