# 📄 DocuMind AI – Ask Anything from Your Documents

DocuMind AI is a powerful AI-powered document assistant that allows users to upload PDF files and ask questions directly from the content.

---

## 🚀 Features

- 📄 Upload any PDF document
- 💬 Ask questions in natural language
- 🧠 AI extracts answers directly from the document
- 🔍 Smart context selection for better accuracy
- ⚡ Fast response with optimized processing
- 🔒 Strict document-based answering (no hallucination)

---

## 🧠 How It Works

1. PDF is uploaded and text is extracted
2. Text is split into meaningful chunks
3. Relevant chunks are selected based on the question
4. AI generates answers strictly from document content

---

## 🛠️ Tech Stack

- Streamlit (Frontend + Deployment)
- OpenRouter API (LLM)
- Python
- PDF Processing (pypdf, pdfplumber, pytesseract)

---

## 📦 Installation

```bash
git clone https://github.com/rjvibez/documind-ai.git
cd documind-ai

pip install -r requirements.txt

🔐 Setup Environment Variables

Create a .env file:

OPENROUTER_API_KEY=your_api_key_here

▶️ Run the App

streamlit run app.py

🌐 Deployment

Deployed using Streamlit Community Cloud.

Author

Rajesh – AI/ML Engineer |Ai Artist