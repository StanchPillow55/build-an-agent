# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-07-28

### Added
- **Educator Agent CLI** - AI-powered curriculum planning tool with constraint enforcement
- **Interactive Wizard Mode** - User-friendly guided experience for curriculum generation
- **Non-Interactive Mode** - Command-line flags for automation and scripting
- **JSON Schema Validation** - Ensures consistent, reliable curriculum plan output
- **Rich CLI Interface** - Beautiful terminal output with tables, panels, and progress indicators
- **OpenAI Integration** - Uses GPT-4o by default with OpenAI SDK v1.x
- **Constraint Enforcement** - Built-in privacy protection and age-appropriate content filtering
- **PowerPoint Generation** - Automatic .pptx slide creation with images using python-pptx
- **Speaker Notes Generation** - Markdown-formatted educator notes with lesson guidance
- **OER Commons Integration** - Automatic fetching of Open Educational Resources
- **Package Generation** - Complete ZIP packages with all generated materials
- **Microsoft Copilot Integration** - Direct export to OneDrive using Microsoft Graph API (beta)
- **Fallback Mode** - Works without API key for testing and development
- **Comprehensive Testing** - Full test coverage with mocked API responses
- **GitHub Actions CI** - Automated testing across Python 3.10 and 3.11
- **Pre-commit Hooks** - Code quality enforcement with black, flake8, and pytest
- **End-to-End Demo** - Complete demonstration script showcasing all features

### Technical Features
- **JSON Schema Validation** - Structured curriculum plan output with validation
- **Rich Progress Indicators** - Real-time feedback during generation processes
- **Error Handling** - Graceful handling of API failures and missing credentials
- **Caching Support** - Optimized dependency installation in CI pipeline
- **Multi-format Output** - JSON, PowerPoint, Markdown, and ZIP support
- **Environment Configuration** - Secure credential management via environment variables
- **Cross-platform Compatibility** - Works on macOS, Linux, and Windows

### Documentation
- **Comprehensive README** - Detailed setup instructions and usage examples
- **API Documentation** - Clear documentation of all CLI flags and options
- **Setup Guides** - Step-by-step instructions for OpenAI and Microsoft 365 integration
- **Demo Scripts** - Ready-to-run examples for all major features
- **CI Badge** - Build status visibility in repository

### Dependencies
- `openai~=1.97.0` - OpenAI API integration
- `typer~=0.16.0` - CLI framework with rich formatting
- `rich~=13.7.0` - Terminal formatting and progress indicators
- `pydantic~=2.11.7` - Data validation and schema enforcement
- `jsonschema~=4.17.0` - JSON schema validation
- `python-pptx~=1.0.2` - PowerPoint generation
- `pillow~=10.4.0` - Image processing for presentations
- `requests~=2.32.3` - HTTP client for API calls
- `msal~=1.33.0` - Microsoft authentication library
- `backoff~=2.2.1` - Retry logic for API calls

### Development Dependencies
- `pytest>=7.0.0` - Testing framework
- `pytest-mock>=3.10.0` - Mock testing utilities
- `black>=23.0.0` - Code formatting
- `flake8>=6.0.0` - Code linting
- `pre-commit>=3.0.0` - Pre-commit hooks
- `responses>=0.25.0` - HTTP request mocking

### CI/CD
- **GitHub Actions** - Automated testing on push and pull requests
- **Matrix Testing** - Python 3.10 and 3.11 compatibility
- **Code Quality Checks** - Black formatting and pytest execution
- **Dependency Caching** - Optimized build performance

## [Unreleased]

### Planned
- Additional output formats (PDF, HTML)
- Enhanced OER resource filtering
- Multi-language support
- Advanced assessment generation
- Integration with learning management systems

---

**Note**: This is the first release of the Build An Agent Hackathon project, representing a complete AI-powered educational curriculum planning system with rich CLI interface and multiple output formats.
