# Development

## Environment
Use a virtual environment and install the pinned dependencies:

```bash
python -m venv .venv
python -m pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

The local server listens on port 5000 by default.

## Files to know
- `app.py`: Flask routes and inference.
- `templates/index.html`: form and result view.
- `static/style.css`: page styling.
- `Email_Spam_Detection_system_using_Naive_Bayes.ipynb`: model experimentation.
- `spam.csv`: dataset.
- `*_model.pkl` and `vectorizer.pkl`: inference artifacts.

## Validation
```bash
python -m compileall -q app.py
```
For model changes, rerun notebook evaluation and regenerate model and vectorizer artifacts as a matched pair.
