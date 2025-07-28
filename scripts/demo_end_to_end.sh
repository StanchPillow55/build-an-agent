#!/usr/bin/env bash
set -e

echo "🎓 Educator Agent - End-to-End Demo"
echo "====================================="

# Ensure virtual environment is active (if it exists)
if [[ "$VIRTUAL_ENV" == "" ]] && [[ -f ".venv/bin/activate" ]]; then
    echo "📦 Activating virtual environment..."
    source .venv/bin/activate
elif [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "📦 Using system Python environment..."
fi

# Navigate to code directory
cd code

echo "🚀 Generating comprehensive curriculum package..."
echo "Parameters:"
echo "  - Grade Level: 8th"
echo "  - Subject: Environmental Science"
echo "  - Baseline: No prior knowledge of ecosystems"
echo "  - Constraints: PII-safe, simple language"
echo ""

# Run the educator agent with all features
python -m educator_agent \
    --grade "8th" \
    --subject "Environmental Science" \
    --baseline "No prior knowledge of ecosystems" \
    --constraints "PII-safe, simple language" \
    --pptx ../demo_deck.pptx \
    --notes \
    --zip ../demo_package.zip

echo ""
echo "🎉 Demo completed successfully!"
echo ""
echo "Generated files:"
echo "  📊 demo_deck.pptx - PowerPoint presentation"
echo "  📝 Speaker notes markdown file"
echo "  📦 demo_package.zip - Complete curriculum package"
