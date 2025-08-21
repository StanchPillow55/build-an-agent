# Speaker Notes: Greedy & DP Mastery

**Date:** 2025-10-23
**Duration:** 90 minutes
**Week:** 8

## Session Overview
- **Objectives:** 3 learning objectives
- **Activities:** 1 hands-on activities
- **Assessment:** 1 assessment items

## Timing & Agenda
- **16:00** (10 min): Warm-up: greedy fails (counterexample)\n- **16:10** (20 min): Exchange arguments & substructure\n- **16:30** (25 min): Lab: bottom-up DP\n- **16:55** (20 min): Drill: coin change & LIS\n- **17:15** (5 min): Wrap up session

## Speaker Beats
1. Greedy is fast but fragile; find counterexamples early.\n2. DP needs a crisp state and recurrence; don't guess—derive.\n3. Proof sketch via exchange arguments builds interviewer trust.\n4. Patience sorting intuition for LIS.\n5. Compare complexities and memory footprints.

## Demo Steps
1. Walk through coin change DP table fill.\n2. Demonstrate LIS tails array updates.

## Time Cues
- **Minute 10:** present a failing greedy example.\n- **Minute 30:** start coding DP with explicit state notes.\n- **Minute 70:** compare complexities and memory.

## FAQ Preparation
**Q:** When do I choose top-down vs bottom-up?\n**A:** Top-down for sparse states and clarity; bottom-up for tight loops and memory control.\n

## Resources for Reference
- [MIT OCW 6.006 — Dynamic Programming](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/) - Foundational patterns and proofs of correctness.\n- [Algorithm Visualizer — DP](https://algorithm-visualizer.org/) - Visualize table fills and state transitions.\n- [Tech Interview Handbook — DP Patterns](https://www.techinterviewhandbook.org/algorithms/dynamic-programming/) - Interviewer-friendly recipes to structure answers.

## Assessment Details
- **LeetCode Problems:** 322, 300\n  Instructions: For LC 322, implement bottom-up DP and explain why greedy fails on certain coin systems. For LC 300, implement O(n log n) patience sorting approach and compare to O(n^2) DP.

---
*Generated from week08-greedy.md*
