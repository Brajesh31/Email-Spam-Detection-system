# Model Card: SMS Text Spam Classifier

## Model identity

| Property | Description |
| --- | --- |
| Project | Email-Spam-Detection-system |
| Actual task | Binary SMS/text message classification |
| Algorithm | Multinomial Naive Bayes |
| Text representation | TF-IDF |
| Preprocessing | Lowercase, ASCII punctuation removal, NLTK English stop words, Porter stemming |
| Labels | 0 = ham, 1 = spam |
| Runtime | Flask with scikit-learn artifacts |
| Artifacts | `spam_classifier_model.pkl` and `vectorizer.pkl` |

## Intended use

Educational demonstration of:
- supervised text classification;
- text normalization;
- TF-IDF feature extraction;
- a Naive Bayes classifier;
- held-out evaluation;
- persistence and reuse of a fitted model in a Flask application.

## Out-of-scope use

Do not use this model as:
- an enterprise email gateway;
- a phishing or business-email-compromise detector;
- malware or attachment scanner;
- URL reputation service;
- sole control for blocking, deleting or quarantining messages;
- a decision system for financial, legal, employment or safety-critical workflows.

## Training data

The checked-in CSV has `Category` and `Message` fields and contains SMS-style ham/spam messages. Source provenance, data version, checksum and redistribution licence are not documented in this repository. Confirm these before external reuse.

## Evaluation

The notebook records 96.68% accuracy on its saved test split. This is a historical output, not a verified benchmark for the current artifacts or future data. Per-class precision/recall/F1 and confusion matrix should be regenerated and reviewed for any reported result. The split currently uses a fixed random seed and a 20% test size but does not explicitly stratify the labels.

## Limitations and expected failure modes

- Language, spelling, abbreviations and vocabulary may differ from the training corpus.
- The model has no email headers, sender reputation, URL analysis or attachment signals.
- The simple bag-of-words representation does not understand intent or context.
- New spam campaigns and concept drift can degrade performance.
- A legitimate message can be falsely classified as spam.
- A spam message can be missed.
- It does not provide calibrated confidence or an explanation for a decision.
- Preprocessing and artifact version mismatch can change or invalidate predictions.

## Human oversight

Treat model output as a low-stakes hint in a learning demo. Do not automatically delete, quarantine, forward, block, or report messages based solely on this output.

## Safety and privacy

Use synthetic or appropriately authorized sample messages. Do not submit confidential or personal messages to a public deployment. Do not log message bodies. Load only trusted pickle/joblib artifacts.

## Maintenance requirements

Re-evaluate with representative, current data; record model and dataset versions; track false positives and false negatives; check preprocessing parity; regenerate classifier and vectorizer as a pair; and provide a rollback process.
