# Release Checklist

## Code and documentation

- [ ] Review all changes and confirm no secrets or private message content are included.
- [ ] Run `python -m compileall -q app.py tests scripts`.
- [ ] Run `python -m unittest discover -s tests -v`.
- [ ] Confirm the CI workflow is green on the release commit.
- [ ] Review README, model documentation, known limitations, and security notes.

## Model artifact release

- [ ] Confirm dataset provenance and redistribution terms.
- [ ] Record the dataset version and preprocessing implementation.
- [ ] Record train/test split, random seed, class distribution, precision, recall, F1, and confusion matrix.
- [ ] Confirm the classifier and vectorizer were generated together.
- [ ] Load both artifacts in a clean environment using the pinned dependencies.
- [ ] Confirm the NLTK English stop-word resource and serving preprocessing are available.
- [ ] Review artifact provenance before publishing serialized files.

## Deployment

- [ ] Do not use the Flask development server or debug mode in production.
- [ ] Configure a production WSGI server and HTTPS.
- [ ] Configure rate limiting, request limits, privacy-safe logging, and operational monitoring.
- [ ] Document model version, rollback procedure, and message retention behaviour.
- [ ] Confirm the service is not represented as validated email security.
