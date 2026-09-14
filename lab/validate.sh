#!/usr/bin/env bash
# Offline lab validation: course catalog, compose YAML, and script syntax.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

scripts_only=0
if [[ "${1:-}" == "--scripts-only" ]]; then
  scripts_only=1
fi

fail() {
  echo "FAIL: $*" >&2
  exit 1
}

check_scripts() {
  local file
  shopt -s nullglob
  for file in attacker-tools/*.sh lab/*.sh; do
    bash -n "$file" || fail "syntax: $file"
  done
  python3 -m py_compile solutions/detect_misconfigurations.py
  echo "scripts: PASS"
}

if [[ "$scripts_only" -eq 1 ]]; then
  check_scripts
  exit 0
fi

python3 -m pytest
check_scripts
echo "lab-validate: PASS"
