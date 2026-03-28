from .ast import (
    ProgramNode,
    VariableNode,
    PrintNode,
    NumberNode,
    StringNode,
    BinOpNode,
    VarAccessNode,
<<<<<<< HEAD
    IfNode,
=======
>>>>>>> c5d6ec72ac4d610ae9c4d4cf698623e5828b36f8
)


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def parse(self):
        statements = []

        while self.position < len(self.tokens):
            token_type, token_value = self.tokens[self.position]

            if token_type == "VAR":
                statements.append(self.parse_variable())

            elif token_type == "PRINT":
                statements.append(self.parse_print())

<<<<<<< HEAD
            elif token_type == "IF":
                statements.append(self.parse_if())

=======
>>>>>>> c5d6ec72ac4d610ae9c4d4cf698623e5828b36f8
            else:
                self.position += 1

        return ProgramNode(statements)

    def parse_variable(self):
        self.position += 1  # skip VAR
<<<<<<< HEAD
=======

>>>>>>> c5d6ec72ac4d610ae9c4d4cf698623e5828b36f8
        token_type, name = self.tokens[self.position]

        if token_type != "IDENTIFIER":
            raise Exception("Expected variable name")

        self.position += 1
<<<<<<< HEAD
=======

>>>>>>> c5d6ec72ac4d610ae9c4d4cf698623e5828b36f8
        token_type, arrow = self.tokens[self.position]

        if arrow != "->":
            raise Exception("Expected '->' in variable declaration")

        self.position += 1
<<<<<<< HEAD
=======

>>>>>>> c5d6ec72ac4d610ae9c4d4cf698623e5828b36f8
        expr_tokens = []

        while (
            self.position < len(self.tokens)
            and self.tokens[self.position][0] != "NEWLINE"
        ):
            expr_tokens.append(self.tokens[self.position])
            self.position += 1

        expression = self.parse_expression(expr_tokens)
<<<<<<< HEAD
=======

>>>>>>> c5d6ec72ac4d610ae9c4d4cf698623e5828b36f8
        return VariableNode(name, expression)

    def parse_print(self):
        self.position += 1  # skip PRINT
<<<<<<< HEAD
=======

>>>>>>> c5d6ec72ac4d610ae9c4d4cf698623e5828b36f8
        expr_tokens = []

        while (
            self.position < len(self.tokens)
            and self.tokens[self.position][0] != "NEWLINE"
        ):
            expr_tokens.append(self.tokens[self.position])
            self.position += 1

        return PrintNode(self.parse_expression(expr_tokens))

<<<<<<< HEAD
    def parse_if(self):
        self.position += 1  # skip IF
        expr_tokens = []

        while (
            self.position < len(self.tokens)
            and self.tokens[self.position][0] != "NEWLINE"
        ):
            expr_tokens.append(self.tokens[self.position])
            self.position += 1

        condition = self.parse_expression(expr_tokens)
        body = []
        else_body = []

        # Handle indentation (basic version)
        if self.position < len(self.tokens) and self.tokens[self.position][0] == "INDENT":
            self.position += 1
            while self.tokens[self.position][0] != "DEDENT":
                token_type, token_value = self.tokens[self.position]
                if token_type == "VAR":
                    body.append(self.parse_variable())
                elif token_type == "PRINT":
                    body.append(self.parse_print())
                else:
                    self.position += 1
            self.position += 1  # skip DEDENT

        return IfNode(condition, body, else_body)

    # -----------------------
    # Expression parsing
    # -----------------------
    def parse_expression(self, tokens):
        self.expr_tokens = tokens
        self.expr_pos = 0
        return self.parse_logic()

    # Handles 'and' / 'or'
    def parse_logic(self):
        node = self.parse_comparison()

        while self.expr_pos < len(self.expr_tokens):
            token_type, token_value = self.expr_tokens[self.expr_pos]

            if token_type in ("AND", "OR"):
                op = token_type.lower()
                self.expr_pos += 1
                right = self.parse_comparison()
                node = BinOpNode(node, op, right)
            else:
                break

        return node

    def parse_comparison(self):
        left = self.parse_term()
        comparisons = []

        while (
            self.expr_pos < len(self.expr_tokens)
            and self.expr_tokens[self.expr_pos][1] in ("==", "!=", ">", "<", ">=", "<=")
        ):
            op = self.expr_tokens[self.expr_pos][1]
            self.expr_pos += 1
            right = self.parse_term()
            comparisons.append((left, op, right))
            left = right

        if not comparisons:
            return left

        node = BinOpNode(comparisons[0][0], comparisons[0][1], comparisons[0][2])
        for comp in comparisons[1:]:
            next_node = BinOpNode(comp[0], comp[1], comp[2])
            node = BinOpNode(node, "and", next_node)
        return node

    def parse_term(self):
        node = self.parse_factor()
