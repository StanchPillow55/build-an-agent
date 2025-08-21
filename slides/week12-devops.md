---
marp: true
theme: academic
class:


paginate: true
---

<!-- Title Slide -->
<div class="title-slide">

# ML/AI for SWE — Small Models &amp; Serving

<div class="subtitle">
Week 12 • Wednesday, November 19, 2025
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

- Implement a regression and a tree-based model and evaluate bias/variance.
- Create a simple embedding-based search and explain cosine similarity.
- Deploy a model behind a REST endpoint and measure latency.

### Prerequisites
- Use Python notebooks and virtual environments.
- Explain train/validation/test splits.

---

<!-- Session Agenda -->
<div class="agenda">

## 📋 Session Agenda

<div class="agenda-item">
  <div class="agenda-time">16:00</div>
  <div class="agenda-activity">Warm-up: bias vs variance (10 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:10</div>
  <div class="agenda-activity">Models: regression &amp; trees (20 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:30</div>
  <div class="agenda-activity">Embeddings &amp; search (25 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:55</div>
  <div class="agenda-activity">Serving: REST endpoint (20 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">17:15</div>
  <div class="agenda-activity">Wrap up session (5 min)</div>
</div>

</div>

<div class="tip">
Thanksgiving week - final presentations, portfolio reviews
</div>

---

<!-- Key Concepts Overview -->
## 🧠 Key Concepts


### Focus Areas
- **ML**

---


<!-- Hands-On Activities -->
## 🛠️ Hands-On Activities

### 0: Train → Embed → Serve (lab)

<div class="command-sequence">
Train a regression and a small tree model; report metrics.
Compute embeddings for short texts; implement cosine similarity search.
Expose &#x60;/predict&#x60; and &#x60;/search&#x60; endpoints with FastAPI.
Load test with a small client; record median and p95 latency.
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
- **[Scikit-learn — Getting Started](https://scikit-learn.org/stable/getting_started.html)** - Baseline models with consistent APIs for quick iteration.
- **[FastAPI — First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)** - Lightweight serving stack for model endpoints.
- **[Embeddings — Primer](https://developers.google.com/machine-learning/crash-course/embeddings/intro-to-embeddings)** - Conceptual grounding before coding.

### Additional Learning
- [Kaggle — Mini Competition](https://www.kaggle.com/competitions)

### Quick Links
- [Algorithm Visualizer](https://algorithm-visualizer.org/) - Interactive algorithm animations
- [MIT OCW 6.006](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/) - Introduction to Algorithms

</div>

---



---

<!-- Next Week Preview -->
## 🔮 Coming Next Week



---

<!-- Closing Slide -->
<div class="title-slide">

## Questions & Discussion

**Slack:** #swe-interview-prep
**Office Hours:** Wednesdays 3:00-4:00 PM
**Next Session:** Final Presentations

### Keep Practicing! 🚀

*Remember: Consistency beats intensity. Practice a little every day.*

</div>
