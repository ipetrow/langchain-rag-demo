from langchain_openai import OpenAIEmbeddings

from .config import Settings

def create_embeddings(settings: Settings) -> OpenAIEmbeddings:
    return OpenAIEmbeddings(
        model=settings.azure_openai_embedding_model,
        base_url=settings.azure_openai_endpoint,
        api_key=settings.azure_openai_api_key
    )