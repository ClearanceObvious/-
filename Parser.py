TT_NUM = 0
TT_PLUS = 1
TT_MINUS = 2
TT_MUL = 3
TT_DIV = 4

TT_LP = 5
TT_RP = 6

class NumberNode:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f'{self.value}'

class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.right = right
        self.op = op

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
        self.current = self.tokens[self.index]
    
    def advance(self):
        if self.index < len(self.tokens) - 1:
            self.index += 1
            self.current = self.tokens[self.index]
        else:
            self.index = -1
            self.current = None

    def parse_factor(self):
        number = None
        if self.current != None:
            if self.current.tokenType == TT_NUM:
                number = NumberNode(self.current.tokenValue)
                self.advance()
            elif self.current.tokenType == TT_LP:
                self.advance()
                number = self.parse_expression()
                if self.current.tokenType == TT_RP:
                    self.advance()
                else:
                    raise Exception('Expected ")" when closing expression')
            else:
                raise Exception('Parser Issue: No Number Found!')
        else:
            raise Exception('Parser Issue: No Number Found!')
        
        return number
    
    def parse_term(self):
        left = self.parse_factor()

        while self.current != None and self.current.tokenType in (TT_MUL, TT_DIV):
            tokenType = self.current.tokenType
            self.advance()

            left = BinOpNode(left, tokenType, self.parse_factor())
        
        return left

    def parse_expression(self):
        left = self.parse_term()

        while self.current != None and self.current.tokenType in (TT_PLUS, TT_MINUS):
            tokenType = self.current.tokenType
            self.advance()

            left = BinOpNode(left, tokenType, self.parse_term())
        
        return left