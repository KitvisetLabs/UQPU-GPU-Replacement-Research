"""Cycle 037 bounded fixtures; outputs remain local, synthetic, model, or fiction evidence."""
from __future__ import annotations

from decimal import Decimal
from fractions import Fraction
import hashlib
import itertools
import json
import math
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


def seventeenth_graph_orbit_histogram():
    n, full_mask = 13, (1 << 13) - 1
    weights = [1] * n

    def solve(bound):
        scores = [sum(bound[index] for index in range(n)
                      if ((mask >> index) & 1) != ((mask >> ((index + 1) % n)) & 1))
                  for mask in range(1 << n)]
        optimum = max(scores)
        witnesses = [mask for mask, score in enumerate(scores) if score == optimum]
        return {"states": len(scores), "objective": optimum, "witnesses": witnesses,
                "task_sha256": canonical_hash(bound),
                "witness_sha256": canonical_hash(witnesses)}

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
    witness_set, remaining, quotient = set(result["witnesses"]), set(result["witnesses"]), []
    while remaining:
        seed = min(remaining)
        orbit = sorted({transform_mask(seed, *action) for action in actions} & witness_set)
        quotient.append(orbit)
        remaining.difference_update(orbit)
    fixed = [sum(transform_mask(mask, *action) == mask for mask in result["witnesses"])
             for action in actions]
    representatives = [min(orbit) for orbit in quotient]
    reconstructed = sorted({transform_mask(seed, *action)
                            for seed in representatives for action in actions} & witness_set)
    histogram = {}
    for orbit in quotient:
        histogram[str(len(orbit))] = histogram.get(str(len(orbit)), 0) + 1
    numerator = sum(fixed)
    return {"states": result["states"], "objective": result["objective"],
            "witness_count": len(result["witnesses"]), "stabilizer_size": len(stabilizer),
            "action_count": len(actions), "all_dihedral_transforms_match": all(equivariance),
            "canonical_orbit_representatives": representatives,
            "orbit_size_histogram": histogram,
            "representative_reconstruction_matches": reconstructed == result["witnesses"],
            "reconstruction_sha256": canonical_hash(reconstructed),
            "burnside_numerator": numerator, "burnside_orbit_count": numerator // len(actions),
            "burnside_matches_direct": numerator % len(actions) == 0
            and numerator // len(actions) == len(quotient),
            "task_sha256": result["task_sha256"], "witness_sha256": result["witness_sha256"],
            "deterministic": result == solve(weights), "scaling_claim": None,
            "evidence_class": "LOCAL_EXACT_CLASSICAL_FIXTURE"}


def schema_version_transition_gate():
    max_integer, max_depth, max_tokens = 9007199254740991, 10, 68

    def reject_text(value):
        return any(0xD800 <= ord(char) <= 0xDFFF
                   or unicodedata.category(char) in {"Cc", "Cs"} for char in value)

    def canonical(value):
        state = {"tokens": 0}

        def walk(item, path, depth):
            state["tokens"] += 1
            if depth > max_depth or state["tokens"] > max_tokens:
                raise ValueError("caps")
            if isinstance(item, bool):
                return [path, "bool", item]
            if isinstance(item, int):
                if abs(item) > max_integer:
                    raise ValueError("integer")
                return [path, "integer", str(item)]
            if isinstance(item, Decimal):
                if not item.is_finite():
                    raise ValueError("nonfinite")
                bound = item.normalize()
                if bound.as_tuple().exponent < -36 or bound.as_tuple().exponent > 36:
                    raise ValueError("exponent")
                return [path, "decimal", str(bound)]
            if isinstance(item, str):
                if reject_text(item):
                    raise ValueError("unicode")
                return [path, "string", unicodedata.normalize("NFC", item)]
            if isinstance(item, list):
                return [path, "array", [walk(child, f"{path}/{index}", depth + 1)
                                        for index, child in enumerate(item)]]
            if isinstance(item, dict):
                normalized = {}
                for key, child in item.items():
                    if not isinstance(key, str) or reject_text(key):
                        raise ValueError("key")
                    bound = unicodedata.normalize("NFC", key)
                    if bound in normalized or bound == "$type":
                        raise ValueError("key collision")
                    normalized[bound] = child
                return [path, "object", [[key, walk(normalized[key], f"{path}/{key}", depth + 1)]
                                          for key in sorted(normalized)]]
            raise ValueError("tag")

        return walk(value, "$", 0)

    def upgrade(value):
        if not isinstance(value, dict) or value.get("schema_version") != 1:
            raise ValueError("version")
        if set(value) != {"schema_version", "values", "label"}:
            raise ValueError("v1 path")
        return {"schema_version": 2,
                "payload": {"items": value["values"], "label": value["label"]}}

    def validate_v2(value):
        if (not isinstance(value, dict) or value.get("schema_version") != 2
                or set(value) != {"schema_version", "payload"}
                or not isinstance(value["payload"], dict)
                or set(value["payload"]) != {"items", "label"}
                or not isinstance(value["payload"]["items"], list)
                or not isinstance(value["payload"]["label"], str)):
            raise ValueError("v2 path")
        normalized = []
        for item in value["payload"]["items"]:
            token = canonical(item)
            digest = canonical_hash(token)
            if digest in normalized:
                raise ValueError("duplicate normalized value")
            normalized.append(digest)

    def bind(value):
        validate_v2(value)
        return canonical_hash(canonical(value))

    old = {"schema_version": 1,
           "values": [Decimal("1E-36"), Decimal("9.99E+36"), "e\u0301"],
           "label": "transition"}
    current = {"payload": {"label": "transition",
                           "items": [Decimal("0.000000000000000000000000000000000001"),
                                     Decimal("9.99E+36"), "é"]},
               "schema_version": 2}
    malformed = {
        "version_low": {"schema_version": 0, "payload": current["payload"]},
        "version_high": {"schema_version": 3, "payload": current["payload"]},
        "path": {"schema_version": 2, "payload": {"label": "x"}},
        "tag": {"schema_version": 2, "payload": {"label": "x", "items": {}}},
        "duplicate_value": {"schema_version": 2, "payload": {"label": "x",
                             "items": [Decimal("1.0"), Decimal("1.00")]}},
    }
    controls = {}
    for name, value in malformed.items():
        try:
            bind(value)
            controls[name] = False
        except (ValueError, TypeError):
            controls[name] = True
    raw_controls = {
        "normalized_key": {"é": 1, "e\u0301": 2},
        "exponent_low": Decimal("1E-37"), "exponent_high": Decimal("1E+37"),
        "depth": [[[[[[[[[[[0]]]]]]]]]]], "tokens": list(range(69)),
        "integer": max_integer + 1, "surrogate": "\ud800",
    }
    for name, value in raw_controls.items():
        try:
            canonical(value)
            controls[name] = False
        except (ValueError, TypeError):
            controls[name] = True
    return {"upgrade_matches_v2": bind(upgrade(old)) == bind(current),
            "canonical_sha256": bind(current), "negative_controls": controls,
            "caps": {"depth": max_depth, "tokens": max_tokens,
                     "minimum_exponent": -36, "maximum_exponent": 36,
                     "max_exact_integer": max_integer},
            "external_authority": None, "provider_job_invoice": None,
            "evidence_class": "SYNTHETIC_RECEIPT_CANONICALIZATION"}


