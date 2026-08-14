from pathlib import Path

from document_loader import csv_to_documents

from langchain_openai import OpenAIEmbeddings

def main():
    csv_to_documents(Path("book_journal_entries.csv"))

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-large",  # Your Azure deployment name
        base_url="",
        api_key=""
)

if __name__ == "__main__":
    main()