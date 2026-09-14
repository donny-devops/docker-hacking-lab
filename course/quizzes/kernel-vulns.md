# Quiz: Kernel Vulnerabilities
## Questions
1. Rebuilding a container image:
   A) Always patches the host kernel B) Does not change the shared host kernel C) Disables runc D) Enables SELinux
2. CVE-2019-5736 is associated with which layer?
   A) PostgreSQL protocol B) runc `/proc/self/exe` handling C) DNS D) Overlay networking only
3. Unprivileged user namespaces can matter for kernel CVEs because they:
   A) Remove the kernel B) May grant capability bits inside a new namespace C) Sign images D) Block all syscalls
## Answers
1. B 2. B 3. B
