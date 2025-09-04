from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def get_retriever(docs, api_key):
    if not docs:
        raise ValueError("❌ No documents provided to retriever. Check PDF extraction.")

    # Extra debug
    print("📄 Docs count:", len(docs))
    print("🔎 Sample text:", docs[0].page_content[:200])

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=api_key
    )

    vectorstore = FAISS.from_documents(docs, embedding=embeddings)
    return vectorstore.as_retriever(search_kwargs={"k": 4})
