def menu():
    while True:
        print("MENU:")
        print("1. Programa Los Teléfonos de una Empresa")
        print("2. Frase Invertida")
        print("3. Programa Precio de Un Producto en Euros")
        print("4. Salir")
        
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            n = 1
            while n == 1:

                tel = input("Introduce un teléfono con el formato +34-numero-extension: ")
                div = tel.split("-")
                num = div[1]
                print("Numero sin Prefijo ni extension: ",num)

                n = int(input("Volver a Correr Programa 1??=si/otro=no:"))
            else:
                print("Programa 1 Terminado")
                del n
        elif opcion == "2":
            n = 1
            while n == 1:

                frase = input("Introduce una frase: ")
                fraseIn = frase[::-1]
                print("Frase Invertida: ",fraseIn)

                n = int(input("Volver a Correr Programa 2?? 1=si/otro=no:"))
            else:
                    print("Programa 2 Terminado")
                    del n
        elif opcion == "3":
            n = 1
            while n == 1:

                precio = input("Ingrese el Precio en Euros incluyendo dos decimales, formato 000.00: ")
                euros, centimos = precio.split(".")
                print(euros,"Euros Con: ",centimos,"Centimos")

                n = int(input("Volver a Correr Programa 3?? 1=si/otro=no:"))
            else:
                    print("Programa 3 Terminado")
                    del n
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no valida, intenta de nuevo.")

menu()
