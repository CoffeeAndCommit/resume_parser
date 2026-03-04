import numpy as np
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer


def create_tfidf_features(resume_text, labels):
    #  """
    # texts: list of processed resume texts
    # labels: list of corresponding labels
    # returns:
    #     X -> feature matrix
    #     Y -> label array
    #     vectorizer -> fitted vectorizer object
    # """
    vectorizer = TfidfVectorizer(
        max_features=5000,   # limit vocabulary size
        ngram_range=(1, 2)   # use unigrams + bigrams
    )
    joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")
    X = vectorizer.fit_transform(resume_text)
    Y = np.array(labels)
    return X, Y, vectorizer
    
    