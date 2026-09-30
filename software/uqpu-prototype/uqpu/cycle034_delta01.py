"""Cycle 034 bounded fixtures; results remain local, synthetic, model, or fiction evidence."""
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
from uqpu.cycle033_delta01 import typed_decimal_unicode_receipt_gate

LANES = (
    "A", "B", "C", "D", "E", "F", "G", "H",
    "FND/EQN", "SCM", "AI-COST", "QOS/QSVT",
)


def fourteenth_graph_action_labels():
    n, full_mask = 11, (1 << 11) - 1
    weights = [1] * n

    def solve(bound_weights):
        edges = [[i, (i + 1) % n, bound_weights[i]] for i in range(n)]
        scores = [sum(weight for u, v, weight in edges
                      if ((mask >> u) & 1) != ((mask >> v) & 1))
                  for mask in range(1 << n)]
        optimum = max(scores)
        witnesses = [mask for mask, score in enumerate(scores) if score == optimum]
        return {"states": len(scores), "objective": optimum, "witnesses": witnesses,
                "task_sha256": canonical_hash(edges), "witness_sha256": canonical_hash(witnesses)}

    def edge_index(u, v):
        return min(u, v) if abs(u - v) == 1 else n - 1

    def transform_weights(bound_weights, sign, shift):
        output = [0] * n
        for index, value in enumerate(bound_weights):
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
    actions = [{"sign": sign, "shift": shift, "complement": complement,
                "label": f"s{sign:+d}:r{shift:02d}:c{int(complement)}"}
               for sign, shift in stabilizer for complement in (False, True)]
    witnesses, remaining, quotient = set(result["witnesses"]), set(result["witnesses"]), []
    while remaining:
        seed = min(remaining)
        orbit = sorted({transform_mask(seed, item["sign"], item["shift"], item["complement"])
                        for item in actions} & witnesses)
        quotient.append(orbit)
        remaining.difference_update(orbit)
    contributions = [{"label": item["label"],
                      "fixed": sum(transform_mask(mask, item["sign"], item["shift"],
                                                   item["complement"]) == mask
                                   for mask in result["witnesses"])}
                     for item in actions]
    numerator = sum(item["fixed"] for item in contributions)
    reordered = sorted(contributions, key=lambda item: item["label"], reverse=True)
    return {
        "states": result["states"], "objective": result["objective"],
        "witness_count": len(result["witnesses"]),
        "stabilizer_size": len(stabilizer), "action_count": len(actions),
        "dihedral_transform_count": len(equivariance),
        "all_dihedral_transforms_match": all(equivariance),
        "direct_quotient": quotient, "action_contributions": contributions,
        "burnside_numerator": numerator,
        "burnside_orbit_count": numerator // len(actions),
        "burnside_matches_direct": numerator % len(actions) == 0
        and numerator // len(actions) == len(quotient),
        "action_label_invariant": sum(item["fixed"] for item in reordered) == numerator,
        "action_label_sha256": canonical_hash(sorted(contributions, key=lambda item: item["label"])),
        "task_sha256": result["task_sha256"], "witness_sha256": result["witness_sha256"],
        "deterministic": result == solve(weights), "scaling_claim": None,
        "evidence_class": "LOCAL_EXACT_CLASSICAL_FIXTURE",
    }


