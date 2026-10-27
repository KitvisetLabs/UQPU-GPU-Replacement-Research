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



_BIO_OIL_INPUT_EVIDENCE_CLASSES = {
    "MODEL_ONLY",
    "LITERATURE_ONLY",
    "LAB_MEASURED",
    "PUBLISHED_EXPERIMENT",
    "PRODUCTION_DATA",
}


def simple_interest_for_capital_lockup(
    principal: float, annual_rate: float, lockup_days: int
) -> float:
    """Simple interest accrued during an evidence/development capital lock-up.

    This is a separate FIN-001 quantity. It must not be added to plant capital
    recovery if the same financed principal is already included in plant CAPEX.
    """
    principal = _require_nonnegative("principal", principal)
    annual_rate = _require_nonnegative("annual_rate", annual_rate)
    if (
        not isinstance(lockup_days, int)
        or isinstance(lockup_days, bool)
        or lockup_days < 0
    ):
        raise ValueError("lockup_days must be a nonnegative integer")
    return principal * annual_rate * lockup_days / 365.0


@dataclass(frozen=True)
class BioOilBatchCostInputs:
    """Batch-level cost contract for final accepted liquid fuel, not crude oil.

    All cost inputs are in one consistent currency (field names use USD).
    Feedstock price and preprocessing are per wet tonne; yield is calculated on
    dry feedstock mass. Plant CAPEX is annualized with a capital-charge rate
    and allocated by this batch's wet-feedstock throughput. R&D/evidence
    principal is separate and must be excluded from plant CAPEX if provided.

    A coproduct credit must name disjoint coproduct streams and already be net
    of their incremental recovery, upgrading, transport and disposal costs.
    Zero means no credit is claimed; unknown costs must not be entered as zero.
    """

    batch_id: str
    provenance_ids: tuple[str, ...]
    source_evidence_class: str
    wet_feedstock_kg: float
    moisture_fraction: float
    feedstock_cost_usd_per_wet_tonne: float
    preprocessing_cost_usd_per_wet_tonne: float
    logistics_cost_usd: float
    raw_bio_oil_kg: float
    accepted_liquid_kg: float
    accepted_liquid_lhv_mj_per_kg: float
    acceptance_passed: bool
    acceptance_spec_sha256: str
    hydrogen_kg: float
    hydrogen_cost_usd_per_kg: float
    catalyst_cost_usd: float
    utility_cost_usd: float
    other_opex_usd: float
    plant_capex_usd: float
    annual_nameplate_feedstock_kg: float
    capacity_factor: float
    plant_life_years: float
    annual_capital_charge_rate: float
    rnd_financed_principal_usd: float = 0.0
    rnd_annual_interest_rate: float = 0.0
    rnd_lockup_days: int = 0
    rnd_interest_allocation_fraction: float = 0.0
    rnd_principal_excluded_from_plant_capex: bool = True
    accepted_stream_id: str = "accepted-liquid"
    coproduct_stream_ids: tuple[str, ...] = ()
    coproduct_net_credit_usd: float = 0.0
    coproduct_credits_net_of_incremental_costs: bool = False
    product_density_kg_per_litre: float | None = None
    feedstock_lhv_mj_per_dry_kg: float | None = None
    utility_electricity_kwh: float | None = None
    utility_process_heat_mj: float | None = None


@dataclass(frozen=True)
class BioOilBatchCostResult:
    """Calculated cost and yield fields; the result remains MODEL_ONLY."""

    batch_id: str
    dry_feedstock_kg: float
    raw_liquid_mass_yield_kg_per_dry_kg: float
    accepted_liquid_mass_yield_kg_per_dry_kg: float | None
    feedstock_cost_usd: float
    preprocessing_cost_usd: float
    logistics_cost_usd: float
    hydrogen_cost_usd: float
    catalyst_cost_usd: float
    utility_cost_usd: float
    other_opex_usd: float
    operating_cost_usd: float
    annualized_capex_usd: float
    allocated_capital_recovery_usd: float
    rnd_interest_total_usd: float
    allocated_rnd_interest_usd: float
    coproduct_net_credit_usd: float
    precredit_batch_cost_usd: float
    net_batch_cost_usd: float
    accepted_fuel_energy_mj: float
    accepted_liters: float | None
    cost_usd_per_accepted_mj: float | None
    cost_usd_per_accepted_gj: float | None
    cost_usd_per_accepted_liter: float | None
    feedstock_energy_mj: float | None
    utility_energy_mj: float | None
    input_evidence_class: str
    result_evidence_class: str
    coproduct_credit_exceeds_precredit_cost: bool


