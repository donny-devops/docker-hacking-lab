# Quiz: Denial-of-Service (DoS)
## Questions
1. `--pids-limit` is designed to stop:
   A) TLS downgrade B) Fork bombs exhausting PID cgroups C) Image signing D) Seccomp
2. Memory limits without an eviction/restart policy can still:
   A) Patch the kernel B) OOM-kill the container rather than the whole host immediately C) Disable Docker D) Sign images
3. Shared-host DoS is possible because containers:
   A) Each have a hypervisor by default B) Share host CPU/memory/I/O and consume host PID capacity unless limited C) Cannot use cgroups D) Always have 1 millicpu
## Answers
1. B 2. B 3. B
