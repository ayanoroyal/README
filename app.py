import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import os

st.header("Sentiment Analyzer 😊😞")

st.write("Enter a review aur dekho positive hai ya negative!")

# Simple training data (replace with real dataset later)
reviews = [
    "This product is amazing! Love it", "Excellent quality, highly recommend",
    "Great service, very happy", "Worst experience ever", "Terrible product",
    "Don't recommend, waste of money"
]
sentiments = [1, 1, 1, 0, 0, 0]  # 1 = positive, 0 = negative

# Train model
vec = TfidfVectorizer()
X = vec.fit_transform(reviews)
model = MultinomialNB()
model.fit(X, sentiments)

# User input
user_review = st.text_area("Write a review:", placeholder="Type something...")

if st.button("Analyze"):
    if user_review.strip():
        X_user = vec.transform([user_review])
        prediction = model.predict(X_user)[0]
        confidence = model.predict_proba(X_user)[0]
        
        if prediction == 1:
            st.success(f"✅ POSITIVE ({confidence[1]:.0%} confidence)")
        else:
            st.error(f"❌ NEGATIVE ({confidence[0]:.0%} confidence)")
    else:
        st.warning("Please enter a review first!")
else:
    st.info("👆 Type a review and click 'Analyze'")
