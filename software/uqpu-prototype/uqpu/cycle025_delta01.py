"""Cycle 025 bounded fixtures; results remain local, synthetic, model, or fiction evidence."""
from __future__ import annotations

import hashlib
import itertools
import json
import math
import struct
import tempfile
from fractions import Fraction
from pathlib import Path

from uqpu.cycle013_delta01 import canonical_hash
from uqpu.cycle014_delta01 import fictional_transcript
from uqpu.cycle015_delta01 import (
    component_covariance_sweep,
    concurrent_subprocess_replace,
    make_custody_event,
    verify_custody_chain,
)
from uqpu.cycle019_delta01 import canonical_receipt_bytes

LANES = (
    "A", "B", "C", "D", "E", "F", "G", "H",
    "FND/EQN", "SCM", "AI-COST", "QOS/QSVT",
)


def fifth_graph_perturbation():
    """Compare complete witnesses for the fourth and fifth 11-node fixtures."""
    n = 11

    def solve(weights):
        edges = [[i, (i + 1) % n, weights[i]] for i in range(n)]
        scores = [
            sum(weight for u, v, weight in edges
                if ((mask >> u) & 1) != ((mask >> v) & 1))
            for mask in range(1 << n)
        ]
        optimum = max(scores)
        witnesses = [mask for mask, score in enumerate(scores) if score == optimum]
        return {
            "states": len(scores),
            "objective": optimum,
            "witnesses": witnesses,
            "witness_sha256": canonical_hash(witnesses),
            "task_sha256": canonical_hash({"vertices": n, "edges": edges}),
        }

    fourth_weights = [1] * n
    fourth_weights[3] = 2
    fifth_weights = list(fourth_weights)
    fifth_weights[8] = 3
    fourth, fifth = solve(fourth_weights), solve(fifth_weights)
    return {
        "states_each": [fourth["states"], fifth["states"]],
        "state_cap_each": 2048,
        "objectives": [fourth["objective"], fifth["objective"]],
        "witness_counts": [len(fourth["witnesses"]), len(fifth["witnesses"])],
        "fourth_witness_sha256": fourth["witness_sha256"],
        "fifth_witness_sha256": fifth["witness_sha256"],
        "complete_witness_sets_differ": fourth["witnesses"] != fifth["witnesses"],
        "changed_edge_indices": [8],
        "unchanged_edges_identical": all(
            fourth_weights[i] == fifth_weights[i] for i in range(n) if i != 8
        ),
        "fifth_task_sha256": fifth["task_sha256"],
        "deterministic": fifth == solve(fifth_weights),
        "scaling_claim": None,
        "evidence_class": "LOCAL_EXACT_CLASSICAL_FIXTURE",
    }


def typed_receipt_scalar_gate():
    """Bind JSON scalar types while rejecting size, non-finite and NFC ambiguity."""
    first = (
        b'{"body":{"count":7,"ratio":0.25,"enabled":true,"missing":null,'
        b'"nested":[1,false,null]},"scope":"fixture-025"}'
    )
    reordered = (
        b'{"scope":"fixture-025","body":{"nested":[1,false,null],"missing":null,'
        b'"enabled":true,"ratio":0.25,"count":7}}'
    )

    def bounded(raw):
        if len(raw) > 256:
            raise ValueError("receipt byte cap")
        return canonical_receipt_bytes(raw)

    canonical_first = bounded(first)
    controls = {}
    for name, raw in {
        "overlong": b'{"padding":"' + (b"x" * 260) + b'"}',
        "nonfinite_nan": b'{"value":NaN}',
        "nonfinite_infinity": b'{"value":Infinity}',
        "normalization_collision": '{"body":{"é":1,"é":2}}'.encode("utf-8"),
    }.items():
        try:
            bounded(raw)
            controls[name] = False
        except (UnicodeDecodeError, ValueError, json.JSONDecodeError):
            controls[name] = True
    decoded = json.loads(canonical_first)
    scalar_types_bound = (
        type(decoded["body"]["count"]) is int
        and type(decoded["body"]["ratio"]) is float
        and type(decoded["body"]["enabled"]) is bool
        and decoded["body"]["missing"] is None
    )
    return {
        "reordering_invariant": canonical_first == bounded(reordered),
        "canonical_sha256": hashlib.sha256(canonical_first).hexdigest(),
        "scalar_types_bound": scalar_types_bound,
        "negative_controls": controls,
        "byte_cap": 256,
        "external_authority": None,
        "provider_job_invoice": None,
        "evidence_class": "SYNTHETIC_RECEIPT_CANONICALIZATION",
    }


