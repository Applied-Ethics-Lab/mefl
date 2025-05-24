def detect_conflict(values):
    seen = {}
    for val in values:
        if val.name in seen:
            return True, val.name
        seen[val.name] = True
    return False, None
