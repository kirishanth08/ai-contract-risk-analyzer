📄 AI Contract Analysis & Risk Assessment Bot

An AI-powered legal assistant that helps small and medium businesses understand complex contracts, identify risky clauses, and receive clear explanations in simple language.

🚀 Features

- Upload contracts in PDF, DOCX, or TXT format  
- Extract and analyze contract text automatically  
- Detect risky or unfavorable clauses such as:
  - Indemnity clauses  
  - Non-compete restrictions  
  - Unlimited liability  
  - Penalty & late fee terms  
  - Auto-renewal conditions  
- Provide plain-language explanations of contract terms  
- Generate an overall risk score (Low / Medium / High)  
- Downloadable PDF risk assessment report  

🛠 Tech Stack

| Layer | Technology |
|------|------------|
| Frontend | Streamlit |
| Backend | Python |
| AI/NLP Logic | AI-assisted + rule-based legal risk detection |
| Document Parsing | PyPDF2, python-docx |
| Report Generation | FPDF |
| Deployment | Streamlit Community Cloud |

🎯 Problem Solved

Small and medium businesses often sign contracts without fully understanding hidden legal risks. Legal language can be complex and intimidating.

This system acts as a smart legal assistant by:
- Simplifying legal jargon  
- Highlighting potential risks  
- Giving actionable suggestions  

This helps business owners make safer and more informed contract decisions without needing legal expertise.

📂 Project Structure

ai-contract-risk-analyzer/
│
├── app.py                  # Streamlit user interface  
├── utils.py                # Contract processing & risk detection logic  
├── requirements.txt        # Project dependencies  
├── README.md               # Project documentation  
└── .gitignore  

▶ How to Run Locally

pip install -r requirements.txt  
streamlit run app.py  

🌟 Future Scope

- OCR support for scanned contracts  
- Multilingual contract support (English + Hindi)  
- Compliance checks with legal frameworks  
- Clause similarity comparison with standard templates  
- Clause-level risk scoring 

👨‍💻 Hackathon Project  
AI for Legal Contract Risk Assessment
