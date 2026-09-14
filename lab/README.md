# Lab operations

Run this environment on an isolated host only. Published ports bind to `127.0.0.1` unless `LAB_BIND_ADDRESS` is overridden in `.env`.

The insecure and hardened Compose files share container names, ports, and subnets. Stop one stack before starting the other.

## Start (insecure teaching baseline)

```bash
cp .env.example .env
docker compose up -d
```

## Switch to the hardened topology

```bash
docker compose down -v
docker compose -f docker-compose.hardened.yml up -d
```

The hardened file is standalone (do not merge it onto the insecure file). Privileged mode, the Docker socket mount, and the host-root bind are removed. The registry is unpublished on the host but remains unauthenticated for other containers on `lab-internal`.

## Validate without starting containers

```bash
python3 -m pip install -r requirements-dev.txt
make test
```

## Clean up

Default project (`docker-compose.yml`):

```bash
docker compose down -v
```

Hardened project (`name: docker-hacking-lab-hardened`):

```bash
docker compose -f docker-compose.hardened.yml down -v
```
