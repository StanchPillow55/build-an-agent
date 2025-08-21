# Speaker Notes: Setup & Baseline

**Date:** 2025-08-28
**Duration:** 90 minutes
**Week:** 0

## Session Overview
- **Objectives:** 5 learning objectives
- **Activities:** 1 hands-on activities
- **Assessment:** 1 assessment items

## Timing & Agenda
- **16:00** (5 min): Welcome, goals, success criteria\n- **16:05** (25 min): IDE configuration & workspace conventions\n- **16:30** (25 min): Git workflow: branch → commit → PR\n- **16:55** (20 min): Testing harness: run & debug\n- **17:15** (15 min): Baseline drill & wrap

## Speaker Beats
1. State outcome: a reproducible local dev environment + a passing test harness.\n2. Justify Git branching: isolates work and accelerates code review.\n3. Testing payoff: confidence to refactor later weeks without fear.\n4. Baseline rationale: measure to improve; we'll compare again in Week 12.\n5. Homework hand-in: PR with checklist so TAs can spot issues quickly.

## Demo Steps
1. Show installing extensions from a shared `.vscode/extensions.json`.\n2. Create `feat/baseline-setup` branch; commit a README tweak.\n3. Add a trivial unit test; run watcher; fix a failing assertion.\n4. Open a draft PR and tag it with labels.

## Time Cues
- **Minute 10:** transition to IDE setup demo.\n- **Minute 30:** start Git workflow mini-lab.\n- **Minute 55:** run tests and show a failing → passing cycle.\n- **Minute 75:** start baseline drill; remind to record time.

## FAQ Preparation
**Q:** Why not use global Node installations per project?\n**A:** Project-local toolchains avoid version drift; lock files become trustworthy.\n\n**Q:** What if tests are flaky on my machine?\n**A:** Check Node version, lockfile, and ensure no reliance on wall-clock or randomness.\n\n**Q:** How much detail is expected in baseline notes?\n**A:** 3–5 sentences per problem: approach, big-O, and one improvement you'll try next time.\n

## Resources for Reference
- [VS Code — Getting Started](https://code.visualstudio.com/docs) - Step-by-step setup and extension management for a consistent dev environment.\n- [Atlassian — Git Branching Workflows](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) - Clear patterns for feature/release/hotfix flows used in industry.\n- [GitHub Actions — Quickstart](https://docs.github.com/actions/quickstart) - Foundation for CI that you will extend in DevOps weeks.

## Assessment Details
- **LeetCode Problems:** 53, 121\n  Instructions: Solve LC 53 and LC 121 locally. For each, commit: (1) a tested solution; (2) a 3–5 sentence note that explains the approach and time/space complexity; (3) a short note on your elapsed time and what slowed you down.

---
*Generated from week00-setup.md*
