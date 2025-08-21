#!/usr/bin/env node

const fs = require('fs');
const { promisify } = require('util');
const writeFile = promisify(fs.writeFile);
const readdir = promisify(fs.readdir);
const stat = promisify(fs.stat);
const path = require('path');

const weekTemplates = {
  2: {
    id: "week02-sorting",
    title: "Sorting & Arrays",
    topics: ["DSA", "Arrays", "Sorting"],
    leetcode: [912, 280, 75]
  },
  3: {
    id: "week03-hashing",
    title: "Hash Tables & Sliding Window",
    topics: ["DSA", "Arrays"],
    leetcode: [1, 76, 438]
  },
  4: {
    id: "week04-trees",
    title: "Trees & Heaps",
    topics: ["DSA", "Trees"],
    leetcode: [104, 295, 23]
  },
  6: {
    id: "week06-graphs",
    title: "Graphs I - BFS/DFS & Union-Find",
    topics: ["DSA", "Graphs"],
    leetcode: [200, 207, 684]
  },
  7: {
    id: "week07-mst",
    title: "MST & Shortest Path",
    topics: ["DSA", "Graphs"],
    leetcode: [743, 787, 1584]
  },
  8: {
    id: "week08-greedy-dp",
    title: "Greedy vs Dynamic Programming",
    topics: ["DSA", "DP"],
    leetcode: [322, 300, 435]
  },
  10: {
    id: "week10-cloud",
    title: "Cloud & Distributed Systems",
    topics: ["Cloud", "DevOps"],
    leetcode: []
  },
  11: {
    id: "week11-senior-work-day",
    title: "Get Your Career in Gear - Senior Work Day",
    topics: ["Networking"],
    leetcode: []
  },
  12: {
    id: "week12-devops-ml",
    title: "DevOps & ML for SWE + Wrap-up",
    topics: ["DevOps", "ML"],
    leetcode: []
  }
};

function generateWeekSkeleton(weekNum, template) {
  return `id: "${template.id}"
title: "${template.title}"
week: ${weekNum}
duration: "90 minutes"

objectives:
  - "TBD: Add 4-5 learning objectives using action verbs"
  - "TBD: Focus on measurable outcomes"
  - "TBD: Connect to interview readiness"

agenda:
  - time: "16:00"
    activity: "Review and warm-up"
    duration: 10
  - time: "16:10"
    activity: "Core concept introduction"
    duration: 20
  - time: "16:30"
    activity: "Hands-on workshop"
    duration: 30
  - time: "17:00"
    activity: "Problem solving practice"
    duration: 20
  - time: "17:20"
    activity: "Assessment and wrap-up"
    duration: 10

topics:
${template.topics.map(topic => `  - "${topic}"`).join('\n')}

prior_knowledge:
  - "TBD: List 2-3 prerequisite concepts"

activities:
  - type: "demo"
    title: "TBD: Main concept demonstration"
    time_minutes: 20
    steps:
      - "TBD: Step 1"
      - "TBD: Step 2"
      - "TBD: Step 3"
  - type: "coding"
    title: "TBD: Hands-on coding practice"
    time_minutes: 30
    steps:
      - "TBD: Practice problem 1"
      - "TBD: Practice problem 2"
      - "TBD: Implementation exercise"

assessment:${template.leetcode.length > 0 ? `
  - type: "leetcode"
    ids: [${template.leetcode.join(', ')}]
    instructions: "TBD: Specific instructions for the week's focus"` : `
  - type: "project"
    project_description: "TBD: Week-appropriate project or assessment"`}

resources:
  core:
    - title: "Algorithm Visualizer"
      url: "https://algorithm-visualizer.org/"
      why: "Interactive visualization for this week's concepts"
    - title: "TBD: Add 2-3 core resources"
      url: "https://example.com"
      why: "TBD: Explain relevance"
  enrichment:
    - title: "MIT OCW 6.006"
      url: "https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/"

speaker_notes:
  beats:
    - "TBD: Key talking points for this session"
    - "TBD: Common student questions and how to address them"
    - "TBD: Connections to previous weeks and interview relevance"

industry_tip:
  title: "TBD: Career-relevant insight for this week"
  bullets:
    - "TBD: Practical advice from Success With SCE themes"
  source: "Success With SCE slides"

style:
  theme: "academic"
  layout: "single-column"
  callouts: ["tip", "career"]
  slide_count_target: 25
`;
}

async function main() {
  const weeksDir = path.join(__dirname, '../curriculum/weeks');

  for (const [weekNum, template] of Object.entries(weekTemplates)) {
    const filename = `week${weekNum.padStart(2, '0')}-${template.id.split('-')[1]}.yml`;
    const filepath = path.join(weeksDir, filename);

    // Only create if it doesn't exist
    try {
      await stat(filepath);
      console.log(`Skipping existing file: ${filename}`);
    } catch (error) {
      // File doesn't exist, create it
      const content = generateWeekSkeleton(parseInt(weekNum), template);
      await writeFile(filepath, content);
      console.log(`Generated skeleton: ${filename}`);
    }
  }

  console.log('Week skeleton generation complete!');
}

main().catch(console.error);
