# 🚀 AI-Powered Resume Classification System

An automated pipeline to extract text from resumes (PDF), preprocess data using NLP, and classify job seekers into specific roles (Data Scientist, Backend Developer, etc.) using Machine Learning.

---

## 🏗️ Project Architecture

The system is built with a modular structure:

- **PDF Extraction:** Uses `pdfplumber` to extract raw text from PDF files.
- **NLP Preprocessing:** Uses `SpaCy` for tokenization, stop-word removal, and lemmatization.
- **Feature Extraction:** Implements **TF-IDF (Term Frequency-Inverse Document Frequency)** with N-grams (bi-grams) to convert text into numerical vectors.
- **Machine Learning:** Uses a **Logistic Regression** model to classify resumes based on extracted features.

---

## 📂 Project Structure

```bash
resume_ai_system/
├── data/               # Raw resume PDFs
├── models/             # Saved ML models and vectorizers (.pkl)
├── src/                # Core logic
│   ├── parser.py       # PDF text extraction & Regex parsing
│   ├── preprocessing.py# NLP cleaning (SpaCy)
│   ├── features.py     # TF-IDF feature generation
│   ├── config.py       # Logging and environment setup
│   └── utils.py        # Resume & JobSeeker class definitions
├── main.py             # Model training and evaluation script
├── predict.py          # Script for making new predictions
└── requirements.txt    # Project dependencies
```

---

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd resume_ai_system
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```

---

## 🚀 Usage

### 1. Training the Model
To train the classifier on the dataset and save the model:
```bash
python main.py
```

### 2. Running the API
The project includes a Flask-based API for making predictions via text or PDF file upload. Run the server using:
```bash
python predict.py
```
*Note: Ensure an `uploads/` folder exists for saving uploaded PDFs.*

---

## 🧪 Testing the API

You can test the API using `curl` from your terminal while the server is running.

### 1. Predict Role from Text
Send a JSON payload with `resume_text`:
```bash
curl -X POST http://127.0.0.1:5000/predict-text \
     -H "Content-Type: application/json" \
     -d '{"resume_text": "Experienced Python Developer with expertise in Flask and SQL."}'
```

### 2. Predict Role from PDF File
Upload a `.pdf` file:
```bash
curl -X POST http://127.0.0.1:5000/predict-file \
     -F "file=@data/raw/sample_resume.pdf"
```

---

## 📊 Model Evaluation
Currently, the model achieves high accuracy on the sample dataset by distinguishing between roles via key professional terms.

- **Stratified Splitting:** Ensures balanced representation of all roles in training/testing sets.
- **Saved Assets:** The `models/` directory contains:
    - `logistic_model.pkl`: The trained classifier.
    - `tfidf_vectorizer.pkl`: The exact vocabulary mapping used for training.

---

## 📂 API Details (predict.py)
- **POST `/predict-text`**: Accepts JSON with raw text.
- **POST `/predict-file`**: Accepts form-data with a PDF file.

---

## 📝 Future Scope
- [ ] Implement multi-label classification (for candidates with multiple skills).
- [ ] Add a Web Interface using Streamlit.
- [ ] Integrate a Vector Database (FAISS/Chroma) for resume ranking.
