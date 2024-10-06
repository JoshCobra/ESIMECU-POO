#Menu Actividad 23 Sep

def menu():
    while True:
        print("MENU:")
        print("1. Promedio de Notas de 10 Alumnos")
        print("2. Inicial y Longitud del nombre de una persona")
        print("3. Programa Revisa Que tu Correo Electrónico sea Valido")
        print("4. Promedio de Edades de un Grupo de Alumnos")
        print("5. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            n = 1
            while n == 1:

#------------------------------- PROGRAMA 1 --------------------------------------------

                for i in range(10):
                    nota =  float(input("Introduce la nota del alumno: "))
                i+1

                notas_mayores  = 0
                notas_menores = 0

                if nota >= 7:
                    notas_mayores += 1
                else:
                    notas_menores += 1
                print("Las notas Mayores a 7 son: ", notas_mayores)
                print("Las notas Menores a 7 son: ", notas_menores)

#--------------------------------------------------------------------------------------- 

                n = int(input("Volver a Correr Programa 1?? 1=si/otro=no:"))
            else:
                print("Programa 1 Terminado")
                del n
        elif opcion == "2":
            n = 1
            while n == 1:
                
#------------------------------- PROGRAMA 2 --------------------------------------------

                nombre = input("Introduce el nombre de una persona: ")

                inicial = nombre[0]
                longitud = len(nombre)

                print("La inicial del nombre: ", inicial)
                print("Longitud del nombre: ", longitud)


                if inicial.upper() in 'AEIOU':   
                  print("El nombre inicia con una vocal")

#---------------------------------------------------------------------------------------                  

                n = int(input("Volver a Correr Programa 2?? 1=si/otro=no:"))
            else:
                    print("Programa 2 Terminado")
                    del n
        elif opcion == "3":
            n = 1
            while n == 1:

#------------------------------- PROGRAMA 3 --------------------------------------------

                correo = input("Ingresa un correo electrónico: ")

                if correo.count('@') == 1:
                    print("El correo electrónico es valido")
                else:
                    print("El correo electrónico no es valido")

#--------------------------------------------------------------------------------------- 

                n = int(input("Volver a Correr Programa 3?? 1=si/otro=no:"))
            else:
                    print("Programa 3 Terminado")
                    del n
        elif opcion == "4":
            n = 1
            while n == 1:
                
#------------------------------- PROGRAMA 4 --------------------------------------------

                manana = []
                for i in range(5):
                    edad = int(input("Introduce la edad de un estudiante del la mañana: "))
                    i+1
                    manana.append(edad)

                tarde = []
                for i in range(6):
                    edad = int(input("Introduce la edad de un estudiante del la tarde: "))
                    i+1
                    tarde.append(edad)

                noche = []
                for i in range(11):
                    edad = int(input("Introduce la edad de un estudiante del la noche: "))
                    i+1
                    noche.append(edad)

                promedio_m = sum(manana) / len(manana)
                promedio_t = sum(tarde) / len(tarde)
                promedio_n = sum(noche) / len(noche)

                print("Promedio de edades del turno mañana: ",promedio_m)
                print("Promedio de edades del turno tarde: ",promedio_t)
                print("Promedio de edades del turno noche: ",promedio_n)

                if promedio_m > promedio_t and promedio_m > promedio_n:
                    print("El turno mañana tiene el mayor promedio de edades")
                elif promedio_t > promedio_m and promedio_t > promedio_n:
                    print("El turno tarde tiene el mayor promedio de edades")
                else:
                    print("El turno noche tiene el mayor promedio de edades")

#El .append() es un método de las listas en Python que se utiliza para añadir un 
# elemento al final de la lista cada vez que el usuario ingresa la edad 
# de un estudiante, el método .append() la agrega a la lista correspondiente

#Despues de utiliza la funcion sum() para obtener la suma de todas las edades en
#el arreglo y despues dividirlas entre el total de elementos en la lista
#usando len() para asi obtener el promedio

#referencia: https://docs.python.org/es/3/tutorial/datastructures.html
         

#---------------------------------------------------------------------------------------                  

                n = int(input("Volver a Correr Programa 4?? 1=si/otro=no:"))
            else:
                    print("Programa 4 Terminado")
                    del n
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no valida, intenta de nuevo.")

menu()
