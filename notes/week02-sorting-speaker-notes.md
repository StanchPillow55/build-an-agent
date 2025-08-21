# Speaker Notes: DSA II — Sorting & Arrays

**Date:** 2025-09-11
**Duration:** 90 minutes
**Week:** 2

## Session Overview
- **Objectives:** 3 learning objectives
- **Activities:** 1 hands-on activities
- **Assessment:** 1 assessment items

## Timing & Agenda
- **16:00** (5 min): Warm-up: stable vs in-place (quiz)\n- **16:05** (25 min): Partitioning & stability\n- **16:30** (25 min): Lab: implement & benchmark\n- **16:55** (20 min): Drill: array problems\n- **17:15** (5 min): Wrap up session

## Speaker Beats
1. Define stability with a counterexample; why it matters for composite keys.\n2. Partition choice drives performance; pivot selection heuristics.\n3. Counting sort assumptions and memory trade-offs.\n4. Benchmark results: don't trust a single dataset.\n5. Interview moves: articulate invariant + complexity succinctly.

## Demo Steps
1. Show a stable vs non-stable sequence with equal keys.\n2. Walk through Hoare partition on a small array.\n3. Run a quick benchmark script and display a simple chart.

## Time Cues
- **Minute 10:** demo stability vs non-stable swap.\n- **Minute 30:** start coding; circulate for partition bugs.\n- **Minute 70:** gather results; ask for one surprising case.

## FAQ Preparation
**Q:** Is three-way partitioning worth it?\n**A:** Yes for many duplicates; reduces to linear on identical elements.\n\n**Q:** When is counting sort appropriate?\n**A:** Small integer ranges where O(n+k) and memory k is acceptable.\n

## Resources for Reference
- [MIT OCW 6.006 — Sorting](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/) - Canonical analysis and implementations of sorting algorithms.\n- [Algorithm Visualizer — Sorting](https://algorithm-visualizer.org/algorithm/sorting) - Visual intuition for stability and partitioning.\n- [Tech Interview Handbook — Sorting Patterns](https://www.techinterviewhandbook.org/algorithms/sorting/) - Interviewer-facing tips and common pitfalls.

## Assessment Details
- **LeetCode Problems:** 912, 280\n  Instructions: For LC 912, submit two passes: (A) merge sort; (B) quicksort with careful partition. For LC 280, document the invariant you maintain. Include time/space analysis and a 3–4 sentence note on stability/in-place trade-offs.

---
*Generated from week02-sorting.md*
