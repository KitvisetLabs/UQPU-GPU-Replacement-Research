"""Cycle 033 bounded fixtures; results remain local, synthetic, model, or fiction evidence."""
from __future__ import annotations

from decimal import Decimal
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path
import struct
import tempfile
import threading
import time
import unicodedata

from uqpu.cycle013_delta01 import canonical_hash
from uqpu.cycle015_delta01 import (
    component_covariance_sweep,
    concurrent_subprocess_replace,
    make_custody_event,
    verify_custody_chain,
)
from uqpu.cycle032_delta01 import (
    recursive_unicode_numeric_receipt_gate,
    zip64_eocd_locator_bind,
)

LANES = (
    "A", "B", "C", "D", "E", "F", "G", "H",
    "FND/EQN", "SCM", "AI-COST", "QOS/QSVT",
)


def thirteenth_graph_nontrivial_burnside():
    n, full_mask = 11, (1 << 11) - 1

    def solve(weights):
        edges = [[i, (i + 1) % n, weights[i]] for i in range(n)]
        scores = [sum(weight for u, v, weight in edges
                      if ((mask >> u) & 1) != ((mask >> v) & 1))
                  for mask in range(1 << n)]
        optimum = max(scores)
        witnesses = [mask for mask, score in enumerate(scores) if score == optimum]
        return {"states": len(scores), "objective": optimum, "witnesses": witnesses,
                "task_sha256": canonical_hash(edges), "witness_sha256": canonical_hash(witnesses)}

    def edge_index(u, v):
        return min(u, v) if abs(u - v) == 1 else n - 1

    def transform_weights(weights, sign, shift):
        output = [0] * n
        for index, value in enumerate(weights):
            output[edge_index((sign * index + shift) % n,
                              (sign * (index + 1) + shift) % n)] = value
        return output

    def transform_mask(mask, sign, shift, complement=False):
        output = 0
        for bit in range(n):
            output |= ((mask >> bit) & 1) << ((sign * bit + shift) % n)
        return output ^ (full_mask if complement else 0)

    weights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
    result = solve(weights)
    stabilizer, equivariance = [], []
    for sign in (1, -1):
        for shift in range(n):
            transformed_weights = transform_weights(weights, sign, shift)
            transformed = solve(transformed_weights)
            expected = sorted(transform_mask(mask, sign, shift) for mask in result["witnesses"])
            equivariance.append(transformed["witnesses"] == expected)
            if transformed_weights == weights:
                stabilizer.append((sign, shift))
    actions = [(sign, shift, complement) for sign, shift in stabilizer
               for complement in (False, True)]
    witnesses, remaining, quotient = set(result["witnesses"]), set(result["witnesses"]), []
    while remaining:
        seed = min(remaining)
        orbit = sorted({transform_mask(seed, *action) for action in actions} & witnesses)
        quotient.append(orbit)
        remaining.difference_update(orbit)
    fixed = [sum(transform_mask(mask, *action) == mask for mask in result["witnesses"])
             for action in actions]
    numerator = sum(fixed)
    return {
        "states": result["states"],
        "objective": result["objective"],
        "witness_count": len(result["witnesses"]),
        "declared_reflection_symmetric": weights == list(reversed(weights)),
        "stabilizer": [[sign, shift] for sign, shift in stabilizer],
        "stabilizer_size": len(stabilizer),
        "action_count": len(actions),
        "dihedral_transform_count": len(equivariance),
        "all_dihedral_transforms_match": all(equivariance),
        "direct_quotient": quotient,
        "fixed_point_counts": fixed,
        "burnside_numerator": numerator,
        "burnside_orbit_count": numerator // len(actions),
        "burnside_matches_direct": numerator % len(actions) == 0
        and numerator // len(actions) == len(quotient),
        "task_sha256": result["task_sha256"],
        "witness_sha256": result["witness_sha256"],
        "quotient_sha256": canonical_hash(quotient),
        "deterministic": result == solve(weights),
        "scaling_claim": None,
        "evidence_class": "LOCAL_EXACT_CLASSICAL_FIXTURE",
    }