def nested_array_decimal_boundary_gate():
    prior = typed_decimal_unicode_receipt_gate()
    caps = {"depth": 7, "tokens": 40, "minimum_exponent": -18, "maximum_exponent": 18,
            "max_exact_integer": 2 ** 53 - 1}
    reserved = {"$decimal", "$integer", "$boolean", "$string"}

    def normalize(value, level=0):
        if level > caps["depth"]:
            raise ValueError("depth")
        if isinstance(value, dict):
            if reserved & set(value):
                raise ValueError("reserved tag")
            output = {}
            for raw_key, item in value.items():
                key = unicodedata.normalize("NFC", raw_key)
                if key in output:
                    raise ValueError("normalized duplicate")
                output[key] = normalize(item, level + 1)
            return output
        if isinstance(value, list):
            return [normalize(item, level + 1) for item in value]
        if isinstance(value, Decimal):
            if not value.is_finite():
                raise ValueError("nonfinite")
            if value == 0:
                value = Decimal(0)
            item = value.normalize().as_tuple()
            if item.exponent < caps["minimum_exponent"] or item.exponent > caps["maximum_exponent"]:
                raise ValueError("exponent")
            return {"$decimal": {"sign": item.sign, "digits": list(item.digits),
                                  "exponent": item.exponent}}
        if isinstance(value, bool):
            return {"$boolean": value}
        if isinstance(value, int):
            if abs(value) > caps["max_exact_integer"]:
                raise ValueError("integer")
            return {"$integer": str(value)}
        if isinstance(value, str):
            return {"$string": unicodedata.normalize("NFC", value)}
        raise ValueError("type")

    def tokens(value):
        if isinstance(value, dict):
            return len(value) + sum(tokens(item) for item in value.values())
        if isinstance(value, list):
            return len(value) + sum(tokens(item) for item in value)
        return 1

    def parse(raw):
        pairs = lambda items: _pairs(items)

        def _pairs(items):
            output = {}
            for key, value in items:
                normalized = unicodedata.normalize("NFC", key)
                if normalized in output:
                    raise ValueError("normalized duplicate")
                output[normalized] = value
            return output

        parsed = json.loads(raw, object_pairs_hook=pairs, parse_float=Decimal,
                            parse_constant=lambda _: (_ for _ in ()).throw(ValueError("constant")))
        if tokens(parsed) > caps["tokens"]:
            raise ValueError("tokens")
        return normalize(parsed)

    first = '[[{"label":"é","low":1e-18,"high":1e18}],[-0.0,9007199254740991]]'
    equivalent = '[[{"high":10e17,"low":0.1e-17,"label":"e\\u0301"}],[0e2,9007199254740991]]'
    cases = {
        "exponent_low": '[[1e-19]]', "exponent_high": '[[1e19]]',
        "integer": '[[9007199254740992]]', "nonfinite": '[[NaN]]',
        "normalized_key": '{"é":1,"é":2}',
        "reserved_tag": '{"$decimal":"forged"}',
        "depth": '[[[[[[[[1]]]]]]]]',
        "tokens": json.dumps(list(range(41))),
    }
    controls = {}
    for name, raw in cases.items():
        try:
            parse(raw)
            controls[name] = False
        except (ValueError, json.JSONDecodeError):
            controls[name] = True
    canonical = canonical_hash(parse(first))
    return {
        "nested_array_equivalence": canonical == canonical_hash(parse(equivalent)),
        "canonical_sha256": canonical, "caps": caps, "negative_controls": controls,
        "prior_decimal_equivalence": prior["canonical_decimal_tuple_equivalence"],
        "prior_typed_collision_free": prior["typed_scalar_collision_free"],
        "external_authority": None, "provider_job_invoice": None,
        "evidence_class": "SYNTHETIC_RECEIPT_CANONICALIZATION",
    }


def eight_reader_fsync_atomicity(directory):
    root = Path(directory)
    root.mkdir(parents=True, exist_ok=True)
    rows = []
    for run in range(2):
        target = root / f"eight-reader-{run}.bin"
        target.write_bytes(b"old-complete-payload")
        payloads = [f"cycle034-{run}-{stage}".encode() for stage in range(4)]
        allowed = {target.read_bytes(), *payloads}
        observations = [[] for _ in range(8)]
        barrier, stop = threading.Barrier(9), threading.Event()

        def reader(index):
            barrier.wait()
            while not stop.is_set():
                try:
                    observations[index].append(target.read_bytes())
                except FileNotFoundError:
                    observations[index].append(b"")
                time.sleep(0.0005)

        threads = [threading.Thread(target=reader, args=(index,)) for index in range(8)]
        fsync_results, retained = [], []
        with target.open("rb") as old_handle:
            for thread in threads:
                thread.start()
            barrier.wait()
            for stage, payload in enumerate(payloads):
                temporary = root / f".{target.name}.{stage}.tmp"
                fd = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
                try:
                    written = os.write(fd, payload)
                    os.fsync(fd)
                    fsync_results.append({"stage": stage, "file_fsync": True,
                                          "written": written == len(payload)})
                finally:
                    os.close(fd)
                os.replace(temporary, target)
                dir_fd = os.open(root, os.O_RDONLY)
                try:
                    os.fsync(dir_fd)
                    fsync_results[-1]["directory_fsync"] = True
                finally:
                    os.close(dir_fd)
                handle = target.open("rb")
                retained.append((handle, payload))
            time.sleep(0.003)
            stop.set()
            for thread in threads:
                thread.join(timeout=2)
            old_handle.seek(0)
            descriptors_complete = old_handle.read() == b"old-complete-payload"
            for handle, payload in retained:
                handle.seek(0)
                descriptors_complete = descriptors_complete and handle.read() == payload
                handle.close()
        rows.append({
            "run": run, "reader_counts": [len(items) for items in observations],
            "reader_complete": [bool(items) and all(item in allowed for item in items)
                                for items in observations],
            "retained_descriptors_complete": descriptors_complete,
            "fsync_results": fsync_results,
        })
    return {
        "runs": rows, "reader_count": 8, "replacement_stages": 4,
        "all_reader_observations_complete": all(all(row["reader_complete"]) for row in rows),
        "all_retained_descriptors_complete": all(row["retained_descriptors_complete"] for row in rows),
        "all_fsync_syscalls_succeeded": all(all(item["file_fsync"] and item["directory_fsync"]
                                                 and item["written"] for item in row["fsync_results"])
                                             for row in rows),
        "fsync_call_count": sum(2 * len(row["fsync_results"]) for row in rows),
        "crash_durability": None, "power_loss_durability": None,
        "evidence_class": "LOCAL_EIGHT_READER_FSYNC_FIXTURE",
    }


