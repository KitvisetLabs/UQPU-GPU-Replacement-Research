"""Cycle 036 bounded fixtures; outputs remain local, synthetic, model, or fiction evidence."""
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


def sixteenth_graph_orbit_representatives():
    n, full_mask = 12, (1 << 12) - 1
    weights = [2, 3] * 6

    def solve(bound):
        scores = [sum(bound[i] for i in range(n)
                      if ((mask >> i) & 1) != ((mask >> ((i + 1) % n)) & 1))
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
    membership = sorted([item, min(orbit)] for orbit in quotient for item in orbit)
    independent_partition = sorted(sorted({transform_mask(mask, *action)
                                           for action in actions} & witness_set)
                                   for mask in result["witnesses"])
    independent_partition = [key for key, _ in itertools.groupby(independent_partition)]
    numerator = sum(fixed)
    return {
        "states": result["states"], "objective": result["objective"],
        "witness_count": len(result["witnesses"]), "stabilizer_size": len(stabilizer),
        "action_count": len(actions), "all_dihedral_transforms_match": all(equivariance),
        "canonical_orbit_representatives": representatives,
        "orbit_membership_sha256": canonical_hash(membership),
        "second_partition_sha256": canonical_hash(independent_partition),
        "partition_digest_matches": independent_partition == quotient,
        "burnside_numerator": numerator, "burnside_orbit_count": numerator // len(actions),
        "burnside_matches_direct": numerator % len(actions) == 0
        and numerator // len(actions) == len(quotient),
        "task_sha256": result["task_sha256"], "witness_sha256": result["witness_sha256"],
        "deterministic": result == solve(weights), "scaling_claim": None,
        "evidence_class": "LOCAL_EXACT_CLASSICAL_FIXTURE",
    }


def schema_path_numeric_gate():
    max_integer, max_depth, max_tokens = 9007199254740991, 9, 60

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
                return {"path": path, "tag": "bool", "value": item}
            if isinstance(item, int):
                if abs(item) > max_integer:
                    raise ValueError("integer")
                return {"path": path, "tag": "integer", "value": str(item)}
            if isinstance(item, Decimal):
                if not item.is_finite():
                    raise ValueError("nonfinite")
                normalized = item.normalize()
                exponent = normalized.as_tuple().exponent
                if exponent < -30 or exponent > 30:
                    raise ValueError("exponent")
                return {"path": path, "tag": "decimal", "value": str(normalized)}
            if isinstance(item, str):
                if reject_text(item):
                    raise ValueError("unicode")
                return {"path": path, "tag": "string", "value": unicodedata.normalize("NFC", item)}
            if isinstance(item, list):
                return {"path": path, "tag": "array",
                        "value": [walk(child, f"{path}/{index}", depth + 1)
                                  for index, child in enumerate(item)]}
            if isinstance(item, dict):
                normalized, rows = {}, []
                for key, child in item.items():
                    if not isinstance(key, str) or reject_text(key):
                        raise ValueError("key")
                    bound = unicodedata.normalize("NFC", key)
                    if bound in normalized or bound == "$type":
                        raise ValueError("key collision")
                    normalized[bound] = child
                for key in sorted(normalized):
                    rows.append([key, walk(normalized[key], f"{path}/{key}", depth + 1)])
                return {"path": path, "tag": "object", "value": rows}
            raise ValueError("tag")

        return walk(value, "$", 0)

    def validate_schema(value):
        if (not isinstance(value, dict) or set(value) != {"enabled", "payload"}
                or not isinstance(value["enabled"], bool)
                or not isinstance(value["payload"], list) or len(value["payload"]) != 3
                or not isinstance(value["payload"][0], int)
                or not isinstance(value["payload"][1], Decimal)
                or not isinstance(value["payload"][2], dict)
                or set(value["payload"][2]) != {"name", "series"}
                or not isinstance(value["payload"][2]["name"], str)
                or not isinstance(value["payload"][2]["series"], list)
                or not all(isinstance(item, Decimal)
                           for item in value["payload"][2]["series"])):
            raise ValueError("schema path")

    def bind(value, schema=True):
        if schema:
            validate_schema(value)
        return canonical_hash(canonical(value))

    fixture = {"payload": [7, Decimal("1.2300"),
                           {"name": "e\u0301", "series": [Decimal("1E-30"), Decimal("9.99E+30")]}],
               "enabled": True}
    equivalent = {"enabled": True,
                  "payload": [7, Decimal("1.23"),
                              {"series": [Decimal("0.000000000000000000000000000001"),
                                          Decimal("9.99E+30")], "name": "é"}]}
    malformed = {
        "path": ({"enabled": True, "payload": [7, Decimal("1"), {"name": "x"}]}, True),
        "tag": ({"enabled": True, "payload": [7, Decimal("1"), {"name": 3, "series": []}]}, True),
        "normalized_key": ({"é": 1, "e\u0301": 2}, False),
        "exponent_low": (Decimal("1E-31"), False),
        "exponent_high": (Decimal("1E+31"), False),
        "depth": ([[[[[[[[[[0]]]]]]]]]], False),
        "tokens": (list(range(61)), False),
        "integer": (max_integer + 1, False),
        "surrogate": ("\ud800", False),
        "reserved": ({"$type": 1}, False),
    }
    controls = {}
    for name, (value, schema) in malformed.items():
        try:
            bind(value, schema)
            controls[name] = False
        except (ValueError, TypeError):
            controls[name] = True
    return {"schema_path_equivalence": bind(fixture) == bind(equivalent),
            "canonical_sha256": bind(fixture), "negative_controls": controls,
            "caps": {"depth": max_depth, "tokens": max_tokens,
                     "minimum_exponent": -30, "maximum_exponent": 30,
                     "max_exact_integer": max_integer},
            "external_authority": None, "provider_job_invoice": None,
            "evidence_class": "SYNTHETIC_RECEIPT_CANONICALIZATION"}


def ten_reader_injected_fsync_gate(directory):
    root = Path(directory)
    rows, file_calls, directory_calls = [], 0, 0

    def valid_order(items):
        return items == ["write", "file_fsync", "replace", "directory_fsync"]

    for run in range(2):
        work = root / f"cycle036-{run}"
        work.mkdir(parents=True, exist_ok=True)
        target = work / "state.bin"
        target.write_bytes(b"old-complete-payload")
        old_handle = target.open("rb")
        observations = [[] for _ in range(10)]
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
                   for index in range(10)]
        for thread in threads:
            thread.start()
        retained, traces = [], []
        start.set()
        time.sleep(0.005)
        for stage in range(6):
            payload = (f"cycle036-run{run}-stage{stage}-".encode() + b"z" * (stage + 17))
            temporary = work / f"pending-{stage}.bin"
            trace = ["write"]
            with temporary.open("wb") as handle:
                handle.write(payload)
                handle.flush()
                os.fsync(handle.fileno())
                file_calls += 1
            trace.append("file_fsync")
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
                     "all_stage_orders_valid": all(valid_order(item) for item in traces)})

    def inject(failure):
        trace, replaced = ["write"], False
        try:
            if failure == "file_fsync":
                raise OSError("injected file fsync failure")
            trace.append("file_fsync")
            trace.append("replace")
            replaced = True
            if failure == "directory_fsync":
                raise OSError("injected directory fsync failure")
            trace.append("directory_fsync")
            accepted = valid_order(trace)
        except OSError:
            accepted = False
        return {"trace": trace, "replace_occurred": replaced,
                "evidence_promoted": accepted, "rejected_as_durable": not accepted}

    injected = {name: inject(name) for name in ("file_fsync", "directory_fsync")}
    return {"runs": rows, "reader_count": 10, "replacement_stages": 6,
            "all_reader_observations_complete": all(all(row["reader_complete"]) for row in rows),
            "all_retained_descriptors_complete": all(row["retained_descriptors_complete"] for row in rows),
            "all_fsync_orders_valid": all(row["all_stage_orders_valid"] for row in rows),
            "file_fsync_call_count": file_calls, "directory_fsync_call_count": directory_calls,
            "injected_failure_controls": injected,
            "crash_durability": None, "power_loss_durability": None,
            "evidence_class": "LOCAL_TEN_READER_INJECTED_FSYNC_FIXTURE"}


