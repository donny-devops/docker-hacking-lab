# Quiz: Insecure Container Orchestration
## Questions
1. Default ServiceAccount tokens in every pod are risky because:
   A) They compress logs B) Stolen tokens may call the Kubernetes API C) They disable DNS D) They enable seccomp
2. `automountServiceAccountToken: false` is appropriate when:
   A) The workload must manage the cluster B) The app does not need the in-cluster API C) You want hostPID D) You need privileged
3. Pod Security "restricted" is meant to block:
   A) Signed images B) Privileged, host namespaces, and most hostPath uses C) Resource limits D) Read-only rootfs
## Answers
1. B 2. B 3. B
