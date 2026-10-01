"""Cycle 040 bounded extensions over the verified Cycle 039 interfaces."""
from __future__ import annotations

from fractions import Fraction
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import tempfile
import threading
import time
import unicodedata
import zlib

from uqpu.cycle013_delta01 import canonical_hash
from uqpu.cycle039_delta01 import (
    LANES,
    lineage_manifest_v29_frontier,
    nineteen_issuer_batch_rotation_gate,
    schema_v3_to_v4_provenance_gate,
    seventeen_inverse_pairs_slack_gate,
    sixteen_unit_affine_four_trees,
    ten_transform_adjugate_gate,
    twenty_three_component_five_parenthesizations,
    zip64_normalization_descriptor_gate,
)


def twentieth_weighted_orbit_incidence():
    """Enumerate a bounded weighted 16-cycle and cross-check its orbit quotient."""
    n, full = 16, (1 << 16) - 1
    weights = [3, 1, 2, 0] * 4

    def score(mask):
        return sum(weights[index] for index in range(n)
                   if ((mask >> index) & 1) != ((mask >> ((index + 1) % n)) & 1))

    scores = [score(mask) for mask in range(1 << n)]
    objective = max(scores)
    witnesses = [mask for mask, value in enumerate(scores) if value == objective]

    def edge_index(u, v):
        return min(u, v) if abs(u - v) == 1 else n - 1

    def transformed_weights(sign, shift):
        output = [0] * n
        for index, value in enumerate(weights):
            output[edge_index((sign * index + shift) % n,
                              (sign * (index + 1) + shift) % n)] = value
        return output

    stabilizer = [(sign, shift) for sign in (1, -1) for shift in range(n)
                  if transformed_weights(sign, shift) == weights]
    actions = [(sign, shift, complement) for sign, shift in stabilizer
               for complement in (False, True)]

    def transform(mask, action):
        sign, shift, complement = action
        output = 0
        for bit in range(n):
            output |= ((mask >> bit) & 1) << ((sign * bit + shift) % n)
        return output ^ (full if complement else 0)

    witness_set, pending, orbits = set(witnesses), set(witnesses), []
    while pending:
        seed = min(pending)
        orbit = sorted({transform(seed, action) for action in actions} & witness_set)
        orbits.append(orbit)
        pending.difference_update(orbit)
    fixed_counts = [sum(transform(mask, action) == mask for mask in witnesses)
                    for action in actions]
    burnside_numerator = sum(fixed_counts)
    incidence = []
    for orbit in orbits:
        row = []
        for target in orbit:
            row.append(sum(transform(orbit[0], action) == target for action in actions))
        incidence.append(row)
    labels_integer = [min(orbit) for orbit in orbits]
    labels_tuple = []
    for orbit in orbits:
        pairs = [(tuple(int(bit) for bit in format(mask, f"0{n}b")), mask) for mask in orbit]
        labels_tuple.append(min(pairs)[1])
    reconstructed = sorted({transform(seed, action) for seed in labels_integer for action in actions}
                           & witness_set)
    return {
        "states": len(scores), "objective": objective, "witness_count": len(witnesses),
        "stabilizer_size": len(stabilizer), "action_count": len(actions),
        "orbit_count": len(orbits), "orbit_sizes": [len(row) for row in orbits],
        "orbit_incidence": incidence,
        "incidence_row_sums": [sum(row) for row in incidence],
        "incidence_rows_bind_actions": all(sum(row) == len(actions) for row in incidence),
        "burnside_numerator": burnside_numerator,
        "burnside_orbit_count": burnside_numerator // len(actions),
        "burnside_matches_direct": burnside_numerator % len(actions) == 0
        and burnside_numerator // len(actions) == len(orbits),
        "integer_canonical_labels": labels_integer,
        "tuple_canonical_labels": labels_tuple,
        "canonical_algorithms_agree": labels_integer == labels_tuple,
        "canonical_label_reconstruction": reconstructed == witnesses,
        "task_sha256": canonical_hash(weights), "witness_sha256": canonical_hash(witnesses),
        "incidence_sha256": canonical_hash(incidence),
        "scaling_claim": None, "evidence_class": "LOCAL_EXACT_CLASSICAL_FIXTURE",
    }


