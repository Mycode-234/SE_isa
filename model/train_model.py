import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Example training data
X_train = ["happy", "sad", "joy", "anger", "love", "hate"]
y_train = ["positive", "negative", "positive", "negative", "positive", "negative"]

# Train model
vectorizer = CountVectorizer()
X_train_vectors = vectorizer.fit_transform(X_train)
model = MultinomialNB()
model.fit(X_train_vectors, y_train)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)
