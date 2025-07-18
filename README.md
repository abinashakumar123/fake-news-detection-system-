Objective:
To detect and classify news articles as real or fake using machine learning and natural language processing techniques.

Problem Statement:
In today’s digital era, the rapid spread of misinformation can mislead the public. This system aims to combat fake news by providing an automated solution.

Technology Used:

Programming Language: Python
Libraries: Scikit-learn, NLTK, Pandas, NumPy, Matplotlib, Seaborn
NLP Techniques: Stopword removal, stemming, TF-IDF vectorization
Models Used: Random Forest, Logistic Regression

Dataset:

Source: Kaggle – Fake and Real News Dataset
Total Samples: ~20,000

Labels:

0: Real News
1: Fake News

Preprocessing Steps:

Handling missing values
Combining author and title into a single content field
Removing stopwords and applying stemming

Model Training:

Data split: 70% training, 20% validation, 10% testing
Text vectorized using TF-IDF
Models trained and evaluated using accuracy, precision, recall, and F1-score

Performance:

Accuracy: 99%

Precision & Recall: 98%+
F1-Score: 99%
Confusion matrix used to visualize prediction results

Output:

Predicts whether a news article is Fake or Real
Provides a confidence score for each prediction

Future Enhancements:

Integrate deep learning models like LSTM or BERT
Add multilingual support
Deploy as a web/mobile application
Include real-time news scraping for dynamic predictions



<img width="781" height="386" alt="Screenshot 2025-07-18 231904" src="https://github.com/user-attachments/assets/22bdac37-1f29-4fda-ac34-c281d12599ba" />
<img width="778" height="383" alt="Screenshot 2025-07-18 232145" src="https://github.com/user-attachments/assets/8401cfea-a58d-4b6b-bc72-8178f9261095" />
