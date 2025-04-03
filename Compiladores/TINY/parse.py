import sys
from lex import *

class Parser: 
    def __init__(self, lexer):
        self.lexer = lexer

        self.curToken = None
        self.peekToken = None
        self.nextToken()
        self.nextToken()

    # Devolverá True si el token corresponde
    def checkToken(self, kind):
        return kind == self.curToken.kind

    # Devuelve True si el token siguiente corresponde
    def checkPeek(self, kind):
        return kind == self.peekToken.kind

    # Intenta match el token actual, si no, error
    def match(self, kind):
        if not self.checkToken(kind):
            self.abort(f'Se esperaba {kind.name}, se obtuvo: {self.curToken.kind.name}')
            self.nextToken()

    # Avanza al siguiente token
    def nextToken(self):
        self.curToken = self.peekToken
        self.peekToken = self.lexer.getToken()

    def abort(self, message):
        sys.exit(f'Error {message}')

    def program(self):
        print("PROGRAM")

        while not self.checkToken(TokenType.EOF):
            self.statement()

    def statement(self):
        # Checa el primer token para ver que tipo es

        # "PRINT" (expression | string)
        if self.checkToken(TokenType.PRINT):
            print("STATEMENT-PRINT")
            self.nextToken()

            if self.checkToken(TokenType.STRING):
                # String simple.
                self.nextToken()
            else:
                # Espera una expresion.
                self.expression()

        elif self.checkToken(TokenType.IF):
            print("STATEMENT-IF")
            self.nextToken()
            # self.comparasion()
        

        # Nueva linea.
        self.nl()

    def nl(self):
        print("NEWLINE")

        # Requiere al menos una nueva linea
        self.match(TokenType.NEWLINE)
        # También permite multiples lineas
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()