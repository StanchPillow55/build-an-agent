# Speaker Notes: System Design Bootcamp

**Date:** 2025-10-30
**Duration:** 90 minutes
**Week:** 9

## Session Overview
- **Objectives:** 5 learning objectives
- **Activities:** 1 hands-on activities
- **Assessment:** 1 assessment items

## Timing & Agenda
- **16:00** (5 min): Warm-up: requirements triage\n- **16:05** (25 min): Scaling patterns: cache, shard, replicate\n- **16:30** (25 min): Design lab: URL shortener\n- **16:55** (20 min): Design lab: rate limiter\n- **17:15** (5 min): Share-outs & wrap

## Speaker Beats
1. Scope ruthlessly: agree on API and scale first.\n2. CAP is about trade-offs; pick consistency per operation.\n3. Caching strategy and invalidation plan up front.\n4. Defense technique: risks, mitigations, and why now vs later.

## Demo Steps
1. Whiteboard a working shortener schema (id, long_url, ttl, clicks).\n2. Walk a token-bucket timeline under burst load.

## Time Cues
- **Minute 10:** quick pattern recap.\n- **Minute 30:** switch to shortener; enforce timeboxes.\n- **Minute 75:** 2-minute defenses.

## FAQ Preparation
**Q:** Do I always need a message queue?\n**A:** No; introduce when async processing or back-pressure is required.\n

## Resources for Reference
- [ByteByteGo — System Design Primer](https://bytebytego.com/) - Succinct overviews of common patterns and trade-offs.\n- [Google SRE — Availability & SLIs](https://sre.google/sre-book/availability-table/) - Ground design decisions in reliability targets.\n- [Cloudflare — Rate Limiting Concepts](https://developers.cloudflare.com/rate-limits/about/) - Concrete designs and pitfalls from a production CDN.

## Assessment Details
- **project:** Submit two diagrams (URL shortener + rate limiter) with a 1-page note that states assumptions, SLOs, and two trade-offs you would revisit with more time.

---
*Generated from week09-system-design.md*
