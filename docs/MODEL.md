# Model and Dataset

## Dataset
The checked-in `spam.csv` is associated with the SMS Spam Collection dataset. Its labels distinguish spam from legitimate (ham) messages. It is not a representative corpus of corporate email, attachments, headers, phishing URLs, or mail-server telemetry.

## Runtime inference
The Flask route transforms one submitted string using the saved vectorizer, then passes the resulting feature matrix to the saved classifier. The artifacts must be generated from compatible preprocessing and feature settings.

## Evaluation requirements
Do not quote an accuracy figure without a reproducible evaluation. Record:
- dataset version and cleaning steps;
- train/test split and random seed;
- class balance and leakage prevention;
- precision, recall, F1 and confusion matrix;
- whether metrics are from held-out data or training data.

## Artifact safety
Pickle/joblib files are executable serialization formats. Only load artifacts generated and reviewed within a trusted workflow.
