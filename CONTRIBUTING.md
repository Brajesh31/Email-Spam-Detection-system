# Contributing

Thank you for helping improve the project. Keep contributions reproducible, privacy-conscious and honest about what the classifier can do.

## Development setup

Follow [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md). Install the pinned dependencies and provision the NLTK English stop-word corpus with `python scripts/setup_nltk.py`.

## Required contribution principles

- Keep the task described as SMS/text classification, not full email security.
- Keep Flask preprocessing identical to the notebook pipeline.
- Treat the classifier and vectorizer as a matched artifact pair.
- Document changes to dataset, preprocessing, tokenization, labels, feature extraction, split strategy, training, evaluation and export.
- Never commit private message samples, production mail exports, credentials, tokens or personally identifiable information.
- Do not load untrusted pickle/joblib artifacts.
- Keep the HTML template's autoescaping for user-submitted text.
- Do not add persistence or telemetry without documenting purpose, access, retention and deletion.
- Keep tests deterministic and synthetic.

## Validation

```bash
python -m compileall -q app.py tests scripts
python -m unittest discover -s tests -v
```

For notebook changes, the test suite compiles code cells. For model changes, run the notebook from a clean kernel and record dataset provenance, split, seed, class distribution, precision, recall, F1, confusion matrix, false-positive/negative counts, package versions and artifact pairing.

## Model contribution checklist

Before committing model changes:
1. Confirm dataset source and licence.
2. Review labels, nulls, duplicates and class balance.
3. Version preprocessing changes with the notebook and serving app.
4. Fit learned transforms on training data only.
5. Evaluate on a held-out split not used for repeated tuning.
6. Regenerate classifier and vectorizer together.
7. Load both artifacts in a clean pinned environment.
8. Update model card, evaluation document and release checklist.

## Pull requests

Describe the problem, implementation, validation and known limitations. Include UI screenshots only with synthetic messages. For model changes, clearly distinguish archived metrics from newly reproduced results.
