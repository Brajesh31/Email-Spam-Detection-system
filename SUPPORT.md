# Support

## Before asking for help

1. Read [README.md](README.md) and the relevant files in `docs/`.
2. Recreate the environment using the pinned `requirements.txt`.
3. Run `python scripts/setup_nltk.py`.
4. Run compilation and unit tests.
5. Check the corresponding GitHub Actions run if the failure occurs in CI.
6. Confirm that model and vectorizer artifacts are both present and were not replaced independently.

## Local validation

```bash
python -m pip install -r requirements.txt
python scripts/setup_nltk.py
python -m compileall -q app.py tests scripts
python -m unittest discover -s tests -v
```

## Report a reproducible issue

Include:
- operating system and Python version;
- dependency installation commands;
- NLTK setup result, without user-specific file paths;
- startup or test commands;
- expected and actual behaviour;
- sanitized traceback or workflow log;
- whether the issue occurs with the checked-in artifacts.

Never include private email/SMS content, credentials, personal identifiers, confidential data or arbitrary serialized model files.

## Scope

This project is a learning example for SMS/text classification. Integrations with mail providers, guaranteed phishing detection, malware scanning, enterprise email filtering or production service-level commitments are outside the current implementation.
