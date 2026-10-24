## Email Spam Detection System using Naive Bayes

An intelligent web-based email spam classifier that uses natural language processing and a **Multinomial Naive Bayes** model to detect spam messages with high accuracy. Built with clean text preprocessing, TF-IDF vectorization, and trained on the well-known [`spam.csv`](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset) dataset.

---

### Algorithm Overview

> **Multinomial Naive Bayes** is chosen for its effectiveness on textual data with discrete features like word frequencies and TF-IDF scores. It’s simple, fast, and highly accurate for spam filtering tasks.

---

### Dataset

* **Source**: [SMS Spam Collection Dataset (Kaggle)](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
* **Features**:

  * `v1`: Label (`spam` or `ham`)
  * `v2`: Email/SMS text content

---

### Key Features

Text preprocessing pipeline:
 • Lowercasing, punctuation removal, stopwords removal, and stemming with **PorterStemmer**

Feature engineering:
 • TF-IDF vectorisation

Model training:
 • Multinomial Naive Bayes (via Scikit-learn)

Evaluation metrics:
 • Accuracy, confusion matrix, classification report

Frontend:
 • Clean and professional **Flask-based web interface** to analyze email text

---

### Technologies Used

```bash
Python
Flask
Scikit-learn
NLTK
Pandas, NumPy
HTML, CSS, Jinja2
```

---

### Model Performance

| Metric    | Value  |
| --------- | ------ |
| Accuracy  | 97%+   |
| Precision | High   |
| Recall    | High   |
| F1-Score  | Robust |

---

### Getting Started

#### 1. Clone the Repository

```bash
git clone https://github.com/Brajesh31/Email-Spam-Detection-system.git
cd Email-Spam-Detection-system
```

#### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 3. Run the Web App

```bash
python app.py
```

Then open your browser and visit:
 [http://localhost:5000](http://localhost:5000)

---

### Project Structure

```
Email-Spam-Detection-system/
│
├── app.py                         # Flask web app
├── vectorizer.pkl                 # TF-IDF Vectorizer
├── spam_classifier_model.pkl      # Trained Naive Bayes model
├── Email_Spam_Detection_system_using_Naive_Bayes.ipynb
├── static/
│   └── style.css                  # Custom frontend styling
├── templates/
│   └── index.html                 # Frontend HTML with Jinja2
├── spam.csv                       # Raw dataset
├── README.md
└── requirements.txt
```


Last updated: 2026-10-24 14:16 UTC
