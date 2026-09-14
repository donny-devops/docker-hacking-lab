# Quiz: Container Image Tampering
## Questions
1. Why is `app:latest` a weak deploy pin?
   A) Latest is always distroless B) The tag can be moved to a different digest C) Tags cannot be pushed D) Compose rejects latest
2. Cosign/Sigstore is used to:
   A) Compress layers B) Sign and verify an image digest C) Replace seccomp D) Disable registries
3. A typosquat registry name is dangerous because:
   A) DNSSEC always blocks it B) Humans and scripts may pull the wrong image C) Docker refuses unknown names D) It enables seccomp
## Answers
1. B 2. B 3. B