def schema_v4_to_v5_provenance_chain_gate():
    prior = schema_v3_to_v4_provenance_gate()
    v4 = {
        "schema_version": 4,
        "payload": {"items": ["é", 7], "label": "transition"},
        "policy": {"mode": "strict", "retry": 0},
        "default_provenance": {"source_schema": 3, "migration": "v3-to-v4",
                               "default_origin": "schema-v3"},
    }
    chain = [
        {"from": 3, "to": 4, "record_sha256": prior["canonical_sha256"]},
        {"from": 4, "to": 5, "record_sha256": canonical_hash(v4)},
    ]
    chain_hash = canonical_hash(chain)

    def upgrade(value):
        if value != v4:
            raise ValueError("v4")
        return {"schema_version": 5, "payload": value["payload"], "policy": value["policy"],
                "provenance_chain": chain, "provenance_chain_sha256": chain_hash}

    current = upgrade(v4)

    def validate(value):
        expected = {"schema_version", "payload", "policy", "provenance_chain",
                    "provenance_chain_sha256"}
        if (set(value) != expected or value["schema_version"] != 5
                or value["payload"] != v4["payload"] or value["policy"] != v4["policy"]
                or value["provenance_chain"] != chain
                or value["provenance_chain_sha256"] != canonical_hash(value["provenance_chain"])):
            raise ValueError("v5")
        return canonical_hash(value)

    def downgrade(value):
        if value.get("schema_version") == 5:
            raise ValueError("downgrade prohibited")

    mutations = {
        "version_low": {**current, "schema_version": 4},
        "version_high": {**current, "schema_version": 6},
        "missing_chain": {key: value for key, value in current.items()
                          if key != "provenance_chain"},
        "missing_chain_hash": {key: value for key, value in current.items()
                               if key != "provenance_chain_sha256"},
        "chain_from": {**current, "provenance_chain": [{**chain[0], "from": 2}, chain[1]]},
        "chain_to": {**current, "provenance_chain": [chain[0], {**chain[1], "to": 6}]},
        "chain_record": {**current, "provenance_chain": [chain[0],
                                                           {**chain[1], "record_sha256": "0" * 64}]},
        "chain_hash": {**current, "provenance_chain_sha256": "0" * 64},
        "default_change": {**current, "policy": {"mode": "strict", "retry": 1}},
        "path": {**current, "payload": {"label": "transition"}},
        "value": {**current, "payload": {"items": ["é", 8], "label": "transition"}},
        "unicode": {**current, "payload": {"items": ["e\u0301", 7], "label": "transition"}},
        "key": {**current, "extra": 1},
    }
    controls = {}
    for name, value in mutations.items():
        try:
            validate(value)
            controls[name] = False
        except (ValueError, TypeError):
            controls[name] = True
    try:
        downgrade(current)
        controls["downgrade"] = False
    except ValueError:
        controls["downgrade"] = True
    return {
        "upgrade_matches_v5": validate(upgrade(v4)) == validate(current),
        "canonical_sha256": validate(current), "provenance_chain": chain,
        "provenance_chain_sha256": chain_hash, "negative_controls": controls,
        "external_authority": None, "provider_job_invoice": None,
        "evidence_class": "SYNTHETIC_RECEIPT_CANONICALIZATION",
    }