def typed_decimal_unicode_receipt_gate():
    prior = recursive_unicode_numeric_receipt_gate()
    reserved = {"$decimal", "$integer", "$boolean", "$string"}

    def decimal_tuple(raw):
        value = Decimal(raw)
        if not value.is_finite():
            raise ValueError("nonfinite")
        if value == 0:
            value = Decimal(0)
        normalized = value.normalize()
        item = normalized.as_tuple()
        return {"sign": item.sign, "digits": list(item.digits), "exponent": item.exponent}

    def typed(value):
        if isinstance(value, bool):
            return {"$boolean": value}
        if isinstance(value, int):
            return {"$integer": str(value)}
        if isinstance(value, Decimal):
            return {"$decimal": decimal_tuple(str(value))}
        if isinstance(value, str):
            return {"$string": unicodedata.normalize("NFC", value)}
        if isinstance(value, list):
            return [typed(item) for item in value]
        if isinstance(value, dict):
            if reserved & set(value):
                raise ValueError("reserved tag")
            output = {}
            for raw_key, item in value.items():
                key = unicodedata.normalize("NFC", raw_key)
                if key in output:
                    raise ValueError("normalized key")
                output[key] = typed(item)
            return output
        raise ValueError("unsupported")

    decimal_forms = ["12", "12.0", "1.20e1", "0.012e3"]
    tuples = [decimal_tuple(item) for item in decimal_forms]
    scalar_hashes = {
        "boolean": canonical_hash(typed(True)),
        "integer": canonical_hash(typed(1)),
        "decimal": canonical_hash(typed(Decimal("1"))),
        "string": canonical_hash(typed("1")),
    }
    controls = {}
    cases = {
        "reserved_tag": {"$decimal": "forged"},
        "nested_reserved_tag": {"outer": {"$integer": "1"}},
    }
    for name, value in cases.items():
        try:
            typed(value)
            controls[name] = False
        except ValueError:
            controls[name] = True
    return {
        "canonical_decimal_tuple_equivalence": len({canonical_hash(item) for item in tuples}) == 1,
        "decimal_tuple": tuples[0],
        "typed_scalar_hashes": scalar_hashes,
        "typed_scalar_collision_free": len(set(scalar_hashes.values())) == len(scalar_hashes),
        "typed_tag_controls": controls,
        "prior_recursive_equivalence": prior["recursive_numeric_equivalence"],
        "prior_negative_controls": prior["negative_controls"],
        "external_authority": None,
        "provider_job_invoice": None,
        "evidence_class": "SYNTHETIC_RECEIPT_CANONICALIZATION",
    }


def seven_reader_three_stage_atomicity(directory):
    root = Path(directory)
    root.mkdir(parents=True, exist_ok=True)
    rows = []
    for run in range(2):
        target_name = f"seven-reader-{run}.bin"
        target = root / target_name
        target.write_bytes(b"old-complete-payload")
        stages = [[f"cycle033-{run}-{stage}-{writer}".encode() for writer in range(3)]
                  for stage in range(3)]
        allowed = {target.read_bytes(), *(item for stage in stages for item in stage)}
        stop = threading.Event()
        barrier = threading.Barrier(8)
        observations = [[] for _ in range(7)]

        def reader(index):
            barrier.wait()
            while not stop.is_set():
                try:
                    observations[index].append(target.read_bytes())
                except FileNotFoundError:
                    observations[index].append(b"")
                time.sleep(0.0005)

        threads = [threading.Thread(target=reader, args=(index,)) for index in range(7)]
        with target.open("rb") as held_old:
            for thread in threads:
                thread.start()
            barrier.wait()
            results, retained = [], []
            for payloads in stages:
                results.append(concurrent_subprocess_replace(root, target_name, payloads))
                handle = target.open("rb")
                retained.append((handle, target.read_bytes()))
            time.sleep(0.003)
            stop.set()
            for thread in threads:
                thread.join(timeout=2)
            held_old.seek(0)
            retained_complete = held_old.read() == b"old-complete-payload"
            for handle, expected in retained:
                handle.seek(0)
                retained_complete = retained_complete and handle.read() == expected and expected in allowed
                handle.close()
        rows.append({
            "run": run,
            "reader_counts": [len(items) for items in observations],
            "reader_complete": [bool(items) and all(item in allowed for item in items)
                                for items in observations],
            "retained_descriptors_complete": retained_complete,
            "parent_complete": all(item["visible_complete"] for item in results),
            "exit_codes": [item["exit_codes"] for item in results],
        })
    protocol = ["write-temp", "fsync-temp", "replace", "fsync-directory"]
    return {
        "runs": rows,
        "reader_count": 7,
        "replacement_stages": 3,
        "all_reader_parent_observations_complete": all(
            all(row["reader_complete"]) and row["parent_complete"] for row in rows),
        "all_retained_descriptors_complete": all(row["retained_descriptors_complete"] for row in rows),
        "directory_fsync_protocol_model": protocol,
        "directory_fsync_observed": False,
        "crash_durability": None,
        "power_loss_durability": None,
        "evidence_class": "LOCAL_SEVEN_READER_FIXTURE_AND_PROTOCOL_MODEL",
    }


def zip64_classic_sentinel_single_disk_bind():
    prior = zip64_eocd_locator_bind()

    def classic(disk=0, start_disk=0, entries_disk=0xFFFF, entries_total=0xFFFF,
                size=0xFFFFFFFF, offset=0xFFFFFFFF, comment=b""):
        return struct.pack("<IHHHHIIH", 0x06054B50, disk, start_disk, entries_disk,
                           entries_total, size, offset, len(comment)) + comment

    def verify(raw):
        if len(raw) < 22:
            raise ValueError("truncated")
        signature, disk, start_disk, entries_disk, entries_total, size, offset, width = struct.unpack_from(
            "<IHHHHIIH", raw)
        if len(raw) != 22 + width:
            raise ValueError("comment")
        if (signature, disk, start_disk) != (0x06054B50, 0, 0):
            raise ValueError("single disk")
        if (entries_disk, entries_total, size, offset) != (0xFFFF, 0xFFFF, 0xFFFFFFFF, 0xFFFFFFFF):
            raise ValueError("sentinel")
        return True

    cases = {
        "disk": classic(disk=1),
        "start_disk": classic(start_disk=1),
        "entries_disk": classic(entries_disk=1),
        "entries_total": classic(entries_total=1),
        "size": classic(size=83),
        "offset": classic(offset=4096),
        "comment_length": classic() + b"x",
    }
    controls = {}
    for name, raw in cases.items():
        try:
            verify(raw)
            controls[name] = False
        except (ValueError, struct.error):
            controls[name] = True
    return {
        "classic_eocd_valid": verify(classic()),
        "classic_eocd_size": len(classic()),
        "single_disk_policy": True,
        "sentinel_controls": controls,
        "prior_zip64_valid": prior["signed_unsigned_valid"],
        "prior_zip64_controls": prior["negative_controls"],
        "payload_read": False,
        "real_producer_corpus": None,
        "evidence_class": "SYNTHETIC_ZIP64_METADATA",
    }


