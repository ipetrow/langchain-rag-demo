from langchain_openai import OpenAIEmbeddings

def create_embeddings() -> OpenAIEmbeddings:
    return OpenAIEmbeddings(
        model="", # TODO add Azure embedding model name
        base_url="", # TODO add Azure endpont
        api_key="" # TODO add Azure api key
    )