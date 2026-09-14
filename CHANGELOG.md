# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-09-14

### Added

- Complete 11-module course catalog, including privileged containers (issue #7)
- Unique module and final assessments (22 files)
- Offline validation (`lab/validate.sh`, pytest) and GitHub Actions CI
- Hardened Compose topology and Compose misconfiguration detector
- Localhost-bound lab landing page under `lab/www/`

### Changed

- Attacker-tool scripts are detection helpers (no exploit payloads)
- Dependabot limited to ecosystems that exist in the repo
- Published lab ports bind to `127.0.0.1`

### Security

- `lab-internal` is an internal network
- Example AWS key remains Amazon's documentation placeholder

## [0.1.0] - 2026-06-08

### Added

- Initial Docker hacking lab scaffolding
- Repository meta files (SECURITY, CODEOWNERS, CONTRIBUTING, SUPPORT, CODE_OF_CONDUCT)
- Basic architecture and roadmap documentation

### Security

- Draft security policy and best practices for secret handling
