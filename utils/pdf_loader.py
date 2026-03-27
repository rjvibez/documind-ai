import pdfplumber
from pypdf import PdfReader

def extract_with_pypdf(file):
    try:
        reader = PdfReader(file)
        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

        return text
    except:
        return ""


def extract_with_pdfplumber(file):
    try:
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

        return text
    except:
        return ""


def load_pdf(file):
    # 🔹 Try both methods
    text_pypdf = extract_with_pypdf(file)
    file.seek(0)  # reset file pointer
    text_pdfplumber = extract_with_pdfplumber(file)

    # 🔹 Choose best result
    if len(text_pdfplumber) > len(text_pypdf):
        print("✅ Using pdfplumber (better extraction)")
        return text_pdfplumber
    else:
        print("✅ Using pypdf (better extraction)")
        return text_pypdf