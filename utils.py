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

# ---------- SMART RISK ANALYSIS ENGINE ----------

def analyze_contract_with_ai(contract_text):
    text = contract_text.lower()

    # 🔴 HIGH RISK KEYWORDS (Financial + Legal + Control)
    high_risk_keywords = [
        "unlimited liability", "indemnify", "indemnification", "liquidated damages",
        "compound interest", "automatic renewal", "non-compete", "exclusive rights",
        "terminate immediately", "loan recall", "recall the loan", "nominee director",
        "publish defaulter", "sole discretion", "without notice", "penalty",
        "security enforcement", "charge over assets", "personal guarantee",
        "cross default", "event of default", "accelerated repayment",
        "all legal costs", "borrower shall bear all costs", "lender may take possession",
        "right to seize", "reputation damage"
    ]

    # 🟡 MEDIUM RISK KEYWORDS
    medium_risk_keywords = [
        "late fee", "arbitration", "liability is limited", "termination notice",
        "service level agreement"
