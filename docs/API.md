# HTTP Interface and API Contract

## Overview

The current application is a small server-rendered Flask site. It exposes two application routes and does not expose a JSON API, authentication endpoint, database endpoint, model-training endpoint, or file upload endpoint.

The word "API" in this document refers to the HTTP form contract between the browser and Flask, not a REST API suitable for external integrations.

## Route: GET /

**Purpose:** Render the text-classification form.

| Property | Value |
| --- | --- |
| Method | GET |
| Path | `/` |
| Input | None |
| Success status | 200 |
| Response | HTML rendered from `templates/index.html` |
| Model invocation | None |
| State persistence | None |

The response includes the message textarea and the client-side maximum-length hint. The model is loaded when the Python module is imported, but the prediction function is not called by the home route.

## Route: POST /predict

**Purpose:** Validate one submitted message and return a rendered classification.

| Property | Value |
| --- | --- |
| Method | POST |
| Path | `/predict` |
| Content type | Standard HTML form submission, typically `application/x-www-form-urlencoded` |
| Field | `email_text` |
| Empty/whitespace response | 400 |
| Character-limit response | 413 |
| Request body limit | 16 KiB via Flask `MAX_CONTENT_LENGTH` |
| NLTK resource unavailable | 503 |
| Successful prediction | 200 |
| Response | HTML page with prediction result |

### Request field

`email_text` is expected to be a single text string. The server does not parse MIME messages, RFC 5322 headers, attachments, multipart email, sender information, or URLs into separate features.

### Validation order

1. Flask parses the submitted form.
2. The route reads `email_text`, defaulting to an empty string when the field is missing.
3. Whitespace-only content is rejected with status 400.
4. Text longer than 10,000 Python characters is rejected with status 413.
5. If preprocessing cannot load NLTK stop words, the route returns status 503 with setup guidance.
6. Otherwise, the cleaned text is passed to the vectorizer and model.

The request body size limit is enforced by Flask before or during request parsing and may trigger the 413 error handler before the character-count check.

## Successful response

The model output is a single label:
- `1` becomes `Spam`.
- `0` becomes `Not Spam`.

The result is rendered into the page. The submitted message is displayed using Jinja template auto-escaping, so HTML-like characters are not interpreted as markup in the response.

No confidence score or probability is currently displayed. The UI does not expose the model's `predict_proba` output.

## Error behaviour

| Status | Condition | User-visible behaviour |
| --- | --- | --- |
| 400 | Missing or blank text | Prompt to enter a message |
| 413 | Character limit or request-body limit exceeded | Size warning |
| 503 | NLTK English stop-word corpus unavailable | Setup instruction |
| 500 | Model/vectorizer failure or unexpected runtime exception | Flask default server error behaviour |

Unexpected inference exceptions are not converted into domain-specific error responses by the current route. A production service should implement structured error handling, request IDs and privacy-safe logs without recording message bodies.

## Not implemented

There are no routes for login, user management, file upload, message history, training, model selection, health checks, metrics, or external API integration.

## External integration guidance

Do not call this HTML form endpoint as if it were a stable machine API. A future JSON endpoint should define versioning, authentication, schema validation, rate limits, request-size limits, error codes, privacy policy, idempotency expectations, and model-version metadata.
