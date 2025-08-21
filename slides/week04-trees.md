---
marp: true
theme: academic
class:


paginate: true
---

<!-- Title Slide -->
<div class="title-slide">

# Balanced Trees &amp; Heaps

<div class="subtitle">
Week 4 • Wednesday, September 24, 2025
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

- Implement RB-tree rotations and fix-up to restore red/black properties.
- Build a binary heap and compute median of a stream with two heaps.
- Compare balancing strategies (AVL, RB) and evaluate trade-offs.

### Prerequisites
- Describe binary search tree properties and traversal orders.
- Trace pointer manipulations and recursive insert/delete.

---

<!-- Session Agenda -->
<div class="agenda">

## 📋 Session Agenda

<div class="agenda-item">
  <div class="agenda-time">16:00</div>
  <div class="agenda-activity">Warm-up: BST vs balanced BST (10 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:10</div>
  <div class="agenda-activity">RB-tree invariants &amp; rotations (20 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:30</div>
  <div class="agenda-activity">Lab: CLI visualizer + heaps (25 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:55</div>
  <div class="agenda-activity">Drill: median stream (20 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">17:15</div>
  <div class="agenda-activity">Wrap up session (5 min)</div>
</div>

</div>

<div class="tip">
Intro meeting IDE/GIT fundamentals recap
</div>

---

<!-- Key Concepts Overview -->
## 🧠 Key Concepts


<div class="two-column">
<div class="column">

### Core Data Structures & Algorithms
- **DSA**: Essential patterns and techniques
- **Trees**: Essential patterns and techniques

</div>
<div class="column">

### Problem-Solving Approach
1. **Understand** the problem
2. **Plan** your approach
3. **Code** the solution
4. **Test** and optimize

</div>
</div>

---


<!-- Hands-On Activities -->
## 🛠️ Hands-On Activities

### 0: RB-tree rotation visualizer (lab)

<div class="command-sequence">
Implement left/right rotation functions.
Animate insertions and call fix-up to restore invariants.
Log color flips and rotations; verify black-height consistency.
Add min-heap and max-heap; compute streaming median.
</div>

⏱️ **Time allocated:** 25 minutes

---


<!-- Assessment -->
<div class="assessment-block">

## 📊 Assessment & Practice

### LeetCode Problems
<span class="leetcode-problem">98</span>
<span class="leetcode-problem">230</span>

**Instructions:** For LC 98, state the invariant (BST via in-order monotonicity or bounds). For LC 230, compare inorder vs heap approaches and justify time/space trade-offs.

<div class="tip">
Time-box each problem to 25 minutes. Focus on explaining your approach clearly, even if you don't finish coding.
</div>

</div>

---

<!-- Resources -->
<div class="resources-block">

## 📚 Resources & References

### Core Resources
- **[MIT OCW 6.006 — Balanced BSTs &amp; Heaps](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/)** - Grounding theory with practical operations and complexity.
- **[Algorithm Visualizer — Heaps](https://algorithm-visualizer.org/)** - See heapify and sift-up/down dynamics.
- **[Tech Interview Handbook — Trees](https://www.techinterviewhandbook.org/algorithms/trees/)** - Interview cues and common invariants to state.

### Additional Learning
- [CLRS — Red-Black Trees](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/)

### Quick Links
- [Algorithm Visualizer](https://algorithm-visualizer.org/) - Interactive algorithm animations
- [MIT OCW 6.006](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/) - Introduction to Algorithms
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/) - Time/space complexity reference

</div>

---


<!-- DO/DON'T for DSA - Success With SCE Style -->
<div class="two-column">

<div class="do">
**Focus on problem-solving approach**
- Explain your thinking out loud
- Start with brute force, then optimize
- Test your solution with examples
- Practice coding by hand occasionally
</div>

<div class="dont">
**Don't memorize solutions**
- Avoid just copying code from discussions
- Don't skip the explanation step
- Don't ignore edge cases
- Don't panic when stuck - think step by step
</div>

</div>

---

<!-- Next Week Preview -->
## 🔮 Coming Next Week

**Week 5: Industry Mixer** 🎉
- Virtual networking and interview tips
- Technical interview anxiety management
- Breakout rooms with industry professionals


---

<!-- Closing Slide -->
<div class="title-slide">

## Questions & Discussion

**Slack:** #swe-interview-prep
**Office Hours:** Wednesdays 3:00-4:00 PM
**Next Session:** Week 5 • October 1

### Keep Practicing! 🚀

*Remember: Consistency beats intensity. Practice a little every day.*

</div>
