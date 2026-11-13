"""Flask interface for the SMS spam-classification demo."""

import os
import string
from functools import lru_cache
from pathlib import Path

import joblib
from flask import Flask, render_template, request
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "spam_classifier_model.pkl"
VECTORIZER_PATH = BASE_DIR / "vectorizer.pkl"

MAX_MESSAGE_LENGTH = 10_000
MAX_REQUEST_BYTES = 16 * 1024

# The classifier and vectorizer must be loaded from trusted, matching artifacts.
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)
stemmer = PorterStemmer()

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = MAX_REQUEST_BYTES


@lru_cache(maxsize=1)
def _english_stop_words():
    """Load the NLTK corpus once, and fail clearly when setup was skipped."""
    try:
        return set(stopwords.words("english"))
    except LookupError as exc:
        raise LookupError(
            "NLTK English stop words are missing. Run: python scripts/setup_nltk.py"
        ) from exc


def preprocess_message(text):
    """Mirror the notebook's preprocessing before applying the fitted vectorizer."""
    without_punctuation = text.lower().translate(
        str.maketrans("", "", string.punctuation)
    )
    stop_words = _english_stop_words()
    tokens = [
        stemmer.stem(word)
        for word in without_punctuation.split()
        if word not in stop_words
    ]
    return " ".join(tokens)


def render_form(*, result=None, email_text="", error=None, status=200):
    return (
        render_template(
            "index.html",
            result=result,
            email_text=email_text,
            error=error,
            max_message_length=MAX_MESSAGE_LENGTH,
        ),
        status,
    )


@app.route("/", methods=["GET"])
def home():
    return render_form()


@app.route("/predict", methods=["POST"])
def predict():
    email_text = request.form.get("email_text", "")

    if not email_text.strip():
        return render_form(
            email_text=email_text,
            error="Enter a message before running the analysis.",
            status=400,
        )

    if len(email_text) > MAX_MESSAGE_LENGTH:
        return render_form(
            email_text=email_text[:MAX_MESSAGE_LENGTH],
            error=f"Messages must be {MAX_MESSAGE_LENGTH:,} characters or fewer.",
            status=413,
        )

    try:
        cleaned_text = preprocess_message(email_text)
    except LookupError as exc:
        return render_form(email_text=email_text, error=str(exc), status=503)

    features = vectorizer.transform([cleaned_text])
    prediction = model.predict(features)[0]
    result = "Spam" if prediction == 1 else "Not Spam"
    return render_form(result=result, email_text=email_text)


@app.errorhandler(413)
def request_too_large(_error):
    return render_form(
        error="The submitted request is too large. Shorten the message and try again.",
        status=413,
    )


if __name__ == "__main__":
    debug_enabled = os.getenv("FLASK_DEBUG", "").strip().lower() in {
        "1",
        "true",
        "yes",
    }
    app.run(
        host=os.getenv("FLASK_HOST", "127.0.0.1"),
        port=int(os.getenv("PORT", "5000")),
        debug=debug_enabled,
    )
