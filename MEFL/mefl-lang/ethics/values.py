class EthicalValue:
    def __init__(self, name, description, priority=1):
        self.name = name
        self.description = description
        self.priority = priority

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"

class Duty(EthicalValue): pass
class Virtue(EthicalValue): pass
class Principle(EthicalValue): pass
class Value(EthicalValue): pass
