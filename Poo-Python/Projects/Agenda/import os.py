import os

#Función para cargar la agenda desde el archivo de texto
def cargar_agenda(primer_agenda):
    agenda=[]
    if os.path.exists(primer_agenda):
        with open(primer_agenda, "r") as archivo:
            for linea in archivo:
        #se realiza la separación por pipes
                contacto = linea.strip().split("|")
                agenda.append(contacto)
    else: 
        with open(primer_agenda, "w") as archivo:
            pass  #Crea el archivo si no existe
        return agenda
            
#Función para guardar la agenda en el archivo de texto
def guardar_agenda(primer_agenda, agenda):
    with open(primer_agenda, "w") as archivo:
        for contacto in agenda:
            archivo.write("|".join(contacto)+"\n")

#Función para mostrar el menu principal 
def mostrar_menu():
    print("\n ---- Agenda de Contactos ----")
    print("1. Añadir contacto")
    print("2. Buscar contacto por nombre")
    print("3. Editar contacto por nombre")
    print("4. Eliminar contacto por nombre")
    print("5. Mostrar todos los contactos ")
    print("6. Salir")

#Función para añadir un contacto
def añadir_contacto(agenda):
    nombre = input("Ingrese su nombre: ")
    teléfono = input("Ingrese teléfono: ")
    correo = input("Ingrese el correo electrónico: ")
    dirección = input("Ingresa la dirección: ")

    agenda.append([nombre,teléfono,correo,dirección])
    print(f"Contacto {nombre} añadido")

#Función para buscar un contacto
def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre a buscar: ")
    for contacto in agenda:
        if contacto[0].lower() == nombre.lower():
            print(f"Contacto encontrado: {contacto}")
            return contacto
    print("Contacto no encontrado")
    return None
    
#Función para editar un contacto
def editar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto a editar: ")
    for contacto in agenda:
        if contacto[0].lower() == nombre.lower():
            print(f"Contacto encontrado: {contacto}")
            campo = input("Que campo desea editar? (nombre, teléfono, correo, dirección): ").lower()
            if campo == "nombre":
                nuevo_valor = input("Ingrese el nuevo nombre: ")
                contacto[0] = nuevo_valor
            elif campo == "teléfono":
                nuevo_valor = input("Ingrese el nuevo teléfono: ")
                contacto[1] = nuevo_valor
            elif campo == "correo":
                nuevo_valor = input("Ingrese nuevo correo electrónico: ")
                contacto[2] = nuevo_valor
            elif campo == "dirección":
                nuevo_valor = input("Ingresa nueva dirección: ")
                contacto[3] = nuevo_valor
            else:
                print("Campo no valido")
                return
            print(f"Contacto actualizado: {contacto}")
            return
    print("Contacto no encontrado")

#Función para eliminar un contacto 
def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    for contacto in agenda:
        if contacto[0].lower() == nombre.lower():
            agenda.remove(contacto)
            print(f"Contacto {nombre} eliminado")
            return
    print("Contacto no encontrado")

#Función para mostrar todos los contactos
def mostrar_contactos(agenda):
    if not agenda:
        print("No hay contactos en la agenda")
    else:
        print("\n Lista de contactos: ")
        for contacto in agenda:
            print(f"Nombre: {contacto[0]}, Teléfono: {contacto[1]}, Correo: {contacto[2]}, Dirección: {contacto[3]}")

#Función principal 
def main():
    primer_agenda = "agenda.txt"
    agenda = cargar_agenda(primer_agenda)

    while True:
        mostrar_menu()
        opción = input("Seleccione una opción: ")
        if opción == "1":
            añadir_contacto(agenda)
        elif opción == "2":
            buscar_contacto(agenda)
        elif opción == "3":
            editar_contacto(agenda)
        elif opción == "4":
            eliminar_contacto(agenda)
        elif opción == "5":
            mostrar_contactos(agenda)
        elif opción == "6":
            guardar_agenda(primer_agenda,agenda)
            print("Saliendo y guardando los contactos en el archivo")
            break
print("Opción no valida. Intente de nuevo")

if __name__ == "__main__":

    main()



    
        
