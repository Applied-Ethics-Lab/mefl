# utils.py

class MEFLRuntimeError(Exception):
    pass

class MEFLSyntaxError(Exception):
    pass

def error(msg):
    raise MEFLRuntimeError(msg)

def syntax_error(msg):
    raise MEFLSyntaxError(msg)

def is_truthy(value):
    """
    Define truthiness for MEFL values.
    """
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value != 0
    if isinstance(value, str):
        return len(value) > 0
    # Extend as needed
    return True
