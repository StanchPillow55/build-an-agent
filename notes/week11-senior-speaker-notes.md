# Speaker Notes: DevOps & Observability — CI, Tracing, SLOs

**Date:** 2025-11-12
**Duration:** 90 minutes
**Week:** 11

## Session Overview
- **Objectives:** 3 learning objectives
- **Activities:** 1 hands-on activities
- **Assessment:** 1 assessment items

## Timing & Agenda
- **16:00** (10 min): Warm-up: what SLOs buy you\n- **16:10** (20 min): CI: GH Actions pipeline\n- **16:30** (25 min): Tracing & metrics\n- **16:55** (20 min): Dashboards & alerting\n- **17:15** (5 min): Wrap up session

## Speaker Beats
1. CI builds trust; flaky tests erode it—stabilize first.\n2. Trace spans connect the dots across services.\n3. Dashboards should answer a question; avoid chart sprawl.\n4. SLOs turn reliability into a contract with users.

## Demo Steps
1. Run a PR and watch checks pass.\n2. Hit an instrumented endpoint; view traces/metrics.\n3. Cause a 500 spike; watch the alert fire.

## Time Cues
- **Minute 10:** open the workflow file live.\n- **Minute 30:** show spans in a trace viewer.\n- **Minute 65:** trigger an alert intentionally.

## FAQ Preparation
**Q:** What if I can't run Grafana locally?\n**A:** Provide screenshots from a demo stack or use a lightweight local stack.\n

## Resources for Reference
- [GitHub Actions — Testing on Pull Requests](https://docs.github.com/actions/using-workflows/events-that-trigger-workflows#pull_request) - Trigger CI on the right events with required checks.\n- [OpenTelemetry — Getting Started](https://opentelemetry.io/docs/) - Vendor-neutral tracing and metrics.\n- [Grafana — Building Dashboards](https://grafana.com/docs/grafana/latest/getting-started/) - Translate signals into actionable visuals.

## Assessment Details
- **project:** Submit a PR link showing CI status checks, a screenshot of a trace waterfall, a dashboard snapshot with p50/p95 latency, and an alert screenshot (or alert log).

---
*Generated from week11-senior.md*
