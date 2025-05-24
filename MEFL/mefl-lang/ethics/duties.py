# ethics/duties.py

from enum import Enum, auto

class DutyType(Enum):
    PERFECT = auto()   # Duties that must always be followed (e.g., do not lie)
    IMPERFECT = auto() # Duties that are more flexible (e.g., help others)

class Duty:
    def __init__(self, name, description, duty_type, condition_func=None):
        """
        name: str - name of the duty
        description: str - explanation of the duty
        duty_type: DutyType
        condition_func: callable that returns bool if duty applies (optional)
        """
        self.name = name
        self.description = description
        self.duty_type = duty_type
        self.condition_func = condition_func or (lambda context: True)

    def applies(self, context):
        return self.condition_func(context)

    def __repr__(self):
        return f"Duty({self.name}, {self.duty_type.name})"

# Example: predefined duties
def no_lying_condition(context):
    # Example context check (could be more complex)
    return 'lie' in context.get('actions', [])

NO_LYING = Duty(
    "No Lying",
    "It is a perfect duty to never lie.",
    DutyType.PERFECT,
    no_lying_condition
)

HELP_OTHERS = Duty(
    "Help Others",
    "It is an imperfect duty to help others when possible.",
    DutyType.IMPERFECT
)
