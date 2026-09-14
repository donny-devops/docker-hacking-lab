.PHONY: help test validate compose-config scripts

help:
	@echo "Targets:"
	@echo "  test            Run inventory, compose, and script checks"
	@echo "  validate        Same as test via lab/validate.sh"
	@echo "  scripts         Syntax-check attacker-tools and lab scripts"
	@echo "  compose-config  Render compose if Docker is installed"

test:
	python3 -m pytest

validate:
	bash lab/validate.sh

scripts:
	bash lab/validate.sh --scripts-only

compose-config:
	@if command -v docker >/dev/null 2>&1; then \
		docker compose -f docker-compose.yml config >/dev/null && echo "compose: OK"; \
		docker compose -f docker-compose.hardened.yml config >/dev/null && echo "hardened compose: OK"; \
	else \
		echo "Docker is not installed; YAML is still checked by pytest."; \
	fi
