import pytest

from src.app.document_loader import csv_to_documents
from src.app.rag import create_retriever, retrieve_documents
from src.app.services.config import load_settings
from src.app.services.embeddings import create_embeddings
from src.app.vectorstore import create_vector_store

from tests.data.documents import test_document

EXPECTED_RETRIEVED_DOCUMENTS_NUMBER = 2
USER_QUERY = "Did I start The Great Hunt right after the first Wheel of Time book?"

@pytest.fixture
def documents_retriever():
    settings = load_settings()
    
    documents = csv_to_documents(settings.data_path)

    embeddings = create_embeddings(settings)
    vector_store = create_vector_store(embeddings)
    retriever = create_retriever(vector_store)
    
    vector_store.add_documents(documents=documents)

    yield retriever

def test_documents(documents_retriever):

    retrieved_documents = retrieve_documents(
        retriever=documents_retriever, 
        query=USER_QUERY
    )

    assert len(retrieved_documents) == EXPECTED_RETRIEVED_DOCUMENTS_NUMBER
    assert test_document in retrieved_documents