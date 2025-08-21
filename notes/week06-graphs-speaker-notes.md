# Speaker Notes: Graphs I — BFS/DFS & Union-Find

**Date:** 2025-10-09
**Duration:** 90 minutes
**Week:** 6

## Session Overview
- **Objectives:** 3 learning objectives
- **Activities:** 1 hands-on activities
- **Assessment:** 1 assessment items

## Timing & Agenda
- **16:00** (10 min): Warm-up: graph reps (adj list vs matrix)\n- **16:10** (20 min): BFS/DFS patterns\n- **16:30** (25 min): Lab: DSU with tests\n- **16:55** (20 min): Drill: grid + course schedule\n- **17:15** (5 min): Wrap up session

## Speaker Beats
1. Representation impacts complexity and memory.\n2. BFS for shortest unweighted paths; DFS for reachability/topology.\n3. DSU excels at dynamic connectivity and cycle checks.\n4. Trade-offs: recursion depth vs explicit stacks.

## Demo Steps
1. Show path compression effect with a before/after depth.\n2. Demonstrate cycle detection with DSU.

## Time Cues
- **Minute 10:** draw queue/stack transitions.\n- **Minute 30:** begin DSU coding; stress tests first.\n- **Minute 70:** recap and link to MST next week.

## FAQ Preparation
**Q:** When not to use DSU?\n**A:** When you need actual paths or topological ordering.\n

## Resources for Reference
- [MIT OCW — Graph Traversals](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/) - Connect representation choices to traversal complexity.\n- [Algorithm Visualizer — Graphs](https://algorithm-visualizer.org/) - See queue/stack behavior for BFS/DFS.\n- [Tech Interview Handbook — Graph Patterns](https://www.techinterviewhandbook.org/algorithms/graph/) - Common interview prompts and templates.

## Assessment Details
- **LeetCode Problems:** 200, 207, 684\n  Instructions: For LC 200, use BFS/DFS and justify O(V+E). For LC 207 and 684, compare DSU vs graph traversal and explain which strategy you chose and why.

---
*Generated from week06-graphs.md*
