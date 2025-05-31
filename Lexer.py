TT_NUM = 0
TT_PLUS = 1
TT_MINUS = 2
TT_MUL = 3
TT_DIV = 4

TT_LP = 5
TT_RP = 6

class Token:
    def __init__(self, tokenType, tokenValue=None):
        self.tokenType = tokenType
        self.tokenValue = tokenValue
    
    def __repr__(self):
        tokenType = ''
        if self.tokenType == TT_PLUS:
            tokenType = '+'
        elif self.tokenType == TT_MINUS:
            tokenType = '-'
        elif self.tokenType == TT_MUL:
            tokenType = '*'
        elif self.tokenType == TT_DIV:
            tokenType = '/'
        elif self.tokenType == TT_NUM:
            tokenType = 'NUM'

        return f'({tokenType} : {self.tokenValue})'


class Lexer:
    def __init__(self, code):
        self.code = code
        self.index = 0
        self.current = self.code[self.index]
    
    def advance(self):
        if self.index < len(self.code) - 1:
            self.index += 1
            self.current = self.code[self.index]
        else:
            self.index = -1
            self.current = None
    
    def lex(self):
        tokens = []

        while self.current != None:
            if self.current in ' \t\n\0':
                self.advance()
            elif self.current == '+':
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current == '-':
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current == '*':
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current == '/':
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current == '(':
                tokens.append(Token(TT_LP))
                self.advance()
            elif self.current == ')':
                tokens.append(Token(TT_RP))
                self.advance()
            elif self.current in '0123456789':
                tokens.append(Token(TT_NUM, self.lex_number()))
            else:
                raise Exception('Syntax Issue: Invalid Character')
        
        return tokens

    def lex_number(self):
        dot = 0
        numStr = ''

        while self.current != None and self.current in '0123456789.':
            if self.current == '.':
                dot += 1
            
            if dot > 1:
                raise Exception('Number Invalid')
            
            numStr += self.current
            self.advance()

        return float(numStr)
