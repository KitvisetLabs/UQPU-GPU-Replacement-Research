"""Fail-closed validator for the Cycle 013 typed goal registry."""
REQUIRED_LANES = {"A","B","C","D","E","F","G","H","FND/EQN","SCM","AI-COST","QOS/QSVT"}
REQUIRED_FIELDS = {"goal_id","lane","domain","objective","observable_and_units","acceptance_contract","falsifier","current_evidence_state","evidence_promotion_rule","unknowns","status"}

def validate_registry(data):
    if not isinstance(data, dict) or data.get("schema") != "uqpu-typed-goal-registry-v1" or data.get("cycle") != "013":
        raise ValueError("schema/cycle")
    goals = data.get("goals")
    if not isinstance(goals, list) or len(goals) != 12:
        raise ValueError("goal count")
    if any(not isinstance(g, dict) or not REQUIRED_FIELDS.issubset(g) for g in goals):
        raise ValueError("goal fields")
    lanes = [g["lane"] for g in goals]
    if set(lanes) != REQUIRED_LANES or len(set(lanes)) != len(lanes):
        raise ValueError("lane coverage")
    if any(not isinstance(g["observable_and_units"], str) or not g["observable_and_units"].strip() for g in goals):
        raise ValueError("observable/units")
    if any(not isinstance(g["falsifier"], str) or not g["falsifier"].strip() for g in goals):
        raise ValueError("falsifier")
    if any(g["status"] != "DEFINED_NOT_PASSED" for g in goals):
        raise ValueError("unsupported promotion state")
    scm = next(g for g in goals if g["lane"] == "SCM")
    if "FICTION_ONLY" not in scm["current_evidence_state"] or "empirical" not in scm["falsifier"].lower():
        raise ValueError("SCM evidence firewall")
    if data.get("evidence_nonclaim") is None:
        raise ValueError("evidence nonclaim")
    return {"goal_count": len(goals), "lane_count": len(set(lanes)), "status": "VALID_DEFINITION_ONLY"}
