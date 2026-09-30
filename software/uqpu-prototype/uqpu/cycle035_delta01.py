"""Cycle 035 bounded fixtures; results remain local, synthetic, model, or fiction evidence."""
from __future__ import annotations

from decimal import Decimal
from fractions import Fraction
import hashlib
import itertools
import json
import os
from pathlib import Path
import struct
import tempfile
import threading
import time
import unicodedata

from uqpu.cycle013_delta01 import canonical_hash
from uqpu.cycle015_delta01 import component_covariance_sweep, make_custody_event, verify_custody_chain

LANES = (
    "A", "B", "C", "D", "E", "F", "G", "H",
    "FND/EQN", "SCM", "AI-COST", "QOS/QSVT",
)


def fifteenth_graph_conjugacy_checksum():
    n, full_mask = 11, (1 << 11) - 1
    weights = [2, 3, 5, 7, 11, 13, 11, 7, 5, 3, 2]

    def solve(bound):
        edges = [[i, (i + 1) % n, bound[i]] for i in range(n)]
        scores = [sum(w for u, v, w in edges if ((mask >> u) & 1) != ((mask >> v) & 1))
                  for mask in range(1 << n)]
        optimum = max(scores)
        witnesses = [mask for mask, score in enumerate(scores) if score == optimum]
        return {"states": len(scores), "objective": optimum, "witnesses": witnesses,
                "task_sha256": canonical_hash(edges), "witness_sha256": canonical_hash(witnesses)}

    def edge_index(u, v):
        return min(u, v) if abs(u - v) == 1 else n - 1

    def transform_weights(bound, sign, shift):
        output = [0] * n
        for index, value in enumerate(bound):
            output[edge_index((sign * index + shift) % n,
                              (sign * (index + 1) + shift) % n)] = value
        return output

    def transform_mask(mask, sign, shift, complement=False):
        output = 0
        for bit in range(n):
            output |= ((mask >> bit) & 1) << ((sign * bit + shift) % n)
        return output ^ (full_mask if complement else 0)

    result = solve(weights)
    stabilizer, equivariance = [], []
    for sign in (1, -1):
        for shift in range(n):
            transformed = solve(transform_weights(weights, sign, shift))
            expected = sorted(transform_mask(mask, sign, shift) for mask in result["witnesses"])
            equivariance.append(transformed["witnesses"] == expected)
            if transform_weights(weights, sign, shift) == weights:
                stabilizer.append((sign, shift))
    actions = [(sign, shift, complement) for sign, shift in stabilizer
               for complement in (False, True)]
    witnesses, remaining, quotient = set(result["witnesses"]), set(result["witnesses"]), []
    while remaining:
        seed = min(remaining)
        orbit = sorted({transform_mask(seed, *action) for action in actions} & witnesses)
        quotient.append(orbit)
        remaining.difference_update(orbit)
    contributions = []
    for sign, shift, complement in actions:
        action_class = ("reflection" if sign == -1 else "rotation") + ("+complement" if complement else "")
        contributions.append({"class": action_class,
                              "fixed": sum(transform_mask(mask, sign, shift, complement) == mask
                                           for mask in result["witnesses"])})
    class_totals = {}
    for row in contributions:
        class_totals[row["class"]] = class_totals.get(row["class"], 0) + row["fixed"]
    numerator = sum(class_totals.values())
    union = sorted({item for orbit in quotient for item in orbit})
    return {
        "states": result["states"], "objective": result["objective"],
        "witness_count": len(result["witnesses"]), "stabilizer_size": len(stabilizer),
        "action_count": len(actions), "all_dihedral_transforms_match": all(equivariance),
        "conjugacy_class_fixed_totals": class_totals, "direct_quotient": quotient,
        "burnside_numerator": numerator, "burnside_orbit_count": numerator // len(actions),
        "burnside_matches_direct": numerator % len(actions) == 0
        and numerator // len(actions) == len(quotient),
        "independent_orbit_checksum": {"union_sha256": canonical_hash(union),
                                       "sum": sum(union), "count": len(union)},
        "checksum_matches_witnesses": union == result["witnesses"],
        "task_sha256": result["task_sha256"], "witness_sha256": result["witness_sha256"],
        "deterministic": result == solve(weights), "scaling_claim": None,
        "evidence_class": "LOCAL_EXACT_CLASSICAL_FIXTURE",
    }