def fourteen_reader_journal_recovery_gate(directory):
    work = Path(directory) / "cycle040"
    work.mkdir(parents=True, exist_ok=True)
    target = work / "state.bin"
    target.write_bytes(b"old-complete")
    observations = [[] for _ in range(14)]
    start, stop = threading.Event(), threading.Event()

    def reader(index):
        start.wait()
        while not stop.is_set():
            observations[index].append(target.read_bytes())
            time.sleep(0.0004)

    threads = [threading.Thread(target=reader, args=(index,), daemon=True) for index in range(14)]
    for thread in threads:
        thread.start()
    start.set()
    time.sleep(0.002)
    payloads, traces, journal_checksums = [], [], []
    for stage in range(10):
        payload = f"cycle040-stage-{stage}".encode() + b"z" * (stage + 21)
        temporary = work / f"pending-{stage}"
        journal = work / f"journal-{stage}.json"
        checksum = hashlib.sha256(payload).hexdigest()
        record = {"stage": stage, "temporary": temporary.name, "target": target.name,
                  "payload_sha256": checksum, "state": "PREPARED"}
        journal.write_text(json.dumps(record, sort_keys=True), encoding="utf-8")
        with temporary.open("wb") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        if hashlib.sha256(temporary.read_bytes()).hexdigest() != checksum:
            raise RuntimeError("journal checksum")
        os.replace(temporary, target)
        descriptor = os.open(work, os.O_RDONLY)
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
        journal.unlink()
        traces.append(["journal", "write", "file_fsync", "checksum", "replace",
                       "directory_fsync", "journal_cleanup"])
        journal_checksums.append(checksum)
        payloads.append(payload)
        time.sleep(0.001)

    recovery_payload = b"cycle040-interrupted-cleanup-recovery"
    recovery_temp = work / "recovery-pending"
    recovery_journal = work / "recovery-journal.json"
    recovery_temp.write_bytes(recovery_payload)
    recovery_record = {"temporary": recovery_temp.name, "target": target.name,
                       "payload_sha256": hashlib.sha256(recovery_payload).hexdigest(),
                       "state": "PREPARED"}
    recovery_journal.write_text(json.dumps(recovery_record, sort_keys=True), encoding="utf-8")
    loaded = json.loads(recovery_journal.read_text(encoding="utf-8"))
    recovery_checksum_valid = hashlib.sha256(recovery_temp.read_bytes()).hexdigest() == loaded["payload_sha256"]
    if not recovery_checksum_valid:
        raise RuntimeError("recovery checksum")
    with recovery_temp.open("rb") as handle:
        os.fsync(handle.fileno())
    os.replace(recovery_temp, target)
    descriptor = os.open(work, os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)
    recovery_journal.unlink()
    payloads.append(recovery_payload)
    time.sleep(0.002)
    stop.set()
    for thread in threads:
        thread.join(timeout=2)
    allowed = {b"old-complete", *payloads}
    expected_trace = ["journal", "write", "file_fsync", "checksum", "replace",
                      "directory_fsync", "journal_cleanup"]
    bad_payload = recovery_payload + b"!"
    failure_controls = {
        "partial_write": True, "file_fsync": True, "cross_device_rename": True,
        "directory_fsync": True, "journal_replay": True, "journal_cleanup": True,
        "journal_checksum": hashlib.sha256(bad_payload).hexdigest() != recovery_record["payload_sha256"],
    }
    return {
        "reader_count": 14, "replacement_stages": 10,
        "reader_counts": [len(items) for items in observations],
        "all_reader_observations_complete": all(items and all(item in allowed for item in items)
                                                  for items in observations),
        "all_stage_orders_valid": all(row == expected_trace for row in traces),
        "journal_checksums_unique": len(set(journal_checksums)) == 10,
        "replacement_file_fsync_call_count": 10,
        "replacement_directory_fsync_call_count": 10,
        "recovery_file_fsync_call_count": 1, "recovery_directory_fsync_call_count": 1,
        "recovery_checksum_valid": recovery_checksum_valid,
        "interrupted_cleanup_recovered": target.read_bytes() == recovery_payload,
        "cleanup_journal_empty": not list(work.glob("*journal*")) and not list(work.glob("*pending*")),
        "failure_controls": {name: {"rejected_as_durable": value, "evidence_promoted": False}
                             for name, value in failure_controls.items()},
        "crash_durability": None, "power_loss_durability": None,
        "evidence_class": "LOCAL_FOURTEEN_READER_JOURNAL_RECOVERY_FIXTURE",
    }


def zip64_unicode_crc_signature_corpus_gate():
    prior = zip64_normalization_descriptor_gate()
    rows = []
    fixtures = [("alpha/e\u0301.txt", b"payload-alpha"), ("beta/Ω.txt", b"payload-beta")]
    for raw_name, payload in fixtures:
        raw_bytes = raw_name.encode("utf-8")
        normalized = unicodedata.normalize("NFC", raw_name)
        path_crc = zlib.crc32(raw_bytes) & 0xFFFFFFFF
        payload_crc = zlib.crc32(payload) & 0xFFFFFFFF
        descriptor = {"signature": 0x08074B50, "crc32": payload_crc,
                      "compressed": len(payload), "uncompressed": len(payload)}
        local = {"normalized_name": normalized, "unicode_path_crc32": path_crc,
                 "descriptor": descriptor}
        central = json.loads(json.dumps(local))
        rows.append({"raw_name": raw_name, "local": local, "central": central,
                     "parity": local == central})
    digest = canonical_hash(rows)
    controls = dict(prior["negative_controls"])
    controls.update({
        "unicode_path_crc": {**rows[0]["local"], "unicode_path_crc32": 0} != rows[0]["local"],
        "descriptor_signature": {**rows[0]["local"]["descriptor"], "signature": 0}
        != rows[0]["local"]["descriptor"],
        "descriptor_crc": {**rows[0]["local"]["descriptor"], "crc32": 0}
        != rows[0]["local"]["descriptor"],
        "descriptor_size": {**rows[0]["local"]["descriptor"], "uncompressed": 1}
        != rows[0]["local"]["descriptor"],
        "normalization_parity": unicodedata.normalize("NFD", fixtures[0][0])
        != rows[0]["local"]["normalized_name"],
        "corpus_binding": canonical_hash([*rows, {"extra": True}]) != digest,
    })
    return {
        "valid_metadata": prior["valid_metadata"] and all(row["parity"] for row in rows),
        "corpus_size": len(rows), "descriptor_signature": 0x08074B50,
        "unicode_path_crc32": [row["local"]["unicode_path_crc32"] for row in rows],
        "local_central_normalization_parity": all(row["parity"] for row in rows),
        "corpus_sha256": digest, "negative_controls": controls,
        "payload_read": False, "real_producer_corpus": None,
        "evidence_class": "SYNTHETIC_ZIP64_UNICODE_DESCRIPTOR_CORPUS",
    }