def alternating_process_termination(directory):
    rows = []
    for run in range(4):
        target = f"target-{run % 2}.bin"
        payloads = [f"cycle025-{run}-{writer}".encode("ascii") for writer in range(3)]
        result = concurrent_subprocess_replace(directory, target, payloads)
        rows.append({
            "run": run,
            "target": target,
            "interruption_points": ["after_replace", "before_replace", "after_replace"],
            "exit_codes": result["exit_codes"],
            "visible_complete_old_or_new": result["visible_complete"],
            "visible_sha256": result["visible_sha256"],
        })
    return {
        "runs": rows,
        "targets": sorted({row["target"] for row in rows}),
        "classified_digests": [row["visible_sha256"] for row in rows],
        "all_recovered_complete": all(row["visible_complete_old_or_new"] for row in rows),
        "crash_durability": None,
        "power_loss_durability": None,
        "evidence_class": "LOCAL_PROCESS_TERMINATION_FIXTURE",
    }


def zip64_extra_field_cross_bind():
    """Apply a declared synthetic extra-field order policy before payload access."""
    expected = {"crc32": 0x10203040, "compressed": 13, "uncompressed": 21}

    def field(identifier, body):
        return struct.pack("<HH", identifier, len(body)) + body

    zip64_body = struct.pack("<QQ", expected["uncompressed"], expected["compressed"])
    vendor_body = b"fixture-025"
    extras = field(0x0001, zip64_body) + field(0xCAFE, vendor_body)

    def parse_extras(raw):
        offset, parsed, order = 0, {}, []
        while offset < len(raw):
            if offset + 4 > len(raw):
                raise ValueError("truncated extra header")
            identifier, width = struct.unpack_from("<HH", raw, offset)
            offset += 4
            if identifier in parsed or offset + width > len(raw):
                raise ValueError("duplicate or truncated extra field")
            parsed[identifier] = raw[offset:offset + width]
            order.append(identifier)
            offset += width
        if order != [0x0001, 0xCAFE] or len(parsed[0x0001]) != 16:
            raise ValueError("declared synthetic extra-field order")
        uncompressed, compressed = struct.unpack("<QQ", parsed[0x0001])
        if (compressed, uncompressed) != (expected["compressed"], expected["uncompressed"]):
            raise ValueError("ZIP64 extra/central size mismatch")
        return order

    def descriptor(signed=True, crc=None, compressed=None, uncompressed=None):
        body = struct.pack(
            "<IQQ",
            expected["crc32"] if crc is None else crc,
            expected["compressed"] if compressed is None else compressed,
            expected["uncompressed"] if uncompressed is None else uncompressed,
        )
        return (b"PK\x07\x08" + body) if signed else body

    def parse_descriptor(raw):
        if len(raw) == 24 and raw[:4] == b"PK\x07\x08":
            form, body = "signed", raw[4:]
        elif len(raw) == 20:
            form, body = "unsigned", raw
        else:
            raise ValueError("descriptor form")
        if struct.unpack("<IQQ", body) != (
            expected["crc32"], expected["compressed"], expected["uncompressed"]
        ):
            raise ValueError("descriptor/central metadata mismatch")
        return form

    parse_extras(extras)
    forms = [parse_descriptor(descriptor(True)), parse_descriptor(descriptor(False))]

    mutations = {
        "descriptor_crc": lambda: parse_descriptor(descriptor(False, crc=0)),
        "descriptor_size": lambda: parse_descriptor(descriptor(True, compressed=14)),
        "duplicate_extra": lambda: parse_extras(extras + field(0x0001, zip64_body)),
        "reordered_extra": lambda: parse_extras(
            field(0xCAFE, vendor_body) + field(0x0001, zip64_body)
        ),
    }
    rejected = {}
    for name, operation in mutations.items():
        try:
            operation()
            rejected[name] = False
        except ValueError:
            rejected[name] = True
    return {
        "descriptor_forms": forms,
        "declared_extra_field_order": ["0x0001", "0xcafe"],
        "mutations_rejected_before_payload": rejected,
        "payload_read": False,
        "real_producer_corpus": None,
        "evidence_class": "SYNTHETIC_ZIP64_METADATA",
    }


