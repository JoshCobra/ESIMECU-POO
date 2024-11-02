def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")


if __name__ == '__main__':
    main()

"""Trata de crear un directorio llamado config.txt en la misma ubicación que el archivo config.py y ejecuta el script.
Deberías ver el mensaje "Couldn't find the config.txt file!" en la consola. Ahora, elimina el archivo config.txt y ejecuta el script nuevamente.
Deberías ver el mismo mensaje de error en la consola. Ahora, crea un archivo config.txt en la misma ubicación que el archivo config.py y ejecuta el script.
Deberías ver que el script se ejecuta sin errores."""

"""Este es el problema por eso agregamos ahora una nueva condición para que el programa no se detenga y siga ejecutándose, "except IsADirectoryError:" """
"""
def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
"""

"""Ahora, si config.txt es un directorio, verás el mensaje "Found config.txt but it is a directory, couldn't read it" en la consola."""