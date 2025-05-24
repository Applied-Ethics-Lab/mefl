from ethics.evaluators import is_action_ethical, score_action, evaluate_duties, evaluate_virtues
from ethics.duties import NO_LYING, HELP_OTHERS
from ethics.virtues import HONESTY, COURAGE

def builtin_is_ethical(args, env):
    action = args[0]
    return is_action_ethical(action)

def builtin_score(args, env):
    action = args[0]
    duties = env.get("duties", [NO_LYING, HELP_OTHERS])
    return score_action(action, duties)

def get_builtins():
    return {
        "is_ethical": builtin_is_ethical,
        "score": builtin_score,
        "evaluate_duties": lambda args, env: evaluate_duties(args[0], [NO_LYING, HELP_OTHERS]),
        "evaluate_virtues": lambda args, env: evaluate_virtues(args[0], [HONESTY, COURAGE])
    }
