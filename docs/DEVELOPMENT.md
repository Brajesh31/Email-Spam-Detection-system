# Development Guide

## Runtime and reproducible environment

The current CI runtime is Python 3.11. Create a virtual environment for local work and install only the pinned dependencies in `requirements.txt`. Use the same environment for notebook execution, NLTK setup, tests and Flask.

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python scripts/setup_nltk.py
```

Activate with `.venv\\Scripts\\Activate.ps1` on Windows PowerShell or `source .venv/bin/activate` on macOS/Linux.

## Run the web app

```bash
python app.py
```

Open <http://127.0.0.1:5000/>. The built-in Flask server is for local development. Debug mode remains disabled by default.

## Run the notebook

Start Jupyter from the repository root so relative data loading resolves:

```bash
jupyter notebook Email_Spam_Detection_system_using_Naive_Bayes.ipynb
```

Run from the first cell in a clean kernel. The notebook downloads NLTK stop words, loads `spam.csv`, preprocesses and splits the messages, fits TF-IDF on the training partition, trains MultinomialNB, evaluates, and exports both artifacts.

## Commands

```bash
python -m compileall -q app.py tests scripts
python -m unittest discover -s tests -v
```

The test suite compiles all Python notebook code cells, validates the relative dataset path and report plotting order, and uses Flask mocks to test inference integration. It does not retrain the model.

## Code and data organization

- `app.py`: application entry point and inference route.
- `templates/`: Jinja HTML.
- `static/`: CSS.
- `scripts/`: environment/bootstrap utilities.
- `tests/`: route and notebook-contract tests.
- `docs/`: detailed technical and operational documents.
- `spam.csv`: sample training data.
- `*.pkl`: trusted model and vectorizer artifacts.
- `*.ipynb`: exploratory/training workflow.

## Maintenance requirements

Keep notebook preprocessing and Flask preprocessing in sync. Keep model and vectorizer exports from the same training run. Do not include private message samples or credentials in fixtures, tests, logs or screenshots. Explain package and artifact changes in a pull request.
