# SMS Spam Detection System

A small Flask application that classifies a submitted text message as **Spam** or **Not Spam** using a saved scikit-learn Multinomial Naive Bayes classifier and its matching TF-IDF vectorizer.

> **Scope matters:** the checked-in `spam.csv` contains the SMS Spam Collection data, with `Category` and `Message` columns. Despite the UI wording “Email Spam Detector”, the training data is SMS-focused. This repository is an educational SMS/text spam-classification demo, not a validated email-security or phishing-detection product.

## What it includes

- A Flask page for submitting a text message.
- A saved Multinomial Naive Bayes model and fitted TF-IDF vectorizer.
- A Jupyter notebook showing dataset preparation, preprocessing, training, evaluation, and artifact export.
- A shared preprocessing routine in the Flask application that mirrors the notebook's lowercasing, punctuation removal, English stop-word removal, and Porter stemming.
- Input-length and empty-input validation.
- Unit and Flask route tests.

## Technology

| Area | Technology |
| --- | --- |
| Web application | Python, Flask, Jinja |
| Machine learning | scikit-learn, Multinomial Naive Bayes |
| Text features | TF-IDF |
| Text processing | NLTK, Porter Stemmer, English stop words |
| Data and notebook | pandas, NumPy, Jupyter |
| UI | HTML and CSS |
| Validation | Python `unittest`, GitHub Actions |

## Repository layout

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
│   └── test_app.py
├── docs/
└── .github/
    └── workflows/
```

## Run locally

Use Python 3.11. The dependency versions in `requirements.txt` are pinned for a repeatable environment.

### 1. Clone and create a virtual environment

```bash
git clone https://github.com/Brajesh31/Email-Spam-Detection-system.git
cd Email-Spam-Detection-system
python -m venv .venv
```

Activate it:

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source .venv/bin/activate
```

### 2. Install dependencies and the NLTK resource

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python scripts/setup_nltk.py
```

The NLTK English stop-word corpus is downloaded separately from the Python package. Run the setup script once in each environment that will serve predictions.

### 3. Start the development server

```bash
python app.py
```

Open <http://127.0.0.1:5000/>.

The development server binds to localhost and debug mode is off by default. Optional local settings:

- `FLASK_HOST`: bind address, defaults to `127.0.0.1`.
- `PORT`: port, defaults to `5000`.
- `FLASK_DEBUG`: set to `1` only for local debugging.

Do not enable Flask debug mode on a public server.

## Prediction flow

1. The browser submits the text to `POST /predict`.
2. The server rejects blank or overlong input.
3. `preprocess_message()` applies the same text normalization used by the training notebook.
4. The saved TF-IDF vectorizer transforms the normalized text.
5. The saved classifier predicts class `1` (Spam) or `0` (Not Spam).
6. Jinja renders the result and the submitted text.

The model and vectorizer are a matched artifact pair. Replacing one without regenerating and validating the other can make inference invalid.

## Run tests

```bash
python -m compileall -q app.py tests scripts
python -m unittest discover -s tests -v
```

The route tests replace the model and vectorizer with controlled test doubles. They validate application behaviour without retraining the classifier or relying on a particular model prediction for sample text.

## Model and dataset limitations

- The dataset is SMS-focused and does not represent full email headers, attachments, sender reputation, domains, URLs, or mail-server telemetry.
- The notebook records a historical accuracy output, but that value alone is not a complete performance assessment. Review class-wise precision, recall, F1, confusion matrix, split strategy, and data leakage before reporting a benchmark.
- The classifier is a basic demonstration. It should not be used as the sole control for phishing, malware, fraud, or enterprise mail filtering.
- Pickle/joblib artifacts can execute code when loaded. Load only artifacts generated and reviewed in a trusted environment.
- The app does not provide accounts, persistence, rate limiting, message-retention controls, or production monitoring.

See [Model and dataset](docs/MODEL.md), [Testing](docs/TESTING.md), [Security review](docs/SECURITY_REVIEW.md), and [Limitations](docs/LIMITATIONS.md).

## Responsible use

Do not submit confidential or personal messages. Do not use the output as a definitive security decision. See [SECURITY.md](SECURITY.md) for reporting guidance.

## Contributing and license

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. The project is distributed under the MIT License in [LICENSE](LICENSE).


Last updated: 2026-11-13 21:50 UTC
