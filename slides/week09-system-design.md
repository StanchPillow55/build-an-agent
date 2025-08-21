---
marp: true
theme: academic
class:


paginate: true
---

<!-- Title Slide -->
<div class="title-slide">

# System Design Bootcamp

<div class="subtitle">
Week 9 • Wednesday, October 29, 2025
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

- Define high-level APIs and data models for a small web service.
- Evaluate CAP and consistency models for the core operations.
- Design a scaling plan using caching, sharding, and replication.
- Design a URL shortener and rate limiter with clear trade-offs.
- Present and justify design decisions under time constraints.

### Prerequisites
- Describe latency vs throughput and p-percentiles.
- Differentiate strong vs eventual consistency at a high level.

---

<!-- Session Agenda -->
<div class="agenda">

## 📋 Session Agenda

<div class="agenda-item">
  <div class="agenda-time">16:00</div>
  <div class="agenda-activity">Warm-up: requirements triage (5 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:05</div>
  <div class="agenda-activity">Scaling patterns: cache, shard, replicate (25 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:30</div>
  <div class="agenda-activity">Design lab: URL shortener (25 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:55</div>
  <div class="agenda-activity">Design lab: rate limiter (20 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">17:15</div>
  <div class="agenda-activity">Share-outs &amp; wrap (5 min)</div>
</div>

</div>

<div class="tip">
Halloween week - URL shortener + rate limiting
</div>

---

<!-- Key Concepts Overview -->
## 🧠 Key Concepts


### Focus Areas
- **System-Design**

---


<!-- Hands-On Activities -->
## 🛠️ Hands-On Activities

### 0: Two-problem design studio (lab)

<div class="command-sequence">
URL shortener: define API, schema, and hash/id strategy.
Sketch read/write paths with cache and DB.
Rate limiter: choose algorithm (token bucket or leaky bucket) and data store.
List trade-offs and failure modes; present a 2-minute defense.
</div>

⏱️ **Time allocated:** 45 minutes

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
- **[ByteByteGo — System Design Primer](https://bytebytego.com/)** - Succinct overviews of common patterns and trade-offs.
- **[Google SRE — Availability &amp; SLIs](https://sre.google/sre-book/availability-table/)** - Ground design decisions in reliability targets.
- **[Cloudflare — Rate Limiting Concepts](https://developers.cloudflare.com/rate-limits/about/)** - Concrete designs and pitfalls from a production CDN.


### Quick Links
- [Algorithm Visualizer](https://algorithm-visualizer.org/) - Interactive algorithm animations
- [MIT OCW 6.006](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/) - Introduction to Algorithms

</div>

---



---

<!-- Next Week Preview -->
## 🔮 Coming Next Week

**Week 10: Cloud & Distributed Systems**
- AWS Well-Architected Framework principles
- Docker containerization and Kubernetes orchestration
- Infrastructure as Code with Terraform


---

<!-- Closing Slide -->
<div class="title-slide">

## Questions & Discussion

**Slack:** #swe-interview-prep
**Office Hours:** Wednesdays 3:00-4:00 PM
**Next Session:** Week 10 • November 5

### Keep Practicing! 🚀

*Remember: Consistency beats intensity. Practice a little every day.*

</div>
