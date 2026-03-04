# ===============================
# Resume Role Prediction API
# With PDF Upload Support
# ===============================

from flask import Flask, request, jsonify
import joblib
import os
from werkzeug.utils import secure_filename

from src.preprocessing import preprocess_text
from src.parser import extract_text_from_pdf


# Initialize app
app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# Load model and vectorizer
model = joblib.load("models/logistic_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")


@app.route("/")
def home():
    return "Resume Role Prediction API is running!"


# -------------------------------
# TEXT BASED PREDICTION
# -------------------------------
@app.route("/predict-text", methods=["POST"])
def predict_text():

    try:
        data = request.get_json()

        if "resume_text" not in data:
            return jsonify({"error": "resume_text key missing"}), 400

        resume_text = data["resume_text"]

        processed = preprocess_text(resume_text)
        features = vectorizer.transform([processed])
        prediction = model.predict(features)

        return jsonify({
            "predicted_role": prediction[0]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -------------------------------
# PDF FILE UPLOAD PREDICTION
# -------------------------------
@app.route("/predict-file", methods=["POST"])
def predict_file():

    try:
        if "file" not in request.files:
            return jsonify({"error": "No file part"}), 400

        file = request.files["file"]

        if file.filename == "":
            return jsonify({"error": "No selected file"}), 400

        if not file.filename.endswith(".pdf"):
            return jsonify({"error": "Only PDF files allowed"}), 400

        # Secure filename
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

        # Save file
        file.save(filepath)

        # Extract text
        extracted_text = extract_text_from_pdf(filepath)

        # Preprocess
        processed = preprocess_text(extracted_text)

        # TF-IDF transform
        features = vectorizer.transform([processed])

        # Predict
        prediction = model.predict(features)

        return jsonify({
            "predicted_role": prediction[0]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)