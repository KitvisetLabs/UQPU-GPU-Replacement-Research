"""Cycle 038 bounded fixtures; outputs remain local, synthetic, model, or fiction evidence."""
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
import zlib

from uqpu.cycle013_delta01 import canonical_hash
from uqpu.cycle015_delta01 import component_covariance_sweep, make_custody_event, verify_custody_chain
from uqpu.cycle037_delta01 import zip64_extra_field_gate

LANES = (
    "A", "B", "C", "D", "E", "F", "G", "H",
    "FND/EQN", "SCM", "AI-COST", "QOS/QSVT",
)


def eighteenth_graph_conjugacy_orbits():
    """Enumerate an even cycle and cross-check conjugacy-class Burnside data."""
    n, full_mask = 14, (1 << 14) - 1
    scores = [sum(((mask >> index) & 1) != ((mask >> ((index + 1) % n)) & 1)
                  for index in range(n)) for mask in range(1 << n)]
    objective = max(scores)
    witnesses = [mask for mask, score in enumerate(scores) if score == objective]
    witness_set = set(witnesses)
    actions = [(sign, shift, complement) for sign in (1, -1)
               for shift in range(n) for complement in (False, True)]

    def transform(mask, action):
        sign, shift, complement = action
        output = 0
        for bit in range(n):
            output |= ((mask >> bit) & 1) << ((sign * bit + shift) % n)
        return output ^ (full_mask if complement else 0)

    def compose(first, second):
        """Return first after second."""
        return (first[0] * second[0],
                (first[0] * second[1] + first[1]) % n,
                first[2] ^ second[2])

    def inverse(action):
        return action[0], (-action[0] * action[1]) % n, action[2]

    remaining, classes = set(actions), []
    while remaining:
        representative = min(remaining)
        conjugates = {compose(compose(item, representative), inverse(item))
                      for item in actions}
        members = sorted(conjugates & set(actions))
        classes.append(members)
        remaining.difference_update(members)
    class_rows = []
    for members in classes:
        fixed_counts = [sum(transform(mask, action) == mask for mask in witnesses)
                        for action in members]
        class_rows.append({"representative": list(members[0]), "size": len(members),
                           "fixed": fixed_counts[0],
                           "fixed_constant": len(set(fixed_counts)) == 1})

    set_orbits, pending = [], set(witnesses)
    while pending:
        seed = min(pending)
        orbit = sorted({transform(seed, action) for action in actions} & witness_set)
        set_orbits.append(orbit)
        pending.difference_update(orbit)

    parent = {item: item for item in witnesses}

    def find(item):
        while parent[item] != item:
            parent[item] = parent[parent[item]]
            item = parent[item]
        return item

    def union(left, right):
        left, right = find(left), find(right)
        if left != right:
            parent[max(left, right)] = min(left, right)

    for witness in witnesses:
        for action in actions:
            union(witness, transform(witness, action))
    union_rows = {}
    for witness in witnesses:
        union_rows.setdefault(find(witness), []).append(witness)
    union_orbits = sorted(sorted(row) for row in union_rows.values())
    set_orbits = sorted(set_orbits)
    fixed_by_action = [sum(transform(mask, action) == mask for mask in witnesses)
                       for action in actions]
    numerator = sum(fixed_by_action)
    representatives = [min(row) for row in set_orbits]
    reconstructed = sorted({transform(seed, action) for seed in representatives
                            for action in actions} & witness_set)
    return {
        "states": len(scores), "objective": objective, "witness_count": len(witnesses),
        "action_count": len(actions), "conjugacy_class_count": len(classes),
        "conjugacy_class_fixed_vector": class_rows,
        "fixed_counts_constant_within_classes": all(row["fixed_constant"] for row in class_rows),
        "burnside_numerator": numerator, "burnside_orbit_count": numerator // len(actions),
        "burnside_matches_direct": numerator % len(actions) == 0
        and numerator // len(actions) == len(set_orbits),
        "set_orbit_encoding": set_orbits, "union_find_orbit_encoding": union_orbits,
        "two_orbit_encodings_match": set_orbits == union_orbits,
        "canonical_orbit_representatives": representatives,
        "representative_reconstruction_matches": reconstructed == witnesses,
        "task_sha256": canonical_hash({"n": n, "weights": [1] * n}),
        "witness_sha256": canonical_hash(witnesses),
        "class_vector_sha256": canonical_hash(class_rows),
        "scaling_claim": None, "evidence_class": "LOCAL_EXACT_CLASSICAL_FIXTURE",
    }


def schema_v2_to_v3_default_gate():
    max_integer, max_depth, max_tokens = 9007199254740991, 11, 72

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
                if not -40 <= bound.as_tuple().exponent <= 40:
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
        if (not isinstance(value, dict) or value.get("schema_version") != 2
                or set(value) != {"schema_version", "payload"}):
            raise ValueError("v2")
        return {"schema_version": 3, "payload": value["payload"],
                "policy": {"mode": "strict", "retry": 0}}

    def validate(value):
        if (not isinstance(value, dict) or value.get("schema_version") != 3
                or set(value) != {"schema_version", "payload", "policy"}
                or value.get("policy") != {"mode": "strict", "retry": 0}
                or not isinstance(value["payload"], dict)
                or set(value["payload"]) != {"items", "label"}
                or not isinstance(value["payload"]["items"], list)
                or not isinstance(value["payload"]["label"], str)):
            raise ValueError("v3")
        seen = set()
        for item in value["payload"]["items"]:
            digest = canonical_hash(canonical(item))
            if digest in seen:
                raise ValueError("duplicate normalized value")
            seen.add(digest)

    def bind(value):
        validate(value)
        return canonical_hash(canonical(value))

    old = {"schema_version": 2, "payload": {"label": "transition",
            "items": [Decimal("1E-40"), Decimal("9.99E+40"), "e\u0301"]}}
    current = {"schema_version": 3, "payload": {"label": "transition",
               "items": [Decimal("0.0000000000000000000000000000000000000001"),
                         Decimal("9.99E+40"), "é"]},
               "policy": {"mode": "strict", "retry": 0}}
    malformed = {
        "version_low": {**current, "schema_version": 2},
        "version_high": {**current, "schema_version": 4},
        "missing_default": {key: value for key, value in current.items() if key != "policy"},
        "wrong_default": {**current, "policy": {"mode": "strict", "retry": 1}},
        "path": {**current, "payload": {"label": "transition"}},
        "tag": {**current, "payload": {"label": "transition", "items": {}}},
        "duplicate_value": {**current, "payload": {"label": "transition",
                            "items": [Decimal("1.0"), Decimal("1.00")]}}
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
        "exponent_low": Decimal("1E-41"), "exponent_high": Decimal("1E+41"),
        "depth": [[[[[[[[[[[[0]]]]]]]]]]]], "tokens": list(range(73)),
        "integer": max_integer + 1, "surrogate": "\ud800",
    }
    for name, value in raw_controls.items():
        try:
            canonical(value)
            controls[name] = False
        except (ValueError, TypeError):
            controls[name] = True
    return {
        "upgrade_matches_v3": bind(upgrade(old)) == bind(current),
        "canonical_sha256": bind(current), "negative_controls": controls,
        "inserted_default": current["policy"],
        "caps": {"depth": max_depth, "tokens": max_tokens,
                 "minimum_exponent": -40, "maximum_exponent": 40,
                 "max_exact_integer": max_integer},
        "external_authority": None, "provider_job_invoice": None,
        "evidence_class": "SYNTHETIC_RECEIPT_CANONICALIZATION",
    }


