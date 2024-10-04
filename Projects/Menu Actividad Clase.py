def menu():
    while True:
        print("MENU:")
        print("1. Programa Indica Año Bisiesto o No Bisiesto")
        print("2. Programa Indica Numero Entero en Horas y Minutos")
        print("3. Salir")
        
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            n = 1
            while n == 1:
                anio = int(input("Introduce el Año:" ))
                if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
                    print("Es Bisiesto")
                else:
                    print("No es Bisiesto")
                n = int(input("Ingresar Otro Año? 1=si/otro=no:"))
            else:
                print("Programa 1 Terminado")
        elif opcion == "2":
            s = 1
            while s == 1:

                num = int(input("Introduce el Numero:"))
                horas = num // 60
                minutos = num % 60

                print("Horas:")
                print(horas)
                print("Minutos:")
                print(minutos)

                s = int(input("Ingresar Otro Numero? 1=si/otro=no:"))
            else:
                    print("Programa 2 Terminado")
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida, intenta de nuevo.")

menu()
