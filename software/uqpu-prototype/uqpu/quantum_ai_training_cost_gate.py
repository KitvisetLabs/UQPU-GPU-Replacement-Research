"""Necessary-condition accounting for the UQPU quantum-AI training cost moonshot.

Evidence level: analytic accounting / model only.  This module does not establish
quantum advantage or a real-hardware cost reduction.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass

RESEARCH_ATTRIBUTION = {
    "research_owner_principal_investigator_research_direction": "Kanutsanan Pongpanna",
    "facebook": "https://www.facebook.com/LoveMoneyTH",
    "youtube": "https://www.youtube.com/@LoveMoneyTHOfficial",
    "ai_research_agent": "OpenAI GPT-5.6 Sol",
    "ai_assisted_contribution": "cost-compression formulation, executable necessary-condition gate, tests and research documentation",
}


@dataclass(frozen=True)
class CostCompressionContract:
    baseline_usd: float
    target_thb: float
    thb_per_usd: float
    target_usd: float
    required_reduction: float
    maximum_residual_fraction: float


def build_contract(*, baseline_usd: float, target_thb: float, thb_per_usd: float) -> CostCompressionContract:
    """Build an end-to-end compression contract from explicit monetary units."""
    if baseline_usd <= 0 or target_thb <= 0 or thb_per_usd <= 0:
        raise ValueError("all monetary inputs and the FX rate must be positive")
    target_usd = target_thb / thb_per_usd
    required_reduction = baseline_usd / target_usd
    return CostCompressionContract(
        baseline_usd=baseline_usd,
        target_thb=target_thb,
        thb_per_usd=thb_per_usd,
        target_usd=target_usd,
        required_reduction=required_reduction,
        maximum_residual_fraction=1.0 / required_reduction,
    )


def normalized_cost_fraction(*, residual_fraction: float, accelerated_reduction: float) -> float:
    """Amdahl-style end-to-end cost fraction: r + (1-r)/S."""
    if not 0.0 <= residual_fraction <= 1.0:
        raise ValueError("residual_fraction must lie in [0, 1]")
    if accelerated_reduction < 1.0:
        raise ValueError("accelerated_reduction must be at least 1")
    return residual_fraction + (1.0 - residual_fraction) / accelerated_reduction


def required_accelerated_reduction(*, residual_fraction: float, target_fraction: float) -> float | None:
    """Return required S, or None when the residual floor already blocks the target."""
    if not 0.0 <= residual_fraction <= 1.0:
        raise ValueError("residual_fraction must lie in [0, 1]")
    if not 0.0 < target_fraction <= 1.0:
        raise ValueError("target_fraction must lie in (0, 1]")
    if residual_fraction >= target_fraction:
        return None
    return (1.0 - residual_fraction) / (target_fraction - residual_fraction)


def residual_floor_cost(*, baseline_usd: float, residual_fraction: float, thb_per_usd: float) -> dict[str, float]:
    """Cost floor if the accelerated portion were made free."""
    if baseline_usd <= 0 or thb_per_usd <= 0:
        raise ValueError("baseline_usd and thb_per_usd must be positive")
    if not 0.0 <= residual_fraction <= 1.0:
        raise ValueError("residual_fraction must lie in [0, 1]")
    usd = baseline_usd * residual_fraction
    return {"usd": usd, "thb": usd * thb_per_usd}


def canonical_batch038_result() -> dict:
    """Return the deterministic Batch-038 accounting snapshot."""
    thb_per_usd = 33.045
    target_thb = 50_000.0
    low = build_contract(baseline_usd=10_000_000_000_000.0, target_thb=target_thb, thb_per_usd=thb_per_usd)
    high = build_contract(baseline_usd=100_000_000_000_000.0, target_thb=target_thb, thb_per_usd=thb_per_usd)
    residual_example = 1e-6
    return {
        "batch": 38,
        "gate": "AI-COST-001",
        "classification": "AI_TRAINING_COST_MOONSHOT_NECESSARY_CONDITION_GATE_ESTABLISHED",
        "evidence_level": "ANALYTIC_ACCOUNTING_NECESSARY_CONDITION",
        "canonical_target_thb": target_thb,
        "fx_snapshot_thb_per_usd": thb_per_usd,
        "baseline_low": asdict(low),
        "baseline_high": asdict(high),
        "one_hundred_million_x_cost_thb": {
            "from_10_trillion_usd": 10_000_000_000_000.0 / 100_000_000.0 * thb_per_usd,
            "from_100_trillion_usd": 100_000_000_000_000.0 / 100_000_000.0 * thb_per_usd,
        },
        "residual_fraction_example": residual_example,
        "infinite_acceleration_residual_floor": {
            "from_10_trillion_usd": residual_floor_cost(
                baseline_usd=10_000_000_000_000.0,
                residual_fraction=residual_example,
                thb_per_usd=thb_per_usd,
            ),
            "from_100_trillion_usd": residual_floor_cost(
                baseline_usd=100_000_000_000_000.0,
                residual_fraction=residual_example,
                thb_per_usd=thb_per_usd,
            ),
        },
        "real_qpu": False,
        "quantum_advantage_demonstrated": False,
        "frontier_ai_training_cost_advantage_demonstrated": False,
        "gpu_npu_ram_dram_hbm_replacement_demonstrated": False,
        "research_attribution": RESEARCH_ATTRIBUTION,
    }
