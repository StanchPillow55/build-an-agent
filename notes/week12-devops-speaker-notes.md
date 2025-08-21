# Speaker Notes: ML/AI for SWE — Small Models & Serving

**Date:** 2025-11-20
**Duration:** 90 minutes
**Week:** 12

## Session Overview
- **Objectives:** 3 learning objectives
- **Activities:** 1 hands-on activities
- **Assessment:** 1 assessment items

## Timing & Agenda
- **16:00** (10 min): Warm-up: bias vs variance\n- **16:10** (20 min): Models: regression & trees\n- **16:30** (25 min): Embeddings & search\n- **16:55** (20 min): Serving: REST endpoint\n- **17:15** (5 min): Wrap up session

## Speaker Beats
1. Bias/variance trade-off: show under/overfit curves.\n2. Embeddings turn text into vectors; cosine captures semantic proximity.\n3. Serving concerns: serialization, warm-up, concurrency.\n4. Measure before optimizing; p95 tells the real story.

## Demo Steps
1. Train and print metrics.\n2. Show a nearest-neighbors search.\n3. Spin up FastAPI; run a simple load test.

## Time Cues
- **Minute 10:** fit a tiny model live.\n- **Minute 30:** compute embeddings and run a demo query.\n- **Minute 55:** hit the REST endpoint with a client.

## FAQ Preparation
**Q:** Is GPU required?\n**A:** No; we'll use CPU-friendly models to focus on engineering and evaluation.\n

## Resources for Reference
- [Scikit-learn — Getting Started](https://scikit-learn.org/stable/getting_started.html) - Baseline models with consistent APIs for quick iteration.\n- [FastAPI — First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/) - Lightweight serving stack for model endpoints.\n- [Embeddings — Primer](https://developers.google.com/machine-learning/crash-course/embeddings/intro-to-embeddings) - Conceptual grounding before coding.

## Assessment Details
- **project:** Submit a repo link with a notebook (metrics & plots), an API server with `/predict` and `/search`, and a short latency report with one optimization you tried.

---
*Generated from week12-devops.md*
