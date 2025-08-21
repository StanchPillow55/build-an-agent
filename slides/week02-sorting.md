---
marp: true
theme: academic
class:


paginate: true
---

<!-- Title Slide -->
<div class="title-slide">

# DSA II — Sorting &amp; Arrays

<div class="subtitle">
Week 2 • Wednesday, September 10, 2025
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

- Implement merge sort and quicksort and verify stability and in-place properties.
- Compare time/space behavior of counting vs merge vs quicksort on synthetic data.
- Analyze partition schemes and justify worst-case behavior with adversarial inputs.

### Prerequisites
- Identify array indexing and memory layout basics.
- Describe asymptotic notation and compare n, n log n, and n^2.
- Trace simple loops and swaps.

---

<!-- Session Agenda -->
<div class="agenda">

## 📋 Session Agenda

<div class="agenda-item">
  <div class="agenda-time">16:00</div>
  <div class="agenda-activity">Warm-up: stable vs in-place (quiz) (5 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:05</div>
  <div class="agenda-activity">Partitioning &amp; stability (25 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:30</div>
  <div class="agenda-activity">Lab: implement &amp; benchmark (25 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:55</div>
  <div class="agenda-activity">Drill: array problems (20 min)</div>
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
- **Sorting**: Essential patterns and techniques
- **Arrays**: Essential patterns and techniques

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

### 0: Benchmarking lab (lab)

<div class="command-sequence">
Implement merge sort and quicksort (Lomuto or Hoare).
Generate arrays: random, sorted, reverse, and many duplicates.
Time each algorithm across sizes and input types; capture results to CSV.
Summarize which algorithm wins under which distribution and why.
</div>

⏱️ **Time allocated:** 25 minutes

---


<!-- Assessment -->
<div class="assessment-block">

## 📊 Assessment & Practice

### LeetCode Problems
<span class="leetcode-problem">912</span>
<span class="leetcode-problem">280</span>

**Instructions:** For LC 912, submit two passes: (A) merge sort; (B) quicksort with careful partition. For LC 280, document the invariant you maintain. Include time/space analysis and a 3–4 sentence note on stability/in-place trade-offs.

<div class="tip">
Time-box each problem to 25 minutes. Focus on explaining your approach clearly, even if you don't finish coding.
</div>

</div>

---

<!-- Resources -->
<div class="resources-block">

## 📚 Resources & References

### Core Resources
- **[MIT OCW 6.006 — Sorting](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/)** - Canonical analysis and implementations of sorting algorithms.
- **[Algorithm Visualizer — Sorting](https://algorithm-visualizer.org/algorithm/sorting)** - Visual intuition for stability and partitioning.
- **[Tech Interview Handbook — Sorting Patterns](https://www.techinterviewhandbook.org/algorithms/sorting/)** - Interviewer-facing tips and common pitfalls.

### Additional Learning
- [CLRS — Sorting (reference)](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/)

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

**Week 3: Hash Tables & Sliding Window**
- Hash table collision resolution strategies
- Sliding window technique for substring problems
- Time/space complexity analysis


---

<!-- Closing Slide -->
<div class="title-slide">

## Questions & Discussion

**Slack:** #swe-interview-prep
**Office Hours:** Wednesdays 3:00-4:00 PM
**Next Session:** Week 3 • September 17

### Keep Practicing! 🚀

*Remember: Consistency beats intensity. Practice a little every day.*

</div>
