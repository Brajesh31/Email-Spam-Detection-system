# Security Policy

## Supported use

This repository is an educational Flask/SMS text-classification demo. It is not a production email-security service. Do not submit confidential or personal messages.

## Security-sensitive implementation details

- Flask debug mode is disabled by default. Do not enable it on a public server.
- The built-in Flask server is for local development only. Use a production WSGI server for deployment.
- Pickle/joblib artifacts may execute code during loading. Load only trusted, reviewed model and vectorizer files.
- The current application has no authentication, rate limiting, persistent audit controls, or production monitoring.
- Model output is probabilistic and must not be treated as a definitive security decision.

## Reporting a vulnerability

Please do not publish exploitable vulnerabilities, credentials, or sensitive message content in a public issue. Use GitHub's private vulnerability reporting feature when available, or contact the repository owner privately with a concise description, impact, affected revision, and safe reproduction steps.

## Data handling

Never include private emails/SMS, personal identifiers, credentials, or confidential company content in bug reports, tests, screenshots, or logs.
