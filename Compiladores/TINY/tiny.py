from lex import *

def main():
    source = 'ES una PruEBa = 123'
    lexer = Lexer(source)

    while lexer.peek() != '\0':
        print (lexer.curChar)
        lexer.nextChar()


main()