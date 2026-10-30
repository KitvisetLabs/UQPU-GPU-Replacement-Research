# FIN-001 hurdle-rate, financial-cost-of-capital and principal contract

**Date:** 2026-10-30  
**Primary owner:** Lane F  
**Publication/strategy interface:** Lane H  
**Evidence class:** SOFTWARE_CONTRACT + MODEL_ONLY_PREREGISTRATION until actual financing records are available

## Objective

Reduce financing burden through smaller required principal, shorter capital lock-up and earlier evidence while measuring actual interest and risk terms. Keep internal investment hurdle rates separate from debt coupons, financial cost of capital and WACC.

## Required ledger

For each project and financing tranche record:
- amount requested, committed, drawn and outstanding; date and purpose;
- debt coupon, fees, compounding, amortization and actual interest paid;
- equity contribution, capital structure and WACC calculation;
- internal hurdle rate and decision rule;
- risk-free rate, market premium, project/innovation premium and lender spread where identifiable;
- collateral, IP pledgeability, guarantees and covenants;
- working capital, construction/development duration and capital lock-up;
- evidence milestone dates, stage-gate decisions, continuation/termination and sunk cost;
- actual cashflows, realized project outcomes and uncertainty.

## Separate causal pathways

1. **Principal pathway:** at unchanged coupon, fees, term and repayment schedule, lower financed principal reduces absolute interest. Calculate from the actual debt schedule.
2. **Time pathway:** earlier evidence may reduce duration and amount of capital tied up. Measure dated drawdowns and release/termination decisions.
3. **Risk/WACC pathway:** risk reduction may change lender spreads, equity returns, pledgeability or WACC; estimate each separately and do not infer from principal reduction.
4. **Hurdle-rate pathway:** internal hurdle rates can diverge from the financial cost of capital because decision-makers price undiversifiable innovation risk or face pledgeability frictions. Record actual internal decision thresholds separately.

## Test protocol

- Reconstruct the actual project cashflow and debt schedule.
- Compute a fixed-terms counterfactual changing principal only.
- Compute a separate rate/risk counterfactual changing only the relevant rate parameter.
- Compare internal hurdle rate, debt coupon, WACC and realized return without substituting one for another.
- Measure whether earlier technical evidence changes principal, capital lock-up, project continuation or financing terms.
- Preserve failed projects and negative evidence; do not use survivor-only samples.

## Nonclaims

No UQPU project principal, interest, hurdle rate, WACC, risk premium or economy-wide rate has been measured or reduced. A working-paper mechanism is a research hypothesis, not a project financing result.


## 2026-10-30 — financing instrument-choice extension

Pan et al. (Journal of Corporate Finance 102, 103099; early online 2026-10-14; DOI 10.1016/j.jcorpfin.2026.103099) adds a literature-only instrument-choice layer. The model makes debt/equity/hybrid financing conditional on R&D risk, collateral/asset composition, cashflow and institutional quality, and reports a conditional subsidy-versus-guarantee result. No universal ranking is inferred. The full PDF and calibration were not independently audited.

Extend each FIN-001 financing event with instrument type, amount requested/committed/drawn/outstanding, coupon/fees, equity dilution/required return, collateral, guarantees/subsidies, cashflow, risk class, institutional context, milestone dates, time-to-evidence and failure/termination outcome. Compare instruments on identical accepted-milestone cashflows; validate instrument-choice predictions on held-out actual events. Report principal and absolute interest separately from hurdle rate, WACC and risk premium.
