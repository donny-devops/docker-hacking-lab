## Summary

- What changed, and why.
- Link related issues (for example, `Closes #7`).

## Security considerations

- Lab remains isolated (bind to localhost; no production secrets).
- Insecure services stay labeled and documented.
- Hardening overlay / detection scripts stay defensive.

## How to run and clean up

```bash
python3 -m pip install -r requirements-dev.txt
make test
docker compose up -d   # isolated host only
docker compose down -v
```

## Checklist

- [ ] `make test` passes
- [ ] Course catalog still has all 11 modules and 22 assessments
- [ ] No real credentials committed
