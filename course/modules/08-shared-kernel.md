# Shared Kernel Exploitation

Namespaces are the isolation primitive. Sharing the host PID, network, or IPC namespace exposes host and neighbor state.

## Attack scenario

`--pid=host` lets a container see every process. Environment files under `/proc/<pid>/environ` then leak secrets from other workloads and from host agents.

## Noncompliant

```bash
docker run --pid=host --cap-add SYS_ADMIN alpine
```

## Compliant

```bash
docker run --user 65534:65534 --pid container --cap-drop ALL alpine
```

## Remediation

- Keep PID, mount, IPC, UTS, and network namespaces container-scoped.
- Avoid `--network=host` except for tightly controlled infra.
- Enable `kernel.dmesg_restrict` and restrict `/proc` where possible.

## Hands-on lab

1. Confirm lab services do not set `pid: host` in Compose.
2. From a container, list `/proc/self/ns` and compare inode numbers conceptually with the host.
3. Use `inspect_internals.sh` to record namespace and seccomp state.
4. Note that `internal: true` on `lab-internal` reduces accidental east-west internet egress.
