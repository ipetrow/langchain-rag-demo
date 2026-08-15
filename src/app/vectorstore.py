from langchain_core.vectorstores import InMemoryVectorStore

from src.app.services.embeddings import OpenAIEmbeddings

def create_vector_store(embeddings: OpenAIEmbeddings):
    return InMemoryVectorStore(
        embedding=embeddings
    )