def eleven_reader_partial_write_gate(directory):
    root = Path(directory)
    rows, file_calls, directory_calls = [], 0, 0
    for run in range(2):
        work = root / f"cycle037-{run}"
        work.mkdir(parents=True, exist_ok=True)
        target = work / "state.bin"
        target.write_bytes(b"old-complete-payload")
        old_handle = target.open("rb")
        observations = [[] for _ in range(11)]
        start, stop = threading.Event(), threading.Event()

        def reader(index):
            start.wait()
            while not stop.is_set():
                try:
                    observations[index].append(target.read_bytes())
                except FileNotFoundError:
                    observations[index].append(b"missing")
                time.sleep(0.0005)

        threads = [threading.Thread(target=reader, args=(index,), daemon=True)
                   for index in range(11)]
        for thread in threads:
            thread.start()
        retained, traces = [], []
        start.set()
        time.sleep(0.005)
        for stage in range(7):
            payload = f"cycle037-run{run}-stage{stage}-".encode() + b"w" * (stage + 19)
            temporary = work / f"pending-{stage}.bin"
            with temporary.open("wb") as handle:
                handle.write(payload)
                handle.flush()
                os.fsync(handle.fileno())
                file_calls += 1
            trace = ["write", "file_fsync"]
            os.replace(temporary, target)
            trace.append("replace")
            descriptor = os.open(work, os.O_RDONLY)
            try:
                os.fsync(descriptor)
                directory_calls += 1
            finally:
                os.close(descriptor)
            trace.append("directory_fsync")
            traces.append(trace)
            retained.append((target.open("rb"), payload))
            time.sleep(0.004)
        stop.set()
        for thread in threads:
            thread.join(timeout=2)
        allowed = {b"old-complete-payload", *(item[1] for item in retained)}
        old_handle.seek(0)
        retained_complete = old_handle.read() == b"old-complete-payload"
        old_handle.close()
        for handle, expected in retained:
            handle.seek(0)
            retained_complete = retained_complete and handle.read() == expected
            handle.close()
        rows.append({"run": run, "reader_counts": [len(items) for items in observations],
                     "reader_complete": [bool(items) and all(item in allowed for item in items)
                                         for items in observations],
                     "retained_descriptors_complete": retained_complete,
                     "stage_orders": traces,
                     "all_stage_orders_valid": all(item == ["write", "file_fsync", "replace", "directory_fsync"]
                                                   for item in traces)})

    failure_controls = {
        "partial_write": {"trace": ["partial_write"], "replace_occurred": False,
                          "evidence_promoted": False, "rejected_as_durable": True},
        "file_fsync": {"trace": ["write"], "replace_occurred": False,
                       "evidence_promoted": False, "rejected_as_durable": True},
        "directory_fsync": {"trace": ["write", "file_fsync", "replace"],
                            "replace_occurred": True, "evidence_promoted": False,
                            "rejected_as_durable": True},
    }
    return {"runs": rows, "reader_count": 11, "replacement_stages": 7,
            "all_reader_observations_complete": all(all(row["reader_complete"]) for row in rows),
            "all_retained_descriptors_complete": all(row["retained_descriptors_complete"] for row in rows),
            "all_fsync_orders_valid": all(row["all_stage_orders_valid"] for row in rows),
            "file_fsync_call_count": file_calls, "directory_fsync_call_count": directory_calls,
            "failure_controls": failure_controls,
            "crash_durability": None, "power_loss_durability": None,
            "evidence_class": "LOCAL_ELEVEN_READER_PARTIAL_WRITE_FIXTURE"}


def zip64_extra_field_gate():
    zip64_position, locator_position, classic_position = 8192, 8248, 8268
    comment = b"cycle037"

    def extra(fields=((0x0001, b"z" * 16), (0x5455, b"t" * 5))):
        return b"".join(struct.pack("<HH", identifier, len(payload)) + payload
                        for identifier, payload in fields)

    def parse_extra(raw):
        cursor, rows = 0, []
        while cursor < len(raw):
            if cursor + 4 > len(raw):
                raise ValueError("extra header")
            identifier, width = struct.unpack_from("<HH", raw, cursor)
            cursor += 4
            if cursor + width > len(raw):
                raise ValueError("extra length")
            rows.append((identifier, raw[cursor:cursor + width]))
            cursor += width
        identifiers = [item[0] for item in rows]
        if identifiers != [0x0001, 0x5455] or len(set(identifiers)) != len(identifiers):
            raise ValueError("extra order/identifier")
        if [len(item[1]) for item in rows] != [16, 5]:
            raise ValueError("extra payload")
        return rows

    def zip64(signature=0x06064B50, disk=0, entries=19, size=640, offset=3072):
        return struct.pack("<IQHHIIQQQQ", signature, 44, 45, 45, disk, disk,
                           entries, entries, size, offset)

    def locator(offset=zip64_position):
        return struct.pack("<IIQI", 0x07064B50, 0, offset, 1)

    def classic(bound_comment=comment, trailing=b"", disk=0, entries=0xFFFF,
                size=0xFFFFFFFF, offset=0xFFFFFFFF):
        return struct.pack("<IHHHHIIH", 0x06054B50, disk, disk, entries, entries,
                           size, offset, len(bound_comment)) + bound_comment + trailing

    def descriptor(crc=0xA1B2C3D4, compressed=1234, uncompressed=5678):
        return struct.pack("<IIQQ", 0x08074B50, crc, compressed, uncompressed)

    def verify(raw_extra, raw_zip64, raw_locator, raw_classic, raw_descriptor,
               positions=(zip64_position, locator_position, classic_position)):
        parse_extra(raw_extra)
        if struct.unpack("<IQHHIIQQQQ", raw_zip64) != (
                0x06064B50, 44, 45, 45, 0, 0, 19, 19, 640, 3072):
            raise ValueError("zip64")
        if struct.unpack("<IIQI", raw_locator) != (0x07064B50, 0, zip64_position, 1):
            raise ValueError("locator")
        if positions[0] + 56 != positions[1] or positions[1] + 20 != positions[2]:
            raise ValueError("adjacency")
        fields = struct.unpack_from("<IHHHHIIH", raw_classic)
        if fields[:-1] != (0x06054B50, 0, 0, 0xFFFF, 0xFFFF, 0xFFFFFFFF, 0xFFFFFFFF):
            raise ValueError("classic")
        if len(raw_classic) != 22 + fields[-1] or raw_classic[22:] != comment:
            raise ValueError("comment/trailing")
        if struct.unpack("<IIQQ", raw_descriptor) != (0x08074B50, 0xA1B2C3D4, 1234, 5678):
            raise ValueError("descriptor")
        return True

    valid = verify(extra(), zip64(), locator(), classic(), descriptor())
    bad_length = struct.pack("<HH", 0x0001, 17) + b"z" * 16
    cases = {
        "unknown_extra": (extra(((0x0001, b"z" * 16), (0x9999, b"x"))), zip64(), locator(), classic(), descriptor()),
        "duplicate_extra": (extra(((0x0001, b"z" * 16), (0x0001, b"t" * 5))), zip64(), locator(), classic(), descriptor()),
        "extra_order": (extra(((0x5455, b"t" * 5), (0x0001, b"z" * 16))), zip64(), locator(), classic(), descriptor()),
        "declared_length": (bad_length, zip64(), locator(), classic(), descriptor()),
        "signature": (extra(), zip64(signature=0), locator(), classic(), descriptor()),
        "multi_disk": (extra(), zip64(disk=1), locator(), classic(), descriptor()),
        "count": (extra(), zip64(entries=18), locator(), classic(), descriptor()),
        "crc": (extra(), zip64(), locator(), classic(), descriptor(crc=0)),
        "offset": (extra(), zip64(), locator(offset=zip64_position - 1), classic(), descriptor()),
        "size": (extra(), zip64(), locator(), classic(), descriptor(compressed=1235)),
        "comment": (extra(), zip64(), locator(), classic(b"other"), descriptor()),
        "trailing": (extra(), zip64(), locator(), classic(trailing=b"x"), descriptor()),
    }
    controls = {}
    for name, args in cases.items():
        try:
            verify(*args)
            controls[name] = False
        except (ValueError, struct.error):
            controls[name] = True
    return {"valid_metadata": valid, "extra_field_count": 2,
            "zip64_eocd_position": zip64_position, "locator_position": locator_position,
            "classic_eocd_position": classic_position, "negative_controls": controls,
            "payload_read": False, "real_producer_corpus": None,
            "evidence_class": "SYNTHETIC_ZIP64_METADATA"}


