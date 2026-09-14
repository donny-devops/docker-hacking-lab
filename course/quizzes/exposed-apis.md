# Quiz: Exposed Container APIs
## Questions
1. Unauthenticated Docker API on TCP 2375 is closest to:
   A) Read-only metrics B) Host-root equivalent control C) Image-layer compression D) DNS hijacking only
2. Which port/protocol pairing is the authenticated Engine listener?
   A) 2375/plain TCP B) 2376 with TLS client auth C) 80/HTTP D) 53/UDP
3. Why is mounting `/var/run/docker.sock` into an app container dangerous?
   A) It slows overlay2 B) The socket speaks the Engine API as the daemon user C) It disables IPv6 D) It blocks healthchecks
## Answers
1. B 2. B 3. B
