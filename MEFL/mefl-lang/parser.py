def parse(tokens):
    i = 0

    def parse_expression():
        nonlocal i
        if i >= len(tokens):
            return None
        token_type, value = tokens[i]
        if token_type == "NUMBER":
            i += 1
            return ("number", value)
        elif token_type == "STRING":
            i += 1
            return ("string", value)
        elif token_type == "IDENT":
            # Could be variable or function call
            if i + 1 < len(tokens) and tokens[i + 1][0] == "LPAREN":
                func_name = value
                i += 2  # skip IDENT and LPAREN
                args = []
                # Handle empty argument list
                if tokens[i][0] == "RPAREN":
                    i += 1  # skip RPAREN
                    return ("call", func_name, args)
                while True:
                    args.append(parse_expression())
                    if tokens[i][0] == "COMMA":
                        i += 1
                    elif tokens[i][0] == "RPAREN":
                        i += 1
                        break
                    else:
                        raise SyntaxError(f"Expected ',' or ')' but got {tokens[i]}")
                return ("call", func_name, args)
            else:
                i += 1
                return ("var", value)
        else:
            raise SyntaxError(f"Unexpected token in expression: {tokens[i]}")

    def parse_block():
        nonlocal i
        if tokens[i][0] != "LBRACE":
            raise SyntaxError(f"Expected '{{' at start of block, got {tokens[i]}")
        i += 1  # skip LBRACE
        body = []
        while i < len(tokens) and tokens[i][0] != "RBRACE":
            stmt = parse_statement()
            body.append(stmt)
        if i >= len(tokens) or tokens[i][0] != "RBRACE":
            raise SyntaxError("Expected '}' at end of block")
        i += 1  # skip RBRACE
        return body

    def parse_statement():
        nonlocal i
        if i >= len(tokens):
            return None

        token_type, token_value = tokens[i]

        if token_type == "LET":
            i += 1
            if tokens[i][0] != "IDENT":
                raise SyntaxError(f"Expected identifier after 'let', got {tokens[i]}")
            var_name = tokens[i][1]
            i += 1
            if tokens[i][0] != "EQUAL":
                raise SyntaxError(f"Expected '=' after variable name, got {tokens[i]}")
            i += 1
            expr = parse_expression()
            if tokens[i][0] != "SEMICOLON":
                raise SyntaxError(f"Expected ';' after let statement, got {tokens[i]}")
            i += 1
            return ("let", var_name, expr)

        elif token_type == "PRINT":
            i += 1
            expr = parse_expression()
            if tokens[i][0] != "SEMICOLON":
                raise SyntaxError(f"Expected ';' after print statement, got {tokens[i]}")
            i += 1
            return ("print", expr)

        elif token_type == "FUNCTION":
            i += 1
            if tokens[i][0] != "IDENT":
                raise SyntaxError(f"Expected function name after 'function', got {tokens[i]}")
            func_name = tokens[i][1]
            i += 1
            if tokens[i][0] != "LPAREN":
                raise SyntaxError(f"Expected '(' after function name, got {tokens[i]}")
            i += 1
            params = []
            while tokens[i][0] != "RPAREN":
                if tokens[i][0] == "IDENT":
                    params.append(tokens[i][1])
                    i += 1
                elif tokens[i][0] == "COMMA":
                    i += 1
                else:
                    raise SyntaxError(f"Unexpected token in function parameters: {tokens[i]}")
            i += 1  # skip RPAREN
            body = parse_block()
            return ("function", func_name, params, body)

        elif token_type == "RETURN":
            i += 1
            expr = parse_expression()
            if tokens[i][0] != "SEMICOLON":
                raise SyntaxError(f"Expected ';' after return statement, got {tokens[i]}")
            i += 1
            return ("return", expr)

        else:
            expr = parse_expression()
            if tokens[i][0] == "SEMICOLON":
                i += 1
                return ("expr", expr)
            else:
                raise SyntaxError(f"Unexpected token {tokens[i]}")

    ast = []
    while i < len(tokens):
        stmt = parse_statement()
        if stmt is None:
            break
        ast.append(stmt)
    return ast
