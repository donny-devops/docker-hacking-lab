# Final assessment: Container Escape
## Questions
1. Which option most directly reduces runtime breakout surface?
   A) `--privileged` B) drop caps + seccomp + read-only C) expose 2375 D) host network
2. After removing a socket mount, what should you re-check?
   A) That `docker.sock` is absent from `docker inspect` mounts B) That the image has more CVEs C) That privileged is now true D) That the host kernel is older
## Answers
1. B 2. A
