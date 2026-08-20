from pydantic import BaseModel, Field

class CorrectnessResult(BaseModel):
    correct: bool = Field(
        description="True if the answer is correct, False otherwise."
    )
    explanation: str = Field(
        description="reasoning behind the correctness decision."
    )

class RelevanceResult(BaseModel):
    relevant: bool = Field(
        description="True if the answer addresses the question, False otherwise."
    )
    explanation: str = Field(
        description="reasoning behind the relevance decision."
    )