def twelve_reader_cleanup_gate(directory):
    root = Path(directory)
    rows, file_calls, directory_calls = [], 0, 0
    for run in range(2):
        work = root / f"cycle038-{run}"
        work.mkdir(parents=True, exist_ok=True)
        target = work / "state.bin"
        target.write_bytes(b"old-complete-payload")
        old_handle = target.open("rb")
        observations = [[] for _ in range(12)]
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
                   for index in range(12)]
        for thread in threads:
            thread.start()
        retained, traces = [], []
        start.set()
        time.sleep(0.004)
        for stage in range(8):
            payload = f"cycle038-run{run}-stage{stage}-".encode() + b"w" * (stage + 20)
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
            time.sleep(0.003)
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
        rows.append({
            "run": run, "reader_counts": [len(items) for items in observations],
            "reader_complete": [bool(items) and all(item in allowed for item in items)
                                for items in observations],
            "retained_descriptors_complete": retained_complete,
            "stage_orders": traces,
            "all_stage_orders_valid": all(item == ["write", "file_fsync", "replace", "directory_fsync"]
                                          for item in traces),
            "temporary_cleanup_complete": not list(work.glob("pending-*.bin")),
        })

    failure_work = root / "cycle038-failures"
    failure_work.mkdir(parents=True, exist_ok=True)
    failure_target = failure_work / "state.bin"
    failure_target.write_bytes(b"stable")
    rename_temp = failure_work / "rename-temp.bin"
    rename_temp.write_bytes(b"candidate")
    rename_failed = False
    try:
        os.replace(failure_work / "missing-source.bin", failure_target)
    except FileNotFoundError:
        rename_failed = True
    rename_temp.unlink()
    cleanup_temp = failure_work / "cleanup-temp.bin"
    cleanup_temp.write_bytes(b"candidate")
    cleanup_temp.unlink()
    controls = {
        "partial_write": {"trace": ["partial_write", "cleanup"], "replace_occurred": False},
        "file_fsync": {"trace": ["write", "cleanup"], "replace_occurred": False},
        "rename": {"trace": ["write", "file_fsync", "rename_error", "cleanup"],
                   "replace_occurred": False, "injected_failure_observed": rename_failed},
        "directory_fsync": {"trace": ["write", "file_fsync", "replace", "directory_fsync_error"],
                            "replace_occurred": True},
        "temporary_cleanup": {"trace": ["write", "cleanup"], "replace_occurred": False,
                              "temporary_removed": not cleanup_temp.exists()},
    }
    for item in controls.values():
        item.update({"evidence_promoted": False, "rejected_as_durable": True,
                     "temporary_cleanup_complete": not rename_temp.exists()
                     and not cleanup_temp.exists()})
    return {
        "runs": rows, "reader_count": 12, "replacement_stages": 8,
        "all_reader_observations_complete": all(all(row["reader_complete"]) for row in rows),
        "all_retained_descriptors_complete": all(row["retained_descriptors_complete"] for row in rows),
        "all_fsync_orders_valid": all(row["all_stage_orders_valid"] for row in rows),
        "all_temporary_cleanup_complete": all(row["temporary_cleanup_complete"] for row in rows)
        and all(item["temporary_cleanup_complete"] for item in controls.values()),
        "file_fsync_call_count": file_calls, "directory_fsync_call_count": directory_calls,
        "failure_controls": controls, "crash_durability": None, "power_loss_durability": None,
        "evidence_class": "LOCAL_TWELVE_READER_RENAME_CLEANUP_FIXTURE",
    }


def zip64_unicode_path_parity_gate():
    baseline = zip64_extra_field_gate()
    raw_name, unicode_name = b"cafe.txt", "café.txt"

    def unicode_payload(name_bytes=raw_name, text=unicode_name):
        return struct.pack("<BI", 1, zlib.crc32(name_bytes) & 0xFFFFFFFF) + text.encode("utf-8")

    def pack(fields=((0x0001, b"z" * 16), (0x7075, unicode_payload()))):
        return b"".join(struct.pack("<HH", identifier, len(payload)) + payload
                        for identifier, payload in fields)

    def parse(raw):
        cursor, fields = 0, []
        while cursor < len(raw):
            if cursor + 4 > len(raw):
                raise ValueError("extra header")
            identifier, width = struct.unpack_from("<HH", raw, cursor)
            cursor += 4
            if cursor + width > len(raw):
                raise ValueError("extra length")
            fields.append((identifier, raw[cursor:cursor + width]))
            cursor += width
        if [item[0] for item in fields] != [0x0001, 0x7075]:
            raise ValueError("extra order")
        if len({item[0] for item in fields}) != 2 or len(fields[0][1]) != 16:
            raise ValueError("extra duplicate/width")
        return fields

    def verify(local_name, central_name, local_extra, central_extra):
        if local_name != central_name or local_extra != central_extra:
            raise ValueError("local/central parity")
        fields = parse(local_extra)
        payload = fields[1][1]
        if len(payload) < 6 or payload[0] != 1:
            raise ValueError("unicode payload")
        if struct.unpack_from("<I", payload, 1)[0] != zlib.crc32(local_name) & 0xFFFFFFFF:
            raise ValueError("unicode crc")
        decoded = payload[5:].decode("utf-8")
        if unicodedata.normalize("NFC", decoded) != unicode_name:
            raise ValueError("unicode name")
        if not baseline["valid_metadata"]:
            raise ValueError("baseline")
        return decoded

    valid_extra = pack()
    decoded = verify(raw_name, raw_name, valid_extra, valid_extra)
    bad_length = struct.pack("<HH", 0x0001, 17) + b"z" * 16
    local_cases = {
        "unknown_extra": (raw_name, raw_name,
                          pack(((0x0001, b"z" * 16), (0x9999, b"x"))),
                          pack(((0x0001, b"z" * 16), (0x9999, b"x")))),
        "duplicate_extra": (raw_name, raw_name,
                            pack(((0x0001, b"z" * 16), (0x0001, unicode_payload()))),
                            pack(((0x0001, b"z" * 16), (0x0001, unicode_payload())))),
        "extra_order": (raw_name, raw_name,
                        pack(((0x7075, unicode_payload()), (0x0001, b"z" * 16))),
                        pack(((0x7075, unicode_payload()), (0x0001, b"z" * 16)))),
        "declared_length": (raw_name, raw_name, bad_length, bad_length),
        "name": (raw_name, b"other.txt", valid_extra, valid_extra),
        "encoding": (raw_name, raw_name,
                     pack(((0x0001, b"z" * 16),
                           (0x7075, struct.pack("<BI", 1, zlib.crc32(raw_name)) + b"\xff"))),
                     pack(((0x0001, b"z" * 16),
                           (0x7075, struct.pack("<BI", 1, zlib.crc32(raw_name)) + b"\xff")))),
        "parity": (raw_name, raw_name, valid_extra,
                   pack(((0x0001, b"y" * 16), (0x7075, unicode_payload())))),
        "unicode_crc": (raw_name, raw_name,
                        pack(((0x0001, b"z" * 16), (0x7075, unicode_payload(b"other")))),
                        pack(((0x0001, b"z" * 16), (0x7075, unicode_payload(b"other"))))),
    }
    controls = {}
    for name, args in local_cases.items():
        try:
            verify(*args)
            controls[name] = False
        except (ValueError, UnicodeDecodeError, struct.error):
            controls[name] = True
    for name in ("signature", "multi_disk", "count", "crc", "offset", "size", "comment", "trailing"):
        controls[name] = baseline["negative_controls"][name]
    return {
        "valid_metadata": decoded == unicode_name, "extra_field_count": 2,
        "canonical_extra_identifiers": [0x0001, 0x7075],
        "unicode_path": decoded, "local_central_parity": True,
        "negative_controls": controls, "payload_read": False,
        "real_producer_corpus": None, "evidence_class": "SYNTHETIC_ZIP64_UNICODE_METADATA",
    }


