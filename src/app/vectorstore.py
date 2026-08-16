from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore

from src.app.services.embeddings import OpenAIEmbeddings

def create_vector_store(embeddings: OpenAIEmbeddings):
    return InMemoryVectorStore(
        embedding=embeddings
    )

def create_retriever(vector_store):
    return vector_store.as_retriever(
        search_kwargs={"k": 2}
    )

# TODO: Remove
def retrieve_documents(retriever, query: str) -> list[Document]:
    return retriever.invoke(query)