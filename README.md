# Python for AI — Module 1

## Module 1 Project: AI Prompt Kit for a Clinic

A beginner-friendly Python tool that collects five clinic details and generates three ready-to-use AI prompts for marketing, patient customer service, and low-cost clinic growth.

### Features

- Collects basic business information from the user.
- Generates a healthcare marketing prompt.
- Generates a patient customer service prompt.
- Generates a clinic growth prompt with budget considerations.
- Includes safety instructions for healthcare-related content.

### Requirements

- Python 3.11 or compatible version
- `uv` package manager
- Ollama
- Ollama model: `gemma3:1b`

### Run the Project

From the repository root, run:

```bash
uv run code/project_m1_prompt_kit.py
```

Enter the requested clinic details when prompted.

### Example Business Details

- **Name:** CarePlus Clinic
- **Type:** Family clinic
- **City:** Lahore
- **Main patients:** Families
- **Monthly budget:** 15000 PKR

### Test with Ollama

This project generates prompts but does not automatically send them to an AI model.

1. Run the Python script.
2. Copy each generated prompt.
3. Test each prompt using the `gemma3:1b` model in Ollama.
4. Save the actual prompts and responses.
5. Review the results for usefulness, accuracy, unsupported medical claims, invented prices, and patient privacy.

Save your test results in:

```text
docs/project-m1-results.md
```

**Important:** Record actual model outputs only. Do not use example responses as real test results.

### Screenshot

Take a screenshot of the running Python script and save it as:

```text
docs/project-m1-run.png
```

### Who Would Pay for This?

Small clinic owners who need help drafting general marketing content, patient-service replies, and ideas for improving clinic operations but are unsure how to write effective AI prompts.

### Limitations

- The tool generates prompts; it does not automatically generate AI responses.
- It does not connect to an AI model automatically.
- It does not provide medical advice or diagnose patients.
- Generated prompts and responses may require correction and review.

### Healthcare Safety and Privacy

A qualified clinic staff member should review all patient-facing content before publication or sending.

Never enter identifiable patient information into an AI tool unless the clinic has approved an appropriate privacy-compliant process.

### Project Status

- [ ] Python prompt-generation script
- [ ] Test all three prompts with Ollama
- [ ] Review and document actual AI responses
- [ ] Save the results in `docs/project-m1-results.md`
- [ ] Save the running-script screenshot in `docs/project-m1-run.png`
