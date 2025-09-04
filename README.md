# AI-Document-Analyser

📄 AI Document Analyser (Gemini RAG PDF QA)

A simple and powerful Retrieval-Augmented Generation (RAG) app built with Google Gemini and LangChain.

It lets you:
✅ Upload one or more PDFs
✅ Get a quick summary of the content
✅ Ask natural language questions about the documents
✅ Receive AI-generated answers backed by the document context

🚀 Features

🔎 PDF Q&A – Ask questions directly from your uploaded PDFs

📝 Automatic Summarization – Get a point-wise summary

🤖 Gemini 1.5 Flash – Fast and efficient Google Gemini model

🖥️ Streamlit UI – Clean and interactive web interface

📂 Project Structure
app.py               # Main Streamlit app
document_loader.py   # Loads & splits PDF documents
retriever.py         # FAISS retriever setup
qa_chain.py          # Gemini QA chain setup
requirements.txt     # Python dependencies
.env.example         # Example environment variables


⚙️ Setup
1️⃣ Clone the repository
git clone https://github.com/shahid9153/AI-Document-Analyser.git
cd AI-Document-Analyser

2️⃣ Create a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate  # On Mac/Linux

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Set up API key

Copy .env.example → .env

Add your Google API key inside:

GOOGLE_API_KEY=your_api_key_here
GEMINI_MODEL_NAME=gemini-1.5-flash

5️⃣ Run the app
streamlit run app.py

📌 Usage

Upload a PDF (or multiple PDFs).

The app generates a quick summary.

Use the chat input to ask questions like:

“Summarize the key points”

“Who is the author?”

“What are the recommendations?”

Get AI-powered answers sourced from your document.

🛡️ Notes

Keep your .env file private (do not upload to GitHub).

This app uses FAISS for local vector search, so no external DB is required.

🙌 Acknowledgements

LangChain
Google Gemini
Streamlit