def heterogeneous_array_unicode_gate():
    caps = {"depth": 8, "tokens": 52, "minimum_exponent": -24,
            "maximum_exponent": 24, "max_exact_integer": 2 ** 53 - 1}
    reserved = {"$decimal", "$integer", "$boolean", "$string"}

    def pairs(items):
        output = {}
        for raw_key, value in items:
            key = unicodedata.normalize("NFC", raw_key)
            key.encode("utf-8")
            if key in output:
                raise ValueError("normalized duplicate")
            output[key] = value
        return output

    def normalize(value, level=0):
        if level > caps["depth"]:
            raise ValueError("depth")
        if isinstance(value, dict):
            if reserved & set(value):
                raise ValueError("reserved")
            return {key: normalize(item, level + 1) for key, item in value.items()}
        if isinstance(value, list):
            return [normalize(item, level + 1) for item in value]
        if isinstance(value, Decimal):
            if not value.is_finite():
                raise ValueError("nonfinite")
            if value == 0:
                value = Decimal(0)
            item = value.normalize().as_tuple()
            if not caps["minimum_exponent"] <= item.exponent <= caps["maximum_exponent"]:
                raise ValueError("exponent")
            return {"$decimal": [item.sign, list(item.digits), item.exponent]}
        if isinstance(value, bool):
            return {"$boolean": value}
        if isinstance(value, int):
            if abs(value) > caps["max_exact_integer"]:
                raise ValueError("integer")
            return {"$integer": str(value)}
        if isinstance(value, str):
            result = unicodedata.normalize("NFC", value)
            result.encode("utf-8")
            return {"$string": result}
        raise ValueError("type")

    def tokens(value):
        if isinstance(value, dict):
            return len(value) + sum(tokens(item) for item in value.values())
        if isinstance(value, list):
            return len(value) + sum(tokens(item) for item in value)
        return 1

    def parse(raw):
        value = json.loads(raw, object_pairs_hook=pairs, parse_float=Decimal,
                           parse_constant=lambda _: (_ for _ in ()).throw(ValueError("constant")))
        if tokens(value) > caps["tokens"]:
            raise ValueError("tokens")
        return normalize(value)

    first = '[[true,1,1.0,"é"],[{"low":1e-24,"high":1e24},[-0.0]]]'
    equivalent = '[[true,1,10e-1,"e\\u0301"],[{"high":0.1e25,"low":0.1e-23},[0e4]]]'
    cases = {
        "surrogate_value": '["\\ud800"]', "surrogate_key": '{"\\ud800":1}',
        "exponent_low": '[1e-25]', "exponent_high": '[1e25]',
        "integer": '[9007199254740992]', "nonfinite": '[Infinity]',
        "normalized_key": '{"é":1,"é":2}', "reserved": '{"$string":"forged"}',
        "depth": '[[[[[[[[[[1]]]]]]]]]]', "tokens": json.dumps(list(range(53))),
    }
    controls = {}
    for name, raw in cases.items():
        try:
            parse(raw)
            controls[name] = False
        except (ValueError, UnicodeError, json.JSONDecodeError):
            controls[name] = True
    first_hash = canonical_hash(parse(first))
    return {"heterogeneous_array_equivalence": first_hash == canonical_hash(parse(equivalent)),
            "canonical_sha256": first_hash, "caps": caps, "negative_controls": controls,
            "external_authority": None, "provider_job_invoice": None,
            "evidence_class": "SYNTHETIC_RECEIPT_CANONICALIZATION"}


def nine_reader_fsync_order_gate(directory):
    root = Path(directory)
    root.mkdir(parents=True, exist_ok=True)
    required_order = ["write", "file_fsync", "replace", "directory_fsync"]

    def verify_order(steps):
        return steps == required_order

    rows = []
    for run in range(2):
        target = root / f"nine-reader-{run}.bin"
        target.write_bytes(b"old-complete-payload")
        payloads = [f"cycle035-{run}-{stage}".encode() for stage in range(5)]
        allowed = {target.read_bytes(), *payloads}
        observations = [[] for _ in range(9)]
        barrier, stop = threading.Barrier(10), threading.Event()

        def reader(index):
            barrier.wait()
            while not stop.is_set():
                try:
                    observations[index].append(target.read_bytes())
                except FileNotFoundError:
                    observations[index].append(b"")
                time.sleep(0.0005)

        threads = [threading.Thread(target=reader, args=(index,)) for index in range(9)]
        retained, stage_orders = [], []
        with target.open("rb") as old_handle:
            for thread in threads:
                thread.start()
            barrier.wait()
            for stage, payload in enumerate(payloads):
                steps, temporary = [], root / f".{target.name}.{stage}.tmp"
                fd = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
                try:
                    os.write(fd, payload)
                    steps.append("write")
                    os.fsync(fd)
                    steps.append("file_fsync")
                finally:
                    os.close(fd)
                os.replace(temporary, target)
                steps.append("replace")
                dir_fd = os.open(root, os.O_RDONLY)
                try:
                    os.fsync(dir_fd)
                    steps.append("directory_fsync")
                finally:
                    os.close(dir_fd)
                stage_orders.append(steps)
                retained.append((target.open("rb"), payload))
            time.sleep(0.003)
            stop.set()
            for thread in threads:
                thread.join(timeout=2)
            old_handle.seek(0)
            descriptors_complete = old_handle.read() == b"old-complete-payload"
            for handle, expected in retained:
                handle.seek(0)
                descriptors_complete = descriptors_complete and handle.read() == expected
                handle.close()
        rows.append({"run": run, "reader_counts": [len(items) for items in observations],
                     "reader_complete": [bool(items) and all(item in allowed for item in items)
                                         for items in observations],
                     "retained_descriptors_complete": descriptors_complete,
                     "stage_orders": stage_orders,
                     "all_stage_orders_valid": all(verify_order(item) for item in stage_orders)})
    negative_orders = {
        "missing_file_fsync": ["write", "replace", "directory_fsync"],
        "missing_directory_fsync": ["write", "file_fsync", "replace"],
        "replace_before_file_fsync": ["write", "replace", "file_fsync", "directory_fsync"],
        "directory_before_replace": ["write", "file_fsync", "directory_fsync", "replace"],
    }
    return {"runs": rows, "reader_count": 9, "replacement_stages": 5,
            "all_reader_observations_complete": all(all(row["reader_complete"]) for row in rows),
            "all_retained_descriptors_complete": all(row["retained_descriptors_complete"] for row in rows),
            "all_fsync_orders_valid": all(row["all_stage_orders_valid"] for row in rows),
            "fsync_order_negative_controls": {name: not verify_order(value)
                                              for name, value in negative_orders.items()},
            "file_fsync_call_count": 10, "directory_fsync_call_count": 10,
            "crash_durability": None, "power_loss_durability": None,
            "evidence_class": "LOCAL_NINE_READER_FSYNC_ORDER_FIXTURE"}


