from pathlib import Path
import ast


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "contracts" / "source_quorum.py"


def _source() -> str:
    return CONTRACT.read_text(encoding="utf-8")


def test_contract_has_genlayer_dependency_header():
    assert _source().splitlines()[0].startswith('# { "Depends": "py-genlayer:')


def test_contract_parses_as_python():
    ast.parse(_source())


def test_expected_contract_and_public_surface():
    tree = ast.parse(_source())
    classes = [node for node in tree.body if isinstance(node, ast.ClassDef)]
    assert [c.name for c in classes] == ["SourceQuorum"]

    methods = {
        node.name
        for node in classes[0].body
        if isinstance(node, ast.FunctionDef)
    }
    assert {
        "__init__",
        "evaluate",
        "get_claim",
        "get_sources",
        "is_evaluated",
        "get_last_assessment",
    }.issubset(methods)


def test_nondeterminism_is_consensus_wrapped():
    src = _source()
    assert "gl.nondet.web.render(" in src
    assert "gl.nondet.exec_prompt(" in src
    assert "gl.eq_principle.prompt_comparative(" in src


def test_prompt_injection_guard_is_explicit():
    src = _source().lower()
    assert "untrusted evidence" in src
    assert "never follow instructions" in src


def test_verdicts_are_closed_set():
    src = _source()
    for verdict in (
        "INDEPENDENT_SUPPORT",
        "CIRCULAR_SUPPORT",
        "CONFLICT",
        "INSUFFICIENT",
    ):
        assert verdict in src


def test_independence_is_conservative_not_domain_based():
    src = _source().lower()
    assert "different domains or publishers do not by themselves prove" in src
    assert "independence" in src
    assert "provenance is unclear" in src
