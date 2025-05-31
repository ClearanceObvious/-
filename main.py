from Lexer import Lexer
from Parser import Parser
from Interpreter import Interpreter

code = ''

while code != 'exit':
    code = input('>> ')

    lexer = Lexer(code)
    tokens = lexer.lex()

    parser = Parser(tokens)
    ast = parser.parse_expression()

    interpreter = Interpreter(ast)
    interpreter.evaluate()