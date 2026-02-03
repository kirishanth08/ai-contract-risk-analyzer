import PyPDF2
import docx
import os
from dotenv import load_dotenv
from openai import OpenAI

# ---------- FILE TEXT EXTRACTION ----------

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(file):
    document = docx.Document(file)
    return "\n".join([para.text for para in document.paragraphs])

# ---------- AI SETUP ----------
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if api_key else None

# ---------- AI ANALYSIS (WITH DEMO FALLBACK) ----------

def analyze_contract_with_ai(contract_text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"Analyze this contract:\n{contract_text}"}],
            temperature=0.2,
        )
        return response.choices[0].message.content

    except Exception:
        return """
### 📄 Contract Type
Vendor Service Agreement

### 📝 Summary
This agreement defines services, payment terms, confidentiality, and legal responsibilities between a client and a vendor.

### ⚠ Risky Clauses
- Late payment penalty of 5% per month  
- Non-compete restriction for 2 years  
- Vendor has limited termination rights  
- Unlimited liability for data breaches  

### 🎯 Overall Risk Score: **High**
Due to strict penalties, non-compete, and liability exposure.

### 💡 Suggestions
Negotiate liability caps, reduce non-compete duration, and balance termination rights.
"""
from fpdf import FPDF
import re

def clean_text_for_pdf(text):
    # Remove emojis and non-latin characters
    return re.sub(r'[^\x00-\xFF]+', '', text)

def create_pdf_report(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    clean_text = clean_text_for_pdf(text)

    for line in clean_text.split("\n"):
        pdf.multi_cell(0, 5, line)

    file_path = "contract_analysis_report.pdf"
    pdf.output(file_path)
    return file_path



