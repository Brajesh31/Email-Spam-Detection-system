# Model and Dataset

## Dataset scope

The checked-in `spam.csv` contains two relevant fields, `Category` and `Message`, representing ham/spam SMS messages. The training notebook maps `ham` to `0` and `spam` to `1`.

This is not a representative email corpus. It does not model email headers, sender authentication, attachments, embedded images, URL reputation, domain age, or mail-server telemetry. The app's original page wording called the input an email, but the dataset supports a text/SMS demonstration only.

The repository does not currently document a verified dataset source URL, dataset license, or a data-version checksum. Confirm the data provenance and redistribution terms before using the CSV outside this educational repository.

## Training pipeline

The notebook currently performs the following steps:

1. Reads `spam.csv` using Latin-1 encoding and selects `Category` and `Message`.
2. Renames those fields to `label` and `message`.
3. Converts each message to lowercase.
4. Removes ASCII punctuation.
5. Splits on whitespace, removes NLTK English stop words, and applies the NLTK Porter stemmer.
6. Maps ham/spam labels to numeric classes.
7. Splits the data with `test_size=0.2` and `random_state=42`.
8. Fits `TfidfVectorizer` on training text and transforms test text with the same fitted vectorizer.
9. Fits `MultinomialNB` on the training feature matrix.
10. Evaluates predictions and exports the classifier and vectorizer as separate joblib/pickle artifacts.

The notebook's classification-report plot now builds its report DataFrame explicitly. It reads the dataset relative to the notebook's working directory rather than using a Colab-only absolute path.

## Runtime contract

The Flask application must repeat the exact text preprocessing sequence before calling the saved vectorizer. The model and vectorizer must come from the same training run. A changed stop-word list, stemming rule, punctuation policy, or vectorizer configuration requires regeneration of both artifacts.

The NLTK English stop-word corpus is not embedded in the repository. Install dependencies and run:

```bash
python scripts/setup_nltk.py
```

## Evaluation and reporting

The notebook contains a historical output of 96.68% accuracy. Treat that as a saved notebook result, not as a current reproducible benchmark. It should not be promoted as a model guarantee without rerunning the complete notebook and reviewing the evaluation setup.

For any published result, record:

- dataset source/version and cleaning decisions;
- train/test split, random seed, and stratification policy;
- label distribution in each split;
- precision, recall, F1, and confusion matrix for both classes;
- false-positive and false-negative counts;
- whether evaluation is held-out, cross-validation, or training data;
- Python, NLTK, NumPy, and scikit-learn versions.

Accuracy alone can hide poor spam recall or an unacceptable false-positive rate.

## Artifact safety

The `.pkl` files are executable serialized Python objects. Never load artifacts received from an untrusted source. Review and validate the training process, keep the model and vectorizer together, and record their provenance when publishing releases.
