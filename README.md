# 🛡️ ContextGuard AI

*Context-Aware Data Privacy Interceptor for Enterprise AI*  
Problem Statement 2.2

---

## 📌 Problem Overview
As enterprises rapidly adopt public generative AI tools (e.g., ChatGPT, Claude), employees risk accidentally sharing sensitive corporate data—such as live API keys, internal financial metrics, HR updates, and client PII. 

*ContextGuard AI* acts as a zero-trust local privacy shield that intercepts, analyzes, risk-scores, and automatically redacts sensitive data before prompts reach external LLM servers.

---

## ✨ Key Features
* *Dynamic Context Detection:* Automatically categorizes text into Financial, HR, Legal, Security, or Strategy risk categories.
* *Risk Scoring Engine:* Evaluates threat levels and assigns a quantitative risk score out of 100.
* *Automated Redaction Pipeline:* Uses zero-latency regular expressions to mask API keys, emails, phone numbers, and financial figures with standard placeholder tags.
* *Local Boundary Execution:* Runs entirely on the user's environment to guarantee zero external data leaks.

---

## 🛠️ Tech Stack
* *Language:* Python
* *UI Framework:* Streamlit
* *Parsing Engine:* Python Regular Expressions (re)

---

## 🚀 Quick Start & Installation

1. *Clone the Repository*
   ```bash
   git clone https://github.com/deeksha233434/ContextGuard-AI.git
   cd ContextGuard-AI

## Install Dependencies:

   pip install -r requirements.txt
   
## Run the Streamlit App:

   streamlit run app.py
