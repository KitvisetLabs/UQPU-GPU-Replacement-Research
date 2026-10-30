# FIN-001 contract — separate credit-availability and interest-rate stress

**Stable ID:** FIN-001-CREDIT-SUPPLY-STRESS-001  
**Primary owner:** Lane F — project economics and financing evidence  
**Interfaces:** E (BIO/FUS project CAPEX/OPEX), H (strategic finance), A/C (ledger/runtime evidence)  
**Opened:** 2026-10-30  
**Status:** MODEL_ONLY / COUNTERPARTY_TERMS_NOT_OBTAINED  
**Source:** Pragati Priya, *Emerging Markets Review* (2026), DOI 10.1016/j.ememar.2026.101479, https://doi.org/10.1016/j.ememar.2026.101479  
**Related:** INV-033; FIN-001; BIO-001; FUS-001.

## Objective

Measure how a project milestone plan responds separately to (1) changes in interest rate and (2) changes in the availability/timing/conditions of credit. Do not conflate these mechanisms.

## Source boundary

The 2026 *Emerging Markets Review* paper reports stronger sensitivity of R&D-intensive Indian firms to monetary tightening and bank credit-supply shocks using 2002–2024 firm-level data. Full publisher text and coefficient tables were not retrievable in this cycle. Its estimates are not Thailand-specific, not UQPU-project estimates and do not establish a project WACC change.

## Required financing ledger

For every milestone/tranche record:
- required principal and committed amount;
- drawdown schedule and actual disbursement date;
- interest rate, benchmark, spread, fees, compounding and currency;
- maturity, grace period, amortization and refinancing date;
- collateral, covenants, guarantees and withdrawal conditions;
- working-capital need and cash-burn profile;
- evidence acceptance gate, planned and actual time-to-evidence;
- delay probability, delay duration and cash-flow consequence;
- equity/debt/grant mix and contingency capital;
- project risk and counterparty source for every term.

## Three separate stress scenarios

1. **Rate-only:** hold committed principal, drawdown dates and credit availability fixed; vary rate/spread/refinancing assumptions. Report incremental interest and debt-service coverage.
2. **Credit-only:** hold contractual interest rates fixed; vary committed limits, delayed drawdown, reduced availability, covenant tightening, collateral requirements and lender withdrawal. Report principal shortfall, milestone delay, working-capital gap and time-to-evidence.
3. **Joint:** combine rate and credit shocks with an explicitly stated dependence assumption. Do not add independent shock probabilities without evidence.

Keep a baseline case with actual counterparty terms when available. Until then, label all inputs MODEL_ONLY and run sensitivity ranges rather than claiming expected financing costs.

## Required outputs

- financed principal by milestone and in total;
- absolute interest paid at unchanged terms;
- interest change under rate-only stress;
- principal shortfall and delayed-capital duration under credit-only stress;
- working capital and cash runway;
- delay to accepted evidence and capital lock-up time;
- risk/uncertainty ranges and probability source;
- cost per validated milestone and total lifecycle financing cost.

## Invariant interpretation

A lower required principal directly reduces absolute interest at unchanged terms. Lowering the interest rate, lender spread, project risk premium, WACC or economy-wide policy rate is a separate causal claim requiring actual financing offers/transactions or appropriate empirical evidence. A literature coefficient from Indian R&D-intensive firms cannot be used as a project rate.

## Falsifiers / stop conditions

Reject a claimed finance improvement if it only moves principal between entities, excludes fees/working capital, double-counts grants/coproducts, ignores delayed drawdown, or attributes lower WACC to lower principal without separate evidence. Reject an assumed credit-supply benefit if lender commitment, covenants and drawdown are not documented.

## Current result

No UQPU financing offer, credit line, debt drawdown, project WACC or interest saving was measured. This is a ledger and stress-test contract only. See `docs/literature_watch/2026-10-30-biomass-scwl-and-rd-credit-supply.md`.
