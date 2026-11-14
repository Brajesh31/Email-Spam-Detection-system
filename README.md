# SMS Spam Detection System

A Flask web application and Jupyter-based machine-learning demonstration that classifies a submitted text message as **Spam** or **Not Spam** using a saved scikit-learn Multinomial Naive Bayes classifier and a matching TF-IDF vectorizer.

> **Product scope and naming:** the repository is named "Email Spam Detection", and early UI text used email terminology. The checked-in `spam.csv` has `Category` and `Message` fields containing SMS-style messages. The actual scope is therefore an SMS/text spam-classification demonstration. It is not trained or validated as a full email filtering system and must not be presented as a production phishing or email-security control.

## Project goals

This repository demonstrates the end-to-end structure of a small text-classification project:

1. Load a labelled message dataset.
2. Normalize message text using a deterministic preprocessing routine.
3. Convert normalized text into TF-IDF features.
4. Train a Multinomial Naive Bayes classifier.
5. Evaluate predictions on a held-out split.
6. Save the fitted classifier and vectorizer as a matched artifact pair.
7. Load those artifacts in a Flask application.
8. Validate a form submission, preprocess it identically, transform it, predict a class, and render the result.

The repository is an educational prototype. Its purpose is to demonstrate a reproducible pipeline, not to guarantee that any message is safe or dangerous.

## Current features

- Flask home page with a message input form.
- Spam and Not Spam result presentation.
- Saved Multinomial Naive Bayes model and TF-IDF vectorizer.
- Notebook covering data selection, preprocessing, splitting, vectorization, training, evaluation, a manual example, and artifact export.
- Runtime preprocessing that mirrors the notebook's lowercasing, ASCII punctuation removal, NLTK English stop-word removal, and Porter stemming.
- Server-side rejection of blank input and overlong messages.
- Flask request-body size limit.
- Clear response when the required NLTK stop-word resource is unavailable.
- Jinja auto-escaping for the submitted text rendered back to the page.
- Unit tests for the routes, preprocessing contract, model/vectorizer invocation, validation, and output escaping.
- Notebook source compilation tests and GitHub Actions validation.

## Explicit non-features

| Capability | Current implementation |
| --- | --- |
| Full email parsing | Not implemented. Input is one plain text string. |
| Email headers, sender reputation, SPF/DKIM/DMARC | Not inspected. |
| URL or attachment analysis | Not implemented. |
| Phishing or malware detection | Not established by this classifier. |
| User accounts or authentication | Not implemented. |
| Message history or database | Not implemented. |
| Rate limiting or abuse detection | Not implemented. |
| Production monitoring or audit records | Not implemented. |
| Explanation of a prediction | Not implemented. |
| Guaranteed detection | Not possible; output is a model prediction. |

## Technology stack

| Layer | Technology | Responsibility |
| --- | --- | --- |
| HTTP application | Flask 3.1.1 | GET form and POST prediction route |
| Rendering | Jinja templates | Render form, error, and prediction states |
| Feature representation | scikit-learn TF-IDF | Convert normalized text to sparse numeric features |
| Classifier | MultinomialNB | Predict numeric ham/spam class |
| Text preprocessing | NLTK | English stop words and Porter stemming |
| Dataset preparation | pandas, NumPy | Read and prepare tabular messages |
| Evaluation | scikit-learn metrics, Matplotlib, Seaborn | Accuracy, classification report and confusion matrix |
| Notebook | Jupyter | Exploratory training and evaluation |
| Tests | Python unittest and Flask test client | Deterministic route and preprocessing checks |
| Automation | GitHub Actions | Compile, test and repository validation |

The package versions in `requirements.txt` are pinned. The scikit-learn pin is aligned to the version recorded by the checked-in serialized model artifacts. Treat that alignment as important for deserialization compatibility.

## Repository structure

```text
.
├── app.py
├── requirements.txt
├── spam.csv
├── spam_classifier_model.pkl
├── vectorizer.pkl
├── Email_Spam_Detection_system_using_Naive_Bayes.ipynb
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── scripts/
│   └── setup_nltk.py
├── tests/
│   ├── test_app.py
│   └── test_notebook.py
├── docs/
│   ├── ARCHITECTURE.md
│   ├── API.md
│   ├── DATASET.md
│   ├── DEPLOYMENT.md
│   ├── ENVIRONMENT.md
│   ├── EVALUATION.md
│   ├── LIMITATIONS.md
│   ├── MODEL.md
│   ├── MODEL-CARD.md
│   ├── OPERATIONS.md
│   ├── PREPROCESSING.md
│   ├── SECURITY_REVIEW.md
│   ├── TESTING.md
│   └── TROUBLESHOOTING.md
└── .github/
    └── workflows/
```

