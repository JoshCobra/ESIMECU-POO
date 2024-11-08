# Realizar una clase que administre una agenda. 
# Se debe almacenar para cada contacto el nombre, el teléfono y el email. 
# Además, deberá mostrar un menú con las siguientes opciones 

# Añadir contacto 
# Lista de contactos 
# Buscar contacto 
# Editar contacto 
# Cerrar agenda 

class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"

class Agenda:
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self, nombre, telefono, email):
        contacto = Contacto(nombre, telefono, email)
        self.contactos.append(contacto)
        print("Contacto añadido.")

    def lista_contactos(self):
        for contacto in self.contactos:
            print(contacto)

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                print(contacto)
                return
        print("Contacto no encontrado.")

    def editar_contacto(self, nombre, nuevo_telefono=None, nuevo_email=None):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                if nuevo_telefono:
                    contacto.telefono = nuevo_telefono
                if nuevo_email:
                    contacto.email = nuevo_email
                print("Contacto actualizado.")
                return
        print("Contacto no encontrado.")

    def cerrar_agenda(self):
        print("Agenda cerrada.")
        exit()

    def mostrar_menu(self):
        while True:
            print("\n--- Menú ---")
            print("1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                nombre = input("Nombre: ")
                telefono = input("Teléfono: ")
                email = input("Email: ")
                self.añadir_contacto(nombre, telefono, email)
            elif opcion == '2':
                self.lista_contactos()
            elif opcion == '3':
                nombre = input("Nombre del contacto a buscar: ")
                self.buscar_contacto(nombre)
            elif opcion == '4':
                nombre = input("Nombre del contacto a editar: ")
                nuevo_telefono = input("Nuevo teléfono (dejar en blanco para no cambiar): ")
                nuevo_email = input("Nuevo email (dejar en blanco para no cambiar): ")
                self.editar_contacto(nombre, nuevo_telefono or None, nuevo_email or None)
            elif opcion == '5':
                self.cerrar_agenda()
            else:
                print("Opción no válida, intente de nuevo.")

agenda = Agenda()
agenda.mostrar_menu()