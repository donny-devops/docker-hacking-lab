# Final assessment: Insecure Container Orchestration
## Questions
1. Least-privilege RBAC for an app should:
   A) Bind cluster-admin to default B) Grant only the API verbs/resources that workload needs C) Share one SA for the whole cluster D) Mount docker.sock
2. Compose `privileged: true` maps most closely to which Kubernetes anti-pattern?
   A) `securityContext.privileged: true` B) `imagePullPolicy: IfNotPresent` C) `replicas: 2` D) `ClusterIP`
## Answers
1. B 2. A
