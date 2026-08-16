class ChatSession:

    def __init__(self, llm):
        self._llm = llm

    async def run(self):
        """Run an interactive chat session"""

        print("\n\nType your queries or 'quit' to exit.")
        
        while True:
            try:
                query = input("\nQuestion: ").strip()

                if query.lower() == "quit":
                    break

                response = await self._llm.invoke(query)
                print("\nAnswer:" + response)
            except Exception as e:
                print(f"\nError: {str(e)}")

