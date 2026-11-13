# Testing

## Test strategy

The project uses Python's built-in `unittest` framework and Flask's test client. Tests do not retrain the model and do not assert that specific free-form messages must be classified as spam or ham. The inference tests replace the model and vectorizer with mocks so the web contract is deterministic.

## Run locally

```bash
python -m compileall -q app.py tests scripts
python -m unittest discover -s tests -v
```

## Coverage

The current tests cover:

- Home page rendering and presence of the message form.
- Missing and whitespace-only input.
- Maximum message length validation.
- Spam and not-spam rendering using controlled classifier outputs.
- Passing normalized text to the fitted vectorizer.
- A clear response when the NLTK stop-word resource is missing.
- Jinja escaping of markup in submitted message text.
- The preprocessing sequence, using a controlled English stop-word list.

## Model evaluation is separate

The unit suite does not establish model quality. Model changes must be evaluated in the notebook against a held-out split. Record class balance, precision, recall, F1, confusion matrix, and false-positive/false-negative counts. Do not use training accuracy as a substitute for held-out performance.

## Test data privacy

Use synthetic messages only. Never add private email/SMS content, personal identifiers, credentials, or confidential business material to fixtures, logs, screenshots, or issue reports.
