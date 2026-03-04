# ===============================
# Resume Role Prediction Script
# ===============================


import joblib
from src.preprocessing import preprocess_text

# Load saved model and vectorizer
model = joblib.load("models/logistic_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

def predict_role(resume_text):
    # Step 1: Preprocess text
    processed_text = preprocess_text(resume_text)

    # Step 2: Convert to TF-IDF features
    features = vectorizer.transform([processed_text])

    # Step 3: Predict
    prediction = model.predict(features)

    return prediction[0]


# ----------- Test -------------
if __name__ == "__main__":
    
    sample_resume = """
    I have experience in python, Django,
    Java, Backend, SpringBoot,SQL  .
    """

    role = predict_role(sample_resume)
    print("Predicted Role:", role)