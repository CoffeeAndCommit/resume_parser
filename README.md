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

### 2. Making Predictions
To predict the role of a new resume snippet:
```bash
python predict.py
```

---

## 📊 Model Evaluation
Currently, the model achieves high accuracy on the sample dataset by distinguishing between roles via key professional terms.

- **Stratified Splitting:** Ensures balanced representation of all roles in training/testing sets.
- **Saved Assets:** The `models/` directory contains:
    - `logistic_model.pkl`: The trained classifier.
    - `tfidf_vectorizer.pkl`: The exact vocabulary mapping used for training.

---

## 📝 Future Scope
- [ ] Implement multi-label classification (for candidates with multiple skills).
- [ ] Add a Web Interface (Flask/Streamlit).
- [ ] Integrate a Vector Database (FAISS/Chroma) for resume ranking.
