# Denial-of-Service (DoS)
Covers CPU/memory/PIDs/I/O exhaustion and runtime limits.

## Attack scenario
Fork bomb or memory hog crashes neighboring containers/host.

## Noncompliant
docker run -d --name stress docker-stress

## Compliant
docker run -d --name stress --cpus 0.5 --memory 256m --pids-limit 64 docker-stress

## Remediation
- Set --cpus --memory --pids-limit.
- Use --restart on-failure:5.
- Monitor with cAdvisor/Prometheus.

## Hands-on lab
1. Run stress unconstrained.
2. Observe impact.
3. Apply limits and compare.
