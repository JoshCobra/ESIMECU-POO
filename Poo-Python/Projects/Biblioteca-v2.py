import os
import sqlite3
import tkinter as tk
import shutil
from tkinter import filedialog, messagebox, simpledialog

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

def clone_library(destination_path):
    # Clonar la biblioteca
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)  # Crear la ruta de destino si no existe

    # Copiar todos los archivos de la biblioteca
    for item in os.listdir(library_dir):
        source_item = os.path.join(library_dir, item)
        dest_item = os.path.join(destination_path, item)
        
        if os.path.isdir(source_item):
            shutil.copytree(source_item, dest_item)  # Copiar directorio
        else:
            shutil.copy2(source_item, dest_item)  # Copiar archivo

    # Clonar listas
    for list_name in os.listdir(lists_dir):
        source_list = os.path.join(lists_dir, list_name)
        dest_list = os.path.join(destination_path, list_name)
        
        if os.path.isdir(source_list):
            shutil.copytree(source_list, dest_list)  # Copiar directorio de listas

# Funciones de backend (sin interfaz)
def add_files_to_library(file_paths):
    added_files = []
    for file_path in file_paths:
        if os.path.exists(file_path):
            file_name = os.path.basename(file_path)
            destination = os.path.join(library_dir, file_name)
            if not os.path.exists(destination):
                os.symlink(file_path, destination)
                added_files.append(file_name)
                print(f'Archivo {file_name} añadido a la biblioteca.')
            else:
                added_files.append(file_name)
                print(f'El archivo {file_name} ya existe en la biblioteca.')
    return added_files


def add_files_to_list(file_names, list_name):
    # Crear carpeta para la lista si no existe
    list_path = os.path.join(lists_dir, list_name)
    os.makedirs(list_path, exist_ok=True)
    
    for file_name in file_names:
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


def remove_file_from_list(file_name, list_name):
    list_path = os.path.join(lists_dir, list_name)
    file_path = os.path.join(list_path, file_name)

    if os.path.exists(file_path):
        os.remove(file_path)
        #Actualiza la base de datos
        c.execute('DELETE FROM file_lists WHERE list name = ? AND file_name = ?', (list_name,file_name))
        conn.commit()
        print(f'Archivo{file_name} elimiado de la lista {list_name}')
    else:
        print(f'El archivo {file_name} no se encuentra en la lista {list_name}')


def show_files_in_list(list_name):
    c.execute('SELECT file_name FROM file_lists WHERE list_name = ?', (list_name,))
    files = c.fetchall()
    return [file[0] for file in files]

# Interfaz gráfica con Tkinter
class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Tu Gestión de Biblioteca y Listas')
        
        # Widgets

        # Botón para clonar la biblioteca
        self.clone_library_btn = tk.Button(root, text="Clonar Biblioteca", command=self.clone_library_ui)
        self.clone_library_btn.pack(pady=5)

        self.label = tk.Label(root, text="Biblioteca y Listas", font=("Arial", 16))
        self.label.pack(pady=10)
        
        self.add_file_btn = tk.Button(root, text="Agregar Archivos a la Biblioteca General", command=self.add_files)
        self.add_file_btn.pack(pady=5)

        self.show_all_lists_btn = tk.Button(root, text="Mostrar Todas las Listas", command=self.show_all_lists)
        self.show_all_lists_btn.pack(pady=5)
        
        self.create_list_btn = tk.Button(root, text="Agregar archivos a la lista Descrita ", command=self.create_list)
        self.create_list_btn.pack(pady=5)

        self.show_list_btn = tk.Button(root, text="Mostrar Archivos en Lista Descrita", command=self.show_list)
        self.show_list_btn.pack(pady=5)

        #Boton para eliminar archivoss
        self.delete_file_btn = tk.Button(root, text="Eliminar Archivo", command=self.delete_file)
        self.delete_file_btn.pack(pady=5)

        self.list_name_entry = tk.Entry(root, width=30)
        self.list_name_entry.pack(pady=5)
        self.list_name_entry.insert(0, "Nombre de la Lista a Manipular")
        
        self.output_box = tk.Text(root, height=10, width=50)
        self.output_box.pack(pady=10)

        #Llamar la funcion para mostrar todos los archivos de la biblioteca
        self.update_library_view()

    def clone_library_ui(self):
        destination_path = filedialog.askdirectory(title="Seleccionar Ruta de Destino")
        if destination_path:
            clone_library(destination_path)
            messagebox.showinfo("Clonación Completa", "La biblioteca ha sido clonada exitosamente.")


    def add_files(self):
        file_paths = filedialog.askopenfilenames()
        if file_paths:
            added_files = add_files_to_library(file_paths)
            if added_files:
                messagebox.showinfo("Éxito", f'Se añadieron los siguientes archivos a la biblioteca:\n' + "\n".join(added_files))
                self.update_library_view() #Actualiza en tiempo real 
            else:
                messagebox.showwarning("Error", "No se pudo añadir los archivos.")

    def delete_file(self):
        file_name = simpledialog.askstring("Eliminar archivo","Nombre del archivo a eliminar:")
        if not file_name:
            return
        
        choice = messagebox.askquestion("Eliminar Archivo", "Eliminar de la biblioteca?", icon='warning')

        if choice == 'yes': #Eliminar de la biblioteca
            remove_file_from_list(file_name)
            self.update_library_view()   #Actualiza la vista de la biblioteca
        else:
            list_name = simpledialog.askstring("Eliminar de lista", "Nombre de la lista:")
            if list_name:
                remove_file_from_list(file_name, list_name)
                self.show_list() #Actualiza la vista de la lista
    
    def create_list(self):
        list_name = self.list_name_entry.get()
        if list_name:
            file_paths = filedialog.askopenfilenames()
            if file_paths:
                file_names = [os.path.basename(file) for file in file_paths]
                add_files_to_list(file_names, list_name)
                messagebox.showinfo("Éxito", f'Se añadieron los siguientes archivos a la lista "{list_name}":\n' + "\n".join(file_names))

    
    def show_list(self):
        list_name = self.list_name_entry.get()
        if list_name:
            files = show_files_in_list(list_name)
            if files:
                self.output_box.delete(1.0, tk.END)
                self.output_box.insert(tk.END, f'Archivos en la lista "{list_name}":\n')
                for file in files:
                    self.output_box.insert(tk.END, f'- {file}\n')
            else:
                messagebox.showwarning("Error", f'No se encontraron archivos en la lista "{list_name}".')

    def show_all_lists(self):
        lists = [d for d in os.listdir(lists_dir) if os.path.isdir(os.path.join(lists_dir, d))]
        self.output_box.delete(1.0,tk.END) #Limpia el contenido actual
        if lists:
            self.output_box.insert(tk.END, 'Todas las Listas Creadas:\n')
            for list_name in lists:
                self.output_box.insert(tk.END, f'- {list_name}\n')
        else:
            self.output_box.insert(tk.END, 'No hay listas creadas aun')


    def update_library_view(self):
        files = os.listdir(library_dir)
        self.output_box.delete(1.0, tk.END)  # Limpiar el contenido actual
        if files:
            self.output_box.insert(tk.END, 'Archivos en la Biblioteca:\n')
            for file in files:
                self.output_box.insert(tk.END, f'- {file}\n')
        else:
            self.output_box.insert(tk.END, 'No hay archivos en la biblioteca.')


if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
