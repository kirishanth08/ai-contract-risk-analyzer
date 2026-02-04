import streamlit as st
from utils import extract_text_from_pdf, extract_text_from_docx, analyze_contract_with_ai, create_pdf_report

st.set_page_config(page_title="AI Contract Risk Analyzer")

st.title("📄 AI Contract Analysis & Risk Assessment Bot")
st.write("Upload a contract to analyze risks and get a simple explanation.")

uploaded_file = st.file_uploader("Upload Contract File", type=["pdf", "docx", "txt"])

if uploaded_file:
    st.success("File uploaded successfully!")
    st.write("Filename:", uploaded_file.name)

    if uploaded_file.name.endswith(".pdf"):
        contract_text = extract_text_from_pdf(uploaded_file)
    elif uploaded_file.name.endswith(".docx"):
        contract_text = extract_text_from_docx(uploaded_file)
    else:
        contract_text = str(uploaded_file.read(), "utf-8")

    st.subheader("📜 Extracted Contract Text")
    st.text_area("Contract Content", contract_text, height=200)

    if st.button("🔍 Analyze Contract with AI"):
        with st.spinner("AI is analyzing the contract..."):
            analysis = analyze_contract_with_ai(contract_text)

            st.subheader("🤖 AI Analysis Result")
            st.markdown(analysis)

            # Risk Indicator
            if "High" in analysis:
                st.error("🔴 Overall Risk Level: HIGH")
            elif "Medium" in analysis:
                st.warning("🟡 Overall Risk Level: MEDIUM")
            elif "Low" in analysis:
                st.success("🟢 Overall Risk Level: LOW")

            # Generate PDF Report
            pdf_path = create_pdf_report(analysis)

            with open(pdf_path, "rb") as f:
                st.download_button(
                    "📥 Download Risk Report (PDF)",
                    f,
                    file_name="contract_risk_report.pdf"
                )

