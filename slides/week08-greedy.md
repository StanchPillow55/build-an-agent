---
marp: true
theme: academic
class:


paginate: true
---

<!-- Title Slide -->
<div class="title-slide">

# Greedy &amp; DP Mastery

<div class="subtitle">
Week 8 • Wednesday, October 22, 2025
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

- Transform a brute-force interval scheduling solution into a DP with optimal substructure.
- Implement bottom-up DP for coin change and LIS and compare to greedy heuristics.
- Explain correctness via exchange arguments and subproblem independence.

### Prerequisites
- Define overlapping subproblems and optimal substructure.
- Trace a 1D or 2D DP table update.

---

<!-- Session Agenda -->
<div class="agenda">

## 📋 Session Agenda

<div class="agenda-item">
  <div class="agenda-time">16:00</div>
  <div class="agenda-activity">Warm-up: greedy fails (counterexample) (10 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:10</div>
  <div class="agenda-activity">Exchange arguments &amp; substructure (20 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:30</div>
  <div class="agenda-activity">Lab: bottom-up DP (25 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:55</div>
  <div class="agenda-activity">Drill: coin change &amp; LIS (20 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">17:15</div>
  <div class="agenda-activity">Wrap up session (5 min)</div>
</div>

</div>

<div class="tip">
Graphs speaker event
</div>

---

<!-- Key Concepts Overview -->
## 🧠 Key Concepts


<div class="two-column">
<div class="column">

### Core Data Structures & Algorithms
- **DSA**: Essential patterns and techniques
- **DP**: Essential patterns and techniques

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

### 0: From greedy to DP (lab)

<div class="command-sequence">
Start with a greedy attempt; intentionally fail on a counterexample.
Define DP state, transitions, and base cases.
Implement bottom-up with a table and reconstruct the solution.
Write a 4-sentence correctness argument (exchange or induction).
</div>

⏱️ **Time allocated:** 25 minutes

---


<!-- Assessment -->
<div class="assessment-block">

## 📊 Assessment & Practice

### LeetCode Problems
<span class="leetcode-problem">322</span>
<span class="leetcode-problem">300</span>

**Instructions:** For LC 322, implement bottom-up DP and explain why greedy fails on certain coin systems. For LC 300, implement O(n log n) patience sorting approach and compare to O(n^2) DP.

<div class="tip">
Time-box each problem to 25 minutes. Focus on explaining your approach clearly, even if you don't finish coding.
</div>

</div>

---

<!-- Resources -->
<div class="resources-block">

## 📚 Resources & References

### Core Resources
- **[MIT OCW 6.006 — Dynamic Programming](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/)** - Foundational patterns and proofs of correctness.
- **[Algorithm Visualizer — DP](https://algorithm-visualizer.org/)** - Visualize table fills and state transitions.
- **[Tech Interview Handbook — DP Patterns](https://www.techinterviewhandbook.org/algorithms/dynamic-programming/)** - Interviewer-friendly recipes to structure answers.

### Additional Learning
- [6.851 — Advanced Data Structures (optional)](https://ocw.mit.edu/courses/6-851-advanced-data-structures-spring-2012/)

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

**Week 9: System Design Bootcamp**
- Scalability fundamentals and trade-offs
- URL shortener and rate limiting systems
- Database partitioning and caching strategies


---

<!-- Closing Slide -->
<div class="title-slide">

## Questions & Discussion

**Slack:** #swe-interview-prep
**Office Hours:** Wednesdays 3:00-4:00 PM
**Next Session:** Week 9 • October 29

### Keep Practicing! 🚀

*Remember: Consistency beats intensity. Practice a little every day.*

</div>
