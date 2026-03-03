
import re
import pdfplumber
#  function to extract text from pdf
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# function to parse resume
def parse_resume(file_path):
    text = extract_text_from_pdf(file_path)
    processed = preprocess_text(text)

    data = {
        "email": extract_email(text),
        "phone": extract_phone(text),
        "linkedin": extract_linkedin(text),
        "processed_text": processed
    }

    return data

#  regex function for regular expression extractionn

def extract_email(text):
    pattern = r"[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+"
    matches = re.findall(pattern, text)
    return matches[0] if matches else None


def extract_phone(text):
    pattern = r"\+?\d[\d -]{8,12}\d"
    matches = re.findall(pattern, text)
    return matches[0] if matches else None

def extract_linkedin(text):
    pattern = r"https://www.linkedin.com/in/[a-zA-Z0-9_-]+"
    matches = re.findall(pattern, text)
    return matches[0] if matches else None