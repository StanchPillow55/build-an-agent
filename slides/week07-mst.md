---
marp: true
theme: academic
class:


paginate: true
---

<!-- Title Slide -->
<div class="title-slide">

# Graphs II — MST &amp; SSSP

<div class="subtitle">
Week 7 • Wednesday, October 15, 2025
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

- Implement Kruskal&#x27;s algorithm with DSU and prove the cut property informally.
- Implement Dijkstra with a binary heap and analyze heap operations.
- Compare Prim vs Kruskal on sparse vs dense graphs and justify choice.

### Prerequisites
- Compute big-O for sorting edges and union/find operations.
- Explain negative edge constraints for SSSP.

---

<!-- Session Agenda -->
<div class="agenda">

## 📋 Session Agenda

<div class="agenda-item">
  <div class="agenda-time">16:00</div>
  <div class="agenda-activity">Warm-up: MST properties (10 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:10</div>
  <div class="agenda-activity">Kruskal + DSU (20 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:30</div>
  <div class="agenda-activity">Lab: Dijkstra with PQ (25 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:55</div>
  <div class="agenda-activity">Drill: flight routes (20 min)</div>
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
- **Graphs**: Essential patterns and techniques

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

### 0: Implement SSSP and MST (lab)

<div class="command-sequence">
Code Kruskal with DSU; verify spanning property and acyclicity.
Implement Dijkstra with a binary heap; log relaxations.
Generate sparse vs dense graphs and compare run times.
Write a short summary: which algorithm wins and why.
</div>

⏱️ **Time allocated:** 25 minutes

---


<!-- Assessment -->
<div class="assessment-block">

## 📊 Assessment & Practice

### LeetCode Problems
<span class="leetcode-problem">743</span>
<span class="leetcode-problem">787</span>

**Instructions:** For LC 743, implement Dijkstra with a PQ; justify complexity O(E log V). For LC 787, discuss why simple Dijkstra fails and how you modified the state (stops constraint).

<div class="tip">
Time-box each problem to 25 minutes. Focus on explaining your approach clearly, even if you don't finish coding.
</div>

</div>

---

<!-- Resources -->
<div class="resources-block">

## 📚 Resources & References

### Core Resources
- **[MIT OCW 6.006 — MST &amp; Shortest Paths](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/)** - Proof ideas and complexity guarantees for MST/SSSP.
- **[Algorithm Visualizer — Dijkstra](https://algorithm-visualizer.org/)** - Intuition for relaxation and frontier growth.
- **[Tech Interview Handbook — Graph Shortest Paths](https://www.techinterviewhandbook.org/algorithms/graph/)** - Patterns and pitfalls to mention aloud.

### Additional Learning
- [6.851 — Advanced Data Structures (for PQ variants)](https://ocw.mit.edu/courses/6-851-advanced-data-structures-spring-2012/)

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

**Week 8: Greedy vs Dynamic Programming**
- When to choose greedy vs DP approaches
- Classical DP patterns (knapsack, LCS, coin change)
- Optimization techniques and space complexity


---

<!-- Closing Slide -->
<div class="title-slide">

## Questions & Discussion

**Slack:** #swe-interview-prep
**Office Hours:** Wednesdays 3:00-4:00 PM
**Next Session:** Week 8 • October 22

### Keep Practicing! 🚀

*Remember: Consistency beats intensity. Practice a little every day.*

</div>
