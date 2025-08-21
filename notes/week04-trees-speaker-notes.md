# Speaker Notes: Balanced Trees & Heaps

**Date:** 2025-09-25
**Duration:** 90 minutes
**Week:** 4

## Session Overview
- **Objectives:** 3 learning objectives
- **Activities:** 1 hands-on activities
- **Assessment:** 1 assessment items

## Timing & Agenda
- **16:00** (10 min): Warm-up: BST vs balanced BST\n- **16:10** (20 min): RB-tree invariants & rotations\n- **16:30** (25 min): Lab: CLI visualizer + heaps\n- **16:55** (20 min): Drill: median stream\n- **17:15** (5 min): Wrap up session

## Speaker Beats
1. BSTs degrade without balancing; invariants prevent skew.\n2. RB-tree fix-up patterns: recolor vs rotate.\n3. Median of stream: two heaps maintain balance.\n4. Interview: narrate invariants and rotation effects.\n5. Trade-offs: AVL stricter balance vs RB fewer rotations.

## Demo Steps
1. Insert a key causing a red-red violation; fix it.\n2. Show heap push/pop and median update.

## Time Cues
- **Minute 10:** draw RB cases.\n- **Minute 30:** begin visualizer; show a rotation log.\n- **Minute 65:** switch to heap median drill.

## FAQ Preparation
**Q:** Why RB over AVL in libraries?\n**A:** Fewer rotations on updates; better constants in many workloads.\n\n**Q:** Is heap median always O(log n)?\n**A:** Yes per insert; O(1) to read median with two heaps.\n

## Resources for Reference
- [MIT OCW 6.006 — Balanced BSTs & Heaps](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/) - Grounding theory with practical operations and complexity.\n- [Algorithm Visualizer — Heaps](https://algorithm-visualizer.org/) - See heapify and sift-up/down dynamics.\n- [Tech Interview Handbook — Trees](https://www.techinterviewhandbook.org/algorithms/trees/) - Interview cues and common invariants to state.

## Assessment Details
- **LeetCode Problems:** 98, 230\n  Instructions: For LC 98, state the invariant (BST via in-order monotonicity or bounds). For LC 230, compare inorder vs heap approaches and justify time/space trade-offs.

---
*Generated from week04-trees.md*
