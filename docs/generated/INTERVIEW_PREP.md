# 🎯 Interview Prep - Build-An-Agent (Educator Agent)

**Last Updated:** 2026-04-29

---

## 60-90 Second STAR Pitch

### Situation
Educators need efficient tools to create curriculum plans, presentations, and teaching materials, but existing solutions require manual assembly.

### Task
Build an AI-powered curriculum planning agent with constraint enforcement, multi-format export, and integration with educational platforms.

### Action
- Created **Educator Agent CLI** with interactive wizard mode using Typer + Rich
- Integrated **OpenAI GPT-4o** with JSON schema validation for consistent output
- Built **PowerPoint generation** with python-pptx and automatic image sourcing
- Added **OER Commons integration** for open educational resources
- Implemented **Microsoft Copilot/Graph API** export to OneDrive
- Developed comprehensive **MkDocs documentation** with auto-generated API reference

### Result

| Feature | Status | Evidence |
|---------|--------|----------|
| Interactive CLI wizard | **Confirmed** | Typer prompts + Rich progress |
| PowerPoint generation | **Confirmed** | `--pptx` flag |
| Speaker notes | **Confirmed** | `--notes` flag |
| OER integration | **Confirmed** | `--oer` flag |
| Copilot export | **Confirmed** | `--copilot` flag |
| Full test coverage | **Confirmed** | `pytest -q` passing |

---

## Technical Deep Dive

### Architecture
- **CLI:** Typer + Rich for interactive prompts and output
- **LLM:** OpenAI GPT-4o with structured JSON output
- **Export:** python-pptx for slides, Markdown for notes
- **Integrations:** OER Commons API, Microsoft Graph API
- **Docs:** MkDocs with mkdocstrings for API reference

### Key Features
- **Constraint enforcement:** Age-appropriate, privacy-protecting content
- **Fallback mode:** Works without API key for testing
- **Complete packages:** ZIP with all materials
- **JSON Schema validation:** Consistent, reliable output

---

## Drill-Down Q&A

### Q1: "How does constraint enforcement work?"

**Answer (Confirmed):** Built-in constraints (age-appropriate, privacy-protecting) are injected into prompts. Custom constraints can be added via `--constraints` flag. JSON schema validation ensures output compliance.

### Q2: "How do you generate PowerPoint slides?"

**Answer (Confirmed):** Uses python-pptx library. Creates slides from curriculum sections, adds images via web search, formats with consistent styling.

### Q3: "What's the OER integration?"

**Answer (Confirmed):** Live search against OER Commons API. Fetches open educational resources matching the subject, integrates into curriculum plan.

### Q4: "How does Microsoft Copilot export work?"

**Answer (Confirmed):** Uses Microsoft Graph API with device code flow authentication. Uploads generated PPTX directly to OneDrive. Requires Azure app registration.

---

## Quick Reference

| Topic | Evidence |
|-------|----------|
| CLI flags | `README.md:147-163` |
| Features | `README.md:175-186` |
| Testing | `pytest -q` |
| Documentation | MkDocs at GitHub Pages |
