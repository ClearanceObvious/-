from Parser import *

TT_PLUS = 1
TT_MINUS = 2
TT_MUL = 3
TT_DIV = 4

class Interpreter:
    def __init__(self, root):
        self.root = root
    
    def visitExpression(self, expr):
        if isinstance(expr, NumberNode):
            return expr
        elif isinstance(expr, BinOpNode):
            return self.visitBinOpNode(expr)
    
    def visitBinOpNode(self, binopnode):
        left = self.visitExpression(binopnode.left)
        right = self.visitExpression(binopnode.right)

        if binopnode.op == TT_PLUS:
            return NumberNode(left.value + right.value)
        elif binopnode.op == TT_MINUS:
            return NumberNode(left.value - right.value)
        elif binopnode.op == TT_MUL:
            return NumberNode(left.value * right.value)
        elif binopnode.op == TT_DIV:
            if right.value == 0:
                raise Exception(f'Cannot divide number {left.value} by 0')

            return NumberNode(left.value / right.value)                        

    
    def evaluate(self):
        print(self.visitExpression(self.root))