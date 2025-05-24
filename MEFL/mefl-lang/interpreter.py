from stdlib.builtins import get_builtins  # If you have this module
from ethics.values import Duty, Virtue, Principle, Value  # If this is relevant

def run(ast):
    env = {}

    # === 1. Bind built-in ethics classes/functions into the global environment ===
    env.update({
        "Duty": Duty,
        "Virtue": Virtue,
        "Principle": Principle,
        "Value": Value
    })

    # === 2. Add any built-in functions you have ===
    env.update(get_builtins())

    def eval_expr(expr, local_env):
        if expr[0] == "number":
            return float(expr[1])
        elif expr[0] == "string":
            return expr[1].strip('"')
        elif expr[0] == "var":
            return local_env.get(expr[1], env.get(expr[1], None))
        elif expr[0] == "call":
            _, name, args = expr
            func = env.get(name)
            if not func:
                raise Exception(f"Function '{name}' not found")
            # Native Python callables (e.g., Duty, Virtue, etc.)
            if callable(func):
                evaled_args = [eval_expr(arg, local_env) for arg in args]
                return func(*evaled_args)
            # User-defined function
            elif isinstance(func, tuple) and func[0] == "function":
                _, _, params, body = func
                if len(args) != len(params):
                    raise Exception("Argument count mismatch")
                local_vars = {param: eval_expr(arg, local_env) for param, arg in zip(params, args)}
                result, did_return = run_block(body, local_vars)
                return result
            else:
                raise Exception(f"Cannot call object '{name}'")
        else:
            raise Exception(f"Unknown expr type {expr[0]}")

    def run_block(block, local_env):
        for stmt in block:
            result, did_return = run_stmt(stmt, local_env)
            if did_return:
                return result, True
        return None, False

    def run_stmt(stmt, local_env):
        if stmt[0] == "let":
            _, name, expr = stmt
            local_env[name] = eval_expr(expr, local_env)
            return None, False
        elif stmt[0] == "print":
            val = eval_expr(stmt[1], local_env)
            print(val)
            return None, False
        elif stmt[0] == "return":
            val = eval_expr(stmt[1], local_env)
            return val, True
        elif stmt[0] == "expr":
            eval_expr(stmt[1], local_env)
            return None, False
        elif stmt[0] == "function":
            name = stmt[1]
            env[name] = stmt
            return None, False
        else:
            raise Exception(f"Unknown statement type {stmt[0]}")

    for stmt in ast:
        _, did_return = run_stmt(stmt, env)
        if did_return:
            break