import os
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Settings:
    data_path: Path
    azure_openai_endpoint: str
    azure_openai_api_key: str
    azure_openai_embedding_model: str
    azure_anthropic_endpoint: str
    azure_anthropic_api_key: str
    azure_anthropic_model: str

def load_settings() -> Settings:
    return Settings(
        data_path = Path(os.getenv("DATA_PATH")),
        azure_openai_endpoint = os.environ("AZUTE_OPENAI_ENDPOINT"),
        azure_openai_api_key = os.environ("AZUTE_OPENAI_API_KEY"),
        azure_openai_embedding_model = os.environ("AZUTE_OPENAI_EMBEDDING_MODEL"),
        azure_anthropic_endpoint = os.environ("AZUTE_ANTHROPIC_ENDPOINT"),
        azure_anthropic_api_key = os.environ("AZUTE_ANTHROPIC_API_KEY"),
        azure_anthropic_model = os.environ("AZUTE_ANTHROPIC_MODEL")
    )