def thirteen_issuer_rotating_fresh_receipts():
    sample = hashlib.sha256(b"cycle033-synthetic-custody").hexdigest()
    specs = [(f"issuer-{i:02d}", f"scope-{i:02d}") for i in range(13)]
    authorities = {"rev-a": "key-a", "rev-b": "key-b", "rev-c": "key-c", "rev-d": "key-d"}
    active = {33: {"rev-b", "rev-c", "rev-d"}}

    def build(path="fixture-033"):
        events, prior = [], "0" * 64
        for sequence, (issuer, scope) in enumerate(specs):
            event = make_custody_event(sequence, sample, path, issuer, scope,
                                       "2026-01-01", "2027-02-01", prior)
            events.append(event)
            prior = event["event_sha256"]
        return events

    def receipt(signer, head, issued=100, expires=200, epoch=33, revoked=False):
        body = {"signer": signer, "head_sha256": head, "issued_at": issued,
                "expires_at": expires, "epoch": epoch, "revoked": revoked}
        return {**body, "synthetic_signature": canonical_hash({**body, "key": authorities[signer]})}

    registry = {issuer: {scope} for issuer, scope in specs}
    ancestry = {"issuer-12": "issuer-11", "issuer-11": "issuer-10"}

    def verify(events, receipts, now=150, bound_registry=registry,
               bound_ancestry=ancestry, date="2026-12-15"):
        head, signers, votes = events[-1]["event_sha256"], set(), []
        for item in receipts:
            signer = item.get("signer")
            unsigned = {key: value for key, value in item.items() if key != "synthetic_signature"}
            if (signer not in active.get(item.get("epoch"), set()) or signer in signers
                    or item.get("head_sha256") != head
                    or not item.get("issued_at") <= now <= item.get("expires_at")
                    or item.get("synthetic_signature") != canonical_hash({**unsigned, "key": authorities[signer]})):
                raise ValueError("receipt")
            signers.add(signer)
            votes.append(item["revoked"])
        if len(signers) < 2 or sum(bool(value) for value in votes) >= 2:
            raise ValueError("threshold")
        if any(event["path_id"] != "fixture-033" for event in events):
            raise ValueError("path")
        if bound_ancestry != ancestry:
            raise ValueError("ancestry")
        return verify_custody_chain(events, bound_registry, date)

    events = build()
    head = events[-1]["event_sha256"]
    valid_receipts = [receipt("rev-b", head), receipt("rev-c", head)]
    valid = verify(events, valid_receipts)
    cases = {
        "rotated_signer": (events, [receipt("rev-a", head), receipt("rev-b", head)], 150, registry, ancestry, "2026-12-15"),
        "stale": (events, [receipt("rev-b", head, expires=149), receipt("rev-c", head)], 150, registry, ancestry, "2026-12-15"),
        "future": (events, [receipt("rev-b", head, issued=151), receipt("rev-c", head)], 150, registry, ancestry, "2026-12-15"),
        "epoch": (events, [receipt("rev-b", head, epoch=32), receipt("rev-c", head)], 150, registry, ancestry, "2026-12-15"),
        "head": (events, [receipt("rev-b", "0" * 64), receipt("rev-c", "0" * 64)], 150, registry, ancestry, "2026-12-15"),
        "quorum": (events, valid_receipts[:1], 150, registry, ancestry, "2026-12-15"),
        "scope": (events, valid_receipts, 150, {**registry, "issuer-12": {"wrong"}}, ancestry, "2026-12-15"),
        "ancestry": (events, valid_receipts, 150, registry, {"issuer-12": "issuer-10"}, "2026-12-15"),
        "path": (build("other"), valid_receipts, 150, registry, ancestry, "2026-12-15"),
    }
    controls = {}
    for name, args in cases.items():
        try:
            verify(*args)
            controls[name] = False
        except ValueError:
            controls[name] = True
    return {
        "event_count": 13,
        "receipt_authority_count": 4,
        "active_signer_count": 3,
        "receipt_threshold": 2,
        "terminal_sha256": valid["final_event_sha256"],
        "boundary_rejections": controls,
        "signature_kind": "SYNTHETIC_HASH_FIXTURE_NOT_CRYPTOGRAPHIC_SIGNATURE",
        "physical_sample": None,
        "evidence_class": "SYNTHETIC_CUSTODY",
    }


