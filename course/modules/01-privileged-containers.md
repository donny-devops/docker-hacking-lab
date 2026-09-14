# Privileged Containers

`--privileged` is a single flag that disables Docker's main isolation controls. The container then has host-equivalent capabilities, devices, and kernel interfaces.

## Attack scenario

An operator adds `--privileged` so a debugging tool can see extra `/dev` nodes. Any later compromise of that workload can reconfigure the host kernel, mount host disks, and persist outside the container.

## Noncompliant

```bash
docker run --rm --privileged ubuntu:20.04 sleep infinity
```

Equivalent lab service: `escape-target-privileged` in `docker-compose.yml`.

## Compliant

```bash
docker run --rm --cap-drop ALL --security-opt no-new-privileges:true \
  --read-only --user 65534:65534 ubuntu:20.04 sleep infinity
```

Equivalent lab service: `escape-target-privileged` in `docker-compose.hardened.yml`.

## Remediation

- Do not use `--privileged` in application workloads.
- Grant only the specific capabilities the process needs.
- Keep seccomp, AppArmor/SELinux, and `no-new-privileges` enabled.
- Block privileged pods/containers with an admission policy in orchestration.
- Detect drift: `docker inspect --format '{{.HostConfig.Privileged}}' <id>`

## Hands-on lab

1. Start the insecure baseline and inspect `escape-target-privileged`.
2. Compare `CapBnd`, seccomp mode, and `/dev` with `defender-hardened`.
3. Switch to `docker-compose.hardened.yml` and confirm `Privileged=false`.
4. Run `python3 solutions/detect_misconfigurations.py docker-compose.yml --expect-findings`.
