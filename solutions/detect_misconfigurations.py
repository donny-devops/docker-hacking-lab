#!/usr/bin/env python3
"""Detect teaching misconfigurations in lab Compose files.

Educational use only. Reports privileged mode, host-root mounts, Docker socket
bind-mounts, published daemon-like ports, and example secrets. Does not exploit
or mutate running systems.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

FINDING_SOCKET = "docker-socket-mount"
FINDING_PRIVILEGED = "privileged"
FINDING_HOST_ROOT = "host-root-mount"
FINDING_EXAMPLE_SECRET = "example-secret-in-env"
FINDING_PUBLISHED_PORT = "published-port"

EXAMPLE_SECRET_MARKERS = (
    "AKIAIOSFODNN7EXAMPLE",
    "SuperSecret123!",
    "password123",
)


def load_compose(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} is not a mapping")
    return data


def _volume_strings(service: dict) -> list[str]:
    volumes = service.get("volumes") or []
    out: list[str] = []
    for item in volumes:
        if isinstance(item, str):
            out.append(item)
        elif isinstance(item, dict):
            source = item.get("source") or item.get("host") or ""
            target = item.get("target") or item.get("container") or ""
            out.append(f"{source}:{target}")
    return out


def inspect_service(name: str, service: dict) -> list[dict]:
    findings: list[dict] = []
    volumes = _volume_strings(service)

    if any("/var/run/docker.sock" in vol for vol in volumes):
        findings.append(
            {
                "service": name,
                "id": FINDING_SOCKET,
                "severity": "high",
                "message": "Docker Unix socket is bind-mounted into the container.",
                "remediation": "Remove the socket mount; use a least-privilege API proxy if Docker access is required.",
            }
        )

    if any(vol.startswith("/:") or vol.startswith("/:/") for vol in volumes):
        findings.append(
            {
                "service": name,
                "id": FINDING_HOST_ROOT,
                "severity": "high",
                "message": "Host root filesystem is mounted into the container.",
                "remediation": "Mount only the specific path required, read-only when possible.",
            }
        )

    if service.get("privileged") is True:
        findings.append(
            {
                "service": name,
                "id": FINDING_PRIVILEGED,
                "severity": "high",
                "message": "Service runs with privileged=true.",
                "remediation": "Set privileged=false, drop capabilities, and keep seccomp/AppArmor enabled.",
            }
        )

    env = service.get("environment") or {}
    if isinstance(env, list):
        env_values = env
    elif isinstance(env, dict):
        env_values = [f"{k}={v}" for k, v in env.items()]
    else:
        env_values = []
    for value in env_values:
        if any(marker in str(value) for marker in EXAMPLE_SECRET_MARKERS):
            findings.append(
                {
                    "service": name,
                    "id": FINDING_EXAMPLE_SECRET,
                    "severity": "medium",
                    "message": "Environment contains a documented lab/example secret.",
                    "remediation": "Use a secret manager or tmpfs-backed files; never use production credentials.",
                }
            )
            break

    for mapping in service.get("ports") or []:
        text = str(mapping)
        if "2375" in text or "0.0.0.0:" in text:
            findings.append(
                {
                    "service": name,
                    "id": FINDING_PUBLISHED_PORT,
                    "severity": "high",
                    "message": f"Published port mapping may be overly broad: {text}",
                    "remediation": "Bind to 127.0.0.1 or a private management network; require TLS client auth for Docker APIs.",
                }
            )

    return findings


def inspect_compose(path: Path) -> list[dict]:
    data = load_compose(path)
    services = data.get("services") or {}
    findings: list[dict] = []
    for name, service in services.items():
        if isinstance(service, dict):
            findings.extend(inspect_service(name, service))
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "compose_file",
        nargs="?",
        default="docker-compose.yml",
        type=Path,
    )
    parser.add_argument("--json", action="store_true", help="Print findings as JSON")
    parser.add_argument(
        "--expect-findings",
        action="store_true",
        help="Exit 0 when the insecure lab baseline still contains teaching findings",
    )
    args = parser.parse_args(argv)

    findings = inspect_compose(args.compose_file)
    if args.json:
        print(json.dumps(findings, indent=2))
    else:
        if not findings:
            print(f"{args.compose_file}: no teaching misconfigurations reported")
        for item in findings:
            print(f"[{item['severity']}] {item['service']}: {item['id']} — {item['message']}")

    if args.expect_findings:
        required = {FINDING_SOCKET, FINDING_PRIVILEGED, FINDING_HOST_ROOT}
        present = {item["id"] for item in findings}
        missing = required - present
        if missing:
            print(f"expected teaching findings missing: {sorted(missing)}", file=sys.stderr)
            return 1
        return 0

    return 0 if not findings else 1


if __name__ == "__main__":
    raise SystemExit(main())
