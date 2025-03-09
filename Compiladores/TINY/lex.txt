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
        pass

    # Saltar espacios en blanco excepto salto de linea que
    # indicara el final de una instrucción
    def skipWhitespace(self):
        pass 

    # Saltar comentarios en el código
    def skipComment(self):
        pass

    # Regresar el siguiente token
    def getToken(self):
        if self.curChar == '+': # Token de Suma
            pass
        elif self.curChar == '-': # Token de Resta
            pass
        elif self.curChar == '*': # Token de Multiplicación
            pass
        elif self.curChar == '/': # Token de Slash
            pass
        elif self.curChar == '\0': # EOF Token
            pass
        else:
            # Token no identificado
            pass

        self.nextChar()
