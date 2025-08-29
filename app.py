from flask import Flask, render_template, request
import joblib

# Load the saved model and vectorizer
model = joblib.load('spam_classifier_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    email_text = request.form['email_text']
    features = vectorizer.transform([email_text])
    prediction = model.predict(features)[0]
    result = "Spam" if prediction == 1 else "Not Spam"
    return render_template('index.html', result=result, email_text=email_text)


if __name__ == "__main__":
    app.run(debug=True)