def zip64_adjacency_sentinel_gate():
    zip64_offset, zip64_position = 4096, 4096
    locator_position, classic_position = zip64_position + 56, zip64_position + 56 + 20
    comment = b"cycle036"

    def zip64(signature=0x06064B50, disk=0, entries=17, central_size=512,
              central_offset=2048):
        return struct.pack("<IQHHIIQQQQ", signature, 44, 45, 45, disk, disk,
                           entries, entries, central_size, central_offset)

    def locator(signature=0x07064B50, disk=0, offset=zip64_offset, disks=1):
        return struct.pack("<IIQI", signature, disk, offset, disks)

    def classic(bound_comment=comment, trailing=b"", disk=0, entries=0xFFFF,
                size=0xFFFFFFFF, offset=0xFFFFFFFF):
        return (struct.pack("<IHHHHIIH", 0x06054B50, disk, disk, entries, entries,
                            size, offset, len(bound_comment)) + bound_comment + trailing)

    def descriptor(crc=0xA1B2C3D4, compressed=1234, uncompressed=5678):
        return struct.pack("<IIQQ", 0x08074B50, crc, compressed, uncompressed)

    def verify(raw_zip64, raw_locator, raw_classic, raw_descriptor,
               positions=(zip64_position, locator_position, classic_position)):
        zfields = struct.unpack("<IQHHIIQQQQ", raw_zip64)
        if zfields != (0x06064B50, 44, 45, 45, 0, 0, 17, 17, 512, 2048):
            raise ValueError("zip64")
        lfields = struct.unpack("<IIQI", raw_locator)
        if lfields != (0x07064B50, 0, zip64_offset, 1):
            raise ValueError("locator")
        if positions[0] + len(raw_zip64) != positions[1] or positions[1] + len(raw_locator) != positions[2]:
            raise ValueError("adjacency")
        if len(raw_classic) < 22:
            raise ValueError("classic truncated")
        cfields = struct.unpack_from("<IHHHHIIH", raw_classic)
        if cfields[:-1] != (0x06054B50, 0, 0, 0xFFFF, 0xFFFF, 0xFFFFFFFF, 0xFFFFFFFF):
            raise ValueError("classic sentinel")
        if len(raw_classic) != 22 + cfields[-1] or raw_classic[22:] != comment:
            raise ValueError("comment/trailing")
        if struct.unpack("<IIQQ", raw_descriptor) != (0x08074B50, 0xA1B2C3D4, 1234, 5678):
            raise ValueError("descriptor")
        return True

    valid = verify(zip64(), locator(), classic(), descriptor())
    cases = {
        "adjacency": (zip64(), locator(), classic(), descriptor(),
                      (zip64_position, locator_position + 1, classic_position + 1)),
        "signature": (zip64(signature=0), locator(), classic(), descriptor()),
        "sentinel": (zip64(), locator(), classic(entries=17), descriptor()),
        "multi_disk": (zip64(disk=1), locator(), classic(), descriptor()),
        "locator_offset": (zip64(), locator(offset=zip64_offset - 1), classic(), descriptor()),
        "crc": (zip64(), locator(), classic(), descriptor(crc=0)),
        "size": (zip64(), locator(), classic(), descriptor(compressed=1235)),
        "comment": (zip64(), locator(), classic(b"other"), descriptor()),
        "trailing": (zip64(), locator(), classic(trailing=b"x"), descriptor()),
    }
    controls = {}
    for name, args in cases.items():
        try:
            verify(*args)
            controls[name] = False
        except (ValueError, struct.error):
            controls[name] = True
    return {"valid_metadata": valid, "zip64_eocd_position": zip64_position,
            "locator_position": locator_position, "classic_eocd_position": classic_position,
            "adjacency_bytes": [56, 20], "negative_controls": controls,
            "payload_read": False, "real_producer_corpus": None,
            "evidence_class": "SYNTHETIC_ZIP64_METADATA"}


