import sys
import enum

class Lexer:
    def __init__(self, source):
        self.source = source + '\n'
        self.curChar = '' # Caracter actual en el string
        self.curPos = -1 # Posición actual del caracter en el string
        self.nextChar()

    # Procesar el siguiente caracter
    def nextChar(self):
        self.curPos += 1
        if self.curPos >= len(self.source):
            self.curChar = '\0' # Coloca el caracter en EOF (end-of-file marker) 
                                # \0 es el caracter nulo
        else:
            self.curChar = self.source[self.curPos]

    # Devolver el caracter 
    def peek(self):
        if self.curPos + 1 >= len(self.source):
            return '\0'
        return self.source[self.curPos + 1]

    # Token invalido, imprimir mensaje de error y salir
    def abort(self, message):
        sys.exit(f'Lexing error: {message}')

    # Saltar espacios en blanco excepto salto de linea que
    # indicara el final de una instrucción
    def skipWhitespace(self):
        while self.curChar == ' ' or self.curChar == '\t' or self.curChar == '\r':
            self.nextChar()

    # Saltar comentarios en el código
    def skipComment(self):
        pass

    # Regresar el siguiente token
    def getToken(self):
        self.skipWhitespace()
        token = None 

        if self.curChar == '+': # Token de Suma
            token = Token(self.curChar, TokenType.PLUS)

        elif self.curChar == '-': # Token de Resta
            token = Token(self.curChar, TokenType.MINUS)

        elif self.curChar == '*': # Token de Multiplicación
            token = Token(self.curChar, TokenType.ASTERISK)

        elif self.curChar == '/': # Token de Slash
            token = Token(self.curChar, TokenType.SLASH)
        
        elif self.curChar == '=': 
            # Revisar si el token es = o ==
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.EQEQ)
            else: 
                token = Token(self.curChar, TokenType.EQ)

        elif self.curChar == '>':
            # Revisar si el token es > o >=
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.GTEQ)
            else:
                token = Token(self.curChar, TokenType.GT)
        elif self.curChar == '<':
                # Revisar si el token es < o <=
                if self.peek() == '=':
                    lastChar = self.curChar
                    self.nextChar()
                    token = Token(lastChar + self.curChar, TokenType.LTEQ)
                else:
                    token = Token(self.curChar, TokenType.LT)
        elif self.curChar == '!':
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.NOTEQ)
            else:
                self.abort("Se esperaba !=, escribiste !" + self.peek())
        
        elif self.curChar == '\n':
            token = Token(self.curChar, TokenType.NEWLINE)

        elif self.curChar == '\0': # EOF Token
            token = Token(self.curChar, TokenType.EOF)

        else:
            # Token no identificado
            self.abort(f'Token no ha sido identificado: {self.curChar}')
            pass

        self.nextChar()
        return token
    

class Token:
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText
        self.kind = tokenKind

class TokenType(enum.Enum):
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING =3 
    #Keywords
    LABEL = 101
    GOTO = 102
    PRINT = 103
    INPUT = 104
    LET = 105
    IF = 106
    THEN = 107
    ENDIF = 108
    WHILE = 109
    REPEAT =110
    ENDWHILE = 111
    #Operators
    EQ = 201
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT = 208
    LTEQ = 209
    GT = 210
    GTEQ = 211
