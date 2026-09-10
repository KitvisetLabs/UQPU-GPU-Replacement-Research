"""Energy and financing research utilities for the UQPU/Ketskaew Chulamani program.

These functions are accounting/model tools, not claims that a particular bio-oil or
fusion pathway has achieved the returned cost. Inputs must come from measured or
explicitly labeled modeled evidence.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite


HOURS_PER_YEAR = 8760.0


def _require_finite(name: str, value: float) -> float:
    value = float(value)
    if not isfinite(value):
        raise ValueError(f"{name} must be finite")
    return value


def _require_nonnegative(name: str, value: float) -> float:
    value = _require_finite(name, value)
    if value < 0:
        raise ValueError(f"{name} must be >= 0")
    return value


def _require_positive(name: str, value: float) -> float:
    value = _require_finite(name, value)
    if value <= 0:
        raise ValueError(f"{name} must be > 0")
    return value


def capital_recovery_factor(annual_rate: float, years: float) -> float:
    """Return the annual capital-recovery factor for a constant discount rate.

    A zero-rate project returns 1/years. Rates are decimal fractions, e.g. 0.08.
    """

    rate = _require_nonnegative("annual_rate", annual_rate)
    years = _require_positive("years", years)
    if rate == 0:
        return 1.0 / years
    growth = (1.0 + rate) ** years
    return rate * growth / (growth - 1.0)


@dataclass(frozen=True)
class BioOilCostInputs:
    """Inputs for a levelized saleable-liquid cost model.

    Currency is intentionally generic but must be internally consistent.
    `saleable_liters_per_dry_t` means final accepted liquid product after required
    stabilization/upgrading, not merely crude condensate yield.
    """

    dry_feedstock_t_per_year: float
    feedstock_cost_per_dry_t: float
    saleable_liters_per_dry_t: float
    capex: float
    fixed_om_per_year: float
    variable_process_cost_per_liter: float
    coproduct_credit_per_liter: float = 0.0
    annual_discount_rate: float = 0.08
    plant_life_years: float = 20.0


def bio_oil_levelized_cost_per_liter(inputs: BioOilCostInputs) -> float:
    """Compute modeled levelized cost per liter of accepted saleable liquid."""

    feedstock_t = _require_positive(
        "dry_feedstock_t_per_year", inputs.dry_feedstock_t_per_year
    )
    feedstock_cost = _require_nonnegative(
        "feedstock_cost_per_dry_t", inputs.feedstock_cost_per_dry_t
    )
    yield_lpt = _require_positive(
        "saleable_liters_per_dry_t", inputs.saleable_liters_per_dry_t
    )
    capex = _require_nonnegative("capex", inputs.capex)
    fixed_om = _require_nonnegative("fixed_om_per_year", inputs.fixed_om_per_year)
    variable = _require_nonnegative(
        "variable_process_cost_per_liter", inputs.variable_process_cost_per_liter
    )
    credit = _require_nonnegative(
        "coproduct_credit_per_liter", inputs.coproduct_credit_per_liter
    )

    annual_output_l = feedstock_t * yield_lpt
    annualized_capex = capex * capital_recovery_factor(
        inputs.annual_discount_rate, inputs.plant_life_years
    )
    annual_feedstock = feedstock_t * feedstock_cost
    fixed_cost_per_l = (annualized_capex + annual_feedstock + fixed_om) / annual_output_l
    return fixed_cost_per_l + variable - credit


def liquid_cost_per_gj(cost_per_liter: float, lower_heating_value_mj_per_liter: float) -> float:
    """Normalize a liquid cost to cost per GJ of lower-heating-value energy."""

    cost = _require_nonnegative("cost_per_liter", cost_per_liter)
    lhv = _require_positive(
        "lower_heating_value_mj_per_liter", lower_heating_value_mj_per_liter
    )
    return cost * 1000.0 / lhv


@dataclass(frozen=True)
class FusionElectricityCostInputs:
    """Inputs for a simple net-electric LCOE-like fusion plant model.

    `net_capacity_mw` must already be net of plant recirculating power. The model
    deliberately exposes capacity factor and financing because plasma gain alone is
    not an electricity-cost result.
    """

    net_capacity_mw: float
    capacity_factor: float
    capex: float
    fixed_om_per_year: float
    variable_om_per_mwh: float
    fuel_cycle_per_mwh: float = 0.0
    replacement_reserve_per_mwh: float = 0.0
    annual_discount_rate: float = 0.08
    plant_life_years: float = 30.0


def fusion_lcoe_per_mwh(inputs: FusionElectricityCostInputs) -> float:
    """Compute modeled cost per MWh of net delivered plant electricity."""

    capacity_mw = _require_positive("net_capacity_mw", inputs.net_capacity_mw)
    capacity_factor = _require_positive("capacity_factor", inputs.capacity_factor)
    if capacity_factor > 1.0:
        raise ValueError("capacity_factor must be <= 1")
    capex = _require_nonnegative("capex", inputs.capex)
    fixed_om = _require_nonnegative("fixed_om_per_year", inputs.fixed_om_per_year)
    variable_om = _require_nonnegative(
        "variable_om_per_mwh", inputs.variable_om_per_mwh
    )
    fuel_cycle = _require_nonnegative(
        "fuel_cycle_per_mwh", inputs.fuel_cycle_per_mwh
    )
    replacement = _require_nonnegative(
        "replacement_reserve_per_mwh", inputs.replacement_reserve_per_mwh
    )

    annual_net_mwh = capacity_mw * HOURS_PER_YEAR * capacity_factor
    annualized_capex = capex * capital_recovery_factor(
        inputs.annual_discount_rate, inputs.plant_life_years
    )
    fixed_per_mwh = (annualized_capex + fixed_om) / annual_net_mwh
    return fixed_per_mwh + variable_om + fuel_cycle + replacement


def amortizing_loan_payment(
    principal: float,
    annual_rate: float,
    years: float,
    payments_per_year: int = 12,
) -> float:
    """Return constant payment for a fully amortizing fixed-rate loan."""

    principal = _require_nonnegative("principal", principal)
    rate = _require_nonnegative("annual_rate", annual_rate)
    years = _require_positive("years", years)
    if payments_per_year <= 0:
        raise ValueError("payments_per_year must be > 0")

    periods = int(round(years * payments_per_year))
    if periods <= 0:
        raise ValueError("loan must have at least one payment period")
    if principal == 0:
        return 0.0
    if rate == 0:
        return principal / periods

    periodic_rate = rate / payments_per_year
    growth = (1.0 + periodic_rate) ** periods
    return principal * periodic_rate * growth / (growth - 1.0)


def amortizing_loan_total_interest(
    principal: float,
    annual_rate: float,
    years: float,
    payments_per_year: int = 12,
) -> float:
    """Return total nominal interest over a fixed-rate amortizing loan."""

    principal = _require_nonnegative("principal", principal)
    payment = amortizing_loan_payment(
        principal, annual_rate, years, payments_per_year=payments_per_year
    )
    periods = int(round(years * payments_per_year))
    return payment * periods - principal


def interest_savings_from_lower_principal(
    original_principal: float,
    reduced_principal: float,
    annual_rate: float,
    years: float,
    payments_per_year: int = 12,
) -> float:
    """Direct project-level interest saving when financing terms stay unchanged.

    This function intentionally does *not* infer a lower market interest rate from a
    cheaper technology. Any change in WACC/risk premium requires separate evidence.
    """

    original = _require_nonnegative("original_principal", original_principal)
    reduced = _require_nonnegative("reduced_principal", reduced_principal)
    if reduced > original:
        raise ValueError("reduced_principal must be <= original_principal")
    before = amortizing_loan_total_interest(
        original, annual_rate, years, payments_per_year=payments_per_year
    )
    after = amortizing_loan_total_interest(
        reduced, annual_rate, years, payments_per_year=payments_per_year
    )
    return before - after
