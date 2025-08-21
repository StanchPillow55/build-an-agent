# Speaker Notes: Cloud & Distributed Systems

**Date:** 2025-11-06
**Duration:** 90 minutes
**Week:** 10

## Session Overview
- **Objectives:** 3 learning objectives
- **Activities:** 1 hands-on activities
- **Assessment:** 1 assessment items

## Timing & Agenda
- **16:00** (10 min): Warm-up: Well-Architected pillars\n- **16:10** (20 min): IaC: Terraform mini-stack\n- **16:30** (25 min): K8s: containerize & deploy\n- **16:55** (20 min): HPA: load test & observe\n- **17:15** (5 min): Wrap up session

## Speaker Beats
1. IaC is about repeatability; drift is your hidden enemy.\n2. K8s primitives: Deployment, Service, HPA—interview essentials.\n3. Autoscaling demo shows elasticity; mention metrics and SLOs.\n4. Rollbacks and health checks build credibility.

## Demo Steps
1. Run `terraform apply` twice to show no changes.\n2. Deploy image; edit deployment to roll a new version.\n3. Trigger load; view `kubectl top pods`.

## Time Cues
- **Minute 10:** show a Terraform plan.\n- **Minute 30:** deploy and inspect pods.\n- **Minute 55:** start load and watch HPA events.

## FAQ Preparation
**Q:** Do interviews require cloud accounts?\n**A:** No; discuss patterns and trade-offs clearly and you'll score well.\n

## Resources for Reference
- [AWS Well-Architected Framework (overview)](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-six-pillars.html) - Shared language for reliability, performance, and cost.\n- [Terraform — Getting Started](https://developer.hashicorp.com/terraform/tutorials/aws-get-started) - Declarative infra with idempotent plans/applies.\n- [Kubernetes — Concepts](https://kubernetes.io/docs/concepts/overview/) - Core objects and rollout strategies relevant to interviews.

## Assessment Details
- **project:** Submit a short screencast or log showing: `terraform plan` → `apply`, `kubectl rollout status`, HPA scaling events, and one rollback. Add a 1-page note on failure modes and mitigations.

---
*Generated from week10-cloud.md*
