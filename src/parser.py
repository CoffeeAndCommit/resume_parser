
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

    data = {
        "email": extract_email(text),
        "phone": extract_phone(text),
        "raw_text": text[:1000]  # just preview
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