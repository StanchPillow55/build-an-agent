# Curriculum Planning Examples

This section provides practical examples and tutorials for using the Educator Agent's curriculum planning capabilities.

## Basic Examples

### Simple Curriculum Generation

Generate a basic curriculum plan for middle school science:

```bash
cd code
python -m educator_agent --grade "8th Grade" --subject "Environmental Science"
```

**Expected Output:**
```
🎓 Curriculum Planner Demo
Task 2: Advanced curriculum planning with JSON validation

📝 Input Parameters:
┌─────────────┬─────────────────────────────────────┐
│ Parameter   │ Value                               │
├─────────────┼─────────────────────────────────────┤
│ Grade Level │ 8th Grade                           │
│ Subject     │ Environmental Science               │
│ Constraints │ age-appropriate, privacy-protecting │
│ Duration    │ 45 minutes                          │
└─────────────┴─────────────────────────────────────┘

🔄 Generating curriculum plan...
✅ Plan generated and validated successfully!

📚 Lesson Title: Introduction to Environmental Science

🎯 Learning Objectives:
  1. Students will define what an ecosystem is
  2. Students will identify biotic and abiotic factors
  3. Students will explain food chains and energy flow

📖 Content Outline:
┌──────────────────────────┬─────────────────────────────────────────────────┐
│ Section                  │ Description                                     │
├──────────────────────────┼─────────────────────────────────────────────────┤
│ What is an Ecosystem?    │ Introduce the concept of ecosystems using local │
│                          │ examples                                        │
│ Living vs Non-Living     │ Explore biotic and abiotic factors through      │
│ Components               │ hands-on activities                             │
│ Energy Flow in           │ Demonstrate food chains and energy transfer     │
│ Ecosystems               │ concepts                                        │
└──────────────────────────┴─────────────────────────────────────────────────┘

📝 Suggested Assessments:
  1. Ecosystem components identification worksheet
  2. Food chain construction activity
  3. Exit ticket with key vocabulary terms
```

### Custom Parameters

Generate a more tailored curriculum with specific constraints:

```bash
python -m educator_agent \
  --grade "5th Grade" \
  --subject "Mathematics" \
  --baseline "basic arithmetic and counting" \
  --constraints "age-appropriate,hands-on-activities,no-calculators,visual-learning" \
  --duration "60 minutes" \
  --model "gpt-4"
```

This example demonstrates:
- **Grade-specific content**: Tailored to 5th grade level
- **Prerequisite knowledge**: Assumes basic arithmetic skills
- **Learning constraints**: Hands-on, visual, no technology
- **Extended duration**: 60-minute lesson plan
- **Specific model**: Uses GPT-4 instead of default

## Advanced Use Cases

### Multi-Subject Curriculum

Generate curricula for multiple subjects using a batch script:

```bash
#!/bin/bash
# batch_curriculum.sh

subjects=("Mathematics" "Science" "History" "Literature" "Art")
grade="6th Grade"

for subject in "${subjects[@]}"; do
    echo "Generating curriculum for $subject..."
    python -m educator_agent \
        --grade "$grade" \
        --subject "$subject" \
        --constraints "interdisciplinary,project-based" \
        --quiet
    echo "✅ $subject curriculum complete"
    echo "---"
done
```

### Differentiated Learning

Create curricula for different learning styles:

#### Visual Learners
```bash
python -m educator_agent \
  --grade "7th Grade" \
  --subject "Biology" \
  --constraints "visual-learning,diagrams,infographics,minimal-text"
```

#### Kinesthetic Learners
```bash
python -m educator_agent \
  --grade "7th Grade" \
  --subject "Biology" \
  --constraints "hands-on-activities,experiments,movement,tactile"
```

#### Auditory Learners
```bash
python -m educator_agent \
  --grade "7th Grade" \
  --subject "Biology" \
  --constraints "discussion-based,audio-content,storytelling,verbal-explanation"
```

## Integration Examples

### Python API Usage

Use the curriculum planner in your own Python applications:

```python
from code.educator_agent import plan_curriculum
import json

# Define curriculum parameters
params = {
    "grade_level": "9th Grade",
    "subject": "World History",
    "baseline": "basic knowledge of chronology and geography", 
    "constraints": ["age-appropriate", "culturally-sensitive", "evidence-based"],
    "duration": "50 minutes"
}

# Generate curriculum
try:
    curriculum = plan_curriculum(params)
    
    # Access specific components
    print(f"Lesson: {curriculum['lesson_title']}")
    print(f"Objectives: {len(curriculum['learning_objectives'])}")
    print(f"Sections: {len(curriculum['content_outline'])}")
    
    # Save to file
    with open("history_curriculum.json", "w") as f:
        json.dump(curriculum, f, indent=2)
        
    print("✅ Curriculum saved to history_curriculum.json")
    
except Exception as e:
    print(f"❌ Error generating curriculum: {e}")
```