def five_issuer_revocation_boundary():
    sample = hashlib.sha256(b"cycle025-synthetic-custody").hexdigest()
    specs = [
        ("issuer-a", "intake", "2026-01-01"),
        ("issuer-b", "storage", "2026-02-01"),
        ("issuer-c", "transfer", "2026-03-01"),
        ("issuer-d", "analysis", "2026-04-01"),
        ("issuer-e", "archive", "2026-05-01"),
    ]
    events, prior = [], "0" * 64
    for sequence, (issuer, scope, start) in enumerate(specs):
        event = make_custody_event(
            sequence, sample, "fixture-025", issuer, scope, start, "2027-01-01", prior
        )
        events.append(event)
        prior = event["event_sha256"]
    registry = {issuer: {scope} for issuer, scope, _ in specs}
    valid = verify_custody_chain(events, registry, "2026-05-01")

    def registry_at(now):
        active = dict(registry)
        if now >= "2026-06-01":
            active.pop("issuer-e")
        return active

    rejected = {}
    for name, now in (
        ("before_fifth_validity", "2026-04-30"),
        ("at_revocation_effective_boundary", "2026-06-01"),
    ):
        try:
            verify_custody_chain(events, registry_at(now), now)
            rejected[name] = False
        except ValueError:
            rejected[name] = True
    return {
        "event_count": len(events),
        "terminal_sha256": valid["final_event_sha256"],
        "revocation_effective_at": "2026-06-01",
        "boundary_rejections": rejected,
        "physical_sample": None,
        "evidence_class": "SYNTHETIC_CUSTODY",
    }


def nine_component_covariance_sweep():
    n = 9
    covariance = [[0.01 if i == j else 0.0004 for j in range(n)] for i in range(n)]
    indefinite = [[1.0 if i == j else 2.0 for j in range(n)] for i in range(n)]
    nonfinite = [
        [float("inf") if i == j == 0 else (1.0 if i == j else 0.0)
         for j in range(n)] for i in range(n)
    ]
    sweeps = {}
    for sigma in (0.5, 1.0, 2.0, 3.0):
        sweeps[str(sigma)] = component_covariance_sweep(
            [[1, 2]] * n,
            {
                "correlated": covariance,
                "missing": None,
                "indefinite": indefinite,
                "nonfinite": nonfinite,
            },
            [1, 3, 9, 0],
            sigma=sigma,
        )
    return {
        "components": n,
        "sigma_values": [0.5, 1.0, 2.0, 3.0],
        "sweeps": sweeps,
        "commercial_interpretation": None,
        "evidence_class": "MODEL_ONLY",
    }


