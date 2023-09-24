import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

class SentimentAnalyzer:
    def __init__(self):
        # Sample dataset (you can replace this with your dataset)
        data = {'text': ['I love this product!', 'This is terrible.', 'It works great.'],
                'label': [1, 0, 1]}
        self.df = pd.DataFrame(data)
        
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(self.df['text'], self.df['label'], test_size=0.2, random_state=42)
        
        # Convert text data to TF-IDF features
        tfidf_vectorizer = TfidfVectorizer(max_features=1000)
        X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
        X_test_tfidf = tfidf_vectorizer.transform(X_test)
        
        # Train a Linear Support Vector Classifier (SVC)
        self.classifier = LinearSVC()
        self.classifier.fit(X_train_tfidf, y_train)
        
        # Predict sentiment for test data
        y_pred = self.classifier.predict(X_test_tfidf)
        
        # Calculate accuracy
        self.accuracy = accuracy_score(y_test, y_pred)

    def predict_sentiment(self, text):
        new_text_tfidf = tfidf_vectorizer.transform([text])
        prediction = self.classifier.predict(new_text_tfidf)

        if prediction == 1:
            sentiment = 'positive'
        else:
            sentiment = 'negative'

        return sentiment, self.accuracy