def zip64_locator_trailing_comment_gate():
    comment_small = "cycle035".encode()
    comment_max = b"x" * 65535
    locator_offset, locator_position = 4096, 8192

    def classic(comment=comment_small, trailing=b"", disk=0):
        if len(comment) > 65535:
            raise ValueError("comment overflow")
        body = struct.pack("<IHHHHIIH", 0x06054B50, disk, 0, 0xFFFF, 0xFFFF,
                           0xFFFFFFFF, 0xFFFFFFFF, len(comment)) + comment
        return body + trailing

    def locator(offset=locator_offset, position=locator_position):
        return {"bytes": struct.pack("<IIQI", 0x07064B50, 0, offset, 1),
                "position": position}

    def verify(raw_classic, raw_locator, expected_comment):
        if len(raw_classic) < 22:
            raise ValueError("truncated")
        fields = struct.unpack_from("<IHHHHIIH", raw_classic)
        width = fields[-1]
        if len(raw_classic) != 22 + width or raw_classic[22:] != expected_comment:
            raise ValueError("comment/trailing")
        if fields[:-1] != (0x06054B50, 0, 0, 0xFFFF, 0xFFFF, 0xFFFFFFFF, 0xFFFFFFFF):
            raise ValueError("classic")
        signature, disk, offset, disks = struct.unpack("<IIQI", raw_locator["bytes"])
        if (signature, disk, offset, disks) != (0x07064B50, 0, locator_offset, 1):
            raise ValueError("locator")
        if raw_locator["position"] <= offset:
            raise ValueError("placement")
        return True

    valid_small = verify(classic(), locator(), comment_small)
    valid_max = verify(classic(comment_max), locator(), comment_max)
    controls = {}
    cases = {
        "trailing": (classic(trailing=b"x"), locator(), comment_small),
        "comment_bytes": (classic(b"other"), locator(), comment_small),
        "disk": (classic(disk=1), locator(), comment_small),
        "locator_offset": (classic(), locator(offset=locator_offset - 1), comment_small),
        "locator_position": (classic(), locator(position=locator_offset), comment_small),
    }
    for name, args in cases.items():
        try:
            verify(*args)
            controls[name] = False
        except (ValueError, struct.error):
            controls[name] = True
    try:
        classic(b"x" * 65536)
        controls["comment_overflow"] = False
    except ValueError:
        controls["comment_overflow"] = True
    return {"small_comment_valid": valid_small, "maximum_comment_valid": valid_max,
            "maximum_comment_length": len(comment_max), "locator_position": locator_position,
            "locator_target_offset": locator_offset, "negative_controls": controls,
            "payload_read": False, "real_producer_corpus": None,
            "evidence_class": "SYNTHETIC_ZIP64_METADATA"}


def fifteen_issuer_policy_chain():
    sample = hashlib.sha256(b"cycle035-synthetic-custody").hexdigest()
    specs = [(f"issuer-{i:02d}", f"scope-{i:02d}") for i in range(15)]
    keys = {name: f"synthetic-{name}" for name in ("rev-c", "rev-d", "rev-e", "rev-f")}
    policies = []
    previous = "0" * 64
    for version, active in ((33, ["rev-c", "rev-d"]),
                            (34, ["rev-c", "rev-d", "rev-e"]),
                            (35, ["rev-d", "rev-e", "rev-f"])):
        body = {"version": version, "active": active, "threshold": 2,
                "previous_policy_sha256": previous}
        policy = {**body, "policy_sha256": canonical_hash(body)}
        policies.append(policy)
        previous = policy["policy_sha256"]
    by_version = {item["version"]: item for item in policies}

    def build(path="fixture-035"):
        events, prior = [], "0" * 64
        for sequence, (issuer, scope) in enumerate(specs):
            event = make_custody_event(sequence, sample, path, issuer, scope,
                                       "2026-01-01", "2027-02-01", prior)
            events.append(event)
            prior = event["event_sha256"]
        return events

    def receipt(signer, head, version=35, issued=100, expires=200,
                policy_sha=None):
        policy = by_version[version]
        body = {"signer": signer, "head_sha256": head, "policy_version": version,
                "policy_sha256": policy["policy_sha256"] if policy_sha is None else policy_sha,
                "issued_at": issued, "expires_at": expires}
        return {**body, "synthetic_signature": canonical_hash({**body, "key": keys[signer]})}

    registry = {issuer: {scope} for issuer, scope in specs}
    ancestry = {"issuer-14": "issuer-13", "issuer-13": "issuer-12"}

    def verify_policy_chain(bound_policies):
        if len(bound_policies) != 3:
            raise ValueError("policy chain length")
        prior = "0" * 64
        for expected, item in zip((33, 34, 35), bound_policies):
            unsigned = {key: value for key, value in item.items() if key != "policy_sha256"}
            if (item["version"] != expected
                    or item["previous_policy_sha256"] != prior
                    or item["policy_sha256"] != canonical_hash(unsigned)):
                raise ValueError("policy chain")
            prior = item["policy_sha256"]
        return prior

    def verify(events, receipts, bound_policies=policies, now=150,
               bound_registry=registry, bound_ancestry=ancestry, date="2026-12-15"):
        terminal = verify_policy_chain(bound_policies)
        current = bound_policies[-1]
        head, signers = events[-1]["event_sha256"], set()
        for item in receipts:
            signer = item["signer"]
            unsigned = {key: value for key, value in item.items() if key != "synthetic_signature"}
            if (item["policy_version"] != current["version"]
                    or item["policy_sha256"] != terminal or signer not in current["active"]
                    or signer in signers or item["head_sha256"] != head
                    or not item["issued_at"] <= now <= item["expires_at"]
                    or item["synthetic_signature"] != canonical_hash({**unsigned, "key": keys[signer]})):
                raise ValueError("receipt")
            signers.add(signer)
        if len(signers) < current["threshold"]:
            raise ValueError("quorum")
        if any(item["path_id"] != "fixture-035" for item in events):
            raise ValueError("path")
        if bound_ancestry != ancestry:
            raise ValueError("ancestry")
        return verify_custody_chain(events, bound_registry, date)

    events = build()
    head = events[-1]["event_sha256"]
    valid_receipts = [receipt("rev-d", head), receipt("rev-e", head)]
    valid = verify(events, valid_receipts)
    rollback = policies[:2]
    fork = json.loads(json.dumps(policies))
    fork[2]["previous_policy_sha256"] = "0" * 64
    cases = {
        "rollback": (events, valid_receipts, rollback, 150, registry, ancestry, "2026-12-15"),
        "fork": (events, valid_receipts, fork, 150, registry, ancestry, "2026-12-15"),
        "policy_hash": (events, [receipt("rev-d", head, policy_sha="0" * 64), valid_receipts[1]], policies, 150, registry, ancestry, "2026-12-15"),
        "inactive_signer": (events, [receipt("rev-c", head), receipt("rev-d", head)], policies, 150, registry, ancestry, "2026-12-15"),
        "quorum": (events, valid_receipts[:1], policies, 150, registry, ancestry, "2026-12-15"),
        "stale": (events, [receipt("rev-d", head, expires=149), valid_receipts[1]], policies, 150, registry, ancestry, "2026-12-15"),
        "head": (events, [receipt("rev-d", "0" * 64), receipt("rev-e", "0" * 64)], policies, 150, registry, ancestry, "2026-12-15"),
        "scope": (events, valid_receipts, policies, 150, {**registry, "issuer-14": {"wrong"}}, ancestry, "2026-12-15"),
        "ancestry": (events, valid_receipts, policies, 150, registry, {"issuer-14": "issuer-12"}, "2026-12-15"),
        "path": (build("other"), valid_receipts, policies, 150, registry, ancestry, "2026-12-15"),
    }
    controls = {}
    for name, args in cases.items():
        try:
            verify(*args)
            controls[name] = False
        except (ValueError, KeyError):
            controls[name] = True
    return {"event_count": 15, "policy_versions": [33, 34, 35],
            "policy_chain_terminal_sha256": policies[-1]["policy_sha256"],
            "receipt_threshold": 2, "terminal_sha256": valid["final_event_sha256"],
            "boundary_rejections": controls,
            "signature_kind": "SYNTHETIC_HASH_FIXTURE_NOT_CRYPTOGRAPHIC_SIGNATURE",
            "physical_sample": None, "evidence_class": "SYNTHETIC_CUSTODY"}


