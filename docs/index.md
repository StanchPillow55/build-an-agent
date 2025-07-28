# Build An Agent

[![CI](https://github.com/StanchPillow55/build-an-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/StanchPillow55/build-an-agent/actions/workflows/ci.yml)

Welcome to the **Build An Agent Hackathon**! This hands-on workshop teaches you how to create intelligent AI agents that can perform complex tasks using Large Language Models (LLMs) and tools.

## What is an AI Agent?

An AI agent is an intelligent program that can:

- **Use tools** to perform actions like web searches, API calls, and data processing
- **Maintain conversation context** across multiple interactions
- **Make decisions** about next steps based on available information
- **Handle complex multi-step workflows** autonomously

Unlike simple workflows, agents can adapt to changing requirements, choose tools dynamically, and perform complex reasoning and planning.

## The Educator Agent

The main focus of this project is the **Educator Agent** - an AI-powered curriculum planning tool that demonstrates key agent capabilities:

### 🎯 Core Features

- **Intelligent Curriculum Planning**: Generate comprehensive educational plans tailored to specific grade levels and subjects
- **Content Sanitization**: Built-in PII detection and profanity filtering for safe educational content
- **Multi-format Output**: Create PowerPoint presentations, speaker notes, and complete lesson packages
- **Rich CLI Interface**: Beautiful terminal experience with progress indicators and formatted output
- **Microsoft Integration**: Export directly to OneDrive using Microsoft Graph API

### 🔧 Architecture

The Educator Agent showcases several important agent design patterns:

- **Tool Integration**: Uses multiple tools (OpenAI API, PowerPoint generation, file operations)
- **Schema Validation**: Ensures consistent, reliable output with JSON schema validation
- **Constraint Enforcement**: Applies content policies and age-appropriate filtering
- **Error Handling**: Graceful fallbacks and robust error management
- **Testing Strategy**: Comprehensive test coverage with mocked external dependencies

## Quick Start

Get up and running in minutes:

```bash
# Clone the repository
git clone https://github.com/StanchPillow55/build-an-agent.git
cd build-an-agent

# Install dependencies
pip install -r requirements.txt

# Set up your OpenAI API key
echo "OPENAI_API_KEY=your_api_key_here" >> .env

# Generate your first curriculum
cd code
python -m educator_agent --grade "8th Grade" --subject "Environmental Science"
```

## What You'll Learn

By exploring this project, you'll understand:

### Agent Architecture
- How to structure an AI agent with multiple capabilities
- Best practices for tool integration and orchestration
- Error handling and fallback strategies

### LLM Integration
- Modern OpenAI SDK usage (v1.x)
- Prompt engineering for consistent outputs
- Response validation and parsing

### Production Considerations
- Content safety and sanitization
- Schema validation for reliable outputs
- Testing strategies for AI-powered applications
- CLI design and user experience

### Advanced Features
- Multi-format content generation
- External API integration (Microsoft Graph)
- Package and deployment strategies

## Project Components

This repository contains several key components:

| Component | Description |
|-----------|-------------|
| **Educator Agent** | Main curriculum planning agent with CLI interface |
| **Document Generation Agent** | Example agent for research and report writing |
| **Curriculum Agent** | Core curriculum planning logic |
| **Content Sanitizer** | PII detection and content filtering |
| **Test Suite** | Comprehensive testing with mocked dependencies |

## Next Steps

Ready to dive deeper? Check out:

- [**Usage Guide**](usage.md) - Detailed usage instructions and examples
- [**API Reference**](api.md) - Complete API documentation
- [**Examples**](examples/curriculum.md) - Step-by-step examples and tutorials

## Contributing

This project is part of the Build An Agent Hackathon. Contributions are welcome! Please see the repository for contribution guidelines.

## License

This project is open source and available under the MIT License.
