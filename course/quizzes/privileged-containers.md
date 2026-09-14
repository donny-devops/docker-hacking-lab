# Quiz: Privileged Containers
## Questions
1. What does `--privileged` do to seccomp and AppArmor in Docker?
   A) Tightens both profiles B) Disables both C) Enables user namespaces D) Only drops NET_RAW
2. Which inspect field confirms a container is privileged?
   A) Config.Tty B) HostConfig.Privileged C) NetworkSettings.IPAddress D) Config.WorkingDir
3. Safest default replacement for a previously privileged helper container?
   A) `--privileged --read-only` B) `--cap-drop ALL` plus `no-new-privileges` C) `--pid=host` D) `--network=host`
## Answers
1. B 2. B 3. B
