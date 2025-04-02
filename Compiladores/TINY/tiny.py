from lex import *
from parse import *
import sys

def main():
    print ("Compilador TINY")

    if len(sys.argv) !=2:
        sys.exit("Error! El compilador necesita un archivo como argumento")
    with open(sys.argv[1], 'r') as inputFile:
        source = inputFile.read()

    # Inicializamos el lexer    
    lexer = Lexer(source)
    parser = Parser(lexer)

    parser.program() #Iniciar el Parser
    print("Análisis Sintáctico Terminado")

main()