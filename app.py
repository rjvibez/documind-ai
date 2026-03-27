import streamlit as st
from utils.pdf_loader import load_pdf
from utils.text_splitter import split_text
from utils.llm import generate_answer

st.set_page_config(page_title="DocuMind AI", layout="centered")

st.title("📄 DocuMind AI")
st.caption("Ask anything from your documents")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:

    # 📄 Load PDF
    text = load_pdf(uploaded_file)

    if not text.strip():
        st.error("❌ Could not extract text from PDF")
        st.stop()

    # ⚡ Faster chunking
    chunks = split_text(text, chunk_size=800, overlap=100)

    # 💬 Question input
    question = st.text_input("💬 Ask a question")

    if st.button("Get Answer"):
        if question:

            question_lower = question.lower()

            with st.spinner("🤖 Thinking..."):

                try:
                    # 🔥 Handle vague queries
                    if "end note" in question_lower:
                        question = "List all end notes mentioned in the document."

                    # 🔍 Context selection

                    if "summary" in question_lower or "overview" in question_lower:
                        context = text[:4000]

                    elif "end note" in question_lower or "notes" in question_lower:
                        context = text[-4000:]

                    else:
                        # 🔍 Simple keyword scoring (FAST)
                        scored_chunks = []

                        for chunk in chunks:
                            score = sum(
                                1 for word in question_lower.split()
                                if word in chunk.lower()
                            )
                            scored_chunks.append((score, chunk))

                        # 🔝 Top 3 chunks (faster)
                        top_chunks = sorted(scored_chunks, reverse=True)[:3]

                        context = "\n\n".join([c[1] for c in top_chunks])

                        # 🔁 Fallback if weak context
                        if len(context.strip()) < 150:
                            context = text[:4000]

                    # 🤖 Generate answer
                    answer = generate_answer(context, question)

                    # 🔒 Strict control
                    if "not available" in answer.lower():
                        st.warning("⚠️ This question is not relevant to the uploaded document.")
                    else:
                        st.subheader("🤖 Answer")
                        st.write(answer)

                except Exception as e:
                    st.error(f"❌ Error while generating answer: {e}")