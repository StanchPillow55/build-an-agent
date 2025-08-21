# Speaker Notes: Graphs II — MST & SSSP

**Date:** 2025-10-16
**Duration:** 90 minutes
**Week:** 7

## Session Overview
- **Objectives:** 3 learning objectives
- **Activities:** 1 hands-on activities
- **Assessment:** 1 assessment items

## Timing & Agenda
- **16:00** (10 min): Warm-up: MST properties\n- **16:10** (20 min): Kruskal + DSU\n- **16:30** (25 min): Lab: Dijkstra with PQ\n- **16:55** (20 min): Drill: flight routes\n- **17:15** (5 min): Wrap up session

## Speaker Beats
1. MST cut & cycle properties guide correctness.\n2. Dijkstra's invariant: current PQ min has final shortest distance.\n3. Sparse vs dense: data structure choice matters.\n4. When negatives appear, pick Bellman-Ford or SPFA.

## Demo Steps
1. Trace one Kruskal run on a 6-node graph.\n2. Show PQ push/pop and distance updates.

## Time Cues
- **Minute 10:** sketch Kruskal steps.\n- **Minute 30:** start Dijkstra; highlight relaxations.\n- **Minute 70:** wrap with performance comparison.

## FAQ Preparation
**Q:** Why not Prim always?\n**A:** Prim with Fibonacci heaps has nice bounds but higher constants; implementation complexity matters.\n

## Resources for Reference
- [MIT OCW 6.006 — MST & Shortest Paths](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/) - Proof ideas and complexity guarantees for MST/SSSP.\n- [Algorithm Visualizer — Dijkstra](https://algorithm-visualizer.org/) - Intuition for relaxation and frontier growth.\n- [Tech Interview Handbook — Graph Shortest Paths](https://www.techinterviewhandbook.org/algorithms/graph/) - Patterns and pitfalls to mention aloud.

## Assessment Details
- **LeetCode Problems:** 743, 787\n  Instructions: For LC 743, implement Dijkstra with a PQ; justify complexity O(E log V). For LC 787, discuss why simple Dijkstra fails and how you modified the state (stops constraint).

---
*Generated from week07-mst.md*