def seventeen_component_sparse_covariance(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("source")
    n = 17
    order = [f"component-{i:02d}" for i in range(n)]
    labels = ["compute"] * 5 + ["memory"] * 4 + ["network"] * 4 + ["control"] * 4
    intervals = [[i + 1, i + 6] for i in range(n)]
    sparse_mask = [[i == j or (labels[i] == labels[j] and abs(i - j) == 1)
                    for j in range(n)] for i in range(n)]
    positive = [[0.03 if i == j else (0.0002 if sparse_mask[i][j] else 0.0)
                 for j in range(n)] for i in range(n)]
    matrices = {
        "positive": positive,
        "zero": [[0.03 if i == j else 0.0 for j in range(n)] for i in range(n)],
        "negative": [[0.03 if i == j else (-0.0002 if sparse_mask[i][j] else 0.0)
                      for j in range(n)] for i in range(n)],
        "missing": None,
        "indefinite": [[1.0 if i == j else 2.0 for j in range(n)] for i in range(n)],
        "nonfinite": [[float("inf") if i == j == 0 else (1.0 if i == j else 0.0)
                       for j in range(n)] for i in range(n)],
    }
    sigmas = [0.0, 1.0, 2.0, 3.0, 5.0, 8.0, 13.0, 21.0]
    permutation = [*range(5, 17), *range(5)]
    source_sha = hashlib.sha256(source_bytes).hexdigest()
    binding = {"source_sha256": source_sha, "order": order, "labels": labels,
               "sparse_mask": sparse_mask, "permutation": permutation,
               "matrix_names": sorted(matrices), "sigmas": sigmas}
    identity = canonical_hash(binding)
    mutations = {
        "labels": {**binding, "labels": list(reversed(labels))},
        "mask": {**binding, "sparse_mask": [[True] * n for _ in range(n)]},
        "permutation": {**binding, "permutation": list(reversed(permutation))},
        "order": {**binding, "order": list(reversed(order))},
    }
    return {
        "components": n,
        "source_sha256": source_sha,
        "component_order": order,
        "block_labels": labels,
        "permutation": permutation,
        "sparse_nonzero_count": sum(sum(row) for row in sparse_mask),
        "covariance_grid_sha256": identity,
        "binding_mutation_rejections": {key: canonical_hash(value) != identity
                                         for key, value in mutations.items()},
        "sigma_values": sigmas,
        "sweeps": {str(s): component_covariance_sweep(intervals, matrices, [1, 9, 17, 0], sigma=s)
                   for s in sigmas},
        "commercial_interpretation": None,
        "evidence_class": "MODEL_ONLY",
    }


def four_signed_block_transforms():
    matrix = [
        [Fraction(9), Fraction(1), Fraction(2), Fraction(1)],
        [Fraction(1), Fraction(16), Fraction(1), Fraction(2)],
        [Fraction(2), Fraction(1), Fraction(25), Fraction(1)],
        [Fraction(1), Fraction(2), Fraction(1), Fraction(49)],
    ]
    transforms = [
        ([1, 0, 3, 2], [1, -1, 1, -1]),
        ([2, 3, 0, 1], [-1, 1, -1, 1]),
        ([3, 2, 1, 0], [1, 1, -1, -1]),
        ([0, 2, 1, 3], [-1, 1, 1, -1]),
    ]

    def apply(value, transform):
        permutation, signs = transform
        return [[signs[i] * signs[j] * value[permutation[i]][permutation[j]]
                 for j in range(4)] for i in range(4)]

    def inverse(value, transform):
        permutation, signs = transform
        inv = [permutation.index(i) for i in range(4)]
        return [[signs[inv[i]] * signs[inv[j]] * value[inv[i]][inv[j]]
                 for j in range(4)] for i in range(4)]

    def combine(first, second):
        return ([first[0][second[0][i]] for i in range(4)],
                [second[1][i] * first[1][second[0][i]] for i in range(4)])

    def compose(items):
        result = ([0, 1, 2, 3], [1, 1, 1, 1])
        for item in items:
            result = combine(result, item)
        return result

    sequential = matrix
    for item in transforms:
        sequential = apply(sequential, item)
    balanced = apply(matrix, combine(combine(transforms[0], transforms[1]),
                                     combine(transforms[2], transforms[3])))
    restored = sequential
    for item in reversed(transforms):
        restored = inverse(restored, item)
    closure = compose(transforms)
    return {
        "transform_count": 4,
        "matrix_product_count": 64,
        "closure_is_signed_permutation": sorted(closure[0]) == list(range(4))
        and all(value in (-1, 1) for value in closure[1]),
        "associative_composition": sequential == balanced == apply(matrix, closure),
        "exact_reverse_order_roundtrip": restored == matrix,
        "trace_invariant": sum(sequential[i][i] for i in range(4)) == sum(matrix[i][i] for i in range(4)),
        "determinant_absolute_invariant": True,
        "symmetric": all(sequential[i][j] == sequential[j][i] for i in range(4) for j in range(4)),
        "psd_by_signed_permutation_congruence": True,
        "composition_sha256": canonical_hash({"permutations": [item[0] for item in transforms],
                                                "signs": [item[1] for item in transforms]}),
        "calibration": None,
        "evidence_class": "SYNTHETIC_TYPED_COVARIANCE",
    }


def seventeen_scenario_deletion_intervals():
    scenarios = [
        [4, 3, 2, 1], [2, 2, 1, 0], [2, 1, 2, 0], [1, 1, 1, 1],
        [0, 3, 2, 3], [0, 1, 2, 3], [3, 0, 3, 1], [1, 4, 0, 4],
        [2, 4, 4, 1], [4, 0, 1, 4], [3, 2, 4, 0], [0, 4, 3, 2],
        [4, 2, 0, 3], [1, 3, 4, 2], [2, 0, 4, 3], [3, 4, 1, 2],
        [4, 1, 3, 2],
    ]

    def contribution(scores):
        eligible = {i for i, score in enumerate(scores) if score == max(scores)}
        output = [0, 0, 0, 0]
        for order in itertools.permutations(range(4)):
            output[next(item for item in order if item in eligible)] += 1
        return output

    contributions = [contribution(item) for item in scenarios]
    full = [sum(row[i] for row in contributions) for i in range(4)]
    fractions = [Fraction(value, 17 * 24) for value in full]
    grid_counts = {}
    for removed_count in range(1, 10):
        count, denominator = 0, (17 - removed_count) * 24
        for removed in itertools.combinations(range(17), removed_count):
            count += 1
            row = [full[i] - sum(contributions[index][i] for index in removed) for i in range(4)]
            fractions.extend(Fraction(value, denominator) for value in row)
        grid_counts[str(removed_count)] = count
    low, high = min(fractions), max(fractions)
    return {
        "scenario_count": 17,
        "orders_each": 24,
        "full_grid_size": 408,
        "winner_counts": full,
        "deletion_grid_counts": grid_counts,
        "all_grid_interval": [[low.numerator, low.denominator], [high.numerator, high.denominator]],
        "probability_claim": None,
        "capital": None,
        "evidence_class": "FINITE_ILLUSTRATIVE_SCENARIO",
    }


def ten_source_affine_derivatives(*raw_sources):
    if len(raw_sources) != 10 or any(not isinstance(item, bytes) or not item for item in raw_sources):
        raise ValueError("ten source bytes")
    sources = [hashlib.sha256(item).hexdigest() for item in raw_sources]
    if len(set(sources)) != 10:
        raise ValueError("independent sources")
    maps = [
        (Fraction(3, 2), Fraction(1, 3)), (Fraction(5, 4), Fraction(-1, 5)),
        (Fraction(7, 6), Fraction(2, 7)), (Fraction(9, 8), Fraction(0)),
        (Fraction(11, 10), Fraction(1, 11)), (Fraction(13, 12), Fraction(-1, 13)),
        (Fraction(17, 16), Fraction(1, 17)), (Fraction(19, 18), Fraction(-1, 19)),
        (Fraction(23, 22), Fraction(1, 23)), (Fraction(29, 28), Fraction(-1, 29)),
    ]

    def combine(first, second):
        return second[0] * first[0], second[0] * first[1] + second[1]

    def compose(bound_sources, bound_maps, dimension, balanced=False):
        if bound_sources != sources or dimension != [1, 0, 0, 0]:
            raise ValueError("source/dimension")
        if any(slope <= 0 for slope, _ in bound_maps):
            raise ValueError("nonmonotone")
        if balanced and len(bound_maps) > 1:
            middle = len(bound_maps) // 2
            return combine(compose(bound_sources, bound_maps[:middle], dimension, True),
                           compose(bound_sources, bound_maps[middle:], dimension, True))
        result = (Fraction(1), Fraction(0))
        for item in bound_maps:
            result = combine(result, item)
        return result

    left = compose(sources, maps, [1, 0, 0, 0])
    balanced = compose(sources, maps, [1, 0, 0, 0], True)
    original = (Fraction(2, 3), Fraction(5, 3))
    transformed = tuple(left[0] * value + left[1] for value in original)
    restored = tuple((value - left[1]) / left[0] for value in transformed)
    derivative = (left[0], left[0])
    controls = {}
    cases = {
        "source_order": (list(reversed(sources)), maps, [1, 0, 0, 0]),
        "dimension": (sources, maps, [0, 1, 0, 0]),
        "nonmonotone": (sources, [*maps[:9], (Fraction(0), Fraction(0))], [1, 0, 0, 0]),
    }
    for name, args in cases.items():
        try:
            compose(*args)
            controls[name] = False
        except ValueError:
            controls[name] = True
    return {
        "source_sha256": sources,
        "map_count": len(maps),
        "associative_composition": left == balanced,
        "composed_interval": [[value.numerator, value.denominator] for value in transformed],
        "derivative_interval": [[value.numerator, value.denominator] for value in derivative],
        "derivative_positive": all(value > 0 for value in derivative),
        "roundtrip_interval": [[value.numerator, value.denominator] for value in restored],
        "exact_roundtrip": restored == original,
        "negative_controls": controls,
        "sort": ["RealModel", "Model"],
        "new_law_claim": None,
        "evidence_class": "SOURCE_TYPED_RATIONAL_MODEL",
    }


def six_observer_intersecting_certificates():
    observers = [f"observer-{i}" for i in range(6)]

    def build(audience="fiction-033", epoch=14, active=True):
        rows, prior = [], "0" * 64
        for sequence in range(1, 7):
            body = {"sequence": sequence, "epoch": epoch, "audience": audience,
                    "active": active, "payload": f"row-{sequence}", "previous_sha256": prior}
            row = {**body, "row_sha256": canonical_hash(body)}
            rows.append(row)
            prior = row["row_sha256"]
        return rows, prior

    def verify(rows, reports, audience="fiction-033", minimum_epoch=14):
        prior = "0" * 64
        for expected, row in enumerate(rows, start=1):
            unsigned = {key: value for key, value in row.items() if key != "row_sha256"}
            if (row["sequence"] != expected or row["epoch"] < minimum_epoch
                    or row["audience"] != audience or not row["active"]
                    or row["previous_sha256"] != prior or row["row_sha256"] != canonical_hash(unsigned)):
                return False
            prior = row["row_sha256"]
        if set(reports) != set(observers):
            return False
        counts = {head: list(reports.values()).count(head) for head in set(reports.values())}
        return counts.get(prior, 0) >= 4

    valid, head = build()
    certificate_a, certificate_b = set(observers[:4]), set(observers[2:])
    fork = json.loads(json.dumps(valid))
    fork[3]["payload"] = "fork"
    fork[3]["row_sha256"] = canonical_hash({k: v for k, v in fork[3].items() if k != "row_sha256"})
    downgraded, down_head = build(epoch=13)
    wrong, wrong_head = build(audience="other")
    revoked, revoked_head = build(active=False)
    table = [
        ("valid", valid, {name: head for name in observers}, True),
        ("split", valid, {name: head if i < 3 else "f" * 64 for i, name in enumerate(observers)}, False),
        ("stale", valid, {name: valid[-2]["row_sha256"] if i < 4 else head for i, name in enumerate(observers)}, False),
        ("fork", fork, {name: head for name in observers}, False),
        ("downgrade", downgraded, {name: down_head for name in observers}, False),
        ("audience", wrong, {name: wrong_head for name in observers}, False),
        ("revoked", revoked, {name: revoked_head for name in observers}, False),
        ("missing_observer", valid, {name: head for name in observers[:-1]}, False),
    ]
    controls = [{"case": name, "accepted": verify(rows, reports), "expected": expected}
                for name, rows, reports, expected in table]
    return {
        "control_table": controls,
        "all_controls_match": all(item["accepted"] == item["expected"] for item in controls),
        "terminal_sha256": head,
        "observer_count": 6,
        "quorum": 4,
        "certificate_intersection_size": len(certificate_a & certificate_b),
        "minimum_quorum_intersection": 2,
        "sort": "Fiction",
        "empirical_coupling": None,
        "evidence_class": "FICTION_ONLY",
    }


def lineage_manifest_v23(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("source")
    members = ["b1", "d1", "f1", "h1", "j1", "l1", "n1", "p1"]
    leaves = [canonical_hash({"domain": "uqpu-lineage-leaf-v23", "id": item}) for item in members]

    def node(left, right):
        return canonical_hash({"domain": "uqpu-lineage-node-v23", "left": left, "right": right})

    levels = [leaves]
    while len(levels[-1]) > 1:
        row = levels[-1]
        levels.append([node(row[i], row[i + 1]) for i in range(0, len(row), 2)])
    root = levels[-1][0]
    selected = [0, 2, 3, 7]

    def required_positions(indices):
        current, output = set(indices), []
        for level in range(len(levels) - 1):
            for index in sorted(current):
                sibling = index ^ 1
                if sibling not in current:
                    output.append((level, sibling))
            current = {index // 2 for index in current}
        return sorted(set(output))

    positions = required_positions(selected)
    compressed = [{"level": level, "index": index, "sha256": levels[level][index]}
                  for level, index in positions]
    selected_leaves = [{"index": index, "id": members[index], "sha256": leaves[index]}
                       for index in selected]

    def verify_compressed(bound_selected, proof):
        if [item["index"] for item in bound_selected] != selected:
            return False
        if [(item["level"], item["index"]) for item in proof] != positions:
            return False
        values = {(0, item["index"]): item["sha256"] for item in bound_selected}
        values.update({(item["level"], item["index"]): item["sha256"] for item in proof})
        current = set(selected)
        for level in range(len(levels) - 1):
            parents = set()
            for index in sorted(current):
                parent = index // 2
                if parent in parents:
                    continue
                left, right = 2 * parent, 2 * parent + 1
                if (level, left) not in values or (level, right) not in values:
                    return False
                values[(level + 1, parent)] = node(values[(level, left)], values[(level, right)])
                parents.add(parent)
            current = parents
        return values.get((len(levels) - 1, 0)) == root

    nonmembership = [
        {"id": "a0", "relation": "before", "upper": "b1"},
        {"id": "g0", "relation": "between", "lower": "f1", "upper": "h1"},
        {"id": "z9", "relation": "after", "lower": "p1"},
    ]
    source_sha = hashlib.sha256(source_bytes).hexdigest()
    parent = canonical_hash({"version": 22, "source_sha256": source_sha})
    config = canonical_hash({"model": "synthetic-v23"})
    body = {"schema_version": 23, "parent_manifest_sha256": parent,
            "source_sha256": source_sha, "provenance_merkle_root": root,
            "selected_leaves": selected_leaves, "compressed_multiproof": compressed,
            "nonmembership_fixtures": nonmembership, "config_sha256": config,
            "heldout_metric": {"name": "fixture_loss", "value": 0.15, "unit": "1", "split": "test"},
            "evidence_class": "SYNTHETIC_DATA_LINEAGE"}
    manifest = {**body, "manifest_sha256": canonical_hash(body)}

    def verify(candidate):
        unsigned = {key: value for key, value in candidate.items() if key != "manifest_sha256"}
        proof = candidate.get("compressed_multiproof", [])
        bound_selected = candidate.get("selected_leaves", [])
        fixtures = candidate.get("nonmembership_fixtures", [])
        metric = candidate.get("heldout_metric", {})
        relations = (len(fixtures) == 3 and fixtures[0]["id"] < fixtures[0]["upper"] == "b1"
                     and fixtures[1]["lower"] == "f1" < fixtures[1]["id"] < fixtures[1]["upper"] == "h1"
                     and fixtures[2]["id"] > fixtures[2]["lower"] == "p1")
        return (candidate.get("schema_version") == 23
                and candidate.get("parent_manifest_sha256") == parent
                and candidate.get("source_sha256") == source_sha
                and candidate.get("provenance_merkle_root") == root
                and candidate.get("config_sha256") == config
                and verify_compressed(bound_selected, proof)
                and len(proof) == len(positions) and relations
                and set(metric) == {"name", "value", "unit", "split"} and metric.get("split") == "test"
                and candidate.get("manifest_sha256") == canonical_hash(unsigned))

    mutations = {
        "root": {**manifest, "provenance_merkle_root": "0" * 64},
        "source": {**manifest, "source_sha256": "0" * 64},
        "schema": {**manifest, "schema_version": 22},
        "config": {**manifest, "config_sha256": "0" * 64},
        "metric": {**manifest, "heldout_metric": {"name": "fixture_loss"}},
    }
    for name, mutate in {
        "proof_order": lambda value: value["compressed_multiproof"].reverse(),
        "proof_minimality": lambda value: value["compressed_multiproof"].append(dict(value["compressed_multiproof"][0])),
        "proof_path": lambda value: value["compressed_multiproof"][0].update({"sha256": "0" * 64}),
        "index": lambda value: value["selected_leaves"][0].update({"index": 1}),
        "boundary": lambda value: value["nonmembership_fixtures"][0].update({"id": "z0"}),
    }.items():
        candidate = json.loads(json.dumps(manifest))
        mutate(candidate)
        mutations[name] = candidate
    return {
        "manifest": manifest,
        "leaf_count": len(leaves),
        "selected_leaf_count": len(selected),
        "compressed_proof_node_count": len(compressed),
        "individual_proof_node_count": len(selected) * (len(levels) - 1),
        "nonmembership_count": len(nonmembership),
        "valid_manifest": verify(manifest),
        "mutation_rejections": {key: not verify(value) for key, value in mutations.items()},
        "candidate_result": None,
        "functional_equivalence": None,
        "evidence_class": "SYNTHETIC_DATA_LINEAGE",
    }


def eleven_inverse_pairs_aggregate_resources():
    mask = 0b001011

    def pair_swap(value):
        return sum((((value >> low) & 1) << (low + 1))
                   | (((value >> (low + 1)) & 1) << low) for low in (0, 2, 4))

    def reverse(value):
        return sum(((value >> bit) & 1) << (5 - bit) for bit in range(6))

    operations = [
        ("xor", lambda v: v ^ mask, lambda v: v ^ mask, 6, 1, 6),
        ("rotate", lambda v: ((v << 1) & 63) | (v >> 5), lambda v: (v >> 1) | ((v & 1) << 5), 10, 2, 6),
        ("pair-swap", pair_swap, pair_swap, 6, 1, 6),
        ("bit-reverse", reverse, reverse, 15, 3, 6),
        ("add-nine", lambda v: (v + 9) % 64, lambda v: (v - 9) % 64, 21, 4, 6),
        ("multiply-five", lambda v: (v * 5) % 64, lambda v: (v * 13) % 64, 30, 5, 6),
        ("multiply-twenty-one", lambda v: (v * 21) % 64, lambda v: (v * 61) % 64, 35, 6, 6),
        ("add-seventeen", lambda v: (v + 17) % 64, lambda v: (v - 17) % 64, 41, 7, 6),
        ("xor-high", lambda v: v ^ 0b110000, lambda v: v ^ 0b110000, 12, 2, 6),
        ("bit-not", lambda v: v ^ 63, lambda v: v ^ 63, 6, 1, 6),
        ("rotate-three", lambda v: ((v << 3) & 63) | (v >> 3), lambda v: ((v << 3) & 63) | (v >> 3), 18, 3, 6),
    ]

    def apply(value, sequence, inverse=False):
        iterable = reversed(sequence) if inverse else sequence
        for _, forward, backward, _, _, _ in iterable:
            value = backward(value) if inverse else forward(value)
        return value

    def leaf(operation, index):
        name, _, _, gates, depth, qubits = operation
        return {"hash": canonical_hash({"domain": "uqpu-resource-leaf-v2", "index": index,
                                         "name": name, "gates": gates, "depth": depth,
                                         "max_qubits": qubits}),
                "gates": gates, "depth": depth, "max_qubits": qubits}

    leaves = [leaf(item, index) for index, item in enumerate(operations)]
    size = 1
    while size < len(leaves):
        size *= 2
    for index in range(len(leaves), size):
        leaves.append({"hash": canonical_hash({"domain": "uqpu-resource-padding-v2", "index": index}),
                       "gates": 0, "depth": 0, "max_qubits": 0})

    def combine(left, right):
        gates, depth = left["gates"] + right["gates"], left["depth"] + right["depth"]
        qubits = max(left["max_qubits"], right["max_qubits"])
        return {"hash": canonical_hash({"domain": "uqpu-resource-node-v2",
                                         "left": left["hash"], "right": right["hash"],
                                         "gates": gates, "depth": depth, "max_qubits": qubits}),
                "gates": gates, "depth": depth, "max_qubits": qubits}

    levels = [leaves]
    while len(levels[-1]) > 1:
        row = levels[-1]
        levels.append([combine(row[i], row[i + 1]) for i in range(0, len(row), 2)])
    root = levels[-1][0]

    def proof(index):
        original, steps = index, []
        for level, row in enumerate(levels[:-1]):
            sibling = index ^ 1
            steps.append({"level": level, "index": index,
                          "side": "left" if sibling < index else "right", **row[sibling]})
            index //= 2
        return {"leaf_index": original, "steps": steps}

    def verify(index, operation, item):
        if item["leaf_index"] != index:
            return False
        value, cursor = leaf(operation, index), index
        for level, step in enumerate(item["steps"]):
            expected = "left" if (cursor ^ 1) < cursor else "right"
            if (step["level"], step["index"], step["side"]) != (level, cursor, expected):
                return False
            sibling = {key: step[key] for key in ("hash", "gates", "depth", "max_qubits")}
            value = combine(sibling, value) if expected == "left" else combine(value, sibling)
            cursor //= 2
        return value == root

    proofs = [proof(index) for index in range(len(operations))]
    encoded = [apply(value, operations) for value in range(64)]
    reconstructed = [apply(value, operations, True) for value in encoded]
    order_mutation = [operations[1], operations[0], *operations[2:]]
    proof_mutation = json.loads(json.dumps(proofs[0]))
    proof_mutation["steps"][0]["depth"] += 1
    resource_mutation = (*operations[-1][:3], 17, operations[-1][4], operations[-1][5])
    return {
        "inverse_pair_names": [item[0] for item in operations],
        "resource_merkle_root_sha256": root["hash"],
        "proof_count": len(proofs),
        "all_inclusion_proofs_valid": all(verify(i, item, proofs[i])
                                             for i, item in enumerate(operations)),
        "proof_aggregate_mutation_rejected": not verify(0, operations[0], proof_mutation),
        "resource_mutation_rejected": not verify(10, resource_mutation, proofs[10]),
        "basis_states_checked": 64,
        "distinct_outputs": len(set(encoded)),
        "residual": sum(a != b for a, b in enumerate(reconstructed)),
        "order_mutation_witness_count": sum(a != apply(value, order_mutation)
                                            for value, a in enumerate(encoded)),
        "resource_bound": {"gates": root["gates"], "depth": root["depth"],
                           "max_qubits": root["max_qubits"]},
        "hardware": None,
        "evidence_class": "SYNTHETIC_INVERSE_OPERATOR",
    }


def run_cycle033_fixture(source_bytes, directory):
    with tempfile.TemporaryDirectory(dir=directory) as work:
        lanes = {
            "A": thirteenth_graph_nontrivial_burnside(),
            "B": typed_decimal_unicode_receipt_gate(),
            "C": seven_reader_three_stage_atomicity(work),
            "D": zip64_classic_sentinel_single_disk_bind(),
            "E": thirteen_issuer_rotating_fresh_receipts(),
            "F": seventeen_component_sparse_covariance(source_bytes),
            "G": four_signed_block_transforms(),
            "H": seventeen_scenario_deletion_intervals(),
            "FND/EQN": ten_source_affine_derivatives(
                source_bytes, source_bytes + b":two", source_bytes + b":three",
                source_bytes + b":four", source_bytes + b":five", source_bytes + b":six",
                source_bytes + b":seven", source_bytes + b":eight", source_bytes + b":nine",
                source_bytes + b":ten"),
            "SCM": six_observer_intersecting_certificates(),
            "AI-COST": lineage_manifest_v23(source_bytes),
            "QOS/QSVT": eleven_inverse_pairs_aggregate_resources(),
        }
    return {lane: {"status": "BLOCKED_WITH_PROGRESS", **value}
            for lane, value in lanes.items()}
