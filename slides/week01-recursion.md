---
marp: true
theme: academic
class:


paginate: true
---

<!-- Title Slide -->
<div class="title-slide">

# DSA I — Recursion &amp; Master Theorem

<div class="subtitle">
Week 1 • Wednesday, September 3, 2025
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

- Analyze divide-and-conquer recurrences using recursion trees.
- Apply Master Theorem cases to compute tight asymptotic bounds.
- Implement a small runtime estimator to compare theory vs. measurements.
- Prove a bound for T(n)&#x3D;2T(n/2)+cn using tree summation.
- Compare recursion and iteration trade-offs for stack depth and readability.

### Prerequisites
- Define big-O, big-Ω, and big-Θ.
- Identify base case and recursive case in simple code.
- Trace stack frames for a recursive function.

---

<!-- Session Agenda -->
<div class="agenda">

## 📋 Session Agenda

<div class="agenda-item">
  <div class="agenda-time">16:00</div>
  <div class="agenda-activity">Warm-up: 8-minute recap clip (5 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:05</div>
  <div class="agenda-activity">Recursion trees: build &amp; sum levels (20 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:25</div>
  <div class="agenda-activity">Master Theorem: pick the right case (15 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">16:40</div>
  <div class="agenda-activity">Lab: runtime estimator (20 min)</div>
</div>
<div class="agenda-item">
  <div class="agenda-time">17:00</div>
  <div class="agenda-activity">Drill &amp; wrap (25 min)</div>
</div>

</div>

<div class="tip">
Labor Day week - confirm attendance
</div>

---

<!-- Key Concepts Overview -->
## 🧠 Key Concepts


<div class="two-column">
<div class="column">

### Core Data Structures & Algorithms
- **DSA**: Essential patterns and techniques
- **Recursion**: Essential patterns and techniques

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

<!-- Industry Relevance -->
<div class="career">

## 🚀 Quality Over Quantity in Interview Practice

- Solve 50-100 problems deeply rather than 500 problems superficially
- Practice explaining your approach out loud - communication matters as much as coding
- Time yourself but don&#x27;t stress about speed initially - correctness and clarity first
- Keep a problem journal noting patterns and techniques that repeatedly appear
- Join hackathons to practice under pressure and build portfolio projects

*Source: Success With SCE slides p.8-10*

</div>

---

<!-- Hands-On Activities -->
## 🛠️ Hands-On Activities

### 0: Estimator mini-lab (lab)

<div class="command-sequence">
Write a function that runs your algorithm at sizes n ∈ {2^10,…,2^18}.
Record runtimes and plot n vs time.
Overlay predicted growth (n, n log n, n^2) and discuss fit.
Commit a short note: which Master Theorem case matched and why.
</div>

⏱️ **Time allocated:** 20 minutes

---


<!-- Assessment -->
<div class="assessment-block">

## 📊 Assessment & Practice

### LeetCode Problems
<span class="leetcode-problem">53</span>
<span class="leetcode-problem">121</span>

**Instructions:** Solve LC 53 (use divide-and-conquer Kadane variant) and LC 121 (linear scan). For LC 53, analyze whether your approach is O(n) or O(n log n) and justify with a recurrence or exchange argument.

<div class="tip">
Time-box each problem to 25 minutes. Focus on explaining your approach clearly, even if you don't finish coding.
</div>

</div>

---

<!-- Resources -->
<div class="resources-block">

## 📚 Resources & References

### Core Resources
- **[MIT OCW 6.046 — Divide &amp; Conquer](https://ocw.mit.edu/courses/6-046j-introduction-to-algorithms-sma-5503-fall-2005/)** - Formal treatment of recurrences and tight bounds.
- **[Algorithm Visualizer — Recursion Examples](https://algorithm-visualizer.org/)** - Experiment to build intuition before proving.
- **[Tech Interview Handbook — Big-O Cheatsheet](https://www.techinterviewhandbook.org/algorithms/big-o-cheatsheet/)** - Quick reference for complexity when checking your solutions.

### Additional Learning
- [Algorithms Explained (video) — Recursion Trees](https://www.youtube.com/playlist?list&#x3D;PLLlTVphLQsuMtyeB91jyHXu5GtONlRLKR)

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

**Week 2: Sorting & Arrays**
- Master merge sort and quicksort implementations
- Array manipulation techniques and two-pointer patterns
- Stability vs. in-place sorting trade-offs


---

<!-- Closing Slide -->
<div class="title-slide">

## Questions & Discussion

**Slack:** #swe-interview-prep
**Office Hours:** Wednesdays 3:00-4:00 PM
**Next Session:** Week 2 • September 10

### Keep Practicing! 🚀

*Remember: Consistency beats intensity. Practice a little every day.*

</div>
