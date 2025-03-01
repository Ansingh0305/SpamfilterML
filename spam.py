import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

# New: inject custom CSS for enhanced styling
st.markdown(
    """
    <style>
    body, .stApp {
        background-color: #f5f5f5;
        font-family: 'Helvetica Neue', sans-serif;
        color: #333333;
    }
    h1 {
        color: #4CAF50;
        text-align: center;
        font-weight: 600;
    }
    div.stButton > button {
        background-color: #4CAF50 !important;
        color: white !important;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        border-radius: 4px;
        transition: background-color 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #45a049 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

stemmer = PorterStemmer()

def preprocess_message(message):
    message = message.lower()
    message = nltk.word_tokenize(message)
    tokens = []
    for token in message:
        if token.isalnum():
            tokens.append(token)
    filtered_tokens = tokens[:]  # make a copy
    tokens.clear()
    for token in filtered_tokens:
        if token not in stopwords.words('english') and token not in string.punctuation:
            tokens.append(token)
    final_tokens = tokens[:]  # another copy
    tokens.clear()
    processed_tokens = []
    for token in final_tokens:
        processed_tokens.append(stemmer.stem(token))
    return " ".join(processed_tokens)

vectorizer = pickle.load(open('vectorizer.pkl','rb'))
classifier = pickle.load(open('model.pkl','rb'))

st.title("Spam Classifier")

message_input = st.text_area("Enter the message")

if st.button('Predict'):
    # 1. Preprocess the message
    processed_message = preprocess_message(message_input)
    # 2. Vectorize the preprocessed message
    vectorized_message = vectorizer.transform([processed_message])
    # 3. Predict using the classifier
    prediction = classifier.predict(vectorized_message)[0]
    # 4. Display the result
    if prediction == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")