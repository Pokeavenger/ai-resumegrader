import pdfplumber

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file.file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()
    return text