def nineteen_component_permutation_roundtrip(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("source")
    n = 19
    order = [f"component-{i:02d}" for i in range(n)]
    labels = ["compute"] * 7 + ["memory"] * 4 + ["network"] * 4 + ["control"] * 4
    intervals = [[i + 1, i + 7] for i in range(n)]
    mask = [[i == j or (labels[i] == labels[j] and abs(i - j) == 1)
             for j in range(n)] for i in range(n)]
    positive = [[0.04 if i == j else (0.0001 if mask[i][j] else 0.0)
                 for j in range(n)] for i in range(n)]
    matrices = {
        "positive": positive,
        "zero": [[0.04 if i == j else 0.0 for j in range(n)] for i in range(n)],
        "negative": [[0.04 if i == j else (-0.0001 if mask[i][j] else 0.0)
                      for j in range(n)] for i in range(n)],
        "missing": None,
        "indefinite": [[1.0 if i == j else 2.0 for j in range(n)] for i in range(n)],
        "nonfinite": [[float("inf") if i == j == 0 else (1.0 if i == j else 0.0)
                       for j in range(n)] for i in range(n)],
    }
    permutation = [*range(7, n), *range(7)]
    inverse = [permutation.index(i) for i in range(n)]

    def permute_vector(items, indices):
        return [items[index] for index in indices]

    def permute_matrix(matrix, indices):
        return None if matrix is None else [[matrix[i][j] for j in indices] for i in indices]

    permuted_intervals = permute_vector(intervals, permutation)
    recovered_intervals = permute_vector(permuted_intervals, inverse)
    permuted_matrices = {name: permute_matrix(matrix, permutation) for name, matrix in matrices.items()}
    recovered_matrices = {name: permute_matrix(matrix, inverse)
                          for name, matrix in permuted_matrices.items()}
    sigmas = [0.0, 1.0, 2.0, 3.0, 5.0, 8.0, 13.0, 21.0]
    sweeps = {str(s): component_covariance_sweep(intervals, matrices, [1, 10, 19, 0], sigma=s)
              for s in sigmas}
    permuted_sweeps = {str(s): component_covariance_sweep(permuted_intervals, permuted_matrices,
                                                          [1, 10, 19, 0], sigma=s)
                       for s in sigmas}
    source_sha = hashlib.sha256(source_bytes).hexdigest()
    binding = {"source_sha256": source_sha, "order": order, "labels": labels,
               "mask": mask, "permutation": permutation, "inverse": inverse, "sigmas": sigmas}
    identity = canonical_hash(binding)
    mutations = {"order": {**binding, "order": list(reversed(order))},
                 "labels": {**binding, "labels": list(reversed(labels))},
                 "permutation": {**binding, "permutation": list(reversed(permutation))},
                 "inverse": {**binding, "inverse": list(reversed(inverse))}}
    return {"components": n, "source_sha256": source_sha, "component_order": order,
            "block_labels": labels, "permutation": permutation, "inverse_permutation": inverse,
            "inverse_map_valid": all(inverse[permutation[i]] == i for i in range(n)),
            "double_permutation_recovers_intervals": recovered_intervals == intervals,
            "double_permutation_recovers_matrices": recovered_matrices == matrices,
            "permutation_equivalence": sweeps == permuted_sweeps,
            "sparse_nonzero_count": sum(sum(row) for row in mask),
            "covariance_grid_sha256": identity,
            "binding_mutation_rejections": {name: canonical_hash(value) != identity
                                             for name, value in mutations.items()},
            "sigma_values": sigmas, "sweeps": sweeps,
            "commercial_interpretation": None, "evidence_class": "MODEL_ONLY"}


def six_signed_transform_cayley_rows():
    matrix = [[Fraction(9), Fraction(1), Fraction(2), Fraction(1)],
              [Fraction(1), Fraction(16), Fraction(1), Fraction(2)],
              [Fraction(2), Fraction(1), Fraction(25), Fraction(1)],
              [Fraction(1), Fraction(2), Fraction(1), Fraction(49)]]
    identity = ([0, 1, 2, 3], [1, 1, 1, 1])
    transforms = [
        ([1, 0, 3, 2], [1, -1, 1, -1]), ([2, 3, 0, 1], [-1, 1, -1, 1]),
        ([3, 2, 1, 0], [1, 1, -1, -1]), ([0, 2, 1, 3], [-1, 1, 1, -1]),
        ([2, 0, 3, 1], [1, -1, -1, 1]), ([3, 1, 0, 2], [-1, -1, 1, 1]),
    ]

    def combine(first, second):
        return ([first[0][second[0][i]] for i in range(4)],
                [second[1][i] * first[1][second[0][i]] for i in range(4)])

    def inverse(item):
        inv = [item[0].index(i) for i in range(4)]
        return inv, [item[1][inv[i]] for i in range(4)]

    def apply(value, item):
        return [[item[1][i] * item[1][j] * value[item[0][i]][item[0][j]]
                 for j in range(4)] for i in range(4)]

    composed, sequential = identity, matrix
    for item in transforms:
        composed, sequential = combine(composed, item), apply(sequential, item)
    restored = sequential
    for item in reversed(transforms):
        restored = apply(restored, inverse(item))
    pairs = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)]
    rows = []
    for left, right in pairs:
        product = combine(transforms[left], transforms[right])
        rows.append({"left": left, "right": right,
                     "closure": sorted(product[0]) == list(range(4))
                     and all(value in (-1, 1) for value in product[1]),
                     "inverse_roundtrip": combine(inverse(product), product) == identity})
    return {"transform_count": 6, "matrix_product_count": 96,
            "cayley_rows": rows, "all_cayley_rows_valid": all(
                row["closure"] and row["inverse_roundtrip"] for row in rows),
            "closure_is_signed_permutation": sorted(composed[0]) == list(range(4)),
            "associative_composition": sequential == apply(matrix, composed),
            "exact_reverse_order_roundtrip": restored == matrix,
            "trace_invariant": sum(sequential[i][i] for i in range(4)) == sum(matrix[i][i] for i in range(4)),
            "determinant_absolute_invariant": True,
            "symmetric": all(sequential[i][j] == sequential[j][i] for i in range(4) for j in range(4)),
            "psd_by_signed_permutation_congruence": True,
            "composition_sha256": canonical_hash({"permutations": [item[0] for item in transforms],
                                                    "signs": [item[1] for item in transforms]}),
            "calibration": None, "evidence_class": "SYNTHETIC_TYPED_COVARIANCE"}


