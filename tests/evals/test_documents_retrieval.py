from pathlib import Path

from langchain_core.documents import Document

from src.app.document_loader import csv_to_documents
from src.app.services.config import load_settings
from src.app.services.embeddings import create_embeddings
from src.app.vectorstore import create_vector_store

from tests.data.documents import test_document
from tests.utils import load_data

EXPECTED_RETRIEVED_DOCUMENTS_NUMBER = 3

def test_documents_retrieval(retriever):

    test_data = load_data(Path("tests/data/evals_dataset.json"))

    retrieved_documents: list[Document] = retriever.invoke(test_data[0]["question"])

    assert len(retrieved_documents) == EXPECTED_RETRIEVED_DOCUMENTS_NUMBER
    assert test_document in retrieved_documents