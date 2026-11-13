# Deployment

## Current status

This repository is an educational Flask demonstration. It has no authentication, persistence, rate limiting, monitoring, abuse controls, or production email integration. Do not expose it as a public mail-security service in its current form.

## Pre-deployment requirements

1. Build and review the model and vectorizer together from a trusted training environment.
2. Confirm the data license and the right to redistribute the dataset and model artifacts.
3. Install the pinned Python dependencies and the NLTK English stop-word resource.
4. Run the full test suite in the target environment.
5. Use a production WSGI server. Do not run Flask's built-in development server with debug mode in production.
6. Terminate HTTPS at a maintained reverse proxy or load balancer.
7. Restrict request size, apply rate limits, and define abuse monitoring.
8. Do not log message bodies. Decide whether messages are processed only in memory and document retention behaviour.
9. Add operational health checks, error monitoring, dependency updates, and a model rollback procedure.
10. Verify that the deployed model and vectorizer correspond to the same reviewed training run.

## Example WSGI launch

Gunicorn is not included in `requirements.txt`. Install and pin it as part of the deployment environment, then run:

```bash
gunicorn --workers 2 --bind 127.0.0.1:8000 app:app
```

A reverse proxy should provide HTTPS and forward traffic to the WSGI server. Choose worker counts based on measured resource use, not this example.

On Windows, use a production WSGI server supported by the deployment platform, such as Waitress.

## Environment

- `FLASK_HOST`: development-server bind address, default `127.0.0.1`.
- `PORT`: development-server port, default `5000`.
- `FLASK_DEBUG`: local-only debug switch. Leave unset in production.

The WSGI server should be configured directly by the hosting platform. Do not rely on `app.py`'s development-server block to launch production traffic.
