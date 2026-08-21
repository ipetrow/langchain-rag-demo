from pathlib import Path

from src.app.document_loader import csv_to_documents
from src.app.rag import retrieve_documents
from src.app.services.config import load_settings
from src.app.services.embeddings import create_embeddings
from src.app.vectorstore import create_vector_store

from tests.data.documents import test_document
from tests.utils import load_data

EXPECTED_RETRIEVED_DOCUMENTS_NUMBER = 2

def test_documents(retriever):

    test_data = load_data(Path("tests/data/evals_correctness_relevance_dataset.json"))

    retrieved_documents = retrieve_documents(
        retriever=retriever,
        query=test_data[0]["question"]
    )

    print(f"DEBUG: Question: {test_data[0]["question"]}")

    assert len(retrieved_documents) == EXPECTED_RETRIEVED_DOCUMENTS_NUMBER
    assert test_document in retrieved_documents