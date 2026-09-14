"""FND-008B1 accepted-function gate for SiC vs diamond spin-defect evidence.

Research Attribution:
- Research Owner / Principal Investigator / Research Direction: Kanutsanan Pongpanna
- Facebook: https://www.facebook.com/LoveMoneyTH
- YouTube: https://www.youtube.com/@LoveMoneyTHOfficial
- AI Research Agent: OpenAI GPT-5.6 Sol
- AI-assisted contribution: primary-source literature audit, apples-to-apples
  benchmark-contract design, executable comparability gate, tests and evidence ledger.

This module deliberately rejects cross-paper winner claims when measurement
conditions or evidence classes differ. It does not claim SiC or diamond wins.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from itertools import combinations

SENSOR_CLASSES = {"SINGLE_DEFECT", "ENSEMBLE"}
EVIDENCE_STATUSES = {"MEASURED_DIRECT", "MODEL_DERIVED_FROM_MEASURED_PARAMETERS", "NOT_REPORTED"}
CLAIM_KINDS = {"PERFORMANCE_WINNER", "END_TO_END_COST_WINNER"}


@dataclass(frozen=True)
class EvidencePoint:
    name: str
    host: str
    accepted_function: str
    sensor_class: str
    temperature_regime: str
    protocol: str
    sensitivity_nt_sqrt_hz: float | None
    sensitivity_status: str
    frequency_min_hz: float | None
    frequency_max_hz: float | None
    defect_depth_nm: float | None
    readout: str
    control: str
    cost_boundary_complete: bool
    source_url: str
    note: str

    def validate(self) -> None:
        if self.sensor_class not in SENSOR_CLASSES:
            raise ValueError("unsupported sensor_class")
        if self.sensitivity_status not in EVIDENCE_STATUSES:
            raise ValueError("unsupported sensitivity_status")
        if self.sensitivity_nt_sqrt_hz is not None and self.sensitivity_nt_sqrt_hz <= 0:
            raise ValueError("sensitivity must be positive")
        if self.sensitivity_status == "NOT_REPORTED" and self.sensitivity_nt_sqrt_hz is not None:
            raise ValueError("NOT_REPORTED cannot contain a sensitivity value")
        if self.sensitivity_status != "NOT_REPORTED" and self.sensitivity_nt_sqrt_hz is None:
            raise ValueError("reported/modelled sensitivity requires a value")
        if (self.frequency_min_hz is None) != (self.frequency_max_hz is None):
            raise ValueError("frequency range must provide both bounds or neither")
        if self.frequency_min_hz is not None and not (0 <= self.frequency_min_hz <= self.frequency_max_hz):
            raise ValueError("invalid frequency range")
        if self.defect_depth_nm is not None and self.defect_depth_nm <= 0:
            raise ValueError("defect depth must be positive")
        for value in (self.name, self.host, self.accepted_function, self.temperature_regime,
                      self.protocol, self.readout, self.control, self.source_url, self.note):
            if not value.strip():
                raise ValueError("text fields must be non-empty")


def frequency_ranges_overlap(a: EvidencePoint, b: EvidencePoint) -> bool:
    if a.frequency_min_hz is None or b.frequency_min_hz is None:
        return False
    return max(a.frequency_min_hz, b.frequency_min_hz) <= min(a.frequency_max_hz, b.frequency_max_hz)


def depth_matched(a: EvidencePoint, b: EvidencePoint, factor: float = 2.0) -> bool:
    if a.defect_depth_nm is None or b.defect_depth_nm is None:
        return False
    ratio = max(a.defect_depth_nm, b.defect_depth_nm) / min(a.defect_depth_nm, b.defect_depth_nm)
    return ratio <= factor


def comparison_blockers(a: EvidencePoint, b: EvidencePoint, claim_kind: str = "PERFORMANCE_WINNER") -> tuple[str, ...]:
    if claim_kind not in CLAIM_KINDS:
        raise ValueError("unsupported claim_kind")
    a.validate(); b.validate()
    blockers: list[str] = []
    if a.accepted_function != b.accepted_function:
        blockers.append("ACCEPTED_FUNCTION_MISMATCH")
    if a.sensor_class != b.sensor_class:
        blockers.append("SENSOR_CLASS_MISMATCH")
    if a.temperature_regime != b.temperature_regime:
        blockers.append("TEMPERATURE_REGIME_MISMATCH")
    if a.protocol != b.protocol:
        blockers.append("PROTOCOL_MISMATCH")
    if a.sensitivity_status != "MEASURED_DIRECT" or b.sensitivity_status != "MEASURED_DIRECT":
        blockers.append("DIRECT_MEASURED_SENSITIVITY_REQUIRED")
    if a.sensitivity_nt_sqrt_hz is None or b.sensitivity_nt_sqrt_hz is None:
        blockers.append("SENSITIVITY_MISSING")
    if not frequency_ranges_overlap(a, b):
        blockers.append("MATCHED_FREQUENCY_BAND_REQUIRED")
    if not depth_matched(a, b):
        blockers.append("MATCHED_DEFECT_DEPTH_REQUIRED")
    if claim_kind == "END_TO_END_COST_WINNER" and not (a.cost_boundary_complete and b.cost_boundary_complete):
        blockers.append("COMPLETE_COST_BOUNDARY_REQUIRED")
    return tuple(blockers)


def winner_claim_allowed(a: EvidencePoint, b: EvidencePoint, claim_kind: str = "PERFORMANCE_WINNER") -> bool:
    return not comparison_blockers(a, b, claim_kind)


def current_public_evidence() -> tuple[EvidencePoint, ...]:
    points = (
        EvidencePoint(
            name="SiC shallow single-divacancy magnetometry estimate",
            host="4H-SiC",
            accepted_function="ROOM_TEMPERATURE_MAGNETIC_FIELD_SENSING",
            sensor_class="SINGLE_DEFECT",
            temperature_regime="ROOM_TEMPERATURE",
            protocol="PULSED_ESR_QNMR",
            sensitivity_nt_sqrt_hz=13.0,
            sensitivity_status="MODEL_DERIVED_FROM_MEASURED_PARAMETERS",
            frequency_min_hz=None,
            frequency_max_hz=None,
            defect_depth_nm=2.0,
            readout="NEAR_INFRARED_OPTICAL",
            control="MICROWAVE_PLUS_OPTICAL",
            cost_boundary_complete=False,
            source_url="https://www.nature.com/articles/s41563-025-02382-9",
            note="~13 nT/sqrt(Hz) is a projected single-divacancy sensitivity for isotope-engineered material; the paper also reports an anticipated ~56 nT/sqrt(Hz) from observed non-optimized shallow-center parameters.",
        ),
        EvidencePoint(
            name="Diamond shallow single-NV AC sensitivity estimate",
            host="diamond",
            accepted_function="ROOM_TEMPERATURE_MAGNETIC_FIELD_SENSING",
            sensor_class="SINGLE_DEFECT",
            temperature_regime="ROOM_TEMPERATURE",
            protocol="ECHO_AC_MAGNETOMETRY",
            sensitivity_nt_sqrt_hz=23.0,
            sensitivity_status="MODEL_DERIVED_FROM_MEASURED_PARAMETERS",
            frequency_min_hz=None,
            frequency_max_hz=None,
            defect_depth_nm=None,
            readout="OPTICAL_NV",
            control="MICROWAVE_PLUS_OPTICAL",
            cost_boundary_complete=False,
            source_url="https://www.nature.com/articles/s41467-025-61026-3",
            note="23 nT/sqrt(Hz) is calculated from recorded shallow-NV coherence/readout parameters under echo sensing; the same study reports >1 ms coherence under CPMG.",
        ),
        EvidencePoint(
            name="Portable diamond NV ensemble magnetometer",
            host="diamond",
            accepted_function="ROOM_TEMPERATURE_MAGNETIC_FIELD_SENSING",
            sensor_class="ENSEMBLE",
            temperature_regime="ROOM_TEMPERATURE",
            protocol="CONTINUOUS_PORTABLE_VECTOR_MAGNETOMETRY",
            sensitivity_nt_sqrt_hz=0.3,
            sensitivity_status="MEASURED_DIRECT",
            frequency_min_hz=10.0,
            frequency_max_hz=150.0,
            defect_depth_nm=None,
            readout="OPTICAL_NV_ENSEMBLE",
            control="MICROWAVE_PLUS_OPTICAL_FEEDBACK",
            cost_boundary_complete=False,
            source_url="https://www.sciencedirect.com/science/article/pii/S0925963525000020",
            note="Measured mean 0.3 +/- 0.2 nT/sqrt(Hz in non-vector mode over 10-150 Hz; ensemble portable device, so it cannot be compared directly with a single-defect SiC number.",
        ),
        EvidencePoint(
            name="SiC single-spin photoelectrical readout",
            host="4H-SiC",
            accepted_function="ROOM_TEMPERATURE_SINGLE_SPIN_STATE_READOUT",
            sensor_class="SINGLE_DEFECT",
            temperature_regime="ROOM_TEMPERATURE",
            protocol="PDMR_SINGLE_SPIN_READOUT",
            sensitivity_nt_sqrt_hz=None,
            sensitivity_status="NOT_REPORTED",
            frequency_min_hz=None,
            frequency_max_hz=None,
            defect_depth_nm=None,
            readout="PHOTOELECTRICAL",
            control="RF_PLUS_OPTICAL",
            cost_boundary_complete=False,
            source_url="https://www.nature.com/articles/s41467-025-58629-1",
            note="Electrical detection produced 1.7-2.0x higher single-spin SNR than optical detection within the SiC experiment; this is a readout result, not an end-to-end SiC-vs-diamond magnetometry winner.",
        ),
        EvidencePoint(
            name="Diamond single-NV surface-voltage readout",
            host="diamond",
            accepted_function="ROOM_TEMPERATURE_SINGLE_SPIN_STATE_READOUT",
            sensor_class="SINGLE_DEFECT",
            temperature_regime="ROOM_TEMPERATURE",
            protocol="SVDMR_KPFM_READOUT",
            sensitivity_nt_sqrt_hz=None,
            sensitivity_status="NOT_REPORTED",
            frequency_min_hz=None,
            frequency_max_hz=None,
            defect_depth_nm=7.0,
            readout="SURFACE_VOLTAGE_KPFM",
            control="MICROWAVE_PLUS_OPTICAL",
            cost_boundary_complete=False,
            source_url="https://www.nature.com/articles/s41467-025-58635-3",
            note="Ambient single-spin coherent dynamics were read by surface photovoltage; reported response time is on the order of 10 ms, and no matched cross-host cost/sensitivity comparison is established.",
        ),
    )
    for point in points:
        point.validate()
    return points


def audit_current_pairs() -> list[dict[str, object]]:
    points = current_public_evidence()
    rows: list[dict[str, object]] = []
    for a, b in combinations(points, 2):
        if a.host == b.host:
            continue
        blockers = comparison_blockers(a, b)
        rows.append({
            "a": a.name,
            "b": b.name,
            "accepted_function_match": a.accepted_function == b.accepted_function,
            "performance_winner_allowed": not blockers,
            "blockers": list(blockers),
        })
    return rows


def batch049_certificate() -> dict[str, object]:
    evidence = current_public_evidence()
    pairs = audit_current_pairs()
    return {
        "program": "FND-008B1/BATCH-049",
        "classification": "SIC_DIAMOND_ACCEPTED_FUNCTION_BENCHMARK_SUFFICIENCY_GATE",
        "evidence_level": "SOURCE_GROUNDED_COMPARABILITY_AUDIT",
        "principle": "SAME_ACCEPTED_FUNCTION_OR_NO_WINNER",
        "public_evidence": [asdict(point) for point in evidence],
        "cross_host_pair_audit": pairs,
        "any_current_performance_winner_allowed": any(row["performance_winner_allowed"] for row in pairs),
        "next_experiment": "Run one matched room-temperature single-defect magnetic-sensing fixture on SiC and diamond with the same protocol, frequency band, depth class, acquisition time, calibration, accepted sensitivity target, control/readout resource ledger and lifecycle-cost boundary.",
        "non_claims": {
            "sic_beats_diamond": False,
            "diamond_beats_sic": False,
            "sic_is_cheaper_end_to_end": False,
            "diamond_is_cheaper_end_to_end": False,
            "pangola_device_grade_diamond_demonstrated": False,
            "quantum_advantage": False,
            "hundred_x_saving": False,
            "hundred_million_x_saving": False,
        },
    }
