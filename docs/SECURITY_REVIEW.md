# Security Review

This document records implementation-level observations. It is not a penetration test or a production security certification.

## Improvements in this revision

- Flask debug mode is disabled by default.
- The development server binds to localhost by default.
- Request body size and message character count are bounded.
- Missing/blank input is rejected server-side.
- Submitted message text continues to be rendered through Jinja auto-escaping.
- Inference preprocessing is aligned with the training notebook.
- No message body is written to an application database or log by the current code.

## Remaining risks and gaps

| Area | Current state | Required before public use |
| --- | --- | --- |
| Model artifacts | Pickle/joblib files loaded at process startup | Build provenance, integrity verification, trusted artifact pipeline |
| User input | One text field, capped in size | Rate limiting, abuse monitoring, stricter operational controls |
| Privacy | No persistence in current route | Document processor/logging behaviour and retention policy |
| Access control | No authentication | Add access control if the service is not intentionally public |
| Model quality | SMS corpus and simple classifier | Evaluate on representative, consented, current data |
| Dataset rights | Provenance/licence not recorded in repo | Confirm source and redistribution terms |
| Operations | Local Flask server for development | Production WSGI, HTTPS, monitoring, patching, rollback |
| Dependencies | Pinned requirements | Regular vulnerability review and tested updates |

## Sensitive data handling

Do not submit real private messages. Do not add personal message samples to the repository. Avoid logging message bodies, even when debugging failures. Treat any production message processing as a privacy-sensitive data flow requiring explicit retention and access controls.

## Artifact threat

Loading an untrusted `.pkl` or joblib artifact can execute code. Only load trusted, reviewed files. A checksum alone does not make an artifact trustworthy; the source and build process must also be trusted.

## Reporting

Report vulnerabilities privately through GitHub's private vulnerability reporting feature when available. Do not publish exploit instructions, credentials, or user message samples in public issues.