### Curriculum Validation

Validate generated curricula programmatically:

```python
from code.educator_agent.curriculum_planner import validate_plan
import json

# Load existing curriculum
with open("curriculum.json", "r") as f:
    curriculum = json.load(f)

# Validate structure
try:
    validate_plan(curriculum)
    print("✅ Curriculum is valid")
except ValueError as e:
    print(f"❌ Validation error: {e}")

# Check content quality
required_sections = ["introduction", "main_content", "assessment"]
outline_titles = [section["title"].lower() for section in curriculum["content_outline"]]

missing_sections = [section for section in required_sections 
                   if not any(section in title for title in outline_titles)]

if missing_sections:
    print(f"⚠️ Missing recommended sections: {missing_sections}")
else:
    print("✅ All recommended sections present")
```

## Common Patterns

### Grade-Level Progression

Create a series of curricula that build upon each other:

```python
grade_levels = ["6th Grade", "7th Grade", "8th Grade"]
subject = "Algebra"

curricula = {}
baseline = "basic arithmetic"

for grade in grade_levels:
    params = {
        "grade_level": grade,
        "subject": subject,
        "baseline": baseline,
        "constraints": ["sequential-learning", "scaffolded-instruction"]
    }
    
    curriculum = plan_curriculum(params)
    curricula[grade] = curriculum
    
    # Update baseline for next grade
    baseline = f"knowledge from {grade} {subject}"
    
    print(f"✅ {grade} {subject} curriculum generated")

# Save progression
with open("algebra_progression.json", "w") as f:
    json.dump(curricula, f, indent=2)
```

### Seasonal/Thematic Curricula

Generate themed curricula for special occasions:

```python
themes = {
    "Fall": ["harvest", "changing-seasons", "thanksgiving"],
    "Winter": ["weather-patterns", "cultural-celebrations", "hibernation"],
    "Spring": ["growth", "renewal", "earth-day"],
    "Summer": ["exploration", "outdoor-learning", "vacation-projects"]
}

subject = "Science"
grade = "4th Grade"

for season, theme_list in themes.items():
    constraints = ["age-appropriate", "seasonal-relevance"] + theme_list
    
    params = {
        "grade_level": grade,
        "subject": f"{season} {subject}",
        "constraints": constraints,
        "duration": "45 minutes"
    }
    
    curriculum = plan_curriculum(params)
    filename = f"{season.lower()}_{subject.lower()}_curriculum.json"
    
    with open(filename, "w") as f:
        json.dump(curriculum, f, indent=2)
    
    print(f"✅ {season} {subject} curriculum saved to {filename}")
```

## Troubleshooting

### Common Issues

#### Empty or Invalid Content
```python
# Problem: Curriculum contains placeholder or invalid content
if "[REDACTED]" in str(curriculum):
    print("⚠️ Content was sanitized - may need to adjust constraints")

# Solution: Use more specific, appropriate constraints
params["constraints"] = ["educational-content-only", "no-personal-info"]
```

#### Inconsistent Difficulty Level
```python
# Problem: Content too advanced or too simple
if "college-level" in curriculum["lesson_title"].lower():
    print("⚠️ Content may be too advanced for grade level")

# Solution: Adjust baseline and add grade-specific constraints
params["baseline"] = "age-appropriate foundational knowledge"
params["constraints"].append("grade-level-appropriate")
```

#### Missing Required Components
```python
# Check for all required schema components
required_keys = ["lesson_title", "learning_objectives", "content_outline", "suggested_assessments"]
missing_keys = [key for key in required_keys if key not in curriculum]

if missing_keys:
    print(f"❌ Missing required components: {missing_keys}")
    print("Regenerating curriculum...")
    curriculum = plan_curriculum(params)
```

### Best Practices

1. **Start Simple**: Begin with basic parameters and add complexity gradually
2. **Validate Early**: Always validate curricula before using in production
3. **Test Constraints**: Experiment with different constraint combinations
4. **Save Examples**: Keep successful parameter combinations for reuse
5. **Monitor Content**: Regularly review generated content for quality

## Next Steps

- Explore [PowerPoint generation](powerpoint.md) to create presentations from curricula
- Learn about [content sanitization](sanitizer.md) for safer educational content
- Check the [API Reference](../api.md) for detailed function documentation
