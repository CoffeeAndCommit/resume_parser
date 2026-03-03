import re
import spacy


nlp = spacy.load("en_core_web_sm")

def tokenize_text(text):
    doc = nlp(text)
    tokens = []
    for token in doc:
        if not token.is_stop and not token.is_punct:
            tokens.append(token.text)
    return tokens

def preprocess_text(text):
    doc = nlp(text)

    tokens = []
    for token in doc:
        if not token.is_stop and not token.is_punct:
            tokens.append(token.lemma_)

    return " ".join(tokens)
    
    

def clean_text(text):
    # Lowercase
    text = text.lower()

    # Remove special characters
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text