# Attacker-tools directory

Scripts in this folder are **detection and comparison helpers** for the isolated lab. They inspect namespaces, mounts, and Compose/Engine configuration. They do not include exploit payloads, credential dumping, or traffic spoofing.

Run them from a lab shell after `docker compose up -d`, or with the Docker CLI on the lab host.

Companion analyzer: `solutions/detect_misconfigurations.py`.
