# Scope and Limitations

## Implemented task

The application accepts one plain-text message and returns a Spam or Not Spam label using TF-IDF and a saved Multinomial Naive Bayes classifier trained on SMS-style data.

## Not implemented

- Parsing full email messages or RFC-compliant email structure.
- Sender/domain reputation or SPF, DKIM and DMARC analysis.
- URL reputation, redirect analysis or attachment scanning.
- Gmail, Outlook, SMTP, IMAP or mail-gateway integration.
- User accounts, authentication, message history or a database.
- Rate limiting, abuse monitoring or enterprise operations.
- Confidence calibration, model explanations or guaranteed prediction.
- Malware detection or phishing classification as a validated task.

## Technical limitations

- Dataset provenance, licence and exact revision are not documented in the repository.
- Data split uses a fixed 20% test size and random seed but does not explicitly stratify labels.
- The historical accuracy output may be stale and is not a complete report.
- No external/temporal evaluation dataset is included.
- The bag-of-words TF-IDF representation does not understand intent or message context.
- Simple ASCII punctuation removal and whitespace tokenization have language and Unicode limitations.
- Model and vectorizer are serialized artifacts and require trusted provenance and compatible software versions.
- NLTK stop-word resources must be downloaded separately.
- No authentication, rate limiting, persistent audit, monitoring or retention configuration exists.
- The built-in Flask server is for local development only.

## Appropriate use

Use this repository as a local learning example for a small NLP pipeline and Flask inference interface. Do not make operational security decisions from its output. A production mail-security system needs representative email data, richer signals, careful false-positive controls, privacy governance, operational monitoring and human escalation.
