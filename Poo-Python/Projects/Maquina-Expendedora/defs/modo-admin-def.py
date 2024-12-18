def modo_administrador():
    password = str(input("Ingrese contraseña de administrador: "))
    if password == "12345":
        while True:
            print("1. Insertar Bandejas")
            print("2. Insertar Productos")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                break

            elif opcion == "2":
                 break

            elif opcion == "3":
                break
            else:
                print("Opción inválida. Intenta de nuevo")

    else:
        print("Contraseña de administrador incorrecta")

modo_administrador()