# Speaker Notes: DSA I — Recursion & Master Theorem

**Date:** 2025-09-04
**Duration:** 90 minutes
**Week:** 1

## Session Overview
- **Objectives:** 5 learning objectives
- **Activities:** 1 hands-on activities
- **Assessment:** 1 assessment items

## Timing & Agenda
- **16:00** (5 min): Warm-up: 8-minute recap clip\n- **16:05** (20 min): Recursion trees: build & sum levels\n- **16:25** (15 min): Master Theorem: pick the right case\n- **16:40** (20 min): Lab: runtime estimator\n- **17:00** (25 min): Drill & wrap

## Speaker Beats
1. Tie recursion trees to geometric series; the base dominates vs leaves dominate.\n2. Case selection: compare f(n) to n^{log_b a} with a concrete numeric example.\n3. Bridge to practice: when a recurrence is messy, estimate by levels.\n4. Estimator demo proves value of empirical checks.\n5. Preview: sorting recurrences next week.

## Demo Steps
1. Expand T(n)=2T(n/2)+n into a tree and sum c·n per level.\n2. Show T(n)=3T(n/2)+n^2 as a contrasting case.\n3. Run the estimator at multiple n and produce a quick plot.

## Time Cues
- **Minute 10:** draw the first two levels of the tree live.\n- **Minute 30:** show the three cases with contrasting examples.\n- **Minute 55:** start estimator; remind to commit plots.\n- **Minute 80:** final Q&A.

## FAQ Preparation
**Q:** What if the recurrence doesn't match any clean Master Theorem case?\n**A:** Use expansion or Akra–Bazzi; for interviews, argue by upper/lower bounding.\n\n**Q:** Is divide-and-conquer always recursive in code?\n**A:** Often, but you can replace recursion with an explicit stack if needed.\n\n**Q:** Why compare to empirical curves?\n**A:** Catches constant-factor surprises and validates your mental model.\n

## Resources for Reference
- [MIT OCW 6.046 — Divide & Conquer](https://ocw.mit.edu/courses/6-046j-introduction-to-algorithms-sma-5503-fall-2005/) - Formal treatment of recurrences and tight bounds.\n- [Algorithm Visualizer — Recursion Examples](https://algorithm-visualizer.org/) - Experiment to build intuition before proving.\n- [Tech Interview Handbook — Big-O Cheatsheet](https://www.techinterviewhandbook.org/algorithms/big-o-cheatsheet/) - Quick reference for complexity when checking your solutions.

## Assessment Details
- **LeetCode Problems:** 53, 121\n  Instructions: Solve LC 53 (use divide-and-conquer Kadane variant) and LC 121 (linear scan). For LC 53, analyze whether your approach is O(n) or O(n log n) and justify with a recurrence or exchange argument.

---
*Generated from week01-recursion.md*
