from langchain_core.documents import Document

test_document = Document(
    id='2', 
    metadata={
        'source': 'tests/data/test_book_journal_entries.csv', 
        'row': 2
    }, 
    page_content='title: The Wheel of Time, The Great Hunt\nentry: Happy to be back - two years have passed since I finished the first one.'
)