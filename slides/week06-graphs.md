---
marp: true
theme: academic
class:


paginate: true
---

<!-- Title Slide -->
<div class="title-slide">

# Graphs I — BFS/DFS &amp; Union-Find

<div class="subtitle">
Week 6 • Wednesday, October 8, 2025
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

- Implement BFS and DFS traversals and compute O(V+E) complexity.
- Implement Union-Find with union-by-rank and path compression and profile ops.
- Identify cycles and connectivity using DSU and compare to DFS-based methods.

### Prerequisites
- Describe adjacency list vs adjacency matrix trade-offs.
- Trace recursion depth limits and iterative alternatives.

---

<!-- Session Agenda -->
<div class="agenda">

## 📋 Session Agenda

<div class="agenda-item">
  <div class="agenda-time">16:00</div>
  <div class="agenda-activity">Warm-up: graph reps (adj list vs matrix) (10 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:10</div>
  <div class="agenda-activity">BFS/DFS patterns (20 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:30</div>
  <div class="agenda-activity">Lab: DSU with tests (25 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:55</div>
  <div class="agenda-activity">Drill: grid + course schedule (20 min)</div>
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

### 0: DSU implementation + benchmarks (lab)

<div class="command-sequence">
Implement &#x60;find&#x60; with path compression.
Implement &#x60;union&#x60; with union-by-rank.
Generate random edges and compare performance with and without optimizations.
Add tests: cycle detection and component counting.
</div>

⏱️ **Time allocated:** 25 minutes

---


<!-- Assessment -->
<div class="assessment-block">

## 📊 Assessment & Practice

### LeetCode Problems
<span class="leetcode-problem">200</span>
<span class="leetcode-problem">207</span>
<span class="leetcode-problem">684</span>

**Instructions:** For LC 200, use BFS/DFS and justify O(V+E). For LC 207 and 684, compare DSU vs graph traversal and explain which strategy you chose and why.

<div class="tip">
Time-box each problem to 25 minutes. Focus on explaining your approach clearly, even if you don't finish coding.
</div>

</div>

---

<!-- Resources -->
<div class="resources-block">

## 📚 Resources & References

### Core Resources
- **[MIT OCW — Graph Traversals](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/)** - Connect representation choices to traversal complexity.
- **[Algorithm Visualizer — Graphs](https://algorithm-visualizer.org/)** - See queue/stack behavior for BFS/DFS.
- **[Tech Interview Handbook — Graph Patterns](https://www.techinterviewhandbook.org/algorithms/graph/)** - Common interview prompts and templates.

### Additional Learning
- [DSU Explained](https://cp-algorithms.com/data_structures/disjoint_set_union.html)

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

**Week 7: MST & Shortest Path**
- Minimum spanning trees with Kruskal's algorithm
- Dijkstra's shortest path with optimizations
- Real-world applications in networks


---

<!-- Closing Slide -->
<div class="title-slide">

## Questions & Discussion

**Slack:** #swe-interview-prep
**Office Hours:** Wednesdays 3:00-4:00 PM
**Next Session:** Week 7 • October 15

### Keep Practicing! 🚀

*Remember: Consistency beats intensity. Practice a little every day.*

</div>
