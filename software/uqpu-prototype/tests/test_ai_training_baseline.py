import math

from uqpu.ai_training_baseline import (
    BaselineConfig,
    CostScenario,
    cost_from_runtime,
    exact_training_operation_ledger,
    parameter_count,
    tensor_payload_ledger,
    train_baseline,
)


def test_parameter_and_operation_ledger_are_frozen():
    cfg = BaselineConfig()
    assert parameter_count(cfg) == 65
    ops = exact_training_operation_ledger(cfg)
    assert ops == {
        "training_samples_processed": 204800,
        "multiply": 29595200,
        "add_subtract": 26676000,
        "tanh": 3276800,
        "exp": 204800,
        "division": 204800,
    }


def test_tensor_payload_contract_is_frozen():
    payload = tensor_payload_ledger(BaselineConfig())
    assert payload == {
        "parameter_payload_bytes": 520,
        "gradient_payload_bytes": 520,
        "train_dataset_payload_bytes": 6144,
        "streaming_activation_payload_bytes_per_example": 136,
        "logical_peak_payload_bytes_streaming": 7320,
        "minimum_dataset_read_bytes_over_training": 4915200,
        "optimizer_parameter_traffic_bytes": 832000,
    }


def test_baseline_meets_accepted_capability_contract():
    result = train_baseline()
    assert result["parameter_count"] == 65
    assert result["train_metrics"]["accuracy"] >= 0.97
    assert result["test_metrics"]["accuracy"] >= 0.98
    assert result["test_metrics"]["binary_cross_entropy"] < 0.19
    assert result["measured_training_wall_seconds"] > 0


def test_cost_adapter_uses_explicit_assumptions():
    scenario = CostScenario(
        host_power_w=65.0,
        electricity_usd_per_kwh=0.10,
        host_capex_usd=500.0,
        host_lifetime_years=3.0,
        utilization_fraction=0.5,
    )
    cost = cost_from_runtime(1.0, scenario)
    assert math.isclose(cost["energy_kwh_model"], 65.0 / 3_600_000.0)
    assert cost["electricity_plus_host_amortization_usd_model"] > 0
