from uqpu.scm_replication_manifest import *

def rec(site,h="a"*64):
    return ReplicationRecord(site,"op","hw","cal","v1",h,"b"*64)

def test_two_sites_validate():
    assert validate_replication([rec("A"),rec("B")])==()

def test_duplicate_site_rejected():
    assert any("duplicate_site" in x for x in validate_replication([rec("A"),rec("A")]))

def test_bad_hash_rejected():
    assert any("invalid_sha256" in x for x in validate_replication([rec("A","bad")]))
