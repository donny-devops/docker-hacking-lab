# Quiz: Insecure Container Images
## Questions
1. `php:7.4-apache` in this lab is useful as a teaching target because:
   A) It is the current PHP LTS B) It is an EOL runtime with a larger historical CVE set C) It enables SELinux D) It is distroless
2. Distroless/minimal runtime images reduce:
   A) The need for TLS B) Extra packages and shells in the attack surface C) The need to patch the kernel D) Namespace isolation
3. A deploy gate that runs Trivy with `--exit-code 1`:
   A) Always pushes anyway B) Fails the pipeline when findings meet the threshold C) Disables Compose D) Grants SYS_ADMIN
## Answers
1. B 2. B 3. B
