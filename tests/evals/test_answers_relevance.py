from pathlib import Path

from tests.utils import load_data
from tests.data.documents import test_document
from tests.evals.evaluators.relevance_evaluator import (
    RelevanceEvaluator,
    RelevanceResult
)

def test_answers_relevance(rag, relevance_evaluator: RelevanceEvaluator):

    evaluation_results: list[(str, RelevanceResult)] = []

    test_data = load_data(Path("tests/data/evals_correctness_relevance_dataset.json"))

    for question_item in test_data:
        question = question_item["question"]

        answer = rag.execute(question)

        evaluation_result_item: RelevanceResult = relevance_evaluator.evaluate(
            question=question,
            answer=answer
        )

        evaluation_results.append((question, evaluation_result_item))

        print(f"\nQuestion: {question}")
        print(f"Answer: {answer}")
        print(f"Relevant: {evaluation_result_item.relevant}")
        print(f"Reasoning: {evaluation_result_item.explanation}")

    for evaluation_result_item in evaluation_results:
        question_item = evaluation_result_item[0]
        relevance_result_item = evaluation_result_item[1]
        
        print(f"\nEvaluating question: {question_item}")
        assert relevance_result_item.relevant
