from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate

SYSTEM_MESSAGE = (
    "system",
    """
    You are a helpful assistant.
    Answer questions relying ONLY on the provided context.

    If you don't know the answer to the question, admit that you don't know.

    Context:
    {context}
    """
)
HUMAN_MESSAGE = (
    "human",
    """
    {question}
    """
)

class RAG():

    def __init__(self, retriever, llm):
        self._retriever = retriever
        self._llm = llm

        self._prompt = ChatPromptTemplate.from_messages([
            SYSTEM_MESSAGE,
            HUMAN_MESSAGE
        ])

    def execute(self, question: str) -> str:
        documents: list[Document] = self._retriever.invoke(question)

        context = "\n".join(
            document.page_content 
            for document in documents
        )

        messages = self._prompt.format_messages(
            context = context,
            question = question
        )

        response = self._llm.invoke(messages)

        return response.content
