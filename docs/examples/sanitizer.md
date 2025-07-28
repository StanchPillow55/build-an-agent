# Content Sanitization Examples

Learn how the Educator Agent's content sanitization system protects student privacy and ensures safe educational content.

## Overview

The content sanitizer automatically:
- **Filters profanity** using industry-standard detection
- **Redacts PII** (Personally Identifiable Information)
- **Maintains educational value** while ensuring safety
- **Applies recursively** to all generated content

## Basic Sanitization

### Automatic PII Detection

The sanitizer automatically detects and redacts various types of sensitive information:

#### Names
```python
from code.educator_agent.sanitizer import clean_text

# Full names are automatically redacted
text = "Contact John Smith or Mary Johnson for more information"
cleaned = clean_text(text)
print(cleaned)
# Output: "Contact [REDACTED] or [REDACTED] for more information"

# Single names are preserved (may be common words)
text = "John will explain the concept"
cleaned = clean_text(text)
print(cleaned)
# Output: "John will explain the concept"
```

#### Email Addresses
```python
text = "Send questions to teacher@school.edu or admin@example.com"
cleaned = clean_text(text)
print(cleaned)
# Output: "Send questions to [REDACTED] or [REDACTED]"
```

#### Phone Numbers
```python
text = "Call (555) 123-4567 or 555.123.4567 for assistance"
cleaned = clean_text(text)
print(cleaned)
# Output: "Call [REDACTED] or [REDACTED] for assistance"
```

#### Social Security Numbers
```python
text = "Submit SSN 123-45-6789 or 123456789 for verification"
cleaned = clean_text(text)
print(cleaned)
# Output: "Submit SSN [REDACTED] or [REDACTED] for verification"
```

#### Credit Card Numbers
```python
text = "Payment with card 1234-5678-9012-3456 or 1234 5678 9012 3456"
cleaned = clean_text(text)
print(cleaned)
# Output: "Payment with card [REDACTED] or [REDACTED]"
```

### Profanity Filtering

```python
text = "This is damn difficult to understand"
cleaned = clean_text(text)
print(cleaned)
# Output: "This is **** difficult to understand"

# Educational content remains unchanged
text = "Students will understand photosynthesis processes"
cleaned = clean_text(text)
print(cleaned)
# Output: "Students will understand photosynthesis processes"
```

## Curriculum Sanitization

### Complete Plan Sanitization

The sanitizer processes entire curriculum structures:

```python
from code.educator_agent.sanitizer import enforce_constraints

# Example problematic curriculum
curriculum = {
    "lesson_title": "Bob Wilson's chemistry lesson",
    "learning_objectives": [
        "Students will email professor@university.edu for help",
        "Students will call (555) 123-4567 for lab time"
    ],
    "content_outline": [
        {
            "title": "Introduction by Dr. Sarah Lee",
            "description": "Contact sarah.lee@school.org for questions"
        }
    ],
    "suggested_assessments": [
        "Submit SSN 123-45-6789 for grade verification"
    ]
}

# Apply sanitization
clean_curriculum = enforce_constraints(curriculum)
print(json.dumps(clean_curriculum, indent=2))
```

**Output:**
```json
{
  "lesson_title": "[REDACTED]'s chemistry lesson",
  "learning_objectives": [
    "Students will email [REDACTED] for help",
    "Students will call [REDACTED] for lab time"
  ],
  "content_outline": [
    {
      "title": "Introduction by Dr. [REDACTED]",
      "description": "Contact [REDACTED] for questions"
    }
  ],
  "suggested_assessments": [
    "Submit SSN [REDACTED] for grade verification"
  ]
}
```

### Preserving Educational Content

The sanitizer is designed to preserve legitimate educational content:

```python
educational_curriculum = {
    "lesson_title": "Introduction to Photosynthesis",
    "learning_objectives": [
        "Students will understand chlorophyll's role in photosynthesis",
        "Students will identify reactants and products"
    ],
    "content_outline": [
        {
            "title": "What is Photosynthesis?",
            "description": "Basic introduction to the process"
        }
    ],
    "suggested_assessments": [
        "Quiz on photosynthesis basics",
        "Lab report on leaf experiments"
    ]
}

clean_curriculum = enforce_constraints(educational_curriculum)
# All content remains unchanged - no PII or profanity detected
```

