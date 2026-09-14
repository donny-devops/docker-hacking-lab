# Quiz: Container Escape
## Questions
1. Which misconfiguration lets a non-privileged container create privileged siblings?
   A) Read-only rootfs B) Docker socket bind-mount C) Memory limit D) `tmpfs /tmp`
2. Host-root bind (`-v /:/host`) primarily enables:
   A) Faster DNS B) Direct host filesystem access from the container C) Automatic image signing D) Seccomp logging
3. Which combination most reduces breakout surface?
   A) `--privileged` and host PID B) drop caps + seccomp + read-only + non-root C) publish 2375 D) `--network=host`
## Answers
1. B 2. B 3. B