def permuted_typed_covariance_roundtrip():
    order = ["mass", "length", "duration", "current"]
    dimensions = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    factors = [Fraction(1000), Fraction(100), Fraction(1000), Fraction(10)]
    permutation = [2, 0, 3, 1]
    base = [[Fraction(20 if i == j else 1, 20) for j in range(4)] for i in range(4)]
    scaled = [[base[i][j] * factors[i] * factors[j] for j in range(4)] for i in range(4)]
    permuted = [[scaled[permutation[i]][permutation[j]] for j in range(4)] for i in range(4)]
    inverse_permutation = [permutation.index(i) for i in range(4)]
    unpermuted = [
        [permuted[inverse_permutation[i]][inverse_permutation[j]] for j in range(4)]
        for i in range(4)
    ]
    restored = [[unpermuted[i][j] / factors[i] / factors[j] for j in range(4)]
                for i in range(4)]
    product_dimensions = [
        [a + b for a, b in zip(dimensions[i], dimensions[j])]
        for i in range(4) for j in range(4)
    ]
    permuted_order = [order[i] for i in permutation]
    return {
        "operation_sequence": ["positive_diagonal_rescale", "axis_permutation"],
        "order_sha256": canonical_hash(order),
        "permuted_order_sha256": canonical_hash(permuted_order),
        "dimension_sha256": canonical_hash(product_dimensions),
        "permutation": permutation,
        "matrix_product_count": 16,
        "exact_inverse_roundtrip": restored == base,
        "symmetric": all(permuted[i][j] == permuted[j][i]
                         for i in range(4) for j in range(4)),
        "psd_by_congruence_and_permutation": all(value > 0 for value in factors),
        "calibration": None,
        "evidence_class": "SYNTHETIC_TYPED_COVARIANCE",
    }


def nine_scenario_leave_one_out():
    scenarios = [
        [4, 3, 2, 1], [2, 2, 1, 0], [2, 1, 2, 0], [1, 1, 1, 1],
        [0, 3, 2, 3], [0, 1, 2, 3], [3, 0, 3, 1], [1, 4, 0, 4],
        [2, 4, 4, 1],
    ]

    def counts(rows):
        result = [0, 0, 0, 0]
        for scores in rows:
            eligible = {i for i, score in enumerate(scores) if score == max(scores)}
            for order in itertools.permutations(range(4)):
                result[next(candidate for candidate in order if candidate in eligible)] += 1
        return result

    full = counts(scenarios)
    leave_one_out = [counts(scenarios[:i] + scenarios[i + 1:])
                     for i in range(len(scenarios))]
    full_total = len(scenarios) * math.factorial(4)
    all_fractions = [Fraction(value, full_total) for value in full]
    for row in leave_one_out:
        all_fractions.extend(Fraction(value, (len(scenarios) - 1) * 24) for value in row)
    interval = [min(all_fractions), max(all_fractions)]
    return {
        "scenario_count": len(scenarios),
        "orders_each": 24,
        "grid_size": full_total,
        "winner_counts": full,
        "leave_one_out_winner_counts": leave_one_out,
        "full_and_leave_one_out_interval": [
            [interval[0].numerator, interval[0].denominator],
            [interval[1].numerator, interval[1].denominator],
        ],
        "probability_claim": None,
        "capital": None,
        "evidence_class": "FINITE_ILLUSTRATIVE_SCENARIO",
    }


def composed_source_bound_interval_maps(source_one, source_two):
    if (not isinstance(source_one, bytes) or not source_one
            or not isinstance(source_two, bytes) or not source_two):
        raise ValueError("source bytes")
    sources = [hashlib.sha256(source_one).hexdigest(), hashlib.sha256(source_two).hexdigest()]
    if sources[0] == sources[1]:
        raise ValueError("independent source bindings")
    interval = (Fraction(2, 3), Fraction(5, 3))
    factors = (Fraction(3, 2), Fraction(5, 4))
    after_first = tuple(value * factors[0] for value in interval)
    after_second = tuple(value * factors[1] for value in after_first)
    roundtrip = tuple(value / factors[0] for value in
                      (item / factors[1] for item in after_second))

    def verify(bound_sources, dimension):
        if bound_sources != sources:
            raise ValueError("source binding")
        if dimension != [1, 0, 0, 0]:
            raise ValueError("dimension")
        return True

    controls = {}
    for name, bound, dimension in (
        ("source_mutation", ["0" * 64, sources[1]], [1, 0, 0, 0]),
        ("dimension_mutation", sources, [0, 1, 0, 0]),
    ):
        try:
            verify(bound, dimension)
            controls[name] = False
        except ValueError:
            controls[name] = True
    return {
        "source_sha256": sources,
        "factors": [[item.numerator, item.denominator] for item in factors],
        "composed_interval": [[item.numerator, item.denominator] for item in after_second],
        "roundtrip_interval": [[item.numerator, item.denominator] for item in roundtrip],
        "exact_roundtrip": roundtrip == interval,
        "negative_controls": controls,
        "sort": ["RealModel", "Model"],
        "new_law_claim": None,
        "evidence_class": "SOURCE_TYPED_RATIONAL_MODEL",
    }


