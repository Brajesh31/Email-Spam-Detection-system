# Release Checklist

## Repository and code

- [ ] Review changes and confirm no secrets, real message samples or personal data were added.
- [ ] Run `python -m compileall -q app.py tests scripts`.
- [ ] Run `python -m unittest discover -s tests -v`.
- [ ] Confirm notebook code cells compile.
- [ ] Confirm GitHub Actions passes on the release commit.
- [ ] Review dependencies and security advisories.
- [ ] Verify the Flask app starts in a clean environment.

## Dataset and model

- [ ] Confirm dataset provenance and redistribution rights.
- [ ] Record dataset checksum and source/version.
- [ ] Review label mapping and class distribution.
- [ ] Record split strategy, random seed and partition sizes.
- [ ] Record per-class precision, recall, F1, support and confusion matrix.
- [ ] Distinguish fresh held-out results from old notebook outputs.
- [ ] Confirm preprocessing parity between training and serving.
- [ ] Confirm vectorizer and classifier were generated together.
- [ ] Load both artifacts with the pinned package versions.
- [ ] Record artifact checksums and rollback versions.

## Web application

- [ ] Confirm blank and overlong inputs return expected statuses.
- [ ] Confirm request-body limit behaviour.
- [ ] Confirm Jinja autoescaping is retained.
- [ ] Confirm NLTK resource is available under the runtime user.
- [ ] Do not enable Flask debug mode in production.
- [ ] Configure production WSGI and HTTPS before public use.

## Privacy and operations

- [ ] Document message handling and retention.
- [ ] Confirm message bodies are not written to logs.
- [ ] Configure rate limiting and abuse monitoring before public exposure.
- [ ] Configure error monitoring, health checks and rollback.
- [ ] Confirm no claim of full email/phishing security appears in the UI or docs.

## Release decision

A green test suite proves code-level checks pass. It does not validate real-world spam-detection performance or make the tool suitable for production security decisions.
