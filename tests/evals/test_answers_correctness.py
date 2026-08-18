from pathlib import Path

from tests.utils import load_data
from tests.data.documents import test_document
from tests.evals.correctness_evaluator import CorrectnessResult

def test_answers_correctness(rag, correctness_evaluator):

    test_data = load_data(Path("tests/data/evals_correctness.json"))

    for question_item in test_data:
        question = question_item["question"]
        reference_answer = question_item["reference_answer"]

        generated_answer = rag.execute(question)

        evaluation_result: CorrectnessResult = correctness_evaluator.evaluate(
            question=question,
            reference_answer=reference_answer,
            generated_answer=generated_answer
        )

        print(f"Quesetion: {question}")
        print(f"Regerence answer: {reference_answer}")
        print(f"Generated answer: {generated_answer}")
        print(f"Correct: {evaluation_result.correct}")
        print(f"Reasoning: {evaluation_result.e}")