def seventeen_issuer_nonce_window():
    sample = hashlib.sha256(b"cycle037-synthetic-custody").hexdigest()
    specs = [(f"issuer-{index:02d}", f"scope-{index:02d}") for index in range(17)]
    keys = {name: f"synthetic-{name}" for name in ("rev-d", "rev-e", "rev-f", "rev-g", "rev-h")}
    policies, previous = [], "0" * 64
    for version, epoch, active in ((35, 8, ["rev-d", "rev-e", "rev-f"]),
                                   (36, 9, ["rev-e", "rev-f", "rev-g"]),
                                   (37, 10, ["rev-f", "rev-g", "rev-h"])):
        body = {"version": version, "revocation_epoch": epoch, "active": active,
                "threshold": 2, "nonce_min": 1000, "nonce_max": 1009,
                "previous_policy_sha256": previous}
        policy = {**body, "policy_sha256": canonical_hash(body)}
        policies.append(policy)
        previous = policy["policy_sha256"]
    by_version = {item["version"]: item for item in policies}
    registry = {issuer: {scope} for issuer, scope in specs}
    ancestry = {"issuer-16": "issuer-15", "issuer-15": "issuer-14"}

    def build(path="fixture-037"):
        events, prior = [], "0" * 64
        for sequence, (issuer, scope) in enumerate(specs):
            event = make_custody_event(sequence, sample, path, issuer, scope,
                                       "2026-01-01", "2027-02-01", prior)
            events.append(event)
            prior = event["event_sha256"]
        return events

    def receipt(signer, head, receipt_id, nonce, version=37, epoch=10,
                issued=100, expires=200):
        policy = by_version[version]
        body = {"receipt_id": receipt_id, "nonce": nonce, "signer": signer,
                "head_sha256": head, "policy_version": version,
                "revocation_epoch": epoch, "policy_sha256": policy["policy_sha256"],
                "issued_at": issued, "expires_at": expires}
        return {**body, "synthetic_signature": canonical_hash({**body, "key": keys[signer]})}

    def policy_chain(bound):
        if len(bound) != 3:
            raise ValueError("length")
        prior = "0" * 64
        for version, epoch, item in zip((35, 36, 37), (8, 9, 10), bound):
            unsigned = {key: value for key, value in item.items() if key != "policy_sha256"}
            if (item["version"] != version or item["revocation_epoch"] != epoch
                    or item["previous_policy_sha256"] != prior
                    or item["policy_sha256"] != canonical_hash(unsigned)):
                raise ValueError("policy")
            prior = item["policy_sha256"]
        return prior

    def verify(events, receipts, bound=policies, now=150,
               bound_registry=registry, bound_ancestry=ancestry, date="2026-12-15"):
        terminal, current = policy_chain(bound), bound[-1]
        head, signers, identifiers, nonces = events[-1]["event_sha256"], set(), set(), set()
        for item in receipts:
            signer = item["signer"]
            unsigned = {key: value for key, value in item.items() if key != "synthetic_signature"}
            if (item["policy_version"] != current["version"]
                    or item["revocation_epoch"] != current["revocation_epoch"]
                    or item["policy_sha256"] != terminal or signer not in current["active"]
                    or signer in signers or item["receipt_id"] in identifiers
                    or item["nonce"] in nonces
                    or not current["nonce_min"] <= item["nonce"] <= current["nonce_max"]
                    or item["head_sha256"] != head
                    or not item["issued_at"] <= now <= item["expires_at"]
                    or item["synthetic_signature"] != canonical_hash({**unsigned, "key": keys[signer]})):
                raise ValueError("receipt")
            signers.add(signer); identifiers.add(item["receipt_id"]); nonces.add(item["nonce"])
        if len(signers) < current["threshold"]:
            raise ValueError("quorum")
        if any(item["path_id"] != "fixture-037" for item in events):
            raise ValueError("path")
        if bound_ancestry != ancestry:
            raise ValueError("ancestry")
        return verify_custody_chain(events, bound_registry, date)

    events = build(); head = events[-1]["event_sha256"]
    valid_receipts = [receipt("rev-f", head, "r-f", 1000), receipt("rev-g", head, "r-g", 1009)]
    valid = verify(events, valid_receipts)
    fork = json.loads(json.dumps(policies)); fork[2]["previous_policy_sha256"] = "0" * 64
    other = build("other"); other_head = other[-1]["event_sha256"]
    cases = {
        "rollback": (events, valid_receipts, policies[:2], 150, registry, ancestry, "2026-12-15"),
        "fork": (events, valid_receipts, fork, 150, registry, ancestry, "2026-12-15"),
        "epoch": (events, [receipt("rev-f", head, "old-f", 1000, epoch=9), valid_receipts[1]], policies, 150, registry, ancestry, "2026-12-15"),
        "cross_policy_replay": (events, [receipt("rev-f", head, "v36-f", 1000, version=36, epoch=9), receipt("rev-g", head, "v36-g", 1009, version=36, epoch=9)], policies, 150, registry, ancestry, "2026-12-15"),
        "nonce_low": (events, [receipt("rev-f", head, "low", 999), valid_receipts[1]], policies, 150, registry, ancestry, "2026-12-15"),
        "nonce_high": (events, [valid_receipts[0], receipt("rev-g", head, "high", 1010)], policies, 150, registry, ancestry, "2026-12-15"),
        "nonce_replay": (events, [valid_receipts[0], receipt("rev-g", head, "same", 1000)], policies, 150, registry, ancestry, "2026-12-15"),
        "inactive_signer": (events, [receipt("rev-e", head, "inactive", 1001), valid_receipts[0]], policies, 150, registry, ancestry, "2026-12-15"),
        "quorum": (events, valid_receipts[:1], policies, 150, registry, ancestry, "2026-12-15"),
        "stale": (events, [receipt("rev-f", head, "stale", 1001, expires=149), valid_receipts[1]], policies, 150, registry, ancestry, "2026-12-15"),
        "head": (events, [receipt("rev-f", "0" * 64, "bad-f", 1001), receipt("rev-g", "0" * 64, "bad-g", 1002)], policies, 150, registry, ancestry, "2026-12-15"),
        "scope": (events, valid_receipts, policies, 150, {**registry, "issuer-16": {"wrong"}}, ancestry, "2026-12-15"),
        "ancestry": (events, valid_receipts, policies, 150, registry, {"issuer-16": "issuer-14"}, "2026-12-15"),
        "path": (other, [receipt("rev-f", other_head, "other-f", 1001), receipt("rev-g", other_head, "other-g", 1002)], policies, 150, registry, ancestry, "2026-12-15"),
    }
    controls = {}
    for name, args in cases.items():
        try:
            verify(*args); controls[name] = False
        except (ValueError, KeyError):
            controls[name] = True
    return {"event_count": 17, "policy_versions": [35, 36, 37],
            "revocation_epochs": [8, 9, 10], "nonce_window": [1000, 1009],
            "receipt_threshold": 2, "policy_chain_terminal_sha256": policies[-1]["policy_sha256"],
            "terminal_sha256": valid["final_event_sha256"], "boundary_rejections": controls,
            "signature_kind": "SYNTHETIC_HASH_FIXTURE_NOT_CRYPTOGRAPHIC_SIGNATURE",
            "physical_sample": None, "evidence_class": "SYNTHETIC_CUSTODY"}


