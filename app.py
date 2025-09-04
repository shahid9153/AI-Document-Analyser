import streamlit as st
from document_loader import load_documents
from retriever import get_retriever
from qa_chain import get_qa_chain
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Page config
st.set_page_config(page_title="📄 Gemini RAG PDF QA", layout="wide")

# --- Sidebar ---
with st.sidebar:
    st.header("⚙️ Settings")
    uploaded_files = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)
    retriever_k = st.slider("Retriever Top-K", 1, 10, 4)
    temperature = st.slider("Creativity (temperature)", 0.0, 1.0, 0.3)
    st.markdown("---")
    st.caption("Built with LangChain + Gemini 💡")

# --- Title ---
st.title("📄 Gemini RAG PDF QA")
st.write("Upload PDFs and chat with them using Google Gemini.")

# --- Chat History State ---
if "history" not in st.session_state:
    st.session_state.history = []
if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None

# --- Document Loading ---
if uploaded_files and st.session_state.qa_chain is None:
    with st.spinner("📚 Processing PDFs..."):
        try:
            docs, summary = load_documents(uploaded_files)
        except ValueError as e:
            st.error(str(e))
            st.stop()

        # Show summary
        with st.expander("📌 Pointwise Summary", expanded=True):
            for i, point in enumerate(summary, 1):
                st.markdown(f"**{i}.** {point}")

        # Retriever + QA chain
        retriever = get_retriever(docs, api_key)
        qa_chain = get_qa_chain(retriever, api_key)
        st.session_state.qa_chain = qa_chain

# --- Chat Interface ---
if st.session_state.qa_chain:
    question = st.chat_input("Ask a question about your PDFs...")

    if question:
        with st.spinner("🤔 Thinking..."):
            response = st.session_state.qa_chain.invoke({"query": question})
            answer = response.get("result") or response.get("answer", "⚠️ No answer returned.")

        # Save conversation
        st.session_state.history.append({"role": "user", "content": question})
        st.session_state.history.append({"role": "assistant", "content": answer})

    # Display chat
    for msg in st.session_state.history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
