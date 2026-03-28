class ProgramNode:
    def __init__(self, statements):
        self.statements = statements


class VariableNode:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class PrintNode:
    def __init__(self, value):
        self.value = value


class NumberNode:
    def __init__(self, value):
        self.value = value


class StringNode:
    def __init__(self, value):
        self.value = value
<<<<<<< HEAD


class BinOpNode:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right
=======
>>>>>>> c5d6ec72ac4d610ae9c4d4cf698623e5828b36f8


class VarAccessNode:
    def __init__(self, name):
        self.name = name


<<<<<<< HEAD
class IfNode:
    def __init__(self, condition, body, else_body=None):
        self.condition = condition
        self.body = body
        self.else_body = else_body



class UnaryOpNode:
    def __init(self, operator, node):
        self.operator = operator
        self.node = node

=======
class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
>>>>>>> c5d6ec72ac4d610ae9c4d4cf698623e5828b36f8
