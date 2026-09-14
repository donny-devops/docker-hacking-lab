# Docker Hacking Lab
### Hands-on Docker Hacking Course
**Author: Adonis Jimenez | BizDevStudio**

> Warning: This lab contains intentional vulnerabilities. Run in an isolated environment only. Published ports bind to `127.0.0.1` by default (`LAB_BIND_ADDRESS`).

## Quick Start

```bash
git clone https://github.com/donny-devops/docker-hacking-lab
cd docker-hacking-lab
cp .env.example .env
python3 -m pip install -r requirements-dev.txt
make test
docker compose up -d
```

Open http://127.0.0.1:8080 for the lab landing page.

The insecure and hardened files share `container_name` values, host ports, and subnets. Tear the first stack down before starting the other:

```bash
docker compose down -v
docker compose -f docker-compose.hardened.yml up -d
```

Tear down the hardened project (it uses `name: docker-hacking-lab-hardened`):

```bash
docker compose -f docker-compose.hardened.yml down -v
```

Hardened topology removes privileged mode, the Docker socket mount, and the host-root bind. The registry is unpublished on the host but stays unauthenticated for peers on `lab-internal`.

## Course modules

Catalog files live in `course/modules/` (11 modules) with 22 assessments in `course/quizzes/`.

| # | Topic | Lab focus |
|---|--------|-----------|
| 01 | Privileged Containers | `escape-target-privileged` |
| 02 | Exposed Container APIs | `vuln-web` socket mount |
| 03 | Container Escape | compare insecure vs hardened |
| 04 | Container Image Tampering | unauthenticated `registry` |
| 05 | Insecure Configuration | `defender-hardened` baseline |
| 06 | Denial-of-Service | cgroup limits |
| 07 | Kernel Vulnerabilities | shared kernel patching |
| 08 | Shared Kernel Exploitation | namespaces, `lab-internal` |
| 09 | Insecure Container Orchestration | PSA mapping |
| 10 | Insecure Container Images | floating tags |
| 11 | Seccomp, AppArmor, SELinux | `solutions/seccomp-restricted.json` |

Hands-on compose modules from the original lab map onto the same stack (setup, internals, enumeration, privileged, host-mount, socket, TCP daemon, registry, supply chain, network, runtime defense). Detection helpers are in `attacker-tools/`; static analysis is `solutions/detect_misconfigurations.py`.

## Agents

Cursor agents in this repo can use **granola-engineer** to ground work in Granola meeting decisions. Open the project in Cursor (workspace `.cursor/` files load automatically), or copy `.cursor/plugins/granola-engineer` to `~/.cursor/plugins/local/granola-engineer`. Sign-in is browser OAuth; no API keys belong in git. See `AGENTS.md`.

## Checks

CI runs `bash lab/validate.sh` (pytest + `bash -n`). Keep that job green before merge.
