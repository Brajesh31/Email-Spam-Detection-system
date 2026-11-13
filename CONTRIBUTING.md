# Contributing

## Setup
Create a virtual environment, install `requirements.txt`, and run `python app.py`. See the README for platform-specific activation commands.

## Contribution guidelines
- Keep the distinction between SMS classification and email classification explicit.
- Explain changes to preprocessing, feature extraction, training, and model artifacts.
- Do not commit private message samples, credentials, or personally identifiable information.
- Do not load model artifacts from untrusted sources.
- Keep UI changes accessible and compatible with the existing Flask/Jinja structure.

## Validation
Run:
```bash
python -m compileall -q app.py
```
For model changes, include reproducible evaluation details, the train/test split method, and the metrics generated from the notebook.

## Pull requests
Describe the issue, implementation, tests, and any changes to model artifacts or dependencies. Include screenshots for UI changes.