def extended_consent_null_table(now):
    base = {
        "fiction_only": True,
        "empirical_coupling": None,
        "seen": set(),
        "scope": "fiction-025",
        "active": True,
        "expires_at": "2030-01-01",
    }

    def attempt(record, nonce, scope, mismatch=False):
        challenge = canonical_hash({"scope": scope, "nonce": nonce})
        response = ("0" * 64) if mismatch else challenge
        try:
            return fictional_transcript(
                record, nonce, scope, challenge, response, now
            )["accepted"]
        except ValueError:
            return False

    rows = [
        ("valid_replacement", base, "new", "fiction-025", False, True),
        ("replay", {**base, "seen": {"old"}}, "old", "fiction-025", False, False),
        ("scope_mismatch", base, "scope", "fiction-other", False, False),
        ("expired", {**base, "expires_at": "2020-01-01"}, "expired", "fiction-025", False, False),
        ("revoked", {**base, "active": False}, "revoked", "fiction-025", False, False),
        ("challenge_mismatch", base, "challenge", "fiction-025", True, False),
        (
            "post_expiry_nonce_replacement",
            {**base, "expires_at": "2026-09-29"},
            "replacement",
            "fiction-025",
            False,
            False,
        ),
    ]
    results = [
        {
            "case": name,
            "accepted": attempt(record, nonce, scope, mismatch),
            "expected": expected,
        }
        for name, record, nonce, scope, mismatch, expected in rows
    ]
    return {
        "control_table": results,
        "all_controls_match": all(row["accepted"] == row["expected"] for row in results),
        "sort": "Fiction",
        "empirical_coupling": None,
        "evidence_class": "FICTION_ONLY",
    }


