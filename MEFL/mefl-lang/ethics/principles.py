# ethics/principles.py

class Principle:
    def __init__(self, name, description, priority=1):
        """
        name: str - name of the principle
        description: str
        priority: int - higher number means higher priority in conflicts
        """
        self.name = name
        self.description = description
        self.priority = priority

    def conflicts_with(self, other):
        # Placeholder for conflict detection logic
        # e.g., return True if principles contradict
        return False

    def __repr__(self):
        return f"Principle({self.name}, priority={self.priority})"

class PrincipleSet:
    def __init__(self):
        self.principles = []

    def add_principle(self, principle):
        self.principles.append(principle)
        self.principles.sort(key=lambda p: p.priority, reverse=True)

    def highest_priority(self):
        return self.principles[0] if self.principles else None

    def __repr__(self):
        return f"PrincipleSet({self.principles})"

# Examples
PRINCIPLE_AUTONOMY = Principle("Autonomy", "Respect for individual's self-governance", priority=5)
PRINCIPLE_BENEFICENCE = Principle("Beneficence", "Acting to benefit others", priority=4)
