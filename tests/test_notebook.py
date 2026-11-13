"""Validate the checked-in training notebook source without retraining the model."""

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_PATH = ROOT / "Email_Spam_Detection_system_using_Naive_Bayes.ipynb"


class NotebookIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with NOTEBOOK_PATH.open("r", encoding="utf-8") as notebook_file:
            cls.notebook = json.load(notebook_file)
        cls.cells = cls.notebook.get("cells", [])

    def test_notebook_has_valid_format_metadata(self):
        self.assertEqual(self.notebook.get("nbformat"), 4)
        self.assertIn("kernelspec", self.notebook.get("metadata", {}))

    def test_every_code_cell_compiles(self):
        for index, cell in enumerate(self.cells):
            if cell.get("cell_type") != "code":
                continue

            source = cell.get("source", "")
            source_text = "".join(source) if isinstance(source, list) else source
            if not source_text.strip():
                continue

            with self.subTest(cell=index):
                compile(source_text, f"notebook-cell-{index}", "exec")

    def test_dataset_load_uses_repository_relative_path(self):
        source = "".join(self.cells[3].get("source", []))
        self.assertIn('pd.read_csv("spam.csv", encoding="latin-1")', source)
        self.assertNotIn("/content/spam.csv", source)

    def test_classification_report_is_defined_before_plotting(self):
        source = "".join(self.cells[14].get("source", []))
        self.assertIn("report_df = pd.DataFrame(report).T", source)
        self.assertLess(source.index("report_df ="), source.index("class_report.plot("))
        self.assertIn("classification_report(", source)

    def test_notebook_splits_before_fitting_vectorizer(self):
        split_source = "".join(self.cells[8].get("source", []))
        fit_source = "".join(self.cells[9].get("source", []))
        transform_source = "".join(self.cells[10].get("source", []))

        self.assertIn("train_test_split(", split_source)
        self.assertIn("fit_transform(X_train)", fit_source)
        self.assertIn("transform(X_test)", transform_source)


if __name__ == "__main__":
    unittest.main()
