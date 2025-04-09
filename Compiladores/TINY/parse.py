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

        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()

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
            self.comparasion()

            self.match(TokenType.THEN)
            self.nl()

            while not self.checkToken(TokenType.ENDIF):
                self.statement()
            
            self.match(TokenType.ENDIF)

        elif self.checkToken(TokenType.WHILE):
            print("STATEMENT-WHILE")
            self.nextToken()
            self.comparasion()

            self.match(TokenType.REPEAT)
            self.nl()

            while not self.checkToken(TokenType.ENDWHILE):
                self.statement()

            self.match(TokenType.ENDWHILE)

        elif self.checkToken(TokenType.LABEL):
            print("STATEMENT-LABEL")
            self.nextToken()
            self.match(TokenType.IDENT)

        # "GOTO" ident
        elif self.checkToken(TokenType.GOTO):
            print("STATEMENT-GOTO")
            self.nextToken()
            self.match(TokenType.IDENT)

        # "LET" ident "=" expression
        elif self.checkToken(TokenType.LET):
            print("STATEMENT-LET")
            self.nextToken()
            self.match(TokenType.IDENT)
            self.match(TokenType.EQ)
            self.expression()

        # "INPUT" ident
        elif self.checkToken(TokenType.INPUT):
            print("STATEMENT-INPUT")
            self.nextToken()
            self.match(TokenType.IDENT)

        # This is not a valid statement. Error!
        else:
            self.abort("Statement Invalido en " + self.curToken.text + " (" + self.curToken.kind.name + ")")

        # Nueva linea.
        self.nl()

    def nl(self):
        print("NEWLINE")

        # Requiere al menos una nueva linea
        self.match(TokenType.NEWLINE)
        # También permite multiples lineas
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()

    def primary(self):
        print("PRIMARY (" + self.curToken.text + ")")

        if self.checkToken(TokenType.NUMBER): 
            self.nextToken()
        elif self.checkToken(TokenType.IDENT):
            self.nextToken()
        else:
            # Error!
            self.abort("Unexpected token at " + self.curToken.text)
    
    def term(self):
        print("TERM")

        self.unary()
        # Puede tener 0 o mas *// y expresiones.
        while self.checkToken(TokenType.ASTERISK) or self.checkToken(TokenType.SLASH):
            self.nextToken()
            self.unary()

    # unary ::= ["+" | "-"] primary
    def unary(self):
        print("UNARY")

        if self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS):
            self.nextToken()        
        self.primary()

    def expression(self):
        print("EXPRESSION")

        self.term()
        # Puede tener 0 o mas +/-  y expresiones.
        while self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS):
            self.nextToken()
            self.term()

    def comparasion(self):
        print("COMPARASION")

        self.expression()
        if self.isComparasionOperator():
            self.nextToken()
            self.expression()
        else:
            self.abort("Se esperaba un operador de comparasion en: " + self.curToken.text)

        while self.isComparasionOperator():
            self.nextToken()
            self.expression()

    def isComparasionOperator(self):
        return self.checkToken(TokenType.GT) or self.checkToken(TokenType.GTEQ) or self.checkToken(TokenType.LT) or self.checkToken(TokenType.LTEQ) or self.checkToken(TokenType.EQEQ) or self.checkToken(TokenType.NOTEQ)
    