# Contributing

Thanks for helping improve this project. Keep contributions focused, reproducible, and privacy-conscious.

## Development setup

Follow [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md). Install the pinned dependencies and the NLTK English stop-word corpus before running the application.

## Contribution guidelines

- Keep the distinction between SMS text classification and full email security explicit.
- Keep runtime preprocessing identical to the notebook's training preprocessing.
- Treat the classifier and vectorizer as a single artifact pair.
- Explain changes to preprocessing, feature extraction, training, evaluation, dataset, and serialized artifacts.
- Do not commit private message samples, credentials, API tokens, or personally identifiable information.
- Do not load or commit model artifacts from untrusted sources.
- Keep UI changes accessible and compatible with Flask/Jinja.
- Do not add persistence or telemetry without documenting privacy and retention behaviour.

## Validation

Run:

```bash
python -m compileall -q app.py tests scripts
python -m unittest discover -s tests -v
```

For model changes, rerun the notebook from a clean kernel and include the dataset version, split strategy, seed, class distribution, precision, recall, F1, and confusion matrix. Distinguish held-out metrics from training metrics.

## Pull requests

Describe the problem, implementation, validation performed, and any changes to model artifacts or dependencies. Include screenshots for visible UI changes, using synthetic text only. Complete the repository pull request template.
