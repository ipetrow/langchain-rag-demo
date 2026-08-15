from langchain_core.documents import Document

def create_retriever(vector_store):
    return vector_store.as_retriever(
        search_kwargs={"k": 2}
    )

def retrieve_documents(retriever, query: str) -> list[Document]:
    return retriever.invoke(query)