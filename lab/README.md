# Lab operations

Run this environment on an isolated host only. Published ports bind to `127.0.0.1`.

## Start (insecure teaching baseline)

```bash
cp .env.example .env
docker compose up -d
```

## Hardened overlay (defensive solution)

```bash
docker compose -f docker-compose.yml -f docker-compose.hardened.yml up -d
```

## Validate without starting containers

```bash
python3 -m pip install -r requirements-dev.txt
make test
```

## Clean up

```bash
docker compose down -v
```
