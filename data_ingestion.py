import os
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def ingest_data(data_folder="data"):
    """Reads .txt files in the data folder, chunks them, embeds them, and stores in FAISS."""
    docs = []
    for filename in os.listdir(data_folder):
        if filename.endswith(".txt"):
            with open(os.path.join(data_folder, filename), "r", encoding="utf-8") as f:
                text = f.read()
                docs.append(Document(page_content=text))

    # Split large documents into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    split_docs = []
    for doc in docs:
        for chunk in text_splitter.split_text(doc.page_content):
            split_docs.append(Document(page_content=chunk))

    # Generate embeddings and store in FAISS
    embeddings = OpenAIEmbeddings()  # uses OPENAI_API_KEY
    vectorstore = FAISS.from_documents(split_docs, embeddings)

    # Save the FAISS index to a local folder
    faiss_index_path = "tec_it_faiss_index"
    vectorstore.save_local(faiss_index_path)
    print(f"FAISS index saved to {faiss_index_path}")

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    print("Make sure your .txt files are in the 'data' folder.")
    ingest_data()