def bio_oil_batch_cost(inputs: BioOilBatchCostInputs) -> BioOilBatchCostResult:
    """Calculate a fail-closed, batch-level accepted-fuel cost scenario.

    A rejected batch contributes zero accepted fuel energy. Cost/MJ and cost/L
    are then None, never a divide-by-zero or an implied saleable-fuel result.
    The output is always MODEL_ONLY: this calculator does not authenticate
    source data, certify fuel specifications, or demonstrate commercial economics.
    """

    if not isinstance(inputs.batch_id, str) or not inputs.batch_id.strip():
        raise ValueError("batch_id is required")
    if (
        not isinstance(inputs.provenance_ids, tuple)
        or not inputs.provenance_ids
        or any(not isinstance(item, str) or not item.strip() for item in inputs.provenance_ids)
        or len(set(inputs.provenance_ids)) != len(inputs.provenance_ids)
    ):
        raise ValueError("provenance_ids must be a nonempty tuple of unique identifiers")
    if inputs.source_evidence_class not in _BIO_OIL_INPUT_EVIDENCE_CLASSES:
        raise ValueError("source_evidence_class is not recognized")
    if not isinstance(inputs.acceptance_passed, bool):
        raise ValueError("acceptance_passed must be a boolean")
    if not isinstance(inputs.rnd_principal_excluded_from_plant_capex, bool):
        raise ValueError("rnd_principal_excluded_from_plant_capex must be a boolean")
    if not isinstance(inputs.acceptance_spec_sha256, str) or (
        len(inputs.acceptance_spec_sha256) != 64
        or any(ch not in "0123456789abcdef" for ch in inputs.acceptance_spec_sha256)
    ):
        raise ValueError("acceptance_spec_sha256 must be a lowercase SHA-256 digest")

    wet_feedstock_kg = _require_positive("wet_feedstock_kg", inputs.wet_feedstock_kg)
    moisture = _require_nonnegative("moisture_fraction", inputs.moisture_fraction)
    if moisture >= 1.0:
        raise ValueError("moisture_fraction must be < 1")
    dry_feedstock_kg = wet_feedstock_kg * (1.0 - moisture)

    feedstock_price = _require_nonnegative(
        "feedstock_cost_usd_per_wet_tonne", inputs.feedstock_cost_usd_per_wet_tonne
    )
    preprocessing_price = _require_nonnegative(
        "preprocessing_cost_usd_per_wet_tonne",
        inputs.preprocessing_cost_usd_per_wet_tonne,
    )
    logistics = _require_nonnegative("logistics_cost_usd", inputs.logistics_cost_usd)
    raw_oil_kg = _require_nonnegative("raw_bio_oil_kg", inputs.raw_bio_oil_kg)
    accepted_liquid_kg = _require_nonnegative(
        "accepted_liquid_kg", inputs.accepted_liquid_kg
    )
    product_lhv = _require_positive(
        "accepted_liquid_lhv_mj_per_kg", inputs.accepted_liquid_lhv_mj_per_kg
    )
    if not inputs.acceptance_passed and accepted_liquid_kg > 0:
        raise ValueError("rejected batches must have accepted_liquid_kg == 0")

    hydrogen_kg = _require_nonnegative("hydrogen_kg", inputs.hydrogen_kg)
    hydrogen_price = _require_nonnegative(
        "hydrogen_cost_usd_per_kg", inputs.hydrogen_cost_usd_per_kg
    )
    catalyst = _require_nonnegative("catalyst_cost_usd", inputs.catalyst_cost_usd)
    utilities = _require_nonnegative("utility_cost_usd", inputs.utility_cost_usd)
    other_opex = _require_nonnegative("other_opex_usd", inputs.other_opex_usd)
    capex = _require_nonnegative("plant_capex_usd", inputs.plant_capex_usd)
    annual_capacity = _require_positive(
        "annual_nameplate_feedstock_kg", inputs.annual_nameplate_feedstock_kg
    )
    capacity_factor = _require_positive("capacity_factor", inputs.capacity_factor)
    if capacity_factor > 1.0:
        raise ValueError("capacity_factor must be <= 1")
    life = _require_positive("plant_life_years", inputs.plant_life_years)
    capital_rate = _require_nonnegative(
        "annual_capital_charge_rate", inputs.annual_capital_charge_rate
    )

    rnd_principal = _require_nonnegative(
        "rnd_financed_principal_usd", inputs.rnd_financed_principal_usd
    )
    rnd_rate = _require_nonnegative(
        "rnd_annual_interest_rate", inputs.rnd_annual_interest_rate
    )
    if (
        not isinstance(inputs.rnd_lockup_days, int)
        or isinstance(inputs.rnd_lockup_days, bool)
        or inputs.rnd_lockup_days < 0
    ):
        raise ValueError("rnd_lockup_days must be a nonnegative integer")
    allocation = _require_nonnegative(
        "rnd_interest_allocation_fraction", inputs.rnd_interest_allocation_fraction
    )
    if allocation > 1.0:
        raise ValueError("rnd_interest_allocation_fraction must be <= 1")
    if rnd_principal > 0 and not inputs.rnd_principal_excluded_from_plant_capex:
        raise ValueError("R&D principal must be excluded from plant CAPEX to avoid double counting")

    if not isinstance(inputs.accepted_stream_id, str) or not inputs.accepted_stream_id.strip():
        raise ValueError("accepted_stream_id is required")
    coproduct_ids = inputs.coproduct_stream_ids
    if (
        not isinstance(coproduct_ids, tuple)
        or any(not isinstance(item, str) or not item.strip() for item in coproduct_ids)
        or len(set(coproduct_ids)) != len(coproduct_ids)
    ):
        raise ValueError("coproduct_stream_ids must be a tuple of unique nonempty identifiers")
    if inputs.accepted_stream_id in coproduct_ids:
        raise ValueError("accepted liquid stream cannot also be credited as a coproduct")
    coproduct_credit = _require_nonnegative(
        "coproduct_net_credit_usd", inputs.coproduct_net_credit_usd
    )
    if coproduct_credit > 0 and (
        not coproduct_ids or not inputs.coproduct_credits_net_of_incremental_costs
    ):
        raise ValueError(
            "coproduct credits require disjoint stream IDs and net incremental-cost accounting"
        )

    density = inputs.product_density_kg_per_litre
    if density is not None:
        density = _require_positive("product_density_kg_per_litre", density)
    feedstock_lhv = inputs.feedstock_lhv_mj_per_dry_kg
    if feedstock_lhv is not None:
        feedstock_lhv = _require_positive(
            "feedstock_lhv_mj_per_dry_kg", feedstock_lhv
        )
    electricity_kwh = inputs.utility_electricity_kwh
    if electricity_kwh is not None:
        electricity_kwh = _require_nonnegative(
            "utility_electricity_kwh", electricity_kwh
        )
    process_heat_mj = inputs.utility_process_heat_mj
    if process_heat_mj is not None:
        process_heat_mj = _require_nonnegative(
            "utility_process_heat_mj", process_heat_mj
        )

    wet_tonnes = wet_feedstock_kg / 1000.0
    feedstock_cost = wet_tonnes * feedstock_price
    preprocessing_cost = wet_tonnes * preprocessing_price
    hydrogen_cost = hydrogen_kg * hydrogen_price
    operating_cost = (
        feedstock_cost
        + preprocessing_cost
        + logistics
        + hydrogen_cost
        + catalyst
        + utilities
        + other_opex
    )
    annualized_capex = capex * capital_recovery_factor(capital_rate, life)
    annual_actual_feedstock_kg = annual_capacity * capacity_factor
    allocated_capital_recovery = (
        annualized_capex * wet_feedstock_kg / annual_actual_feedstock_kg
    )
    rnd_interest_total = simple_interest_for_capital_lockup(
        rnd_principal, rnd_rate, inputs.rnd_lockup_days
    )
    allocated_rnd_interest = rnd_interest_total * allocation
    precredit_cost = operating_cost + allocated_capital_recovery + allocated_rnd_interest
    net_cost = precredit_cost - coproduct_credit

    accepted_energy = (
        accepted_liquid_kg * product_lhv if inputs.acceptance_passed else 0.0
    )
    accepted_liters = (
        accepted_liquid_kg / density
        if density is not None and accepted_energy > 0
        else None
    )
    cost_per_mj = net_cost / accepted_energy if accepted_energy > 0 else None
    cost_per_gj = cost_per_mj * 1000.0 if cost_per_mj is not None else None
    cost_per_liter = (
        net_cost / accepted_liters if accepted_liters is not None else None
    )
    feedstock_energy = (
        dry_feedstock_kg * feedstock_lhv if feedstock_lhv is not None else None
    )
    utility_energy = (
        electricity_kwh * 3.6 + process_heat_mj
        if electricity_kwh is not None and process_heat_mj is not None
        else None
    )

    return BioOilBatchCostResult(
        batch_id=inputs.batch_id,
        dry_feedstock_kg=dry_feedstock_kg,
        raw_liquid_mass_yield_kg_per_dry_kg=raw_oil_kg / dry_feedstock_kg,
        accepted_liquid_mass_yield_kg_per_dry_kg=(
            accepted_liquid_kg / dry_feedstock_kg if accepted_energy > 0 else None
        ),
        feedstock_cost_usd=feedstock_cost,
        preprocessing_cost_usd=preprocessing_cost,
        logistics_cost_usd=logistics,
        hydrogen_cost_usd=hydrogen_cost,
        catalyst_cost_usd=catalyst,
        utility_cost_usd=utilities,
        other_opex_usd=other_opex,
        operating_cost_usd=operating_cost,
        annualized_capex_usd=annualized_capex,
        allocated_capital_recovery_usd=allocated_capital_recovery,
        rnd_interest_total_usd=rnd_interest_total,
        allocated_rnd_interest_usd=allocated_rnd_interest,
        coproduct_net_credit_usd=coproduct_credit,
        precredit_batch_cost_usd=precredit_cost,
        net_batch_cost_usd=net_cost,
        accepted_fuel_energy_mj=accepted_energy,
        accepted_liters=accepted_liters,
        cost_usd_per_accepted_mj=cost_per_mj,
        cost_usd_per_accepted_gj=cost_per_gj,
        cost_usd_per_accepted_liter=cost_per_liter,
        feedstock_energy_mj=feedstock_energy,
        utility_energy_mj=utility_energy,
        input_evidence_class=inputs.source_evidence_class,
        result_evidence_class="MODEL_ONLY",
        coproduct_credit_exceeds_precredit_cost=coproduct_credit > precredit_cost,
    )


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