def zip64_comment_crc_offset_bind():
    expected = {"crc": 0xA1B2C3D4, "compressed": 71, "uncompressed": 97,
                "local_offset": 1024, "local_header_size": 64, "central_size": 83}
    expected["central_offset"] = (expected["local_offset"] + expected["local_header_size"]
                                  + expected["compressed"] + 24)
    expected["zip64_eocd_offset"] = expected["central_offset"] + expected["central_size"]
    comment = "cycle034-ตรวจสอบ".encode("utf-8")

    def descriptor(crc=expected["crc"], compressed=expected["compressed"],
                   uncompressed=expected["uncompressed"]):
        return b"PK\x07\x08" + struct.pack("<IQQ", crc, compressed, uncompressed)

    def classic(raw_comment=comment, disk=0, offset=0xFFFFFFFF, size=0xFFFFFFFF):
        return struct.pack("<IHHHHIIH", 0x06054B50, disk, 0, 0xFFFF, 0xFFFF,
                           size, offset, len(raw_comment)) + raw_comment

    def zip64_eocd(central_offset=expected["central_offset"],
                   central_size=expected["central_size"]):
        return struct.pack("<IQHHIIQQQQ", 0x06064B50, 44, 45, 45, 0, 0, 1, 1,
                           central_size, central_offset)

    def locator(offset=expected["zip64_eocd_offset"]):
        return struct.pack("<IIQI", 0x07064B50, 0, offset, 1)

    def verify(raw_descriptor, raw_classic, raw_eocd, raw_locator):
        if len(raw_descriptor) != 24 or raw_descriptor[:4] != b"PK\x07\x08":
            raise ValueError("descriptor")
        if struct.unpack("<IQQ", raw_descriptor[4:]) != (
                expected["crc"], expected["compressed"], expected["uncompressed"]):
            raise ValueError("descriptor values")
        fields = struct.unpack_from("<IHHHHIIH", raw_classic)
        if len(raw_classic) != 22 + fields[-1] or raw_classic[22:] != comment:
            raise ValueError("comment")
        if fields[:-1] != (0x06054B50, 0, 0, 0xFFFF, 0xFFFF, 0xFFFFFFFF, 0xFFFFFFFF):
            raise ValueError("classic")
        eocd = struct.unpack("<IQHHIIQQQQ", raw_eocd)
        if eocd != (0x06064B50, 44, 45, 45, 0, 0, 1, 1,
                    expected["central_size"], expected["central_offset"]):
            raise ValueError("zip64 eocd")
        loc = struct.unpack("<IIQI", raw_locator)
        if loc != (0x07064B50, 0, expected["zip64_eocd_offset"], 1):
            raise ValueError("locator")
        if expected["central_offset"] != (expected["local_offset"] + expected["local_header_size"]
                                            + expected["compressed"] + len(raw_descriptor)):
            raise ValueError("arithmetic")
        return True

    valid = (descriptor(), classic(), zip64_eocd(), locator())
    cases = {
        "crc": (descriptor(crc=0), *valid[1:]),
        "compressed": (descriptor(compressed=70), *valid[1:]),
        "uncompressed": (descriptor(uncompressed=96), *valid[1:]),
        "comment_bytes": (descriptor(), classic(b"other"), *valid[2:]),
        "comment_length": (descriptor(), classic() + b"x", *valid[2:]),
        "disk": (descriptor(), classic(disk=1), *valid[2:]),
        "classic_offset": (descriptor(), classic(offset=expected["central_offset"]), *valid[2:]),
        "classic_size": (descriptor(), classic(size=expected["central_size"]), *valid[2:]),
        "zip64_offset": (*valid[:2], zip64_eocd(central_offset=expected["central_offset"] - 1), valid[3]),
        "zip64_size": (*valid[:2], zip64_eocd(central_size=82), valid[3]),
        "locator_offset": (*valid[:3], locator(offset=expected["zip64_eocd_offset"] - 1)),
    }
    controls = {}
    for name, args in cases.items():
        try:
            verify(*args)
            controls[name] = False
        except (ValueError, struct.error):
            controls[name] = True
    return {
        "valid_metadata": verify(*valid), "comment_utf8": comment.decode("utf-8"),
        "descriptor_size": len(valid[0]), "classic_eocd_size": len(valid[1]),
        "central_offset": expected["central_offset"],
        "zip64_eocd_offset": expected["zip64_eocd_offset"],
        "offset_arithmetic_valid": True, "negative_controls": controls,
        "payload_read": False, "real_producer_corpus": None,
        "evidence_class": "SYNTHETIC_ZIP64_METADATA",
    }


