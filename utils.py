import PyPDF2
import docx
import re
from fpdf import FPDF

# -------------------------
# TEXT EXTRACTION
# -------------------------

def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text


def extract_text_from_docx(uploaded_file):
    doc = docx.Document(uploaded_file)
    return "\n".join([para.text for para in doc.paragraphs])


# -------------------------
# RISK ANALYSIS ENGINE
# -------------------------

def analyze_contract_with_ai(contract_text):

    text = contract_text.lower()
    risk_score = 0
    risky_clauses = []

    # HIGH RISK KEYWORDS
    high_risk_patterns = {
        "unlimited liability": 3,
        "indemnify": 2,
        "penalty": 2,
        "interest rate above": 2,
        "non-compete": 2,
        "terminate without notice": 3,
        "arbitration in foreign": 2,
        "exclusive jurisdiction": 2,
        "auto renewal": 1,
        "lock-in period": 2,
        "data breach liability": 3
    }

    # MEDIUM RISK KEYWORDS
    medium_risk_patterns = {
        "late payment fee": 1,
        "limited termination rights": 2,
        "intellectual property transfer": 2,
        "confidentiality breach penalty": 1,
        "service level penalty": 1
    }

    # LOW RISK (positive signals)
    low_risk_patterns = [
        "mutual termination",
        "liability cap",
        "notice period",
        "dispute resolution by mutual consent"
    ]

    for phrase, score in high_risk_patterns.items():
        if phrase in text:
            risk_score += score
            risky_clauses.append(phrase)

    for phrase, score in medium_risk_patterns.items():
        if phrase in text:
            risk_score += score
            risky_clauses.append(phrase)

    for phrase in low_risk_patterns:
        if phrase in text:
            risk_score -= 1

    # Risk Level Decision
    if risk_score >= 6:
        risk_level = "High"
    elif risk_score >= 3:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    # Build Analysis Report
    analysis = f"""
### 📄 Contract Type
Automatically Detected Agreement

### 📝 Summary
This contract has been analyzed for legal and financial risk exposure.

### ⚠ Risky Clauses Identified
{chr(10).join(["- " + clause for clause in risky_clauses]) if risky_clauses else "No major risky clauses found."}

### 🎯 Overall Risk Score: **{risk_level}**

### 💡 Suggestions
- Review indemnity and liability terms  
- Add liability caps  
- Ensure balanced termination rights  
- Limit penalty clauses  
"""

    return analysis


# -------------------------
# PDF REPORT GENERATION
# -------------------------

def create_pdf_report(analysis_text):

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Remove emojis / special chars
    clean_text = re.sub(r'[^\x00-\x7F]+', '', analysis_text)

    for line in clean_text.split("\n"):
        pdf.multi_cell(0, 8, line)

    file_path = "contract_risk_report.pdf"
    pdf.output(file_path)
    return file_path

