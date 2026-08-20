import pytest

from langchain_anthropic import ChatAnthropic

from src.app.document_loader import csv_to_documents
from src.app.services.config import load_settings
from src.app.services.embeddings import create_embeddings
from src.app.services.llm import create_llm
from src.app.vectorstore import (
    create_retriever,
    create_vector_store
)
from src.app.rag import RAG

from tests.utils import load_data
from tests.data.documents import test_document
from tests.evals.correctness_evaluator import CorrectnessEvaluator

@pytest.fixture(scope="session")
def settings():
    return load_settings()

@pytest.fixture(scope="session")
def llm(settings):
    return create_llm(settings=settings)

@pytest.fixture
def rag(settings, llm):
    documents = csv_to_documents(settings.data_path)
    
    embeddings = create_embeddings(settings)
    vector_store = create_vector_store(embeddings)
    retriever = create_retriever(vector_store)
    
    vector_store.add_documents(documents=documents)
    
    return RAG(retriever=retriever, llm=llm)

@pytest.fixture
def correctness_evaluator(llm):
    return CorrectnessEvaluator(llm)
