from pathlib import Path

from tests.utils import load_data
from tests.evals.evaluators.correctness_evaluator import CorrectnessResult

def test_answers_correctness(rag, correctness_evaluator):

    evaluation_results: list[(str, CorrectnessResult)] = []

    test_data = load_data(Path("tests/data/evals_correctness_relevance_dataset.json"))

    for question_item in test_data:
        question = question_item["question"]
        reference_answer = question_item["reference_answer"]

        generated_answer = rag.execute(question)

        evaluation_result_item: CorrectnessResult = correctness_evaluator.evaluate(
            question=question,
            reference_answer=reference_answer,
            generated_answer=generated_answer
        )

        evaluation_results.append((question, evaluation_result_item))

        print(f"Question: {question}")
        print(f"Reference answer: {reference_answer}")
        print(f"Generated answer: {generated_answer}")
        print(f"Correct: {evaluation_result_item.correct}")
        print(f"Reasoning: {evaluation_result_item.explanation}\n")

    for evaluation_result_item in evaluation_results:
        question_item = evaluation_result_item[0]
        correctness_result_item = evaluation_result_item[1]
        
        print(f"Evaluating question: {question_item}\n")
        assert correctness_result_item.correct

