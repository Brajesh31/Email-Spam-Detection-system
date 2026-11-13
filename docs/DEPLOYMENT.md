# Deployment

## Current deployment status

This repository is an educational Flask demonstration. It has no authentication, persistence, rate limiting, abuse controls, monitoring, or production email integration. Do not deploy it as a public mail-security service or invite users to submit private messages.

## Pre-deployment review

1. Build and review the classifier and vectorizer together.
2. Confirm dataset provenance and redistribution rights.
3. Install pinned Python packages and the NLTK stop-word corpus.
4. Run compile, unit and notebook tests in the target environment.
5. Use a production WSGI server rather than Flask's built-in development server.
6. Terminate TLS at a maintained reverse proxy or hosting platform.
7. Apply rate limits and request-size restrictions at both edge and application layers.
8. Avoid logging message content and define retention behaviour.
9. Configure health checks, structured error monitoring and rollback.
10. Record model/vectorizer versions and artifact provenance.

## Example WSGI deployment

Gunicorn is not included in `requirements.txt`. Add and pin a supported WSGI server in the deployment environment before using the following example:

```bash
gunicorn --workers 2 --bind 127.0.0.1:8000 app:app
```

A reverse proxy should serve HTTPS and forward requests to the WSGI process. Select worker count based on measured request latency and memory use. On Windows, use a WSGI server supported by the hosting platform.

## Development-server settings

- `FLASK_HOST`: default `127.0.0.1`.
- `PORT`: default `5000`.
- `FLASK_DEBUG`: local-only debug switch; leave unset in production.

The WSGI service should be configured by the hosting platform. The `if __name__ == "__main__"` block is not a production process manager.

## Production controls still missing

Authentication, request rate limiting, abuse monitoring, privacy retention controls, security headers, operational health endpoints, alerting, dependency scanning, and a model rollback process. The model is not evaluated for full email-security use.

See [OPERATIONS.md](OPERATIONS.md) and [SECURITY_REVIEW.md](SECURITY_REVIEW.md).
