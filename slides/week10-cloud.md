---
marp: true
theme: academic
class:


paginate: true
---

<!-- Title Slide -->
<div class="title-slide">

# Cloud &amp; Distributed Systems

<div class="subtitle">
Week 10 • Wednesday, November 5, 2025
</div>

<div class="meta">
4:00-17 PM • Engineering 294
<br>SJSU Hoplite Club • SWE Interview Master Plan
</div>

</div>

---

<!-- Learning Objectives -->
## 🎯 Learning Objectives

By the end of this session, you will be able to:

- Implement a minimal Terraform stack and verify idempotent applies.
- Containerize a service and deploy to Kubernetes; roll forward/back.
- Measure autoscaling behavior with HPA under synthetic load.

### Prerequisites
- Use Dockerfiles and push/pull images.
- Read YAML manifests and basic kubectl commands.

---

<!-- Session Agenda -->
<div class="agenda">

## 📋 Session Agenda

<div class="agenda-item">
  <div class="agenda-time">16:00</div>
  <div class="agenda-activity">Warm-up: Well-Architected pillars (10 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:10</div>
  <div class="agenda-activity">IaC: Terraform mini-stack (20 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:30</div>
  <div class="agenda-activity">K8s: containerize &amp; deploy (25 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:55</div>
  <div class="agenda-activity">HPA: load test &amp; observe (20 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">17:15</div>
  <div class="agenda-activity">Wrap up session (5 min)</div>
</div>

</div>


---

<!-- Key Concepts Overview -->
## 🧠 Key Concepts


### Focus Areas
- **Cloud**
- **DevOps**

---


<!-- Hands-On Activities -->
## 🛠️ Hands-On Activities

### 0: IaC → K8s pipeline (lab)

<div class="command-sequence">
Provision a minimal VPC or namespace with Terraform; run apply twice to confirm idempotency.
Build a container image; deploy a Deployment + Service.
Configure an HPA on CPU; run a load generator and observe scaling.
Perform a controlled rollback and verify availability.
</div>

⏱️ **Time allocated:** 25 minutes

---


<!-- Assessment -->
<div class="assessment-block">

## 📊 Assessment & Practice

### Project Assignment


</div>

---

<!-- Resources -->
<div class="resources-block">

## 📚 Resources & References

### Core Resources
- **[AWS Well-Architected Framework (overview)](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-six-pillars.html)** - Shared language for reliability, performance, and cost.
- **[Terraform — Getting Started](https://developer.hashicorp.com/terraform/tutorials/aws-get-started)** - Declarative infra with idempotent plans/applies.
- **[Kubernetes — Concepts](https://kubernetes.io/docs/concepts/overview/)** - Core objects and rollout strategies relevant to interviews.

### Additional Learning
- [GitHub Actions — Deploy Workflows](https://docs.github.com/actions/deployment)

### Quick Links
- [Algorithm Visualizer](https://algorithm-visualizer.org/) - Interactive algorithm animations
- [MIT OCW 6.006](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/) - Introduction to Algorithms

</div>

---



---

<!-- Next Week Preview -->
## 🔮 Coming Next Week

**Week 11: Senior Work Day** 🎓
- Career prep table at Student Union
- Portfolio reviews and technical interview practice
- One-on-one guidance from senior members


---

<!-- Closing Slide -->
<div class="title-slide">

## Questions & Discussion

**Slack:** #swe-interview-prep
**Office Hours:** Wednesdays 3:00-4:00 PM
**Next Session:** Week 11 • November 12

### Keep Practicing! 🚀

*Remember: Consistency beats intensity. Practice a little every day.*

</div>
