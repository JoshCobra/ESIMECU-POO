def lista():
    num_palabras = int(input("Cuántas palabras desea ingresar?: "))
    lista_p = []
    for i in range(num_palabras):
        palabra = input("Introduce la palabra: ")
        i+1
        lista_p.append(palabra)
    print("\nLista de palabras creada")
    return lista_p

def imprimir(lista_p):
    print("Lista de palabras:")
    for palabra in lista_p:
        print(palabra)

def contar(lista_p):
    palabra = input("Introduce una palabra para contar cuantas veces aparece: ")
    cantidad = lista_p.count(palabra)
    print("La palabra", palabra, "aparece", cantidad, "veces en la lista")

def sustituir(lista_p):
    palabra_sustituir = input("Introduce la palabra que quieres sustituir: ")
    nueva_palabra = input("Introduce la nueva palabra: ")
    for i in range(len(lista_p)):
        if lista_p[i] == palabra_sustituir:
            lista_p[i] = nueva_palabra
    print("Palabra" , palabra_sustituir, " sustituida por ", nueva_palabra,)

def eliminar(lista_p):
    palabra = input("Introduce la palabra a eliminar: ")
    if palabra in lista_p:
        lista_p.remove(palabra)
        print("La palabra ",palabra," se elimino")
    else:
        print("La palabra ", palabra, " no se encuentra en la lista")

def eliminar_duplicados(lista_p):
    lista_sin_duplicados = list(set(lista_p))
    print("Se eliminaron las palabras duplicadas")
    return lista_sin_duplicados

def menu():
    print("\tDE LA ROSA VAZQUEZ JOSUE\n")
    print("\t----- MENU -----")
    print("\t1. Crear lista de palabras")
    print("\t2. Imprimir lista")
    print("\t3. Contar palabra")
    print("\t4. Sustituir palabra")
    print("\t5. Eliminar palabra")
    print("\t6. Eliminar duplicados")
    print("\t7. Salir")

def programa():
    
    lista_p = []
    while True:
        menu()
        opcion = input("\tElige una opción: ")
        
        if opcion == "1":
            lista_p = lista()
        elif opcion == "2":
            imprimir(lista_p)
        elif opcion == "3":
            contar(lista_p)
        elif opcion == "4":
            sustituir(lista_p)
        elif opcion == "5":
            eliminar(lista_p)
        elif opcion == "6":
            lista_p = eliminar_duplicados(lista_p)
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, elige una opción correcta.")

programa()
