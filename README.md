# SMS Spam Detection System

A small Flask application that classifies a submitted text message as spam or not spam using a saved scikit-learn Multinomial Naive Bayes model and TF-IDF vectorizer.

> **Dataset clarification:** The checked-in dataset is the SMS Spam Collection. Although the interface uses the word “email”, the training data is SMS text. This repository should therefore be understood as an SMS/text spam-classification demo, not a validated enterprise email-security product.

## Features
- Flask web interface for entering a message.
- Saved scikit-learn classifier and TF-IDF vectorizer.
- Text preprocessing and model experimentation in a Jupyter notebook.
- Binary spam / not-spam prediction.

## Technology
- Python and Flask
- pandas, NumPy and scikit-learn
- NLTK for text preprocessing experiments
- HTML, CSS and Jinja templates
- Jupyter Notebook

## Repository structure
```text
.
├── app.py
├── requirements.txt
├── spam.csv
├── spam_classifier_model.pkl
├── vectorizer.pkl
├── Email_Spam_Detection_system_using_Naive_Bayes.ipynb
├── templates/index.html
├── static/style.css
└── docs/
```

## Setup
Use Python 3.10 or a compatible version supported by the pinned dependencies.

```bash
git clone https://github.com/Brajesh31/Email-Spam-Detection-system.git
cd Email-Spam-Detection-system
python -m venv .venv
```

Activate the environment:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```

Install dependencies and run:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

Open <http://127.0.0.1:5000/>.

## How prediction works
1. The browser submits text to the Flask `/predict` route.
2. The application transforms the input with the saved vectorizer.
3. The classifier predicts a class.
4. The template displays the result.

See [model documentation](docs/MODEL.md) and [architecture](docs/ARCHITECTURE.md) for details.

## Model and dataset limitations
- The source dataset is SMS-focused and may not represent email traffic.
- The saved pickle files must be treated as trusted artifacts. Loading untrusted pickle/joblib files can execute arbitrary code.
- The README's earlier “97%+” claim is not treated as a verified benchmark here. Report measured results only with the notebook, split strategy, and evaluation output.
- A single prediction is not a substitute for human review or a production mail-security pipeline.
- The current Flask development server is configured with debug mode in `app.py`. Do not expose it publicly. Use a production WSGI server and disable debug mode before deployment.

## Development
Run syntax validation:

```bash
python -m compileall -q app.py
```

For changes to preprocessing or training, document the dataset split, random seed, metrics, confusion matrix, and artifact-generation steps. Do not silently replace the model artifacts.

## Security
Do not upload private messages, personal data, credentials, or untrusted model files. See [SECURITY.md](SECURITY.md).

## Contributing and license
Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. This project is distributed under the MIT License in [LICENSE](LICENSE).
