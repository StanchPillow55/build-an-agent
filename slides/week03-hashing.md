---
marp: true
theme: academic
class:


paginate: true
---

<!-- Title Slide -->
<div class="title-slide">

# Hash Tables &amp; Sliding Window

<div class="subtitle">
Week 3 • Wednesday, September 17, 2025
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

- Implement an open-addressing hash map with linear probing and proper deletion.
- Analyze expected probes vs load factor and evaluate resizing strategies.
- Apply frequency-map and sliding-window templates to solve substring problems.

### Prerequisites
- Trace pointer-free arrays and understand sentinel values.
- Explain amortized O(1) for dynamic arrays and why it matters for resizing.

---

<!-- Session Agenda -->
<div class="agenda">

## 📋 Session Agenda

<div class="agenda-item">
  <div class="agenda-time">16:00</div>
  <div class="agenda-activity">Warm-up: map vs set patterns (5 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:05</div>
  <div class="agenda-activity">Hashing: collisions, probing, deletion (25 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:30</div>
  <div class="agenda-activity">Lab: build &amp; test hash map (25 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:55</div>
  <div class="agenda-activity">Drill: sliding window (20 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">17:15</div>
  <div class="agenda-activity">Wrap up session (5 min)</div>
</div>

</div>


---

<!-- Key Concepts Overview -->
## 🧠 Key Concepts


<div class="two-column">
<div class="column">

### Core Data Structures & Algorithms
- **DSA**: Essential patterns and techniques

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

### 0: Build a lightweight hash map (lab)

<div class="command-sequence">
Implement &#x60;put/get/delete&#x60; with linear probing.
Add tombstones to handle deletions correctly.
Track load factor and trigger resize at 0.7.
Write tests that simulate clustering and verify expected probe counts.
</div>

⏱️ **Time allocated:** 25 minutes

---


<!-- Assessment -->
<div class="assessment-block">

## 📊 Assessment & Practice

### LeetCode Problems
<span class="leetcode-problem">1</span>
<span class="leetcode-problem">76</span>
<span class="leetcode-problem">438</span>

**Instructions:** For LC 1/76/438, apply frequency-map or sliding-window templates. In your notes, identify the window invariant and explain why shrinking/expanding preserves correctness and yields O(n).

<div class="tip">
Time-box each problem to 25 minutes. Focus on explaining your approach clearly, even if you don't finish coding.
</div>

</div>

---

<!-- Resources -->
<div class="resources-block">

## 📚 Resources & References

### Core Resources
- **[MIT OCW — Hashing (6.006)](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/)** - Covers hash functions, chaining vs open addressing, and analysis.
- **[Algorithm Visualizer — Sliding Window](https://algorithm-visualizer.org/)** - Helps reason about window expansion/contraction.
- **[Tech Interview Handbook — Hash Map Patterns](https://www.techinterviewhandbook.org/algorithms/hash-map/)** - Interview-ready templates and pitfalls.

### Additional Learning
- [Open addressing vs chaining](https://en.wikipedia.org/wiki/Hash_table)

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

**Week 4: Trees & Heaps**
- Binary tree traversals and properties
- Heap operations and priority queues
- Balanced tree concepts


---

<!-- Closing Slide -->
<div class="title-slide">

## Questions & Discussion

**Slack:** #swe-interview-prep
**Office Hours:** Wednesdays 3:00-4:00 PM
**Next Session:** Week 4 • September 24

### Keep Practicing! 🚀

*Remember: Consistency beats intensity. Practice a little every day.*

</div>