def sixteen_issuer_revocation_chain():
    sample = hashlib.sha256(b"cycle036-synthetic-custody").hexdigest()
    specs = [(f"issuer-{index:02d}", f"scope-{index:02d}") for index in range(16)]
    keys = {name: f"synthetic-{name}" for name in ("rev-c", "rev-d", "rev-e", "rev-f", "rev-g")}
    policies, previous = [], "0" * 64
    for version, epoch, active in ((34, 7, ["rev-c", "rev-d", "rev-e"]),
                                   (35, 8, ["rev-d", "rev-e", "rev-f"]),
                                   (36, 9, ["rev-e", "rev-f", "rev-g"])):
        body = {"version": version, "revocation_epoch": epoch, "active": active,
                "threshold": 2, "previous_policy_sha256": previous}
        policy = {**body, "policy_sha256": canonical_hash(body)}
        policies.append(policy)
        previous = policy["policy_sha256"]
    by_version = {item["version"]: item for item in policies}
    registry = {issuer: {scope} for issuer, scope in specs}
    ancestry = {"issuer-15": "issuer-14", "issuer-14": "issuer-13"}

    def build(path="fixture-036"):
        events, prior = [], "0" * 64
        for sequence, (issuer, scope) in enumerate(specs):
            event = make_custody_event(sequence, sample, path, issuer, scope,
                                       "2026-01-01", "2027-02-01", prior)
            events.append(event)
            prior = event["event_sha256"]
        return events

    def receipt(signer, head, receipt_id, version=36, epoch=9, issued=100,
                expires=200, policy_sha=None):
        policy = by_version[version]
        body = {"receipt_id": receipt_id, "signer": signer, "head_sha256": head,
                "policy_version": version, "revocation_epoch": epoch,
                "policy_sha256": policy["policy_sha256"] if policy_sha is None else policy_sha,
                "issued_at": issued, "expires_at": expires}
        return {**body, "synthetic_signature": canonical_hash({**body, "key": keys[signer]})}

    def verify_policy_chain(bound):
        if len(bound) != 3:
            raise ValueError("policy chain length")
        prior = "0" * 64
        for expected_version, expected_epoch, item in zip((34, 35, 36), (7, 8, 9), bound):
            unsigned = {key: value for key, value in item.items() if key != "policy_sha256"}
            if (item["version"] != expected_version or item["revocation_epoch"] != expected_epoch
                    or item["previous_policy_sha256"] != prior
                    or item["policy_sha256"] != canonical_hash(unsigned)):
                raise ValueError("policy chain")
            prior = item["policy_sha256"]
        return prior

    def verify(events, receipts, bound_policies=policies, now=150,
               bound_registry=registry, bound_ancestry=ancestry, date="2026-12-15"):
        terminal = verify_policy_chain(bound_policies)
        current, head = bound_policies[-1], events[-1]["event_sha256"]
        signers, identifiers = set(), set()
        for item in receipts:
            signer = item["signer"]
            unsigned = {key: value for key, value in item.items() if key != "synthetic_signature"}
            if (item["policy_version"] != current["version"]
                    or item["revocation_epoch"] != current["revocation_epoch"]
                    or item["policy_sha256"] != terminal or signer not in current["active"]
                    or signer in signers or item["receipt_id"] in identifiers
                    or item["head_sha256"] != head
                    or not item["issued_at"] <= now <= item["expires_at"]
                    or item["synthetic_signature"] != canonical_hash({**unsigned, "key": keys[signer]})):
                raise ValueError("receipt")
            signers.add(signer)
            identifiers.add(item["receipt_id"])
        if len(signers) < current["threshold"]:
            raise ValueError("quorum")
        if any(item["path_id"] != "fixture-036" for item in events):
            raise ValueError("path")
        if bound_ancestry != ancestry:
            raise ValueError("ancestry")
        return verify_custody_chain(events, bound_registry, date)

    events = build()
    head = events[-1]["event_sha256"]
    valid_receipts = [receipt("rev-e", head, "r-e"), receipt("rev-f", head, "r-f")]
    valid = verify(events, valid_receipts)
    fork = json.loads(json.dumps(policies))
    fork[2]["previous_policy_sha256"] = "0" * 64
    other_events = build("other")
    other_head = other_events[-1]["event_sha256"]
    cases = {
        "rollback": (events, valid_receipts, policies[:2], 150, registry, ancestry, "2026-12-15"),
        "fork": (events, valid_receipts, fork, 150, registry, ancestry, "2026-12-15"),
        "revocation_epoch": (events, [receipt("rev-e", head, "old-e", epoch=8), valid_receipts[1]], policies, 150, registry, ancestry, "2026-12-15"),
        "cross_policy_replay": (events, [receipt("rev-e", head, "v35-e", version=35, epoch=8), receipt("rev-f", head, "v35-f", version=35, epoch=8)], policies, 150, registry, ancestry, "2026-12-15"),
        "duplicate_receipt": (events, [valid_receipts[0], valid_receipts[0]], policies, 150, registry, ancestry, "2026-12-15"),
        "inactive_signer": (events, [receipt("rev-d", head, "inactive"), valid_receipts[0]], policies, 150, registry, ancestry, "2026-12-15"),
        "quorum": (events, valid_receipts[:1], policies, 150, registry, ancestry, "2026-12-15"),
        "stale": (events, [receipt("rev-e", head, "stale", expires=149), valid_receipts[1]], policies, 150, registry, ancestry, "2026-12-15"),
        "head": (events, [receipt("rev-e", "0" * 64, "bad-e"), receipt("rev-f", "0" * 64, "bad-f")], policies, 150, registry, ancestry, "2026-12-15"),
        "scope": (events, valid_receipts, policies, 150, {**registry, "issuer-15": {"wrong"}}, ancestry, "2026-12-15"),
        "ancestry": (events, valid_receipts, policies, 150, registry, {"issuer-15": "issuer-13"}, "2026-12-15"),
        "path": (other_events, [receipt("rev-e", other_head, "other-e"), receipt("rev-f", other_head, "other-f")], policies, 150, registry, ancestry, "2026-12-15"),
    }
    controls = {}
    for name, args in cases.items():
        try:
            verify(*args)
            controls[name] = False
        except (ValueError, KeyError):
            controls[name] = True
    return {"event_count": 16, "policy_versions": [34, 35, 36],
            "revocation_epochs": [7, 8, 9], "receipt_threshold": 2,
            "policy_chain_terminal_sha256": policies[-1]["policy_sha256"],
            "terminal_sha256": valid["final_event_sha256"],
            "boundary_rejections": controls,
            "signature_kind": "SYNTHETIC_HASH_FIXTURE_NOT_CRYPTOGRAPHIC_SIGNATURE",
            "physical_sample": None, "evidence_class": "SYNTHETIC_CUSTODY"}


