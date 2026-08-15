from langchain_core.documents import Document
import pandas as pd
from pathlib import Path

ID = "id"
BOOK_TITLE = "book_title"
ENTRY = "entry"

def csv_to_documents(path: Path) -> list[Document]:

    if not path.is_file():
        raise FileNotFoundError(f"The CSV file not found: {path}")

    documents = []

    df = pd.read_csv(path)

    for index, row in df.iterrows():
        content = (
            f"title: {row[BOOK_TITLE]}\n"
            f"entry: {row[ENTRY]}"
        )

        documents.append(
            Document(
                id=row[ID],
                page_content=content,
                metadata={
                    "source": str(path),
                    "row": index
                }
            )
        )

    return documents
