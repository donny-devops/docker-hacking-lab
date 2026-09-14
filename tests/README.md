# Tests

Offline checks that keep the lab catalog, Compose contracts, and the in-repo granola-engineer plugin passing.

```bash
python3 -m pip install -r requirements-dev.txt
python3 -m pytest
```

Suggested extra runners if the lab grows application code:

- Python: `pytest` (already used)
- Node/TS: `vitest` or `jest`
- Rust: `cargo test`
