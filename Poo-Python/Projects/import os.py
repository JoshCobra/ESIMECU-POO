import os
import sqlite3

# Configuración de las carpetas
library_dir = './library/'
lists_dir = './lists/'

# Asegurarse de que las carpetas existen
os.makedirs(library_dir, exist_ok=True)
os.makedirs(lists_dir, exist_ok=True)

# Conexión a la base de datos SQLite
conn = sqlite3.connect('library.db')
c = conn.cursor()

# Crear tabla para gestionar la organización de listas
c.execute('''
CREATE TABLE IF NOT EXISTS file_lists (
    id INTEGER PRIMARY KEY,
    list_name TEXT NOT NULL,
    file_name TEXT NOT NULL
)
''')
conn.commit()

# Función para agregar un archivo a la biblioteca
def add_file_to_library(file_path):
    if os.path.exists(file_path):
        file_name = os.path.basename(file_path)
        destination = os.path.join(library_dir, file_name)
        if not os.path.exists(destination):
            os.symlink(file_path, destination)
            print(f'Archivo {file_name} añadido a la biblioteca.')
        else:
            print(f'El archivo {file_name} ya existe en la biblioteca.')
    else:
        print(f'El archivo {file_path} no existe.')

# Función para crear una lista y añadir archivos desde la biblioteca
def add_file_to_list(file_name, list_name):
    # Crear carpeta para la lista si no existe
    list_path = os.path.join(lists_dir, list_name)
    os.makedirs(list_path, exist_ok=True)
    
    # Crear enlace simbólico del archivo en la lista
    original_file = os.path.join(library_dir, file_name)
    if os.path.exists(original_file):
        link_path = os.path.join(list_path, file_name)
        if not os.path.exists(link_path):
            os.symlink(original_file, link_path)
            # Guardar la referencia en la base de datos
            c.execute('INSERT INTO file_lists (list_name, file_name) VALUES (?, ?)', (list_name, file_name))
            conn.commit()
            print(f'Archivo {file_name} añadido a la lista "{list_name}".')
        else:
            print(f'El archivo {file_name} ya está en la lista "{list_name}".')
    else:
        print(f'El archivo {file_name} no existe en la biblioteca.')

# Función para mostrar todos los archivos en una lista
def show_files_in_list(list_name):
    c.execute('SELECT file_name FROM file_lists WHERE list_name = ?', (list_name,))
    files = c.fetchall()
    if files:
        print(f'Archivos en la lista "{list_name}":')
        for file in files:
            print(f'- {file[0]}')
    else:
        print(f'La lista "{list_name}" está vacía o no existe.')

# Ejemplo de uso
if __name__ == "__main__":
    # Agregar un archivo a la biblioteca
    add_file_to_library("D:\Descargas\luca-ercolani-GFTMZJfh1nU-unsplash.jpg")
    
    # Crear una lista y agregar un archivo
    add_file_to_list('luca-ercolani-GFTMZJfh1nU-unsplash.jpg', 'Mi Lista Favorita')
    
    # Mostrar archivos en la lista
    show_files_in_list('Mi Lista Favorita')
