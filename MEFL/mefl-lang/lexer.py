import re

def tokenize(code):
    keywords = {
        "let": "LET",
        "print": "PRINT",
        "function": "FUNCTION",
        "return": "RETURN"
    }

    token_specification = [
        ("NUMBER",    r'\d+(\.\d*)?'),
        ("STRING",    r'"[^"]*"'),
        ("IDENT",     r'[A-Za-z_][A-Za-z0-9_]*'),
        ("EQUAL",     r'='),
        ("LPAREN",    r'\('),
        ("RPAREN",    r'\)'),
        ("LBRACE",    r'\{'),
        ("RBRACE",    r'\}'),
        ("COMMA",     r','),
        ("SEMICOLON", r';'),
        ("SKIP",      r'[ \t\n]+'),
        ("MISMATCH",  r'.')
    ]


    tok_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in token_specification)
    get_token = re.compile(tok_regex).match
    pos = 0
    tokens = []
    while pos < len(code):
        match = get_token(code, pos)
        if not match:
            raise SyntaxError(f'Unexpected character: {code[pos]}')
        kind = match.lastgroup
        value = match.group()
        if kind == "SKIP":
            pass
        elif kind == "IDENT" and value in keywords:
            tokens.append((keywords[value], value))
        elif kind == "MISMATCH":
            raise SyntaxError(f'Unexpected character: {value}')
        else:
            tokens.append((kind, value))
        pos = match.end()
    return tokens
