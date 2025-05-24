# functions.py

class Function:
    def __init__(self, name, param_names, body, closure=None):
        self.name = name
        self.param_names = param_names
        self.body = body
        self.closure = closure or {}

    def call(self, args, call_context):
        # Create new local context with closure + params
        local_context = self.closure.copy()
        if len(args) != len(self.param_names):
            raise TypeError(f"Function {self.name} expected {len(self.param_names)} arguments but got {len(args)}")

        for name, val in zip(self.param_names, args):
            local_context[name] = val

        # Execute body in local context
        return self.body.execute(local_context)

class FunctionDeclaration:
    def __init__(self, func):
        self.func = func

    def execute(self, context):
        context[self.func.name] = self.func
        return None

class ReturnException(Exception):
    def __init__(self, value):
        self.value = value

# Usage inside body execution, raise ReturnException(value) to handle return
