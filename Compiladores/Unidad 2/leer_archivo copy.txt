def leer_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

# Ejemplo de uso
ruta_archivo = 'ruta/al/archivo.txt'
leer_archivo(ruta_archivo)