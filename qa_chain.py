from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI

def get_qa_chain(retriever, api_key):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",   # ✅ updated
        google_api_key=api_key,
        temperature=0.3
    )
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=False
    )
    return chain
