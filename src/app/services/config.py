from dataclasses import dataclass
import os
from pathlib import Path

@dataclass(frozen=True)
class Settings:
    data_path: Path
    azure_openai_endpoint: str
    azure_openai_api_key: str
    azure_openai_model_name: str

def load_settings() -> Settings:
    return Settings(
        data_path = "data/book_journal_entries.csv",
        azure_openai_endpoint = os.environ("AZUTE_OPENAI_ENDPOINT"),
        azure_openai_api_key = os.environ("AZUTE_OPENAI_API_KEY"),
        azure_openai_embedding_model_name = os.environ("AZUTE_OPENAI_EMBEDDING_MODEL_NAME")
    )