def twenty_one_component_three_permutations(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("source")
    n = 21
    order = [f"component-{index:02d}" for index in range(n)]
    labels = ["compute"] * 6 + ["memory"] * 5 + ["network"] * 5 + ["control"] * 5
    intervals = [[index + 3, index + 11] for index in range(n)]
    mask = [[i == j or (labels[i] == labels[j] and abs(i - j) == 1)
             for j in range(n)] for i in range(n)]
    positive = [[0.06 if i == j else (0.0001 if mask[i][j] else 0.0)
                 for j in range(n)] for i in range(n)]
    matrices = {"positive": positive,
                "zero": [[0.06 if i == j else 0.0 for j in range(n)] for i in range(n)],
                "negative": [[0.06 if i == j else (-0.0001 if mask[i][j] else 0.0)
                              for j in range(n)] for i in range(n)],
                "missing": None,
                "indefinite": [[1.0 if i == j else 2.0 for j in range(n)] for i in range(n)],
                "nonfinite": [[float("inf") if i == j == 0 else (1.0 if i == j else 0.0)
                               for j in range(n)] for i in range(n)]}
    first = [*range(7, n), *range(7)]
    second = [*range(14, n), *range(14)]
    third = list(reversed(range(n)))

    def compose(left, right):
        return [left[index] for index in right]

    def permute_vector(items, indices):
        return [items[index] for index in indices]

    def permute_matrix(matrix, indices):
        return None if matrix is None else [[matrix[i][j] for j in indices] for i in indices]

    left_composed = compose(compose(first, second), third)
    right_composed = compose(first, compose(second, third))
    inverse = [left_composed.index(index) for index in range(n)]
    sequential_intervals = permute_vector(permute_vector(permute_vector(intervals, first), second), third)
    composed_intervals = permute_vector(intervals, left_composed)
    sequential_matrices = {name: permute_matrix(permute_matrix(permute_matrix(value, first), second), third)
                           for name, value in matrices.items()}
    composed_matrices = {name: permute_matrix(value, left_composed) for name, value in matrices.items()}
    recovered_intervals = permute_vector(composed_intervals, inverse)
    recovered_matrices = {name: permute_matrix(value, inverse) for name, value in composed_matrices.items()}
    sigmas = [0.0, 1.0, 2.0, 3.0, 5.0, 8.0, 13.0, 21.0]
    sweeps = {str(sigma): component_covariance_sweep(intervals, matrices, [1, 11, 21, 0], sigma=sigma)
              for sigma in sigmas}
    permuted_sweeps = {str(sigma): component_covariance_sweep(composed_intervals, composed_matrices,
                                                              [1, 11, 21, 0], sigma=sigma)
                       for sigma in sigmas}
    source_sha = hashlib.sha256(source_bytes).hexdigest()
    binding = {"source_sha256": source_sha, "order": order, "labels": labels, "mask": mask,
               "first": first, "second": second, "third": third,
               "composed": left_composed, "inverse": inverse, "sigmas": sigmas}
    identity = canonical_hash(binding)
    mutations = {"order": {**binding, "order": list(reversed(order))},
                 "labels": {**binding, "labels": list(reversed(labels))},
                 "composition": {**binding, "composed": list(reversed(left_composed))},
                 "inverse": {**binding, "inverse": list(reversed(inverse))}}
    return {"components": n, "source_sha256": source_sha, "component_order": order,
            "block_labels": labels, "first_permutation": first, "second_permutation": second,
            "third_permutation": third, "composed_permutation": left_composed,
            "inverse_permutation": inverse, "composition_associative": left_composed == right_composed,
            "composition_matches_sequential_intervals": sequential_intervals == composed_intervals,
            "composition_matches_sequential_matrices": sequential_matrices == composed_matrices,
            "inverse_map_valid": all(inverse[left_composed[index]] == index for index in range(n)),
            "triple_permutation_recovers_intervals": recovered_intervals == intervals,
            "triple_permutation_recovers_matrices": recovered_matrices == matrices,
            "permutation_equivalence": sweeps == permuted_sweeps,
            "sparse_nonzero_count": sum(sum(row) for row in mask),
            "covariance_grid_sha256": identity,
            "binding_mutation_rejections": {name: canonical_hash(value) != identity
                                             for name, value in mutations.items()},
            "sigma_values": sigmas, "sweeps": sweeps,
            "commercial_interpretation": None, "evidence_class": "MODEL_ONLY"}


def eight_signed_transform_characteristic_invariants():
    matrix = [[Fraction(25), Fraction(1), Fraction(2), Fraction(1)],
              [Fraction(1), Fraction(36), Fraction(1), Fraction(2)],
              [Fraction(2), Fraction(1), Fraction(49), Fraction(1)],
              [Fraction(1), Fraction(2), Fraction(1), Fraction(81)]]
    identity = ([0, 1, 2, 3], [1, 1, 1, 1])
    transforms = [
        ([1, 0, 3, 2], [1, -1, 1, -1]), ([2, 3, 0, 1], [-1, 1, -1, 1]),
        ([3, 2, 1, 0], [1, 1, -1, -1]), ([0, 2, 1, 3], [-1, 1, 1, -1]),
        ([2, 0, 3, 1], [1, -1, -1, 1]), ([3, 1, 0, 2], [-1, -1, 1, 1]),
        ([1, 3, 0, 2], [1, 1, -1, -1]), ([2, 1, 3, 0], [-1, 1, 1, -1]),
    ]

    def combine(first, second):
        return ([first[0][second[0][index]] for index in range(4)],
                [second[1][index] * first[1][second[0][index]] for index in range(4)])

    def inverse(item):
        indices = [item[0].index(index) for index in range(4)]
        return indices, [item[1][indices[index]] for index in range(4)]

    def apply(value, item):
        return [[item[1][i] * item[1][j] * value[item[0][i]][item[0][j]]
                 for j in range(4)] for i in range(4)]

    def multiply(left, right):
        return [[sum(left[i][k] * right[k][j] for k in range(len(right)))
                 for j in range(len(right[0]))] for i in range(len(left))]

    def determinant(value):
        total, size = Fraction(0), len(value)
        for order in itertools.permutations(range(size)):
            inversions = sum(order[i] > order[j]
                             for i in range(size) for j in range(i + 1, size))
            term = Fraction(-1 if inversions % 2 else 1)
            for row, column in enumerate(order):
                term *= value[row][column]
            total += term
        return total

    def characteristic(value):
        powers, current = [], value
        for _ in range(4):
            powers.append(sum(current[index][index] for index in range(4)))
            current = multiply(current, value)
        e1 = powers[0]
        e2 = (powers[0] ** 2 - powers[1]) / 2
        e3 = (powers[0] ** 3 - 3 * powers[0] * powers[1] + 2 * powers[2]) / 6
        e4 = determinant(value)
        return [Fraction(1), -e1, e2, -e3, e4]

    def principal_minors(value):
        return [determinant([row[:size] for row in value[:size]])
                for size in range(1, len(value) + 1)]

    composed, sequential = identity, matrix
    for item in transforms:
        composed, sequential = combine(composed, item), apply(sequential, item)
    restored = sequential
    for item in reversed(transforms):
        restored = apply(restored, inverse(item))
    rows = []
    for left, right in [(index, (index + 1) % len(transforms)) for index in range(len(transforms))]:
        product = combine(transforms[left], transforms[right])
        rows.append({"left": left, "right": right,
                     "closure": sorted(product[0]) == list(range(4))
                     and all(value in (-1, 1) for value in product[1]),
                     "inverse_roundtrip": combine(inverse(product), product) == identity})
    original_characteristic, transformed_characteristic = characteristic(matrix), characteristic(sequential)
    minors = [*principal_minors(matrix), *principal_minors(sequential)]
    return {"transform_count": 8, "matrix_product_count": 128,
            "cayley_rows": rows,
            "all_cayley_rows_valid": all(row["closure"] and row["inverse_roundtrip"] for row in rows),
            "closure_is_signed_permutation": sorted(composed[0]) == list(range(4)),
            "associative_composition": sequential == apply(matrix, composed),
            "exact_reverse_order_roundtrip": restored == matrix,
            "characteristic_coefficients": [[item.numerator, item.denominator]
                                             for item in original_characteristic],
            "characteristic_polynomial_invariant": original_characteristic == transformed_characteristic,
            "trace_invariant": original_characteristic[1] == transformed_characteristic[1],
            "determinant_invariant": original_characteristic[-1] == transformed_characteristic[-1],
            "all_principal_minors_positive": all(item > 0 for item in minors),
            "symmetric": all(sequential[i][j] == sequential[j][i] for i in range(4) for j in range(4)),
            "composition_sha256": canonical_hash({"permutations": [item[0] for item in transforms],
                                                    "signs": [item[1] for item in transforms]}),
            "calibration": None, "evidence_class": "SYNTHETIC_TYPED_COVARIANCE"}


def twenty_one_scenario_deletion_intervals():
    scenarios = [
        [4, 3, 2, 1], [2, 2, 1, 0], [2, 1, 2, 0], [1, 1, 1, 1],
        [0, 3, 2, 3], [0, 1, 2, 3], [3, 0, 3, 1], [1, 4, 0, 4],
        [2, 4, 4, 1], [4, 0, 1, 4], [3, 2, 4, 0], [0, 4, 3, 2],
        [4, 2, 0, 3], [1, 3, 4, 2], [2, 0, 4, 3], [3, 4, 1, 2],
        [4, 1, 3, 2], [2, 3, 1, 4], [1, 2, 4, 3], [3, 1, 4, 2],
        [4, 3, 1, 2],
    ]

    def contribution(scores):
        eligible = {index for index, score in enumerate(scores) if score == max(scores)}
        output = [0, 0, 0, 0]
        for order in itertools.permutations(range(4)):
            output[next(item for item in order if item in eligible)] += 1
        return tuple(output)

    contributions = [contribution(item) for item in scenarios]
    full = tuple(sum(row[index] for row in contributions) for index in range(4))
    states = [{(0, 0, 0, 0): 1}] + [{} for _ in range(13)]
    for contribution_row in contributions:
        for count in range(min(13, len(scenarios)), 0, -1):
            for subtotal, multiplicity in list(states[count - 1].items()):
                bound = tuple(subtotal[index] + contribution_row[index] for index in range(4))
                states[count][bound] = states[count].get(bound, 0) + multiplicity
    fractions = [Fraction(value, 21 * 24) for value in full]
    grid_counts, state_counts = {}, {}
    for removed_count in range(1, 14):
        denominator = (21 - removed_count) * 24
        grid_counts[str(removed_count)] = sum(states[removed_count].values())
        state_counts[str(removed_count)] = len(states[removed_count])
        for removed in states[removed_count]:
            fractions.extend(Fraction(full[index] - removed[index], denominator) for index in range(4))
    low, high = min(fractions), max(fractions)
    return {"scenario_count": 21, "orders_each": 24, "full_grid_size": 504,
            "winner_counts": list(full), "deletion_grid_counts": grid_counts,
            "dynamic_program_state_counts": state_counts,
            "counts_match_binomial": all(grid_counts[str(count)] == math.comb(21, count)
                                         for count in range(1, 14)),
            "all_grid_interval": [[low.numerator, low.denominator],
                                  [high.numerator, high.denominator]],
            "probability_claim": None, "capital": None,
            "evidence_class": "FINITE_ILLUSTRATIVE_SCENARIO"}


def fourteen_unit_affine_split_conditions(*raw_sources):
    if len(raw_sources) != 14 or any(not isinstance(item, bytes) or not item for item in raw_sources):
        raise ValueError("sources")
    source_sha = [hashlib.sha256(item).hexdigest() for item in raw_sources]
    maps = []
    for index, digest in enumerate(bytes.fromhex(item) for item in source_sha):
        maps.append({"slope": Fraction(2 + digest[0] % 7, 1 + digest[1] % 5),
                     "bias": Fraction(digest[2] % 11, 1 + digest[3] % 7),
                     "input_unit": f"u{index:02d}", "output_unit": f"u{index + 1:02d}"})

    def compose(bound):
        if not bound:
            raise ValueError("empty")
        slope, bias, input_unit, output_unit = (Fraction(1), Fraction(0),
                                                bound[0]["input_unit"], bound[0]["input_unit"])
        for item in bound:
            if item["input_unit"] != output_unit or item["slope"] <= 0:
                raise ValueError("unit/monotonicity")
            slope, bias = item["slope"] * slope, item["slope"] * bias + item["bias"]
            output_unit = item["output_unit"]
        return {"slope": slope, "bias": bias, "input_unit": input_unit,
                "output_unit": output_unit}

    def combine(first, second):
        if first["output_unit"] != second["input_unit"]:
            raise ValueError("split unit")
        return {"slope": second["slope"] * first["slope"],
                "bias": second["slope"] * first["bias"] + second["bias"],
                "input_unit": first["input_unit"], "output_unit": second["output_unit"]}

    total = compose(maps)
    splits = [1, 4, 7, 10, 13]
    split_rows = []
    for split in splits:
        reconstructed = combine(compose(maps[:split]), compose(maps[split:]))
        split_rows.append({"split": split, "matches": reconstructed == total,
                           "condition_product": [1, 1]})
    interval = (Fraction(2, 3), Fraction(5, 3))
    transformed = tuple(total["slope"] * value + total["bias"] for value in interval)
    recovered = tuple((value - total["bias"]) / total["slope"] for value in transformed)
    unit_mutation = [dict(item) for item in maps]; unit_mutation[8]["input_unit"] = "wrong"
    nonmonotone = [dict(item) for item in maps]; nonmonotone[5]["slope"] = Fraction(-1)
    controls = {"source_order": source_sha != list(reversed(source_sha)),
                "dimension": len(maps[:-1]) != 14, "unit": False, "nonmonotone": False}
    for name, value in (("unit", unit_mutation), ("nonmonotone", nonmonotone)):
        try:
            compose(value)
        except ValueError:
            controls[name] = True
    return {"source_sha256": source_sha, "map_count": 14,
            "unit_chain": [maps[0]["input_unit"], *[item["output_unit"] for item in maps]],
            "terminal_unit": total["output_unit"], "split_composition_rows": split_rows,
            "all_split_compositions_match": all(row["matches"] for row in split_rows),
            "composed_interval": [[value.numerator, value.denominator] for value in transformed],
            "lipschitz_bound": [total["slope"].numerator, total["slope"].denominator],
            "inverse_lipschitz_bound": [total["slope"].denominator, total["slope"].numerator],
            "lipschitz_product": [1, 1],
            "roundtrip_interval": [[value.numerator, value.denominator] for value in recovered],
            "exact_roundtrip": recovered == interval, "negative_controls": controls,
            "sort": ["RealModel", "Model"], "new_law_claim": None,
            "evidence_class": "SOURCE_TYPED_RATIONAL_MODEL"}


def ten_observer_two_transitions():
    observers = [f"observer-{index:02d}" for index in range(10)]

    def transition(epoch, key_epoch, previous):
        body = {"epoch": epoch, "members": observers, "previous_sha256": previous,
                "key_epoch": key_epoch}
        return {**body, "transition_sha256": canonical_hash(body)}

    first = transition(17, 2, "0" * 64)
    second = transition(18, 3, first["transition_sha256"])
    third = transition(19, 4, second["transition_sha256"])
    head = canonical_hash({"domain": "fiction-scm-037", "height": 37})

    def certificate(signers, nonce, epoch=19, bound_head=head, audience="uqpu-scm",
                    transition_sha=third["transition_sha256"], policy=37):
        return {"signers": signers, "nonce": nonce, "membership_epoch": epoch,
                "head_sha256": bound_head, "audience": audience,
                "transition_sha256": transition_sha, "policy_version": policy}

    left, right = certificate(observers[:8], "left"), certificate(observers[2:], "right")

    def validate(one, two, chain=(first, second, third)):
        prior = "0" * 64
        for expected_epoch, expected_key, item in zip((17, 18, 19), (2, 3, 4), chain):
            unsigned = {key: value for key, value in item.items() if key != "transition_sha256"}
            if (item["epoch"] != expected_epoch or item["key_epoch"] != expected_key
                    or item["previous_sha256"] != prior
                    or item["transition_sha256"] != canonical_hash(unsigned)):
                return False
            prior = item["transition_sha256"]
        current = chain[-1]
        for item in (one, two):
            signers = item["signers"]
            if (len(signers) != 8 or len(set(signers)) != 8
                    or not set(signers) <= set(current["members"])
                    or item["membership_epoch"] != current["epoch"]
                    or item["head_sha256"] != head or item["audience"] != "uqpu-scm"
                    or item["transition_sha256"] != current["transition_sha256"]
                    or item["policy_version"] != 37):
                return False
        return one["nonce"] != two["nonce"] and len(set(one["signers"]) & set(two["signers"])) >= 6

    bad_chain = [dict(item) for item in (first, second, third)]; bad_chain[2]["previous_sha256"] = "0" * 64
    cases = {
        "valid": (left, right, (first, second, third), True),
        "split": (left, certificate(observers[3:], "short"), (first, second, third), False),
        "stale": (left, certificate(observers[2:], "right", epoch=18), (first, second, third), False),
        "fork": (left, certificate(observers[2:], "right", bound_head="0" * 64), (first, second, third), False),
        "replay": (left, certificate(observers[2:], "left"), (first, second, third), False),
        "downgrade": (left, certificate(observers[2:], "right", policy=36), (first, second, third), False),
        "audience": (left, certificate(observers[2:], "right", audience="wrong"), (first, second, third), False),
        "membership_hash": (left, certificate(observers[2:], "right", transition_sha="0" * 64), (first, second, third), False),
        "transition_chain": (left, right, tuple(bad_chain), False),
        "revocation": (left, certificate([*observers[2:9], "observer-10"], "right"), (first, second, third), False),
        "missing_member": (left, certificate(observers[2:9], "right"), (first, second, third), False),
    }
    table = [{"case": name, "accepted": validate(one, two, chain), "expected": expected}
             for name, (one, two, chain, expected) in cases.items()]
    return {"observer_count": 10, "quorum": 8,
            "certificate_intersection_size": len(set(left["signers"]) & set(right["signers"])),
            "minimum_quorum_intersection": 6, "membership_epoch": 19,
            "transition_count": 2, "transition_chain_sha256": third["transition_sha256"],
            "control_table": table,
            "all_controls_match": all(row["accepted"] == row["expected"] for row in table),
            "sort": "Fiction", "empirical_coupling": None, "evidence_class": "FICTION_ONLY"}


def lineage_manifest_v27(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("source")
    source_sha = hashlib.sha256(source_bytes).hexdigest()
    real = [{"kind": "real", "index": index, "source_sha256": source_sha,
             "schema": "uqpu-lineage-v27", "config": f"cfg-{index % 5}",
             "metric": f"metric-{index % 4}"} for index in range(14)]
    padding = [{"kind": "padding", "index": index, "domain": "uqpu-lineage-padding-v27"}
               for index in range(14, 16)]

    def leaf_hash(item):
        return canonical_hash({"domain": "uqpu-lineage-leaf-v27", **item})

    def combine(left, right):
        return canonical_hash({"domain": "uqpu-lineage-node-v27", "left": left, "right": right})

    leaves = [leaf_hash(item) for item in [*real, *padding]]
    levels = [leaves]
    while len(levels[-1]) > 1:
        row = levels[-1]
        levels.append([combine(row[index], row[index + 1]) for index in range(0, len(row), 2)])
    root = levels[-1][0]

    def proof(index):
        original, steps = index, []
        for level, row in enumerate(levels[:-1]):
            sibling = index ^ 1
            steps.append({"level": level, "side": "left" if sibling < index else "right",
                          "hash": row[sibling]})
            index //= 2
        return {"leaf_index": original, "steps": steps}

    def verify(item, item_proof):
        index, value = item_proof["leaf_index"], leaf_hash(item)
        if index != item["index"]:
            return False
        for level, step in enumerate(item_proof["steps"]):
            side = "left" if (index ^ 1) < index else "right"
            if step["level"] != level or step["side"] != side:
                return False
            value = combine(step["hash"], value) if side == "left" else combine(value, step["hash"])
            index //= 2
        return value == root

    selected, exclusions = [0, 3, 6, 9, 13], [14, 15]
    inclusion = [proof(index) for index in selected]
    exclusion = [proof(index) for index in exclusions]
    manifest = {"version": 27, "root_sha256": root, "source_sha256": source_sha,
                "real_indices": list(range(14)), "padding_exclusion_indices": exclusions,
                "selected_indices": selected,
                "config_sha256": canonical_hash([item["config"] for item in real]),
                "metric_sha256": canonical_hash([item["metric"] for item in real]),
                "inclusion_proof_sha256": canonical_hash(inclusion),
                "exclusion_proof_sha256": canonical_hash(exclusion)}

    def validate(bound, bound_inclusion=inclusion, bound_exclusion=exclusion):
        expected = {**manifest, "inclusion_proof_sha256": canonical_hash(bound_inclusion),
                    "exclusion_proof_sha256": canonical_hash(bound_exclusion)}
        return (bound == expected
                and all(verify(real[index], item) for index, item in zip(selected, bound_inclusion))
                and all(verify(padding[index - 14], item)
                        for index, item in zip(exclusions, bound_exclusion)))

    mutations = {
        "root": {**manifest, "root_sha256": "0" * 64},
        "padding_exclusion": {**manifest, "padding_exclusion_indices": [13, 15]},
        "order": {**manifest, "selected_indices": list(reversed(selected))},
        "index": {**manifest, "real_indices": list(range(13)) + [15]},
        "source": {**manifest, "source_sha256": "0" * 64},
        "schema": {**manifest, "version": 26},
        "config": {**manifest, "config_sha256": "0" * 64},
        "metric": {**manifest, "metric_sha256": "0" * 64},
    }
    rejection = {name: not validate(value) for name, value in mutations.items()}
    proof_mutations = {}
    for name in ("proof_minimality", "proof_order", "proof_path"):
        bound = json.loads(json.dumps(inclusion))
        if name == "proof_minimality":
            bound[0]["steps"].append(bound[0]["steps"][-1])
        elif name == "proof_order":
            bound[0]["steps"] = list(reversed(bound[0]["steps"]))
        else:
            bound[0]["steps"][0]["side"] = "left" if bound[0]["steps"][0]["side"] == "right" else "right"
        proof_mutations[name] = bound
    for name, bound in proof_mutations.items():
        rejection[name] = not validate({**manifest, "inclusion_proof_sha256": canonical_hash(bound)}, bound)
    bad_exclusion = json.loads(json.dumps(exclusion)); bad_exclusion[0]["steps"][0]["hash"] = "0" * 64
    rejection["exclusion_proof"] = not validate(
        {**manifest, "exclusion_proof_sha256": canonical_hash(bad_exclusion)}, inclusion, bad_exclusion)
    rejection["padding_domain"] = leaf_hash({**padding[0], "domain": "wrong"}) != leaves[14]
    proof_nodes = {(step["level"], step["side"], step["hash"])
                   for item in [*inclusion, *exclusion] for step in item["steps"]}
    return {"manifest": manifest, "real_leaf_count": 14, "padded_leaf_count": 16,
            "padding_leaf_count": 2, "padding_exclusion_count": 2,
            "selected_leaf_count": 5, "batch_proof_count": 7,
            "compressed_proof_node_count": len(proof_nodes),
            "valid_manifest": validate(manifest), "mutation_rejections": rejection,
            "candidate_result": None, "functional_equivalence": None,
            "evidence_class": "SYNTHETIC_DATA_LINEAGE"}


def fifteen_inverse_pairs_antichain_dag():
    mask = 63

    def rotl(value, width):
        return ((value << width) | (value >> (6 - width))) & mask

    def rotr(value, width):
        return ((value >> width) | (value << (6 - width))) & mask

    operations = [
        ("add-01", lambda x: (x + 1) & mask, lambda x: (x - 1) & mask, 7, 2, 6),
        ("xor-03", lambda x: x ^ 3, lambda x: x ^ 3, 8, 3, 6),
        ("rotl-01", lambda x: rotl(x, 1), lambda x: rotr(x, 1), 9, 3, 6),
        ("add-05", lambda x: (x + 5) & mask, lambda x: (x - 5) & mask, 11, 4, 6),
        ("xor-12", lambda x: x ^ 12, lambda x: x ^ 12, 12, 4, 6),
        ("rotl-02", lambda x: rotl(x, 2), lambda x: rotr(x, 2), 13, 5, 6),
        ("add-07", lambda x: (x + 7) & mask, lambda x: (x - 7) & mask, 15, 5, 6),
        ("xor-21", lambda x: x ^ 21, lambda x: x ^ 21, 17, 6, 6),
        ("rotl-03", lambda x: rotl(x, 3), lambda x: rotr(x, 3), 19, 6, 6),
        ("add-09", lambda x: (x + 9) & mask, lambda x: (x - 9) & mask, 21, 7, 6),
        ("xor-42", lambda x: x ^ 42, lambda x: x ^ 42, 23, 7, 6),
        ("rotl-04", lambda x: rotl(x, 4), lambda x: rotr(x, 4), 25, 8, 6),
        ("add-11", lambda x: (x + 11) & mask, lambda x: (x - 11) & mask, 27, 8, 6),
        ("xor-33", lambda x: x ^ 33, lambda x: x ^ 33, 29, 9, 6),
        ("rotl-05", lambda x: rotl(x, 5), lambda x: rotr(x, 5), 31, 9, 6),
    ]
    dependencies = [[], [], [0], [0], [1], [1], [2, 4], [3, 5],
                    [6], [6], [7], [7], [8, 10], [9, 11], [12, 13]]

    def apply(value, sequence, inverse=False):
        for _, forward, backward, _, _, _ in (reversed(sequence) if inverse else sequence):
            value = backward(value) if inverse else forward(value)
        return value

    def validate_dag(bound):
        return len(bound) == len(operations) and all(
            all(isinstance(parent, int) and 0 <= parent < index for parent in parents)
            for index, parents in enumerate(bound))

    def reachability(bound):
        ancestors = [set() for _ in bound]
        for index, parents in enumerate(bound):
            ancestors[index].update(parents)
            for parent in parents:
                ancestors[index].update(ancestors[parent])
        return ancestors

    def maximum_antichain(bound):
        ancestors = reachability(bound)
        best = []
        for bits in range(1 << len(bound)):
            if bits.bit_count() <= len(best):
                continue
            items = [index for index in range(len(bound)) if bits >> index & 1]
            if all(first not in ancestors[second] and second not in ancestors[first]
                   for position, first in enumerate(items) for second in items[position + 1:]):
                best = items
        return best

    def critical_depth(bound):
        values = []
        for index, parents in enumerate(bound):
            values.append(operations[index][4] + max((values[parent] for parent in parents), default=0))
        return max(values)

    def leaf(operation, index, bound=dependencies):
        name, _, _, gates, depth, qubits = operation
        body = {"domain": "uqpu-resource-leaf-v6", "index": index, "name": name,
                "gates": gates, "depth": depth, "max_qubits": qubits,
                "depends_on": bound[index]}
        return {"hash": canonical_hash(body), "gates": gates,
                "serial_depth": depth, "max_qubits": qubits}

    leaves = [leaf(item, index) for index, item in enumerate(operations)]
    leaves.append({"hash": canonical_hash({"domain": "uqpu-resource-padding-v6", "index": 15}),
                   "gates": 0, "serial_depth": 0, "max_qubits": 0})

    def combine(left, right):
        body = {"domain": "uqpu-resource-node-v6", "left": left["hash"], "right": right["hash"],
                "gates": left["gates"] + right["gates"],
                "serial_depth": left["serial_depth"] + right["serial_depth"],
                "max_qubits": max(left["max_qubits"], right["max_qubits"])}
        return {"hash": canonical_hash(body), "gates": body["gates"],
                "serial_depth": body["serial_depth"], "max_qubits": body["max_qubits"]}

    levels = [leaves]
    while len(levels[-1]) > 1:
        row = levels[-1]
        levels.append([combine(row[index], row[index + 1]) for index in range(0, len(row), 2)])
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
            side = "left" if (cursor ^ 1) < cursor else "right"
            if (step["level"], step["index"], step["side"]) != (level, cursor, side):
                return False
            sibling = {key: step[key] for key in ("hash", "gates", "serial_depth", "max_qubits")}
            value = combine(sibling, value) if side == "left" else combine(value, sibling)
            cursor //= 2
        return value == root

    proofs = [proof(index) for index in range(len(operations))]
    encoded = [apply(value, operations) for value in range(64)]
    reconstructed = [apply(value, operations, True) for value in encoded]
    order_mutation = [operations[1], operations[0], *operations[2:]]
    dag_mutation = json.loads(json.dumps(dependencies)); dag_mutation[6] = [7]
    proof_mutation = json.loads(json.dumps(proofs[0])); proof_mutation["steps"][0]["gates"] += 1
    resource_mutation = (*operations[-1][:3], operations[-1][3] + 1,
                         operations[-1][4], operations[-1][5])
    antichain = maximum_antichain(dependencies)
    antichain_mutation = [*antichain, 14]
    ancestors = reachability(dependencies)

    def valid_antichain(items):
        return len(items) == len(set(items)) and all(
            first not in ancestors[second] and second not in ancestors[first]
            for position, first in enumerate(items) for second in items[position + 1:])

    return {"inverse_pair_names": [item[0] for item in operations],
            "resource_merkle_root_sha256": root["hash"], "proof_count": len(proofs),
            "dependency_dag": [{"node": index, "depends_on": parents}
                               for index, parents in enumerate(dependencies)],
            "dependency_dag_valid": validate_dag(dependencies),
            "dependency_dag_mutation_rejected": not validate_dag(dag_mutation),
            "all_inclusion_proofs_valid": all(verify(index, item, proofs[index])
                                             for index, item in enumerate(operations)),
            "proof_resource_mutation_rejected": not verify(0, operations[0], proof_mutation),
            "leaf_resource_mutation_rejected": not verify(14, resource_mutation, proofs[14]),
            "basis_states_checked": 64, "distinct_outputs": len(set(encoded)),
            "residual": sum(first != second for first, second in enumerate(reconstructed)),
            "order_mutation_witness_count": sum(item != apply(value, order_mutation)
                                                for value, item in enumerate(encoded)),
            "maximum_antichain": antichain, "antichain_width": len(antichain),
            "antichain_valid": valid_antichain(antichain),
            "antichain_mutation_rejected": not valid_antichain(antichain_mutation),
            "resource_bound": {"gates": root["gates"],
                               "serial_depth": sum(item[4] for item in operations),
                               "dag_critical_depth": critical_depth(dependencies),
                               "antichain_width": len(antichain),
                               "unconstrained_parallel_lower_bound": max(item[4] for item in operations),
                               "max_qubits": root["max_qubits"]},
            "parallel_bounds_are_model_only": True, "hardware": None,
            "evidence_class": "SYNTHETIC_INVERSE_OPERATOR"}


def run_cycle037_fixture(source_bytes, directory):
    with tempfile.TemporaryDirectory(dir=directory) as work:
        lanes = {
            "A": seventeenth_graph_orbit_histogram(),
            "B": schema_version_transition_gate(),
            "C": eleven_reader_partial_write_gate(work),
            "D": zip64_extra_field_gate(),
            "E": seventeen_issuer_nonce_window(),
            "F": twenty_one_component_three_permutations(source_bytes),
            "G": eight_signed_transform_characteristic_invariants(),
            "H": twenty_one_scenario_deletion_intervals(),
            "FND/EQN": fourteen_unit_affine_split_conditions(
                source_bytes, source_bytes + b":two", source_bytes + b":three",
                source_bytes + b":four", source_bytes + b":five", source_bytes + b":six",
                source_bytes + b":seven", source_bytes + b":eight", source_bytes + b":nine",
                source_bytes + b":ten", source_bytes + b":eleven", source_bytes + b":twelve",
                source_bytes + b":thirteen", source_bytes + b":fourteen"),
            "SCM": ten_observer_two_transitions(),
            "AI-COST": lineage_manifest_v27(source_bytes),
            "QOS/QSVT": fifteen_inverse_pairs_antichain_dag(),
        }
    return {lane: {"status": "BLOCKED_WITH_PROGRESS", **value}
            for lane, value in lanes.items()}
