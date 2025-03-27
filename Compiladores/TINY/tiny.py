from lex import *

def main():
    source = "# Comentario!\n IF 125  - ** == = /"
    lexer = Lexer(source)

    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()

main()