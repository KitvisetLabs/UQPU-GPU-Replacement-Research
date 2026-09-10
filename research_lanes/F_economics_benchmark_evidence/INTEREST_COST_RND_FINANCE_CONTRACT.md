# Lane F — Interest-Cost / R&D-Finance Measurement Contract

**Parent:** `04_INTEREST_COST_AND_RND_FINANCE_STRATEGY.md` / INV-033  
**Status:** ACTIVE / MODEL + ACCOUNTING CONTRACT  
**Integration:** F + H with all technical lanes

## Required distinction

Two different claims must never be merged:

### Claim A — lower absolute interest expense
If the same loan rate/tenor applies, reducing financed principal directly reduces total nominal interest. This is arithmetic/accounting and can be measured from actual financing terms.

### Claim B — lower financing rate / WACC
A cheaper or less risky technology **may** attract a lower project spread or WACC, but that requires actual lender/investor terms or a clearly labeled risk model. It cannot be inferred from lower CAPEX/OPEX alone.

## FIN-001 record

For every major R&D/factory/infrastructure program collect:

```yaml
program_id:
evidence_milestone:
capital_committed:
debt_principal:
equity_committed:
base_rate:
project_credit_spread:
other_country_currency_risk_premium:
wacc:
loan_tenor_years:
construction_or_time_to_evidence_months:
interest_during_construction:
total_interest_expected_or_paid:
working_capital_financed:
accepted_evidence: true|false
failure_loss:
notes:
```

Unknown fields remain unknown rather than being imputed into measured evidence.

## Primary metrics

- financed principal per validated milestone;
- total interest per validated milestone;
- capital at risk per falsified hypothesis;
- months from capital commitment to usable evidence;
- financing cost per accepted useful service;
- sensitivity of total cost to base rate versus project-specific spread.

## Engineering feedback rule

If two technical designs provide equivalent accepted output, prefer the design with lower total lifecycle finance burden, not necessarily the lowest equipment sticker price. A more expensive component may be economically superior if it materially shortens construction, improves uptime/lifetime or reduces financed working capital.

## Software implementation

`software/uqpu-prototype/uqpu/energy_finance.py` provides capital-recovery and amortizing-loan functions for reproducible modeled comparisons. Model output remains MODEL_ONLY until inputs are tied to measured/evidenced financing terms.