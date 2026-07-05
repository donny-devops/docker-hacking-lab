# Module 2: Privileged Containers & Attack Vectors — Module Summary Script

**Duration:** 2:30  
**Format:** Mixed (PPT slides + terminal teaser)  
**Purpose:** Module overview and orientation  

---

## SCRIPT BEGIN

### [0:00–0:20] — Opening / Hook (PPT Slide: Title Slide)

**SLIDE:** *Module 2: Privileged Containers & Attack Vectors* — Red warning icon, subtitle: "Breaking Out of the Box"

**NARRATION:**
"Welcome to Module 2. In Module 1, we built the security-focused mental model of container architecture. In this module, we break it. You're going to see, step by step, exactly how containers are compromised — from privileged container abuse to full host takeover. This is the offensive security module, and it's where theory becomes reality."

---

### [0:20–0:55] — What You'll Learn (PPT Slide: Learning Objectives)

**SLIDE:** Bullet list with icons:
- What privileged containers are and what they unlock
- Hands-on host system compromise from a privileged container
- Privilege escalation attack techniques
- Container escape methods — from kernel exploits to misconfigurations
- Real-world CVE analysis and exploitation walkthroughs

**NARRATION:**
"We're covering four lessons in this module. First, we'll examine what privileged containers actually are — what capabilities they gain, what protections they lose, and why they exist in the first place. Then we'll demonstrate host system compromise from inside a privileged container — reading host files, writing to host filesystems, and establishing persistence. Next, we'll explore privilege escalation techniques — moving from an unprivileged container to root on the host through multiple attack paths. And finally, we'll analyze real CVEs — CVE-2019-5736, CVE-2020-15257, and CVE-2022-0185 — walking through the exploit chains step by step."

---

### [0:55–1:25] — Why It Matters (PPT Slide: Real-World Context)

**SLIDE:** Headline: "The Privileged Container Problem" — Key facts:
- 23% of cloud containers run with excessive privileges (Sysdig 2024 Report)
- Tesla's Kubernetes cluster was compromised via a privileged container (2018)
- Capital One breach involved container misconfiguration with excessive IAM roles
- Average dwell time for container compromise: 4 hours before detection

**NARRATION:**
"Twenty-three percent of containers in production run with more privileges than they need. One in four. Tesla's Kubernetes cluster was compromised through an exposed dashboard that allowed attackers to run privileged containers — which they used for cryptomining. The Capital One breach involved misconfigured containers with excessive cloud permissions. And once an attacker is inside a container, the average organization takes four hours to detect the compromise. By then, if the container is privileged, the host is already owned. Understanding these attacks is how you learn to prevent them."

---

### [1:25–1:55] — Prerequisites (PPT Slide: Prerequisites)

**SLIDE:** Two columns:  
*Required:* Module 1 completion, Linux CLI proficiency, understanding of namespaces and cgroups  
*Helpful:* Docker experience, basic security/pentesting concepts, familiarity with CVE advisories

**NARRATION:**
"You must complete Module 1 before starting this module — we build directly on the namespace, cgroup, and kernel concepts from those lessons. You need solid Linux command-line skills, because we'll be working extensively in the terminal. Basic Docker experience helps, and if you've done any penetration testing or red team work, you'll find the techniques familiar — but applied in a container context."

---

### [1:55–2:15] — What You'll Be Able To Do (PPT Slide: Outcomes)

**SLIDE:** Checklist with green checkmarks:
- ✅ Identify when a container is running in privileged mode
- ✅ Demonstrate host compromise from a privileged container
- ✅ Execute multiple container escape techniques
- ✅ Analyze CVE advisories for container-relevant exploits
- ✅ Build a container escape detection strategy

**NARRATION:**
"After this module, you'll be able to detect privileged containers in your environment, demonstrate exactly why they're dangerous to stakeholders, execute multiple container escape paths — which is essential for red team and penetration testing work — analyze CVE advisories for container impact, and build detection strategies for container escape attempts."

---

### [2:15–2:30] — Transition (Terminal Teaser)

**SCREEN:** Quick terminal flash showing:
```bash
container# mount /dev/sda1 /mnt
container# chroot /mnt bash
root@actual-host# cat /etc/shadow
root:$6$...encrypted_hash...
```

**NARRATION:**
"Ready? Let's start by understanding exactly what the `--privileged` flag does to a container. Because once you see what it unlocks, you'll understand why it should never appear in production."

---

## SCRIPT END

### Post-Production Notes
- Use a more dramatic/darker slide theme for this module to differentiate from Module 1
- Red accent color for warning elements throughout this module
- Terminal teaser should have a slight glitch/scan-line effect for dramatic impact
- Add a brief "⚠️ Lab Environment Only" disclaimer overlay during the terminal teaser
- Music: slightly more intense/dramatic than Module 1, fading before terminal teaser
