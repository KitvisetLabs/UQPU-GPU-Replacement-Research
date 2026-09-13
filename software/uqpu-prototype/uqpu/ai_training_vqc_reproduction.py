"""AI-COST-003: reproducible 2-qubit VQC XOR reproduction and readout repair.

This module reproduces the public architecture from Seilkhan & Taizhanov
(arXiv:2602.24220; public artifact commit d7dd995d...) on the frozen Batch-039
accepted-capability dataset.  It then evaluates a UQPU-specific readout repair.

Evidence level: ideal 2-qubit statevector simulation + exact analytic gradients
+ explicit circuit/shot-equivalent resource ledger.  No real-QPU, quantum
advantage, or end-to-end cost-saving claim is made.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import math
from typing import Iterable, Sequence

from uqpu.ai_training_baseline import _dataset

RESEARCH_ATTRIBUTION = {
    "research_owner_principal_investigator_research_direction": "Kanutsanan Pongpanna",
    "facebook": "https://www.facebook.com/LoveMoneyTH",
    "youtube": "https://www.youtube.com/@LoveMoneyTHOfficial",
    "ai_research_agent": "OpenAI GPT-5.6 Sol",
    "ai_assisted_contribution": (
        "public VQC reproduction design, theorem/interface-style readout audit, "
        "ideal-statevector implementation, resource ledger, hybrid readout repair, "
        "tests, results and research documentation"
    ),
}

PUBLIC_ROUTE_PROVENANCE = {
    "paper": "Comparing Classical and Quantum Variational Classifiers on the XOR Problem",
    "arxiv": "2602.24220v1",
    "authors": ["Miras Seilkhan", "Adilbek Taizhanov"],
    "public_repo": "mseilkhan/XOR-research-Quantum-ML-vs-Classic",
    "public_repo_commit": "d7dd995db6a19295235c48483fe1abb108d9022d",
    "source_model_path": "core/models/vqc.py",
    "source_settings_path": "experiments/settings.py",
}

# NumPy RandomState seed=0, normal(0, 0.1, size=12), frozen explicitly so the
# reproduction does not depend on NumPy or on RNG-version details.
REFERENCE_INITIAL_PARAMETERS = (
    0.1764052345967664,
    0.040015720836722335,
    0.09787379841057392,
    0.2240893199201458,
    0.18675579901499675,
    -0.0977277879876411,
    0.09500884175255894,
    -0.01513572082976979,
    -0.010321885179355785,
    0.04105985019383723,
    0.014404357116087799,
    0.1454273506962975,
)

# Frozen outputs from the deterministic full reproduction.  They are kept as
# audit anchors; the implementation can regenerate them from the initial vector.
REFERENCE_Z0_FINAL_PARAMETERS = (
    0.022916756015702734,
    1.572968473811061,
    -0.046339322811991095,
    0.13313251682647487,
    1.5612347084891465,
    0.07122196443283349,
    -0.04920427947000607,
    -1.5698693891369893,
    -0.010321885179355785,
    0.041059850193837205,
    0.014404357116087816,
    0.1454273506962975,
)

REFERENCE_ZZ_FINAL_PARAMETERS = (
    0.23040868962872074,
    0.03266016398515395,
    0.09787379841057392,
    0.23016653609082144,
    -0.024328526229055118,
    -0.09764843563428884,
    0.09500884175255894,
    -0.015135720829769802,
    -0.010321885179355785,
    0.0402125970272463,
    -0.003032666093842444,
    0.1454273506962975,
)

REFERENCE_CALIBRATION = (10.603102052547635, -0.08930314977146993)


@dataclass(frozen=True)
class VQCReproductionConfig:
    train_examples: int = 256
    test_examples: int = 256
    epochs: int = 250
    learning_rate: float = 0.2
    depth: int = 2
    calibration_epochs: int = 2000
    calibration_learning_rate: float = 0.2
    dataset_seed: int = 1234

    @property
    def parameter_count(self) -> int:
        return 6 * self.depth


def _rx(angle: float):
    c = math.cos(angle / 2.0)
    s = math.sin(angle / 2.0)
    return ((c, -1j * s), (-1j * s, c))


def _ry(angle: float):
    c = math.cos(angle / 2.0)
    s = math.sin(angle / 2.0)
    return ((c, -s), (s, c))


def _dry(angle: float):
    c = math.cos(angle / 2.0)
    s = math.sin(angle / 2.0)
    return ((-0.5 * s, -0.5 * c), (0.5 * c, -0.5 * s))


def _rz(angle: float):
    lo = complex(math.cos(angle / 2.0), -math.sin(angle / 2.0))
    hi = complex(math.cos(angle / 2.0), math.sin(angle / 2.0))
    return ((lo, 0j), (0j, hi))


def _drz(angle: float):
    lo = complex(math.cos(angle / 2.0), -math.sin(angle / 2.0))
    hi = complex(math.cos(angle / 2.0), math.sin(angle / 2.0))
    return ((-0.5j * lo, 0j), (0j, 0.5j * hi))


def _apply_one_qubit(state: Sequence[complex], wire: int, matrix) -> list[complex]:
    out = [0j] * 4
    if wire == 0:
        for q1 in (0, 1):
            a = state[q1]
            b = state[2 + q1]
            out[q1] = matrix[0][0] * a + matrix[0][1] * b
            out[2 + q1] = matrix[1][0] * a + matrix[1][1] * b
    elif wire == 1:
        for q0 in (0, 1):
            i = 2 * q0
            a = state[i]
            b = state[i + 1]
            out[i] = matrix[0][0] * a + matrix[0][1] * b
            out[i + 1] = matrix[1][0] * a + matrix[1][1] * b
    else:
        raise ValueError("only two wires (0, 1) are supported")
    return out


def _apply_cnot(state: Sequence[complex]) -> list[complex]:
    # Basis order |q0 q1>: 00, 01, 10, 11; control=0, target=1.
    return [state[0], state[1], state[3], state[2]]


def _apply_trainable_gate(state, derivatives, wire, matrix, derivative_matrix, parameter_index):
    previous = state
    next_state = _apply_one_qubit(previous, wire, matrix)
    next_derivatives = [_apply_one_qubit(d, wire, matrix) for d in derivatives]
    source_term = _apply_one_qubit(previous, wire, derivative_matrix)
    next_derivatives[parameter_index] = [
        next_derivatives[parameter_index][i] + source_term[i] for i in range(4)
    ]
    return next_state, next_derivatives


def _observable_signs(observable: str) -> tuple[int, int, int, int]:
    if observable == "Z0":
        return (1, 1, -1, -1)
    if observable == "Z1":
        return (1, -1, 1, -1)
    if observable == "ZZ":
        return (1, -1, -1, 1)
    raise ValueError("observable must be Z0, Z1, or ZZ")


def expectation_and_gradient(
    x1: float,
    x2: float,
    theta: Sequence[float],
    *,
    depth: int = 2,
    observable: str = "Z0",
) -> tuple[float, list[float]]:
    """Evaluate the ideal two-qubit circuit and exact derivative of its observable.

    Batch-039 inputs lie in [-1, 1].  The public Dataset-C VQC expects [0, 1],
    so this reproduction applies the semantics-preserving affine map (x+1)/2
    before the public RX(pi*x) feature encoding.

    qml.Rot(phi, theta, omega) is represented by sequential RZ(phi), RY(theta),
    RZ(omega), which is equivalent to the public PennyLane circuit convention.
    """
    if len(theta) != 6 * depth:
        raise ValueError("theta length must equal 6*depth")

    u1 = (x1 + 1.0) / 2.0
    u2 = (x2 + 1.0) / 2.0
    state = [1 + 0j, 0j, 0j, 0j]
    derivatives = [[0j] * 4 for _ in theta]

    for wire, angle in ((0, math.pi * u1), (1, math.pi * u2)):
        gate = _rx(angle)
        state = _apply_one_qubit(state, wire, gate)
        derivatives = [_apply_one_qubit(d, wire, gate) for d in derivatives]

    for layer in range(depth):
        off = 6 * layer
        for wire, base in ((0, off), (1, off + 3)):
            gates = (
                (base, _rz, _drz),
                (base + 1, _ry, _dry),
                (base + 2, _rz, _drz),
            )
            for index, maker, derivative_maker in gates:
                state, derivatives = _apply_trainable_gate(
                    state,
                    derivatives,
                    wire,
                    maker(theta[index]),
                    derivative_maker(theta[index]),
                    index,
                )
        state = _apply_cnot(state)
        derivatives = [_apply_cnot(d) for d in derivatives]

    signs = _observable_signs(observable)
    expectation = sum(signs[i] * abs(state[i]) ** 2 for i in range(4))
    gradient = [
        2.0 * sum(signs[i] * (d[i].conjugate() * state[i]).real for i in range(4))
        for d in derivatives
    ]
    return float(expectation), gradient


def _batch039_probability(expectation: float) -> float:
    # The public Dataset-C paper labels XOR as class 1; Batch 039 labels same-sign
    # quadrants (XNOR) as class 1.  Swapping the output convention is a fixed label
    # complement, not a trainable resource.  This maps +1 expectation to class 1.
    return min(max((1.0 + expectation) / 2.0, 1e-9), 1.0 - 1e-9)


def _sigmoid(z: float) -> float:
    z = max(-60.0, min(60.0, z))
    return 1.0 / (1.0 + math.exp(-z))


def _metrics(data, theta: Sequence[float], *, depth: int, observable: str, calibration=None):
    correct = 0
    loss = 0.0
    expectations: list[tuple[float, float]] = []
    for x1, x2, y in data:
        expectation, _ = expectation_and_gradient(x1, x2, theta, depth=depth, observable=observable)
        if calibration is None:
            p = _batch039_probability(expectation)
        else:
            scale, bias = calibration
            p = _sigmoid(scale * expectation + bias)
        p = min(max(p, 1e-15), 1.0 - 1e-15)
        correct += int((p >= 0.5) == (y >= 0.5))
        loss += -(y * math.log(p) + (1.0 - y) * math.log(1.0 - p))
        expectations.append((expectation, y))
    return {
        "accuracy": correct / len(data),
        "binary_cross_entropy": loss / len(data),
        "expectations_and_labels": expectations,
    }


def train_quantum_route(
    config: VQCReproductionConfig = VQCReproductionConfig(),
    *,
    observable: str = "Z0",
    initial_parameters: Sequence[float] = REFERENCE_INITIAL_PARAMETERS,
) -> dict:
    """Full-batch GD reproduction using exact ideal-statevector gradients."""
    if config.depth != 2 and len(initial_parameters) != config.parameter_count:
        raise ValueError("supply an initial vector matching non-default depth")
    if len(initial_parameters) != config.parameter_count:
        raise ValueError("initial parameter count mismatch")

    train = _dataset(config.train_examples, config.dataset_seed + 1)
    test = _dataset(config.test_examples, config.dataset_seed + 2)
    theta = list(initial_parameters)

    for _ in range(config.epochs):
        gradient = [0.0] * len(theta)
        for x1, x2, y in train:
            expectation, d_expectation = expectation_and_gradient(
                x1, x2, theta, depth=config.depth, observable=observable
            )
            p = _batch039_probability(expectation)
            d_loss_d_p = (p - y) / (p * (1.0 - p))
            for k in range(len(theta)):
                gradient[k] += d_loss_d_p * 0.5 * d_expectation[k]
        inv_n = 1.0 / len(train)
        theta = [
            value - config.learning_rate * grad * inv_n
            for value, grad in zip(theta, gradient)
        ]

    train_metrics = _metrics(train, theta, depth=config.depth, observable=observable)
    test_metrics = _metrics(test, theta, depth=config.depth, observable=observable)
    return {
        "config": asdict(config),
        "observable": observable,
        "final_parameters": theta,
        "train_metrics": {
            "accuracy": train_metrics["accuracy"],
            "binary_cross_entropy": train_metrics["binary_cross_entropy"],
        },
        "test_metrics": {
            "accuracy": test_metrics["accuracy"],
            "binary_cross_entropy": test_metrics["binary_cross_entropy"],
        },
        "train_expectations_and_labels": train_metrics["expectations_and_labels"],
        "test_expectations_and_labels": test_metrics["expectations_and_labels"],
    }


def fit_logistic_readout(
    expectations_and_labels: Iterable[tuple[float, float]],
    *,
    epochs: int = 2000,
    learning_rate: float = 0.2,
) -> tuple[float, float]:
    """Fit a two-scalar classical calibration layer p=sigmoid(a*m+b)."""
    rows = list(expectations_and_labels)
    scale = 1.0
    bias = 0.0
    for _ in range(epochs):
        grad_scale = 0.0
        grad_bias = 0.0
        for expectation, y in rows:
            p = _sigmoid(scale * expectation + bias)
            residual = p - y
            grad_scale += residual * expectation
            grad_bias += residual
        inv_n = 1.0 / len(rows)
        scale -= learning_rate * grad_scale * inv_n
        bias -= learning_rate * grad_bias * inv_n
    return scale, bias


def evaluate_calibrated(expectations_and_labels, calibration: tuple[float, float]) -> dict[str, float]:
    rows = list(expectations_and_labels)
    scale, bias = calibration
    correct = 0
    loss = 0.0
    for expectation, y in rows:
        p = _sigmoid(scale * expectation + bias)
        p = min(max(p, 1e-15), 1.0 - 1e-15)
        correct += int((p >= 0.5) == (y >= 0.5))
        loss += -(y * math.log(p) + (1.0 - y) * math.log(1.0 - p))
    return {"accuracy": correct / len(rows), "binary_cross_entropy": loss / len(rows)}


def parameter_shift_deployment_ledger(config: VQCReproductionConfig = VQCReproductionConfig()) -> dict:
    """Hardware-style circuit/shot equivalent for ordinary parameter-shift training.

    The executable reproduction above uses exact analytic statevector derivatives,
    so these circuit counts were NOT physically executed.  They expose what a
    straightforward parameter-shift deployment would have to budget before
    batching, parallelism, advanced gradient methods, error correction or retries.
    """
    params = config.parameter_count
    samples = config.train_examples * config.epochs
    circuits_per_training_sample = 1 + 2 * params
    training_circuits = samples * circuits_per_training_sample
    final_evaluation_circuits = config.train_examples + config.test_examples
    single_qubit_rotations_per_circuit = 2 + 6 * config.depth
    cnots_per_circuit = config.depth
    return {
        "status": "PARAMETER_SHIFT_CIRCUIT_EQUIVALENT_NOT_EXECUTED",
        "trainable_parameters": params,
        "training_samples_processed": samples,
        "circuits_per_training_sample": circuits_per_training_sample,
        "training_circuit_evaluations": training_circuits,
        "final_evaluation_circuits": final_evaluation_circuits,
        "feature_encoding_rx_per_circuit": 2,
        "single_qubit_rotations_per_circuit": single_qubit_rotations_per_circuit,
        "cnot_per_circuit": cnots_per_circuit,
        "training_single_qubit_rotation_applications": training_circuits * single_qubit_rotations_per_circuit,
        "training_cnot_applications": training_circuits * cnots_per_circuit,
        "training_total_elementary_gate_applications": training_circuits
        * (single_qubit_rotations_per_circuit + cnots_per_circuit),
        "shots_if_128_per_circuit": training_circuits * 128,
        "shots_if_1024_per_circuit": training_circuits * 1024,
        "warning": (
            "resource-pressure proxy only; not a measured runtime, provider bill, "
            "fault-tolerant estimate, or proof that parameter-shift is optimal"
        ),
    }


def structurally_inactive_parameter_indices(depth: int, observable: str) -> tuple[int, ...]:
    """Return exact last-layer inactive indices for the supported readouts.

    For Z0, the final CNOT leaves Z0 invariant, all target-wire rotations in the
    final layer are invisible to Z0, and the last RZ on wire 0 commutes with Z0.
    For ZZ, only the last RZ on each wire is structurally invisible.
    """
    if depth < 1:
        raise ValueError("depth must be positive")
    off = 6 * (depth - 1)
    if observable == "Z0":
        return (off + 2, off + 3, off + 4, off + 5)
    if observable == "ZZ":
        return (off + 2, off + 5)
    return ()


def run_reproduction(config: VQCReproductionConfig = VQCReproductionConfig()) -> dict:
    paper_route = train_quantum_route(config, observable="Z0")
    repair_quantum = train_quantum_route(config, observable="ZZ")
    calibration = fit_logistic_readout(
        repair_quantum["train_expectations_and_labels"],
        epochs=config.calibration_epochs,
        learning_rate=config.calibration_learning_rate,
    )
    repair_train = evaluate_calibrated(repair_quantum["train_expectations_and_labels"], calibration)
    repair_test = evaluate_calibrated(repair_quantum["test_expectations_and_labels"], calibration)

    # Remove bulky per-example arrays from the publication-oriented summary.
    paper_summary = dict(paper_route)
    paper_summary.pop("train_expectations_and_labels")
    paper_summary.pop("test_expectations_and_labels")
    repair_summary = dict(repair_quantum)
    repair_summary.pop("train_expectations_and_labels")
    repair_summary.pop("test_expectations_and_labels")

    return {
        "batch": 40,
        "gate": "AI-COST-003",
        "classification": "VQC_XOR_ACCEPTED_CAPABILITY_REACHED_BY_HYBRID_READOUT_REPAIR_NO_COST_ADVANTAGE",
        "evidence_level": "IDEAL_STATEVECTOR_REPRODUCTION_PLUS_ANALYTIC_RESOURCE_LEDGER",
        "public_route_provenance": PUBLIC_ROUTE_PROVENANCE,
        "paper_architecture_route": paper_summary,
        "paper_route_inactive_parameter_indices": structurally_inactive_parameter_indices(config.depth, "Z0"),
        "uqpu_readout_repair": {
            "change": "replace <Z0> with parity <Z0 Z1> and fit p=sigmoid(a*m+b)",
            "quantum_route_before_calibration": repair_summary,
            "calibration": {"scale": calibration[0], "bias": calibration[1]},
            "calibrated_train_metrics": repair_train,
            "calibrated_test_metrics": repair_test,
            "inactive_parameter_indices_after_readout_change": structurally_inactive_parameter_indices(
                config.depth, "ZZ"
            ),
        },
        "parameter_shift_deployment_ledger": parameter_shift_deployment_ledger(config),
        "accepted_capability_contract": {
            "held_out_accuracy_minimum": 0.98,
            "held_out_binary_cross_entropy_maximum": 0.19,
            "paper_architecture_route_passes": (
                paper_summary["test_metrics"]["accuracy"] >= 0.98
                and paper_summary["test_metrics"]["binary_cross_entropy"] < 0.19
            ),
            "uqpu_readout_repair_passes": (
                repair_test["accuracy"] >= 0.98
                and repair_test["binary_cross_entropy"] < 0.19
            ),
        },
        "non_claims": {
            "real_qpu_ai_training": False,
            "quantum_advantage": False,
            "practical_quantum_speedup": False,
            "gpu_npu_ram_dram_hbm_replacement": False,
            "measured_end_to_end_tco": False,
            "one_hundred_million_x_saving": False,
            "billion_fold_saving": False,
            "data_center_to_tens_of_thousands_thb_equivalence": False,
            "new_physical_law": False,
        },
        "research_attribution": RESEARCH_ATTRIBUTION,
    }
