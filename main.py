from src.features import create_tfidf_features

texts = [
    "python machine learning data analysis",
    "java backend spring boot microservices",
    "deep learning neural networks python",
    "react frontend javascript ui development"
]

labels = [
    "Data Scientist",
    "Backend Developer",
    "Data Scientist",
    "Frontend Developer"
]

X, Y, vectorizer = create_tfidf_features(resume_text=texts, labels=labels)

print("Shape of feature matrix:", X.shape)
print("Shape of label matrix:", Y.shape)
