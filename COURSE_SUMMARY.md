# Hands-on Docker Hacking

**Status:** operational catalog on `main` via the lab-readiness updates. Isolated lab only.

## Scope

- 11 modules with intro, attack scenario, compliant/noncompliant examples, remediation, and lab
- 22 assessments: 3 questions per module quiz + 2 final questions per module
- Files stored in `course/modules/` and `course/quizzes/`

## Course modules

01 - Privileged Containers
02 - Exposed Container APIs
03 - Container Escape
04 - Container Image Tampering
05 - Insecure Configuration
06 - Denial-of-Service
07 - Kernel Vulnerabilities
08 - Shared Kernel Exploitation
09 - Insecure Container Orchestration
10 - Insecure Container Images
11 - What Seccomp, AppArmor, and SELinux Actually Do

## Notes

- Target runtime: Docker Desktop or a Linux host
- Validate the catalog with `make test`
- Teaching compose file: `docker-compose.yml`
- Defensive compose file: `docker-compose.hardened.yml`
