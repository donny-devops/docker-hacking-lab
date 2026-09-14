import pytest

from conftest import COMPOSE_HARDENED, COMPOSE_INSECURE, load_yaml


REQUIRED_SERVICES = {
    "attacker",
    "vuln-web",
    "internal-db",
    "registry",
    "escape-target-privileged",
    "escape-target-hostmount",
    "defender-hardened",
}


def _port_bindings(service: dict) -> list:
    return list(service.get("ports") or [])


def _port_text(mapping) -> str:
    if isinstance(mapping, dict):
        return str(mapping.get("host_ip") or "")
    return str(mapping)


@pytest.mark.compose
@pytest.mark.parametrize("path", [COMPOSE_INSECURE, COMPOSE_HARDENED])
def test_compose_parses_and_has_services(path):
    data = load_yaml(path)
    services = data.get("services") or {}
    assert set(services) == REQUIRED_SERVICES
    assert "lab-internal" in (data.get("networks") or {})
    assert (data.get("networks") or {})["lab-internal"].get("internal") is True


@pytest.mark.compose
@pytest.mark.parametrize("path", [COMPOSE_INSECURE, COMPOSE_HARDENED])
def test_published_ports_bind_localhost(path):
    services = load_yaml(path)["services"]
    for name, service in services.items():
        for mapping in _port_bindings(service):
            text = _port_text(mapping)
            assert "127.0.0.1" in text, f"{path.name} {name}: {mapping}"
            assert "0.0.0.0" not in text


@pytest.mark.compose
def test_insecure_baseline_keeps_teaching_findings():
    services = load_yaml(COMPOSE_INSECURE)["services"]
    volumes = " ".join(str(v) for v in services["vuln-web"].get("volumes") or [])
    host_volumes = " ".join(
        str(v) for v in services["escape-target-hostmount"].get("volumes") or []
    )
    assert "/var/run/docker.sock" in volumes
    assert services["escape-target-privileged"].get("privileged") is True
    assert "/:/host" in host_volumes
    assert services["defender-hardened"].get("read_only") is True
    assert "ALL" in (services["defender-hardened"].get("cap_drop") or [])


@pytest.mark.compose
def test_hardened_compose_removes_teaching_findings():
    services = load_yaml(COMPOSE_HARDENED)["services"]
    vuln_volumes = " ".join(str(v) for v in services["vuln-web"].get("volumes") or [])
    host_volumes = " ".join(
        str(v) for v in services["escape-target-hostmount"].get("volumes") or []
    )
    assert "/var/run/docker.sock" not in vuln_volumes
    assert services["escape-target-privileged"].get("privileged") is not True
    assert "/:/host" not in host_volumes
    assert not services["registry"].get("ports")
    assert "ALL" in (services["escape-target-privileged"].get("cap_drop") or [])


@pytest.mark.compose
def test_example_aws_key_is_documentation_placeholder():
    env = load_yaml(COMPOSE_INSECURE)["services"]["vuln-web"]["environment"]
    assert env["AWS_ACCESS_KEY_ID"] == "AKIAIOSFODNN7EXAMPLE"


@pytest.mark.compose
@pytest.mark.parametrize("path", [COMPOSE_INSECURE, COMPOSE_HARDENED])
def test_compose_interpolates_env_and_has_no_utf8_bom(path):
    data = path.read_bytes()
    assert not data.startswith(b"\xef\xbb\xbf"), path.name
    text = path.read_text(encoding="utf-8")
    assert "${LAB_BIND_ADDRESS" in text
    assert "${POSTGRES_USER" in text
    assert "${POSTGRES_PASSWORD" in text
    assert "${POSTGRES_DB" in text
    assert "overlay" not in text.lower()
