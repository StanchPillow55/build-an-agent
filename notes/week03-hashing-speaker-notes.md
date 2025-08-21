# Speaker Notes: Hash Tables & Sliding Window

**Date:** 2025-09-18
**Duration:** 90 minutes
**Week:** 3

## Session Overview
- **Objectives:** 3 learning objectives
- **Activities:** 1 hands-on activities
- **Assessment:** 1 assessment items

## Timing & Agenda
- **16:00** (5 min): Warm-up: map vs set patterns\n- **16:05** (25 min): Hashing: collisions, probing, deletion\n- **16:30** (25 min): Lab: build & test hash map\n- **16:55** (20 min): Drill: sliding window\n- **17:15** (5 min): Wrap up session

## Speaker Beats
1. Two collision families: chaining vs open addressing.\n2. Deletion is the subtle bug: tombstones keep probe sequences intact.\n3. Load factor trade-offs: memory vs expected probes.\n4. Window templates: fixed-size vs variable-size.\n5. Interview move: state the invariant out loud.

## Demo Steps
1. Insert a cluster and show how deletion without tombstones fails.\n2. Show resizing doubles capacity and rehashes keys.\n3. Step through a window for LC 76.

## Time Cues
- **Minute 10:** draw probe sequence on whiteboard.\n- **Minute 30:** begin coding; remind to add tests first.\n- **Minute 65:** pivot to sliding window drills.

## FAQ Preparation
**Q:** Why not always use chaining?\n**A:** Cache locality favors open addressing; trade-off depends on workload.\n\n**Q:** How do I pick a good hash?\n**A:** Use library hashes in production; in interviews, mention modulo with large primes and mixing.\n

## Resources for Reference
- [MIT OCW — Hashing (6.006)](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/) - Covers hash functions, chaining vs open addressing, and analysis.\n- [Algorithm Visualizer — Sliding Window](https://algorithm-visualizer.org/) - Helps reason about window expansion/contraction.\n- [Tech Interview Handbook — Hash Map Patterns](https://www.techinterviewhandbook.org/algorithms/hash-map/) - Interview-ready templates and pitfalls.

## Assessment Details
- **LeetCode Problems:** 1, 76, 438\n  Instructions: For LC 1/76/438, apply frequency-map or sliding-window templates. In your notes, identify the window invariant and explain why shrinking/expanding preserves correctness and yields O(n).

---
*Generated from week03-hashing.md*
