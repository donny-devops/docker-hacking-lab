import json
import subprocess
import sys
from pathlib import Path

import pytest

from conftest import ATTACKER_TOOLS, ROOT, SOLUTIONS

EXPECTED_SCRIPTS = {
    "enumerate.sh",
    "inspect_internals.sh",
    "escape_socket.sh",
    "escape_hostmount.sh",
    "exploit_tcp_daemon.sh",
    "registry_attack.sh",
    "supply_chain.sh",
    "arp_spoof.sh",
    "pivot_network.sh",
    "runtime_defense.sh",
}


@pytest.mark.scripts
def test_attacker_tool_filenames_stable():
    names = {p.name for p in ATTACKER_TOOLS.glob("*.sh")}
    assert names == EXPECTED_SCRIPTS


@pytest.mark.scripts
@pytest.mark.parametrize("script", sorted(EXPECTED_SCRIPTS))
def test_attacker_scripts_parse(script):
    path = ATTACKER_TOOLS / script
    completed = subprocess.run(
        ["bash", "-n", str(path)],
        check=False,
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 0, completed.stderr


@pytest.mark.scripts
@pytest.mark.parametrize("script", sorted(EXPECTED_SCRIPTS))
def test_attacker_scripts_are_defensive(script):
    text = (ATTACKER_TOOLS / script).read_text(encoding="utf-8")
    lowered = text.lower()
    assert "isolated lab only" in lowered
    assert '{"Image"' not in text
    assert "/host/etc/shadow" not in text
    assert "arpspoof" not in lowered
    assert "C:\\Users\\" not in text
    assert "reverse shell" not in lowered


@pytest.mark.scripts
def test_detector_reports_insecure_and_clears_hardened():
    detector = SOLUTIONS / "detect_misconfigurations.py"
    insecure = subprocess.run(
        [sys.executable, str(detector), str(ROOT / "docker-compose.yml"), "--expect-findings"],
        check=False,
        capture_output=True,
        text=True,
    )
    hardened = subprocess.run(
        [sys.executable, str(detector), str(ROOT / "docker-compose.hardened.yml")],
        check=False,
        capture_output=True,
        text=True,
    )
    assert insecure.returncode == 0, insecure.stderr
    assert hardened.returncode == 0, hardened.stdout + hardened.stderr


@pytest.mark.scripts
def test_seccomp_profile_is_allow_list():
    profile = json.loads((SOLUTIONS / "seccomp-restricted.json").read_text(encoding="utf-8"))
    assert profile["defaultAction"] == "SCMP_ACT_ERRNO"
    names: list[str] = []
    for entry in profile["syscalls"]:
        names.extend(entry["names"])
        assert entry["action"] == "SCMP_ACT_ALLOW"
    blocked_examples = {"mount", "bpf", "reboot", "kexec_load", "ptrace"}
    assert blocked_examples.isdisjoint(names)
    assert "read" in names
    assert "write" in names


@pytest.mark.scripts
def test_lab_landing_page_exists():
    html = Path(__file__).resolve().parents[1] / "lab" / "www" / "index.html"
    php = Path(__file__).resolve().parents[1] / "lab" / "www" / "index.php"
    for path in (html, php):
        text = path.read_text(encoding="utf-8")
        assert "Isolated lab only" in text
        assert "docker compose" in text.lower()
