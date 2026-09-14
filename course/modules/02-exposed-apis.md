# Exposed Container APIs

The Docker Engine API is host-root equivalent. Binding it to TCP without TLS client authentication, or mounting `docker.sock` into an app container, hands that power to whoever can reach the API.

## Attack scenario

A daemon is started with `tcp://0.0.0.0:2375`. Anyone who can reach port 2375 can create containers, including ones that mount the host filesystem.

## Noncompliant

```bash
dockerd -H unix:///var/run/docker.sock -H tcp://0.0.0.0:2375
```

Lab analogue: `vuln-web` bind-mounts `/var/run/docker.sock`.

## Compliant

```bash
dockerd -H unix:///var/run/docker.sock -H tcp://127.0.0.1:2376 \
  --tlsverify --tlscacert ca.pem --tlscert cert.pem --tlskey key.pem
```

Do not mount the engine socket into application containers. If tooling needs a narrow API, put a socket proxy in front with an allow-list.

## Remediation

- Bind Engine listeners to localhost or a management network only.
- Require TLS client certificates on TCP (2376), never plain 2375.
- Firewall the daemon; do not publish it on lab-external or the internet.
- Prefer rootless Docker or a dedicated CI runner host.

## Hands-on lab

1. Inspect published ports and socket mounts in `docker-compose.yml`.
2. Confirm the lab binds host ports to `127.0.0.1`.
3. Confirm `vuln-web` still has a socket mount in the insecure baseline and not in the hardened file.
4. List Engine listeners on your host (`ss -lntp | grep docker` or equivalent) without sending mutating API calls.
