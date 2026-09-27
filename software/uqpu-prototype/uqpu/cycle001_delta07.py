"""Cycle-001 Delta-07: synchronized research contracts and explicit unknowns.

These ledgers organize tests and future measurements. Their default records do
not contain empirical results or authorize paid/provider/hardware activity.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import math
import re
from typing import Optional

from .scm_replication_contract import ReplicationManifest, validate_manifest, verify_dataset

_SHA256 = re.compile(r"^[0-9a-fA-F]{64}$")


@dataclass(frozen=True)
class IsingClassicalLedger:
    case_id: str
    instance_sha256: str
    output_contract_id: str
    epsilon: float
    confidence: float
    solver: str
    hardware: str
    wall_seconds: Optional[float] = None
    energy_joules: Optional[float] = None
    peak_memory_bytes: Optional[int] = None
    cost_usd: Optional[float] = None
    evidence_class: str = "TEMPLATE_NOT_EXECUTION_EVIDENCE"


@dataclass(frozen=True)
class IsingQuantumLedger:
    case_id: str
    instance_sha256: str
    output_contract_id: str
    epsilon: float
    confidence: float
    estimator: str
    provider: str
    backend: str
    state_prep_seconds: Optional[float] = None
    sampling_shots: Optional[int] = None
    readout_seconds: Optional[float] = None
    postprocess_seconds: Optional[float] = None
    energy_joules: Optional[float] = None
    cost_usd: Optional[float] = None
    evidence_class: str = "TEMPLATE_NOT_EXECUTION_EVIDENCE"


def ising_pair_template() -> tuple[IsingClassicalLedger, IsingQuantumLedger]:
    common = dict(
        case_id="OBS-ISING-ENERGY-001",
        instance_sha256="",
        output_contract_id="ising-energy-epsilon-0.01-confidence-0.95",
        epsilon=0.01,
        confidence=0.95,
    )
    classical = IsingClassicalLedger(
        **common,
        solver="competitive exact/tensor/sampling baseline selected by instance structure",
        hardware="CPU/GPU class and version required",
    )
    quantum = IsingQuantumLedger(
        **common,
        estimator="QOS/QSVT or other estimator; state preparation and all shots charged",
        provider="provider required before execution",
        backend="backend required before execution",
    )
    return classical, quantum


def validate_ising_comparison(
    classical: IsingClassicalLedger, quantum: IsingQuantumLedger
) -> tuple[str, ...]:
    errors: list[str] = []
    for name in ("case_id", "instance_sha256", "output_contract_id", "epsilon", "confidence"):
        a, b = getattr(classical, name), getattr(quantum, name)
        if a != b:
            errors.append(f"mismatch:{name}")
    if not classical.case_id.strip():
        errors.append("missing:case_id")
    if not classical.instance_sha256:
        errors.append("missing:instance_sha256")
    elif not _SHA256.fullmatch(classical.instance_sha256):
        errors.append("invalid:instance_sha256")
    if not classical.output_contract_id.strip():
        errors.append("missing:output_contract_id")
    if not math.isfinite(classical.epsilon) or classical.epsilon <= 0:
        errors.append("invalid:epsilon")
    if not math.isfinite(classical.confidence) or not 0 < classical.confidence < 1:
        errors.append("invalid:confidence")
    for prefix, ledger, names in (
        ("classical", classical, ("wall_seconds", "energy_joules", "cost_usd", "peak_memory_bytes")),
        ("quantum", quantum, ("state_prep_seconds", "sampling_shots", "readout_seconds", "postprocess_seconds", "energy_joules", "cost_usd")),
    ):
        for name in names:
            value = getattr(ledger, name)
            if value is not None and (not math.isfinite(value) or value < 0):
                errors.append(f"invalid:{prefix}.{name}")
    if not classical.solver.strip():
        errors.append("missing:classical.solver")
    if not classical.hardware.strip():
        errors.append("missing:classical.hardware")
    if not quantum.estimator.strip():
        errors.append("missing:quantum.estimator")
    for prefix, ledger, names in (
        ("classical", classical, ("wall_seconds", "energy_joules", "cost_usd")),
        ("quantum", quantum, ("state_prep_seconds", "sampling_shots", "readout_seconds", "postprocess_seconds", "energy_joules", "cost_usd")),
    ):
        if ledger.evidence_class == "MEASURED" and any(getattr(ledger, n) is None for n in names):
            errors.append(f"incomplete_measured:{prefix}")
    return tuple(errors)


def ising_missing_resources(
    classical: IsingClassicalLedger, quantum: IsingQuantumLedger
) -> tuple[str, ...]:
    fields = []
    if not classical.instance_sha256:
        fields.append("shared.instance_sha256")
    for name in ("wall_seconds", "energy_joules", "cost_usd"):
        if getattr(classical, name) is None:
            fields.append(f"classical.{name}")
    for name in ("state_prep_seconds", "sampling_shots", "readout_seconds", "postprocess_seconds", "energy_joules", "cost_usd"):
        if getattr(quantum, name) is None:
            fields.append(f"quantum.{name}")
    return tuple(fields)


@dataclass(frozen=True)
class BosonicMemoryResourceLedger:
    case_id: str
    source_record_id: str
    logical_task: str
    encoding: str
    target_logical_error_rate: Optional[float] = None
    target_retention_cycles: Optional[int] = None
    observed_logical_error_rate: Optional[float] = None
    observed_retention_cycles: Optional[int] = None
    oscillator_count: Optional[int] = None
    ancilla_count: Optional[int] = None
    state_prep_seconds: Optional[float] = None
    stabilization_seconds_per_cycle: Optional[float] = None
    readout_seconds: Optional[float] = None
    decoder_seconds: Optional[float] = None
    energy_joules: Optional[float] = None
    cost_usd: Optional[float] = None
    evidence_class: str = "LITERATURE_ANCHORED_RESOURCE_TEMPLATE"


def bosonic_memory_template() -> BosonicMemoryResourceLedger:
    return BosonicMemoryResourceLedger(
        case_id="FND-BOSONIC-QEC-001",
        source_record_id="docs/CYCLE_001_DELTA_05_LITERATURE_SNAPSHOT_BIOMASS_EMI_BOSONIC_QEC_2026-09-28.md",
        logical_task="matched logical-memory function; contract and target must be frozen",
        encoding="cat/GKP candidate; select one platform before reproduction",
    )


def validate_bosonic_memory(x: BosonicMemoryResourceLedger) -> tuple[str, ...]:
    errors: list[str] = []
    for name in ("case_id", "source_record_id", "logical_task", "encoding"):
        if not getattr(x, name).strip():
            errors.append(f"missing:{name}")
    if x.target_logical_error_rate is not None and not 0 < x.target_logical_error_rate < 1:
        errors.append("invalid:target_logical_error_rate")
    if x.target_retention_cycles is not None and x.target_retention_cycles <= 0:
        errors.append("invalid:target_retention_cycles")
    if x.observed_logical_error_rate is not None and not 0 <= x.observed_logical_error_rate <= 1:
        errors.append("invalid:observed_logical_error_rate")
    if x.observed_retention_cycles is not None and x.observed_retention_cycles < 0:
        errors.append("invalid:observed_retention_cycles")
    for name in ("oscillator_count", "ancilla_count", "state_prep_seconds", "stabilization_seconds_per_cycle", "readout_seconds", "decoder_seconds", "energy_joules", "cost_usd"):
        value = getattr(x, name)
        if value is not None and (not math.isfinite(value) or value < 0):
            errors.append(f"invalid:{name}")
    if x.evidence_class == "MEASURED" and bosonic_missing_resources(x):
        errors.append("incomplete_measured:bosonic_resource_ledger")
    return tuple(errors)


def bosonic_missing_resources(x: BosonicMemoryResourceLedger) -> tuple[str, ...]:
    required = (
        "target_logical_error_rate", "target_retention_cycles",
        "observed_logical_error_rate", "observed_retention_cycles", "oscillator_count",
        "ancilla_count", "state_prep_seconds", "stabilization_seconds_per_cycle",
        "readout_seconds", "decoder_seconds", "energy_joules", "cost_usd",
    )
    return tuple(name for name in required if getattr(x, name) is None)


@dataclass(frozen=True)
class PangolaCouponResult:
    case_id: str
    feedstock_lot: str
    incumbent_id: str
    process_recipe_id: str
    test_method: str
    min_frequency_hz: Optional[float] = None
    max_frequency_hz: Optional[float] = None
    thickness_mm: Optional[float] = None
    areal_density_kg_m2: Optional[float] = None
    conductivity_s_per_m: Optional[float] = None
    shielding_curve_db: tuple[tuple[float, float], ...] = ()
    thermal_stability_c: Optional[float] = None
    mechanical_strength_mpa: Optional[float] = None
    process_yield_fraction: Optional[float] = None
    energy_mj: Optional[float] = None
    chemical_mass_g: Optional[float] = None
    cost_thb: Optional[float] = None
    evidence_class: str = "TEMPLATE_NO_MEASUREMENTS"


def pangola_coupon_result_template() -> PangolaCouponResult:
    return PangolaCouponResult(
        case_id="DMF-BIOCARBON-EMI-001",
        feedstock_lot="",
        incumbent_id="",
        process_recipe_id="",
        test_method="",
    )


def validate_coupon_result(x: PangolaCouponResult) -> tuple[str, ...]:
    errors: list[str] = []
    if x.case_id != "DMF-BIOCARBON-EMI-001":
        errors.append("invalid:case_id")
    if x.min_frequency_hz is not None and (not math.isfinite(x.min_frequency_hz) or x.min_frequency_hz <= 0):
        errors.append("invalid:min_frequency_hz")
    if x.max_frequency_hz is not None and (not math.isfinite(x.max_frequency_hz) or (x.min_frequency_hz is not None and x.max_frequency_hz <= x.min_frequency_hz)):
        errors.append("invalid:max_frequency_hz")
    for name in ("thickness_mm", "areal_density_kg_m2", "conductivity_s_per_m", "thermal_stability_c", "mechanical_strength_mpa", "process_yield_fraction", "energy_mj", "chemical_mass_g", "cost_thb"):
        value = getattr(x, name)
        if value is not None and not math.isfinite(value):
            errors.append(f"invalid:{name}")
        if value is not None and name != "thermal_stability_c" and value < 0:
            errors.append(f"invalid:{name}")
    if x.process_yield_fraction is not None and x.process_yield_fraction > 1:
        errors.append("invalid:process_yield_fraction")
    previous = 0.0
    for frequency, shielding in x.shielding_curve_db:
        if not math.isfinite(frequency) or not math.isfinite(shielding):
            errors.append("invalid:shielding_curve_db")
            break
        if (frequency <= previous or x.min_frequency_hz is None or x.max_frequency_hz is None
                or not x.min_frequency_hz <= frequency <= x.max_frequency_hz):
            errors.append("invalid:shielding_curve_frequency_order_or_band")
            break
        previous = frequency
    if x.evidence_class == "MEASURED":
        for name in ("feedstock_lot", "incumbent_id", "process_recipe_id", "test_method"):
            if not getattr(x, name).strip():
                errors.append(f"missing:{name}")
        if not x.shielding_curve_db or x.thickness_mm is None or x.areal_density_kg_m2 is None:
            errors.append("incomplete_measured:coupon_functional_metrics")
    return tuple(errors)


def coupon_missing_preregistration_and_measurements(x: PangolaCouponResult) -> tuple[str, ...]:
    fields = []
    for name in ("feedstock_lot", "incumbent_id", "process_recipe_id", "test_method", "min_frequency_hz", "max_frequency_hz"):
        if not getattr(x, name):
            fields.append(name)
    if x.thickness_mm is None:
        fields.append("thickness_mm")
    if x.areal_density_kg_m2 is None:
        fields.append("areal_density_kg_m2")
    if not x.shielding_curve_db:
        fields.append("shielding_curve_db")
    return tuple(fields)


def compare_coupon_curves(
    candidate: PangolaCouponResult,
    incumbent: PangolaCouponResult,
    *,
    geometry_rel_tolerance: float = 0.02,
) -> tuple[tuple[float, float], ...]:
    """Return candidate-minus-incumbent dB after a preregistered geometry match.

    The 2% default is a project screening choice, not an ASTM D4935 tolerance.
    A physical test protocol must check that tolerance against its metrology
    uncertainty and freeze the nominal geometry before fabrication.
    """
    if not math.isfinite(geometry_rel_tolerance) or geometry_rel_tolerance < 0:
        raise ValueError("geometry_rel_tolerance must be finite and non-negative")
    if not candidate.shielding_curve_db or not incumbent.shielding_curve_db:
        raise ValueError("both measured shielding curves are required")
    if candidate.thickness_mm is None or incumbent.thickness_mm is None:
        raise ValueError("matched thickness measurements are required")
    if candidate.thickness_mm <= 0 or incumbent.thickness_mm <= 0:
        raise ValueError("positive thickness measurements are required")
    if not math.isclose(candidate.thickness_mm, incumbent.thickness_mm, rel_tol=geometry_rel_tolerance, abs_tol=0.0):
        raise ValueError("thickness mismatch")
    if candidate.areal_density_kg_m2 is None or incumbent.areal_density_kg_m2 is None:
        raise ValueError("matched areal-density measurements are required")
    if candidate.areal_density_kg_m2 <= 0 or incumbent.areal_density_kg_m2 <= 0:
        raise ValueError("positive areal-density measurements are required")
    if not math.isclose(candidate.areal_density_kg_m2, incumbent.areal_density_kg_m2, rel_tol=geometry_rel_tolerance, abs_tol=0.0):
        raise ValueError("areal-density mismatch")
    if tuple(f for f, _ in candidate.shielding_curve_db) != tuple(f for f, _ in incumbent.shielding_curve_db):
        raise ValueError("frequency grids differ")
    return tuple((f, c - i) for (f, c), (_, i) in zip(candidate.shielding_curve_db, incumbent.shielding_curve_db))


@dataclass(frozen=True)
class ReplicationPackage:
    manifest: ReplicationManifest
    raw_data: bytes
    team_id: str
    site_id: str
    independent_from_primary: bool = False


@dataclass(frozen=True)
class ReplicationEvaluation:
    status: str
    errors: tuple[str, ...]
    protocol_drift: tuple[str, ...]
    evidence_class: str = "REPLICATION_INFRASTRUCTURE_ONLY"
    source_claim_supported: bool = False


def evaluate_replication_pair(
    primary: ReplicationPackage, replication: ReplicationPackage
) -> ReplicationEvaluation:
    errors: list[str] = []
    for label, package in (("primary", primary), ("replication", replication)):
        errors.extend(f"{label}:{e}" for e in validate_manifest(package.manifest))
        if not verify_dataset(package.manifest, package.raw_data):
            errors.append(f"{label}:dataset_integrity_failure")
        if not package.team_id.strip() or not package.site_id.strip():
            errors.append(f"{label}:missing_team_or_site")
    if not replication.independent_from_primary:
        errors.append("replication:not_independently_operated")
    if primary.team_id == replication.team_id:
        errors.append("replication:team_not_independent")
    if primary.site_id == replication.site_id:
        errors.append("replication:site_not_independent")
    invariant_fields = (
        "protocol_id", "protocol_version", "code_commit", "schema_version",
        "randomization_method", "scoring_rule", "exclusion_rules",
    )
    drift = tuple(
        name for name in invariant_fields
        if getattr(primary.manifest, name) != getattr(replication.manifest, name)
    )
    errors.extend(f"protocol_drift:{name}" for name in drift)
    status = "CONSISTENT_REPLICATION_PACKAGES" if not errors else "BLOCKED"
    return ReplicationEvaluation(status, tuple(errors), drift)


@dataclass(frozen=True)
class CapitalGateRecord:
    gate_id: str
    evidence_state: str
    next_gate: str
    cheapest_decisive_test: str
    success_unlock: str
    failure_action: str
    proposed_capital_at_risk_thb: Optional[float] = None
    authorization_status: str = "NOT_AUTHORIZED"
    evidence_class: str = "CAPITAL_GOVERNANCE_ONLY"


def capital_gate_records() -> tuple[CapitalGateRecord, ...]:
    return (
        CapitalGateRecord(
            gate_id="CAP-DMF-EMI-001",
            evidence_state="LITERATURE_CANDIDATE_NO_PANGOLA_RESULT",
            next_gate="matched Pangola coupon test against a named incumbent",
            cheapest_decisive_test=(
                "fabricate controlled coupons; measure shielding vs frequency, conductivity, "
                "thermal/mechanical stability, process yield, energy, chemicals and cost"
            ),
            success_unlock="bounded component prototype review; no automatic factory funding",
            failure_action="stop or reformulate processing/composition before component escalation",
        ),
        CapitalGateRecord(
            gate_id="CAP-BOSONIC-001",
            evidence_state="PUBLISHED_BOSONIC_QEC_EXPERIMENTS_UQPU_ADVANTAGE_UNVERIFIED",
            next_gate="matched logical-memory resource reproduction/model with full overhead",
            cheapest_decisive_test=(
                "populate preparation, stabilization/control, ancilla, readout, decoder, "
                "energy and cost for one frozen logical-memory target"
            ),
            success_unlock="review a bounded authorized provider/device experiment",
            failure_action="deprioritize this platform if full-stack cost closes the useful-output case",
        ),
    )


def validate_capital_gate_record(x: CapitalGateRecord) -> tuple[str, ...]:
    errors: list[str] = []
    for name in ("gate_id", "evidence_state", "next_gate", "cheapest_decisive_test", "success_unlock", "failure_action"):
        if not getattr(x, name).strip():
            errors.append(f"missing:{name}")
    if x.proposed_capital_at_risk_thb is not None:
        if not math.isfinite(x.proposed_capital_at_risk_thb) or x.proposed_capital_at_risk_thb < 0:
            errors.append("invalid:proposed_capital_at_risk_thb")
    if x.authorization_status != "NOT_AUTHORIZED" and x.proposed_capital_at_risk_thb is None:
        errors.append("missing:authorized_capital_amount")
    return tuple(errors)


@dataclass(frozen=True)
class ProviderAICostLink:
    baseline_id: str
    baseline_usd: float
    target_thb: float = 50_000.0
    thb_per_usd: float = 33.045
    provider_component_cost_usd: Optional[float] = None
    other_fixed_cost_usd: Optional[float] = None
    evidence_class: str = "ANALYTIC_LINK_PRICE_EVIDENCE_REQUIRED"


@dataclass(frozen=True)
class ProviderAICostResult:
    baseline_id: str
    target_usd: float
    provider_component_cost_usd: Optional[float]
    other_fixed_cost_usd: Optional[float]
    maximum_residual_fraction: Optional[float]
    status: str
    evidence_class: str = "ANALYTIC_NECESSARY_CONDITION_NOT_COST_EVIDENCE"


def evaluate_provider_ai_cost_link(x: ProviderAICostLink) -> ProviderAICostResult:
    if not x.baseline_id.strip() or x.baseline_usd <= 0 or x.target_thb <= 0 or x.thb_per_usd <= 0:
        raise ValueError("baseline identity and positive cost/FX inputs are required")
    for name in ("provider_component_cost_usd", "other_fixed_cost_usd"):
        value = getattr(x, name)
        if value is not None and (not math.isfinite(value) or value < 0):
            raise ValueError(f"{name} must be a nonnegative finite value or unknown")
    target_usd = x.target_thb / x.thb_per_usd
    if x.provider_component_cost_usd is None or x.other_fixed_cost_usd is None:
        return ProviderAICostResult(
            x.baseline_id, target_usd, x.provider_component_cost_usd,
            x.other_fixed_cost_usd, None, "PRICE_EVIDENCE_REQUIRED",
        )
    remaining = target_usd - x.provider_component_cost_usd - x.other_fixed_cost_usd
    if remaining < 0:
        return ProviderAICostResult(
            x.baseline_id, target_usd, x.provider_component_cost_usd,
            x.other_fixed_cost_usd, 0.0, "FIXED_COSTS_EXCEED_TOTAL_TARGET",
        )
    return ProviderAICostResult(
        x.baseline_id, target_usd, x.provider_component_cost_usd,
        x.other_fixed_cost_usd, min(1.0, remaining / x.baseline_usd),
        "RESIDUAL_BUDGET_AVAILABLE_AS_NECESSARY_CONDITION",
    )


def canonical_provider_ai_cost_links() -> tuple[ProviderAICostLink, ...]:
    return (
        ProviderAICostLink("BASELINE-10T-USD", 10_000_000_000_000.0),
        ProviderAICostLink("BASELINE-100T-USD", 100_000_000_000_000.0),
    )


def cycle001_delta07_artifact() -> dict:
    classical, quantum = ising_pair_template()
    bosonic = bosonic_memory_template()
    coupon = pangola_coupon_result_template()
    return {
        "cycle": "001",
        "delta": "07",
        "status": "ALL_LANE_CONTRACTS_AND_TEMPLATES_NO_NEW_EMPIRICAL_CLAIM",
        "ising": {"classical": asdict(classical), "quantum": asdict(quantum)},
        "bosonic_memory": asdict(bosonic),
        "pangola_coupon": asdict(coupon),
        "scm_replication": {
            "status": "AWAITING_PRIMARY_AND_INDEPENDENT_REPLICATION_PACKAGES",
            "evidence_class": "REPLICATION_INFRASTRUCTURE_ONLY",
        },
        "capital_gates": [asdict(x) for x in capital_gate_records()],
        "provider_ai_cost_links": [
            asdict(evaluate_provider_ai_cost_link(x)) for x in canonical_provider_ai_cost_links()
        ],
    }
