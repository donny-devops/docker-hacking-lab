# Final assessment: Privileged Containers
## Questions
1. Why is "the app is trusted" a weak justification for `--privileged`?
   A) Privileged mode only affects cgroup names B) Base image and dependencies share the same disabled controls C) Privileged mode encrypts `/dev` D) Docker ignores the flag on Linux
2. Which detection command is sufficient to inventory privileged containers?
   A) `docker logs` B) `docker inspect --format '{{.HostConfig.Privileged}}'` C) `docker pull` D) `docker login`
## Answers
1. B 2. B
