from dotenv import load_dotenv

from src.app.services.config import load_settings, Settings
from src.app.services.embeddings import create_embeddings
from src.app.services.llm import create_llm
from src.app.vectorstore import create_vector_store

from .document_loader import csv_to_documents
from .chat_session import ChatSession

def setup_rag(settings: Settings):

    documents = csv_to_documents(settings.data_path)
    
    embeddings = create_embeddings(settings)
    vector_store = create_vector_store(embeddings)
    
    vector_store.add_documents(documents=documents)

if __name__ == "__main__":

    load_dotenv()
    settings = load_settings()

    setup_rag(settings)

    llm = create_llm(settings=settings)

    ChatSession(llm).run