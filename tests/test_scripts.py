import importlib.util
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
def test_attacker_scripts_have_no_utf8_bom(script):
    data = (ATTACKER_TOOLS / script).read_bytes()
    assert not data.startswith(b"\xef\xbb\xbf"), script
    assert data.startswith(b"#!/"), script


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
    assert "touch /test" not in lowered


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
    arch_map = profile["archMap"][0]
    assert "subArchitectures" in arch_map
    assert "subArches" not in arch_map


def _load_detector():
    spec = importlib.util.spec_from_file_location(
        "detect_misconfigurations", SOLUTIONS / "detect_misconfigurations.py"
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.mark.scripts
def test_detector_flags_short_and_unspecified_host_ports():
    detect = _load_detector()
    assert any(
        item["id"] == detect.FINDING_PUBLISHED_PORT
        for item in detect.inspect_service("web", {"ports": ["8080:80"]})
    )
    assert any(
        item["id"] == detect.FINDING_PUBLISHED_PORT
        for item in detect.inspect_service("web", {"ports": ["[::]:8080:80"]})
    )
    assert any(
        item["id"] == detect.FINDING_PUBLISHED_PORT
        for item in detect.inspect_service(
            "web", {"ports": [{"target": 80, "published": 8080}]}
        )
    )
    loopback_mappings = [
        ["127.0.0.1:8080:80"],
        ["${LAB_BIND_ADDRESS:-127.0.0.1}:8080:80"],
        [{"target": 80, "published": 8080, "host_ip": "127.0.0.1"}],
        ["[::1]:8080:80"],
    ]
    for ports in loopback_mappings:
        findings = detect.inspect_service("web", {"ports": ports})
        assert not any(item["id"] == detect.FINDING_PUBLISHED_PORT for item in findings), ports


@pytest.mark.scripts
def test_lab_landing_page_exists():
    html = Path(__file__).resolve().parents[1] / "lab" / "www" / "index.html"
    php = Path(__file__).resolve().parents[1] / "lab" / "www" / "index.php"
    for path in (html, php):
        text = path.read_text(encoding="utf-8")
        assert "Isolated lab only" in text
        assert "docker compose" in text.lower()
