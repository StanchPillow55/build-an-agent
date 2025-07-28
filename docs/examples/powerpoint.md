# PowerPoint Generation Examples

Learn how to generate comprehensive PowerPoint presentations from curriculum plans using the Educator Agent's slide generation capabilities.

## Basic PowerPoint Generation

### Simple Presentation

Generate a PowerPoint presentation alongside your curriculum:

```bash
cd code
python -m educator_agent \
  --grade "8th Grade" \
  --subject "Environmental Science" \
  --pptx "ecosystem_lesson.pptx"
```

This creates a complete presentation with:
- **Title slide** with lesson information
- **Learning objectives slide** 
- **Content slides** for each curriculum section  
- **Assessment slide** with suggested activities
- **Automatically sourced images** for visual appeal

### Custom Presentation Path

Specify a custom output path for your presentation:

```bash
python -m educator_agent \
  --grade "5th Grade" \
  --subject "Mathematics" \
  --baseline "basic arithmetic" \
  --constraints "visual-learning,hands-on-activities" \
  --pptx "presentations/math_lesson_grade5.pptx"
```

## Advanced Features

### Complete Educational Package

Generate curriculum, PowerPoint, speaker notes, and package everything:

```bash
python -m educator_agent \
  --grade "8th Grade" \
  --subject "Environmental Science" \
  --baseline "No prior knowledge of ecosystems" \
  --constraints "PII-safe,simple-language,visual-learning" \
  --pptx "lesson.pptx" \
  --notes \
  --zip "complete_package.zip"
```

**Package Contents:**
- `curriculum_plan.json` - Structured curriculum data
- `lesson.pptx` - PowerPoint presentation
- `speaker_notes.md` - Detailed teaching notes
- `metadata.json` - Generation parameters and timestamps

### Batch Presentation Generation

Create presentations for multiple subjects:

```bash
#!/bin/bash
# generate_presentations.sh

subjects=("Biology" "Chemistry" "Physics" "Earth Science")
grade="9th Grade"

mkdir -p presentations

for subject in "${subjects[@]}"; do
    echo "Generating presentation for $subject..."
    
    python -m educator_agent \
        --grade "$grade" \
        --subject "$subject" \
        --constraints "age-appropriate,visual-learning,lab-activities" \
        --pptx "presentations/${subject,,}_${grade// /_}.pptx" \
        --quiet
    
    echo "✅ $subject presentation complete"
done

echo "🎉 All presentations generated in presentations/ directory"
```

## Python API Usage

### Programmatic Slide Generation

Generate presentations from Python code:

```python
from code.educator_agent import plan_curriculum
from code.educator_agent.slide_generator import create_deck
import os

# Generate curriculum
params = {
    "grade_level": "7th Grade",
    "subject": "World History",
    "baseline": "basic geography knowledge",
    "constraints": ["visual-learning", "timeline-based", "map-activities"],
    "duration": "50 minutes"
}

try:
    # Create curriculum plan
    curriculum = plan_curriculum(params)
    print(f"✅ Generated curriculum: {curriculum['lesson_title']}")
    
    # Create PowerPoint presentation
    output_path = "history_lesson.pptx"
    create_deck(curriculum, output_path)
    print(f"✅ Created presentation: {output_path}")
    
    # Verify file was created
    if os.path.exists(output_path):
        file_size = os.path.getsize(output_path) / 1024  # KB
        print(f"📊 Presentation size: {file_size:.1f} KB")
    
except Exception as e:
    print(f"❌ Error generating presentation: {e}")
```

### Custom Slide Configuration

Customize presentation generation with specific parameters:

```python
from code.educator_agent.slide_generator import create_deck
import json

# Load existing curriculum
with open("curriculum.json", "r") as f:
    curriculum = json.load(f)

# Custom slide generation options
slide_options = {
    "include_images": True,
    "image_style": "educational",
    "slide_layout": "content_with_caption",
    "color_scheme": "professional"
}

# Generate with custom options
try:
    create_deck(
        curriculum, 
        "custom_lesson.pptx",
        **slide_options
    )
    print("✅ Custom presentation generated")
except Exception as e:
    print(f"❌ Generation failed: {e}")
```

## Presentation Structure

### Default Slide Layout

Generated presentations follow this structure:

1. **Title Slide**
   - Lesson title
   - Grade level and subject
   - Duration
   - Generated timestamp

2. **Learning Objectives**
   - Bulleted list of objectives
   - Visual icons for engagement
   - Clear, measurable goals

3. **Content Slides** (one per curriculum section)
   - Section title as slide header
   - Detailed description
   - Relevant educational images
   - Key concepts highlighted

4. **Assessment Slide**
   - List of suggested assessments
   - Mix of formative and summative options
   - Implementation guidance

5. **Conclusion/Summary**
   - Key takeaways
   - Next steps
   - Additional resources

### Slide Content Examples

#### Title Slide
```
Introduction to Environmental Science
8th Grade Science | 45 minutes

Generated on: [timestamp]
```

