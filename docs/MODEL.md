# Model and Dataset

## Dataset scope

The checked-in `spam.csv` contains the columns `Category` and `Message`, with ham/spam SMS-style message data. The notebook maps `ham` to 0 and `spam` to 1.

This is not a full email dataset. It does not model mail headers, sender identity, SPF/DKIM/DMARC results, attachments, embedded images, URL reputation, domain age, mailbox behaviour, message threading or mail-server telemetry.

The repository does not record a verified dataset source URL, exact dataset version, licence or checksum. Confirm provenance and redistribution rights before reusing the CSV elsewhere.

## Training pipeline

1. Read `spam.csv` using Latin-1 encoding.
2. Keep `Category` and `Message`, renaming them to `label` and `message`.
3. Lowercase each message.
4. Remove characters in Python's ASCII `string.punctuation`.
5. Split on whitespace, remove NLTK English stop words and apply Porter stemming.
6. Map ham/spam to 0/1.
7. Split normalized text and labels into train/test using `test_size=0.2` and `random_state=42`.
8. Fit `TfidfVectorizer` only on the training text.
9. Transform test text using the same fitted vectorizer.
10. Fit `MultinomialNB` on training TF-IDF values.
11. Calculate accuracy, classification report and confusion matrix.
12. Export classifier and vectorizer separately using joblib.

## Runtime contract

The Flask app repeats the same normalization before `vectorizer.transform()`. Both serialized artifacts must come from the same training run. A changed preprocessing rule, stop-word list, tokenization method or vectorizer configuration requires both artifacts to be rebuilt.

Run `python scripts/setup_nltk.py` to provision the external English stop-word corpus.

## Evaluation

The checked-in notebook includes a historical 96.68% accuracy output. Treat it as an archived execution result, not a reproducible benchmark or guarantee. A proper report should include class-wise precision, recall, F1, support, confusion matrix, class distribution, dataset provenance, split strategy and software versions.

## Artifact compatibility and safety

The `.pkl` files contain serialized Python objects. Loading a pickle/joblib file can execute code. Only load trusted artifacts from a reviewed training process. scikit-learn serialization is version-sensitive; the repository pins scikit-learn 1.6.1 to match the version reported for the saved artifacts. An intentional upgrade should regenerate and validate both files.