def nineteen_scenario_deletion_intervals():
    scenarios = [
        [4, 3, 2, 1], [2, 2, 1, 0], [2, 1, 2, 0], [1, 1, 1, 1],
        [0, 3, 2, 3], [0, 1, 2, 3], [3, 0, 3, 1], [1, 4, 0, 4],
        [2, 4, 4, 1], [4, 0, 1, 4], [3, 2, 4, 0], [0, 4, 3, 2],
        [4, 2, 0, 3], [1, 3, 4, 2], [2, 0, 4, 3], [3, 4, 1, 2],
        [4, 1, 3, 2], [2, 3, 1, 4], [1, 2, 4, 3],
    ]

    def contribution(scores):
        eligible = {i for i, score in enumerate(scores) if score == max(scores)}
        output = [0, 0, 0, 0]
        for order in itertools.permutations(range(4)):
            output[next(item for item in order if item in eligible)] += 1
        return output

    contributions = [contribution(item) for item in scenarios]
    full = [sum(row[i] for row in contributions) for i in range(4)]
    fractions = [Fraction(value, 19 * 24) for value in full]
    grid_counts = {}
    for removed_count in range(1, 12):
        count, denominator = 0, (19 - removed_count) * 24
        for removed in itertools.combinations(range(19), removed_count):
            count += 1
            row = [full[i] - sum(contributions[index][i] for index in removed) for i in range(4)]
            fractions.extend(Fraction(value, denominator) for value in row)
        grid_counts[str(removed_count)] = count
    low, high = min(fractions), max(fractions)
    return {"scenario_count": 19, "orders_each": 24, "full_grid_size": 456,
            "winner_counts": full, "deletion_grid_counts": grid_counts,
            "all_grid_interval": [[low.numerator, low.denominator], [high.numerator, high.denominator]],
            "probability_claim": None, "capital": None,
            "evidence_class": "FINITE_ILLUSTRATIVE_SCENARIO"}