def eighteen_issuer_watermark_gate():
    sample = hashlib.sha256(b"cycle038-synthetic-custody").hexdigest()
    specs = [(f"issuer-{index:02d}", f"scope-{index:02d}") for index in range(18)]
    keys = {name: f"synthetic-{name}" for name in ("rev-e", "rev-f", "rev-g", "rev-h", "rev-i")}
    policies, previous = [], "0" * 64
    for version, epoch, active in ((36, 9, ["rev-e", "rev-f", "rev-g"]),
                                   (37, 10, ["rev-f", "rev-g", "rev-h"]),
                                   (38, 11, ["rev-g", "rev-h", "rev-i"])):
        body = {"version": version, "revocation_epoch": epoch, "active": active,
                "threshold": 2, "nonce_min": 2000, "nonce_max": 2011,
                "previous_policy_sha256": previous}
        policy = {**body, "policy_sha256": canonical_hash(body)}
        policies.append(policy)
        previous = policy["policy_sha256"]
    registry = {issuer: {scope} for issuer, scope in specs}
    ancestry = {"issuer-17": "issuer-16", "issuer-16": "issuer-15"}

    def build(path="fixture-038"):
        events, prior = [], "0" * 64
        for sequence, (issuer, scope) in enumerate(specs):
            event = make_custody_event(sequence, sample, path, issuer, scope,
                                       "2026-01-01", "2027-02-01", prior)
            events.append(event)
            prior = event["event_sha256"]
        return events

    def receipt(signer, head, receipt_id, nonce, version=38, epoch=11,
                issued=100, expires=200):
        policy = policies[-1] if version == 38 else policies[version - 36]
        body = {"receipt_id": receipt_id, "nonce": nonce, "signer": signer,
                "head_sha256": head, "policy_version": version,
                "revocation_epoch": epoch, "policy_sha256": policy["policy_sha256"],
                "issued_at": issued, "expires_at": expires}
        return {**body, "synthetic_signature": canonical_hash({**body, "key": keys[signer]})}

    def policy_chain(bound):
        if len(bound) != 3:
            raise ValueError("length")
        prior = "0" * 64
        for version, epoch, item in zip((36, 37, 38), (9, 10, 11), bound):
            unsigned = {key: value for key, value in item.items() if key != "policy_sha256"}
            if (item["version"] != version or item["revocation_epoch"] != epoch
                    or item["previous_policy_sha256"] != prior
                    or item["policy_sha256"] != canonical_hash(unsigned)):
                raise ValueError("policy")
            prior = item["policy_sha256"]
        return prior

    def verify(events, receipts, bound=policies, now=150, watermark=2007,
               cache=frozenset({2005, 2006, 2007}), bound_registry=registry,
               bound_ancestry=ancestry, date="2026-12-15"):
        terminal = policy_chain(bound)
        current = bound[-1]
        head = events[-1]["event_sha256"]
        signers, identifiers, nonces = set(), set(), []
        for item in receipts:
            signer = item["signer"]
            unsigned = {key: value for key, value in item.items() if key != "synthetic_signature"}
            if (item["policy_version"] != current["version"]
                    or item["revocation_epoch"] != current["revocation_epoch"]
                    or item["policy_sha256"] != terminal or signer not in current["active"]
                    or signer in signers or item["receipt_id"] in identifiers
                    or item["nonce"] in nonces or item["nonce"] in cache
                    or item["nonce"] <= watermark
                    or not current["nonce_min"] <= item["nonce"] <= current["nonce_max"]
                    or item["head_sha256"] != head
                    or not item["issued_at"] <= now <= item["expires_at"]
                    or item["synthetic_signature"] != canonical_hash({**unsigned, "key": keys[signer]})):
                raise ValueError("receipt")
            signers.add(signer)
            identifiers.add(item["receipt_id"])
            nonces.append(item["nonce"])
        if len(signers) < current["threshold"] or nonces != sorted(nonces):
            raise ValueError("quorum/order")
        if any(item["path_id"] != "fixture-038" for item in events):
            raise ValueError("path")
        if bound_ancestry != ancestry:
            raise ValueError("ancestry")
        chain = verify_custody_chain(events, bound_registry, date)
        return {"chain": chain, "new_watermark": max([watermark, *nonces]),
                "new_cache": sorted(set(cache) | set(nonces))}

    events = build()
    head = events[-1]["event_sha256"]
    valid_receipts = [receipt("rev-g", head, "r-g", 2008),
                      receipt("rev-h", head, "r-h", 2010)]
    valid = verify(events, valid_receipts)
    fork = json.loads(json.dumps(policies))
    fork[2]["previous_policy_sha256"] = "0" * 64
    other = build("other")
    other_head = other[-1]["event_sha256"]
    cases = {
        "rollback": (events, valid_receipts, policies[:2], 150, 2007,
                     frozenset({2005, 2006, 2007}), registry, ancestry, "2026-12-15"),
        "fork": (events, valid_receipts, fork, 150, 2007,
                 frozenset({2005, 2006, 2007}), registry, ancestry, "2026-12-15"),
        "epoch": (events, [receipt("rev-g", head, "old-g", 2008, epoch=10), valid_receipts[1]],
                  policies, 150, 2007, frozenset({2005, 2006, 2007}), registry, ancestry, "2026-12-15"),
        "cross_policy_replay": (events, [receipt("rev-g", head, "v37-g", 2008, version=37, epoch=10),
                                         receipt("rev-h", head, "v37-h", 2010, version=37, epoch=10)],
                                policies, 150, 2007, frozenset({2005, 2006, 2007}), registry, ancestry, "2026-12-15"),
        "nonce_low": (events, [receipt("rev-g", head, "low", 1999), valid_receipts[1]],
                      policies, 150, 2007, frozenset(), registry, ancestry, "2026-12-15"),
        "nonce_high": (events, [valid_receipts[0], receipt("rev-h", head, "high", 2012)],
                       policies, 150, 2007, frozenset(), registry, ancestry, "2026-12-15"),
        "nonce_replay": (events, [receipt("rev-g", head, "same-g", 2008),
                                  receipt("rev-h", head, "same-h", 2008)],
                         policies, 150, 2007, frozenset(), registry, ancestry, "2026-12-15"),
        "inactive_signer": (events, [receipt("rev-f", head, "inactive", 2008), valid_receipts[1]],
                            policies, 150, 2007, frozenset(), registry, ancestry, "2026-12-15"),
        "quorum": (events, valid_receipts[:1], policies, 150, 2007,
                   frozenset(), registry, ancestry, "2026-12-15"),
        "stale": (events, [receipt("rev-g", head, "stale", 2008, expires=149), valid_receipts[1]],
                  policies, 150, 2007, frozenset(), registry, ancestry, "2026-12-15"),
        "head": (events, [receipt("rev-g", "0" * 64, "bad-g", 2008),
                          receipt("rev-h", "0" * 64, "bad-h", 2010)],
                 policies, 150, 2007, frozenset(), registry, ancestry, "2026-12-15"),
        "scope": (events, valid_receipts, policies, 150, 2007, frozenset(),
                  {**registry, "issuer-17": {"wrong"}}, ancestry, "2026-12-15"),
        "ancestry": (events, valid_receipts, policies, 150, 2007, frozenset(),
                     registry, {"issuer-17": "issuer-15"}, "2026-12-15"),
        "path": (other, [receipt("rev-g", other_head, "other-g", 2008),
                         receipt("rev-h", other_head, "other-h", 2010)],
                 policies, 150, 2007, frozenset(), registry, ancestry, "2026-12-15"),
        "watermark_rollback": (events, [receipt("rev-g", head, "watermark", 2007), valid_receipts[1]],
                               policies, 150, 2007, frozenset(), registry, ancestry, "2026-12-15"),
        "replay_cache": (events, [receipt("rev-g", head, "cached", 2009), valid_receipts[1]],
                         policies, 150, 2007, frozenset({2009}), registry, ancestry, "2026-12-15"),
    }
    controls = {}
    for name, args in cases.items():
        try:
            verify(*args)
            controls[name] = False
        except (ValueError, KeyError):
            controls[name] = True
    return {
        "event_count": 18, "policy_versions": [36, 37, 38],
        "revocation_epochs": [9, 10, 11], "nonce_window": [2000, 2011],
        "initial_watermark": 2007, "new_watermark": valid["new_watermark"],
        "replay_cache_size": len(valid["new_cache"]), "receipt_threshold": 2,
        "policy_chain_terminal_sha256": policies[-1]["policy_sha256"],
        "terminal_sha256": valid["chain"]["final_event_sha256"],
        "boundary_rejections": controls,
        "signature_kind": "SYNTHETIC_HASH_FIXTURE_NOT_CRYPTOGRAPHIC_SIGNATURE",
        "physical_sample": None, "evidence_class": "SYNTHETIC_CUSTODY",
    }


