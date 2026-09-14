# Tests

Offline checks that keep the lab catalog and Compose contracts passing.

```bash
python3 -m pip install -r requirements-dev.txt
python3 -m pytest
```

Suggested extra runners if the lab grows application code:

- Python: `pytest` (already used)
- Node/TS: `vitest` or `jest`
- Rust: `cargo test`
