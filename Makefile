# Build An Agent - Makefile

.PHONY: help docs docs-serve docs-build docs-deploy test install clean

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

# Documentation targets
docs: docs-serve  ## Serve documentation locally (alias for docs-serve)

docs-serve:  ## Serve documentation locally with auto-reload
	@echo "Starting MkDocs development server..."
	@echo "Visit http://127.0.0.1:8000 to view the documentation"
	mkdocs serve

docs-build:  ## Build documentation for production
	@echo "Building documentation..."
	mkdocs build
	@echo "Documentation built in site/ directory"

docs-deploy:  ## Deploy documentation to GitHub Pages
	@echo "Deploying documentation to GitHub Pages..."
	mkdocs gh-deploy --force

# Development targets
install:  ## Install project dependencies
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

test:  ## Run test suite
	pytest tests/ -v

test-coverage:  ## Run tests with coverage report
	pytest tests/ --cov=code --cov-report=html --cov-report=term

# Utility targets
clean:  ## Clean build artifacts
	rm -rf site/
	rm -rf htmlcov/
	rm -rf .pytest_cache/
	rm -rf __pycache__/
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete

demo:  ## Run the end-to-end demo
	bash scripts/demo_end_to_end.sh

# Educator Agent CLI shortcuts
curriculum:  ## Generate sample curriculum (requires grade and subject args)
	cd code && python -m educator_agent --grade "$(grade)" --subject "$(subject)"

curriculum-full:  ## Generate complete package with PowerPoint and notes
	cd code && python -m educator_agent \
		--grade "8th Grade" \
		--subject "Environmental Science" \
		--pptx "sample_lesson.pptx" \
		--notes \
		--zip "complete_package.zip"
