# Denial-of-Service (DoS)

Containers share host CPU, memory, PIDs, and I/O. Without cgroup limits, one workload can starve neighbors or the host.

## Attack scenario

A stress process or fork loop in an unlimited container exhausts PIDs or memory. The kubelet/engine and other apps fail.

## Noncompliant

```bash
docker run -d --name stress alpine sh -c 'yes >/dev/null'
```

## Compliant

```bash
docker run -d --name stress --cpus 0.5 --memory 256m --pids-limit 64 alpine \
  sh -c 'yes >/dev/null'
```

## Remediation

- Set `--cpus`, `--memory`, `--pids-limit` (or Kubernetes resources + LimitRange).
- Restart policy `on-failure` with a cap, not unlimited always-restart of a crash-looping bomber.
- Monitor cgroup metrics (cAdvisor/Prometheus).

## Hands-on lab

1. Identify which lab services currently omit memory/PID limits.
2. Propose limits for `vuln-web` and `internal-db` that still allow them to start.
3. Document where those limits would go in Compose (`mem_limit` / `deploy.resources` / `pids_limit`).
4. Confirm `defender-hardened` already uses a read-only rootfs so disk fill-up is constrained.
