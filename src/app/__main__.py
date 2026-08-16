from dotenv import load_dotenv

from src.app.services.config import load_settings, Settings
from src.app.services.embeddings import create_embeddings
from src.app.services.llm import create_llm
from src.app.vectorstore import (
    create_vector_store,
    create_retriever
)

from .document_loader import csv_to_documents
from .chat_session import ChatSession
from .rag import RAG

def setup_rag(settings: Settings) -> RAG:

    documents = csv_to_documents(settings.data_path)
    
    embeddings = create_embeddings(settings)
    vector_store = create_vector_store(embeddings)
    
    vector_store.add_documents(documents=documents)

    retriever = create_retriever(vector_store)
    llm = create_llm(settings=settings)

    return RAG(
        retriever=retriever,
        llm=llm
    )

if __name__ == "__main__":

    load_dotenv()
    settings = load_settings()

    rag = setup_rag(settings)

    ChatSession(rag).run()