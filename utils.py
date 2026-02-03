import PyPDF2
import docx
from fpdf import FPDF
import re

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

# ---------- DEMO AI ANALYSIS WITH RISK LOGIC ----------

def analyze_contract_with_ai(contract_text):
    text = contract_text.lower()

    high_risk_keywords = [
        "unlimited liability",
        "non-compete",
        "penalty",
        "indemnify",
        "automatic renewal",
        "exclusive property",
        "terminate immediately"
    ]

    medium_risk_keywords = [
        "late fee",
        "arbitration",
        "liability is limited",
        "termination notice",
        "service level"
    ]

    high_score = sum(word in text for word in high_risk_keywords)
    medium_score = sum(word in text for word in medium_risk_keywords)

    if high_score >= 2:
        risk_level = "High"
        risky_clauses = """
- Unlimited or heavy liability exposure  
- Strict non-compete or exclusivity  
- Heavy penalties or indemnification  
- One-sided termination rights  
"""
    elif medium_score >= 2:
        risk_level = "Medium"
        risky_clauses = """
- Moderate late payment penalties  
- Arbitration-based dispute resolution  
- Limited liability clauses  
- Notice-based termination conditions  
"""
    else:
        risk_level = "Low"
        risky_clauses = """
- Balanced termination rights  
- No severe penalties  
- Limited and fair liability  
- Mutual obligations  
"""

    return f"""
### 📄 Contract Type
Service / Vendor Agreement

### 📝 Summary
This contract outlines services, responsibilities, payment terms, and legal protections between two business parties.

### ⚠ Risky Clauses
{risky_clauses}

### 🎯 Overall Risk Score: {risk_level}

### 💡 Suggestions
Review highlighted clauses and negotiate terms to balance risk and responsibility.
"""

# ---------- PDF REPORT ----------

def clean_text_for_pdf(text):
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
