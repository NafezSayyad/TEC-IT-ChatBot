import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

def load_vectorstore(index_path="tec_it_faiss_index"):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.load_local(index_path, embeddings)
    return vectorstore

def build_qa_chain(vectorstore):
    llm = OpenAI(
        temperature=0.0,
        model_name="gpt-4o-mini"
    )
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k":3})
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain

def main():
    print("Loading FAISS vector store...")
    vectorstore = load_vectorstore()
    qa_chain = build_qa_chain(vectorstore)

    print("AI Chatbot Backend (CLI test). Type 'exit' to quit.\n")
    while True:
        query = input("User: ")
        if query.lower() in ["exit", "quit"]:
            break
        result = qa_chain(query)
        answer = result["result"]
        print(f"Chatbot: {answer}\n")

if __name__ == "__main__":
    main()
