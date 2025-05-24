# main.py

from ethics.evaluators import is_action_ethical, score_action, evaluate_duties, evaluate_virtues
from ethics.duties import NO_LYING, HELP_OTHERS
from ethics.virtues import HONESTY, COURAGE

if __name__ == "__main__":
    action_context = {"actions": ["lie"]}  # Example unethical action

    print("Duties Evaluated:")
    print(evaluate_duties(action_context, [NO_LYING, HELP_OTHERS]))

    print("\nVirtues Evaluated:")
    print(evaluate_virtues(action_context, [HONESTY, COURAGE]))

    print("\nEthical?")
    print(is_action_ethical(action_context))

    print("\nScore:")
    print(score_action(action_context, [NO_LYING, HELP_OTHERS]))
