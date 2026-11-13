# Security Policy

## Project scope

This repository is an educational Flask/SMS text-classification demonstration. It is not a production email-security service. Do not submit private or confidential messages, personal data, credentials or regulated information.

## Security-sensitive implementation details

- Flask debug mode is disabled by default; do not enable it on a public server.
- The Flask development server is for local use only; production requires a WSGI server and HTTPS.
- Pickle/joblib artifacts may execute code during loading. Only load trusted, reviewed files.
- The current application has no authentication, rate limiting, persistent audit controls or production monitoring.
- Jinja autoescaping must remain enabled for submitted text.
- Model output is probabilistic and is not a security verdict.

## Reporting

Do not publish exploitable details, credentials, message samples or private data in a public issue. Use GitHub private vulnerability reporting when available, or contact the repository owner privately with impact, affected revision, safe reproduction steps and a suggested mitigation.

## Data handling

Never include private emails/SMS, personal identifiers, credentials, production exports or confidential content in bug reports, tests, screenshots or logs.
