from ethics.duties import NO_LYING, HELP_OTHERS
from ethics.virtues import HONESTY, COURAGE
from ethics.duties import Duty
from ethics.virtues import Virtue

def evaluate_duties(action_context, duties):
    results = {}
    for duty in duties:
        applies = duty.applies(action_context)
        results[duty.name] = {
            "applies": applies,
            "duty_type": duty.duty_type.name,
            "violation": applies and duty.duty_type.name == 'PERFECT'
        }
    return results

def evaluate_virtues(action_context, virtues):
    return {v.name: v.is_virtuous() for v in virtues}

def is_action_ethical(action_context):
    duties = [NO_LYING, HELP_OTHERS]
    virtues = [HONESTY, COURAGE]

    duty_results = evaluate_duties(action_context, duties)
    virtue_results = evaluate_virtues(action_context, virtues)

    perfect_violations = any(d['violation'] for d in duty_results.values() if d['duty_type'] == 'PERFECT')
    any_virtue_good = any(virtue_results.values())

    return not perfect_violations and any_virtue_good

def score_action(action_context, duties):
    """
    Give a numeric score for how well an action performs ethically.
    -1 for each perfect duty violation
    +0.5 for each fulfilled imperfect duty
    """
    duty_results = evaluate_duties(action_context, duties)
    score = 0
    for result in duty_results.values():
        if result['duty_type'] == 'PERFECT' and result['violation']:
            score -= 1
        elif result['duty_type'] == 'IMPERFECT' and not result['violation']:
            score += 0.5
    return score