## Advanced Usage

### Custom Sanitization Patterns

Extend the sanitizer with custom patterns:

```python
from code.educator_agent.sanitizer import ContentSanitizer
import re

class CustomSanitizer(ContentSanitizer):
    def __init__(self):
        super().__init__()
        # Add custom patterns
        self.patterns.update({
            'student_ids': re.compile(r'\b\d{6,9}\b'),  # Student ID numbers
            'addresses': re.compile(r'\d+\s+\w+\s+(Street|St|Avenue|Ave|Road|Rd)\b'),
            'grades': re.compile(r'\b[A-F][+-]?\s*grade\b', re.IGNORECASE)  # Individual grades
        })

# Use custom sanitizer
custom_sanitizer = CustomSanitizer()
text = "Student 12345678 lives at 123 Main Street and received an A+ grade"
cleaned = custom_sanitizer.clean_text(text)
print(cleaned)
# Output: "Student [REDACTED] lives at [REDACTED] and received an [REDACTED]"
```

### Batch Sanitization

Process multiple curricula safely:

```python
import json
from code.educator_agent.sanitizer import enforce_constraints

# Load multiple curriculum files
curriculum_files = ['math_curriculum.json', 'science_curriculum.json', 'history_curriculum.json']
sanitized_curricula = {}

for filename in curriculum_files:
    try:
        with open(filename, 'r') as f:
            curriculum = json.load(f)
        
        # Apply sanitization
        clean_curriculum = enforce_constraints(curriculum)
        
        # Save sanitized version
        clean_filename = f"sanitized_{filename}"
        with open(clean_filename, 'w') as f:
            json.dump(clean_curriculum, f, indent=2)
        
        sanitized_curricula[filename] = clean_curriculum
        print(f"✅ Sanitized {filename} -> {clean_filename}")
        
    except Exception as e:
        print(f"❌ Error processing {filename}: {e}")

print(f"🎉 Processed {len(sanitized_curricula)} curricula")
```

## Integration Examples

### CLI Integration

The sanitizer is automatically applied in CLI usage:

```bash
# Sanitization is applied by default
python -m educator_agent \
  --grade "8th Grade" \
  --subject "Environmental Science" \
  --constraints "PII-safe,age-appropriate"
```

### PowerPoint Sanitization

Generated presentations are also sanitized:

```bash
# Both curriculum and slides are sanitized
python -m educator_agent \
  --grade "8th Grade" \
  --subject "Biology" \
  --pptx "biology_lesson.pptx" \
  --constraints "privacy-protecting,content-safe"
```

### Package Sanitization

Complete educational packages receive full sanitization:

```bash
python -m educator_agent \
  --grade "7th Grade" \
  --subject "World History" \
  --pptx "history.pptx" \
  --notes \
  --zip "safe_history_package.zip"
```

All components (curriculum JSON, PowerPoint, speaker notes) are sanitized before packaging.

## Testing and Validation

### Sanitizer Testing

Test the sanitizer with known problematic content:

```python
from code.educator_agent.sanitizer import clean_text

# Test cases with expected behavior
test_cases = [
    {
        "input": "Contact John Smith at john@example.com",
        "should_contain": ["[REDACTED]"],
        "should_not_contain": ["John Smith", "john@example.com"]
    },
    {
        "input": "This lesson is damn good for students",
        "should_contain": ["****"],
        "should_not_contain": ["damn"]
    },
    {
        "input": "Students will learn about photosynthesis",
        "should_contain": ["photosynthesis"],
        "should_not_contain": ["[REDACTED]"]
    }
]

for i, test in enumerate(test_cases):
    cleaned = clean_text(test["input"])
    
    # Check positive conditions
    for should_contain in test["should_contain"]:
        if should_contain not in cleaned:
            print(f"❌ Test {i+1} failed: Missing '{should_contain}'")
            continue
    
    # Check negative conditions
    for should_not_contain in test["should_not_contain"]:
        if should_not_contain in cleaned:
            print(f"❌ Test {i+1} failed: Contains '{should_not_contain}'")
            continue
    
    print(f"✅ Test {i+1} passed")
```

### Validation Reports

Generate sanitization reports for compliance:

