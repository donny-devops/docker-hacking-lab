# Container Escape
Covers breakouts via docker socket, --privileged, host namespaces, and dangerous mounts.

## Attack scenario
A container with /var/run/docker.sock can create privileged sibling containers.

## Noncompliant
docker run -v /var/run/docker.sock:/var/run/docker.sock alpine

## Compliant
docker run --user 1000:1000 --read-only --cap-drop ALL alpine

## Remediation
- Avoid host namespace sharing.
- Drop capabilities; avoid --privileged.
- Use rootless Docker where possible.

## Hands-on lab
1. Run noncompliant container.
2. Attempt docker ps inside.
3. Harden and verify escape path blocked.
