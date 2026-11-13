# Testing Strategy

## Validation layers

The project uses Python's built-in unittest framework and Flask's test client. CI performs:
1. Python bytecode compilation for application, tests and setup script.
2. Route and preprocessing tests.
3. Notebook JSON/source compilation tests.

The suite does not retrain the model and does not treat a specific free-form message as a permanent spam/ham oracle. Route tests replace the classifier and vectorizer with controlled mocks to assert that the web contract passes the expected input to the correct dependency.

## Run locally

```bash
python -m compileall -q app.py tests scripts
python -m unittest discover -s tests -v
```

## Flask behaviour coverage

- Home page returns HTTP 200 and includes the message form.
- Missing form field is rejected with HTTP 400.
- Whitespace-only text is rejected.
- Message longer than 10,000 characters is rejected with HTTP 413.
- Classifier result 1 renders Spam.
- Classifier result 0 renders Not Spam.
- Runtime preprocessing is invoked before the vectorizer.
- The vectorizer receives the preprocessed string.
- Missing NLTK corpus returns a helpful 503 response.
- Submitted HTML markup is escaped by Jinja.

## Preprocessing coverage

The stop-word provider is replaced with a controlled word set so the test is deterministic and does not require an external NLTK corpus download. It verifies the expected lowercasing, punctuation removal, stop-word filtering and stemming behaviour.

## Notebook coverage

The notebook test parses the .ipynb JSON, compiles every non-empty code cell, verifies that the dataset path is relative to the repository root, and checks that the report plotting cell defines its data before plotting. This catches malformed or concatenated source cells without requiring expensive model retraining in CI.

## Model quality is separate

Passing unit tests does not establish classifier quality. A model change must be evaluated on a held-out data partition and reviewed using class-wise precision, recall, F1, support, confusion matrix and false-positive/negative counts.

## Test data privacy

Use synthetic strings only. Never include private SMS/email, personal identifiers, credentials or confidential messages in fixtures, logs, screenshots or issue reports.

## Production tests still required

If a backend is added, create integration and security tests for identity/session lifecycle, server-side authorization, cross-user and cross-tenant denial, upload size/type/signature validation, malware status transitions, object-store access control, signed URL expiry, rate limits, CSRF, deletion/retention and backup/restore.
