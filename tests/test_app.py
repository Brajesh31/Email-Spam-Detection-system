"""Unit tests for the Flask interface and model-input preprocessing."""

import unittest
from unittest.mock import patch

import app as app_module


class SpamDetectorWebTests(unittest.TestCase):
    def setUp(self):
        self.client = app_module.app.test_client()
        app_module.app.config.update(TESTING=True)

    def test_home_page_renders_message_form(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'name="email_text"', response.data)
        self.assertIn(b"Text Spam Detector", response.data)

    def test_missing_message_is_rejected(self):
        response = self.client.post("/predict", data={})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Enter a message", response.data)

    def test_whitespace_only_message_is_rejected(self):
        response = self.client.post("/predict", data={"email_text": "  \n  "})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Enter a message", response.data)

    def test_overlong_message_is_rejected(self):
        message = "x" * (app_module.MAX_MESSAGE_LENGTH + 1)
        response = self.client.post("/predict", data={"email_text": message})
        self.assertEqual(response.status_code, 413)
        self.assertIn(b"characters or fewer", response.data)

    def test_spam_prediction_uses_preprocessed_text(self):
        mock_model = unittest.mock.Mock()
        mock_model.predict.return_value = [1]
        mock_vectorizer = unittest.mock.Mock()
        mock_vectorizer.transform.return_value = "test-features"

        with (
            patch.object(app_module, "model", mock_model),
            patch.object(app_module, "vectorizer", mock_vectorizer),
            patch.object(app_module, "preprocess_message", return_value="cleaned message") as preprocess,
        ):
            response = self.client.post(
                "/predict",
                data={"email_text": "Original submitted message"},
            )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Spam", response.data)
        preprocess.assert_called_once_with("Original submitted message")
        mock_vectorizer.transform.assert_called_once_with(["cleaned message"])
        mock_model.predict.assert_called_once_with("test-features")

    def test_ham_prediction_is_rendered(self):
        mock_model = unittest.mock.Mock()
        mock_model.predict.return_value = [0]
        mock_vectorizer = unittest.mock.Mock()
        mock_vectorizer.transform.return_value = "test-features"

        with (
            patch.object(app_module, "model", mock_model),
            patch.object(app_module, "vectorizer", mock_vectorizer),
            patch.object(app_module, "preprocess_message", return_value="cleaned message"),
        ):
            response = self.client.post(
                "/predict",
                data={"email_text": "A normal message"},
            )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Not Spam", response.data)

    def test_missing_nltk_corpus_returns_actionable_error(self):
        with patch.object(
            app_module,
            "preprocess_message",
            side_effect=LookupError("NLTK English stop words are missing."),
        ):
            response = self.client.post(
                "/predict",
                data={"email_text": "A message to classify"},
            )

        self.assertEqual(response.status_code, 503)
        self.assertIn(b"NLTK English stop words are missing", response.data)

    def test_submitted_markup_is_escaped_in_result(self):
        mock_model = unittest.mock.Mock()
        mock_model.predict.return_value = [0]
        mock_vectorizer = unittest.mock.Mock()
        mock_vectorizer.transform.return_value = "test-features"

        with (
            patch.object(app_module, "model", mock_model),
            patch.object(app_module, "vectorizer", mock_vectorizer),
            patch.object(app_module, "preprocess_message", return_value="cleaned message"),
        ):
            response = self.client.post(
                "/predict",
                data={"email_text": "<script>alert(1)</script>"},
            )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"&lt;script&gt;", response.data)
        self.assertNotIn(b"<script>alert(1)</script>", response.data)


class PreprocessingTests(unittest.TestCase):
    def test_preprocessing_matches_notebook_steps(self):
        with patch.object(
            app_module,
            "_english_stop_words",
            return_value={"the", "are"},
        ):
            result = app_module.preprocess_message("The offers are RUNNING!")

        self.assertEqual(result, "offer run")


if __name__ == "__main__":
    unittest.main()
