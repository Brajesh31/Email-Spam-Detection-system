# Troubleshooting

## NLTK stop words are missing

Run:

```bash
python scripts/setup_nltk.py
```

Use the same active Python environment and OS account for setup and Flask runtime. Confirm the NLTK data directory is on the search path.

## Model or vectorizer file cannot be loaded

Confirm both files exist in the repository root:
- `spam_classifier_model.pkl`
- `vectorizer.pkl`

They must come from a trusted compatible training run. Do not download replacement pickle files from untrusted sources.

## scikit-learn version mismatch

Install the version pinned in `requirements.txt`. Serialized estimators may not load correctly with arbitrary scikit-learn versions. If compatibility is broken, retrain and export both the vectorizer and classifier with a clean pinned environment. Do not upgrade just one dependency and assume the artifacts are portable.

## Notebook cannot locate spam.csv

Launch Jupyter from the repository root. The notebook reads `spam.csv` using a relative path. Confirm the file exists in the current working directory.

## Notebook source or plotting error

Run the notebook from the first cell in a clean kernel. The data-loading cell must execute before any `df` usage. The classification report DataFrame must be defined before the plotting statements. Run `python -m unittest discover -s tests -v` to compile notebook code cells.

## Port 5000 is in use

macOS/Linux:

```bash
PORT=5050 python app.py
```

Windows PowerShell:

```powershell
$env:PORT = "5050"
python app.py
```

## Request returns 413

The application enforces a 10,000-character limit and 16 KiB request-body limit. The total form-encoded request includes field names and encoding overhead, so the body-size limit may be reached first. Shorten the message and try again.

## Prediction output seems inconsistent

Check that preprocessing at runtime matches the notebook and that classifier and vectorizer came from the same training run. The model uses SMS-style training examples. It is not validated for email bodies, long email threads, URLs, attachments or sender metadata.

## CI fails

Run:

```bash
python -m compileall -q app.py tests scripts
python -m unittest discover -s tests -v
```

Inspect the first failed workflow step and reproduce it in a clean virtual environment. Do not report a green build based only on successful dependency installation.
