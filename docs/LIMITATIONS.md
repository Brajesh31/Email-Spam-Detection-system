# Scope and Limitations

## What the project does

The project accepts one text message and labels it with a saved TF-IDF plus Multinomial Naive Bayes classifier trained against an SMS spam dataset. It is useful for learning a basic text-classification workflow and serving a saved model through Flask.

## What it does not do

- It does not inspect full email messages, headers, attachments, sender authentication, links, or domain reputation.
- It does not connect to Gmail, Outlook, SMTP, IMAP, or a mail gateway.
- It does not provide an inbox, user accounts, message history, or a database.
- It does not perform malware scanning, phishing URL analysis, or threat-intelligence lookups.
- It does not provide guaranteed detection or explainable evidence for each classification.
- It is not hardened for unauthenticated public traffic.

## Known technical limitations

- The training dataset's source and redistribution terms are not documented inside this repository.
- The saved model and vectorizer are serialized Python artifacts and require trusted provenance.
- Model quality depends on preprocessing parity, corpus representativeness, and evaluation methodology.
- The NLTK stop-word corpus must be available in the runtime environment.
- There is no rate limiter, authentication layer, persistent audit trail, or production monitoring.
- The training notebook contains interactive and plotting-oriented steps; it is not a production model-training pipeline.

## Appropriate use

Use it as a local educational example. Do not make operational security decisions from its output. A production email-security system needs broader signals, robust evaluation on representative email data, privacy controls, monitoring, abuse prevention, and human escalation paths.
