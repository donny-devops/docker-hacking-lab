# Quiz: Shared Kernel Exploitation
## Questions
1. `--pid=host` causes a container to:
   A) Hide `/proc` B) See host and neighbor process IDs C) Enable seccomp D) Drop CAP_SYS_ADMIN
2. `/proc/<pid>/environ` on a shared PID namespace can leak:
   A) Overlay compression ratios B) Process environment secrets C) Cosign keys from GitHub automatically D) AppArmor profiles only
3. `internal: true` on a Compose network:
   A) Makes the network a hypervisor B) Removes a default external gateway for that network C) Forces `--privileged` D) Publishes all ports
## Answers
1. B 2. B 3. B
