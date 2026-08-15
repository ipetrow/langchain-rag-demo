from langchain_anthropic import ChatAnthropic

from .config import Settings

def create_llm(settings: Settings) -> ChatAnthropic:
    return ChatAnthropic(
        model=settings.azure_anthropic_model,
        base_url=settings.azure_anthropic_endpoint,
        api_key=settings.azure_anthropic_api_key
    )