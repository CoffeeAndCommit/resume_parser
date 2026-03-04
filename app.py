# ===============================
# Resume Role Prediction API
# Using Flask
# ===============================

from flask import Flask, request, jsonify 
import joblib
from src.preprocessing import preprocess_text

# Initialize Flask app
app = Flask(__name__)

#  load model 
model = joblib.load("models/logistic_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

@app.route("/")
def home():
    return "Resume Role Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():

    try:
        data = request.get_json()

        if "resume_text" not in data:
            return jsonify({"error": "resume_text key is missing"}), 400

        resume_text = data["resume_text"]

        # Step 1: Preprocess
        processed_text = preprocess_text(resume_text)

        # Step 2: Convert to TF-IDF
        features = vectorizer.transform([processed_text])

        # Step 3: Predict
        prediction = model.predict(features)

        return jsonify({
            "predicted_role": prediction[0]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