def twenty_component_composed_permutations(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("source")
    n = 20
    order = [f"component-{index:02d}" for index in range(n)]
    labels = ["compute"] * 5 + ["memory"] * 5 + ["network"] * 5 + ["control"] * 5
    intervals = [[index + 2, index + 9] for index in range(n)]
    mask = [[i == j or (labels[i] == labels[j] and abs(i - j) == 1)
             for j in range(n)] for i in range(n)]
    positive = [[0.05 if i == j else (0.0001 if mask[i][j] else 0.0)
                 for j in range(n)] for i in range(n)]
    matrices = {
        "positive": positive,
        "zero": [[0.05 if i == j else 0.0 for j in range(n)] for i in range(n)],
        "negative": [[0.05 if i == j else (-0.0001 if mask[i][j] else 0.0)
                      for j in range(n)] for i in range(n)],
        "missing": None,
        "indefinite": [[1.0 if i == j else 2.0 for j in range(n)] for i in range(n)],
        "nonfinite": [[float("inf") if i == j == 0 else (1.0 if i == j else 0.0)
                       for j in range(n)] for i in range(n)],
    }
    first = [*range(5, n), *range(5)]
    second = [*range(10, n), *range(10)]
    composed = [first[index] for index in second]
    inverse = [composed.index(index) for index in range(n)]

    def permute_vector(items, indices):
        return [items[index] for index in indices]

    def permute_matrix(matrix, indices):
        return None if matrix is None else [[matrix[i][j] for j in indices] for i in indices]

    sequential_intervals = permute_vector(permute_vector(intervals, first), second)
    composed_intervals = permute_vector(intervals, composed)
    recovered_intervals = permute_vector(composed_intervals, inverse)
    sequential_matrices = {name: permute_matrix(permute_matrix(value, first), second)
                           for name, value in matrices.items()}
    composed_matrices = {name: permute_matrix(value, composed) for name, value in matrices.items()}
    recovered_matrices = {name: permute_matrix(value, inverse)
                          for name, value in composed_matrices.items()}
    sigmas = [0.0, 1.0, 2.0, 3.0, 5.0, 8.0, 13.0, 21.0]
    sweeps = {str(sigma): component_covariance_sweep(intervals, matrices, [1, 10, 20, 0], sigma=sigma)
              for sigma in sigmas}
    permuted_sweeps = {str(sigma): component_covariance_sweep(composed_intervals, composed_matrices,
                                                              [1, 10, 20, 0], sigma=sigma)
                       for sigma in sigmas}
    source_sha = hashlib.sha256(source_bytes).hexdigest()
    binding = {"source_sha256": source_sha, "order": order, "labels": labels,
               "mask": mask, "first": first, "second": second,
               "composed": composed, "inverse": inverse, "sigmas": sigmas}
    identity = canonical_hash(binding)
    mutations = {"order": {**binding, "order": list(reversed(order))},
                 "labels": {**binding, "labels": list(reversed(labels))},
                 "composition": {**binding, "composed": list(reversed(composed))},
                 "inverse": {**binding, "inverse": list(reversed(inverse))}}
    return {"components": n, "source_sha256": source_sha, "component_order": order,
            "block_labels": labels, "first_permutation": first, "second_permutation": second,
            "composed_permutation": composed, "inverse_permutation": inverse,
            "composition_matches_sequential_intervals": sequential_intervals == composed_intervals,
            "composition_matches_sequential_matrices": sequential_matrices == composed_matrices,
            "inverse_map_valid": all(inverse[composed[index]] == index for index in range(n)),
            "double_permutation_recovers_intervals": recovered_intervals == intervals,
            "double_permutation_recovers_matrices": recovered_matrices == matrices,
            "permutation_equivalence": sweeps == permuted_sweeps,
            "sparse_nonzero_count": sum(sum(row) for row in mask),
            "covariance_grid_sha256": identity,
            "binding_mutation_rejections": {name: canonical_hash(value) != identity
                                             for name, value in mutations.items()},
            "sigma_values": sigmas, "sweeps": sweeps,
            "commercial_interpretation": None, "evidence_class": "MODEL_ONLY"}


def seven_signed_transform_principal_minors():
    matrix = [[Fraction(16), Fraction(1), Fraction(2), Fraction(1)],
              [Fraction(1), Fraction(25), Fraction(1), Fraction(2)],
              [Fraction(2), Fraction(1), Fraction(36), Fraction(1)],
              [Fraction(1), Fraction(2), Fraction(1), Fraction(64)]]
    identity = ([0, 1, 2, 3], [1, 1, 1, 1])
    transforms = [
        ([1, 0, 3, 2], [1, -1, 1, -1]), ([2, 3, 0, 1], [-1, 1, -1, 1]),
        ([3, 2, 1, 0], [1, 1, -1, -1]), ([0, 2, 1, 3], [-1, 1, 1, -1]),
        ([2, 0, 3, 1], [1, -1, -1, 1]), ([3, 1, 0, 2], [-1, -1, 1, 1]),
        ([1, 3, 0, 2], [1, 1, -1, -1]),
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
    for left, right in [(i, (i + 1) % len(transforms)) for i in range(len(transforms))]:
        product = combine(transforms[left], transforms[right])
        rows.append({"left": left, "right": right,
                     "closure": sorted(product[0]) == list(range(4))
                     and all(value in (-1, 1) for value in product[1]),
                     "inverse_roundtrip": combine(inverse(product), product) == identity})
    original_minors, transformed_minors = principal_minors(matrix), principal_minors(sequential)
    return {"transform_count": 7, "matrix_product_count": 112,
            "cayley_rows": rows,
            "all_cayley_rows_valid": all(row["closure"] and row["inverse_roundtrip"] for row in rows),
            "closure_is_signed_permutation": sorted(composed[0]) == list(range(4)),
            "associative_composition": sequential == apply(matrix, composed),
            "exact_reverse_order_roundtrip": restored == matrix,
            "trace_invariant": sum(sequential[i][i] for i in range(4)) == sum(matrix[i][i] for i in range(4)),
            "determinant_absolute_invariant": abs(determinant(sequential)) == abs(determinant(matrix)),
            "original_principal_minors": [[value.numerator, value.denominator] for value in original_minors],
            "transformed_principal_minors": [[value.numerator, value.denominator]
                                               for value in transformed_minors],
            "all_principal_minors_positive": all(value > 0 for value in original_minors + transformed_minors),
            "symmetric": all(sequential[i][j] == sequential[j][i] for i in range(4) for j in range(4)),
            "composition_sha256": canonical_hash({"permutations": [item[0] for item in transforms],
                                                    "signs": [item[1] for item in transforms]}),
            "calibration": None, "evidence_class": "SYNTHETIC_TYPED_COVARIANCE"}


def twenty_scenario_deletion_intervals():
    scenarios = [
        [4, 3, 2, 1], [2, 2, 1, 0], [2, 1, 2, 0], [1, 1, 1, 1],
        [0, 3, 2, 3], [0, 1, 2, 3], [3, 0, 3, 1], [1, 4, 0, 4],
        [2, 4, 4, 1], [4, 0, 1, 4], [3, 2, 4, 0], [0, 4, 3, 2],
        [4, 2, 0, 3], [1, 3, 4, 2], [2, 0, 4, 3], [3, 4, 1, 2],
        [4, 1, 3, 2], [2, 3, 1, 4], [1, 2, 4, 3], [3, 1, 4, 2],
    ]

    def contribution(scores):
        eligible = {index for index, score in enumerate(scores) if score == max(scores)}
        output = [0, 0, 0, 0]
        for order in itertools.permutations(range(4)):
            output[next(item for item in order if item in eligible)] += 1
        return output

    contributions = [contribution(item) for item in scenarios]
    full = [sum(row[index] for row in contributions) for index in range(4)]
    fractions = [Fraction(value, 20 * 24) for value in full]
    grid_counts = {}
    for removed_count in range(1, 13):
        count, denominator = 0, (20 - removed_count) * 24
        for removed in itertools.combinations(range(20), removed_count):
            count += 1
            row = [full[index] - sum(contributions[item][index] for item in removed)
                   for index in range(4)]
            fractions.extend(Fraction(value, denominator) for value in row)
        grid_counts[str(removed_count)] = count
    low, high = min(fractions), max(fractions)
    return {"scenario_count": 20, "orders_each": 24, "full_grid_size": 480,
            "winner_counts": full, "deletion_grid_counts": grid_counts,
            "all_grid_interval": [[low.numerator, low.denominator],
                                  [high.numerator, high.denominator]],
            "probability_claim": None, "capital": None,
            "evidence_class": "FINITE_ILLUSTRATIVE_SCENARIO"}


def thirteen_unit_affine_bilipschitz(*raw_sources):
    if len(raw_sources) != 13 or any(not isinstance(item, bytes) or not item for item in raw_sources):
        raise ValueError("sources")
    source_sha = [hashlib.sha256(item).hexdigest() for item in raw_sources]
    maps = []
    for index, digest in enumerate(bytes.fromhex(item) for item in source_sha):
        slope = Fraction(2 + digest[0] % 7, 1 + digest[1] % 5)
        bias = Fraction(digest[2] % 11, 1 + digest[3] % 7)
        maps.append({"slope": slope, "bias": bias,
                     "input_unit": f"u{index:02d}", "output_unit": f"u{index + 1:02d}"})

    def compose(bound):
        slope, bias, unit = Fraction(1), Fraction(0), bound[0]["input_unit"]
        for item in bound:
            if item["input_unit"] != unit or item["slope"] <= 0:
                raise ValueError("unit/monotonicity")
            slope, bias = item["slope"] * slope, item["slope"] * bias + item["bias"]
            unit = item["output_unit"]
        return slope, bias, unit

    slope, bias, terminal_unit = compose(maps)
    interval = (Fraction(2, 3), Fraction(5, 3))
    transformed = (slope * interval[0] + bias, slope * interval[1] + bias)
    recovered = ((transformed[0] - bias) / slope, (transformed[1] - bias) / slope)
    unit_mutation = [dict(item) for item in maps]
    unit_mutation[7]["input_unit"] = "wrong-unit"
    controls = {
        "source_order": source_sha != list(reversed(source_sha)),
        "dimension": len(maps[:-1]) != 13,
        "unit": False,
        "nonmonotone": False,
    }
    try:
        compose(unit_mutation)
    except ValueError:
        controls["unit"] = True
    nonmonotone = [dict(item) for item in maps]
    nonmonotone[4]["slope"] = Fraction(-1)
    try:
        compose(nonmonotone)
    except ValueError:
        controls["nonmonotone"] = True
    return {"source_sha256": source_sha, "map_count": len(maps),
            "unit_chain": [maps[0]["input_unit"], *[item["output_unit"] for item in maps]],
            "terminal_unit": terminal_unit, "associative_composition": compose(maps) == (slope, bias, terminal_unit),
            "composed_interval": [[value.numerator, value.denominator] for value in transformed],
            "lipschitz_bound": [slope.numerator, slope.denominator],
            "inverse_lipschitz_bound": [slope.denominator, slope.numerator],
            "lipschitz_product": [1, 1],
            "roundtrip_interval": [[value.numerator, value.denominator] for value in recovered],
            "exact_roundtrip": recovered == interval, "negative_controls": controls,
            "sort": ["RealModel", "Model"], "new_law_claim": None,
            "evidence_class": "SOURCE_TYPED_RATIONAL_MODEL"}


def nine_observer_membership_transition():
    observers = [f"observer-{index:02d}" for index in range(9)]
    first_body = {"epoch": 16, "members": observers, "previous_sha256": "0" * 64,
                  "key_epoch": 1}
    first = {**first_body, "transition_sha256": canonical_hash(first_body)}
    second_body = {"epoch": 17, "members": observers,
                   "previous_sha256": first["transition_sha256"], "key_epoch": 2}
    second = {**second_body, "transition_sha256": canonical_hash(second_body)}
    head = canonical_hash({"domain": "fiction-scm-036", "height": 36})

    def certificate(signers, nonce, epoch=17, bound_head=head, audience="uqpu-scm",
                    transition=second["transition_sha256"], policy=36):
        return {"signers": signers, "nonce": nonce, "membership_epoch": epoch,
                "head_sha256": bound_head, "audience": audience,
                "transition_sha256": transition, "policy_version": policy}

    left = certificate(observers[:7], "left")
    right = certificate(observers[2:], "right")

    def validate_pair(one, two, transition=second):
        unsigned = {key: value for key, value in transition.items() if key != "transition_sha256"}
        if (transition["transition_sha256"] != canonical_hash(unsigned)
                or transition["previous_sha256"] != first["transition_sha256"]):
            return False
        for item in (one, two):
            signers = item["signers"]
            if (len(signers) != 7 or len(set(signers)) != 7
                    or not set(signers) <= set(transition["members"])
                    or item["membership_epoch"] != transition["epoch"]
                    or item["head_sha256"] != head or item["audience"] != "uqpu-scm"
                    or item["transition_sha256"] != transition["transition_sha256"]
                    or item["policy_version"] != 36):
                return False
        return one["nonce"] != two["nonce"] and len(set(one["signers"]) & set(two["signers"])) >= 5

    altered_transition = dict(second)
    altered_transition["previous_sha256"] = "0" * 64
    cases = {
        "valid": (left, right, second, True),
        "split": (left, certificate(observers[3:], "short"), second, False),
        "stale": (left, certificate(observers[2:], "right", epoch=16), second, False),
        "fork": (left, certificate(observers[2:], "right", bound_head="0" * 64), second, False),
        "replay": (left, certificate(observers[2:], "left"), second, False),
        "downgrade": (left, certificate(observers[2:], "right", policy=35), second, False),
        "audience": (left, certificate(observers[2:], "right", audience="wrong"), second, False),
        "membership_hash": (left, certificate(observers[2:], "right", transition="0" * 64), second, False),
        "transition_chain": (left, right, altered_transition, False),
        "revocation": (left, certificate([*observers[2:8], "observer-09"], "right"), second, False),
        "missing_member": (left, certificate(observers[2:8], "right"), second, False),
    }
    table = [{"case": name, "accepted": validate_pair(one, two, transition), "expected": expected}
             for name, (one, two, transition, expected) in cases.items()]
    return {"observer_count": 9, "quorum": 7,
            "certificate_intersection_size": len(set(left["signers"]) & set(right["signers"])),
            "minimum_quorum_intersection": 5, "membership_epoch": 17,
            "transition_chain_sha256": second["transition_sha256"],
            "control_table": table,
            "all_controls_match": all(row["accepted"] == row["expected"] for row in table),
            "sort": "Fiction", "empirical_coupling": None, "evidence_class": "FICTION_ONLY"}


def lineage_manifest_v26(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("source")
    source_sha = hashlib.sha256(source_bytes).hexdigest()
    real = [{"kind": "real", "index": index, "source_sha256": source_sha,
             "schema": "uqpu-lineage-v26", "config": f"cfg-{index % 4}",
             "metric": f"metric-{index % 3}"} for index in range(13)]
    padding = [{"kind": "padding", "index": index, "domain": "uqpu-lineage-padding-v26"}
               for index in range(13, 16)]

    def leaf_hash(item):
        return canonical_hash({"domain": "uqpu-lineage-leaf-v26", **item})

    leaves = [leaf_hash(item) for item in [*real, *padding]]

    def combine(left, right):
        return canonical_hash({"domain": "uqpu-lineage-node-v26", "left": left, "right": right})

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

    def verify(item, item_proof, expected_root=root):
        index, value = item_proof["leaf_index"], leaf_hash(item)
        if item["index"] != index:
            return False
        for level, step in enumerate(item_proof["steps"]):
            expected_side = "left" if (index ^ 1) < index else "right"
            if step["level"] != level or step["side"] != expected_side:
                return False
            value = combine(step["hash"], value) if expected_side == "left" else combine(value, step["hash"])
            index //= 2
        return value == expected_root

    selected = [0, 4, 8, 12]
    exclusions = [13, 14, 15]
    inclusion_proofs = [proof(index) for index in selected]
    exclusion_proofs = [proof(index) for index in exclusions]
    valid = (all(verify(real[index], item) for index, item in zip(selected, inclusion_proofs))
             and all(verify(padding[index - 13], item)
                     for index, item in zip(exclusions, exclusion_proofs)))
    bad_inclusion = json.loads(json.dumps(inclusion_proofs[0]))
    bad_inclusion["steps"][0]["hash"] = "0" * 64
    bad_exclusion = json.loads(json.dumps(exclusion_proofs[0]))
    bad_exclusion["steps"][0]["hash"] = "0" * 64
    manifest = {"version": 26, "root_sha256": root, "source_sha256": source_sha,
                "real_indices": list(range(13)), "padding_exclusion_indices": exclusions,
                "selected_indices": selected,
                "config_sha256": canonical_hash([item["config"] for item in real]),
                "metric_sha256": canonical_hash([item["metric"] for item in real]),
                "inclusion_proof_sha256": canonical_hash(inclusion_proofs),
                "exclusion_proof_sha256": canonical_hash(exclusion_proofs)}

    def validate_manifest(bound, bound_inclusions=inclusion_proofs,
                          bound_exclusions=exclusion_proofs):
        expected = {"version": 26, "root_sha256": root, "source_sha256": source_sha,
                    "real_indices": list(range(13)), "padding_exclusion_indices": exclusions,
                    "selected_indices": selected,
                    "config_sha256": canonical_hash([item["config"] for item in real]),
                    "metric_sha256": canonical_hash([item["metric"] for item in real]),
                    "inclusion_proof_sha256": canonical_hash(bound_inclusions),
                    "exclusion_proof_sha256": canonical_hash(bound_exclusions)}
        return (bound == expected
                and all(verify(real[index], item)
                        for index, item in zip(selected, bound_inclusions))
                and all(verify(padding[index - 13], item)
                        for index, item in zip(exclusions, bound_exclusions)))

    mutations = {
        "root": {**manifest, "root_sha256": "0" * 64},
        "padding_exclusion": {**manifest, "padding_exclusion_indices": [12, 14, 15]},
        "order": {**manifest, "selected_indices": list(reversed(selected))},
        "index": {**manifest, "real_indices": list(range(12)) + [14]},
        "source": {**manifest, "source_sha256": "0" * 64},
        "schema": {**manifest, "version": 25},
        "config": {**manifest, "config_sha256": "0" * 64},
        "metric": {**manifest, "metric_sha256": "0" * 64},
    }
    minimality_mutation = json.loads(json.dumps(inclusion_proofs))
    minimality_mutation[0]["steps"].append(minimality_mutation[0]["steps"][-1])
    order_mutation = json.loads(json.dumps(inclusion_proofs))
    order_mutation[0]["steps"] = list(reversed(order_mutation[0]["steps"]))
    path_mutation = json.loads(json.dumps(inclusion_proofs))
    path_mutation[0]["steps"][0]["side"] = (
        "left" if path_mutation[0]["steps"][0]["side"] == "right" else "right")
    rejection = {name: not validate_manifest(value) for name, value in mutations.items()}
    rejection.update({"inclusion_proof": not validate_manifest(
                          {**manifest, "inclusion_proof_sha256": canonical_hash([bad_inclusion, *inclusion_proofs[1:]])},
                          [bad_inclusion, *inclusion_proofs[1:]]),
                      "exclusion_proof": not validate_manifest(
                          {**manifest, "exclusion_proof_sha256": canonical_hash([bad_exclusion, *exclusion_proofs[1:]])},
                          inclusion_proofs, [bad_exclusion, *exclusion_proofs[1:]]),
                      "proof_minimality": not validate_manifest(
                          {**manifest, "inclusion_proof_sha256": canonical_hash(minimality_mutation)},
                          minimality_mutation),
                      "proof_order": not validate_manifest(
                          {**manifest, "inclusion_proof_sha256": canonical_hash(order_mutation)},
                          order_mutation),
                      "proof_path": not validate_manifest(
                          {**manifest, "inclusion_proof_sha256": canonical_hash(path_mutation)},
                          path_mutation),
                      "padding_domain": leaf_hash({**padding[0], "domain": "wrong"}) != leaves[13]})
    proof_nodes = {(step["level"], step["side"], step["hash"])
                   for item in [*inclusion_proofs, *exclusion_proofs] for step in item["steps"]}
    return {"manifest": manifest, "real_leaf_count": 13, "padded_leaf_count": 16,
            "padding_leaf_count": 3, "padding_exclusion_count": 3,
            "selected_leaf_count": len(selected), "simultaneous_proof_count": 7,
            "compressed_proof_node_count": len(proof_nodes),
            "valid_manifest": valid and validate_manifest(manifest),
            "mutation_rejections": rejection, "candidate_result": None,
            "functional_equivalence": None, "evidence_class": "SYNTHETIC_DATA_LINEAGE"}


def fourteen_inverse_pairs_branched_dag():
    mask = 63

    def rotate_left(value, width):
        return ((value << width) | (value >> (6 - width))) & mask

    def rotate_right(value, width):
        return ((value >> width) | (value << (6 - width))) & mask

    operations = [
        ("add-01", lambda x: (x + 1) & mask, lambda x: (x - 1) & mask, 7, 2, 6),
        ("xor-03", lambda x: x ^ 3, lambda x: x ^ 3, 8, 3, 6),
        ("rotl-01", lambda x: rotate_left(x, 1), lambda x: rotate_right(x, 1), 9, 3, 6),
        ("add-05", lambda x: (x + 5) & mask, lambda x: (x - 5) & mask, 11, 4, 6),
        ("xor-12", lambda x: x ^ 12, lambda x: x ^ 12, 12, 4, 6),
        ("rotl-02", lambda x: rotate_left(x, 2), lambda x: rotate_right(x, 2), 13, 5, 6),
        ("add-07", lambda x: (x + 7) & mask, lambda x: (x - 7) & mask, 15, 5, 6),
        ("xor-21", lambda x: x ^ 21, lambda x: x ^ 21, 17, 6, 6),
        ("rotl-03", lambda x: rotate_left(x, 3), lambda x: rotate_right(x, 3), 19, 6, 6),
        ("add-09", lambda x: (x + 9) & mask, lambda x: (x - 9) & mask, 21, 7, 6),
        ("xor-42", lambda x: x ^ 42, lambda x: x ^ 42, 23, 7, 6),
        ("rotl-04", lambda x: rotate_left(x, 4), lambda x: rotate_right(x, 4), 25, 8, 6),
        ("add-11", lambda x: (x + 11) & mask, lambda x: (x - 11) & mask, 27, 8, 6),
        ("xor-33", lambda x: x ^ 33, lambda x: x ^ 33, 29, 9, 6),
    ]
    dependencies = [[], [], [0], [0], [1], [1], [2, 4], [3, 5],
                    [6], [6], [7], [7], [8, 10], [9, 11, 12]]

    def apply(value, sequence, inverse=False):
        iterable = reversed(sequence) if inverse else sequence
        for _, forward, backward, _, _, _ in iterable:
            value = backward(value) if inverse else forward(value)
        return value

    def validate_dag(bound):
        return (len(bound) == len(operations)
                and all(all(isinstance(parent, int) and 0 <= parent < index for parent in parents)
                        for index, parents in enumerate(bound)))

    def critical_depth(bound):
        values = []
        for index, parents in enumerate(bound):
            values.append(operations[index][4] + max((values[parent] for parent in parents), default=0))
        return max(values)

    def leaf(operation, index, bound_dependencies=dependencies):
        name, _, _, gates, depth, qubits = operation
        body = {"domain": "uqpu-resource-leaf-v5", "index": index, "name": name,
                "gates": gates, "depth": depth, "max_qubits": qubits,
                "depends_on": bound_dependencies[index]}
        return {"hash": canonical_hash(body), "gates": gates,
                "serial_depth": depth, "max_qubits": qubits}

    leaves = [leaf(operation, index) for index, operation in enumerate(operations)]
    size = 1
    while size < len(leaves):
        size *= 2
    for index in range(len(leaves), size):
        leaves.append({"hash": canonical_hash({"domain": "uqpu-resource-padding-v5", "index": index}),
                       "gates": 0, "serial_depth": 0, "max_qubits": 0})

    def combine(left, right):
        body = {"domain": "uqpu-resource-node-v5", "left": left["hash"], "right": right["hash"],
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
            expected = "left" if (cursor ^ 1) < cursor else "right"
            if (step["level"], step["index"], step["side"]) != (level, cursor, expected):
                return False
            sibling = {key: step[key] for key in ("hash", "gates", "serial_depth", "max_qubits")}
            value = combine(sibling, value) if expected == "left" else combine(value, sibling)
            cursor //= 2
        return value == root

    proofs = [proof(index) for index in range(len(operations))]
    encoded = [apply(value, operations) for value in range(64)]
    reconstructed = [apply(value, operations, True) for value in encoded]
    order_mutation = [operations[1], operations[0], *operations[2:]]
    dag_mutation = json.loads(json.dumps(dependencies))
    dag_mutation[6] = [7]
    proof_mutation = json.loads(json.dumps(proofs[0]))
    proof_mutation["steps"][0]["gates"] += 1
    resource_mutation = (*operations[-1][:3], operations[-1][3] + 1,
                         operations[-1][4], operations[-1][5])
    serial_depth = sum(item[4] for item in operations)
    return {"inverse_pair_names": [item[0] for item in operations],
            "resource_merkle_root_sha256": root["hash"], "proof_count": len(proofs),
            "dependency_dag": [{"node": index, "depends_on": parents}
                               for index, parents in enumerate(dependencies)],
            "dependency_dag_valid": validate_dag(dependencies),
            "dependency_dag_mutation_rejected": not validate_dag(dag_mutation),
            "all_inclusion_proofs_valid": all(verify(index, item, proofs[index])
                                             for index, item in enumerate(operations)),
            "proof_resource_mutation_rejected": not verify(0, operations[0], proof_mutation),
            "leaf_resource_mutation_rejected": not verify(13, resource_mutation, proofs[13]),
            "basis_states_checked": 64, "distinct_outputs": len(set(encoded)),
            "residual": sum(first != second for first, second in enumerate(reconstructed)),
            "order_mutation_witness_count": sum(item != apply(value, order_mutation)
                                                for value, item in enumerate(encoded)),
            "resource_bound": {"gates": root["gates"], "serial_depth": serial_depth,
                               "dag_critical_depth": critical_depth(dependencies),
                               "unconstrained_parallel_lower_bound": max(item[4] for item in operations),
                               "max_qubits": root["max_qubits"]},
            "parallel_bounds_are_model_only": True,
            "hardware": None, "evidence_class": "SYNTHETIC_INVERSE_OPERATOR"}


def run_cycle036_fixture(source_bytes, directory):
    with tempfile.TemporaryDirectory(dir=directory) as work:
        lanes = {
            "A": sixteenth_graph_orbit_representatives(),
            "B": schema_path_numeric_gate(),
            "C": ten_reader_injected_fsync_gate(work),
            "D": zip64_adjacency_sentinel_gate(),
            "E": sixteen_issuer_revocation_chain(),
            "F": twenty_component_composed_permutations(source_bytes),
            "G": seven_signed_transform_principal_minors(),
            "H": twenty_scenario_deletion_intervals(),
            "FND/EQN": thirteen_unit_affine_bilipschitz(
                source_bytes, source_bytes + b":two", source_bytes + b":three",
                source_bytes + b":four", source_bytes + b":five", source_bytes + b":six",
                source_bytes + b":seven", source_bytes + b":eight", source_bytes + b":nine",
                source_bytes + b":ten", source_bytes + b":eleven", source_bytes + b":twelve",
                source_bytes + b":thirteen"),
            "SCM": nine_observer_membership_transition(),
            "AI-COST": lineage_manifest_v26(source_bytes),
            "QOS/QSVT": fourteen_inverse_pairs_branched_dag(),
        }
    return {lane: {"status": "BLOCKED_WITH_PROGRESS", **value}
            for lane, value in lanes.items()}
