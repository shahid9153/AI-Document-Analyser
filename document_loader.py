from langchain_community.document_loaders import PyPDFLoader, UnstructuredPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import tempfile

def load_documents(files):
    all_docs = []
    for file in files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(file.read())
            tmp_path = tmp.name

        # Try normal loader
        docs = PyPDFLoader(tmp_path).load()

        # Fallback to OCR if no text found
        if not docs:
            print("⚠️ No text via PyPDFLoader, using OCR...")
            docs = UnstructuredPDFLoader(tmp_path, mode="elements").load()

        all_docs.extend(docs)

    if not all_docs:
        raise ValueError("❌ No text could be extracted from any PDF. Install OCR (Tesseract).")

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_documents(all_docs), ["Summary not implemented yet"]
