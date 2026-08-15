import pytest

from src.app.document_loader import csv_to_documents
from src.app.services.config import load_settings

EXPECTED_DOCUMENTS_COUNT = 3
EXPECTED_ID = "0"
EXPECTED_ROW = 0

@pytest.fixture
def documents():
    settings = load_settings()
    
    documents = csv_to_documents(settings.data_path)

    yield documents

def test_documents(documents):

    assert len(documents) == EXPECTED_DOCUMENTS_COUNT

    assert documents[0].id == EXPECTED_ID
    assert documents[0].page_content.startswith("title:")
    assert documents[0].metadata["row"] == EXPECTED_ROW