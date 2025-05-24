# ethics/virtues.py

class Virtue:
    def __init__(self, name, description, traits=None):
        """
        name: str - virtue name (e.g., Courage)
        description: str
        traits: dict[str, float] - traits representing degree of virtue (0 to 1)
        """
        self.name = name
        self.description = description
        self.traits = traits or {}

    def develop(self, trait_name, amount):
        current = self.traits.get(trait_name, 0.0)
        new_value = max(0.0, min(1.0, current + amount))
        self.traits[trait_name] = new_value

    def is_virtuous(self, threshold=0.7):
        if not self.traits:
            return False
        avg_trait = sum(self.traits.values()) / len(self.traits)
        return avg_trait >= threshold

    def __repr__(self):
        return f"Virtue({self.name}, traits={self.traits})"


# Export example virtues
HONESTY = Virtue("Honesty", "Being truthful and transparent.", {"truthfulness": 0.9, "integrity": 0.85})
COURAGE = Virtue("Courage", "Facing fear and adversity bravely.", {"bravery": 0.8, "steadfastness": 0.6})
