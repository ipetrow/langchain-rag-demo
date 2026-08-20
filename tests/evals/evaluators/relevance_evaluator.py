from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate

from tests.evals.evaluators.evaluation_result import RelevanceResult

SYSTEM_MESSAGE = (
    "system",
    """
    You are an evaluator for question-answering system. 
    You will be provided with a question and its answer.

    Evaluation Criteria:
    - Evaluate whether the answer is relevant and concise.

    Relevance:
    - Relevance value of True: Means the generated answer meets all the criterias.
    - Relevance value of False: Means not all the criterias are met.

    Include a concise, step-be-step explanation of how you reached to the evaluation relevance value.
    """
)
HUMAN_MESSAGE = (
    "human",
    """
    Question:
    {question}

    Answer:
    {answer}
    """
)

class RelevanceEvaluator:

    def __init__(self, llm: ChatAnthropic):
        self._llm = llm.with_structured_output(RelevanceResult)

        self._prompt = ChatPromptTemplate.from_messages([
            SYSTEM_MESSAGE,
            HUMAN_MESSAGE
        ])

    def evaluate(
            self,
            question: str,
            answer: str
    ):
       messages = self._prompt.format_messages(
            question = question,
            answer = answer
        )

       response = self._llm.invoke(messages)

       return response
       