```python
def generate_sanitization_report(original_curriculum, sanitized_curriculum):
    """Generate a report of what was sanitized."""
    
    def count_redactions(text):
        return str(text).count("[REDACTED]")
    
    def count_censoring(text):
        return str(text).count("*")
    
    original_text = str(original_curriculum)
    sanitized_text = str(sanitized_curriculum)
    
    report = {
        "timestamp": datetime.now().isoformat(),
        "original_length": len(original_text),
        "sanitized_length": len(sanitized_text),
        "pii_redactions": count_redactions(sanitized_text),
        "profanity_censoring": count_censoring(sanitized_text),
        "sanitization_applied": count_redactions(sanitized_text) > 0 or count_censoring(sanitized_text) > 0
    }
    
    return report

# Usage
from datetime import datetime
import json

original = load_curriculum("original.json")
sanitized = enforce_constraints(original)
report = generate_sanitization_report(original, sanitized)

print("📊 Sanitization Report")
print(f"PII Redactions: {report['pii_redactions']}")
print(f"Profanity Censoring: {report['profanity_censoring']}")
print(f"Content Safe: {'Yes' if not report['sanitization_applied'] else 'Sanitized'}")
```

## Best Practices

### Content Review

1. **Manual Review**: Always review sanitized content for educational value
2. **Context Preservation**: Ensure sanitization doesn't break educational context
3. **False Positives**: Check for over-sanitization of legitimate content

```python
def review_sanitization(original, sanitized):
    """Helper to review sanitization results."""
    
    original_str = str(original)
    sanitized_str = str(sanitized)
    
    # Check for over-sanitization
    redaction_ratio = sanitized_str.count("[REDACTED]") / len(original_str.split())
    
    if redaction_ratio > 0.1:  # More than 10% of words redacted
        print("⚠️ High redaction ratio - review for over-sanitization")
    
    # Check for broken sentences
    if "[REDACTED]'s" in sanitized_str or "[REDACTED] and [REDACTED]" in sanitized_str:
        print("⚠️ Potential grammar issues from redaction")
    
    # Verify educational terms preserved
    educational_terms = ["students", "lesson", "curriculum", "assessment", "learning"]
    for term in educational_terms:
        if term in original_str.lower() and term not in sanitized_str.lower():
            print(f"⚠️ Educational term '{term}' may have been over-sanitized")
```

### Safe Curriculum Generation

Generate curricula with built-in safety:

```python
def generate_safe_curriculum(grade, subject, **kwargs):
    """Generate curriculum with enhanced safety constraints."""
    
    # Add safety constraints
    safety_constraints = [
        "age-appropriate",
        "privacy-protecting", 
        "PII-safe",
        "content-appropriate",
        "no-personal-examples"
    ]
    
    existing_constraints = kwargs.get("constraints", [])
    kwargs["constraints"] = existing_constraints + safety_constraints
    
    # Generate and sanitize
    params = {
        "grade_level": grade,
        "subject": subject,
        **kwargs
    }
    
    curriculum = plan_curriculum(params)
    sanitized = enforce_constraints(curriculum)
    
    # Validation
    if "[REDACTED]" in str(sanitized):
        print("ℹ️ Content was sanitized for safety")
    
    return sanitized

# Usage
safe_curriculum = generate_safe_curriculum(
    "8th Grade", 
    "Environmental Science",
    baseline="no prior knowledge",
    duration="45 minutes"
)
```

## Troubleshooting

### Over-Sanitization

If legitimate content is being redacted:

```python
# Problem: Educational terms being redacted
text = "Charles Darwin developed the theory of evolution"
cleaned = clean_text(text)
# May incorrectly redact "Charles Darwin" as a name

# Solution: Use educational content constraints
params = {
    "constraints": ["educational-figures-allowed", "historical-names-preserved"]
}
```

### Under-Sanitization

If problematic content passes through:

```python
# Problem: Subtle PII not detected
text = "My teacher's initials are J.S. and lives on Oak St"

# Solution: Add custom patterns or stricter constraints
params = {
    "constraints": ["strict-privacy", "no-personal-references"]
}
```

## Next Steps

- Explore [curriculum planning](curriculum.md) with safety constraints
- Learn about [PowerPoint generation](powerpoint.md) with sanitized content
- Review the [API Reference](../api.md) for detailed sanitization functions
