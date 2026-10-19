import streamlit as st
import re

# Page Configuration
st.set_page_config(page_title="ContextGuard AI", page_icon="🛡️", layout="centered")

# App Header
st.title("🛡️ ContextGuard AI")
st.subheader("Context-Aware Data Privacy Interceptor for Enterprise AI")
st.write("Automatically scans prompts for confidential corporate secrets, financial numbers, legal risks, security credentials,personal PII etc.")

# Input Box
user_input = st.text_area(
    "Type or paste your draft message meant for the AI tool:",
    placeholder="e.g., Draft an email to John Doe at john.doe@email.com (phone: 555-0192) regarding our secret project revenue of 15M USD.",
    height=150
)

# Core Analysis & Sanitization Logic
def context_guard_engine(text):
    if not text.strip():
        return "", "No Input", 0
    
    redacted_text = text
    risk_score = 10
    detected_context = "General / Safe"
    
    text_lower = text.lower()
    
    # Category Keywords
    financial_keywords = ["revenue", "profit", "$", "acquisition", "budget", "funding", "valuation", "million", "billion", "crore", "usd"]
    hr_keywords = ["fire", "layoff", "termination", "salary hike", "promotion", "resignation", "severance"]
    legal_keywords = ["lawsuit", "litigation", "compliance breach", "audit", "subpoena", "settlement"]
    security_keywords = ["password", "api key","api_key", "secret token", "credentials", "access token","sk-live","sk-test"]
    strategy_keywords = ["secret", "roadmap", "launch", "confidential", "internal only", "unreleased", "patent"]
    
    # Context Detection & Risk Scoring
    if any(word in text_lower for word in financial_keywords):
        detected_context = "🚨 High Risk: Confidential Financial / M&A Data"
        risk_score = 85
    elif any(word in text_lower for word in legal_keywords):
        detected_context = "🚨 High Risk: Sensitive Legal / Compliance Matter"
        risk_score = 90
    elif any(word in text_lower for word in security_keywords):
        detected_context = "🚨 High Risk: Exposed Security Credentials / API Key"
        risk_score = 95
    elif any(word in text_lower for word in hr_keywords):
        detected_context = "⚠️ Moderate Risk: Sensitive Internal HR / Staffing Data"
        risk_score = 75
    elif any(word in text_lower for word in strategy_keywords):
        detected_context = "⚠️ Moderate Risk: Unreleased Product / Corporate Strategy"
        risk_score = 70
    elif "@" in text or "phone" in text_lower or re.search(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b', text):
        detected_context = "⚠️ Moderate Risk: Contains Personally Identifiable Info (PII)"
        risk_score = 60

    # Automatic Masking / Redaction Rules
    # 1. Mask Email Addresses
    redacted_text = re.sub(r'[\w\.-]+@[\w\.-]+\.\w+', '[REDACTED_EMAIL]', redacted_text)

    # 2. Mask Phone Numbers
    redacted_text = re.sub(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b|\b\+?\d{10,12}\b', '[REDACTED_PHONE]', redacted_text)
    # 3. Mask Secret API Keys & Tokens (like sk-live-...)
    redacted_text = re.sub(r'\b(sk-live-|sk-test-|bearer\s+)[\w-]+\b', '[REDACTED_API_KEY]', redacted_text, flags=re.IGNORECASE)
    # 4. Mask Financial Figures & Amounts
    redacted_text = re.sub(r'\b\$?\d+(\.\d+)?\s?(million|billion|M|B|K|USD|INR|crore)?\b', '[REDACTED_FINANCIAL_FIGURE]', redacted_text, flags=re.IGNORECASE)
    
    # 5. Mask Secret & Confidential Words
    redacted_text = re.sub(r'\b(secret|confidential|internal only|unreleased|lawsuit|audit|password)\b', '[REDACTED_SENSITIVE_TERM]', redacted_text, flags=re.IGNORECASE)

    return redacted_text, detected_context, risk_score

# Action Button
if st.button("Analyze & Sanitize Text"):
    if user_input:
        sanitized_output, context_type, risk = context_guard_engine(user_input)
        
        st.markdown("---")
        st.subheader("Analysis Results")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Detected Context Category", value=context_type)
        with col2:
            st.metric(label="Data Leak Risk Score", value=f"{risk}/100")
        
        st.markdown("### Sanitized Output (Safe to send to AI):")
        st.success(sanitized_output)
        
        if risk > 50:
            st.warning("⚠️ *Alert:* Sensitive information or confidential context detected and automatically masked.")
        else:
            st.info("✅ *Status:* Input is safe. No critical corporate secrets found.")
    else:
        st.error("Please enter some text to analyze.")