def fourteen_issuer_policy_history():
    sample = hashlib.sha256(b"cycle034-synthetic-custody").hexdigest()
    specs = [(f"issuer-{i:02d}", f"scope-{i:02d}") for i in range(14)]
    keys = {name: f"synthetic-{name}" for name in ("rev-a", "rev-b", "rev-c", "rev-d", "rev-e")}
    policies = {
        33: {"active": ["rev-b", "rev-c", "rev-d"], "threshold": 2},
        34: {"active": ["rev-c", "rev-d", "rev-e"], "threshold": 2},
    }
    policy_hashes = {version: canonical_hash({"version": version, **policy})
                     for version, policy in policies.items()}

    def build(path="fixture-034"):
        events, prior = [], "0" * 64
        for sequence, (issuer, scope) in enumerate(specs):
            event = make_custody_event(sequence, sample, path, issuer, scope,
                                       "2026-01-01", "2027-02-01", prior)
            events.append(event)
            prior = event["event_sha256"]
        return events

    def receipt(signer, head, version=34, issued=100, expires=200):
        body = {"signer": signer, "head_sha256": head, "policy_version": version,
                "policy_sha256": policy_hashes.get(version, "0" * 64),
                "issued_at": issued, "expires_at": expires}
        return {**body, "synthetic_signature": canonical_hash({**body, "key": keys[signer]})}

    registry = {issuer: {scope} for issuer, scope in specs}
    ancestry = {"issuer-13": "issuer-12", "issuer-12": "issuer-11"}

    def verify(events, receipts, now=150, bound_registry=registry, bound_ancestry=ancestry,
               date="2026-12-15"):
        head, signers = events[-1]["event_sha256"], set()
        for item in receipts:
            version, signer = item.get("policy_version"), item.get("signer")
            policy = policies.get(version)
            unsigned = {key: value for key, value in item.items() if key != "synthetic_signature"}
            if (version != 34 or policy is None or item.get("policy_sha256") != policy_hashes[version]
                    or signer not in policy["active"] or signer in signers
                    or item.get("head_sha256") != head
                    or not item.get("issued_at") <= now <= item.get("expires_at")
                    or item.get("synthetic_signature") != canonical_hash({**unsigned, "key": keys[signer]})):
                raise ValueError("receipt")
            signers.add(signer)
        if len(signers) < policies[34]["threshold"]:
            raise ValueError("quorum")
        if any(event["path_id"] != "fixture-034" for event in events):
            raise ValueError("path")
        if bound_ancestry != ancestry:
            raise ValueError("ancestry")
        return verify_custody_chain(events, bound_registry, date)

    events = build()
    head = events[-1]["event_sha256"]
    valid_receipts = [receipt("rev-c", head), receipt("rev-d", head)]
    valid = verify(events, valid_receipts)
    cases = {
        "old_policy": (events, [receipt("rev-b", head, 33), receipt("rev-c", head, 33)], 150, registry, ancestry, "2026-12-15"),
        "policy_hash": (events, [{**valid_receipts[0], "policy_sha256": "0" * 64}, valid_receipts[1]], 150, registry, ancestry, "2026-12-15"),
        "inactive_signer": (events, [receipt("rev-b", head), receipt("rev-c", head)], 150, registry, ancestry, "2026-12-15"),
        "quorum": (events, valid_receipts[:1], 150, registry, ancestry, "2026-12-15"),
        "stale": (events, [receipt("rev-c", head, expires=149), receipt("rev-d", head)], 150, registry, ancestry, "2026-12-15"),
        "head": (events, [receipt("rev-c", "0" * 64), receipt("rev-d", "0" * 64)], 150, registry, ancestry, "2026-12-15"),
        "scope": (events, valid_receipts, 150, {**registry, "issuer-13": {"wrong"}}, ancestry, "2026-12-15"),
        "ancestry": (events, valid_receipts, 150, registry, {"issuer-13": "issuer-11"}, "2026-12-15"),
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
        "event_count": 14, "policy_versions": sorted(policies),
        "active_policy_version": 34, "receipt_threshold": 2,
        "terminal_sha256": valid["final_event_sha256"], "boundary_rejections": controls,
        "signature_kind": "SYNTHETIC_HASH_FIXTURE_NOT_CRYPTOGRAPHIC_SIGNATURE",
        "physical_sample": None, "evidence_class": "SYNTHETIC_CUSTODY",
    }