#### Learning Objectives Slide
```
Learning Objectives

By the end of this lesson, students will:
• Define what an ecosystem is
• Identify biotic and abiotic factors  
• Explain food chains and energy flow
• Analyze human impact on ecosystems
```

#### Content Slide Example
```
What is an Ecosystem?

An ecosystem is a community of living organisms 
interacting with their physical environment.

Key Components:
• Producers (plants)
• Primary consumers (herbivores)
• Secondary consumers (carnivores)
• Decomposers (bacteria, fungi)

[Educational image: Forest ecosystem diagram]
```

## Image Integration

### Automatic Image Sourcing

The slide generator automatically adds relevant educational images:

- **Subject-appropriate**: Images match the lesson topic
- **Age-appropriate**: Suitable for the target grade level
- **Educational quality**: Clear, informative visuals
- **Copyright-safe**: Uses appropriate image sources

### Image Placement

Images are intelligently placed based on content:
- **Title slides**: Subject-themed background or icon
- **Content slides**: Relevant diagrams, photos, or illustrations
- **Assessment slides**: Activity-related visuals

## Microsoft Copilot Integration

### OneDrive Export

Export presentations directly to Microsoft OneDrive:

```bash
python -m educator_agent \
  --grade "8th Grade" \
  --subject "Environmental Science" \
  --copilot
```

**Prerequisites:**
1. Microsoft 365 EDU account
2. Azure app registration with Graph API permissions:
   - `Files.ReadWrite.All`
   - `Sites.ReadWrite.All`
3. Environment variables in `.env`:
   ```
   MS_CLIENT_ID=your_azure_app_client_id
   MS_TENANT_ID=your_azure_tenant_id  
   MS_CLIENT_SECRET=your_azure_app_client_secret
   ```

### Copilot Workflow

The Copilot integration:
1. Generates curriculum and presentation locally
2. Authenticates with Microsoft Graph API
3. Uploads presentation to OneDrive
4. Provides sharing link for collaboration
5. Optionally creates Teams meeting with presentation

```python
from code.educator_agent.copilot_pptx import export_to_onedrive

# Export existing presentation
try:
    result = export_to_onedrive("lesson.pptx", "Environmental Science Lesson")
    print(f"✅ Uploaded to OneDrive: {result['share_url']}")
except Exception as e:
    print(f"❌ Upload failed: {e}")
```

## Troubleshooting

### Common Issues

#### Large File Sizes
```python
# Problem: Presentations are too large
import os

def check_file_size(filepath, max_size_mb=25):
    if os.path.exists(filepath):
        size_mb = os.path.getsize(filepath) / (1024 * 1024)
        if size_mb > max_size_mb:
            print(f"⚠️ Large file: {size_mb:.1f}MB (limit: {max_size_mb}MB)")
            return False
    return True

# Solution: Optimize image settings
slide_options = {
    "include_images": True,
    "compress_images": True,
    "max_image_size": "medium"
}
```

#### Missing Images
```python
# Problem: Slides have placeholder images
def verify_images(pptx_path):
    from pptx import Presentation
    
    prs = Presentation(pptx_path)
    image_count = 0
    
    for slide in prs.slides:
        for shape in slide.shapes:
            if hasattr(shape, "image"):
                image_count += 1
    
    print(f"📊 Found {image_count} images in presentation")
    return image_count > 0

# Solution: Check internet connection and image sources
```

#### PowerPoint Compatibility
```python
# Problem: Presentation won't open in older PowerPoint versions
# Solution: Use compatibility mode
slide_options = {
    "format_version": "2016",  # Compatible with PowerPoint 2016+
    "use_legacy_layouts": True
}
```

### Best Practices

1. **Test Locally**: Always generate and review presentations locally first
2. **Check File Sizes**: Monitor presentation sizes for email/upload limits  
3. **Verify Images**: Ensure all images loaded correctly
4. **Review Content**: Check for appropriate language and concepts
5. **Save Copies**: Keep backup copies of successful generations

## Integration with Other Tools

### Speaker Notes Integration

Combine PowerPoint generation with speaker notes:

```bash
python -m educator_agent \
  --grade "6th Grade" \
  --subject "Ancient Civilizations" \
  --pptx "civilizations.pptx" \
  --notes \
  --zip "complete_lesson.zip"
```

This creates a comprehensive teaching package with synchronized content.

### Learning Management System Export

Export for use in LMS platforms:

```python
# Generate presentation with LMS-friendly settings
slide_options = {
    "format": "pptx",
    "include_notes": True,
    "export_images": True,
    "scorm_compatible": True
}

create_deck(curriculum, "lms_lesson.pptx", **slide_options)
```

## Next Steps

- Learn about [content sanitization](sanitizer.md) for safer presentations
- Explore [curriculum examples](curriculum.md) for more lesson ideas
- Check the [API Reference](../api.md) for detailed slide generation functions
