
def LongitudPila(pila):
    return len(pila)


def EstaVaciaPila(pila):
    return len(pila) == 0

Tamaño_pila = 7
def EstaLlenaPila(pila):
    return len(pila) == Tamaño_pila


def AddPila(pila, elemento):
    if EstaLlenaPila(pila):
        print("Error: la pila está llena y no se puede añadir el elemento")
    else:
        pila.append(elemento)
        print(f"Elemento '{elemento}' añadido a la pila")

def SacarDeLaPila(pila):
    if EstaVaciaPila(pila):
        print("Error: la pila está vacía y no se puede sacar ningún elemento")
    else:
        elemento = pila.pop()
        print(f"Elemento '{elemento}' sacado de la pila")
        return elemento

def EscribirPila(pila):
    if pila:
        print(f"Elementos de la pila: {pila}")
    else:
        print("La pila esta vacía")

def mostrar_menu():
    print("\t ------ Menú ------")
    print("\t1. Añadir elemento a la pila")
    print("\t2. Sacar elemento de la pila")
    print("\t3. Longitud de la pila")
    print("\t4. Mostrar pila")
    print("\t5. Salir")


def main():
    pila = []  
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            elemento = input("Ingrese el elemento a añadir a la pila: ")
            AddPila(pila, elemento)
        elif opcion == "2":
            SacarDeLaPila(pila)
        elif opcion == "3":
            print(f"La pila tiene {LongitudPila(pila)} elementos")
        elif opcion == "4":
            EscribirPila(pila)
        elif opcion == "5":
            print("Saliendo del programa")
            break
        else:
            print("Input No valido, ingrese de nuevo")

if __name__ == "__main__":
    main()