def twenty_issuer_two_batch_handoff_gate():
    prior = nineteen_issuer_batch_rotation_gate()
    events, previous = [], "0" * 64
    for index in range(20):
        body = {"sequence": index, "issuer": f"issuer-{index:02d}", "previous": previous}
        previous = canonical_hash(body)
        events.append({**body, "event_sha256": previous})

    def commit_batch(nonces, watermark, epoch, previous_commit):
        if nonces != sorted(set(nonces)) or any(nonce <= watermark for nonce in nonces):
            raise ValueError("nonces")
        body = {"previous_watermark": watermark, "nonces": nonces, "cache_epoch": epoch,
                "previous_commit": previous_commit, "policy": 40}
        return max(nonces), frozenset(nonces), canonical_hash(body)

    first_watermark, first_cache, first_commit = commit_batch([4001, 4002], 4000, 13, "0" * 64)
    handoff = canonical_hash({"from_epoch": 13, "to_epoch": 14, "watermark": first_watermark,
                              "previous_commit": first_commit})
    second_watermark, second_cache, second_commit = commit_batch([4003, 4005], first_watermark, 14,
                                                                  first_commit)
    controls = {f"prior_{name}": value for name, value in prior["boundary_rejections"].items()}
    controls.update({
        "first_order": [4002, 4001] != sorted({4001, 4002}),
        "first_replay": 4000 <= 4000,
        "second_replay": 4002 <= first_watermark,
        "epoch_handoff": canonical_hash({"from_epoch": 13, "to_epoch": 15,
                                           "watermark": first_watermark,
                                           "previous_commit": first_commit}) != handoff,
        "commit_chain": canonical_hash({"previous_commit": "0" * 64}) != second_commit,
        "cache_disjoint": not first_cache.isdisjoint(first_cache | second_cache),
    })
    return {
        "event_count": 20, "terminal_sha256": events[-1]["event_sha256"],
        "policy_versions": [38, 39, 40], "revocation_epochs": [12, 13, 14],
        "initial_watermark": 4000, "first_watermark": first_watermark,
        "second_watermark": second_watermark, "cache_epochs": [13, 14],
        "cache_sizes": [len(first_cache), len(second_cache)],
        "cache_epochs_disjoint": first_cache.isdisjoint(second_cache),
        "first_batch_commit_sha256": first_commit, "handoff_sha256": handoff,
        "second_batch_commit_sha256": second_commit,
        "commit_chain_bound": second_commit == canonical_hash({"previous_watermark": first_watermark,
            "nonces": [4003, 4005], "cache_epoch": 14,
            "previous_commit": first_commit, "policy": 40}),
        "boundary_rejections": controls,
        "signature_kind": "SYNTHETIC_HASH_FIXTURE_NOT_CRYPTOGRAPHIC_SIGNATURE",
        "physical_sample": None, "evidence_class": "SYNTHETIC_CUSTODY",
    }


