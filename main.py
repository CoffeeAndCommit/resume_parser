# ==============================
# Resume Classification Pipeline
# Day 5 - Model Training
# ==============================
# ---- Imports ----
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)
import joblib

from src.features import create_tfidf_features


# ---- Step 1: Prepare Dataset ----
# (Dummy dataset for testing)

base_texts = [
    "python machine learning data analysis statistics pandas numpy",
    "java backend spring boot microservices sql",
    "deep learning neural networks python tensorflow",
    "react frontend javascript html css ui ux",
    "data analysis excel powerbi sql dashboard",
    "backend api development nodejs express mongodb",
    "machine learning model building python sklearn",
    "frontend development react redux javascript"
]

base_labels = [
    "Data Scientist",
    "Backend Developer",
    "Data Scientist",
    "Frontend Developer",
    "Data Analyst",
    "Backend Developer",
    "Data Scientist",
    "Frontend Developer"
]

# Increase dataset size
texts = base_texts * 10
labels = base_labels * 10


# ---- Step 2: Create TF-IDF Features ----
X, vectorizer = create_tfidf_features(texts)
y = labels

print("Feature Matrix Shape:", X.shape)


# ---- Step 3: Train/Test Split ----
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ---- Step 4: Train Model ----
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)


# ---- Step 5: Predictions ----
y_pred = model.predict(X_test)


# ---- Step 6: Evaluation ----
accuracy = accuracy_score(y_test, y_pred)

print("\n===== MODEL EVALUATION =====")
print("Accuracy:", accuracy)
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))


# ---- Step 7: Save Model & Vectorizer ----
joblib.dump(model, "models/logistic_model.pkl")
joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")

print("\nModel and vectorizer saved successfully.")