=======
    def parse_expression(self, tokens):
        self.expr_tokens = tokens
        self.expr_pos = 0
        return self.parse_comparison()

    def parse_term(self):
        node = self.parse_factor()

>>>>>>> c5d6ec72ac4d610ae9c4d4cf698623e5828b36f8
        while (
            self.expr_pos < len(self.expr_tokens)
            and self.expr_tokens[self.expr_pos][1] in ("+", "-")
        ):
            op = self.expr_tokens[self.expr_pos][1]
            self.expr_pos += 1
            right = self.parse_factor()
            node = BinOpNode(node, op, right)
<<<<<<< HEAD
        return node

    def parse_factor(self):
        token_type, token_value = self.expr_tokens[self.expr_pos]

        if token_type == "NOT":
            self.expr_pos += 1
            node = self.parse_factor()
            return BinOpNode(None, "not", node)

=======

        return node

    def parse_factor(self):
>>>>>>> c5d6ec72ac4d610ae9c4d4cf698623e5828b36f8
        node = self.parse_atom()

        while (
            self.expr_pos < len(self.expr_tokens)
            and self.expr_tokens[self.expr_pos][1] in ("*", "/")
        ):
            op = self.expr_tokens[self.expr_pos][1]
            self.expr_pos += 1
            right = self.parse_atom()
            node = BinOpNode(node, op, right)

        return node

    def parse_atom(self):
        token_type, token_value = self.expr_tokens[self.expr_pos]

        # Parentheses
        if token_value == "(":
            self.expr_pos += 1
<<<<<<< HEAD
            node = self.parse_logic()
=======
            node = self.parse_comparison()
>>>>>>> c5d6ec72ac4d610ae9c4d4cf698623e5828b36f8
            self.expr_pos += 1
            return node

        # Number
        if token_type == "NUMBER":
            self.expr_pos += 1
            return NumberNode(token_value)

        # String
        if token_type == "STRING":
            self.expr_pos += 1
            return StringNode(token_value)

<<<<<<< HEAD
        # Variable
=======
        # Variable access
>>>>>>> c5d6ec72ac4d610ae9c4d4cf698623e5828b36f8
        if token_type == "IDENTIFIER":
            self.expr_pos += 1
            return VarAccessNode(token_value)

<<<<<<< HEAD
        raise Exception(f"Unexpected token: {token_value}")
=======
        raise Exception(f"Unexpected token: {token_value}")

    def parse_comparison(self):
        left = self.parse_term()

        comparisons = []

        while (
            self.expr_pos < len(self.expr_tokens)
            and self.expr_tokens[self.expr_pos][1]
            in ("==", "!=", ">", "<", ">=", "<=")
        ):
            op = self.expr_tokens[self.expr_pos][1]
            self.expr_pos += 1
            right = self.parse_term()

            comparisons.append((left, op, right))
            left = right

        if not comparisons:
            return left

        node = BinOpNode(
            comparisons[0][0],
            comparisons[0][1],
            comparisons[0][2],
        )

        for comp in comparisons[1:]:
            next_node = BinOpNode(comp[0], comp[1], comp[2])
            node = BinOpNode(node, "and", next_node)

        return node
>>>>>>> c5d6ec72ac4d610ae9c4d4cf698623e5828b36f8
