"""
Escribir dos funciones que permitan calcular: 

La cantidad de segundos en un tiempo dado en horas, minutos y segundos. 
La cantidad de horas, minutos y segundos de un tiempo dado en segundos. 

Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a segundos, 
convertir a horas, minutos y segundos o salir del programa. """

class programa:
    def __init__(self):
        pass

    # Función que calcula un tiempo dado en horas minutos y segundos a: segundos    
    def segundos(self):
        print("Introduce la cantidad de tiempo en horas, minutos y segundos")
        horas = int(input("Introduce horas: "))
        minutos = int(input("Introduce minutos: "))
        segundos = int(input("Introduce segundos: "))

        print("El tiempo en segundos es: ")
        return horas * 3600 + minutos * 60 + segundos
    
    # Función que calcula un tiempo dado en segundos a: horas, minutos y segundos
    def tiempo(self):
        segundos = int(input("Introduce tiempo en segundos: "))
        horas = segundos // 3600
        segundos = segundos % 3600
        minutos = segundos // 60
        segundos = segundos % 60
        print(f"El tiempo son: {horas} horas, {minutos} minutos y {segundos} segundos")
        return ""
    # Función que muestra un menú con las opciones de conversión
    def menu(self):
        opcion = 0
        while opcion != 3:
            print("1. Convertir a segundos")
            print("2. Convertir a horas, minutos y segundos")
            print("3. Salir")
            opcion = int(input("Introduce una opción: "))
            if opcion == 1:
                print(self.segundos()) #Se invoca segundos en el objeto actual
            elif opcion == 2:
                print(self.tiempo()) #Se invoca tiempo en el objeto actual
            elif opcion == 3:
                print("Fin del programa")
            else:
                print("Opción incorrecta")


programa = programa()
#Cuando se instancia la clase programa, el objeto ahora tiene acceso a los métodos de la clase
programa.menu()