def lineage_manifest_v15(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("source bytes")
    source_sha = hashlib.sha256(source_bytes).hexdigest()
    splits = {"train": ["t1", "t2"], "validation": ["v1", "v2"], "test": ["h1", "h2"]}
    membership_hashes = {name: canonical_hash(sorted(rows)) for name, rows in splits.items()}
    parent_sha = canonical_hash({"version": 14, "source_sha256": source_sha})
    metric = {
        "name": "fixture_loss",
        "value": 0.2,
        "unit": "1",
        "split": "test",
        "direction": "lower_is_better",
    }
    body = {
        "version": 15,
        "parent_manifest_sha256": parent_sha,
        "source_sha256": source_sha,
        "split_membership_sha256": membership_hashes,
        "heldout_membership_sha256": membership_hashes["test"],
        "config_sha256": canonical_hash({"model": "synthetic-v15"}),
        "heldout_metric": metric,
        "evidence_class": "SYNTHETIC_DATA_LINEAGE",
    }
    manifest = {**body, "manifest_sha256": canonical_hash(body)}

    def verify(candidate):
        required_metric = {"name", "value", "unit", "split", "direction"}
        candidate_metric = candidate.get("heldout_metric")
        if (not isinstance(candidate_metric, dict)
                or set(candidate_metric) != required_metric
                or candidate_metric["split"] != "test"
                or candidate_metric["direction"] not in {"lower_is_better", "higher_is_better"}):
            return False
        if candidate.get("split_membership_sha256") != membership_hashes:
            return False
        if candidate.get("heldout_membership_sha256") != membership_hashes["test"]:
            return False
        unsigned = {key: value for key, value in candidate.items()
                    if key != "manifest_sha256"}
        return (
            candidate.get("parent_manifest_sha256") == parent_sha
            and candidate.get("source_sha256") == source_sha
            and candidate.get("manifest_sha256") == canonical_hash(unsigned)
        )

    def mutation(**updates):
        candidate = json.loads(json.dumps(manifest))
        candidate.update(updates)
        return candidate

    bad_metric = dict(metric)
    bad_metric.pop("direction")
    return {
        "manifest": manifest,
        "valid_manifest": verify(manifest),
        "heldout_membership_mutation_rejected": not verify(
            mutation(heldout_membership_sha256="0" * 64)
        ),
        "metric_schema_mutation_rejected": not verify(mutation(heldout_metric=bad_metric)),
        "parent_mutation_rejected": not verify(
            mutation(parent_manifest_sha256="0" * 64)
        ),
        "candidate_result": None,
        "functional_equivalence": None,
        "evidence_class": "SYNTHETIC_DATA_LINEAGE",
    }


def three_noncommuting_inverse_pairs():
    mask = 0b001011

    def xor(value):
        return value ^ mask

    def rotate_left(value):
        return ((value << 1) & 63) | (value >> 5)

    def rotate_right(value):
        return (value >> 1) | ((value & 1) << 5)

    def swap_pairs(value):
        output = 0
        for low in (0, 2, 4):
            output |= ((value >> low) & 1) << (low + 1)
            output |= ((value >> (low + 1)) & 1) << low
        return output

    pairs = [
        ("xor-mask", xor, xor),
        ("rotate", rotate_left, rotate_right),
        ("pair-swap", swap_pairs, swap_pairs),
    ]

    def forward(value):
        for _, operation, _ in pairs:
            value = operation(value)
        return value

    def inverse(value):
        for _, _, operation in reversed(pairs):
            value = operation(value)
        return value

    encoded = [forward(value) for value in range(64)]
    reconstructed = [inverse(value) for value in encoded]
    noncommuting = {}
    for left, right in itertools.combinations(pairs, 2):
        noncommuting[f"{left[0]}::{right[0]}"] = any(
            left[1](right[1](value)) != right[1](left[1](value))
            for value in range(64)
        )
    return {
        "inverse_pair_names": [item[0] for item in pairs],
        "basis_states_checked": 64,
        "distinct_outputs": len(set(encoded)),
        "residual": sum(original != recovered
                        for original, recovered in enumerate(reconstructed)),
        "pairwise_noncommuting": noncommuting,
        "resource_bound": {"gates": 28, "max_qubits": 6},
        "independent_reference": "pure integer six-bit reconstruction",
        "hardware": None,
        "evidence_class": "SYNTHETIC_INVERSE_OPERATOR",
    }


def run_cycle025_fixture(source_bytes, directory):
    with tempfile.TemporaryDirectory(dir=directory) as work:
        lanes = {
            "A": fifth_graph_perturbation(),
            "B": typed_receipt_scalar_gate(),
            "C": alternating_process_termination(work),
            "D": zip64_extra_field_cross_bind(),
            "E": five_issuer_revocation_boundary(),
            "F": nine_component_covariance_sweep(),
            "G": permuted_typed_covariance_roundtrip(),
            "H": nine_scenario_leave_one_out(),
            "FND/EQN": composed_source_bound_interval_maps(
                source_bytes, source_bytes + b":independent-map-two"
            ),
            "SCM": extended_consent_null_table("2026-09-29"),
            "AI-COST": lineage_manifest_v15(source_bytes),
            "QOS/QSVT": three_noncommuting_inverse_pairs(),
        }
    return {
        lane: {"status": "BLOCKED_WITH_PROGRESS", **value}
        for lane, value in lanes.items()
    }
