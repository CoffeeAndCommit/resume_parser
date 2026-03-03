from src.parser import extract_text_from_pdf
from src.preprocessing import clean_text, tokenize_text, preprocess_text

text =    extract_text_from_pdf("data/raw/sample_resume.pdf")
cleaned = clean_text(text)

tokens = tokenize_text(cleaned)
print(tokens[:50])

processed_text = preprocess_text(text)
print(processed_text[:500])


