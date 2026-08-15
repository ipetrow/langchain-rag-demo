from pathlib import Path

from document_loader import csv_to_documents

from src.app.services.config import load_settings, Settings

from src.app.services.embeddings import create_embeddings

from src.app.vectorstore import create_vector_store

def main():
    
    settings = load_settings()

    documents = csv_to_documents(settings.data_path)
    
    embeddings = create_embeddings()

    vector_store = create_vector_store(embeddings)

    vector_store.add_documents(documents)

if __name__ == "__main__":
    main()