try:
    open('config.txt')
except FileNotFoundError:
    print("Archivo no encontrado")

""" El operador try se utiliza para manejar excepciones. Un bloque try se ejecuta hasta que se lanza una excepción.
    Cuando se lanza una excepción, el bloque try se detiene y se pasa al bloque except. Si no se lanza ninguna excepción, el bloque except no se ejecuta."""

"""Obtenemos como resultado:
Archivo no encontrado"""