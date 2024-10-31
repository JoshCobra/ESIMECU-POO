"""
Desarrollar un programa con tres clases:
- La primera debe ser Universidad, con atributos nombre (Donde se almacena el nombre de la Universidad). 
- La segunda llamada Carrera, con los atributos especialidad (En donde guarda la especialidad de un estudiante). 
- Y por último, una llamada Estudiante, que tenga como atributos su nombre y edad. 
- El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona. 
- El programa debe ser cíclico en un menu, donde el usuario pueda ingresar los datos de la Universidad, Carrera y Estudiante.
"""

class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre

class Carrera:
    def __init__(self, especialidad):
        self.especialidad = especialidad

class Estudiante:
    def __init__(self, nombre, edad, universidad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.universidad = universidad
        self.carrera = carrera

def main():
    while True:
        print("\nMenu:")
        print("1. Ingresa datos de la Universidad")
        print("2. Ingresar datos de la Carrera")
        print("3. Ingresa datos del Estudiante")
        print("4. Mostrar datos del Estudiante")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            nombre_universidad = input("Ingrese el nombre de la Universidad: ")
            universidad = Universidad(nombre_universidad)
        elif opcion == '2':
            especialidad_carrera = input("Ingrese la especialidad de la Carrera: ")
            carrera = Carrera(especialidad_carrera)
        elif opcion == '3':
            nombre_estudiante = input("Ingrese el nombre del Estudiante: ")
            edad_estudiante = input("Ingrese la edad del Estudiante: ")
            persona = Estudiante(nombre_estudiante, edad_estudiante, universidad, carrera)
        elif opcion == '4':
                print(f"\nUniversidad: {persona.universidad.nombre}")
                print(f"Carrera: {persona.carrera.especialidad}")
                print(f"Nombre: {persona.nombre}")
                print(f"Edad: {persona.edad}")
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

main()