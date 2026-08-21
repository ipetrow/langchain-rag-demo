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
from tests.evals.evaluators.correctness_evaluator import CorrectnessEvaluator
from tests.evals.evaluators.relevance_evaluator import RelevanceEvaluator

@pytest.fixture(scope="session")
def settings():
    return load_settings()

@pytest.fixture(scope="session")
def llm(settings):
    return create_llm(settings=settings)

@pytest.fixture
def vector_store(settings):
    embeddings = create_embeddings(settings)
    return create_vector_store(embeddings)

@pytest.fixture
def retriever(vector_store):
    return create_retriever(vector_store)

@pytest.fixture
def rag(settings, vector_store, retriever, llm):
    documents = csv_to_documents(settings.data_path)
    
    vector_store.add_documents(documents=documents)
    
    return RAG(retriever=retriever, llm=llm)

@pytest.fixture
def correctness_evaluator(llm):
    return CorrectnessEvaluator(llm)

@pytest.fixture
def relevance_evaluator(llm):
    return RelevanceEvaluator(llm)
