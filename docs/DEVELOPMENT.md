# Development

## Prerequisites

- Python 3.11
- Git
- Network access for installing Python dependencies and downloading the NLTK English stop-word corpus

## Setup

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python scripts/setup_nltk.py
``

Activate the virtual environment before running commands. On Windows PowerShell use `.venv\\Scripts\\Activate.ps1`; on macOS/Linux use `source .venv/bin/activate`.

## Run the web application

```bash
python app.py
``

The app listens on `127.0.0.1:5000` by default. `FLASK_HOST`, `PORT`, and `FLASK_DEBUG` are optional environment settings. Debug mode is disabled unless explicitly enabled.

## Important files

| Path | Responsibility |
| --- | --- |
| `app.py` | Flask routes, input validation, text preprocessing, model inference |
| `spam.csv` | SMS-labelled training data |
| `Email_Spam_Detection_system_using_Naive_Bayes.ipynb` | Model training and evaluation |
| `spam_classifier_model.pkl` | Serialized classifier |
| `vectorizer.pkl` | Serialized TF-IDF vectorizer |
| `scripts/setup_nltk.py` | NLTK corpus setup |
| `tests/test_app.py` | Web route and preprocessing tests |

## Code conventions

- Keep the runtime preprocessing sequence aligned with the notebook.
- Treat model and vectorizer files as one versioned pair.
- Keep message bodies, personal data, and secrets out of logs and test fixtures.
- Avoid adding persistence unless privacy and retention behaviour are designed first.
- Keep user-visible text escaped through Jinja.

## Validation commands

```bash
python -m compileall -q app.py tests scripts
python -m unittest discover -s tests -v
``

When changing training logic, run the notebook from a clean kernel, retain the split strategy and random seed, and record evaluation metrics. Regenerate both serialized artifacts after any preprocessing or vocabulary change.
