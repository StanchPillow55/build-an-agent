#!/usr/bin/env node

/**
 * Script to apply curriculum compliance changes in bulk
 */

const fs = require('fs');
const path = require('path');

// Update week02-sorting.yml
const week02Content = `id: "week02-sorting"
title: "DSA II — Sorting & Arrays"
week: 2
duration: "90 minutes"

objectives:
  - "Implement merge sort and quicksort and verify stability and in-place properties."
  - "Compare time/space behavior of counting vs merge vs quicksort on synthetic data."
  - "Analyze partition schemes and justify worst-case behavior with adversarial inputs."

agenda:
  - time: "16:00"
    activity: "Warm-up: stable vs in-place (quiz)"
    duration: 5
  - time: "16:05"
    activity: "Partitioning & stability"
    duration: 25
  - time: "16:30"
    activity: "Lab: implement & benchmark"
    duration: 25
  - time: "16:55"
    activity: "Drill: array problems"
    duration: 20
  - time: "17:15"
    activity: "Wrap"
    duration: 5

topics:
  - "DSA"
  - "Sorting"
  - "Arrays"

prior_knowledge:
  - "Identify array indexing and memory layout basics."
  - "Describe asymptotic notation and compare n, n log n, and n^2."
  - "Trace simple loops and swaps."

activities:
  - type: "lab"
    title: "Benchmarking lab"
    time_minutes: 25
    steps:
      - "Implement merge sort and quicksort (Lomuto or Hoare)."
      - "Generate arrays: random, sorted, reverse, and many duplicates."
      - "Time each algorithm across sizes and input types; capture results to CSV."
      - "Summarize which algorithm wins under which distribution and why."

assessment:
  - type: "leetcode"
    ids: [912, 280]
    instructions: "For LC 912, submit two passes: (A) merge sort; (B) quicksort with careful partition. For LC 280, document the invariant you maintain. Include time/space analysis and a 3–4 sentence note on stability/in-place trade-offs."

resources:
  core:
    - title: "MIT OCW 6.006 — Sorting"
      url: "https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/"
      why: "Canonical analysis and implementations of sorting algorithms."
    - title: "Algorithm Visualizer — Sorting"
      url: "https://algorithm-visualizer.org/algorithm/sorting"
      why: "Visual intuition for stability and partitioning."
    - title: "Tech Interview Handbook — Sorting Patterns"
      url: "https://www.techinterviewhandbook.org/algorithms/sorting/"
      why: "Interviewer-facing tips and common pitfalls."
  enrichment:
    - title: "CLRS — Sorting (reference)"
      url: "https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/"
      why: "Deeper dive if you want proofs and exercises."

speaker_notes:
  beats:
    - "Define stability with a counterexample; why it matters for composite keys."
    - "Partition choice drives performance; pivot selection heuristics."
    - "Counting sort assumptions and memory trade-offs."
    - "Benchmark results: don't trust a single dataset."
    - "Interview moves: articulate invariant + complexity succinctly."
  time_cues:
    - minute: 10
      note: "demo stability vs non-stable swap."
    - minute: 30
      note: "start coding; circulate for partition bugs."
    - minute: 70
      note: "gather results; ask for one surprising case."
  demo_steps:
    - "Show a stable vs non-stable sequence with equal keys."
    - "Walk through Hoare partition on a small array."
    - "Run a quick benchmark script and display a simple chart."
  faq:
    - question: "Is three-way partitioning worth it?"
      answer: "Yes for many duplicates; reduces to linear on identical elements."
    - question: "When is counting sort appropriate?"
      answer: "Small integer ranges where O(n+k) and memory k is acceptable."

style:
  theme: "hoplite"
  layout: "two-column"
  callouts: ["do", "dont"]
  slide_count_target: 22
`;

// Write the content
fs.writeFileSync(path.join(__dirname, '../curriculum/weeks/week02-sorting.yml'), week02Content);
console.log('Updated week02-sorting.yml');
