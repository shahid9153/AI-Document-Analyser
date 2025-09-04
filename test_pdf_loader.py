from langchain_community.document_loaders import PyPDFLoader, UnstructuredPDFLoader

pdf_path = "your_file.pdf"

# Try normal loader
loader = PyPDFLoader(pdf_path)
docs = loader.load()
print("PyPDFLoader docs:", len(docs))
if docs:
    print("Sample:", docs[0].page_content[:300])

# Try OCR loader
if not docs:
    loader = UnstructuredPDFLoader(pdf_path, mode="elements")
    docs = loader.load()
    print("UnstructuredPDFLoader docs:", len(docs))
    if docs:
        print("Sample:", docs[0].page_content[:300])
    else:
        print("❌ Still no text found, even with OCR")