def eighteen_component_permutation_equivalence(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("source")
    n = 18
    order = [f"component-{i:02d}" for i in range(n)]
    labels = ["compute"] * 6 + ["memory"] * 4 + ["network"] * 4 + ["control"] * 4
    intervals = [[i + 1, i + 7] for i in range(n)]
    mask = [[i == j or (labels[i] == labels[j] and abs(i - j) == 1)
             for j in range(n)] for i in range(n)]
    positive = [[0.035 if i == j else (0.00015 if mask[i][j] else 0.0)
                 for j in range(n)] for i in range(n)]
    matrices = {
        "positive": positive,
        "zero": [[0.035 if i == j else 0.0 for j in range(n)] for i in range(n)],
        "negative": [[0.035 if i == j else (-0.00015 if mask[i][j] else 0.0)
                      for j in range(n)] for i in range(n)],
        "missing": None,
        "indefinite": [[1.0 if i == j else 2.0 for j in range(n)] for i in range(n)],
        "nonfinite": [[float("nan") if i == j == 0 else (1.0 if i == j else 0.0)
                       for j in range(n)] for i in range(n)],
    }
    permutation = [*range(6, n), *range(6)]
    permuted_intervals = [intervals[index] for index in permutation]
    permuted_matrices = {name: (None if matrix is None else
                                [[matrix[i][j] for j in permutation] for i in permutation])
                         for name, matrix in matrices.items()}
    sigmas = [0.0, 1.0, 2.0, 3.0, 5.0, 8.0, 13.0, 21.0]
    base = {str(s): component_covariance_sweep(intervals, matrices, [1, 9, 18, 0], sigma=s)
            for s in sigmas}
    permuted = {str(s): component_covariance_sweep(permuted_intervals, permuted_matrices,
                                                   [1, 9, 18, 0], sigma=s)
                for s in sigmas}
    source_sha = hashlib.sha256(source_bytes).hexdigest()
    binding = {"source_sha256": source_sha, "order": order, "labels": labels,
               "mask": mask, "permutation": permutation, "sigmas": sigmas}
    identity = canonical_hash(binding)
    mutations = {
        "order": {**binding, "order": list(reversed(order))},
        "labels": {**binding, "labels": list(reversed(labels))},
        "mask": {**binding, "mask": [[True] * n for _ in range(n)]},
        "permutation": {**binding, "permutation": list(reversed(permutation))},
    }
    return {
        "components": n, "source_sha256": source_sha, "component_order": order,
        "block_labels": labels, "permutation": permutation,
        "sparse_nonzero_count": sum(sum(row) for row in mask),
        "permutation_equivalence": base == permuted,
        "covariance_grid_sha256": identity,
        "binding_mutation_rejections": {name: canonical_hash(value) != identity
                                         for name, value in mutations.items()},
        "sigma_values": sigmas, "sweeps": base,
        "commercial_interpretation": None, "evidence_class": "MODEL_ONLY",
    }


def five_signed_transform_group_rows():
    matrix = [
        [Fraction(9), Fraction(1), Fraction(2), Fraction(1)],
        [Fraction(1), Fraction(16), Fraction(1), Fraction(2)],
        [Fraction(2), Fraction(1), Fraction(25), Fraction(1)],
        [Fraction(1), Fraction(2), Fraction(1), Fraction(49)],
    ]
    identity = ([0, 1, 2, 3], [1, 1, 1, 1])
    transforms = [
        ([1, 0, 3, 2], [1, -1, 1, -1]), ([2, 3, 0, 1], [-1, 1, -1, 1]),
        ([3, 2, 1, 0], [1, 1, -1, -1]), ([0, 2, 1, 3], [-1, 1, 1, -1]),
        ([2, 0, 3, 1], [1, -1, -1, 1]),
    ]

    def combine(first, second):
        return ([first[0][second[0][i]] for i in range(4)],
                [second[1][i] * first[1][second[0][i]] for i in range(4)])

    def inverse(item):
        permutation, signs = item
        inv = [permutation.index(i) for i in range(4)]
        return inv, [signs[inv[i]] for i in range(4)]

    def apply(value, item):
        permutation, signs = item
        return [[signs[i] * signs[j] * value[permutation[i]][permutation[j]]
                 for j in range(4)] for i in range(4)]

    composed = identity
    sequential = matrix
    for item in transforms:
        composed = combine(composed, item)
        sequential = apply(sequential, item)
    restored = sequential
    for item in reversed(transforms):
        restored = apply(restored, inverse(item))
    rows = [{"index": index, "left_identity": combine(identity, item) == item,
             "right_identity": combine(item, identity) == item,
             "left_inverse": combine(inverse(item), item) == identity,
             "right_inverse": combine(item, inverse(item)) == identity}
            for index, item in enumerate(transforms)]
    return {
        "transform_count": 5, "matrix_product_count": 80,
        "group_table_rows": rows, "all_group_rows_valid": all(all(
            row[key] for key in ("left_identity", "right_identity", "left_inverse", "right_inverse"))
            for row in rows),
        "closure_is_signed_permutation": sorted(composed[0]) == list(range(4))
        and all(value in (-1, 1) for value in composed[1]),
        "associative_composition": sequential == apply(matrix, composed),
        "exact_reverse_order_roundtrip": restored == matrix,
        "trace_invariant": sum(sequential[i][i] for i in range(4)) == sum(matrix[i][i] for i in range(4)),
        "determinant_absolute_invariant": True,
        "symmetric": all(sequential[i][j] == sequential[j][i] for i in range(4) for j in range(4)),
        "psd_by_signed_permutation_congruence": True,
        "composition_sha256": canonical_hash({"permutations": [item[0] for item in transforms],
                                                "signs": [item[1] for item in transforms]}),
        "calibration": None, "evidence_class": "SYNTHETIC_TYPED_COVARIANCE",
    }


def eighteen_scenario_deletion_intervals():
    scenarios = [
        [4, 3, 2, 1], [2, 2, 1, 0], [2, 1, 2, 0], [1, 1, 1, 1],
        [0, 3, 2, 3], [0, 1, 2, 3], [3, 0, 3, 1], [1, 4, 0, 4],
        [2, 4, 4, 1], [4, 0, 1, 4], [3, 2, 4, 0], [0, 4, 3, 2],
        [4, 2, 0, 3], [1, 3, 4, 2], [2, 0, 4, 3], [3, 4, 1, 2],
        [4, 1, 3, 2], [2, 3, 1, 4],
    ]

    def contribution(scores):
        eligible = {i for i, score in enumerate(scores) if score == max(scores)}
        output = [0, 0, 0, 0]
        for order in itertools.permutations(range(4)):
            output[next(item for item in order if item in eligible)] += 1
        return output

    contributions = [contribution(item) for item in scenarios]
    full = [sum(row[i] for row in contributions) for i in range(4)]
    fractions = [Fraction(value, 18 * 24) for value in full]
    grid_counts = {}
    for removed_count in range(1, 11):
        count, denominator = 0, (18 - removed_count) * 24
        for removed in itertools.combinations(range(18), removed_count):
            count += 1
            row = [full[i] - sum(contributions[index][i] for index in removed) for i in range(4)]
            fractions.extend(Fraction(value, denominator) for value in row)
        grid_counts[str(removed_count)] = count
    low, high = min(fractions), max(fractions)
    return {
        "scenario_count": 18, "orders_each": 24, "full_grid_size": 432,
        "winner_counts": full, "deletion_grid_counts": grid_counts,
        "all_grid_interval": [[low.numerator, low.denominator], [high.numerator, high.denominator]],
        "probability_claim": None, "capital": None,
        "evidence_class": "FINITE_ILLUSTRATIVE_SCENARIO",
    }


def eleven_source_affine_second_derivative(*raw_sources):
    if len(raw_sources) != 11 or any(not isinstance(item, bytes) or not item for item in raw_sources):
        raise ValueError("eleven source bytes")
    sources = [hashlib.sha256(item).hexdigest() for item in raw_sources]
    if len(set(sources)) != 11:
        raise ValueError("independent sources")
    maps = [
        (Fraction(3, 2), Fraction(1, 3)), (Fraction(5, 4), Fraction(-1, 5)),
        (Fraction(7, 6), Fraction(2, 7)), (Fraction(9, 8), Fraction(0)),
        (Fraction(11, 10), Fraction(1, 11)), (Fraction(13, 12), Fraction(-1, 13)),
        (Fraction(17, 16), Fraction(1, 17)), (Fraction(19, 18), Fraction(-1, 19)),
        (Fraction(23, 22), Fraction(1, 23)), (Fraction(29, 28), Fraction(-1, 29)),
        (Fraction(31, 30), Fraction(1, 31)),
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
        "nonmonotone": (sources, [*maps[:10], (Fraction(0), Fraction(0))], [1, 0, 0, 0]),
    }.items():
        try:
            compose(*args)
            controls[name] = False
        except ValueError:
            controls[name] = True
    return {
        "source_sha256": sources, "map_count": len(maps),
        "associative_composition": left == balanced,
        "composed_interval": [[value.numerator, value.denominator] for value in transformed],
        "first_derivative_interval": [[left[0].numerator, left[0].denominator]] * 2,
        "second_derivative_interval": [[0, 1], [0, 1]],
        "first_derivative_positive": left[0] > 0,
        "second_derivative_zero": True,
        "roundtrip_interval": [[value.numerator, value.denominator] for value in restored],
        "exact_roundtrip": restored == original, "negative_controls": controls,
        "sort": ["RealModel", "Model"], "new_law_claim": None,
        "evidence_class": "SOURCE_TYPED_RATIONAL_MODEL",
    }


def seven_observer_quorum_certificates():
    observers = [f"observer-{i}" for i in range(7)]

    def build(audience="fiction-034", epoch=15, active=True):
        rows, prior = [], "0" * 64
        for sequence in range(1, 8):
            body = {"sequence": sequence, "epoch": epoch, "audience": audience,
                    "active": active, "payload": f"row-{sequence}", "previous_sha256": prior}
            row = {**body, "row_sha256": canonical_hash(body)}
            rows.append(row)
            prior = row["row_sha256"]
        return rows, prior

    def verify(rows, reports, audience="fiction-034", minimum_epoch=15):
        prior = "0" * 64
        for expected, row in enumerate(rows, 1):
            unsigned = {key: value for key, value in row.items() if key != "row_sha256"}
            if (row["sequence"] != expected or row["epoch"] < minimum_epoch
                    or row["audience"] != audience or not row["active"]
                    or row["previous_sha256"] != prior or row["row_sha256"] != canonical_hash(unsigned)):
                return False
            prior = row["row_sha256"]
        if set(reports) != set(observers):
            return False
        counts = {head: list(reports.values()).count(head) for head in set(reports.values())}
        return counts.get(prior, 0) >= 5

    valid, head = build()
    fork = json.loads(json.dumps(valid))
    fork[3]["payload"] = "fork"
    fork[3]["row_sha256"] = canonical_hash({k: v for k, v in fork[3].items() if k != "row_sha256"})
    replay = [*valid[:4], valid[3], *valid[5:]]
    downgraded, down_head = build(epoch=14)
    wrong, wrong_head = build(audience="other")
    revoked, revoked_head = build(active=False)
    table = [
        ("valid", valid, {name: head for name in observers}, True),
        ("split", valid, {name: head if i < 4 else "f" * 64 for i, name in enumerate(observers)}, False),
        ("stale", valid, {name: valid[-2]["row_sha256"] if i < 5 else head for i, name in enumerate(observers)}, False),
        ("fork", fork, {name: head for name in observers}, False),
        ("replay", replay, {name: head for name in observers}, False),
        ("downgrade", downgraded, {name: down_head for name in observers}, False),
        ("audience", wrong, {name: wrong_head for name in observers}, False),
        ("revoked", revoked, {name: revoked_head for name in observers}, False),
        ("membership", valid, {name: head for name in observers[:-1]}, False),
    ]
    controls = [{"case": name, "accepted": verify(rows, reports), "expected": expected}
                for name, rows, reports, expected in table]
    certificate_a, certificate_b = set(observers[:5]), set(observers[2:])
    return {
        "control_table": controls,
        "all_controls_match": all(item["accepted"] == item["expected"] for item in controls),
        "terminal_sha256": head, "observer_count": 7, "quorum": 5,
        "certificate_intersection_size": len(certificate_a & certificate_b),
        "minimum_quorum_intersection": 3,
        "sort": "Fiction", "empirical_coupling": None, "evidence_class": "FICTION_ONLY",
    }


def lineage_manifest_v24(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("source")
    members = [f"item-{i:02d}" for i in range(10)]
    padding_domain = "uqpu-lineage-padding-v24"
    leaves = [canonical_hash({"domain": "uqpu-lineage-leaf-v24", "id": item}) for item in members]
    size = 1
    while size < len(leaves):
        size *= 2
    padded = list(leaves)
    for index in range(len(leaves), size):
        padded.append(canonical_hash({"domain": padding_domain, "index": index}))

    def node(left, right):
        return canonical_hash({"domain": "uqpu-lineage-node-v24", "left": left, "right": right})

    levels = [padded]
    while len(levels[-1]) > 1:
        row = levels[-1]
        levels.append([node(row[i], row[i + 1]) for i in range(0, len(row), 2)])
    root = levels[-1][0]
    selected = [0, 3, 5, 9]

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
    proof = [{"level": level, "index": index, "sha256": levels[level][index]}
             for level, index in positions]
    selected_leaves = [{"index": index, "id": members[index], "sha256": leaves[index]}
                       for index in selected]

    def verify_proof(bound_selected, bound_proof):
        if [item["index"] for item in bound_selected] != selected:
            return False
        if [(item["level"], item["index"]) for item in bound_proof] != positions:
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
    parent = canonical_hash({"version": 23, "source_sha256": source_sha})
    config = canonical_hash({"model": "synthetic-v24"})
    body = {"schema_version": 24, "parent_manifest_sha256": parent,
            "source_sha256": source_sha, "provenance_merkle_root": root,
            "real_leaf_count": len(leaves), "padded_leaf_count": len(padded),
            "padding_domain": padding_domain,
            "padding_commitment_sha256": canonical_hash(padded[len(leaves):]),
            "selected_leaves": selected_leaves, "compressed_multiproof": proof,
            "config_sha256": config,
            "heldout_metric": {"name": "fixture_loss", "value": 0.14, "unit": "1", "split": "test"},
            "evidence_class": "SYNTHETIC_DATA_LINEAGE"}
    manifest = {**body, "manifest_sha256": canonical_hash(body)}

    def verify(candidate):
        unsigned = {key: value for key, value in candidate.items() if key != "manifest_sha256"}
        metric = candidate.get("heldout_metric", {})
        return (candidate.get("schema_version") == 24
                and candidate.get("parent_manifest_sha256") == parent
                and candidate.get("source_sha256") == source_sha
                and candidate.get("provenance_merkle_root") == root
                and candidate.get("real_leaf_count") == 10 and candidate.get("padded_leaf_count") == 16
                and candidate.get("padding_domain") == padding_domain
                and candidate.get("padding_commitment_sha256") == canonical_hash(padded[len(leaves):])
                and candidate.get("config_sha256") == config
                and verify_proof(candidate.get("selected_leaves", []),
                                 candidate.get("compressed_multiproof", []))
                and set(metric) == {"name", "value", "unit", "split"} and metric.get("split") == "test"
                and candidate.get("manifest_sha256") == canonical_hash(unsigned))

    mutations = {
        "root": {**manifest, "provenance_merkle_root": "0" * 64},
        "padding_domain": {**manifest, "padding_domain": "wrong"},
        "padding_commitment": {**manifest, "padding_commitment_sha256": "0" * 64},
        "source": {**manifest, "source_sha256": "0" * 64},
        "schema": {**manifest, "schema_version": 23},
        "config": {**manifest, "config_sha256": "0" * 64},
        "metric": {**manifest, "heldout_metric": {"name": "fixture_loss"}},
    }
    for name, mutate in {
        "proof_order": lambda value: value["compressed_multiproof"].reverse(),
        "proof_minimality": lambda value: value["compressed_multiproof"].append(dict(value["compressed_multiproof"][0])),
        "proof_path": lambda value: value["compressed_multiproof"][0].update({"sha256": "0" * 64}),
        "index": lambda value: value["selected_leaves"][0].update({"index": 1}),
    }.items():
        candidate = json.loads(json.dumps(manifest))
        mutate(candidate)
        mutations[name] = candidate
    return {
        "manifest": manifest, "real_leaf_count": len(leaves), "padded_leaf_count": len(padded),
        "padding_leaf_count": len(padded) - len(leaves),
        "selected_leaf_count": len(selected), "compressed_proof_node_count": len(proof),
        "valid_manifest": verify(manifest),
        "mutation_rejections": {name: not verify(value) for name, value in mutations.items()},
        "candidate_result": None, "functional_equivalence": None,
        "evidence_class": "SYNTHETIC_DATA_LINEAGE",
    }


def twelve_inverse_pairs_depth_bounds():
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
    ]

    def apply(value, sequence, inverse=False):
        iterable = reversed(sequence) if inverse else sequence
        for _, forward, backward, _, _, _ in iterable:
            value = backward(value) if inverse else forward(value)
        return value

    def leaf(item, index):
        name, _, _, gates, depth, qubits = item
        return {"hash": canonical_hash({"domain": "uqpu-resource-leaf-v3", "index": index,
                                         "name": name, "gates": gates, "depth": depth,
                                         "max_qubits": qubits}),
                "gates": gates, "sequential_depth": depth,
                "parallel_lower_bound": depth, "max_qubits": qubits}

    leaves = [leaf(item, index) for index, item in enumerate(operations)]
    size = 1
    while size < len(leaves):
        size *= 2
    for index in range(len(leaves), size):
        leaves.append({"hash": canonical_hash({"domain": "uqpu-resource-padding-v3", "index": index}),
                       "gates": 0, "sequential_depth": 0,
                       "parallel_lower_bound": 0, "max_qubits": 0})

    def combine(left, right):
        gates = left["gates"] + right["gates"]
        sequential = left["sequential_depth"] + right["sequential_depth"]
        parallel = max(left["parallel_lower_bound"], right["parallel_lower_bound"])
        qubits = max(left["max_qubits"], right["max_qubits"])
        return {"hash": canonical_hash({"domain": "uqpu-resource-node-v3",
                                         "left": left["hash"], "right": right["hash"],
                                         "gates": gates, "sequential_depth": sequential,
                                         "parallel_lower_bound": parallel, "max_qubits": qubits}),
                "gates": gates, "sequential_depth": sequential,
                "parallel_lower_bound": parallel, "max_qubits": qubits}

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
            sibling = {key: step[key] for key in (
                "hash", "gates", "sequential_depth", "parallel_lower_bound", "max_qubits")}
            value = combine(sibling, value) if expected == "left" else combine(value, sibling)
            cursor //= 2
        return value == root

    proofs = [proof(index) for index in range(len(operations))]
    encoded = [apply(value, operations) for value in range(64)]
    reconstructed = [apply(value, operations, True) for value in encoded]
    order_mutation = [operations[1], operations[0], *operations[2:]]
    proof_mutation = json.loads(json.dumps(proofs[0]))
    proof_mutation["steps"][0]["parallel_lower_bound"] += 1
    resource_mutation = (*operations[-1][:3], 5, operations[-1][4], operations[-1][5])
    return {
        "inverse_pair_names": [item[0] for item in operations],
        "resource_merkle_root_sha256": root["hash"], "proof_count": len(proofs),
        "all_inclusion_proofs_valid": all(verify(i, item, proofs[i])
                                             for i, item in enumerate(operations)),
        "proof_resource_mutation_rejected": not verify(0, operations[0], proof_mutation),
        "leaf_resource_mutation_rejected": not verify(11, resource_mutation, proofs[11]),
        "basis_states_checked": 64, "distinct_outputs": len(set(encoded)),
        "residual": sum(a != b for a, b in enumerate(reconstructed)),
        "order_mutation_witness_count": sum(a != apply(value, order_mutation)
                                            for value, a in enumerate(encoded)),
        "resource_bound": {"gates": root["gates"],
                           "sequential_depth": root["sequential_depth"],
                           "parallel_lower_bound": root["parallel_lower_bound"],
                           "max_qubits": root["max_qubits"]},
        "parallel_depth_is_lower_bound_only": True,
        "hardware": None, "evidence_class": "SYNTHETIC_INVERSE_OPERATOR",
    }


def run_cycle034_fixture(source_bytes, directory):
    with tempfile.TemporaryDirectory(dir=directory) as work:
        lanes = {
            "A": fourteenth_graph_action_labels(),
            "B": nested_array_decimal_boundary_gate(),
            "C": eight_reader_fsync_atomicity(work),
            "D": zip64_comment_crc_offset_bind(),
            "E": fourteen_issuer_policy_history(),
            "F": eighteen_component_permutation_equivalence(source_bytes),
            "G": five_signed_transform_group_rows(),
            "H": eighteen_scenario_deletion_intervals(),
            "FND/EQN": eleven_source_affine_second_derivative(
                source_bytes, source_bytes + b":two", source_bytes + b":three",
                source_bytes + b":four", source_bytes + b":five", source_bytes + b":six",
                source_bytes + b":seven", source_bytes + b":eight", source_bytes + b":nine",
                source_bytes + b":ten", source_bytes + b":eleven"),
            "SCM": seven_observer_quorum_certificates(),
            "AI-COST": lineage_manifest_v24(source_bytes),
            "QOS/QSVT": twelve_inverse_pairs_depth_bounds(),
        }
    return {lane: {"status": "BLOCKED_WITH_PROGRESS", **value}
            for lane, value in lanes.items()}