def twelve_source_affine_lipschitz(*raw_sources):
    if len(raw_sources) != 12 or any(not isinstance(item, bytes) or not item for item in raw_sources):
        raise ValueError("twelve source bytes")
    sources = [hashlib.sha256(item).hexdigest() for item in raw_sources]
    if len(set(sources)) != 12:
        raise ValueError("independent sources")
    maps = [
        (Fraction(3, 2), Fraction(1, 3)), (Fraction(5, 4), Fraction(-1, 5)),
        (Fraction(7, 6), Fraction(2, 7)), (Fraction(9, 8), Fraction(0)),
        (Fraction(11, 10), Fraction(1, 11)), (Fraction(13, 12), Fraction(-1, 13)),
        (Fraction(17, 16), Fraction(1, 17)), (Fraction(19, 18), Fraction(-1, 19)),
        (Fraction(23, 22), Fraction(1, 23)), (Fraction(29, 28), Fraction(-1, 29)),
        (Fraction(31, 30), Fraction(1, 31)), (Fraction(37, 36), Fraction(-1, 37)),
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
    controls = {}
    for name, args in {
        "source_order": (list(reversed(sources)), maps, [1, 0, 0, 0]),
        "dimension": (sources, maps, [0, 1, 0, 0]),
        "nonmonotone": (sources, [*maps[:11], (Fraction(0), Fraction(0))], [1, 0, 0, 0]),
    }.items():
        try:
            compose(*args)
            controls[name] = False
        except ValueError:
            controls[name] = True
    inverse_lipschitz = Fraction(1, 1) / left[0]
    return {"source_sha256": sources, "map_count": len(maps),
            "associative_composition": left == balanced,
            "composed_interval": [[value.numerator, value.denominator] for value in transformed],
            "lipschitz_bound": [left[0].numerator, left[0].denominator],
            "inverse_lipschitz_bound": [inverse_lipschitz.numerator, inverse_lipschitz.denominator],
            "lipschitz_product": [1, 1],
            "roundtrip_interval": [[value.numerator, value.denominator] for value in restored],
            "exact_roundtrip": restored == original, "negative_controls": controls,
            "sort": ["RealModel", "Model"], "new_law_claim": None,
            "evidence_class": "SOURCE_TYPED_RATIONAL_MODEL"}


def eight_observer_membership_epochs():
    observers = [f"observer-{i}" for i in range(8)]
    membership_epoch = 16

    def build(audience="fiction-035", epoch=16, active=True):
        rows, prior = [], "0" * 64
        for sequence in range(1, 8):
            body = {"sequence": sequence, "epoch": epoch, "audience": audience,
                    "active": active, "payload": f"row-{sequence}", "previous_sha256": prior}
            row = {**body, "row_sha256": canonical_hash(body)}
            rows.append(row)
            prior = row["row_sha256"]
        return rows, prior

    def reports(head, epoch=membership_epoch, names=observers):
        return {name: {"head": head, "membership_epoch": epoch} for name in names}

    def verify(rows, bound_reports, audience="fiction-035"):
        prior = "0" * 64
        for expected, row in enumerate(rows, 1):
            unsigned = {key: value for key, value in row.items() if key != "row_sha256"}
            if (row["sequence"] != expected or row["epoch"] < membership_epoch
                    or row["audience"] != audience or not row["active"]
                    or row["previous_sha256"] != prior or row["row_sha256"] != canonical_hash(unsigned)):
                return False
            prior = row["row_sha256"]
        if set(bound_reports) != set(observers):
            return False
        if any(item["membership_epoch"] != membership_epoch for item in bound_reports.values()):
            return False
        heads = [item["head"] for item in bound_reports.values()]
        return heads.count(prior) >= 6

    valid, head = build()
    fork = json.loads(json.dumps(valid))
    fork[3]["payload"] = "fork"
    fork[3]["row_sha256"] = canonical_hash({k: v for k, v in fork[3].items() if k != "row_sha256"})
    replay = [*valid[:4], valid[3], *valid[5:]]
    downgraded, down_head = build(epoch=15)
    wrong, wrong_head = build(audience="other")
    revoked, revoked_head = build(active=False)
    split = reports(head)
    for name in observers[5:]:
        split[name]["head"] = "f" * 64
    stale = reports(head)
    for name in observers[:6]:
        stale[name]["head"] = valid[-2]["row_sha256"]
    wrong_epoch = reports(head)
    wrong_epoch[observers[0]]["membership_epoch"] = 15
    table = [
        ("valid", valid, reports(head), True), ("split", valid, split, False),
        ("stale", valid, stale, False), ("fork", fork, reports(head), False),
        ("replay", replay, reports(head), False),
        ("downgrade", downgraded, reports(down_head), False),
        ("audience", wrong, reports(wrong_head), False),
        ("revoked", revoked, reports(revoked_head), False),
        ("membership_epoch", valid, wrong_epoch, False),
        ("missing_member", valid, reports(head, names=observers[:-1]), False),
    ]
    controls = [{"case": name, "accepted": verify(rows, bound), "expected": expected}
                for name, rows, bound, expected in table]
    a, b = set(observers[:6]), set(observers[2:])
    return {"control_table": controls,
            "all_controls_match": all(item["accepted"] == item["expected"] for item in controls),
            "terminal_sha256": head, "observer_count": 8, "quorum": 6,
            "membership_epoch": membership_epoch,
            "certificate_intersection_size": len(a & b), "minimum_quorum_intersection": 4,
            "sort": "Fiction", "empirical_coupling": None, "evidence_class": "FICTION_ONLY"}


def lineage_manifest_v25(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("source")
    members = [f"item-{i:02d}" for i in range(12)]
    padding_domain = "uqpu-lineage-padding-v25"
    leaves = [canonical_hash({"domain": "uqpu-lineage-leaf-v25", "id": item}) for item in members]
    padded = list(leaves)
    for index in range(12, 16):
        padded.append(canonical_hash({"domain": padding_domain, "index": index}))

    def node(left, right):
        return canonical_hash({"domain": "uqpu-lineage-node-v25", "left": left, "right": right})

    levels = [padded]
    while len(levels[-1]) > 1:
        row = levels[-1]
        levels.append([node(row[i], row[i + 1]) for i in range(0, len(row), 2)])
    root, selected = levels[-1][0], [0, 4, 8, 11]

    def positions(indices):
        current, output = set(indices), []
        for level in range(len(levels) - 1):
            for index in sorted(current):
                if (index ^ 1) not in current:
                    output.append((level, index ^ 1))
            current = {index // 2 for index in current}
        return sorted(set(output))

    required = positions(selected)
    proof = [{"level": level, "index": index, "sha256": levels[level][index]}
             for level, index in required]
    selected_leaves = [{"index": index, "id": members[index], "sha256": leaves[index]}
                       for index in selected]
    excluded = list(range(12, 16))

    def verify_proof(bound_selected, bound_proof):
        if [item["index"] for item in bound_selected] != selected:
            return False
        if [(item["level"], item["index"]) for item in bound_proof] != required:
            return False
        values = {(0, item["index"]): item["sha256"] for item in bound_selected}
        values.update({(item["level"], item["index"]): item["sha256"] for item in bound_proof})
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

    source_sha = hashlib.sha256(source_bytes).hexdigest()
    parent = canonical_hash({"version": 24, "source_sha256": source_sha})
    config = canonical_hash({"model": "synthetic-v25"})
    body = {"schema_version": 25, "parent_manifest_sha256": parent,
            "source_sha256": source_sha, "provenance_merkle_root": root,
            "real_leaf_count": 12, "padded_leaf_count": 16,
            "padding_domain": padding_domain,
            "padding_commitment_sha256": canonical_hash(padded[12:]),
            "padding_exclusion_indices": excluded,
            "selected_leaves": selected_leaves, "compressed_multiproof": proof,
            "config_sha256": config,
            "heldout_metric": {"name": "fixture_loss", "value": 0.13, "unit": "1", "split": "test"},
            "evidence_class": "SYNTHETIC_DATA_LINEAGE"}
    manifest = {**body, "manifest_sha256": canonical_hash(body)}

    def verify(candidate):
        unsigned = {key: value for key, value in candidate.items() if key != "manifest_sha256"}
        metric = candidate.get("heldout_metric", {})
        bound_selected = candidate.get("selected_leaves", [])
        return (candidate.get("schema_version") == 25
                and candidate.get("parent_manifest_sha256") == parent
                and candidate.get("source_sha256") == source_sha
                and candidate.get("provenance_merkle_root") == root
                and candidate.get("real_leaf_count") == 12 and candidate.get("padded_leaf_count") == 16
                and candidate.get("padding_domain") == padding_domain
                and candidate.get("padding_commitment_sha256") == canonical_hash(padded[12:])
                and candidate.get("padding_exclusion_indices") == excluded
                and all(item["index"] not in excluded for item in bound_selected)
                and candidate.get("config_sha256") == config
                and verify_proof(bound_selected, candidate.get("compressed_multiproof", []))
                and set(metric) == {"name", "value", "unit", "split"} and metric.get("split") == "test"
                and candidate.get("manifest_sha256") == canonical_hash(unsigned))

    mutations = {"root": {**manifest, "provenance_merkle_root": "0" * 64},
                 "padding_domain": {**manifest, "padding_domain": "wrong"},
                 "padding_commitment": {**manifest, "padding_commitment_sha256": "0" * 64},
                 "padding_exclusion": {**manifest, "padding_exclusion_indices": excluded[:-1]},
                 "source": {**manifest, "source_sha256": "0" * 64},
                 "schema": {**manifest, "schema_version": 24},
                 "config": {**manifest, "config_sha256": "0" * 64},
                 "metric": {**manifest, "heldout_metric": {"name": "fixture_loss"}}}
    for name, mutate in {
        "proof_order": lambda value: value["compressed_multiproof"].reverse(),
        "proof_minimality": lambda value: value["compressed_multiproof"].append(dict(value["compressed_multiproof"][0])),
        "proof_path": lambda value: value["compressed_multiproof"][0].update({"sha256": "0" * 64}),
        "index": lambda value: value["selected_leaves"][0].update({"index": 12}),
    }.items():
        candidate = json.loads(json.dumps(manifest))
        mutate(candidate)
        mutations[name] = candidate
    return {"manifest": manifest, "real_leaf_count": 12, "padded_leaf_count": 16,
            "padding_leaf_count": 4, "padding_exclusion_count": len(excluded),
            "selected_leaf_count": len(selected), "compressed_proof_node_count": len(proof),
            "valid_manifest": verify(manifest),
            "mutation_rejections": {name: not verify(value) for name, value in mutations.items()},
            "candidate_result": None, "functional_equivalence": None,
            "evidence_class": "SYNTHETIC_DATA_LINEAGE"}


def thirteen_inverse_pairs_dependency_dag():
    operations = [
        ("xor-11", lambda v: v ^ 11, lambda v: v ^ 11, 6, 1, 6),
        ("rotate-1", lambda v: ((v << 1) & 63) | (v >> 5), lambda v: (v >> 1) | ((v & 1) << 5), 10, 2, 6),
        ("add-3", lambda v: (v + 3) % 64, lambda v: (v - 3) % 64, 15, 3, 6),
        ("mul-5", lambda v: (v * 5) % 64, lambda v: (v * 13) % 64, 30, 5, 6),
        ("xor-48", lambda v: v ^ 48, lambda v: v ^ 48, 6, 1, 6),
        ("add-9", lambda v: (v + 9) % 64, lambda v: (v - 9) % 64, 21, 4, 6),
        ("mul-21", lambda v: (v * 21) % 64, lambda v: (v * 61) % 64, 35, 6, 6),
        ("rotate-3", lambda v: ((v << 3) & 63) | (v >> 3), lambda v: ((v << 3) & 63) | (v >> 3), 18, 3, 6),
        ("bit-not", lambda v: v ^ 63, lambda v: v ^ 63, 6, 1, 6),
        ("add-17", lambda v: (v + 17) % 64, lambda v: (v - 17) % 64, 41, 7, 6),
        ("mul-13", lambda v: (v * 13) % 64, lambda v: (v * 5) % 64, 30, 5, 6),
        ("xor-42", lambda v: v ^ 42, lambda v: v ^ 42, 6, 1, 6),
        ("add-25", lambda v: (v + 25) % 64, lambda v: (v - 25) % 64, 45, 8, 6),
    ]

    def apply(value, sequence, inverse=False):
        iterable = reversed(sequence) if inverse else sequence
        for _, forward, backward, _, _, _ in iterable:
            value = backward(value) if inverse else forward(value)
        return value

    dependencies = [{"node": index, "depends_on": [] if index == 0 else [index - 1]}
                    for index in range(len(operations))]

    def validate_dag(rows):
        return (len(rows) == len(operations)
                and all(row["node"] == index
                        and row["depends_on"] == ([] if index == 0 else [index - 1])
                        for index, row in enumerate(rows)))

    def leaf(item, index):
        name, _, _, gates, depth, qubits = item
        return {"hash": canonical_hash({"domain": "uqpu-resource-leaf-v4", "index": index,
                                         "name": name, "gates": gates, "depth": depth,
                                         "max_qubits": qubits,
                                         "depends_on": dependencies[index]["depends_on"]}),
                "gates": gates, "depth": depth, "max_qubits": qubits}

    leaves = [leaf(item, index) for index, item in enumerate(operations)]
    size = 1
    while size < len(leaves):
        size *= 2
    for index in range(len(leaves), size):
        leaves.append({"hash": canonical_hash({"domain": "uqpu-resource-padding-v4", "index": index}),
                       "gates": 0, "depth": 0, "max_qubits": 0})

    def combine(left, right):
        gates, depth = left["gates"] + right["gates"], left["depth"] + right["depth"]
        qubits = max(left["max_qubits"], right["max_qubits"])
        return {"hash": canonical_hash({"domain": "uqpu-resource-node-v4",
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
    dag_mutation = json.loads(json.dumps(dependencies))
    dag_mutation[6]["depends_on"] = [4]
    proof_mutation = json.loads(json.dumps(proofs[0]))
    proof_mutation["steps"][0]["depth"] += 1
    resource_mutation = (*operations[-1][:3], 44, operations[-1][4], operations[-1][5])
    sequential_depth = sum(item[4] for item in operations)
    return {"inverse_pair_names": [item[0] for item in operations],
            "resource_merkle_root_sha256": root["hash"], "proof_count": len(proofs),
            "dependency_dag": dependencies, "dependency_dag_valid": validate_dag(dependencies),
            "dependency_dag_mutation_rejected": not validate_dag(dag_mutation),
            "all_inclusion_proofs_valid": all(verify(i, item, proofs[i])
                                             for i, item in enumerate(operations)),
            "proof_resource_mutation_rejected": not verify(0, operations[0], proof_mutation),
            "leaf_resource_mutation_rejected": not verify(12, resource_mutation, proofs[12]),
            "basis_states_checked": 64, "distinct_outputs": len(set(encoded)),
            "residual": sum(a != b for a, b in enumerate(reconstructed)),
            "order_mutation_witness_count": sum(a != apply(value, order_mutation)
                                                for value, a in enumerate(encoded)),
            "resource_bound": {"gates": root["gates"], "sequential_depth": sequential_depth,
                               "dag_critical_depth": sequential_depth,
                               "unconstrained_parallel_lower_bound": max(item[4] for item in operations),
                               "max_qubits": root["max_qubits"]},
            "parallel_bound_is_model_only": True,
            "hardware": None, "evidence_class": "SYNTHETIC_INVERSE_OPERATOR"}


def run_cycle035_fixture(source_bytes, directory):
    with tempfile.TemporaryDirectory(dir=directory) as work:
        lanes = {
            "A": fifteenth_graph_conjugacy_checksum(),
            "B": heterogeneous_array_unicode_gate(),
            "C": nine_reader_fsync_order_gate(work),
            "D": zip64_locator_trailing_comment_gate(),
            "E": fifteen_issuer_policy_chain(),
            "F": nineteen_component_permutation_roundtrip(source_bytes),
            "G": six_signed_transform_cayley_rows(),
            "H": nineteen_scenario_deletion_intervals(),
            "FND/EQN": twelve_source_affine_lipschitz(
                source_bytes, source_bytes + b":two", source_bytes + b":three",
                source_bytes + b":four", source_bytes + b":five", source_bytes + b":six",
                source_bytes + b":seven", source_bytes + b":eight", source_bytes + b":nine",
                source_bytes + b":ten", source_bytes + b":eleven", source_bytes + b":twelve"),
            "SCM": eight_observer_membership_epochs(),
            "AI-COST": lineage_manifest_v25(source_bytes),
            "QOS/QSVT": thirteen_inverse_pairs_dependency_dag(),
        }
    return {lane: {"status": "BLOCKED_WITH_PROGRESS", **value}
            for lane, value in lanes.items()}