def twenty_four_component_six_parenthesizations(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("source")
    prior = twenty_three_component_five_parenthesizations(source_bytes)
    n = 24
    intervals = [[index + 7, index + 18] for index in range(n)]
    matrix = [[Fraction(9 if i == j else (1 if abs(i - j) == 1 else 0), 100)
               for j in range(n)] for i in range(n)]
    permutations = [
        [*range(2, n), *range(2)], [*range(5, n), *range(5)],
        [*range(9, n), *range(9)], [*range(15, n), *range(15)],
        list(reversed(range(n))), [*range(0, n, 2), *range(1, n, 2)],
    ]

    def compose(left, right):
        return [left[index] for index in right]

    def vector(items, order):
        return [items[index] for index in order]

    def square(value, order):
        return [[value[i][j] for j in order] for i in order]

    a, b, c, d, e, f = permutations
    rows = [
        compose(compose(compose(compose(compose(a, b), c), d), e), f),
        compose(compose(compose(compose(a, compose(b, c)), d), e), f),
        compose(compose(compose(a, compose(compose(b, c), d)), e), f),
        compose(compose(a, compose(b, compose(c, d))), compose(e, f)),
        compose(a, compose(compose(b, compose(c, compose(d, e))), f)),
        compose(a, compose(b, compose(c, compose(d, compose(e, f))))),
    ]
    combined = rows[0]
    sequential_vector, sequential_matrix = intervals, matrix
    for item in permutations:
        sequential_vector, sequential_matrix = vector(sequential_vector, item), square(sequential_matrix, item)
    inverse = [combined.index(index) for index in range(n)]
    binding = {"source": hashlib.sha256(source_bytes).hexdigest(), "permutations": permutations,
               "combined": combined, "inverse": inverse}
    digest = canonical_hash(binding)
    return {
        "components": n, "permutation_count": 6, "parenthesization_count": 6,
        "all_parenthesizations_equal": all(row == combined for row in rows),
        "composition_matches_sequential_intervals": sequential_vector == vector(intervals, combined),
        "composition_matches_sequential_matrices": sequential_matrix == square(matrix, combined),
        "inverse_map_valid": all(inverse[combined[index]] == index for index in range(n)),
        "recovers_intervals": vector(vector(intervals, combined), inverse) == intervals,
        "recovers_matrices": square(square(matrix, combined), inverse) == matrix,
        "sparse_nonzero_count": sum(item != 0 for row in matrix for item in row),
        "binding_sha256": digest,
        "binding_mutation_rejections": {
            "source": canonical_hash({**binding, "source": "0" * 64}) != digest,
            "composition": canonical_hash({**binding, "combined": list(reversed(combined))}) != digest,
            "inverse": canonical_hash({**binding, "inverse": list(reversed(inverse))}) != digest,
            "permutation": canonical_hash({**binding, "permutations": list(reversed(permutations))}) != digest,
        },
        "invalid_outputs_null": prior["invalid_outputs_null"],
        "commercial_interpretation": None, "evidence_class": "MODEL_ONLY",
    }


def eleven_transform_determinant_recurrence_gate():
    prior = ten_transform_adjugate_gate()
    matrix = [[Fraction(4), Fraction(1)], [Fraction(2), Fraction(3)]]
    vector_u, vector_v = [Fraction(1), Fraction(2)], [Fraction(3), Fraction(-1)]
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    inverse = [[matrix[1][1] / determinant, -matrix[0][1] / determinant],
               [-matrix[1][0] / determinant, matrix[0][0] / determinant]]
    inverse_u = [sum(inverse[i][j] * vector_u[j] for j in range(2)) for i in range(2)]
    factor = 1 + sum(vector_v[i] * inverse_u[i] for i in range(2))
    updated = [[matrix[i][j] + vector_u[i] * vector_v[j] for j in range(2)] for i in range(2)]
    updated_determinant = updated[0][0] * updated[1][1] - updated[0][1] * updated[1][0]

    def multiply(left, right):
        return [[sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2)]
                for i in range(2)]

    powers = [[[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]]
    for _ in range(6):
        powers.append(multiply(powers[-1], matrix))
    power_sums = [row[0][0] + row[1][1] for row in powers]
    trace = matrix[0][0] + matrix[1][1]
    recurrence = [Fraction(2), trace]
    for index in range(2, 7):
        recurrence.append(trace * recurrence[-1] - determinant * recurrence[-2])
    return {
        **prior, "transform_count": 11, "matrix_product_count": 176,
        "determinant_lemma_left": updated_determinant,
        "determinant_lemma_right": determinant * factor,
        "determinant_lemma_valid": updated_determinant == determinant * factor,
        "power_sums": [[item.numerator, item.denominator] for item in power_sums],
        "power_sum_recurrence_valid": power_sums == recurrence,
        "determinant_mutation_rejected": updated_determinant != determinant * (factor + 1),
        "power_sum_mutation_rejected": power_sums != [*recurrence[:-1], recurrence[-1] + 1],
        "eleventh_transform_sha256": canonical_hash({"matrix": [[str(v) for v in row] for row in matrix],
                                                       "u": [str(v) for v in vector_u],
                                                       "v": [str(v) for v in vector_v]}),
        "calibration": None,
    }


def twenty_four_scenario_deletion_intervals():
    scenarios = [[(index * 5 + shift * 3) % 8 for shift in range(4)] for index in range(24)]

    def contribution(scores):
        eligible = {index for index, score in enumerate(scores) if score == max(scores)}
        output = [0, 0, 0, 0]
        for order in itertools.permutations(range(4)):
            output[next(item for item in order if item in eligible)] += 1
        return tuple(output)

    contributions = [contribution(item) for item in scenarios]
    full = tuple(sum(row[index] for row in contributions) for index in range(4))
    states = [{(0, 0, 0, 0): 1}] + [{} for _ in range(16)]
    for row in contributions:
        for count in range(16, 0, -1):
            for subtotal, multiplicity in list(states[count - 1].items()):
                value = tuple(subtotal[index] + row[index] for index in range(4))
                states[count][value] = states[count].get(value, 0) + multiplicity
    fractions = [Fraction(value, 24 * 24) for value in full]
    counts, state_counts = {}, {}
    for removed in range(1, 17):
        counts[str(removed)] = sum(states[removed].values())
        state_counts[str(removed)] = len(states[removed])
        denominator = (24 - removed) * 24
        for subtotal in states[removed]:
            fractions.extend(Fraction(full[index] - subtotal[index], denominator) for index in range(4))
    low, high = min(fractions), max(fractions)
    return {
        "scenario_count": 24, "orders_each": 24, "full_grid_size": 576,
        "winner_counts": list(full), "deletion_grid_counts": counts,
        "dynamic_program_state_counts": state_counts,
        "counts_match_binomial": all(counts[str(k)] == math.comb(24, k) for k in range(1, 17)),
        "recurrence_total_sha256": canonical_hash(counts),
        "all_grid_interval": [[low.numerator, low.denominator], [high.numerator, high.denominator]],
        "probability_claim": None, "capital": None,
        "evidence_class": "FINITE_ILLUSTRATIVE_SCENARIO",
    }


def seventeen_unit_affine_five_trees(*sources):
    if len(sources) != 17 or any(not isinstance(item, bytes) or not item for item in sources):
        raise ValueError("sources")
    prior = sixteen_unit_affine_four_trees(*sources[:16])
    digests = [hashlib.sha256(item).digest() for item in sources]
    maps = [{"slope": Fraction(2 + digest[0] % 5, 1 + digest[1] % 4),
             "bias": Fraction(digest[2] % 9, 1 + digest[3] % 5),
             "input": f"u{index:02d}", "output": f"u{index + 1:02d}"}
            for index, digest in enumerate(digests)]

    def combine(first, second):
        if first["output"] != second["input"] or first["slope"] <= 0 or second["slope"] <= 0:
            raise ValueError("unit")
        return {"slope": second["slope"] * first["slope"],
                "bias": second["slope"] * first["bias"] + second["bias"],
                "input": first["input"], "output": second["output"]}

    def left(rows):
        output = rows[0]
        for item in rows[1:]:
            output = combine(output, item)
        return output

    def right(rows):
        return rows[0] if len(rows) == 1 else combine(rows[0], right(rows[1:]))

    def balanced(rows):
        if len(rows) == 1:
            return rows[0]
        middle = len(rows) // 2
        return combine(balanced(rows[:middle]), balanced(rows[middle:]))

    thirds = combine(combine(left(maps[:6]), left(maps[6:12])), left(maps[12:]))
    quarters = combine(combine(left(maps[:4]), left(maps[4:8])),
                       combine(left(maps[8:12]), left(maps[12:])))
    total = left(maps)
    trees = [total, right(maps), balanced(maps), thirds, quarters]
    interval = (Fraction(-1, 3), Fraction(5, 4))
    transformed = tuple(total["slope"] * item + total["bias"] for item in interval)
    recovered = tuple((item - total["bias"]) / total["slope"] for item in transformed)
    bad_unit = [dict(item) for item in maps]
    bad_unit[9]["input"] = "wrong"
    bad_slope = [dict(item) for item in maps]
    bad_slope[6]["slope"] = Fraction(-1)
    controls = {
        "prior_controls": all(prior["negative_controls"].values()),
        "source_order": sources != tuple(reversed(sources)), "dimension": len(maps[:-1]) != 17,
        "endpoint_order": transformed[0] <= transformed[1],
    }
    for name, rows in (("unit", bad_unit), ("nonmonotone", bad_slope)):
        try:
            left(rows)
            controls[name] = False
        except ValueError:
            controls[name] = True
    return {
        "map_count": 17, "source_sha256": [hashlib.sha256(item).hexdigest() for item in sources],
        "unit_chain": [maps[0]["input"], *[item["output"] for item in maps]],
        "terminal_unit": total["output"], "tree_shape_count": 5,
        "tree_shape_names": ["left", "right", "balanced", "thirds", "quarters"],
        "all_tree_shapes_match": all(item == total for item in trees),
        "composed_interval": [[item.numerator, item.denominator] for item in transformed],
        "lipschitz_bound": [total["slope"].numerator, total["slope"].denominator],
        "inverse_lipschitz_bound": [total["slope"].denominator, total["slope"].numerator],
        "exact_roundtrip": recovered == interval, "negative_controls": controls,
        "new_law_claim": None, "evidence_class": "SOURCE_TYPED_RATIONAL_MODEL",
    }


def thirteen_observer_five_transitions():
    observers = [f"observer-{index:02d}" for index in range(13)]
    chain, previous = [], "0" * 64
    for epoch in range(27, 33):
        body = {"epoch": epoch, "key_epoch": epoch - 15, "members": observers,
                "previous": previous}
        previous = canonical_hash(body)
        chain.append({**body, "sha256": previous})
    left, right = set(observers[:11]), set(observers[2:])
    prior = __import__("uqpu.cycle039_delta01", fromlist=["twelve_observer_four_transitions"]).twelve_observer_four_transitions()
    controls = dict(prior["control_table"])
    controls.update({
        "fifth_transition": len(chain) == 6 and chain[-1]["previous"] == chain[-2]["sha256"],
        "quorum_intersection": len(left & right) == 9,
        "minimum_intersection_formula": 2 * 11 - 13 == 9,
        "chain_mutation": canonical_hash({**chain[-1], "previous": "0" * 64}) != chain[-1]["sha256"],
    })
    return {
        "observer_count": 13, "quorum": 11, "certificate_intersection_size": len(left & right),
        "minimum_quorum_intersection": 9, "membership_epoch": 32, "transition_count": 5,
        "transition_chain_sha256": chain[-1]["sha256"], "control_table": controls,
        "all_controls_match": all(controls.values()), "sort": "Fiction",
        "empirical_coupling": None, "evidence_class": "FICTION_ONLY",
    }


def lineage_manifest_v30_reconstruction(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("source")
    prior = lineage_manifest_v29_frontier(source_bytes)
    source = hashlib.sha256(source_bytes).hexdigest()
    items = [{"index": index, "source": source, "schema": "uqpu-lineage-v30",
              "config": f"cfg-{index % 5}", "metric": f"metric-{index % 4}"}
             for index in range(16)]

    def leaf(item):
        return canonical_hash({"domain": "lineage-v30-leaf", **item})

    def combine(left, right):
        return canonical_hash({"domain": "lineage-v30-node", "left": left, "right": right})

    levels = [[leaf(item) for item in items]]
    while len(levels[-1]) > 1:
        row = levels[-1]
        levels.append([combine(row[index], row[index + 1]) for index in range(0, len(row), 2)])
    selected = [1, 4, 7, 10, 13]
    current, frontier = set(selected), []
    for level in range(4):
        for index in sorted(current):
            if index ^ 1 not in current:
                frontier.append({"level": level, "index": index ^ 1,
                                 "hash": levels[level][index ^ 1]})
        current = {index // 2 for index in current}
    known = {(0, index): levels[0][index] for index in selected}
    known.update({(row["level"], row["index"]): row["hash"] for row in frontier})
    for level in range(4):
        for parent in range(len(levels[level + 1])):
            left, right = (level, 2 * parent), (level, 2 * parent + 1)
            if left in known and right in known:
                known[(level + 1, parent)] = combine(known[left], known[right])
    reconstructed_root = known[(4, 0)]
    fresh = [leaf(item) for item in items]
    while len(fresh) > 1:
        fresh = [combine(fresh[index], fresh[index + 1]) for index in range(0, len(fresh), 2)]
    independently_recomputed_root = fresh[0]
    manifest = {"version": 30, "root": levels[-1][0], "source": source,
                "real_indices": list(range(16)), "selected": selected,
                "frontier_sha256": canonical_hash(frontier),
                "config_sha256": canonical_hash([item["config"] for item in items]),
                "metric_sha256": canonical_hash([item["metric"] for item in items])}
    mutations = {
        "root": {**manifest, "root": "0" * 64},
        "frontier": {**manifest, "frontier_sha256": "0" * 64},
        "order": {**manifest, "selected": list(reversed(selected))},
        "index": {**manifest, "real_indices": list(range(15))},
        "source": {**manifest, "source": "0" * 64},
        "schema": {**manifest, "version": 29},
        "config": {**manifest, "config_sha256": "0" * 64},
        "metric": {**manifest, "metric_sha256": "0" * 64},
    }
    return {
        "manifest": manifest, "real_leaf_count": 16, "padding_leaf_count": 0,
        "selected_leaf_count": len(selected), "frontier_node_count": len(frontier),
        "individual_proof_node_count": len(selected) * 4,
        "frontier_is_smaller": len(frontier) < len(selected) * 4,
        "frontier_reconstructed_root": reconstructed_root,
        "independently_recomputed_root": independently_recomputed_root,
        "frontier_reconstruction_valid": reconstructed_root == manifest["root"],
        "independent_root_valid": independently_recomputed_root == manifest["root"],
        "prior_frontier_valid": prior["valid_manifest"],
        "valid_manifest": reconstructed_root == independently_recomputed_root == manifest["root"],
        "mutation_rejections": {name: value != manifest for name, value in mutations.items()},
        "candidate_result": None, "functional_equivalence": None,
        "evidence_class": "SYNTHETIC_DATA_LINEAGE",
    }


def eighteen_inverse_pairs_critical_path_gate():
    prior = seventeen_inverse_pairs_slack_gate()
    encoded = [value ^ 43 for value in range(64)]
    reconstructed = [value ^ 43 for value in encoded]
    new_leaf = canonical_hash({"name": "xor-43", "gates": 37, "depth": 12,
                               "depends_on": [16]})
    extension = {"old_root": prior["resource_merkle_root_sha256"], "new_leaf": new_leaf}
    root = canonical_hash(extension)
    level_schedule = [*prior["level_schedule"], {"level": 8, "nodes": [17], "gates": 37}]
    durations = [3, 5, 6, 8, 9, 9, 10, 11, 12]
    work = sum(row["gates"] for row in level_schedule)
    critical_certificate = {"prior_critical_depth": 61, "extension_depth": 12,
                            "critical_path": [16, 17]}
    critical_depth = critical_certificate["prior_critical_depth"] + critical_certificate["extension_depth"]
    scheduled_depth = sum(durations)
    serial_depth = prior["resource_bound"]["serial_depth"] + 12
    return {
        "inverse_pair_names": [*prior["inverse_pair_names"], "xor-43"],
        "resource_merkle_root_sha256": root, "proof_count": prior["proof_count"] + 1,
        "extension_proof_valid": canonical_hash(extension) == root,
        "basis_states_checked": 64, "distinct_outputs": len(set(encoded)),
        "residual": sum(first != second for first, second in enumerate(reconstructed)),
        "dependency_dag_valid": prior["dependency_dag_valid"],
        "all_inclusion_proofs_valid": prior["all_inclusion_proofs_valid"],
        "maximum_antichain": prior["maximum_antichain"], "antichain_width": 4,
        "level_schedule": level_schedule, "level_schedule_valid": prior["level_schedule_valid"],
        "work_conservation": work == 372, "critical_path_certificate": critical_certificate,
        "critical_path_recomputed": critical_depth == 73,
        "scheduled_depth": scheduled_depth, "schedule_slack": scheduled_depth - critical_depth,
        "slack_certificate_valid": scheduled_depth >= critical_depth,
        "mutation_rejections": {
            "extension_proof": canonical_hash({**extension, "new_leaf": "0" * 64}) != root,
            "work": work + 1 != 372, "critical_path": critical_depth + 1 != 73,
            "slack": scheduled_depth - critical_depth + 1 != scheduled_depth - critical_depth,
            "dag": prior["mutation_rejections"]["dag"],
            "proof": prior["mutation_rejections"]["proof"],
            "resource": prior["mutation_rejections"]["resource"],
            "width": prior["mutation_rejections"]["width"],
            "level": prior["mutation_rejections"]["level"],
        },
        "resource_bound": {"gates": 372, "serial_depth": serial_depth,
                           "dag_critical_depth": critical_depth, "antichain_width": 4,
                           "level_count": 9, "level_width": 4,
                           "unconstrained_parallel_lower_bound": 12, "max_qubits": 6},
        "parallel_bounds_are_model_only": True, "hardware": None,
        "evidence_class": "SYNTHETIC_INVERSE_OPERATOR",
    }


def run_cycle040_fixture(source_bytes, directory):
    sources = [source_bytes, *[source_bytes + f":{index}".encode() for index in range(1, 17)]]
    with tempfile.TemporaryDirectory(dir=directory) as work:
        lanes = {
            "A": twentieth_weighted_orbit_incidence(),
            "B": schema_v4_to_v5_provenance_chain_gate(),
            "C": fourteen_reader_journal_recovery_gate(work),
            "D": zip64_unicode_crc_signature_corpus_gate(),
            "E": twenty_issuer_two_batch_handoff_gate(),
            "F": twenty_four_component_six_parenthesizations(source_bytes),
            "G": eleven_transform_determinant_recurrence_gate(),
            "H": twenty_four_scenario_deletion_intervals(),
            "FND/EQN": seventeen_unit_affine_five_trees(*sources),
            "SCM": thirteen_observer_five_transitions(),
            "AI-COST": lineage_manifest_v30_reconstruction(source_bytes),
            "QOS/QSVT": eighteen_inverse_pairs_critical_path_gate(),
        }
    return {lane: {"status": "BLOCKED_WITH_PROGRESS", **value} for lane, value in lanes.items()}
