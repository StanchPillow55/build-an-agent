---
marp: true
theme: academic
class:
  - special-event

paginate: true
---

<!-- Title Slide -->
<div class="title-slide">

# DevOps &amp; Observability — CI, Tracing, SLOs

<div class="subtitle">
Week 11 • Tuesday, November 11, 2025
</div>

<div class="meta">
4:30-18 PM • Student Union Room 3
<br>SJSU Hoplite Club • SWE Interview Master Plan
</div>

</div>

---

<!-- Learning Objectives -->
## 🎯 Learning Objectives

By the end of this session, you will be able to:

- Implement a CI workflow that runs unit and end-to-end tests on PR.
- Instrument tracing/metrics and build a Grafana dashboard.
- Evaluate SLOs and configure an alert for an error-rate breach.

### Prerequisites
- Write basic unit tests and a simple e2e script.
- Explain percentiles and why p99 matters.

---

<!-- Session Agenda -->
<div class="agenda">

## 📋 Session Agenda

<div class="agenda-item">
  <div class="agenda-time">16:00</div>
  <div class="agenda-activity">Warm-up: what SLOs buy you (10 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:10</div>
  <div class="agenda-activity">CI: GH Actions pipeline (20 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:30</div>
  <div class="agenda-activity">Tracing &amp; metrics (25 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:55</div>
  <div class="agenda-activity">Dashboards &amp; alerting (20 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">17:15</div>
  <div class="agenda-activity">Wrap up session (5 min)</div>
</div>

</div>

<div class="tip">
Wednesday timing - Veterans Day week
</div>

---

<!-- Key Concepts Overview -->
## 🧠 Key Concepts


### Focus Areas
- **DevOps**

---


<!-- Hands-On Activities -->
## 🛠️ Hands-On Activities

### 0: Wire CI and observability (lab)

<div class="command-sequence">
Create &#x60;.github/workflows/ci.yml&#x60; that installs deps and runs unit + e2e tests.
Add OpenTelemetry instrumentation to one request path.
Export metrics to a local collector and visualize in Grafana.
Create an alert: error rate &gt; 2% over 5 minutes.
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
- **[GitHub Actions — Testing on Pull Requests](https://docs.github.com/actions/using-workflows/events-that-trigger-workflows#pull_request)** - Trigger CI on the right events with required checks.
- **[OpenTelemetry — Getting Started](https://opentelemetry.io/docs/)** - Vendor-neutral tracing and metrics.
- **[Grafana — Building Dashboards](https://grafana.com/docs/grafana/latest/getting-started/)** - Translate signals into actionable visuals.

### Additional Learning
- [SRE Workbook — SLOs](https://sre.google/workbook/slo/)

### Quick Links
- [Algorithm Visualizer](https://algorithm-visualizer.org/) - Interactive algorithm animations
- [MIT OCW 6.006](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/) - Introduction to Algorithms

</div>

---



---

<!-- Next Week Preview -->
## 🔮 Coming Next Week

**Week 12: DevOps & ML + Final Presentations**
- CI/CD pipelines and deployment strategies
- Machine Learning for software engineers
- Final project presentations and wrap-up


---

<!-- Closing Slide -->
<div class="title-slide">

## Questions & Discussion

**Slack:** #swe-interview-prep
**Office Hours:** Wednesdays 3:00-4:00 PM
**Next Session:** Week 12 • November 18

### Keep Practicing! 🚀

*Remember: Consistency beats intensity. Practice a little every day.*

</div>
