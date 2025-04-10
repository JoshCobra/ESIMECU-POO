import sys
from lex import *
from emit import *

class Parser: 
    def __init__(self, lexer, emitter):
        self.lexer = lexer
        self.emitter = emitter

        self.symbols = set()
        self.labelDeclared = set()
        self.labelsGotoed = set()

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
        self.emitter.headerLine("#include <stdio.h>")
        self.emitter.headerLine("int main(void){")
        
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()

        while not self.checkToken(TokenType.EOF):
            self.statement()

        self.emitter.emitLine("return 0;")
        self.emitter.emitLine("}")

        for label in self.labelsGotoed:
            if label not in self.labelsDeclared:
                self.abort("Intentando GOTO ir a un label no declarado: " + label)

    def statement(self):
        # Checa el primer token para ver que tipo es

        # "PRINT" (expression | string)
        if self.checkToken(TokenType.PRINT):
            self.nextToken()

            if self.checkToken(TokenType.STRING):
                # Simple string, so print it.
                self.emitter.emitLine("printf(\"" + self.curToken.text + "\\n\");")
                self.nextToken()

            else:
                # Expect an expression and print the result as a float.
                self.emitter.emit("printf(\"%" + ".2f\\n\", (float)(")
                self.expression()
                self.emitter.emitLine("));")

        elif self.checkToken(TokenType.IF):
            self.nextToken()
            self.emitter.emit("if(")
            self.comparison()

            self.match(TokenType.THEN)
            self.nl()
            self.emitter.emitLine("){")

            # Zero or more statements in the body.
            while not self.checkToken(TokenType.ENDIF):
                self.statement()

            self.match(TokenType.ENDIF)
            self.emitter.emitLine("}")

        # "WHILE" comparison "REPEAT" block "ENDWHILE"
        elif self.checkToken(TokenType.WHILE):
            self.nextToken()
            self.emitter.emit("while(")
            self.comparasion()

            self.match(TokenType.REPEAT)
            self.nl()
            self.emitter.emitLine("){")

            # Zero or more statements in the loop body.
            while not self.checkToken(TokenType.ENDWHILE):
                self.statement()

            self.match(TokenType.ENDWHILE)
            self.emitter.emitLine("}")

        # "LABEL" ident
        elif self.checkToken(TokenType.LABEL):
            self.nextToken()

            # Make sure this label doesn't already exist.
            if self.curToken.text in self.labelsDeclared:
                self.abort("Label already exists: " + self.curToken.text)
            self.labelsDeclared.add(self.curToken.text)

            self.emitter.emitLine(self.curToken.text + ":")
            self.match(TokenType.IDENT)

        # "GOTO" ident
        elif self.checkToken(TokenType.GOTO):
            self.nextToken()
            self.labelsGotoed.add(self.curToken.text)
            self.emitter.emitLine("goto " + self.curToken.text + ";")
            self.match(TokenType.IDENT)

        # "LET" ident = expression
        elif self.checkToken(TokenType.LET):
            self.nextToken()

            #  Check if ident exists in symbol table. If not, declare it.
            if self.curToken.text not in self.symbols:
                self.symbols.add(self.curToken.text)
                self.emitter.headerLine("float " + self.curToken.text + ";")

            self.emitter.emit(self.curToken.text + " = ")
            self.match(TokenType.IDENT)
            self.match(TokenType.EQ)
            
            self.expression()
            self.emitter.emitLine(";")

        # "INPUT" ident
        elif self.checkToken(TokenType.INPUT):
            print("STATEMENT-INPUT")
            self.nextToken()

            if self.curToken.text not in self.symbols:
                self.symbols.add(self.curToken.text)

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
            if self.curToken.text not in self.symbols:
                self.abort("Se referencio una variable antes de assignarla: " + self.curToken.text)
            self.nextToken()
        else:
            # Error!
            self.abort("Token inesperado en: " + self.curToken.text)
    
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
    