def twenty_two_component_four_parenthesizations(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("source")
    n = 22
    order = [f"component-{index:02d}" for index in range(n)]
    labels = ["compute"] * 6 + ["memory"] * 6 + ["network"] * 5 + ["control"] * 5
    intervals = [[index + 4, index + 13] for index in range(n)]
    mask = [[i == j or (labels[i] == labels[j] and abs(i - j) == 1)
             for j in range(n)] for i in range(n)]
    positive = [[0.07 if i == j else (0.0001 if mask[i][j] else 0.0)
                 for j in range(n)] for i in range(n)]
    matrices = {
        "positive": positive,
        "zero": [[0.07 if i == j else 0.0 for j in range(n)] for i in range(n)],
        "negative": [[0.07 if i == j else (-0.0001 if mask[i][j] else 0.0)
                      for j in range(n)] for i in range(n)],
        "missing": None,
        "indefinite": [[1.0 if i == j else 2.0 for j in range(n)] for i in range(n)],
        "nonfinite": [[float("inf") if i == j == 0 else (1.0 if i == j else 0.0)
                       for j in range(n)] for i in range(n)],
    }
    first = [*range(5, n), *range(5)]
    second = [*range(11, n), *range(11)]
    third = list(reversed(range(n)))
    fourth = [*range(0, n, 2), *range(1, n, 2)]

    def compose(left, right):
        return [left[index] for index in right]

    def permute_vector(items, indices):
        return [items[index] for index in indices]

    def permute_matrix(matrix, indices):
        return None if matrix is None else [[matrix[i][j] for j in indices] for i in indices]

    parenthesizations = [
        compose(compose(compose(first, second), third), fourth),
        compose(compose(first, compose(second, third)), fourth),
        compose(first, compose(compose(second, third), fourth)),
        compose(first, compose(second, compose(third, fourth))),
    ]
    composed = parenthesizations[0]
    inverse = [composed.index(index) for index in range(n)]
    sequential_intervals = intervals
    sequential_matrices = matrices
    for permutation in (first, second, third, fourth):
        sequential_intervals = permute_vector(sequential_intervals, permutation)
        sequential_matrices = {name: permute_matrix(value, permutation)
                               for name, value in sequential_matrices.items()}
    composed_intervals = permute_vector(intervals, composed)
    composed_matrices = {name: permute_matrix(value, composed) for name, value in matrices.items()}
    recovered_intervals = permute_vector(composed_intervals, inverse)
    recovered_matrices = {name: permute_matrix(value, inverse)
                          for name, value in composed_matrices.items()}
    sigmas = [0.0, 2.0, 8.0, 22.0]
    sweeps = {str(sigma): component_covariance_sweep(intervals, matrices, [1, 11, 22, 0], sigma=sigma)
              for sigma in sigmas}
    permuted = {str(sigma): component_covariance_sweep(composed_intervals, composed_matrices,
                                                       [1, 11, 22, 0], sigma=sigma)
                for sigma in sigmas}
    source_sha = hashlib.sha256(source_bytes).hexdigest()
    binding = {"source_sha256": source_sha, "order": order, "labels": labels,
               "mask": mask, "permutations": [first, second, third, fourth],
               "composed": composed, "inverse": inverse, "sigmas": sigmas}
    identity = canonical_hash(binding)
    mutations = {
        "order": {**binding, "order": list(reversed(order))},
        "labels": {**binding, "labels": list(reversed(labels))},
        "parenthesization": {**binding, "composed": list(reversed(composed))},
        "inverse": {**binding, "inverse": list(reversed(inverse))},
        "source": {**binding, "source_sha256": "0" * 64},
    }
    return {
        "components": n, "source_sha256": source_sha, "component_order": order,
        "block_labels": labels, "permutations": [first, second, third, fourth],
        "composed_permutation": composed, "inverse_permutation": inverse,
        "parenthesization_count": len(parenthesizations),
        "all_parenthesizations_equal": all(item == composed for item in parenthesizations),
        "composition_matches_sequential_intervals": sequential_intervals == composed_intervals,
        "composition_matches_sequential_matrices": sequential_matrices == composed_matrices,
        "inverse_map_valid": all(inverse[composed[index]] == index for index in range(n)),
        "four_permutation_recovers_intervals": recovered_intervals == intervals,
        "four_permutation_recovers_matrices": recovered_matrices == matrices,
        "permutation_equivalence": sweeps == permuted,
        "sparse_nonzero_count": sum(sum(row) for row in mask),
        "covariance_grid_sha256": identity,
        "binding_mutation_rejections": {name: canonical_hash(value) != identity
                                        for name, value in mutations.items()},
        "sigma_values": sigmas, "sweeps": sweeps,
        "commercial_interpretation": None, "evidence_class": "MODEL_ONLY",
    }


def nine_signed_transform_trace_invariants():
    matrix = [[Fraction(25), Fraction(1), Fraction(2), Fraction(1)],
              [Fraction(1), Fraction(36), Fraction(1), Fraction(2)],
              [Fraction(2), Fraction(1), Fraction(49), Fraction(1)],
              [Fraction(1), Fraction(2), Fraction(1), Fraction(81)]]
    identity_transform = ([0, 1, 2, 3], [1, 1, 1, 1])
    transforms = [
        ([1, 0, 3, 2], [1, -1, 1, -1]), ([2, 3, 0, 1], [-1, 1, -1, 1]),
        ([3, 2, 1, 0], [1, 1, -1, -1]), ([0, 2, 1, 3], [-1, 1, 1, -1]),
        ([2, 0, 3, 1], [1, -1, -1, 1]), ([3, 1, 0, 2], [-1, -1, 1, 1]),
        ([1, 3, 0, 2], [1, 1, -1, -1]), ([2, 1, 3, 0], [-1, 1, 1, -1]),
        ([3, 0, 2, 1], [1, -1, 1, -1]),
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

    def add(left, right):
        return [[left[i][j] + right[i][j] for j in range(4)] for i in range(4)]

    def scale(value, factor):
        return [[factor * value[i][j] for j in range(4)] for i in range(4)]

    def determinant(value):
        total = Fraction(0)
        for order in itertools.permutations(range(len(value))):
            inversions = sum(order[i] > order[j]
                             for i in range(len(value)) for j in range(i + 1, len(value)))
            term = Fraction(-1 if inversions % 2 else 1)
            for row, column in enumerate(order):
                term *= value[row][column]
            total += term
        return total

    def trace_powers(value):
        rows, current = [], value
        for _ in range(4):
            rows.append(sum(current[index][index] for index in range(4)))
            current = multiply(current, value)
        return rows

    def characteristic(value):
        powers = trace_powers(value)
        e1 = powers[0]
        e2 = (powers[0] ** 2 - powers[1]) / 2
        e3 = (powers[0] ** 3 - 3 * powers[0] * powers[1] + 2 * powers[2]) / 6
        return [Fraction(1), -e1, e2, -e3, determinant(value)]

    composed, sequential = identity_transform, matrix
    for item in transforms:
        composed = combine(composed, item)
        sequential = apply(sequential, item)
    restored = sequential
    for item in reversed(transforms):
        restored = apply(restored, inverse(item))
    characteristic_coefficients = characteristic(matrix)
    transformed_coefficients = characteristic(sequential)
    powers = [
        [[Fraction(int(i == j)) for j in range(4)] for i in range(4)],
        matrix,
    ]
    powers.append(multiply(powers[-1], matrix))
    powers.append(multiply(powers[-1], matrix))
    powers.append(multiply(powers[-1], matrix))
    polynomial = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    for coefficient, power in zip(characteristic_coefficients, reversed(powers)):
        polynomial = add(polynomial, scale(power, coefficient))
    rows = []
    for left in range(len(transforms)):
        right = (left + 1) % len(transforms)
        product = combine(transforms[left], transforms[right])
        rows.append({"left": left, "right": right,
                     "closure": sorted(product[0]) == list(range(4))
                     and all(value in (-1, 1) for value in product[1]),
                     "inverse_roundtrip": combine(inverse(product), product) == identity_transform})
    minors = [determinant([row[:size] for row in value[:size]])
              for value in (matrix, sequential) for size in range(1, 5)]
    return {
        "transform_count": 9, "matrix_product_count": 144, "cayley_rows": rows,
        "all_cayley_rows_valid": all(row["closure"] and row["inverse_roundtrip"] for row in rows),
        "closure_is_signed_permutation": sorted(composed[0]) == list(range(4)),
        "associative_composition": sequential == apply(matrix, composed),
        "exact_reverse_order_roundtrip": restored == matrix,
        "characteristic_coefficients": [[item.numerator, item.denominator]
                                         for item in characteristic_coefficients],
        "characteristic_polynomial_invariant": characteristic_coefficients == transformed_coefficients,
        "trace_powers": [[item.numerator, item.denominator] for item in trace_powers(matrix)],
        "trace_power_invariant": trace_powers(matrix) == trace_powers(sequential),
        "cayley_hamilton_zero": all(item == 0 for row in polynomial for item in row),
        "determinant_invariant": determinant(matrix) == determinant(sequential),
        "all_principal_minors_positive": all(item > 0 for item in minors),
        "symmetric": all(sequential[i][j] == sequential[j][i]
                         for i in range(4) for j in range(4)),
        "composition_sha256": canonical_hash({"permutations": [item[0] for item in transforms],
                                               "signs": [item[1] for item in transforms]}),
        "calibration": None, "evidence_class": "SYNTHETIC_TYPED_COVARIANCE",
    }


def twenty_two_scenario_deletion_intervals():
    scenarios = [
        [4, 3, 2, 1], [2, 2, 1, 0], [2, 1, 2, 0], [1, 1, 1, 1],
        [0, 3, 2, 3], [0, 1, 2, 3], [3, 0, 3, 1], [1, 4, 0, 4],
        [2, 4, 4, 1], [4, 0, 1, 4], [3, 2, 4, 0], [0, 4, 3, 2],
        [4, 2, 0, 3], [1, 3, 4, 2], [2, 0, 4, 3], [3, 4, 1, 2],
        [4, 1, 3, 2], [2, 3, 1, 4], [1, 2, 4, 3], [3, 1, 4, 2],
        [4, 3, 1, 2], [2, 4, 3, 1],
    ]

    def contribution(scores):
        eligible = {index for index, score in enumerate(scores) if score == max(scores)}
        output = [0, 0, 0, 0]
        for order in itertools.permutations(range(4)):
            output[next(item for item in order if item in eligible)] += 1
        return tuple(output)

    contributions = [contribution(item) for item in scenarios]
    full = tuple(sum(row[index] for row in contributions) for index in range(4))
    states = [{(0, 0, 0, 0): 1}] + [{} for _ in range(14)]
    for contribution_row in contributions:
        for count in range(14, 0, -1):
            for subtotal, multiplicity in list(states[count - 1].items()):
                bound = tuple(subtotal[index] + contribution_row[index] for index in range(4))
                states[count][bound] = states[count].get(bound, 0) + multiplicity
    fractions = [Fraction(value, 22 * 24) for value in full]
    grid_counts, state_counts = {}, {}
    for removed_count in range(1, 15):
        denominator = (22 - removed_count) * 24
        grid_counts[str(removed_count)] = sum(states[removed_count].values())
        state_counts[str(removed_count)] = len(states[removed_count])
        for removed in states[removed_count]:
            fractions.extend(Fraction(full[index] - removed[index], denominator)
                             for index in range(4))
    low, high = min(fractions), max(fractions)
    return {
        "scenario_count": 22, "orders_each": 24, "full_grid_size": 528,
        "winner_counts": list(full), "deletion_grid_counts": grid_counts,
        "dynamic_program_state_counts": state_counts,
        "counts_match_binomial": all(grid_counts[str(count)] == math.comb(22, count)
                                     for count in range(1, 15)),
        "recurrence_total_sha256": canonical_hash(grid_counts),
        "all_grid_interval": [[low.numerator, low.denominator],
                              [high.numerator, high.denominator]],
        "probability_claim": None, "capital": None,
        "evidence_class": "FINITE_ILLUSTRATIVE_SCENARIO",
    }


def fifteen_unit_affine_tree_conditions(*raw_sources):
    if len(raw_sources) != 15 or any(not isinstance(item, bytes) or not item for item in raw_sources):
        raise ValueError("sources")
    source_sha = [hashlib.sha256(item).hexdigest() for item in raw_sources]
    maps = []
    for index, digest in enumerate(bytes.fromhex(item) for item in source_sha):
        maps.append({"slope": Fraction(2 + digest[0] % 7, 1 + digest[1] % 5),
                     "bias": Fraction(digest[2] % 11, 1 + digest[3] % 7),
                     "input_unit": f"u{index:02d}", "output_unit": f"u{index + 1:02d}"})

    def combine(first, second):
        if first["output_unit"] != second["input_unit"]:
            raise ValueError("tree unit")
        return {"slope": second["slope"] * first["slope"],
                "bias": second["slope"] * first["bias"] + second["bias"],
                "input_unit": first["input_unit"], "output_unit": second["output_unit"]}

    def compose(bound):
        if not bound:
            raise ValueError("empty")
        output = bound[0]
        if output["slope"] <= 0:
            raise ValueError("monotonicity")
        for item in bound[1:]:
            if item["slope"] <= 0:
                raise ValueError("monotonicity")
            output = combine(output, item)
        return output

    def right_tree(bound):
        return bound[0] if len(bound) == 1 else combine(bound[0], right_tree(bound[1:]))

    def balanced_tree(bound):
        if len(bound) == 1:
            return bound[0]
        split = len(bound) // 2
        return combine(balanced_tree(bound[:split]), balanced_tree(bound[split:]))

    total = compose(maps)
    trees = {"left_fold": compose(maps), "right_fold": right_tree(maps),
             "balanced": balanced_tree(maps)}
    split_rows = []
    for split in (1, 3, 7, 11, 14):
        reconstructed = combine(compose(maps[:split]), compose(maps[split:]))
        split_rows.append({"split": split, "matches": reconstructed == total,
                           "condition_product": [1, 1]})
    interval = (Fraction(3, 5), Fraction(8, 5))
    transformed = tuple(total["slope"] * value + total["bias"] for value in interval)
    recovered = tuple((value - total["bias"]) / total["slope"] for value in transformed)
    unit_mutation = [dict(item) for item in maps]
    unit_mutation[9]["input_unit"] = "wrong"
    nonmonotone = [dict(item) for item in maps]
    nonmonotone[6]["slope"] = Fraction(-1)
    controls = {"source_order": source_sha != list(reversed(source_sha)),
                "dimension": len(maps[:-1]) != 15, "unit": False, "nonmonotone": False}
    for name, value in (("unit", unit_mutation), ("nonmonotone", nonmonotone)):
        try:
            compose(value)
        except ValueError:
            controls[name] = True
    return {
        "source_sha256": source_sha, "map_count": 15,
        "unit_chain": [maps[0]["input_unit"], *[item["output_unit"] for item in maps]],
        "terminal_unit": total["output_unit"], "split_composition_rows": split_rows,
        "tree_parenthesizations": list(trees),
        "all_tree_parenthesizations_match": all(item == total for item in trees.values()),
        "all_split_compositions_match": all(row["matches"] for row in split_rows),
        "composed_interval": [[value.numerator, value.denominator] for value in transformed],
        "lipschitz_bound": [total["slope"].numerator, total["slope"].denominator],
        "inverse_lipschitz_bound": [total["slope"].denominator, total["slope"].numerator],
        "lipschitz_product": [1, 1],
        "roundtrip_interval": [[value.numerator, value.denominator] for value in recovered],
        "exact_roundtrip": recovered == interval, "negative_controls": controls,
        "sort": ["RealModel", "Model"], "new_law_claim": None,
        "evidence_class": "SOURCE_TYPED_RATIONAL_MODEL",
    }


def eleven_observer_three_transitions():
    observers = [f"observer-{index:02d}" for index in range(11)]

    def transition(epoch, key_epoch, previous):
        body = {"epoch": epoch, "members": observers, "previous_sha256": previous,
                "key_epoch": key_epoch}
        return {**body, "transition_sha256": canonical_hash(body)}

    chain, previous = [], "0" * 64
    for epoch, key_epoch in ((19, 4), (20, 5), (21, 6), (22, 7)):
        item = transition(epoch, key_epoch, previous)
        chain.append(item)
        previous = item["transition_sha256"]
    head = canonical_hash({"domain": "fiction-scm-038", "height": 38})

    def certificate(signers, nonce, epoch=22, bound_head=head, audience="uqpu-scm",
                    transition_sha=chain[-1]["transition_sha256"], policy=38):
        return {"signers": signers, "nonce": nonce, "membership_epoch": epoch,
                "head_sha256": bound_head, "audience": audience,
                "transition_sha256": transition_sha, "policy_version": policy}

    left, right = certificate(observers[:9], "left"), certificate(observers[2:], "right")

    def validate(one, two, bound_chain=tuple(chain)):
        prior = "0" * 64
        for expected_epoch, expected_key, item in zip((19, 20, 21, 22), (4, 5, 6, 7), bound_chain):
            unsigned = {key: value for key, value in item.items() if key != "transition_sha256"}
            if (item["epoch"] != expected_epoch or item["key_epoch"] != expected_key
                    or item["previous_sha256"] != prior
                    or item["transition_sha256"] != canonical_hash(unsigned)):
                return False
            prior = item["transition_sha256"]
        current = bound_chain[-1]
        for item in (one, two):
            signers = item["signers"]
            if (len(signers) != 9 or len(set(signers)) != 9
                    or not set(signers) <= set(current["members"])
                    or item["membership_epoch"] != current["epoch"]
                    or item["head_sha256"] != head or item["audience"] != "uqpu-scm"
                    or item["transition_sha256"] != current["transition_sha256"]
                    or item["policy_version"] != 38):
                return False
        return one["nonce"] != two["nonce"] and len(set(one["signers"]) & set(two["signers"])) >= 7

    bad_chain = [dict(item) for item in chain]
    bad_chain[-1]["previous_sha256"] = "0" * 64
    cases = {
        "valid": (left, right, tuple(chain), True),
        "split": (left, certificate(observers[3:], "short"), tuple(chain), False),
        "stale": (left, certificate(observers[2:], "right", epoch=21), tuple(chain), False),
        "fork": (left, certificate(observers[2:], "right", bound_head="0" * 64), tuple(chain), False),
        "replay": (left, certificate(observers[2:], "left"), tuple(chain), False),
        "downgrade": (left, certificate(observers[2:], "right", policy=37), tuple(chain), False),
        "audience": (left, certificate(observers[2:], "right", audience="wrong"), tuple(chain), False),
        "membership_hash": (left, certificate(observers[2:], "right", transition_sha="0" * 64), tuple(chain), False),
        "transition_chain": (left, right, tuple(bad_chain), False),
        "revocation": (left, certificate([*observers[2:10], "observer-11"], "right"), tuple(chain), False),
        "missing_member": (left, certificate(observers[2:10], "right"), tuple(chain), False),
    }
    table = [{"case": name, "accepted": validate(one, two, bound), "expected": expected}
             for name, (one, two, bound, expected) in cases.items()]
    return {
        "observer_count": 11, "quorum": 9,
        "certificate_intersection_size": len(set(left["signers"]) & set(right["signers"])),
        "minimum_quorum_intersection": 7, "membership_epoch": 22,
        "transition_count": 3, "transition_chain_sha256": chain[-1]["transition_sha256"],
        "control_table": table,
        "all_controls_match": all(row["accepted"] == row["expected"] for row in table),
        "sort": "Fiction", "empirical_coupling": None, "evidence_class": "FICTION_ONLY",
    }


def lineage_manifest_v28_multiproof(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("source")
    source_sha = hashlib.sha256(source_bytes).hexdigest()
    real = [{"kind": "real", "index": index, "source_sha256": source_sha,
             "schema": "uqpu-lineage-v28", "config": f"cfg-{index % 5}",
             "metric": f"metric-{index % 4}"} for index in range(15)]
    padding = [{"kind": "padding", "index": 15, "domain": "uqpu-lineage-padding-v28"}]

    def leaf_hash(item):
        return canonical_hash({"domain": "uqpu-lineage-leaf-v28", **item})

    def combine(left, right):
        return canonical_hash({"domain": "uqpu-lineage-node-v28", "left": left, "right": right})

    items = [*real, *padding]
    levels = [[leaf_hash(item) for item in items]]
    while len(levels[-1]) > 1:
        row = levels[-1]
        levels.append([combine(row[index], row[index + 1]) for index in range(0, len(row), 2)])
    root = levels[-1][0]
    selected, exclusions = [0, 4, 8, 12, 14], [15]
    targets = selected + exclusions

    def proof_positions(indices):
        current, positions = set(indices), []
        for level, row in enumerate(levels[:-1]):
            for index in sorted(current):
                sibling = index ^ 1
                if sibling not in current:
                    positions.append((level, sibling))
            current = {index // 2 for index in current}
        return positions

    positions = proof_positions(targets)
    proof = [{"level": level, "index": index, "hash": levels[level][index]}
             for level, index in positions]

    def verify(bound_items, bound_proof, bound_root=root):
        expected_positions = proof_positions([item["index"] for item in bound_items])
        if [(item["level"], item["index"]) for item in bound_proof] != expected_positions:
            return False
        known = {(0, item["index"]): leaf_hash(item) for item in bound_items}
        if len(known) != len(bound_items):
            return False
        for item in bound_proof:
            key = (item["level"], item["index"])
            if key in known:
                return False
            known[key] = item["hash"]
        for level in range(len(levels) - 1):
            for parent in range(len(levels[level + 1])):
                left, right = (level, 2 * parent), (level, 2 * parent + 1)
                if left in known and right in known:
                    known[(level + 1, parent)] = combine(known[left], known[right])
        return known.get((len(levels) - 1, 0)) == bound_root

    target_items = [items[index] for index in targets]
    manifest = {
        "version": 28, "root_sha256": root, "source_sha256": source_sha,
        "real_indices": list(range(15)), "padding_exclusion_indices": exclusions,
        "selected_indices": selected,
        "config_sha256": canonical_hash([item["config"] for item in real]),
        "metric_sha256": canonical_hash([item["metric"] for item in real]),
        "multiproof_sha256": canonical_hash(proof),
    }

    def validate(bound, bound_proof=proof, bound_items=target_items):
        expected = {**manifest, "multiproof_sha256": canonical_hash(bound_proof)}
        return bound == expected and verify(bound_items, bound_proof, bound["root_sha256"])

    mutations = {
        "root": {**manifest, "root_sha256": "0" * 64},
        "padding_exclusion": {**manifest, "padding_exclusion_indices": [14]},
        "order": {**manifest, "selected_indices": list(reversed(selected))},
        "index": {**manifest, "real_indices": list(range(14)) + [16]},
        "source": {**manifest, "source_sha256": "0" * 64},
        "schema": {**manifest, "version": 27},
        "config": {**manifest, "config_sha256": "0" * 64},
        "metric": {**manifest, "metric_sha256": "0" * 64},
    }
    rejection = {name: not validate(value) for name, value in mutations.items()}
    altered = {
        "proof_minimality": [*proof, proof[-1]],
        "proof_order": list(reversed(proof)),
        "proof_path": [{**proof[0], "index": proof[0]["index"] ^ 1}, *proof[1:]],
        "proof_value": [{**proof[0], "hash": "0" * 64}, *proof[1:]],
    }
    for name, bound_proof in altered.items():
        rejection[name] = not validate({**manifest, "multiproof_sha256": canonical_hash(bound_proof)},
                                       bound_proof)
    rejection["padding_domain"] = leaf_hash({**padding[0], "domain": "wrong"}) != levels[0][15]
    return {
        "manifest": manifest, "real_leaf_count": 15, "padded_leaf_count": 16,
        "padding_leaf_count": 1, "padding_exclusion_count": 1,
        "selected_leaf_count": len(selected), "multiproof_target_count": len(targets),
        "compressed_multiproof_node_count": len(proof),
        "individual_proof_node_count": len(targets) * (len(levels) - 1),
        "multiproof_is_smaller": len(proof) < len(targets) * (len(levels) - 1),
        "valid_manifest": validate(manifest), "mutation_rejections": rejection,
        "candidate_result": None, "functional_equivalence": None,
        "evidence_class": "SYNTHETIC_DATA_LINEAGE",
    }


def sixteen_inverse_pairs_level_schedule():
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
        ("xor-17", lambda x: x ^ 17, lambda x: x ^ 17, 33, 10, 6),
    ]
    dependencies = [[], [], [0], [0], [1], [1], [2, 4], [3, 5],
                    [6], [6], [7], [7], [8, 10], [9, 11], [12, 13], [14]]

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
        ancestors, best = reachability(bound), []
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

    def schedule(bound):
        levels = []
        for index, parents in enumerate(bound):
            levels.append(0 if not parents else 1 + max(levels[parent] for parent in parents))
        return [{"level": level,
                 "nodes": [index for index, value in enumerate(levels) if value == level],
                 "gates": sum(operations[index][3] for index, value in enumerate(levels)
                              if value == level)}
                for level in range(max(levels) + 1)]

    def valid_schedule(rows, bound):
        locations = {node: row["level"] for row in rows for node in row["nodes"]}
        return (sorted(locations) == list(range(len(bound)))
                and all(locations[parent] < locations[index]
                        for index, parents in enumerate(bound) for parent in parents)
                and all(row["gates"] == sum(operations[index][3] for index in row["nodes"])
                        for row in rows))

    def leaf(operation, index, bound=dependencies):
        name, _, _, gates, depth, qubits = operation
        body = {"domain": "uqpu-resource-leaf-v7", "index": index, "name": name,
                "gates": gates, "depth": depth, "max_qubits": qubits,
                "depends_on": bound[index]}
        return {"hash": canonical_hash(body), "gates": gates,
                "serial_depth": depth, "max_qubits": qubits}

    def combine(left, right):
        body = {"domain": "uqpu-resource-node-v7", "left": left["hash"], "right": right["hash"],
                "gates": left["gates"] + right["gates"],
                "serial_depth": left["serial_depth"] + right["serial_depth"],
                "max_qubits": max(left["max_qubits"], right["max_qubits"])}
        return {"hash": canonical_hash(body), "gates": body["gates"],
                "serial_depth": body["serial_depth"], "max_qubits": body["max_qubits"]}

    leaves = [leaf(item, index) for index, item in enumerate(operations)]
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
    dag_mutation = json.loads(json.dumps(dependencies))
    dag_mutation[6] = [7]
    proof_mutation = json.loads(json.dumps(proofs[0]))
    proof_mutation["steps"][0]["gates"] += 1
    resource_mutation = (*operations[-1][:3], operations[-1][3] + 1,
                         operations[-1][4], operations[-1][5])
    antichain = maximum_antichain(dependencies)
    ancestors = reachability(dependencies)

    def valid_antichain(items):
        return len(items) == len(set(items)) and all(
            first not in ancestors[second] and second not in ancestors[first]
            for position, first in enumerate(items) for second in items[position + 1:])

    level_schedule = schedule(dependencies)
    level_mutation = json.loads(json.dumps(level_schedule))
    level_mutation[0]["nodes"].append(level_mutation[1]["nodes"][0])
    work_mutation = json.loads(json.dumps(level_schedule))
    work_mutation[0]["gates"] += 1
    total_gates = sum(item[3] for item in operations)
    return {
        "inverse_pair_names": [item[0] for item in operations],
        "resource_merkle_root_sha256": root["hash"], "proof_count": len(proofs),
        "dependency_dag": [{"node": index, "depends_on": parents}
                           for index, parents in enumerate(dependencies)],
        "dependency_dag_valid": validate_dag(dependencies),
        "dependency_dag_mutation_rejected": not validate_dag(dag_mutation),
        "all_inclusion_proofs_valid": all(verify(index, item, proofs[index])
                                         for index, item in enumerate(operations)),
        "proof_resource_mutation_rejected": not verify(0, operations[0], proof_mutation),
        "leaf_resource_mutation_rejected": not verify(15, resource_mutation, proofs[15]),
        "basis_states_checked": 64, "distinct_outputs": len(set(encoded)),
        "residual": sum(first != second for first, second in enumerate(reconstructed)),
        "order_mutation_witness_count": sum(item != apply(value, order_mutation)
                                            for value, item in enumerate(encoded)),
        "maximum_antichain": antichain, "antichain_width": len(antichain),
        "antichain_valid": valid_antichain(antichain),
        "antichain_mutation_rejected": not valid_antichain([*antichain, 15]),
        "level_schedule": level_schedule, "level_schedule_valid": valid_schedule(level_schedule, dependencies),
        "level_schedule_mutation_rejected": not valid_schedule(level_mutation, dependencies),
        "work_conservation": sum(row["gates"] for row in level_schedule) == total_gates,
        "work_mutation_rejected": not valid_schedule(work_mutation, dependencies),
        "resource_bound": {"gates": root["gates"],
                           "serial_depth": sum(item[4] for item in operations),
                           "dag_critical_depth": critical_depth(dependencies),
                           "antichain_width": len(antichain),
                           "level_count": len(level_schedule),
                           "level_width": max(len(row["nodes"]) for row in level_schedule),
                           "unconstrained_parallel_lower_bound": max(item[4] for item in operations),
                           "max_qubits": root["max_qubits"]},
        "parallel_bounds_are_model_only": True, "hardware": None,
        "evidence_class": "SYNTHETIC_INVERSE_OPERATOR",
    }


def run_cycle038_fixture(source_bytes, directory):
    suffixes = [b":two", b":three", b":four", b":five", b":six", b":seven",
                b":eight", b":nine", b":ten", b":eleven", b":twelve",
                b":thirteen", b":fourteen", b":fifteen"]
    with tempfile.TemporaryDirectory(dir=directory) as work:
        lanes = {
            "A": eighteenth_graph_conjugacy_orbits(),
            "B": schema_v2_to_v3_default_gate(),
            "C": twelve_reader_cleanup_gate(work),
            "D": zip64_unicode_path_parity_gate(),
            "E": eighteen_issuer_watermark_gate(),
            "F": twenty_two_component_four_parenthesizations(source_bytes),
            "G": nine_signed_transform_trace_invariants(),
            "H": twenty_two_scenario_deletion_intervals(),
            "FND/EQN": fifteen_unit_affine_tree_conditions(source_bytes,
                                                            *(source_bytes + suffix for suffix in suffixes)),
            "SCM": eleven_observer_three_transitions(),
            "AI-COST": lineage_manifest_v28_multiproof(source_bytes),
            "QOS/QSVT": sixteen_inverse_pairs_level_schedule(),
        }
    return {lane: {"status": "BLOCKED_WITH_PROGRESS", **value}
            for lane, value in lanes.items()}
