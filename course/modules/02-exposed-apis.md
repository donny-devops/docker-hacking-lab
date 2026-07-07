# Exposed Container APIs
Covers Docker daemon socket/API exposure, auth bypass, TLS, and network exposure risks.

## Attack scenario
Exposing `2375/2376` without auth allows remote host takeover.

## Noncompliant
docker run -d -p 2375:2375 docker:dind

## Compliant
docker run -d -p 127.0.0.1:2376:2376 `
  --tlsverify --tlscacert ca.pem --tlscert cert.pem --tlskey key.pem docker:dind

## Remediation
- Bind to localhost or VPN only.
- Enforce TLS client auth on 2376.
- Firewall-restrict daemon ports.

## Hands-on lab
1. Inspect Docker socket listeners.
2. Confirm remote API auth requirements.
3. Harden with TLS/localhost binding.
