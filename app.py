from flask import Flask, render_template, request
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Initialize Flask app      
app = Flask(__name__)

# Load model and vectorizer
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('model/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

nltk.download('stopwords')
port_stem = PorterStemmer()

# Preprocessing function
def preprocess_text(text):
    text = re.sub('[^a-zA-Z]', ' ', text).lower().split()
    text = [port_stem.stem(word) for word in text if word not in stopwords.words('english')]
    return ' '.join(text)

# Homepage
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        news_text = request.form['news_text']
        processed_text = preprocess_text(news_text)
        vectorized_text = vectorizer.transform([processed_text])
        prediction = model.predict(vectorized_text)[0]

        result = "Real News" if prediction == 0 else "Fake News"
        return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
