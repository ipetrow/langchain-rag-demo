from pydantic import BaseModel, Field
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate

SYSTEM_MESSAGE = (
    "system",
    """
    You are an evaluator for question-answering system. 
    You will be provided with a question, its correct (reference) answer and a generated answer.

    Evaluation Criteria:
    - Evaluate ONLY the factual accuracy of the generated answer against the reference answer. 
    - Moderate amount of additional information, included in the generated answer, is allowed.

    Correctness:
    - Correctness value of True: Means the generated answer meets all the criterias.
    - Correctness value of False: Means not all the criterias are met.

    Include a concise, step-be-step explanation of how you reached to the evaluation correctness value.
    """
)
HUMAN_MESSAGE = (
    "human",
    """
    Question:
    {question}

    Reference Answer:
    {reference_answer}

    Generated Answer:
    {generated_answer}
    """
)

class CorrectnessResult(BaseModel):
    correct: bool = Field(
        description="True if the answer is correct, False otherwise."
    )
    explanation: str = Field(
        description="reasoning behind the correctness decision."
    )

class CorrectnessEvaluator:

    def __init__(self, llm: ChatAnthropic):
        self._llm = llm.with_structured_output(CorrectnessResult)

        self._prompt = ChatPromptTemplate.from_messages([
            SYSTEM_MESSAGE,
            HUMAN_MESSAGE
        ])

    def evaluate(
            self,
            question: str,
            reference_answer: str,
            generated_answer: str
    ):
       messages = self._prompt.format_messages(
            question = question,
            reference_answer = reference_answer,
            generated_answer = generated_answer
        )

       response = self._llm.invoke(messages)

       return response
       