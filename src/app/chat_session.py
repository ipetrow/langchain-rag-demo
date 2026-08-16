from .rag import RAG

class ChatSession:

    def __init__(self, rag: RAG):
        self._rag = rag

    def run(self):
        """Run an interactive chat session"""

        print("\n\nType your queries or 'quit' to exit.")
        
        while True:
            try:
                question = input("\nQuestion: ").strip()

                if question.lower() == "quit":
                    break

                response = self._rag.execute(question)
                print("\nAnswer: " + response)
            except Exception as e:
                print(f"\nError: {str(e)}")

