# Quiz: Insecure Container Configuration
## Questions
1. `--read-only` plus tmpfs is meant to:
   A) Speed overlay2 B) Stop persistence on the container rootfs C) Disable networking D) Grant SYS_ADMIN
2. `no-new-privileges:true` blocks:
   A) DNS B) Privilege-gaining exec (setuid/file caps) C) Healthchecks D) Log drivers
3. Non-root `user:` in Compose reduces impact because:
   A) The kernel is patched B) Compromised processes have fewer host-equivalent rights C) Images become signed D) Ports cannot be published
## Answers
1. B 2. B 3. B
