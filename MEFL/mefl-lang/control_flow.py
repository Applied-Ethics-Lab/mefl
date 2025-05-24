# control_flow.py

class IfStatement:
    def __init__(self, condition_expr, then_block, else_block=None):
        self.condition_expr = condition_expr
        self.then_block = then_block
        self.else_block = else_block

    def execute(self, context):
        if self.condition_expr.evaluate(context):
            return self.then_block.execute(context)
        elif self.else_block:
            return self.else_block.execute(context)
        return None

class WhileLoop:
    def __init__(self, condition_expr, body_block):
        self.condition_expr = condition_expr
        self.body_block = body_block

    def execute(self, context):
        result = None
        while self.condition_expr.evaluate(context):
            result = self.body_block.execute(context)
        return result

class ForLoop:
    def __init__(self, init_stmt, condition_expr, update_stmt, body_block):
        self.init_stmt = init_stmt
        self.condition_expr = condition_expr
        self.update_stmt = update_stmt
        self.body_block = body_block

    def execute(self, context):
        result = None
        self.init_stmt.execute(context)
        while self.condition_expr.evaluate(context):
            result = self.body_block.execute(context)
            self.update_stmt.execute(context)
        return result
