# Final assessment: Shared Kernel Exploitation
## Questions
1. Strongest default PID isolation?
   A) `--pid=host` B) Container-scoped PID namespace C) Sharing `/proc` from the host D) `--privileged`
2. Why avoid `--network=host` for apps?
   A) It improves seccomp B) The container shares the host network stack and host sockets C) It pins image digests D) It drops all capabilities
## Answers
1. B 2. B
