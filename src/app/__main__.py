from dotenv import load_dotenv

from src.app.rag import create_retriever, retrieve_documents
from src.app.services.config import load_settings
from src.app.services.embeddings import create_embeddings
from src.app.vectorstore import create_vector_store

from .document_loader import csv_to_documents

def main():

    load_dotenv()
    settings = load_settings()

    documents = csv_to_documents(settings.data_path)
    
    embeddings = create_embeddings(settings)
    vector_store = create_vector_store(embeddings)
    retriever = create_retriever(vector_store)
    
    vector_store.add_documents(documents=documents)

    retrieved_documents = retrieve_documents(retriever=retriever, query="Did I start The Great Hunt right after the first Wheel of Time book?")

    print(retrieved_documents)

if __name__ == "__main__":
    main()