## Requirements

- Python 3.11 is used by CI.
- pip and a virtual environment.
- Network access to install dependencies.
- Network access for the first NLTK English stop-word download.
- The two trusted model artifacts in the repository root.

## Local installation

Clone the repository and enter its directory:

```bash
git clone https://github.com/Brajesh31/Email-Spam-Detection-system.git
cd Email-Spam-Detection-system
python -m venv .venv
```

Activate the environment.

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies and the NLTK resource:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python scripts/setup_nltk.py
```

Start the local Flask development server:

```bash
python app.py
```

Open <http://127.0.0.1:5000/>.

## Configuration

| Variable | Default | Purpose |
| --- | --- | --- |
| `FLASK_HOST` | `127.0.0.1` | Address used by the built-in Flask development server |
| `PORT` | `5000` | Local development-server port |
| `FLASK_DEBUG` | disabled | Enable Flask debug mode for local debugging only |

Do not enable debug mode on a public server. Production WSGI server configuration is separate from the `app.py` development-server entry point.

## Request-to-prediction flow

1. The browser submits form field `email_text` to `POST /predict`.
2. Flask checks for blank content.
3. Flask enforces a maximum message length of 10,000 characters and a maximum request body of 16 KiB.
4. `preprocess_message()` lowercases the text, removes ASCII punctuation, removes NLTK English stop words, and applies Porter stemming.
5. The fitted vectorizer transforms the normalized string into the same feature space used during training.
6. The saved classifier predicts numeric class `1` or `0`.
7. The route maps `1` to Spam and `0` to Not Spam.
8. Jinja renders the result and the submitted text.

The classifier and vectorizer are a matched pair. Replacing only one artifact can invalidate the pipeline even if both files load without an exception.

See [API contract](docs/API.md), [preprocessing contract](docs/PREPROCESSING.md), and [architecture](docs/ARCHITECTURE.md).

## Training and evaluation

Run Jupyter from the repository root so the notebook can read `spam.csv` with a relative path:

```bash
jupyter notebook Email_Spam_Detection_system_using_Naive_Bayes.ipynb
```

The notebook uses a 20% held-out split with `random_state=42`, fits TF-IDF on the training partition only, and trains Multinomial Naive Bayes. Its saved historical notebook output reports 96.68% accuracy. That number is not a current independent benchmark and must not be treated as a performance guarantee.

Before publishing any model metric, rerun the notebook in a clean environment and record precision, recall, F1, confusion matrix, class support, split strategy, dataset provenance, and software versions. Read [evaluation](docs/EVALUATION.md) and [model card](docs/MODEL-CARD.md).

## Tests and quality checks

Run:

```bash
python -m compileall -q app.py tests scripts
python -m unittest discover -s tests -v
```

The test suite uses controlled classifier and vectorizer doubles for route behaviour. It does not retrain the classifier or assert that arbitrary messages must be categorized as spam or ham. A separate notebook test compiles code cells to catch syntax and notebook-source regressions.

GitHub Actions runs compilation and unit tests on pushes and pull requests to `main`.

## Security and privacy

Do not paste private messages, credentials, financial information, personal data, or confidential business content into this demo. The app currently processes request text in memory and does not intentionally persist message bodies, but this is not a complete privacy program.

The serialized `.pkl` artifacts are executable Python serialization. Loading an untrusted pickle/joblib file can execute code. Only load artifacts generated and reviewed in a trusted environment.

This application does not authenticate users, limit request rates, monitor abuse, scan URLs, analyze attachments, or provide a reliable mail-security decision. See [security review](docs/SECURITY_REVIEW.md), [operations](docs/OPERATIONS.md), and [limitations](docs/LIMITATIONS.md).

## Contributing and license

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Use synthetic text only in tests, screenshots, and issue reports. The project is distributed under the MIT License in [LICENSE](LICENSE).

Last updated: 2026-11-14 05:47 UTC
