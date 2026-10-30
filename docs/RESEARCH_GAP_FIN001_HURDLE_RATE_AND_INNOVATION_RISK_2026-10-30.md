# Research gap RG-FIN001-INNOVATION-RISK-PREMIUM-001 — hurdle rate, WACC and absolute interest separation

**Opened:** 2026-10-30  
**Primary owner:** Lane F — economics/benchmarks/evidence/energy economics/interest-finance/integration  
**Strategic/publication interface:** Lane H  
**Evidence class:** OFFICIAL WORKING PAPER / NO UQPU FINANCING DATA  
**Status:** HYPOTHESIS AND MEASUREMENT CONTRACT ONLY

## New source

Chikis, Goldberg and López-Salido, “The innovator’s risk premium: Sticky hurdle rates, the cost of capital, and creative destruction,” Banco de España Working Paper 2628, 2026-09-22. The official abstract describes a model in which firms' internal hurdle rates exceed financial cost of capital; undiversifiable innovation risk and imperfect pledgeability widen the gap. Higher innovation risk can lower the financial cost of capital while internal hurdle rates remain sticky or rise.

This is a working paper and calibrated theoretical result, not a measurement for KitvisetLabs or evidence that UQPU can lower WACC.

## Measurement contract

Record separate, dated variables for each financing tranche/project:
- required/financed principal, drawdown dates, outstanding balance and working capital;
- debt coupon, fees, amortization schedule, compounding convention and actual interest cashflows;
- equity cost and capital structure; WACC method and tax assumptions where relevant;
- internal hurdle rate used by decision-makers;
- market, project and innovation risk premiums, with the basis for each estimate;
- collateral, pledgeability of IP/innovation profits, guarantees and covenant constraints;
- construction/development duration, capital lock-up time and time-to-evidence;
- stage-gate decisions, continuation/termination, sunk-cost exposure and evidence dates;
- project cashflows, probability assumptions and risk-adjusted NPV, keeping MODEL_ONLY scenarios separate from realized financing.

## Causal hypotheses to test separately

- **H1 — principal:** reducing required or financed principal reduces absolute interest at unchanged coupon, fees, term and repayment schedule. Verify from actual cashflows; do not infer from a rate change.
- **H2 — time-to-evidence:** earlier credible evidence may shorten capital lock-up and reduce total financing needs; measure the time and cashflow path rather than assume a lower WACC.
- **H3 — risk premium/hurdle:** independently replicated technical evidence may affect internal hurdle rates, lender spreads, collateral/pledgeability or WACC differently. A change in one does not establish a change in the others.
- **H4 — continuation bias:** stage-gate discipline may reduce excess capital committed after negative evidence; measure termination timing and capital saved without assuming that a shorter project automatically has a lower risk premium.

## Falsifiable follow-up

1. Build a project-level FIN-001 ledger with actual tranches and dated evidence milestones.
2. Calculate interest under the observed debt schedule and a counterfactual with principal changed but all rate/term assumptions fixed.
3. Estimate WACC and internal hurdle rate independently from actual financing/decision records.
4. Test whether earlier evidence changes principal, lock-up duration, lender terms or only internal hurdle rates.
5. Replicate across multiple projects or financing events before generalizing.

## Nonclaims

No UQPU principal, absolute-interest, hurdle-rate, WACC, risk-premium or economy-wide interest-rate reduction is measured. Lower principal and lower rates remain distinct causal pathways.
