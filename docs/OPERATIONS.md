# Operations, Privacy, and Deployment Controls

## Current runtime

The current Flask route processes a text value synchronously in the web process. It does not intentionally persist message bodies, use a database, write an audit trail, authenticate users, or contact an external classifier service.

This limited persistence footprint does not, by itself, establish a complete privacy or security posture. Hosting logs, reverse proxies, platform request logs, error trackers, backups, browser state and third-party resources need separate review.

## Message handling principles

- Avoid logging submitted message bodies.
- Do not put sample/private messages in issue reports, screenshots or test output.
- Keep error logs focused on exception type, route, request ID and operational metadata.
- Do not store raw request bodies in analytics.
- Define retention and deletion before adding persistence.
- Use synthetic test messages.

## Service controls required before public exposure

- Production WSGI server and HTTPS.
- Rate limiting and abuse monitoring.
- Request-size and message-length controls at proxy and application layers.
- Health checks and error monitoring.
- Dependency vulnerability review and patch cadence.
- Trusted artifact provenance and rollback.
- Resource limits and worker sizing based on load tests.
- Incident escalation and backup/recovery plans.

## Model operations

The classifier and vectorizer must be deployed as one release unit. A new vectorizer vocabulary with an old classifier, or the reverse, can lead to incompatible features or misleading output.

Record:
- model artifact version and checksum;
- vectorizer artifact version and checksum;
- scikit-learn version used to build them;
- dataset version/checksum;
- preprocessing contract version;
- evaluation metrics and test split details;
- date and author of training/export;
- rollback target.

## NLTK resource operations

The NLTK stop-word corpus is downloaded separately from pip dependencies. Include this dependency in environment provisioning and test that the runtime user can read it. Do not rely on a developer workstation's pre-existing NLTK cache.

## Privacy review for future features

Before adding message history, accounts, email-provider integrations or external inference services, document the purpose, data categories, legal basis/notice, data residency, third-party processors, retention, access control, deletion, backup expiry and incident-response obligations.

## Monitoring recommendations

Monitor route latency, response status, request-size rejection counts, inference exceptions, process memory and CPU. If collecting model outcome metrics, avoid storing message bodies or identifiers unless strictly necessary and properly governed. Track false-positive and false-negative rates only with a representative and appropriately authorized evaluation process.
