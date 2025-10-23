#!/usr/bin/env python
import sys
import warnings
from datetime import datetime

from idioms_prompt_creator.crew import IdiomsPromptCreatorCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information
num_sentences = 100
inputs = [
    {
        "topic": "Kindergarten",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "num_sentences": num_sentences,
    },
    {
        "topic": "Parents",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "num_sentences": num_sentences,
    },
    {
        "topic": "Toddlers",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "num_sentences": num_sentences,
    },
]


def run():
    """
    Run the crew.
    """

    try:
        IdiomsPromptCreatorCrew().crew().kickoff_for_each(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    try:
        IdiomsPromptCreatorCrew().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        IdiomsPromptCreatorCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    try:
        IdiomsPromptCreatorCrew().crew().test(
            n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
