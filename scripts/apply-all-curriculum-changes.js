#!/usr/bin/env node

/**
 * Apply all curriculum compliance changes
 */

const fs = require('fs');
const path = require('path');

// Helper function to write file
function writeWeekFile(week, content) {
  const filePath = path.join(__dirname, `../curriculum/weeks/week${week.toString().padStart(2, '0')}-${week === 0 ? 'setup' :
    week === 1 ? 'recursion' :
    week === 2 ? 'sorting' :
    week === 3 ? 'hashing' :
    week === 4 ? 'trees' :
    week === 5 ? 'industry-mixer' :
    week === 6 ? 'graphs' :
    week === 7 ? 'mst' :
    week === 8 ? 'greedy' :
    week === 9 ? 'system-design' :
    week === 10 ? 'cloud' :
    week === 11 ? 'senior' :
    week === 12 ? 'devops' : 'unknown'}.yml`);
  fs.writeFileSync(filePath, content);
  console.log(`Updated week${week.toString().padStart(2, '0')}`);
}

// Week 03 - Hashing
const week03Content = `id: "week03-hashing"
title: "Hash Tables & Sliding Window"
week: 3
duration: "90 minutes"

objectives:
  - "Implement an open-addressing hash map with linear probing and proper deletion."
  - "Analyze expected probes vs load factor and evaluate resizing strategies."
  - "Apply frequency-map and sliding-window templates to solve substring problems."

agenda:
  - time: "16:00"
    activity: "Warm-up: map vs set patterns"
    duration: 5
  - time: "16:05"
    activity: "Hashing: collisions, probing, deletion"
    duration: 25
  - time: "16:30"
    activity: "Lab: build & test hash map"
    duration: 25
  - time: "16:55"
    activity: "Drill: sliding window"
    duration: 20
  - time: "17:15"
    activity: "Wrap"
    duration: 5

topics:
  - "DSA"

prior_knowledge:
  - "Trace pointer-free arrays and understand sentinel values."
  - "Explain amortized O(1) for dynamic arrays and why it matters for resizing."

activities:
  - type: "lab"
    title: "Build a lightweight hash map"
    time_minutes: 25
    steps:
      - "Implement \`put/get/delete\` with linear probing."
      - "Add tombstones to handle deletions correctly."
      - "Track load factor and trigger resize at 0.7."
      - "Write tests that simulate clustering and verify expected probe counts."

assessment:
  - type: "leetcode"
    ids: [1, 76, 438]
    instructions: "For LC 1/76/438, apply frequency-map or sliding-window templates. In your notes, identify the window invariant and explain why shrinking/expanding preserves correctness and yields O(n)."

resources:
  core:
    - title: "MIT OCW — Hashing (6.006)"
      url: "https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/"
      why: "Covers hash functions, chaining vs open addressing, and analysis."
    - title: "Algorithm Visualizer — Sliding Window"
      url: "https://algorithm-visualizer.org/"
      why: "Helps reason about window expansion/contraction."
    - title: "Tech Interview Handbook — Hash Map Patterns"
      url: "https://www.techinterviewhandbook.org/algorithms/hash-map/"
      why: "Interview-ready templates and pitfalls."
  enrichment:
    - title: "Open addressing vs chaining"
      url: "https://en.wikipedia.org/wiki/Hash_table"
      why: "Reference comparison and terminology."

speaker_notes:
  beats:
    - "Two collision families: chaining vs open addressing."
    - "Deletion is the subtle bug: tombstones keep probe sequences intact."
    - "Load factor trade-offs: memory vs expected probes."
    - "Window templates: fixed-size vs variable-size."
    - "Interview move: state the invariant out loud."
  time_cues:
    - minute: 10
      note: "draw probe sequence on whiteboard."
    - minute: 30
      note: "begin coding; remind to add tests first."
    - minute: 65
      note: "pivot to sliding window drills."
  demo_steps:
    - "Insert a cluster and show how deletion without tombstones fails."
    - "Show resizing doubles capacity and rehashes keys."
    - "Step through a window for LC 76."
  faq:
    - question: "Why not always use chaining?"
      answer: "Cache locality favors open addressing; trade-off depends on workload."
    - question: "How do I pick a good hash?"
      answer: "Use library hashes in production; in interviews, mention modulo with large primes and mixing."

style:
  theme: "hoplite"
  layout: "two-column"
  callouts: ["do", "dont"]
  slide_count_target: 22
`;

// Week 09 - System Design
const week09Content = `id: "week09-system-design"
title: "System Design Bootcamp"
week: 9
duration: "90 minutes"

objectives:
  - "Define high-level APIs and data models for a small web service."
  - "Evaluate CAP and consistency models for the core operations."
  - "Design a scaling plan using caching, sharding, and replication."
  - "Design a URL shortener and rate limiter with clear trade-offs."
  - "Present and justify design decisions under time constraints."

agenda:
  - time: "16:00"
    activity: "Warm-up: requirements triage"
    duration: 5
  - time: "16:05"
    activity: "Scaling patterns: cache, shard, replicate"
    duration: 25
  - time: "16:30"
    activity: "Design lab: URL shortener"
    duration: 25
  - time: "16:55"
    activity: "Design lab: rate limiter"
    duration: 20
  - time: "17:15"
    activity: "Share-outs & wrap"
    duration: 5

topics:
  - "System-Design"

prior_knowledge:
  - "Describe latency vs throughput and p-percentiles."
  - "Differentiate strong vs eventual consistency at a high level."

activities:
  - type: "lab"
    title: "Two-problem design studio"
    time_minutes: 45
    steps:
      - "URL shortener: define API, schema, and hash/id strategy."
      - "Sketch read/write paths with cache and DB."
      - "Rate limiter: choose algorithm (token bucket or leaky bucket) and data store."
      - "List trade-offs and failure modes; present a 2-minute defense."

assessment:
  - type: "project"
    instructions: "Submit two diagrams (URL shortener + rate limiter) with a 1-page note that states assumptions, SLOs, and two trade-offs you would revisit with more time."

resources:
  core:
    - title: "ByteByteGo — System Design Primer"
      url: "https://bytebytego.com/"
      why: "Succinct overviews of common patterns and trade-offs."
    - title: "Google SRE — Availability & SLIs"
      url: "https://sre.google/sre-book/availability-table/"
      why: "Ground design decisions in reliability targets."
    - title: "Cloudflare — Rate Limiting Concepts"
      url: "https://developers.cloudflare.com/rate-limits/about/"
      why: "Concrete designs and pitfalls from a production CDN."

speaker_notes:
  beats:
    - "Scope ruthlessly: agree on API and scale first."
    - "CAP is about trade-offs; pick consistency per operation."
    - "Caching strategy and invalidation plan up front."
    - "Defense technique: risks, mitigations, and why now vs later."
  time_cues:
    - minute: 10
      note: "quick pattern recap."
    - minute: 30
      note: "switch to shortener; enforce timeboxes."
    - minute: 75
      note: "2-minute defenses."
  demo_steps:
    - "Whiteboard a working shortener schema (id, long_url, ttl, clicks)."
    - "Walk a token-bucket timeline under burst load."
  faq:
    - question: "Do I always need a message queue?"
      answer: "No; introduce when async processing or back-pressure is required."

style:
  theme: "hoplite"
  layout: "two-column"
  callouts: ["do", "dont"]
  slide_count_target: 22
`;

// Apply updates
writeWeekFile(3, week03Content);
writeWeekFile(9, week09Content);

console.log('All critical curriculum updates applied!');
