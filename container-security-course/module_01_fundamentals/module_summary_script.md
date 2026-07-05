# Module 1: Container Security Fundamentals — Module Summary Script

**Duration:** 2:30  
**Format:** Mixed (PPT slides + terminal teaser + browser)  
**Purpose:** Module overview and orientation  

---

## SCRIPT BEGIN

### [0:00–0:20] — Opening / Hook (PPT Slide: Title Slide)

**SLIDE:** *Module 1: Container Security Fundamentals* — Course logo, module number badge, subtitle: "Understanding What You're Defending"

**NARRATION:**
"Welcome to Module 1 of the Container Security Masterclass. In this module, we're going to take apart container technology piece by piece — not from a DevOps perspective, but from a security perspective. By the end, you'll understand exactly what a container is at the kernel level, where the security boundaries actually are, and where they break down."

---

### [0:20–0:55] — What You'll Learn (PPT Slide: Learning Objectives)

**SLIDE:** Bullet list with icons:
- Container architecture from a security lens
- Linux namespaces and cgroups — the real isolation
- Container vs. VM security models
- The shared kernel problem
- Docker daemon attack surface
- Container threat landscape overview

**NARRATION:**
"Here's what we'll cover across five lessons. First, we'll look at container architecture — not how to use Docker, but how containers actually isolate processes using Linux namespaces and cgroups. Then we'll compare container isolation to virtual machine isolation side by side, and you'll see exactly why containers have a fundamentally different — and in many ways weaker — security model. We'll dig into the shared kernel problem — the single biggest architectural risk in container deployments. Then we'll move to Docker-specific security: the daemon, its configuration, and common misconfigurations that lead to full host compromise. Finally, we'll map the complete container attack surface so you know exactly what adversaries target."

---

### [0:55–1:25] — Why It Matters (PPT Slide: Real-World Context)

**SLIDE:** Headline: "Why This Matters" — Statistics:
- 87% of organizations run containerized workloads (2024 CNCF Survey)
- 76% of container images contain known vulnerabilities (Sysdig Report)
- Average time to exploit a misconfigured container: under 5 minutes

**NARRATION:**
"Why does this matter? Because containers are everywhere — 87 percent of organizations now run containerized workloads in production. But here's the problem: 76 percent of container images in the wild contain known vulnerabilities. And a misconfigured container? An attacker can go from initial access to full host compromise in under five minutes. We'll prove that in later modules. But first, you need the fundamentals — because without understanding how container isolation actually works, you can't evaluate whether it's working correctly."

---

### [1:25–1:55] — Prerequisites (PPT Slide: Prerequisites)

**SLIDE:** Two columns:  
*Required:* Basic Linux command line, understanding of processes and filesystems  
*Helpful but not required:* Prior Docker experience, basic networking concepts

**NARRATION:**
"To get the most from this module, you should be comfortable with the Linux command line — things like navigating the filesystem, running commands as root, and reading process listings. If you've used Docker before, that helps, but it's not required — we'll cover everything from the ground up. We'll also touch on networking concepts, but nothing beyond what we'll explain in context."

---

### [1:55–2:15] — What You'll Be Able To Do (PPT Slide: Outcomes)

**SLIDE:** Checklist with green checkmarks:
- ✅ Inspect container isolation boundaries using Linux tools
- ✅ Identify misconfigured Docker daemon settings
- ✅ Explain the shared kernel risk to stakeholders
- ✅ Map the attack surface of a containerized application
- ✅ Evaluate whether a container deployment meets security baselines

**NARRATION:**
"After completing this module, you'll be able to inspect container isolation boundaries directly using Linux tools — no Docker CLI abstractions. You'll know how to audit a Docker daemon configuration for dangerous settings. You'll be able to clearly explain the shared kernel risk to both technical and non-technical stakeholders. And you'll have a mental map of the entire container attack surface that you'll carry through the rest of this course."

---

### [2:15–2:30] — Transition (Terminal Teaser)

**SCREEN:** Quick terminal flash showing:
```bash
$ unshare --mount --uts --ipc --net --pid --fork bash
# hostname container-demo
# echo $$ 
1
```

**NARRATION:**
"Let's get started. In the first lesson, we're going to build a container from scratch — using nothing but Linux system calls. No Docker, no runtime — just raw kernel features. Let's go."

---

## SCRIPT END

### Post-Production Notes
- Title slide should match course branding established in course summary
- Statistics on the "Why It Matters" slide should use animated count-up effect
- Terminal teaser at the end should be a brief 3-second clip, slightly sped up
- Background music: subtle, professional, fades out before terminal teaser
- Transition to Video 01 should be a hard cut after the terminal flash
