from pathlib import Path
import sys

import pytest


CONTRACT = Path("contracts/source_quorum.py")
SDK_VERSION = "v0.2.12"

pytestmark = pytest.mark.skipif(
    sys.platform == "win32",
    reason=(
        "genlayer-test 0.29.2 Direct Mode currently hits a temporary-file "
        "WinError 32 on Windows before contract execution. Run on Linux/CI."
    ),
)


def test_deploy_and_read_initial_state(direct_deploy):
    quorum = direct_deploy(
        CONTRACT,
        "Example claim",
        "https://example.com/a",
        "https://example.com/b",
        sdk_version=SDK_VERSION,
    )

    assert quorum.get_claim() == "Example claim"
    assert quorum.is_evaluated() is False
    assert quorum.get_last_assessment() == ""
    assert "https://example.com/a" in quorum.get_sources()
    assert "https://example.com/b" in quorum.get_sources()


def test_rejects_empty_claim(direct_vm, direct_deploy):
    with direct_vm.expect_revert("claim must not be empty"):
        direct_deploy(
            CONTRACT,
            "",
            "https://example.com/a",
            "https://example.com/b",
            sdk_version=SDK_VERSION,
        )


def test_rejects_non_https_required_source(direct_vm, direct_deploy):
    with direct_vm.expect_revert("source_a and source_b must use https://"):
        direct_deploy(
            CONTRACT,
            "Example claim",
            "http://example.com/a",
            "https://example.com/b",
            "",
            sdk_version=SDK_VERSION,
        )


