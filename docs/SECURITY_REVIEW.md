# Security Review

This is a source-level review of the Flask app, notebook, serialized artifacts, template and repository configuration. It is not a penetration test, infrastructure review or certification.

## Overall assessment

The current implementation is a low-complexity educational text classifier. It does not persist messages or provide accounts, but it is not hardened as a public security service. Its most sensitive inputs are submitted message text and serialized model artifacts.

## Positive controls in the current code

- Flask debug mode is disabled by default.
- The built-in development server binds to localhost by default.
- Flask request body size is limited to 16 KiB.
- Message length is limited to 10,000 characters.
- Missing and whitespace-only input are rejected.
- Jinja autoescaping protects message text rendered back to the page.
- NLTK resource failures are converted into an actionable 503 response.
- Message body is not intentionally written to an application database or log by current code.
- Runtime text normalization is aligned with training normalization.
- Tests verify input validation and escaped rendering.

## Findings and required action

| Area | Current implementation | Risk / required action |
| --- | --- | --- |
| Artifact loading | joblib loads both files at module import | Load only trusted reviewed artifacts; record provenance and compatibility |
| Artifact pair | Separate classifier and vectorizer files | Version/hash them as one deployment unit |
| Input handling | Form field with body and character limits | Add edge rate limiting, timeout and abuse controls before public exposure |
| Privacy | No app persistence | Review proxy/host logs and define retention before public exposure |
| Authentication | None | Add only if the service requires accounts or private access |
| Model quality | SMS corpus and basic classifier | Evaluate on representative authorized data, including false positives |
| Dataset licence | Not established in repository | Verify source and redistribution conditions |
| Error handling | NLTK missing handled; other inference failures can propagate | Add privacy-safe structured error handling for production |
| Operations | No monitoring or health endpoint | Add alerts, metrics, resource limits and rollback |
| Third-party UI resources | Google Fonts and external icon kit | Review privacy, CSP, availability and supply-chain implications |

## Serialized artifact threat

Pickle/joblib are not safe formats for untrusted data. Deserialization may execute attacker-controlled code. The application currently loads both files when the module is imported. Never replace them with arbitrary downloads or user uploads. A checksum proves file integrity relative to a trusted expected hash, but does not prove that the artifact was created safely.

## UI and content concerns

The page renders the message back to the user, and Jinja autoescaping is relied upon. Keep that behaviour. Do not apply `safe` to submitted text. Avoid storing messages in session or logs. If the service is publicly accessible, add request rate limits and privacy notices.

## Model safety

A Spam label is not proof of fraud, phishing or maliciousness. A Not Spam label is not proof of safety. Do not wire the output directly to deletion, quarantine, blocking, or account actions without a separately validated decision framework and human oversight.

## Security work required before public production use

- Configure a production WSGI service, HTTPS and security headers.
- Add request rate limiting and abuse monitoring.
- Implement safe error reporting and privacy-safe logging.
- Verify data licensing and artifact provenance.
- Establish model evaluation and rollback processes.
- Define message privacy, retention and deletion controls.
- Review dependencies and third-party resources.
