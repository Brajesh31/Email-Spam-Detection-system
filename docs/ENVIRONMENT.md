# Environment and Dependency Reference

## Supported development environment

- Python 3.11 is the CI runtime.
- A virtual environment is recommended for local development.
- Dependencies are pinned in `requirements.txt`.
- NLTK's English stop-word corpus is an external data resource and must be downloaded separately.

## Python dependencies

| Package | Pinned version | Role |
| --- | ---: | --- |
| pandas | 2.2.2 | CSV loading and tabular preprocessing in the notebook |
| NumPy | 1.26.4 | Numeric operations and notebook dependencies |
| scikit-learn | 1.6.1 | TF-IDF, MultinomialNB, train/test split and evaluation metrics |
| joblib | 1.4.2 | Serialized model and vectorizer loading/export |
| NLTK | 3.8.1 | Stop-word corpus and Porter stemmer |
| Jupyter | 1.0.0 | Notebook interface |
| Matplotlib | 3.9.0 | Evaluation plots |
| Seaborn | 0.13.2 | Confusion-matrix heatmap |
| Flask | 3.1.1 | Web application |

The scikit-learn version is deliberately pinned to match the reported serialization version for the checked-in artifacts. Serialized estimators are not a stable interchange format across arbitrary scikit-learn versions.

## Install dependencies

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python scripts/setup_nltk.py
```

Activate the same virtual environment when running the setup script, notebook, tests and Flask process.

## NLTK data directory

The setup script uses NLTK's default downloader behaviour. The actual download location depends on the environment. The repository ignores a local `.nltk_data/` folder, but NLTK may use a user-level data directory instead. If the application cannot find the corpus, confirm where NLTK is configured to search and run the setup command under the same user/environment as Flask.

## Environment variables

| Name | Default | Effect |
| --- | --- | --- |
| `FLASK_HOST` | `127.0.0.1` | Development server bind address |
| `PORT` | `5000` | Development server port |
| `FLASK_DEBUG` | unset/false | Enables debug mode only for local development when set to a truthy value |

These variables do not configure model paths, database connections, API keys, or a storage service.

## Upgrade procedure

Do not casually update scikit-learn or NumPy in place and assume the serialized files remain compatible. Recreate a clean environment, run the notebook, export both artifacts, start the Flask app with those artifacts, run tests, and record the resulting environment versions and model evaluation.

## Reproducibility record

For a published build, record Python version, package versions, NLTK corpus availability, notebook commit, dataset checksum, preprocessing definition, split seed, and checksums for both model artifacts.
