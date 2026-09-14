# docker-hacking-lab Roadmap

## Phase 1 – Foundations

- [x] Base Docker and Compose configuration
- [x] Isolated lab network (`lab-internal` is internal)
- [x] Core misconfiguration scenarios (privileged, socket, host mount)
- [x] Quickstart, safety warning, and support doc

## Phase 2 – Advanced Scenarios

- [x] Course catalog modules 01–11 (privileged containers included)
- [x] Unique quizzes (no copy-paste assessments)
- [ ] Optional Kubernetes manifests that mirror the Compose findings
- [ ] Image signing demo using a local Sigstore/cosign flow

## Phase 3 – Security Automation

- [x] GitHub Actions validation workflow
- [x] Dependabot for Actions, pip, and the lab Dockerfile
- [ ] CodeQL (when application code warrants it)
- [ ] Branch protection requiring the `lab-validate` check

## Phase 4 – Community and Ecosystem

- Community-contributed scenarios
- Integration with other labs or CTF platforms
- Optional self-hosted runner setups (with strict guidance)
